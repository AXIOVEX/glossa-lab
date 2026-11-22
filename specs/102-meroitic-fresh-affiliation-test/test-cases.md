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

**TC-102-07 — Split construction recomputation
(C102-1, C102-2; Stages 2–3; added by amendment
2026-11-22, RT6-H6).** Recompute the §3.6 split
assignment, as amended, for the fixed example texts
below under the fixed example salt
`spec102-split-example-salt-2026-11-22` (UTF-8 bytes;
this example salt is a test fixture, not the study
salt, which the freeze registers): digest =
SHA-256(salt bytes || 0x00 || UTF-8(text)); value =
the digest as a big-endian integer; assignment =
value mod 10; residue 0 is the development side
(the derivation side), residues 1–9 the held-out
side.

| Text | SHA-256 digest | Residue | Side |
|---|---|---|---|
| `ato` | `1f3924e248a2b980d52b2377dcb6a526e7d2953b04513ccfc2edf0ff15c74e2d` | 7 | held-out side |
| `mk lb` | `dc3d011961afa4289598b90d308e39a8a5f34813f5f7d4af475d12c4321e3147` | 3 | held-out side |
| `qore kdi ste` | `39832e505bdfc025077c1f7aafe47d76e40de22471f148b242beb69088e90bb8` | 0 | development side (derivation side) |
| `REM 1003 Akinidad stela text` | `39716c8af11f898ffb36de94eb501ffe5953b03d2ed0970898f018d2bf034e83` | 9 | held-out side |
| `bedewi ato mk` | `6aa442f449ca7fd04e478e36feef2ff2ae3020977107ccf9278276247b0adc54` | 0 | development side (derivation side) |

*Pass:* every recomputed digest, residue, and side
equals the table, and no text appears on both sides.
The computation as executed at this amendment is
filed at
`records/split-construction-execution-note-2026-11-22.md`.
