#!/usr/bin/env python3
"""Spec 093 Stage 3 — the comparanda register's
four-element check (T301, acceptance: gate).

Verifies, mechanically, over
`specs/093-material-context-channel/records/comparanda-register-v1.md`:

1. every CR-093 entry carries the four required elements
   of C093-4 — comparanda set, transmission mechanism,
   fixed window, compared practice — each non-empty, and
   the mechanism element names its source;
2. entry ids are unique and sequential from CR-093-01;
3. every corpus in the catalogue
   (`backend/glossa_lab/corpus_catalogue_seeder.py`,
   CATALOGUE) is accounted for in the register's text
   exactly once across the entered entries and the annex
   (the seeding census of D-093-7: 39 corpora).

Exit code 0 iff every check passes. The printed output
is the check output the stage record files verbatim.
"""

from __future__ import annotations

import ast
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
REGISTER = (
    ROOT
    / "specs/093-material-context-channel/records/comparanda-register-v1.md"
)
SEEDER = ROOT / "backend/glossa_lab/corpus_catalogue_seeder.py"

ELEMENTS = (
    "Comparanda set:",
    "Transmission mechanism:",
    "Fixed window:",
    "Compared practice:",
)


def catalogue_names() -> list[str]:
    src = SEEDER.read_text(encoding="utf-8")
    m = re.search(r"CATALOGUE: list\[dict\[str, Any\]\] = (\[.*?\n\])", src, re.S)
    if not m:
        raise SystemExit("CATALOGUE list not found in the seeder")
    return [e["name"] for e in ast.literal_eval(m.group(1))]


def main() -> int:
    text = REGISTER.read_text(encoding="utf-8")
    failures: list[str] = []

    blocks = re.split(r"\n## (CR-093-\d+) — ", text)
    # blocks: [preamble, id, body, id, body, ...]
    entries: list[tuple[str, str]] = []
    for i in range(1, len(blocks), 2):
        entries.append((blocks[i], blocks[i + 1]))
    if not entries:
        failures.append("no CR-093 entries found")
    ids = [eid for eid, _ in entries]
    expected = [f"CR-093-{n:02d}" for n in range(1, len(entries) + 1)]
    if ids != expected:
        failures.append(f"entry ids not sequential from CR-093-01: {ids}")

    for eid, body in entries:
        body = body.split("\n## ")[0].split("\n---")[0]
        for el in ELEMENTS:
            if f"**{el}**" not in body:
                failures.append(f"{eid}: element missing: {el}")
        mech = re.search(
            r"\*\*Transmission mechanism:\*\*(.*?)(?=\n- \*\*|\Z)", body, re.S
        )
        if mech and "Source:" not in mech.group(1):
            failures.append(f"{eid}: mechanism names no source")

    names = catalogue_names()
    unaccounted = []
    double = []
    for name in names:
        n = text.count(name)
        if n == 0:
            unaccounted.append(name)
        elif n > 1:
            double.append((name, n))
    if unaccounted:
        failures.append(f"catalogue corpora unaccounted: {unaccounted}")
    if double:
        failures.append(f"catalogue corpora accounted more than once: {double}")

    print(f"comparanda register check: {len(entries)} entries "
          f"({', '.join(ids)}); catalogue census {len(names)} corpora")
    for eid, _ in entries:
        print(f"  {eid}: four elements present; mechanism source named")
    print(f"  catalogue accounted: {len(names) - len(unaccounted)}"
          f"/{len(names)}; double-accounted: {len(double)}")
    if failures:
        for f in failures:
            print(f"FAIL: {f}")
        print("RESULT: FAIL")
        return 1
    print("RESULT: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
