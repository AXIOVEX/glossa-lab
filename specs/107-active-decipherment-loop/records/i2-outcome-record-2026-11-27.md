# Spec 107 — Cycle 2: I-2 Outcome Record (T202)

**Date:** 2026-11-27. **Program:** Spec 107 — Active
Decipherment Loop, cycle 2. **Test:** I-2, executed exactly
as registered at `records/cycle-2-registration-2026-11-27.md`
§3, under the owner's OD-O-1 ruling. **Execution:**
`records/i2-execution.py` (the I-1 script with the
registered cycle-2 deltas only; the full diff against
`records/i1-execution.py` is filed at
`records/i2-vs-i1-execution.diff`), run on tower-compute
2026-11-27; raw output at `records/i2-raw-output.json`.
Donor pins: Kovetsky inscriptions source SHA-256
`1e91e3a0c52626482bc4015b597df862e7818602dab48a7e870240ab2e567bc4`
(commit `145af0836c071e7c9796d37d4b36add00d347c8a`); Latin
bytes from cycle-1 custody, SHA-256 as filed in the raw
output. Every replication's predictor advantages were
computed by two independent scorer implementations and
agreed to six decimal places throughout (TC-107-02's
standing standard; a disagreement stops the run — none
occurred).

**Verdict: INDETERMINATE** — under the registered rule,
by the R2-measurability configuration, with the preflight
passed in full. The anatomy is at §2; what the outcome
licenses is stated at §3, and no more than that.

## 1. The OD-O-1 preflight: PASSED, all three gates

1. **Target shape.** Recomputed from the Spec 105 custody
   datasets: 1,670 artifacts, 7,002 tokens, inventory 390,
   20 duplicated artifacts — d = 20/1670 = 0.011976048
   exactly. Token-count multiset SHA-256
   `146998f1ade75425659b60cc76062015cb0aa75ca765c51208b412c3b3ae733f`.
2. **Achieved duplication.** All 120 replications (2
   donors × 3 scales × 20) measured at exactly 0.011976 —
   min = max = the registered rate, inside the ±0.01
   tolerance with the full margin unused. The cycle-2
   construction (admission sampling to U = A′ − ⌊d×A′⌋
   distinct sequences, then exact copies) meets the
   registered rate at every scale: 10/835, 20/1670,
   40/3340. No draw cap was approached.
3. **Ground-truth agreement.** The R2 ground-truth sets
   computed by the two independent implementations agree
   exactly at both levels for both donors. Set sizes:
   Meroitic 1 mark at ρ = 0.95 and 1 at ρ = 0.90 — the
   mark **a**, class initial, at both levels; Latin 0
   marks at both levels.

## 2. The verdict anatomy

**R1 (the G-IND-form separation), at 1×, medians over 20
replications:** Meroitic RIGHT 0.6822 / WRONG −0.0438 /
SHUFFLE 0.2263; Latin RIGHT 0.4338 / WRONG −0.5388 /
SHUFFLE 0.1019. Both donors are R1-positive under the
registered conditions (RIGHT ≥ 0.05 and ≥ 2 × max(WRONG,
SHUFFLE)); neither is R1-negative. The separation also
holds at 0.5× and 2× for both donors (full grid in the
raw output).

**R2 (the positional clause) at the re-specified levels:**
measurable for **neither** donor at either level. The
measurability floor is a median of ≥ 5 ground-truth
marks restricted in the sample; Meroitic's median is 1.0
(its single ground-truth mark — where present, it is
detected with median sensitivity 1.0 at median FPR 0.04,
figures carried here as description of one mark, not as
a clause verdict), and Latin's is 0.0 (its stream
contains no mark at all whose larger non-sole share
reaches 0.90 at the registered occurrence threshold).
ρ* is therefore undefined for both donors.

**Rule application.** Each donor evaluates POSITIVE
(R1-positive; R2 binds only where measurable, and it is
measurable for neither). The registered test-level rule
then gives **INDETERMINATE**: R1 positive for both
donors while R2 is measurable for neither is the
registered indeterminate configuration, carried forward
from cycle 1 without amendment.

**R3 (description only):** median adjacency recovery
1.0 in all six cells.

## 3. What this outcome establishes, and what it does not

The preflight earns exactly what OD-O-1 scoped for it.
The generator now conforms to its registration exactly —
the defect Round O found in I-1 (achieved duplication
0.39/0.23 against a registered 0.012) is closed by
construction and verified by measurement in 120/120
replications — so I-2's R1 figures are calibration
figures at the Indus shape in the strong sense: at that
shape, the program's predictor separates a structured
donor from its wrong-model and shuffled controls by a
wide margin, for both donors and at all three scales.

The positional clause itself remains untested at the
registered levels, and the reason is now measured rather
than suspected: at restriction levels ρ ∈ {0.95, 0.90}
computed over non-sole occurrences, the known-structure
donors contain essentially no restricted marks (one in
Meroitic, none in Latin). A clause about near-absolute
positional restriction cannot be calibrated on donors
that do not exhibit the phenomenon at those levels; the
registration's measurability floor exists to say exactly
this instead of scoring a one-mark sample. I-2 is
therefore **INDETERMINATE (TC-107-07 executed; the
falsifier's indeterminate arm)**, and no "calibrated at
Indus shape" claim is made for the positional clause.
What is calibrated is the R1 separation and the
generator's conformance; the clause awaits donors or
levels at which restricted marks exist in measurable
numbers, which is a future registration's question, not
this cycle's to improvise.

**AI disclosure:** executed by an AI agent (Muse, via
Muse) at the direction of Tristen Pierson, per
constitution sec. VI.
