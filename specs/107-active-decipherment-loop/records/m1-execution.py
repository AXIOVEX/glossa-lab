#!/usr/bin/env python3
"""Spec 107, test M-1 — Meroitic stratum-conditioned structural
recomputation. Executes the registration filed at
specs/107-active-decipherment-loop/records/cycle-1-registration-2026-11-26.md
section 3, over the pinned Kovetsky build. Read-only against the
build; writes only its raw-output JSON (path from argv[1]) and
progress lines to stdout.

Populations:
  S — every build row whose text is not null, in file order (the
      Spec 105 sandbox population). Pooled figures must reproduce
      the filed Spec 105 figures exactly, or the run STOPS.
  P — distinct texts (dedup by stripped text, first row wins);
      held out iff int(sha256(text)) % 10 == 0. Strata counts must
      reproduce the filed campaign counts exactly, or STOP.
Verdict-bearing facts: a-sign conformance (initial+sole)/total and
i-sign conformance (neither initial nor sole)/total, threshold
0.95, verdict-bearing only in strata with >= 30 occurrences of
the sign (Population S).
"""
import hashlib
import json
import sys
from collections import Counter, defaultdict
from datetime import datetime, timezone

BUILD = "/home/tpierson/.syncyard/worktrees/glossa/kovetsky-src/data/inscriptions.jsonl"
BUILD_SHA256 = "1e91e3a0c52626482bc4015b597df862e7818602dab48a7e870240ab2e567bc4"
STRATA = {
    "funerary": "funerary",
    "royal or temple (stela, wall, cartouche, label)": "royal_temple",
    "document (ostracon, papyrus, wood, vessel)": "document",
    "graffito": "graffito",
}
FLOOR = 30
THRESHOLD = 0.95


def log(msg):
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    print(f"[{ts}] M-1 {msg}", flush=True)


def stratum_of(row):
    return STRATA.get(row.get("kind", "?"), "other")


def positional(groups):
    """groups: list of mark lists. Returns per-mark Counter of
    sole/initial/final/medial, adjacency Counter, adjacency total."""
    pos = defaultdict(Counter)
    adj = Counter()
    adj_total = 0
    for g in groups:
        if len(g) == 1:
            pos[g[0]]["sole"] += 1
            continue
        for i, m in enumerate(g):
            if i == 0:
                pos[m]["initial"] += 1
            elif i == len(g) - 1:
                pos[m]["final"] += 1
            else:
                pos[m]["medial"] += 1
        for a, b in zip(g, g[1:]):
            adj[(a, b)] += 1
            adj_total += 1
    return pos, adj, adj_total


def conformance(pos, mark):
    c = pos.get(mark, Counter())
    total = sum(c.values())
    if mark == "a":
        num = c["initial"] + c["sole"]
    elif mark == "i":
        num = c["final"] + c["medial"]
    else:
        raise ValueError(mark)
    return {"occurrences": total, "numerator": num,
            "rate": (num / total) if total else None}


def table(groups):
    pos, adj, adj_total = positional(groups)
    top = adj.most_common(1)
    return {
        "groups": len(groups),
        "tokens": sum(len(g) for g in groups),
        "adjacencies": adj_total,
        "distinct_pairs": len(adj),
        "top_pair": [list(top[0][0]), top[0][1]] if top else None,
        "positional": {m: dict(c) for m, c in sorted(pos.items())},
        "a_conformance": conformance(pos, "a"),
        "i_conformance": conformance(pos, "i"),
        "never_successor": sorted(m for m in pos
                                  if all(a != m for a, _ in adj)),
        "never_predecessor": sorted(m for m in pos
                                    if all(b != m for _, b in adj)),
    }


def main():
    out_path = sys.argv[1]
    raw = open(BUILD, "rb").read()
    sha = hashlib.sha256(raw).hexdigest()
    assert sha == BUILD_SHA256, f"build pin mismatch: {sha}"
    rows = [json.loads(l) for l in raw.decode("utf-8").splitlines() if l.strip()]
    log(f"build verified ({len(rows)} rows); progress 0/4 steps")

    # ---- Population S
    s_rows = [r for r in rows if r.get("text") is not None]
    s_groups = []
    s_strata_groups = defaultdict(list)
    for r in s_rows:
        groups = [list(w) for w in r["text"].split(" ")]
        s_groups.extend(groups)
        s_strata_groups[stratum_of(r)].extend(groups)
    pooled = table(s_groups)
    log(f"Population S built: {len(s_rows)} artifacts, "
        f"{pooled['tokens']} tokens; progress 1/4 steps")

    # Validation gate 1 — pooled figures reproduce Spec 105's filing.
    checks = {
        "adjacencies == 24648": pooled["adjacencies"] == 24648,
        "distinct_pairs == 448": pooled["distinct_pairs"] == 448,
        "top_pair == (t,e)@1352": pooled["top_pair"] == [["t", "e"], 1352],
        "a occurrences == 737": pooled["a_conformance"]["occurrences"] == 737,
        "a numerator == 725": pooled["a_conformance"]["numerator"] == 725,
        "i occurrences == 2880": pooled["i_conformance"]["occurrences"] == 2880,
        "i numerator == 2857": pooled["i_conformance"]["numerator"] == 2857,
        "digits 0,5,6,8,9 never successor":
            all(d in pooled["never_successor"] for d in "05689"),
        "digit 8 no neighbour": ("8" in pooled["never_successor"]
                                 and "8" in pooled["never_predecessor"]),
    }
    if not all(checks.values()):
        bad = [k for k, v in checks.items() if not v]
        log(f"STOP: Population S validation failed: {bad}")
        json.dump({"stop": "population-S validation failed", "failed": bad,
                   "pooled": pooled}, open(out_path, "w"), indent=1)
        return 3
    log("Population S validation PASS (all filed figures reproduce); "
        "progress 2/4 steps")

    s_strata = {s: table(g) for s, g in sorted(s_strata_groups.items())}

    # ---- Population P
    seen = {}
    for r in rows:
        t = (r.get("text") or "").strip()
        if t and t not in seen:
            seen[t] = r
    dev, held = [], []
    for t, r in seen.items():
        h = int(hashlib.sha256(t.encode("utf-8")).hexdigest(), 16) % 10
        (held if h == 0 else dev).append((t, r))
    counts = {
        "development": Counter(stratum_of(r) for _, r in dev),
        "held_out": Counter(stratum_of(r) for _, r in held),
    }
    expected = {
        "development": {"funerary": 223, "royal_temple": 41, "document": 42,
                        "graffito": 22, "other": 7},
        "held_out": {"funerary": 16, "royal_temple": 10, "document": 5,
                     "graffito": 2, "other": 0},
    }
    p_ok = all(counts[arm].get(k, 0) == v
               for arm in expected for k, v in expected[arm].items())
    p_ok = p_ok and len(dev) == 335 and len(held) == 33
    if not p_ok:
        log(f"STOP: Population P validation failed: "
            f"{ {a: dict(c) for a, c in counts.items()} }")
        json.dump({"stop": "population-P validation failed",
                   "counts": {a: dict(c) for a, c in counts.items()}},
                  open(out_path, "w"), indent=1)
        return 3
    log("Population P validation PASS (335 development / 33 held out, "
        "strata counts exact); progress 3/4 steps")

    p_tables = {}
    for arm_name, arm in (("development", dev), ("held_out", held)):
        by_stratum = defaultdict(list)
        for t, r in arm:
            by_stratum[stratum_of(r)].extend([list(w) for w in t.split(" ")])
        p_tables[arm_name] = {s: table(g) for s, g in sorted(by_stratum.items())}

    # Out-of-stratum prediction: funerary rates predict royal_temple
    # (Population P, development arm).
    oos = {}
    for sign in ("a_conformance", "i_conformance"):
        f = p_tables["development"]["funerary"][sign]
        rt = p_tables["development"]["royal_temple"][sign]
        oos[sign] = {"funerary_rate": f["rate"],
                     "royal_temple_rate": rt["rate"],
                     "difference": (None if f["rate"] is None or rt["rate"] is None
                                    else abs(f["rate"] - rt["rate"]))}

    # ---- Verdict (Population S strata; registered rule)
    def fact_verdict(sign_key):
        pooled_rate = pooled[sign_key]["rate"]
        pooled_holds = pooled_rate is not None and pooled_rate >= THRESHOLD
        fun = s_strata["funerary"][sign_key]
        fun_holds = (fun["occurrences"] >= FLOOR and fun["rate"] is not None
                     and fun["rate"] >= THRESHOLD)
        others = {s: t[sign_key] for s, t in s_strata.items()
                  if s != "funerary" and t[sign_key]["occurrences"] >= FLOOR}
        if not pooled_holds:
            return "pooled-fact-absent", others
        if not fun_holds:
            return "genre-artifact (fails in funerary)", others
        if not others:
            return "indeterminate (no second adequate-floor stratum)", others
        if all(o["rate"] >= THRESHOLD for o in others.values()):
            return "holds (stratum-stable)", others
        if all(o["rate"] < THRESHOLD for o in others.values()):
            return "genre-artifact (funerary-only)", others
        return "mixed across adequate-floor strata", others

    verdicts = {}
    for sign_key in ("a_conformance", "i_conformance"):
        v, others = fact_verdict(sign_key)
        verdicts[sign_key] = {"verdict": v,
                              "adequate_floor_other_strata":
                                  {s: o for s, o in others.items()}}
    labels = [v["verdict"] for v in verdicts.values()]
    if any(l.startswith("genre-artifact") for l in labels):
        headline = "NEGATIVE"
    elif all(l.startswith("holds") for l in labels):
        headline = "POSITIVE"
    elif any(l.startswith("holds") for l in labels):
        headline = "POSITIVE (with an indeterminate fact named)"
    else:
        headline = "INDETERMINATE"
    log(f"verdict: {headline} — a: {labels[0]}; i: {labels[1]}; "
        f"progress 4/4 steps")

    out = {
        "test": "M-1 (Spec 107 cycle 1)",
        "build": {"path": BUILD, "sha256": sha},
        "population_S": {"artifacts": len(s_rows), "pooled": pooled,
                         "validation": checks, "strata": s_strata},
        "population_P": {"counts": {a: dict(c) for a, c in counts.items()},
                         "validation_pass": p_ok, "tables": p_tables},
        "out_of_stratum_prediction_development": oos,
        "verdicts": verdicts,
        "headline_verdict": headline,
    }
    json.dump(out, open(out_path, "w"), indent=1, ensure_ascii=False)
    log(f"raw output written to {out_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
