#!/usr/bin/env python3
"""Spec 100 — deposit extractor (runs only when the gate opens).

Produces the per-seal iconography deposit of record from the
pinned Holdat corpus build: one CSV row per seal,
`cisi_id,iconography`, the iconography string exactly as the
source records it (stripped, lowercased, as the historical
scripts read it), keyed on the same seal ids the tracked
sign files use.

The extractor refuses to run on any build whose SHA-256 is
not the pin of record: the deposit must be produced from the
corpus build the program pinned, verified at deposit
time, or not at all. A refusal writes nothing.

Pin of record (RT6-H3, 2026-11-22): the full 64-character
pin is embedded in this tool as PIN_OF_RECORD. Its source
is the program's records — the T303 build record carried in
`reports/phase422_results.json` — NOT the deposit record,
which is created after extraction and cites the pin.
`--pin`, if supplied, must equal PIN_OF_RECORD or the tool
refuses; with no `--pin` the tool uses PIN_OF_RECORD. A
caller can no longer pin an arbitrary source by passing
that source's own hash.

This tool is part of the registered pipeline. It is NOT run
by the registration package: the deposit is held under flag
F-1 until Miller's reply (Spec 100, claims C100-1/C100-6),
and the pinned build is not held on the execution venue at
registration time (see the adoption record). Its schema and
pin behaviour are exercised by TC-100-06 on synthetic
fixtures only.

Exit codes: 0 = deposit written; 2 = refusal (pin mismatch
or source schema not as frozen). The exit code is the
payload verdict.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import sys
from pathlib import Path

PIN_OF_RECORD = "62d14d2bebf7c2c80d98a2958e75ec52bff3f240ff3f5e85d1f7f40cbe28218e"

def extract(source: Path) -> dict[str, str]:
    """Per-seal iconography from the source CSV.

    The source is row-per-sign-position (the historical
    layout): a seal's iconography is taken from its first
    row, as `phase54_falsification.py` reads it.
    """
    seals: dict[str, str] = {}
    with source.open(encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        fields = reader.fieldnames or []
        if "cisi_number" not in fields or "iconography" not in fields:
            raise ValueError(
                "source lacks the frozen columns cisi_number,iconography: "
                f"found {fields}")
        for row in reader:
            cid = (row.get("cisi_number") or "").strip()
            if not cid or cid in seals:
                continue
            seals[cid] = (row.get("iconography") or "").strip().lower()
    return seals


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--source", type=Path, required=True,
                        help="the Holdat corpus CSV, as held in custody")
    parser.add_argument("--pin", default=None,
                        help="optional; if supplied must equal the embedded PIN_OF_RECORD")
    parser.add_argument("--out", type=Path, required=True,
                        help="deposit CSV to write (cisi_id,iconography)")
    args = parser.parse_args(argv)

    if args.pin is not None and args.pin.strip().lower() != PIN_OF_RECORD:
        print(f"PIN MISMATCH: supplied --pin {args.pin.strip().lower()} is "
              f"not the pin of record {PIN_OF_RECORD}. Refusing: a caller "
              "cannot substitute its own pin. Nothing written.")
        return 2
    digest = hashlib.sha256(args.source.read_bytes()).hexdigest()
    if digest != PIN_OF_RECORD:
        print(f"PIN MISMATCH: source SHA-256 {digest} is not the pin of "
              f"record {PIN_OF_RECORD}. Refusing: the deposit "
              "must be produced from the pinned build or not at all. "
              "Nothing written.")
        return 2
    try:
        seals = extract(args.source)
    except ValueError as exc:
        print(f"SCHEMA REFUSAL: {exc}. Nothing written.")
        return 2
    with args.out.open("w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["cisi_id", "iconography"])
        for cid in sorted(seals):
            writer.writerow([cid, seals[cid]])
    print(f"deposit rows: {len(seals)}")
    print("EXIT_OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
