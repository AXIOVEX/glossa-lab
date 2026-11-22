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
