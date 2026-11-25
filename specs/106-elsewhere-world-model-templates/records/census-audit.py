#!/usr/bin/env python3
"""Spec 106 registration audit — TC-106-02, TC-106-03, TC-106-04, TC-106-05.

Run from the spec package root:
    python3 records/census-audit.py
Exits 0 only if every check passes. Prints per-template counts
and every violation found.
"""
import hashlib
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
TEMPLATES = {
    "indus": ROOT / "templates" / "indus-baseline.md",
    "eteocypriot": ROOT / "templates" / "eteocypriot-baseline.md",
    "meroitic": ROOT / "templates" / "meroitic-baseline.md",
}
AXIOM = re.compile(r"^- ([A-Z]{3})-([A-Z]{3})-(\d+) \(([FKH])\)")
DOMAINS = [
    "Domain 1 — Language-internal",
    "Domain 2 — Geography (GEO)",
    "Domain 3 — Politics and administration (POL)",
    "Domain 4 — People movement (MOV)",
    "Domain 5 — DNA and population (DNA)",
    "Domain 6 — Material economy (ECO)",
    "Domain 7 — Environment and chronology (ENV)",
    "Domain 8 — Language contact (CON)",
]
violations = []


def check(cond, msg):
    if not cond:
        violations.append(msg)


seed_hashes = {}
for prog, path in TEMPLATES.items():
    text = path.read_text()
    lines = text.splitlines()
    ax = [l for l in lines if AXIOM.match(l)]
    # TC-106-02: exactly one kind label per line (the regex admits
    # one); source or UNSOURCED; UNSOURCED-sourced lines are (H).
    for l in ax:
        m = AXIOM.match(l)
        check(l.count("(F)") + l.count("(K)") + l.count("(H)") >= 1,
              f"{prog}: line without kind label: {l[:60]}")
        has_source = "Source:" in l
        has_unsourced = "UNSOURCED" in l
        check(has_source or has_unsourced,
              f"{prog}: axiom with neither source nor UNSOURCED: {l[:60]}")
        if has_unsourced and not has_source:
            check(m.group(4) == "H",
                  f"{prog}: UNSOURCED-sourced line not (H): {l[:60]}")
    # TC-106-03: shared schema — same domain headers, same order;
    # Domain 1 is a pointer with no axiom lines.
    headers = [l[3:] for l in lines if l.startswith("## Domain ")]
    check(headers == DOMAINS, f"{prog}: domain headers differ: {headers}")
    d1 = text.split("## Domain 1 — Language-internal")[1].split("## Domain 2")[0]
    check("specs/105-elsewhere-sandbox/" in d1,
          f"{prog}: Domain 1 lacks the Spec 105 pointer")
    check(not any(AXIOM.match(l) for l in d1.splitlines()),
          f"{prog}: Domain 1 carries axiom lines (duplicated floor)")
    # TC-106-05: seed record fields and recomputation.
    for field in ["Study identity", "Baseline template",
                  "The full axiom set as seeded",
                  "The claim queue as opened", "The evidence set",
                  "Date and authorizing order"]:
        check(field in text, f"{prog}: seed record missing field: {field}")
    h = hashlib.sha256(("\n".join(ax) + "\n").encode()).hexdigest()
    seed_hashes[prog] = h
    check(f"`{h}`" in text, f"{prog}: seed-record hash does not recompute")
    kinds = {k: sum(1 for l in ax if AXIOM.match(l).group(4) == k)
             for k in "FKH"}
    stated = re.search(
        r"Axiom census as seeded: (\d+) axioms.*?By kind: \(F\) (\d+), "
        r"\(K\) (\d+), \(H\) (\d+)\. Lines carrying the UNSOURCED "
        r"flag: (\d+)\.", text, re.S)
    check(stated is not None, f"{prog}: seed census statement not found")
    if stated:
        total, f_, k_, h_, uns = (int(x) for x in stated.groups())
        check(total == len(ax), f"{prog}: seed total {total} != {len(ax)}")
        check((f_, k_, h_) == (kinds["F"], kinds["K"], kinds["H"]),
              f"{prog}: seed kind counts {(f_, k_, h_)} != {kinds}")
        uns_actual = sum(1 for l in ax if "UNSOURCED" in l)
        check(uns == uns_actual,
              f"{prog}: seed UNSOURCED count {uns} != {uns_actual}")
    print(f"{prog}: {len(ax)} axioms  F={kinds['F']} K={kinds['K']} "
          f"H={kinds['H']}  sha256(ax-lines)={h}")

# TC-106-04: framework completeness.
fw = (ROOT / "framework.md").read_text().lower()
for term in ["baseline template", "axiom", "kind label", "instance",
             "seed", "claim", "translation", "derivation",
             "evidence set", "checker", "verdict", "ensemble",
             "iteration", "retirement", "solution"]:
    check(f"**{term}" in fw,
          f"framework.md: no definition of {term}")
for elem in ["what may change between iterations",
             "how variations are chosen", "how verdicts accumulate",
             "robust-in-ensemble", "axiom-tracking", "underivable",
             "refuted-in-ensemble", "untested",
             "seed-and-iteration log", "history ledger",
             "backfilled", "written as the work happens",
             "do not retell the story"]:
    check(elem in fw, f"framework.md: missing element: {elem}")

if violations:
    print("\nVIOLATIONS:")
    for v in violations:
        print(" -", v)
    sys.exit(1)
print("\nAUDIT PASS: TC-106-02, TC-106-03, TC-106-04, TC-106-05 all pass.")
