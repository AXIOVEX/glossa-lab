#!/usr/bin/env python3
"""Spec 106 registration audit, version 2 — TC-106-02, TC-106-03,
TC-106-04, TC-106-05.

Version 2 (2026-11-26, Round N unit N-E-2) repairs two coverage
gaps in version 1 (`records/census-audit.py`, preserved
unedited):

1. TC-106-02 requires exactly one kind label per axiom line.
   Version 1's condition admitted one or more (`>= 1`), so a
   line carrying two labels in label position passed. Version 2
   checks the label position exactly: the head of the line, up
   to the first " — " separator, must be exactly `- ID (X)`,
   optionally followed by the UNSOURCED flag word (the filed
   form of three UNSOURCED-sourced lines).
   (A label token occurring later in the line's prose — e.g.
   Indus IND-MOV-11's "retained as (H) because…" — is not a
   second label and does not trip the check.)
2. TC-106-05 registers recomputation and comparison of the
   counts "by domain and by kind". Version 1 compared the
   total, the kind counts, and the UNSOURCED count, but never
   the per-domain counts — so the seed records' false domain
   figures (all zeros, in all three templates) passed.
   Version 2 recomputes the per-domain counts from the axiom
   IDs and compares them against the governing stated census:
   the seed record's statement, superseded for domain counts
   by a dated erratum census line where one is filed in the
   template (see the 2026-11-26 errata in the three baseline
   templates). Where an erratum governs, the seed's original
   figures are reported as superseded, not silently dropped.

Run from the spec package root:
    python3 records/census-audit-v2.py
    python3 records/census-audit-v2.py --self-test

`--self-test` runs the rejection fixtures: scratch copies of
the templates with (a) one erratum domain count altered and
(b) one axiom given two labels in label position must each be
REJECTED, and the unmodified templates must PASS. The
fixtures are built in a temporary directory; no filed file is
touched.

Exits 0 only if every check passes. Prints per-template counts
and every violation found.
"""
import hashlib
import pathlib
import re
import shutil
import sys
import tempfile

ROOT = pathlib.Path(__file__).resolve().parent.parent
AXIOM = re.compile(r"^- ([A-Z]{3})-([A-Z]{3})-(\d+) \(([FKH])\)")
LABEL_HEAD = re.compile(
    r"^- [A-Z]{3}-[A-Z]{3}-\d+ \([FKH]\)( UNSOURCED)?$")
DOM_ORDER = ["GEO", "POL", "MOV", "DNA", "ECO", "ENV", "CON"]
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
SEED_CENSUS = re.compile(
    r"(\d+) axioms in domains 2–8 \(GEO (\d+), POL (\d+), "
    r"MOV (\d+), DNA (\d+), ECO (\d+), ENV (\d+), CON (\d+)\)")
ERRATUM_CENSUS = re.compile(
    r"Erratum census \(machine-readable[^)]*\): GEO (\d+), "
    r"POL (\d+), MOV (\d+), DNA (\d+), ECO (\d+), ENV (\d+), "
    r"CON (\d+)")


def template_paths(root):
    return {
        "indus": root / "templates" / "indus-baseline.md",
        "eteocypriot": root / "templates" / "eteocypriot-baseline.md",
        "meroitic": root / "templates" / "meroitic-baseline.md",
    }


def audit(root):
    """Run every check against the package at `root`.
    Returns (violations, report_lines)."""
    violations = []
    report = []

    def check(cond, msg):
        if not cond:
            violations.append(msg)

    for prog, path in template_paths(root).items():
        text = path.read_text()
        lines = text.splitlines()
        ax = [l for l in lines if AXIOM.match(l)]
        # TC-106-02: exactly one kind label, in label position;
        # source or UNSOURCED; UNSOURCED-sourced lines are (H).
        for l in ax:
            m = AXIOM.match(l)
            head = l.split(" — ")[0]
            check(LABEL_HEAD.match(head) is not None,
                  f"{prog}: line does not carry exactly one kind "
                  f"label in label position: {l[:60]}")
            has_source = "Source:" in l
            has_unsourced = "UNSOURCED" in l
            check(has_source or has_unsourced,
                  f"{prog}: axiom with neither source nor UNSOURCED: "
                  f"{l[:60]}")
            if has_unsourced and not has_source:
                check(m.group(4) == "H",
                      f"{prog}: UNSOURCED-sourced line not (H): "
                      f"{l[:60]}")
        # TC-106-03: shared schema — same domain headers, same
        # order; Domain 1 is a pointer with no axiom lines.
        headers = [l[3:] for l in lines if l.startswith("## Domain ")]
        check(headers == DOMAINS,
              f"{prog}: domain headers differ: {headers}")
        d1 = text.split("## Domain 1 — Language-internal")[1] \
                 .split("## Domain 2")[0]
        check("specs/105-elsewhere-sandbox/" in d1,
              f"{prog}: Domain 1 lacks the Spec 105 pointer")
        check(not any(AXIOM.match(l) for l in d1.splitlines()),
              f"{prog}: Domain 1 carries axiom lines (duplicated floor)")
        # TC-106-05: seed record fields and recomputation,
        # by domain and by kind.
        for field in ["Study identity", "Baseline template",
                      "The full axiom set as seeded",
                      "The claim queue as opened", "The evidence set",
                      "Date and authorizing order"]:
            check(field in text,
                  f"{prog}: seed record missing field: {field}")
        h = hashlib.sha256(("\n".join(ax) + "\n").encode()).hexdigest()
        check(f"`{h}`" in text,
              f"{prog}: seed-record hash does not recompute")
        kinds = {k: sum(1 for l in ax if AXIOM.match(l).group(4) == k)
                 for k in "FKH"}
        stated = re.search(
            r"Axiom census as seeded: (\d+) axioms.*?By kind: \(F\) "
            r"(\d+), \(K\) (\d+), \(H\) (\d+)\. Lines carrying the "
            r"UNSOURCED flag: (\d+)\.", text, re.S)
        check(stated is not None,
              f"{prog}: seed census statement not found")
        if stated:
            total, f_, k_, h_, uns = (int(x) for x in stated.groups())
            check(total == len(ax),
                  f"{prog}: seed total {total} != {len(ax)}")
            check((f_, k_, h_) == (kinds["F"], kinds["K"], kinds["H"]),
                  f"{prog}: seed kind counts {(f_, k_, h_)} != {kinds}")
            uns_actual = sum(1 for l in ax if "UNSOURCED" in l)
            check(uns == uns_actual,
                  f"{prog}: seed UNSOURCED count {uns} != {uns_actual}")
        # TC-106-05, per-domain comparison (new in version 2).
        dom_actual = {d: sum(1 for l in ax
                             if AXIOM.match(l).group(2) == d)
                      for d in DOM_ORDER}
        seed_dom = None
        m_seed = SEED_CENSUS.search(text)
        if m_seed:
            seed_dom = {d: int(v) for d, v in
                        zip(DOM_ORDER, m_seed.groups()[1:])}
        errata = ERRATUM_CENSUS.findall(text)
        if errata:
            governing = {d: int(v) for d, v in
                         zip(DOM_ORDER, errata[-1])}
            report.append(
                f"{prog}: domain census governed by the dated "
                f"erratum census {governing}; the seed record's "
                f"original figures {seed_dom} are superseded "
                f"(see the template's 2026-11-26 erratum)")
        elif seed_dom is not None:
            governing = seed_dom
        else:
            governing = None
            check(False, f"{prog}: no stated domain census found")
        if governing is not None:
            check(governing == dom_actual,
                  f"{prog}: stated domain counts {governing} != "
                  f"recomputed {dom_actual}")
        report.append(
            f"{prog}: {len(ax)} axioms  F={kinds['F']} "
            f"K={kinds['K']} H={kinds['H']}  "
            f"domains={ {d: dom_actual[d] for d in DOM_ORDER} }  "
            f"sha256(ax-lines)={h}")

    # TC-106-04: framework completeness.
    fw = (root / "framework.md").read_text().lower()
    for term in ["baseline template", "axiom", "kind label",
                 "instance", "seed", "claim", "translation",
                 "derivation", "evidence set", "checker", "verdict",
                 "ensemble", "iteration", "retirement", "solution"]:
        check(f"**{term}" in fw,
              f"framework.md: no definition of {term}")
    for elem in ["what may change between iterations",
                 "how variations are chosen",
                 "how verdicts accumulate",
                 "robust-in-ensemble", "axiom-tracking", "underivable",
                 "refuted-in-ensemble", "untested",
                 "seed-and-iteration log", "history ledger",
                 "backfilled", "written as the work happens",
                 "do not retell the story"]:
        check(elem in fw, f"framework.md: missing element: {elem}")
    return violations, report


def self_test():
    """Rejection fixtures. Returns 0 only if the unmodified
    templates PASS and each mutated fixture is REJECTED."""
    failures = []

    def run_fixture(mutate=None):
        with tempfile.TemporaryDirectory() as td:
            root = pathlib.Path(td)
            (root / "templates").mkdir()
            for src in template_paths(ROOT).values():
                shutil.copy(src, root / "templates" / src.name)
            shutil.copy(ROOT / "framework.md", root / "framework.md")
            if mutate:
                mutate(root)
            violations, _ = audit(root)
            return violations

    v = run_fixture()
    print(f"fixture 0 (unmodified templates): "
          f"{'PASS as required' if not v else 'FAIL — ' + str(v)}")
    if v:
        failures.append("unmodified templates rejected")

    def break_domain_count(root):
        p = root / "templates" / "eteocypriot-baseline.md"
        t = p.read_text()
        t2 = t.replace("Erratum census (machine-readable",
                       "Erratum census (machine-readable", 1)
        # alter the governing erratum GEO count by one
        t2 = re.sub(r"(Erratum census \(machine-readable[^)]*\): "
                    r"GEO )(\d+)",
                    lambda m: m.group(1) + str(int(m.group(2)) + 1),
                    t2, count=1)
        assert t2 != t
        p.write_text(t2)

    v = run_fixture(break_domain_count)
    print(f"fixture 1 (erratum domain count altered): "
          f"{'REJECTED as required' if v else 'NOT REJECTED — FAIL'}")
    if not v:
        failures.append("altered domain count not rejected")

    def double_label(root):
        p = root / "templates" / "eteocypriot-baseline.md"
        lines = p.read_text().splitlines()
        for i, l in enumerate(lines):
            m = AXIOM.match(l)
            if m:
                lines[i] = l.replace(f"({m.group(4)}) — ",
                                     f"({m.group(4)}) (F) — ", 1)
                break
        p.write_text("\n".join(lines) + "\n")

    v = run_fixture(double_label)
    print(f"fixture 2 (two kind labels in label position): "
          f"{'REJECTED as required' if v else 'NOT REJECTED — FAIL'}")
    if not v:
        failures.append("double label not rejected")

    if failures:
        print("\nSELF-TEST FAIL:")
        for f in failures:
            print(" -", f)
        return 1
    print("\nSELF-TEST PASS: unmodified templates pass; both "
          "rejection fixtures are rejected.")
    return 0


def main():
    if "--self-test" in sys.argv:
        return self_test()
    violations, report = audit(ROOT)
    for line in report:
        print(line)
    if violations:
        print("\nVIOLATIONS:")
        for v in violations:
            print(" -", v)
        return 1
    print("\nAUDIT PASS (v2): TC-106-02, TC-106-03, TC-106-04, "
          "TC-106-05 all pass, including the per-domain "
          "comparison and the exactly-one-label check.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
