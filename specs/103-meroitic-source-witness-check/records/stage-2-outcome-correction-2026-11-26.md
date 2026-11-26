# Spec 103 — Stage 2 Outcome Record Correction: §6's held-out prediction cells (2026-11-26)

Dated correction to `records/stage-2-outcome-record-2026-11-26.md`
§6, filed 2026-11-26 under Co-scientist Round L unit L-M-1
(adjudication APPLY). The outcome record itself is not edited:
its §6 table stands as filed, and this correction supersedes
four of its cells. Nothing in this correction changes any
Spec 103 outcome.

## 1. What §6 printed, and what the machine record says

§6 attributes its counts to "the control-verified corrected
Step 4 counts of the conformance addendum (§2)" and prints,
in its Frozen column, PASS for xolkete, pxolkete, xolkte, and
wisi. The controlling machine record —
`records/stage-2-results-2026-11-26.json` (`step4_restated`,
the control-verified restatement of the conformance
addendum's Step 4; the addendum replay regenerated its filed
results byte-identical at Stage 2) — gives different values
for those four forms. Verified cell by cell at adjudication
against the filed JSON at head `802ad272`:

| Form | §6 prints (texts, share, result) | Controlling record (texts, share, held-out prediction result) |
|---|---|---|
| soreyi | 10, 1.0, PASS | 10, 1.0, PASS (agrees; not corrected) |
| asoreyi | 2, 1.0, FAIL | 2, 1.0, FAIL (agrees; not corrected) |
| xolkete | 7, 0.714, PASS | **1, 1.0, FAIL** |
| pxolkete | 3, 1.0, PASS | **0, undefined, FAIL** |
| xolkte | 3, 1.0, PASS | **1, 1.0, FAIL** |
| wisi | 9, 1.0, PASS | **0, undefined, FAIL** |

The columns are held-out prediction results: whether the
frozen candidate prediction for each form met its registered
legs on the held-out set. The frozen and corrected machine
legs agree on texts and share for all six forms, so one
controlling row per form suffices. The four corrected forms
fail on the texts leg (the share leg passes for xolkete and
xolkte; both legs fail for pxolkete and wisi).

Share convention for the zero-text forms: the checker stores
share 0.0 where no text carries the form; the frozen record's
share for such a form is undefined (null), as the Stage 1
outcome record explains. Either convention may be used if it
is named; printing 1.0, as §6 did, is wrong under both.

## 2. What this correction does not change

The Outcome column of §6 — CLAIM STANDS for soreyi,
xolkete, pxolkete, xolkte, wisi, and NOT CHECKED —
INCOMPLETE COVERAGE for asoreyi — states
extraction-fidelity outcomes. Those outcomes agree with the
machine record (`outcome_stage2` in `step4_restated`) and
are **not** changed by this correction. The kill-check
reading in §6 is likewise unaffected: no discrepancy is
demonstrated at any locus, and the input-error explanation
for asoreyi is neither confirmed nor retired. Spec 097
Stage 4.4's outcome stands unreopened.

## 3. Provenance

Round L (Meroitic Co-scientist session
`11cac4f7-f109-4fac-bbb5-c670eb33b291`, 2026-11-26)
identified the mismatch by direct comparison of §6 against
the filed JSON and the prior conformance control, under an
advance kill check (withdraw if the §6 columns belong to
another evidential partition, or if the controlling records
support the printed numbers); neither condition held at
adjudication. The session's restated machine fields were
themselves verified equal to the prior conformance objects:
the error is confined to the outcome record's prose table, a
Stage 2 reporting error. It is not a reopening of E-M-1 (the
repaired checker) or D-M-3 (the settled Stage 1 execution).
Adjudication and landing are recorded at row L-M-1 of
`specs/091-anchor-comparison-integrity/records/coscientist-recommendations-ledger.md`
and in that package's rounds history ledger.
