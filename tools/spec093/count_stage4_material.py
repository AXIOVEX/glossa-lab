#!/usr/bin/env python3
"""Spec 093 Stage 4 — T402 material census.

Recomputes the material freeze's §2 counts from the
pinned join output (presence and class counting only —
no sequence property is computed) and reports whether
they reproduce, and how many classes meet the freeze's
floor of 10 (the freeze's §4 administration rule).

Usage: python3 tools/spec093/count_stage4_material.py
Exit 0 iff the frozen counts reproduce exactly.
"""

from __future__ import annotations

import hashlib
import json
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
JOIN_REL = "specs/093-material-context-channel/records/t103-join-pairs-v1.jsonl"
JOIN_SHA256 = (
    "7107f738832a4e3b04cff91d81073212bc0f3a77afed6f0ccc3cee4fce621703"
)
SENTINELS = {"", "None", "-", "--"}
EXPECTED = {"Steatite": 176, "Clay": 1, "Faience": 1}
CLASS_FLOOR = 10


def main() -> int:
    data = (ROOT / JOIN_REL).read_bytes()
    sha = hashlib.sha256(data).hexdigest()
    if sha != JOIN_SHA256:
        print(f"join pin mismatch: computed {sha}")
        return 1
    rows = [json.loads(l) for l in data.decode("utf-8").splitlines() if l.strip()]
    census: Counter = Counter()
    empty = 0
    for r in rows:
        v = r.get("material_raw")
        if v is None or (isinstance(v, str) and v.strip() in SENTINELS):
            empty += 1
        else:
            census[str(v)] += 1
    at_floor = {c: n for c, n in census.items() if n >= CLASS_FLOOR}
    print(f"join pairs: {len(rows)}")
    print(f"material census: {dict(sorted(census.items()))}; empty sentinel: {empty}")
    print(f"classes at or above floor {CLASS_FLOOR}: {at_floor} "
          f"({len(at_floor)} class(es))")
    ok = dict(census) == EXPECTED and empty == 1 and len(rows) == 179
    print("frozen counts reproduce:", ok)
    print("administrable under freeze §4:", len(at_floor) >= 2)
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
