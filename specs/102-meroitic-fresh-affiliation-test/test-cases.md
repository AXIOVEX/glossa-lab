# Spec 102 — Test Cases

Each test case names the claim it exercises, its
procedure, and its pass condition. Test cases for
Stages 1–5 are registered here and executed only when
their stage is commissioned; Stage 0's acceptance
test is T001's (package form) and is recorded in
`records/registration-2026-11-22.md`.

**TC-102-01 — Gate arithmetic (C102-3; Stage 3).**
From the frozen expanded vocabulary and comparator
lists, recompute the scored concept count per family
test, the count of scored concepts outside the
Stage 4.2 twelve, and the G-2 power simulation by
the registered method of spec §4.
*Pass:* every gate figure in the freeze equals its
recomputation, and Leg A is scored only if both
gates pass on the recomputed figures.

**TC-102-02 — Registration precedence (C102-1,
C102-2; Stage 3).** Read the freeze commit and the
first scoring run's record from the repository's
history; inspect the scoring run's inputs.
*Pass:* the freeze commit strictly precedes the
first scoring run, and every input the run loaded
is named in the freeze.

**TC-102-03 — Scoring reproduction (C102-1, C102-2;
Stage 4).** Execute the scoring run twice over the
frozen lists; recompute T, S, and both permutation
p-values independently from the frozen lists by a
second implementation.
*Pass:* the two runs' outcome records are
byte-identical, and the independent recomputation
agrees on every statistic, including the
Holm-adjusted p-values.

**TC-102-04 — Denominators and labels (C102-4;
Stage 3).** Recompute the freeze's per-concept
denominators (Meroitic forms, comparator forms,
attesting inscription texts) from the frozen sources,
and re-run the label check of every gloss against
ASJP parameters.csv under its pinned hash.
*Pass:* every denominator equals its recomputation
and every label verifies.

**TC-102-05 — Custody sweep (C102-5; Stages 2, 4,
5).** Inspect every input file and published output
of the executed stage against the OD-14 chain.
*Pass:* no Leg A input is unclarified in the chain;
Leg B's record cites a filed clarification or
records NOT ADMINISTERED (custody gate); no
Otten-derived text appears in any published output.

**TC-102-06 — Verdict vocabulary (C102-1, C102-2,
C102-3; Stage 5).** Search the outcome record and
the program's citing records for the study's verdict.
*Pass:* the verdict is stated only in spec §5's
vocabulary; R3 appears only as not displaced; a
NOT ADMINISTERED closure is nowhere cited as
evidence about affiliation.
