# Spec 100 — Test Cases

All nine test cases are implemented in
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
3. (RT6-C2, added 2026-11-22) Record mode naming a
   foreign deposit: an existing CSV at any path other
   than the registered deposit path
   `records/iconography-deposit-v1.csv`, with any
   citation string, exits 3 GATE CLOSED and writes no
   outcome.
4. (RT6-C2) Record mode with the deposit at the
   registered path but a bogus citation: a
   `--deposit-record` naming no existing in-tree record
   file, a record file that does not state the deposit
   CSV's actual SHA-256, or a record file whose
   `Permission basis:` line records refusal or silence
   (or states no granting term), each exits 3 GATE
   CLOSED and writes no outcome.
*Pass condition:* all assertions hold; the test process
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
2. (RT6-H3, amended 2026-11-22; assertion 2 as originally
   filed, in which the source's own SHA-256 as pin
   unlocked extraction, is superseded because it made the
   pin caller-supplied) A non-pinned source is refused
   even with its own hash: passing the synthetic source's
   true SHA-256 as `--pin` exits 2 with PIN MISMATCH and
   writes no file, because the supplied pin is not the
   embedded pin of record; and with no `--pin` the
   extractor uses the embedded constant and likewise
   refuses the non-pinned source (exit 2, nothing
   written).
3. The schema leg survives as a direct `extract()` unit
   check: one row per seal, iconography lowercased and
   taken from the seal's first row.
*Pass condition:* all assertions hold; the test process
exits 0.

## TC-100-07 — No standing change without a separate adjudication act

*Exercises:* C100-4 (the rerun changes no standing by
itself).
*Fixture:* a simulated gate-opening record-mode run in a
temporary tree (registered-path deposit with header only,
deposit record stating its SHA-256 and a granting
`Permission basis:` line; synthetic fixture only), plus
the package's claims and spec files hashed before and
after.
*Assertions:*
1. The run's outcome record contains no standing, ledger,
   or register field and changes no standing value.
2. The package's claims/spec files are byte-identical
   before and after the run: an outcome record citing the
   rerun changes no standing absent a separate
   adjudication act, which is a landing check on any
   future outcome PR as well as this test.
*Pass condition:* all assertions hold; the test process
exits 0.

## TC-100-08 — Proof-mode banner and synthetic label set only

*Exercises:* C100-7 (the proof computes nothing from real
labels).
*Fixture:* the real repository root, proof mode.
*Assertions:*
1. Proof mode exits 0, and both its stdout and its
   written output carry the banner "PROOF - NOT A
   RESULT".
2. The synthetic labels the proof uses are drawn only
   from the deterministic synthetic label set
   (`synthetic-tiger`, `synthetic-gharial`,
   `synthetic-elephant`, `synthetic-zebu`,
   `synthetic-rhinoceros`, `synthetic-unicorn`,
   `synthetic-none`); no real iconography string appears
   as a proof label.
*Pass condition:* all assertions hold; the test process
exits 0.

## TC-100-09 — The Miller-reply trigger states

*Exercises:* C100-6 (grant, refusal, silence).
*Fixture:* temporary trees as in TC-100-07, varying only
the deposit record's `Permission basis:` line.
*Assertions:*
1. Grant: a basis line stating Miller's reply grants the
   basis (granting term, no refusal term), with the
   deposit at the registered path and its SHA-256 stated
   in the record, opens the mechanical gate: record mode
   proceeds (the deposit-then-rerun sequence of spec
   section 5 becomes executable).
2. Refusal: a basis line recording a refusal does not
   satisfy the gate; record mode exits 3 GATE CLOSED.
   (Study-level consequence, recorded not executed: the
   study closes as GATE REFUSED, per spec section 4.)
3. Silence: no basis line, or a basis line recording
   silence / no reply, does not satisfy the gate; record
   mode exits 3 GATE CLOSED and the gate stays closed.
*Pass condition:* all assertions hold; the test process
exits 0.
