# Spec 112 — Preflight Record and Closure (2026-11-28)

The conformance preflight of spec.md §4 ran once, under
the execution freeze (records/execution-freeze-2026-11-28.md,
freeze commit `377db656`), on the pinned corpus and the
pinned ground-truth sets. **The preflight did not pass:
all three legs failed their registered floors. Under
kill criterion KC-1 and claim C112-7 the study closes
as filed.** No corpus output was produced, and none is
scoreable under this registration (TC-112-04 holds: the
record tree contains no induction output, and the
harness's induction command was never run). The response
to this failure is a revised design under a new
registration, never a lowered floor; no floor, ground-
truth set, or scoring rule in this record was adjusted
after the run, and nothing was re-run.

Every figure below is the payload's own: harness exit 0,
output at records/preflight-output.json, and each figure
recomputed exactly by the independent implementation of
TC-112-06 (records/execution-verify.py,
records/verify-output.json: 14 of 14 checks agree —
rational figures exact, entropies to 1e-9 with the same
argmax, pass flags consistent).

## P-1 — Segmentation recovery: FAILED

Median boundary F1 over the 1,719 ground-truth forms:
**0**, against the floor of 0.80.

Mechanism, measured, not conjectured: the segmenter's
top-1 candidate is the whole unsegmented form for
**1,719 of 1,719** ground-truth forms. The whole-form
fallback segment is scored under its own positional
class (W), whose distribution is over the 3,532
distinct forms at count 1 each; with the registered
add-0.1 smoothing its log-probability is the same
constant, about -8.17 nats, for every form, and that
constant beats every genuine segmentation (whose
initial- and medial-class segments are scored against
far larger class totals). The run therefore measures
a normalization artefact of the fallback's scoring,
not segmentation recovery: as built, the model cannot
express a segmentation as its top candidate at all.
This is a defect of the segmenter as specified at the
freeze, and it is filed as such. A segmenter whose
fallback cannot win by construction — and, beyond
that, a segmentation statistic with evidence it can
recover known boundaries at this corpus profile — is
a new registration's business. (For the record: the
program has now measured this failure mode twice, in
Spec 109's G2 segmentation family on synthetic ground
truth and here on real ground truth.)

## P-2 — Formula-slot recovery: FAILED

Labeled funerary texts: 95. The band-to-slot mapping
was found (invocation band 0, filiation 2 band 1,
presentation band 2, offering band 3, closing band 5)
but the induced slot sequence matched the Class B
template order on **1 of 95** labeled texts — a match
rate of 1/95 (about 0.011) against the floor of 0.90.
The name-slot leg held: the presentation slot's
filler entropy, 7.42 bits, is strictly the greatest
of the mapped slots'. One sub-leg does not carry the
leg.

Mechanism: the two filiation forms are positionally
diffuse in the real corpus. The most frequent
teɖe-type, `tedxelowi` (88 occurrences), has modal
band 1 with occurrences spread across all six bands
(10 / 37 / 20 / 17 / 3 / 1); the most frequent
terike-type, `terikelowi` (97 occurrences), also has
modal band 1 (4 / 36 / 27 / 22 / 7 / 1). The two
filiation slots therefore collide in a single
positional band, the mapping cannot separate them,
and the formula's middle slots do not live in
relative-position bands of these texts at all — the
texts vary in length and expansion, and the filiation
material moves with the names it attaches to. The
positional-band premise of the slot induction is
falsified at this corpus, by the corpus. Slot yield
of the real run: 2 bands.

## P-3 — Partial validity and the shuffle control:
FAILED on precision; the control held

Induced partials at the registered floors: 812.
Suffixal proposals (final mass at least 0.80): 36.
Of those, 4 are gold suffixal partials (`kes`, `kwi`,
`lEwi`, `lowi`): precision **1/9** (about 0.111)
against the floor of 0.80. The recall of the gold
suffixal partials, filed for transparency as the
freeze provides, is 1/4 (6 of 24 gold strings). The
proposals are dominated by longer word endings
(`betEwi`, `ebetEwi`, `telEwi`, `delowi`, `kelowi`,
`eqowi` and their kin): final-mass concentration
selects the endings of frequent forms generally, not
the suffix inventory, and several short gold
suffixes (`li`, `te`, `wi`, `se`) are diluted below
the final-mass floor by their medial occurrences.
The shuffle leg passed cleanly: the identical
induction on the token-shuffled funerary corpus
yields 0 slots against the real run's 2, a ratio of
0 against the cap of 0.20. The control is not what
failed; the precision of the partial extraction is.

## TC-112-05 — the fixture, filed with both readings

On the planted-structure fixture (120 synthetic
texts, seed 20261128), the ordered run's slot yield
was 1 band against the shuffled run's 0 — the
registered criterion of TC-112-05 (structure present
in the ordered run, absent at the cap in the
shuffled run, ratio 0) is met on its terms. The
stronger recovery expectations the freeze registered
for the fixture are NOT met: sequence match 1 of 120
and the maximum-entropy slot was filiation 2, not
the name slot. The fixture's short texts (4 to 7
tokens) collapse adjacent slots into single bands,
and its name types sit below the concentration
floor; it is filed as a machinery warning that the
real-corpus P-2 failure then confirmed at full
scale. No part of the verdict rests on the fixture:
the verdict rests on the three legs' own figures
against their own floors.

## Closure

- Verdict: **preflight NOT PASSED IN FULL** (P-1
  failed, P-2 failed, P-3 failed). The induction of
  spec.md §6 step 3 does not run. No candidate sets
  are filed, no standing moves, and Spec 102 and
  Spec 109 Stage 5 are untouched (TC-112-08: this
  execution wrote only inside
  specs/112-meroitic-structure-induction/ and the
  PROGRAM-STATE book; a tree diff over both
  neighbouring specs at the close is empty).
- What the closure establishes, in the kill
  discipline's own terms: a finding about these
  designs at this corpus. The positional-band slot
  induction is falsified as a measurement of the
  funerary formula (its ground truth is real, and it
  missed by 89 points). The final-mass partial
  extraction does not recover the known suffix
  inventory at anything near the registered
  precision. The unigram segmenter as specified
  cannot express its own answer. None of this is a
  finding about Meroitic, whose formula and suffix
  inventory are the ground truth that did the
  falsifying.
- Directions a future registration could take, named
  here without being commissioned: a segmenter whose
  whole-form fallback is a fallback in fact and whose
  boundary statistic is validated against the gold
  morphology before any corpus claim; a slot
  induction over filler classes and token identity
  rather than relative position alone (the filiation
  forms' identity is stable even where their
  position is not); a partial extraction scored
  against a significance null rather than a raw
  final-mass threshold (the Spec 109 G2 partials
  lesson, recurring here in a second form).

**AI disclosure:** executed by an AI agent (Muse, via
Muse) under the owner's 2026-11-28 direction.
