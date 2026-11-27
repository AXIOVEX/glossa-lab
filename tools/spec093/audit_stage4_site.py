#!/usr/bin/env python3
"""Spec 093 Stage 4 — T401 independent audit.

An independent implementation that does not import the
runner: it recomputes both executions (administration
and controls) from the pinned inputs under
`stage4-site-freeze-v1.md` by different arithmetic
routes (KS by merged-walk over sorted lists with bisect
counts; TV by the integer form
sum|a_i*B - b_i*A| / (2AB)) and compares every value in
the runs' result blocks exactly. Verdict AGREE iff
every compared value matches, the header pins verify
against the files in the tree, and the store carries no
unexpected Stage 4 runs.

Usage:

    python3 tools/spec093/audit_stage4_site.py \
        --store <run-store-dir> --out <audit-json-path>
"""

from __future__ import annotations

import argparse
import bisect
import hashlib
import json
import random
import sys
from collections import Counter
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SPEC_DIR = "specs/093-material-context-channel"
SNAPSHOT_REL = "glossa-corpus/indus/exports/indus_research.jsonl"
SNAPSHOT_SHA256 = (
    "08fc96c8dbc22a37effb65e789b22b144f4baf22be1da55dc3d84db5dc44505e"
)
FREEZE_REL = f"{SPEC_DIR}/records/stage4-site-freeze-v1.md"
SENTINELS = {"", "None", "-", "--"}


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def empty(v) -> bool:
    if v is None:
        return True
    if isinstance(v, (list, dict)):
        return len(v) == 0
    return isinstance(v, str) and v.strip() in SENTINELS


def load_items():
    items = []
    with (ROOT / SNAPSHOT_REL).open(encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if not line:
                continue
            rec = json.loads(line)
            if rec.get("canonical_grapheme_ids") and not empty(rec.get("site_name")):
                items.append({
                    "id": rec["glossa_id"],
                    "seq": [str(c) for c in rec["canonical_grapheme_ids"]],
                    "site": str(rec["site_name"]),
                })
    return items


def split_arms(items):
    adjudged = [it for it in items
                if Counter(x["site"] for x in items)[it["site"]] >= 50]
    rng = random.Random(20261127)
    arms = {"discovery": [], "held_out": []}
    for label in sorted({it["site"] for it in adjudged}):
        group = sorted((it for it in adjudged if it["site"] == label),
                       key=lambda it: it["id"])
        ids = [it["id"] for it in group]
        rng.shuffle(ids)
        cut = (7 * len(ids)) // 10
        keep = set(ids[:cut])
        for it in group:
            arms["discovery" if it["id"] in keep else "held_out"].append(it)
    return arms


def ks_walk(a: list[int], b: list[int]) -> Fraction:
    sa, sb = sorted(a), sorted(b)
    best = Fraction(0)
    for v in sorted(set(sa) | set(sb)):
        fa = Fraction(bisect.bisect_right(sa, v), len(sa))
        fb = Fraction(bisect.bisect_right(sb, v), len(sb))
        if abs(fa - fb) > best:
            best = abs(fa - fb)
    return best


def tv_integer(a_seqs, b_seqs) -> Fraction:
    ca: Counter = Counter()
    cb: Counter = Counter()
    for s in a_seqs:
        for g in s:
            ca[g] += 1
    for s in b_seqs:
        for g in s:
            cb[g] += 1
    ta, tb = sum(ca.values()), sum(cb.values())
    num = sum(abs(ca.get(g, 0) * tb - cb.get(g, 0) * ta)
              for g in set(ca) | set(cb))
    return Fraction(num, 2 * ta * tb)


def arm_stats(arm):
    md = [it for it in arm if it["site"] == "Mohenjo-daro"]
    ha = [it for it in arm if it["site"] == "Harappa"]
    mdl = [len(it["seq"]) for it in md]
    hal = [len(it["seq"]) for it in ha]
    return {
        "n_mohenjo_daro": len(md),
        "n_harappa": len(ha),
        "q1_ks": float(ks_walk(mdl, hal)),
        "q2_tv": float(tv_integer([it["seq"] for it in md],
                                  [it["seq"] for it in ha])),
        "mean_length_mohenjo_daro": float(Fraction(sum(mdl), len(mdl))),
        "mean_length_harappa": float(Fraction(sum(hal), len(hal))),
    }


def battery(arm, seed):
    ids = sorted(it["id"] for it in arm)
    by_id = {it["id"]: it for it in arm}
    labels = [by_id[i]["site"] for i in ids]
    rng = random.Random(seed)
    q1, q2 = [], []
    for _ in range(2000):
        perm = list(labels)
        rng.shuffle(perm)
        md = [by_id[i] for i, lab in zip(ids, perm) if lab == "Mohenjo-daro"]
        ha = [by_id[i] for i, lab in zip(ids, perm) if lab == "Harappa"]
        q1.append(ks_walk([len(it["seq"]) for it in md],
                          [len(it["seq"]) for it in ha]))
        q2.append(tv_integer([it["seq"] for it in md],
                             [it["seq"] for it in ha]))
    q1s, q2s = sorted(q1), sorted(q2)
    return {
        "n_permutations": 2000,
        "q1_values": [float(v) for v in q1s],
        "q2_values": [float(v) for v in q2s],
        "q1_p99_index1979": float(q1s[1979]),
        "q1_p95_index1899": float(q1s[1899]),
        "q2_p99_index1979": float(q2s[1979]),
        "q2_p95_index1899": float(q2s[1899]),
    }


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--store", required=True, type=Path)
    ap.add_argument("--out", required=True, type=Path)
    args = ap.parse_args()

    runs = []
    for path in sorted(args.store.glob("study-*.json")):
        rec = json.loads(path.read_text(encoding="utf-8"))
        runs.append((path.name, rec))
    mine = [(n, r) for n, r in runs
            if r.get("run", {}).get("tool") == "run_stage4_site.py"]
    problems = []
    if len(mine) != 2:
        problems.append(f"expected 2 stage-4 runs, found {len(mine)}")
    by_kind = {}
    for name, rec in mine:
        result = rec.get("result") or {}
        by_kind[result.get("kind")] = (name, rec)
        pins = rec.get("run", {}).get("key", {}).get("input_pins", {})
        if pins.get("snapshot", {}).get("sha256") != SNAPSHOT_SHA256:
            problems.append(f"{name}: snapshot pin in header wrong")
        if pins.get("freeze_record_sha256") != sha256_file(ROOT / FREEZE_REL):
            problems.append(f"{name}: freeze pin in header wrong")

    items = load_items()
    arms = split_arms(items)
    expected_admin = {
        "spec": "093", "stage": "4", "task": "T401",
        "kind": "administration",
        "population": 966,
        "adjudged_classes": {"Harappa": 110, "Mohenjo-daro": 839},
        "excluded_classes": {"Chanhu-Daro": 7, "Kalibangan": 1,
                             "Lothal": 3, "Sutkagen-Dor": 6},
        "adjudged_total": 949,
        "arms": {k: arm_stats(arms[k]) for k in ("discovery", "held_out")},
    }
    disc = battery(arms["discovery"], 20261128)
    held = battery(arms["held_out"], 20261129)
    md_disc = sorted((it for it in arms["discovery"]
                      if it["site"] == "Mohenjo-daro"), key=lambda it: it["id"])
    rng = random.Random(20261130)
    pq1, pq2 = [], []
    for _ in range(200):
        pool = list(md_disc)
        rng.shuffle(pool)
        pha, pmd = pool[:77], pool[77:]
        pq1.append(ks_walk([len(it["seq"]) for it in pmd],
                           [len(it["seq"]) for it in pha]))
        pq2.append(tv_integer([it["seq"] for it in pmd],
                              [it["seq"] for it in pha]))
    pq1s, pq2s = sorted(pq1), sorted(pq2)
    expected_controls = {
        "spec": "093", "stage": "4", "task": "T401",
        "kind": "permutation-controls",
        "adjudged_classes": {"Harappa": 110, "Mohenjo-daro": 839},
        "discovery_battery": disc,
        "held_out_battery": held,
        "pseudo_site_control": {
            "n_draws": 200,
            "pseudo_harappa_size": 77,
            "q1_values": [float(v) for v in pq1s],
            "q2_values": [float(v) for v in pq2s],
            "q1_p95_index189": float(pq1s[189]),
            "q2_p95_index189": float(pq2s[189]),
        },
    }

    compared = {"administration": 0, "permutation-controls": 0}
    for kind, expected in (("administration", expected_admin),
                           ("permutation-controls", expected_controls)):
        if kind not in by_kind:
            problems.append(f"missing run of kind {kind}")
            continue
        name, rec = by_kind[kind]
        got = rec.get("result")
        if got != expected:
            problems.append(f"{name}: result block differs from recomputation")
            # name the first differing key for the record
            for k in expected:
                if got.get(k) != expected[k]:
                    problems.append(f"  first differing key: {k}")
                    break
        else:
            compared[kind] = 1

    verdict = "AGREE" if not problems else "DIVERGE"
    audit = {
        "spec": "093", "stage": "4", "task": "T401",
        "auditor": "audit_stage4_site.py (independent implementation)",
        "runs_compared": {k: (by_kind[k][0] if k in by_kind else None)
                          for k in compared},
        "blocks_matching": compared,
        "problems": problems,
        "verdict": verdict,
    }
    args.out.write_text(json.dumps(audit, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(audit, indent=2))
    return 0 if verdict == "AGREE" else 1


if __name__ == "__main__":
    raise SystemExit(main())
