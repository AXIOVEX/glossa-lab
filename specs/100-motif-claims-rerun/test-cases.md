# Spec 100 — Test Cases

All six test cases are implemented in
`tests/test_motif_rerun.py` against the pipeline of record
(`tools/motif_rerun.py`, `tools/deposit_extract.py`), run
on synthetic fixtures only — no real iconography label is
read by any test — except TC-100-04, which computes sign
marginals (no labels) over the repository's real tracked
population files. Execution at registration is recorded,
with payload verdicts, in
`records/tc-execution-2026-11-22.md`.

## TC-100-01 — The gate refuses record mode without a deposit

*Exercises:* C100-1 (nothing computed before the deposit).
*Fixture:* the real repository root; no deposit.
*Assertions:*
1. Record mode with no `--deposit` exits 3, prints
   GATE CLOSED, and writes no outcome file.
2. Record mode naming a deposit path that does not exist
   exits 3 the same way.
*Pass condition:* both assertions hold; the test process
exits 0.

## TC-100-02 — Fixture arithmetic and the strict threshold

*Exercises:* C100-2 (replay at the filed threshold),
C100-3 (mechanical counts).
*Fixture:* a 20-seal synthetic population and label set,
hand-computed.
*Assertions:*
1. M006/tiger: cells (2, 0, 2, 16), lift exactly 5.0, and
   the verdict is NOT REPRODUCED — the filed bar is
   strict (lift > 5.0); the odds ratio is undefined
   (b = 0).
2. M080/tiger: cells (3, 1, 1, 15), lift 3.75, odds
   ratio 45.0, verdict NOT REPRODUCED.
3. M013/gharial: cells (2, 0, 0, 18), lift 10.0, verdict
   REPRODUCED; odds ratio undefined (b = c = 0).
*Pass condition:* all assertions hold; the test process
exits 0.

## TC-100-03 — The frozen lift formula reproduces the filed M063 value

*Exercises:* C100-2 (the filed figures and the formula
that must replay them).
*Fixture:* a synthetic 1,670-seal population with M063 on
18 seals and gharial labels on 64, overlapping on 3 — the
filed fragment's own numbers.
*Assertions:*
1. Cells are (3, 15, 61, 1591).
2. The computed lift rounds to 4.35 at two places — the
   filed value — and the verdict is NOT REPRODUCED.
*Pass condition:* all assertions hold; the test process
exits 0.

## TC-100-04 — Marginals replication over the tracked population

*Exercises:* C100-3 (the two-path discipline on the real
representations).
*Fixture:* the repository's tracked
`outputs/phase100_full_corpus.json` and
`outputs/phase114_full_seal_translations.json`. No labels.
*Assertions:*
1. Both paths give a 1,670-seal population.
2. For all 13 claim signs, both paths' sign marginals
   equal PR #634's replicated counts exactly (M006 15,
   M013 23, M016 23, M039 18, M045 24, M057 18, M060 20,
   M062 28, M063 18, M067 15, M068 13, M073 25, M080 19).
*Pass condition:* all assertions hold; the test process
exits 0.

## TC-100-05 — Missing-label handling and the join defect

*Exercises:* C100-5 (missing labels), spec section 3.2
(the join).
*Fixture:* a 10-seal synthetic population; deposit rows
for 7 seals only, one of them an empty iconography
string.
*Assertions:*
1. The labeled population is 7; the cells sum to 7; the
   hand-computed cells (2, 2, 0, 3) hold; the population
   is still reported as 10.
2. A deposit row keyed outside the population raises the
   pipeline's DEPOSIT DEFECT outcome rather than a table.
*Pass condition:* all assertions hold; the test process
exits 0.

## TC-100-06 — The extractor's pin and schema discipline

*Exercises:* C100-1, C100-6 (the deposit must come from
the pinned build or not at all).
*Fixture:* a synthetic source CSV in the historical
layout (columns cisi_number, position, letters,
iconography, site; two rows for one seal).
*Assertions:*
1. With a wrong pin the extractor exits 2 with PIN
   MISMATCH and writes no file.
2. With the source's true SHA-256 as pin it exits 0 and
   writes one row per seal, iconography lowercased and
   taken from the seal's first row.
*Pass condition:* all assertions hold; the test process
exits 0.
