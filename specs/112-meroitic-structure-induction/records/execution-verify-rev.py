#!/usr/bin/env python3
"""Spec 112 REVISION - independent recomputation (TC-112-11).

Recomputes the revision preflight's headline figures from the filed
outputs (records/preflight-rev-output.json) and the pinned corpus,
with implementations written independently of
records/execution-harness-rev.py (no shared code but the corpus
pins). Rational figures must agree exactly; entropies to 1e-9 with
the same argmax. Payload verdict = exit code (0 iff all checks
agree).
"""

import hashlib
import json
import math
import re
import sys
from fractions import Fraction

KOVETSKY_DIR = "/home/tpierson/.syncyard/worktrees/glossa/kovetsky-src"
INSCRIPTIONS_SHA256 = ("1e91e3a0c52626482bc4015b597df862e7818602dab48a7e8702"
                       "40ab2e567bc4")
GOLD_MORPH_SHA256 = ("c5dc8f3479e81a270a3ee68a9f602c125dcc1211c5fa8b1f8091"
                     "e56b4bf8a5b8")
OTTEN_FILE = ("/home/tpierson/.syncyard/worktrees/glossa/glossa-custody/"
              "spec097/otten-corpus/Data/mero-corpus.txt")
MERO_SHA256 = ("b7f3350c2f2118a8223854462a8e881c424cba6b26c01ebfb676efa92e"
               "a253ce")
TEMPLATE_ORDER = ["invocation", "presentation", "filiation1",
                  "filiation2", "offering", "closing"]

checks = []


def check(name, ok, detail=""):
    checks.append({"check": name, "agree": bool(ok), "detail": detail})


def sha256_file(path):
    with open(path, "rb") as fh:
        return hashlib.sha256(fh.read()).hexdigest()


def held_out(key):
    return int(hashlib.sha256(key.encode()).hexdigest(), 16) % 10 == 0


def tokenize(text):
    return [t for t in re.split(r"[\s.]+", text) if t and t.isalpha()]


def funerary_texts():
    path = KOVETSKY_DIR + "/data/inscriptions.jsonl"
    assert sha256_file(path) == INSCRIPTIONS_SHA256
    texts = {}
    for line in open(path):
        r = json.loads(line)
        t = r.get("text")
        if t and t not in texts:
            texts[t] = r["kind"]
    out = []
    for t, kind in sorted(texts.items()):
        if kind == "funerary" and not held_out(t):
            toks = tokenize(t)
            if len(toks) >= 4:
                out.append(toks)
    return out


def label_text(toks):
    def find(pred, lo=0):
        for i in range(lo, len(toks)):
            if pred(toks[i]):
                return i
        return None

    wos = find(lambda t: t == "woSi")
    sor = find(lambda t: t in ("Soreyi", "aSoreyi"))
    if wos is None or sor is None or wos > 3 or sor > 4 or wos > sor:
        return None
    fil1 = find(lambda t: "tedxe" in t or "tdxe" in t, sor + 1)
    fil2 = find(lambda t: "terike" in t or "yerike" in t, sor + 1)
    if fil1 is None and fil2 is None:
        return None
    off = find(lambda t: t == "ato" or (t.startswith("ato")
                                        and len(t) <= 7), sor + 1)
    present = {"invocation"}
    anchors = [i for i in (fil1, fil2, off) if i is not None]
    if min(anchors) > sor + 1:
        present.add("presentation")
    if fil1 is not None:
        present.add("filiation1")
    if fil2 is not None:
        present.add("filiation2")
    if off is not None:
        present.add("offering")
    if max(anchors) < len(toks) - 1:
        present.add("closing")
    return present


def f1(pred, gold):
    p, g = set(pred), set(gold)
    tp = len(p & g)
    if not p and not g:
        return Fraction(1)
    if not p or not g:
        return Fraction(0)
    return Fraction(2 * tp, 2 * tp + len(p - g) + len(g - p))


def main():
    import os
    here = os.path.dirname(os.path.abspath(__file__))
    gt = json.load(open(os.path.join(here, "ground-truth-sets.json")))
    gt = gt["ground_truth"]
    pf = json.load(open(os.path.join(here, "preflight-rev-output.json")))

    # ---- P-1
    p1 = pf["P-1"]
    f1s = []
    ok = True
    for key, rec in gt.items():
        pred = p1["per_form_pred_boundaries"][key]
        v = f1(pred, rec["boundaries"])
        f1s.append(v)
        if str(v) != p1["per_form_f1"][key]:
            ok = False
    check("P-1 per-form F1 values", ok)
    vals = sorted(f1s)
    m = len(vals)
    median = vals[m // 2] if m % 2 else (vals[m // 2 - 1] + vals[m // 2]) / 2
    check("P-1 median F1", str(median) == p1["median_f1"],
          f"recomputed {median} vs filed {p1['median_f1']}")
    check("P-1 pass flag", p1["pass"] == (median >= Fraction(4, 5)))
    check("P-1 form count", p1["n_forms"] == len(gt) == 1719)

    # ---- P-2
    p2 = pf["P-2"]
    texts = funerary_texts()
    labeled = []
    for toks in texts:
        lab = label_text(toks)
        if lab is not None:
            labeled.append((toks, lab))
    check("P-2 labeled count", len(labeled) == p2["labeled_texts"] == 95,
          f"recomputed {len(labeled)}")
    filed = {e["text_sha256"]: e for e in p2["per_text"]}
    matches = 0
    ok = True
    for toks, present in labeled:
        h = hashlib.sha256(" ".join(toks).encode()).hexdigest()
        e = filed.get(h)
        if e is None or sorted(present) != e["label_present"]:
            ok = False
            continue
        want = [s for s in TEMPLATE_ORDER if s in present]
        if e["induced_sequence"] == want:
            matches += 1
    check("P-2 per-text labels", ok)
    rate = Fraction(matches, len(labeled))
    check("P-2 match rate", str(rate) == p2["match_rate"]
          and matches == p2["sequence_matches"],
          f"recomputed {matches}/{len(labeled)} = {rate}")
    ent = {}
    for s, counts in p2["slot_type_counts"].items():
        tot = sum(counts.values())
        if tot:
            ent[s] = -sum((c / tot) * math.log2(c / tot)
                          for c in counts.values())
    ok = all(abs(ent[s] - p2["slot_entropy"][s]) <= 1e-9 for s in ent) \
        and set(ent) == set(p2["slot_entropy"])
    check("P-2 slot entropies", ok)
    name_max = bool(ent) and max(ent, key=lambda s: ent[s]) == "presentation"
    check("P-2 name-slot argmax", name_max == p2["name_slot_is_max_entropy"])
    check("P-2 pass flag",
          p2["pass"] == (rate >= Fraction(9, 10) and name_max))
    y = sum(1 for v in p2["yield_by_slot"].values() if v)
    check("P-2 yield recount", y == p2["yield"])
    sy = sum(1 for v in p2["shuffle_yield_by_slot"].values() if v)
    check("P-2 shuffle yield recount", sy == p2["shuffle_yield"])

    # ---- P-3
    p3 = pf["P-3"]
    gm_path = KOVETSKY_DIR + "/data/gold_morphology.json"
    assert sha256_file(gm_path) == GOLD_MORPH_SHA256
    assert sha256_file(OTTEN_FILE) == MERO_SHA256
    ott_forms = set()
    for line in open(OTTEN_FILE):
        line = line.rstrip("\n")
        if not line or held_out(line):
            continue
        ott_forms.update(tokenize(line))
    gold = set()
    for e in json.load(open(gm_path)):
        if e["form"].startswith("-") and e.get("corpus_form"):
            strs = [e["corpus_form"]] + list(e.get("corpus_variants") or [])
            for s in strs:
                if s in ott_forms:
                    gold.add(s)
                    gold.add(s.replace("E", "o"))
    check("P-3 gold union", gold == set(p3["gold_suffix_string_set"]),
          f"recomputed {len(gold)} strings")
    props = set(p3["proposal_set"])
    check("P-3 proposal counts consistent",
          len(props) == len(p3["proposals"])
          and all(p3["proposals"][s] == p3["real_final_segment_supports"][s]
                  for s in props)
          and all(v >= p3["tau_st"] for v in p3["proposals"].values()))
    tau_re = max(p3["null_final_segment_supports"].values())
    check("P-3 tau is the null maximum", tau_re == p3["tau_st"],
          f"recomputed {tau_re}")
    precision = Fraction(len(props & gold), len(props)) if props \
        else Fraction(0)
    check("P-3 precision", str(precision) == p3["precision"]
          and len(props & gold) == p3["proposal_hits"],
          f"recomputed {precision}")
    pr = Fraction(p3["shuffle_proposal_count"], len(props)) if props \
        else None
    check("P-3 shuffle proposal ratio",
          (str(pr) if pr is not None else None)
          == p3["shuffle_proposal_ratio"])
    sr = Fraction(p3["slot_yield_shuffle"], p3["slot_yield_real"]) \
        if p3["slot_yield_real"] else None
    check("P-3 slot yield ratio",
          (str(sr) if sr is not None else None) == p3["slot_yield_ratio"])
    check("P-3 pass flag",
          p3["pass"] == (precision >= Fraction(4, 5)
                         and pr is not None and pr <= Fraction(1, 5)
                         and sr is not None and sr <= Fraction(1, 5)))
    check("pass_in_full consistency",
          pf["pass_in_full"] == bool(p1["pass"] and p2["pass"]
                                     and p3["pass"]))

    out = {"checks": checks,
           "agree": sum(1 for c in checks if c["agree"]),
           "total": len(checks)}
    with open(os.path.join(here, "verify-rev-output.json"), "w") as fh:
        json.dump(out, fh, indent=1, sort_keys=True)
        fh.write("\n")
    for c in checks:
        print(("AGREE " if c["agree"] else "DISAGREE ") + c["check"]
              + ((" — " + c["detail"]) if c["detail"] else ""))
    print(f"TC-112-11: {out['agree']}/{out['total']} checks agree")
    sys.exit(0 if out["agree"] == out["total"] else 1)


if __name__ == "__main__":
    main()
