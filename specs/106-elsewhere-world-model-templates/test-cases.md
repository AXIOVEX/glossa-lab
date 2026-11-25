# Spec 106 — Test Cases

Each test case names the claim it exercises, its procedure, and
its pass condition. TC-106-01..TC-106-05 are Stage 0's
acceptance tests and are recorded in
`records/registration-2026-11-25.md`; TC-106-06 is the landing
audit, recorded in the same record.

**TC-106-01 — Package form (C106-1..C106-6; Stage 0).**
Parse `aee-claims.json`; compare its claim ids and order
against claims.md; check every claim carries a falsifier and a
does-not-establish line.
*Pass:* the JSON parses; the same six claim ids in the same
order in both files; every falsifier and does-not-establish
line present.

**TC-106-02 — Axiom label and source audit (C106-2; Stage 0).**
Run `records/census-audit.py` over the three template files:
every line in axiom form (an ID of the shape `XXX-YYY-NN`
followed by a parenthesised kind label) must carry exactly one
kind label, and either a named source (`Source:`) or the
UNSOURCED flag; every line whose sourcing is the UNSOURCED flag
(no `Source:` present) must be an (H).
*Pass:* zero violations across all three templates, with the
per-template axiom counts and kind counts printed and equal to
the counts stated in spec.md §3 and in each seed record.

**TC-106-03 — Shared schema conformance (C106-3; Stage 0).**
The audit script extracts each template's domain headers.
*Pass:* all three templates carry the same eight domain headers
in the same order (Domain 1 Language-internal through Domain 8
Language contact), and each Domain 1 section is a pointer to
Spec 105 (contains the Spec 105 package path and no axiom
lines).

**TC-106-04 — Framework completeness (C106-1; Stage 0).** The
audit script checks `framework.md` for a definition of each
registered moving part (baseline template, axiom, kind label,
instance, seed, claim, translation, derivation, evidence set,
checker, verdict, ensemble, iteration, retirement, solution),
for the seeding protocol's contents list, for the iteration
protocol's three registered elements (what may change, how
variations are chosen, how verdicts accumulate), for the
solution criterion's three conditions, and for the five lesser
status labels (ROBUST-IN-ENSEMBLE, AXIOM-TRACKING, UNDERIVABLE,
REFUTED-IN-ENSEMBLE, UNTESTED); and for the history-ledger
standard's registered elements (§10: the ledger as a first-class
record opened at registration and written as the work happens,
the entry kinds, the separation rule, the BACKFILLED marking
rule with GAP entries).
*Pass:* every element present.

**TC-106-05 — Seed-record verification (C106-5; Stage 0).** The
audit script recomputes, per template, the axiom count, the
counts by domain and by kind, the UNSOURCED-mention count, and
the SHA-256 over the axiom lines as filed, and compares each
against the values stated in that template's seed record; it
also checks the seed record carries all framework §4 fields.
*Pass:* every stated value recomputes exactly; every §4 field
present in all three seed records.

**TC-106-06 — No-standing-moves audit (C106-6; landing).**
Inspect the landing's full diff against origin/main at the
branch point.
*Pass:* the diff touches only `specs/106-elsewhere-world-model-templates/`,
the claims-ledger intake artifacts for C106-1..C106-6, the
program-map taxonomy, the regenerated matrix and map layers,
the settling records of the registration cascade, and the
census pins in the conformance tests and frontend e2e texts
that the cascade regenerates; no file recording a program
standing, verdict, or tally is altered in content; no instance,
derivation, or claim verdict exists in the package.
