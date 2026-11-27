#!/usr/bin/env python3
"""Spec 093 Stage 4 — T403 contact-context administration.

Adjudges the frozen expectations E1–E4 of
`stage4-contact-freeze-v1.md` mechanically from the rows
of the two rebuilt contact-zone files (field and period
counting over the named evidence class only), compares
the E4 recomputation against the file's own filed
aggregates, and writes the machine output the outcome
record files. No statistic over any population is
computed.

Usage: python3 tools/spec093/run_stage4_contact.py --out <json>
"""

from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / "glossa-corpus/indus/sources/contact-zone-rebuilt-2026-10-25"
UNPROVENANCED = ("unprovenanced", "no excavation context", "collection piece")
OUTSIDE_SPOTS = (
    "Ur", "Tell Asmar", "Kish", "Susa", "Failaka", "Bahrain",
    "Janabiyah", "Al-Maqsha", "Konar Sandal", "Jalalabad",
)
IN_WINDOW = {
    "ED IIIb (ca. 2500-2340 BC)", "ED IIIb (ca. 2500-2340 BC) ?",
    "Old Akkadian (ca. 2340-2200 BC)", "Lagash II (ca. 2200-2100 BC)",
    "Ur III (ca. 2100-2000 BC)", "Early Old Babylonian (ca. 2000-1900 BC)",
    "Old Babylonian (ca. 1900-1600 BC)",
}


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--out", required=True, type=Path)
    args = ap.parse_args()

    seals_doc = json.loads((BASE / "seals_at_mesopotamia.json")
                           .read_text(encoding="utf-8"))
    seals = seals_doc["seals"]
    mel_doc = json.loads((BASE / "meluhha_tablets.json")
                         .read_text(encoding="utf-8"))
    tablets = mel_doc["tablets"]

    n_period = sum(1 for s in seals if str(s.get("find_period") or "").strip())
    n_spot = sum(
        1 for s in seals
        if str(s.get("find_spot") or "").strip()
        and not any(u in str(s["find_spot"]) for u in UNPROVENANCED)
    )
    n_outside = sum(
        1 for s in seals
        if any(o in str(s.get("find_spot") or "") for o in OUTSIDE_SPOTS)
    )
    n_inscribed = sum(
        1 for s in seals
        if (s.get("inscription_length") or 0) >= 2
        and s.get("signs_confidence") != "none"
    )
    periods = Counter(str(t.get("period")) for t in tablets)
    modal_period, modal_n = periods.most_common(1)[0]
    in_window = sum(n for p, n in periods.items() if p in IN_WINDOW)
    filed = {k: v for k, v in (mel_doc.get("hits_by_period") or {}).items()}
    recomputed = {k: v for k, v in periods.items()}
    aggregates_agree = (
        {k: v for k, v in filed.items()} == recomputed
        if filed else None
    )

    out = {
        "spec": "093", "stage": "4", "task": "T403",
        "freeze": "stage4-contact-freeze-v1.md §3",
        "seals_total": len(seals),
        "e1": {"with_find_period": n_period, "with_excavation_spot": n_spot,
               "verdict": "MET" if n_period == 14 and n_spot >= 12 else "NOT MET"},
        "e2": {"outside_indus_region": n_outside,
               "verdict": "MET" if n_outside >= 10 else "NOT MET"},
        "e3": {"inscription_bearing": n_inscribed,
               "verdict": "MET" if n_inscribed >= 10 else "NOT MET"},
        "meluhha_total": len(tablets),
        "e4": {"modal_period": modal_period, "modal_count": modal_n,
               "in_window_hits": in_window,
               "filed_aggregates_agree": aggregates_agree,
               "verdict": "MET" if modal_period.startswith("Ur III")
               and in_window >= 1000 else "NOT MET"},
        "period_census": dict(sorted(periods.items())),
    }
    args.out.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(out, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
