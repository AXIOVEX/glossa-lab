# Spec 101 — Test Cases

Each test case names the claim it exercises, its
procedure, and its pass condition. Test cases for
Stages 1–4 are registered here and executed only when
their stage is commissioned; Stage 0's acceptance test
is T001's (package form) and is recorded in
`records/registration-2026-11-22.md`.

**TC-101-01 — Intake identity (C101-4; Stage 1).**
Build the Perna-side corpus state; recompute its
per-inscription SHA-256 pins from the filed records
and compare against the identity record; hash the
Spec 096 corpus file before and after the intake.
*Pass:* every pin recomputes to the identity record's
value, and the Spec 096 corpus file hashes to
`2954283d…` (version 1.1.1) on both sides of the
intake.

**TC-101-02 — Registration precedence (C101-1;
Stage 2).** Read the candidate registration commit and
the first scoring run's record from the repository's
history; inspect the candidate derivation's inputs.
*Pass:* the registration commit strictly precedes the
first scoring run, and the derivation's inputs are
development-set records only (ICS 196; the ICS 217
control excerpt admissible as control, never as
candidate source).

**TC-101-03 — Scoring reproduction (C101-1; Stage 3).**
Execute the scoring run twice over the intaken state;
recount every candidate's occurrences independently
from the corpus state by a second implementation.
*Pass:* the two runs' outcome records are
byte-identical, and the independent recount agrees on
every candidate's count.

**TC-101-04 — Exposure statement (C101-2; Stage 4).**
Search the outcome record for the exposure statement
of claims.md C101-2 (Perna 2019 read in full on
2026-11-22, before any candidate was registered), and
search the program's records for any description of
this study's result as a blind or held-out prediction.
*Pass:* the statement is present verbatim in the
outcome record, and no blind-prediction description
exists.

**TC-101-05 — Floor arithmetic (C101-1, C101-3;
Stage 2).** Recompute the freeze addendum's
instantiated floors from the intaken census and the
registered candidate set.
*Pass:* every floor in the addendum equals its
recomputation from the census of record, and every
table the scoring run will use appears in the
addendum in full.

## Amendments — 2026-11-22 (Red Team Round 6) — BINDING

The test-case texts above are preserved unchanged.
The binding amendment record is
`records/floor-derivation-and-outcome-registration-2026-11-22.md`
("the floor record").

**TC-101-02 — extended (RT6-M6).** In addition to
the commit-order and input checks above, recompute
every registered candidate's floor from the floor
record's §1.3 formula and the registered inputs
(each candidate's enumerated development occurrences
and f_i, D = 11, K, and the freeze's M).
*Additional pass condition:* every registered floor
**value** equals its recomputation exactly; a floor
that differs from the formula's value fails this
test however regular its commit order is.

**TC-101-04 — target fixed (RT6-L6).** The exposure
statement this test searches for is the canonical
string quoted character-for-character in the floor
record's §5: "that Perna 2019's chapter including its printed reading of ICS 194/195 was read in full on 2026-11-22 (OD-9) before any candidate was registered"
*Pass, as amended:* that exact string is present
verbatim in the outcome record, and no
blind-prediction description exists. A paraphrase of
the exposure does not pass.

**TC-101-05 — conformed (RT6-M6).** The recomputation
this test names is the floor record's §1.3 formula
applied to the T201-registered inputs and the
intaken census's M (segment-final position count),
with the freeze's registered E_i, q_i, and
family-wise Q recomputed alongside the floors.
*Pass, as amended:* every floor, expectation, tail
probability, and Q in the addendum equals its
recomputation, Q is below 0.05, and every table the
scoring run will use appears in the addendum in
full.

**TC-101-06 — TOO THIN closure (C101-1; Stage 2;
RT6-M5, new).** At the freeze, attempt to instantiate
every registered candidate's predicted positions
against the intaken census; include in the procedure
a candidate whose predicted position kind is absent
from the census (a position kind the census carries
no instance of), so the closure path is exercised
and not merely read. *Pass:* on encountering a
candidate whose positions cannot be instantiated,
the study closes TOO THIN at its freeze; no
candidate is scored, on the weakened position set or
any other; the closure record states the
uninstantiable candidate and the census basis for
its uninstantiability; and C101-1 stands NOT TESTED
in every record of the study — reported neither as
SUPPORTED nor as NOT SUPPORTED, and counted in no
verdict tally.
