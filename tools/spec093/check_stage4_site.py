#!/usr/bin/env python3
"""Spec 093 Stage 4 — T401 mechanical adjudication.

Gated on the independent audit's AGREE verdict: reads
the audit JSON and the two run records, applies
`stage4-site-freeze-v1.md` §6 clause by clause, and
writes the adjudication JSON. Refuses (exit 1) if the
audit does not read AGREE.

Usage:

    python3 tools/spec093/check_stage4_site.py \
        --store <run-store-dir> --audit <audit-json> --out <adjudication-json>
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--store", required=True, type=Path)
    ap.add_argument("--audit", required=True, type=Path)
    ap.add_argument("--out", required=True, type=Path)
    args = ap.parse_args()

    audit = json.loads(args.audit.read_text(encoding="utf-8"))
    if audit.get("verdict") != "AGREE":
        print("adjudication refused: audit verdict is not AGREE")
        return 1
    admin = controls = None
    for path in sorted(args.store.glob("study-*.json")):
        rec = json.loads(path.read_text(encoding="utf-8"))
        result = rec.get("result") or {}
        if result.get("task") == "T401" and result.get("kind") == "administration":
            admin = result
        if result.get("task") == "T401" and result.get("kind") == "permutation-controls":
            controls = result
    if admin is None or controls is None:
        print("adjudication refused: run records missing")
        return 1

    disc, held = admin["arms"]["discovery"], admin["arms"]["held_out"]
    db = controls["discovery_battery"]
    hb = controls["held_out_battery"]
    ps = controls["pseudo_site_control"]

    def sign(x: float) -> int:
        return (x > 0) - (x < 0)

    q1 = {
        "discovery_statistic": disc["q1_ks"],
        "discovery_p99": db["q1_p99_index1979"],
        "clause1_discovery_above_p99": disc["q1_ks"] > db["q1_p99_index1979"],
        "held_out_statistic": held["q1_ks"],
        "held_out_p95": hb["q1_p95_index1899"],
        "clause2_held_out_above_p95": held["q1_ks"] > hb["q1_p95_index1899"],
        "direction_discovery": sign(disc["mean_length_mohenjo_daro"]
                                    - disc["mean_length_harappa"]),
        "direction_held_out": sign(held["mean_length_mohenjo_daro"]
                                   - held["mean_length_harappa"]),
        "clause3_direction_agrees": sign(disc["mean_length_mohenjo_daro"]
                                         - disc["mean_length_harappa"])
        == sign(held["mean_length_mohenjo_daro"] - held["mean_length_harappa"]),
        "pseudo_site_p95": ps["q1_p95_index189"],
        "clause4_control_behaves": ps["q1_p95_index189"] < db["q1_p99_index1979"],
    }
    q1["verdict"] = (
        "ACCEPTED"
        if all(q1[k] for k in list(q1) if k.startswith("clause"))
        else "NOT YET"
    )
    q2 = {
        "discovery_statistic": disc["q2_tv"],
        "discovery_p99": db["q2_p99_index1979"],
        "clause1_discovery_above_p99": disc["q2_tv"] > db["q2_p99_index1979"],
        "held_out_statistic": held["q2_tv"],
        "held_out_p95": hb["q2_p95_index1899"],
        "clause2_held_out_above_p95": held["q2_tv"] > hb["q2_p95_index1899"],
        "pseudo_site_p95": ps["q2_p95_index189"],
        "clause4_control_behaves": ps["q2_p95_index189"] < db["q2_p99_index1979"],
    }
    q2["verdict"] = (
        "ACCEPTED"
        if all(q2[k] for k in list(q2) if k.startswith("clause"))
        else "NOT YET"
    )
    adjudication = {
        "spec": "093", "stage": "4", "task": "T401",
        "freeze": "stage4-site-freeze-v1.md §6",
        "audit_verdict": "AGREE",
        "q1_length": q1,
        "q2_sign_choice": q2,
        "pass_outcome": (
            "ACCEPTED"
            if q1["verdict"] == "ACCEPTED" and q2["verdict"] == "ACCEPTED"
            else "NOT YET"
        ),
    }
    args.out.write_text(json.dumps(adjudication, indent=2) + "\n",
                        encoding="utf-8")
    print(json.dumps(adjudication, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
