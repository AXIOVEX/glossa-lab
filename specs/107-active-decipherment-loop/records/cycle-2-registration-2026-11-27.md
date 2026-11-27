# Cycle 2 Registration — Active Decipherment Loop, Cycle 2 (Spec 107)

**Status: REGISTERED 2026-11-27** (on the landing of the
registration PR; no scoring run of any kind precedes that
landing). Cycle 2 is commissioned by the owner's act of
2026-11-27 in the Glossa-Lab chat (the keep-working
directive: work continues until nothing is left undone;
cycle 2 named in the cycle-1 report as the next loop
work). Cycle 1's outcome and trace records
(`records/cycle-1-outcome-2026-11-27.md`,
`records/cycle-1-trace-2026-11-27.md`) name cycle 2's
leads; this record registers them. Registration moves no
standing, verdict, or tally in any program.

**Owner ruling OD-O-1 (2026-11-27).** Round O referred
the I-1 duplication nonconformance's criterion-5
treatment to the owner (OD-O-1 in the Round O
adjudication record,
`specs/091-anchor-comparison-integrity/records/coscientist-sweep-adjudication-2026-11-27-round-o.md`
§5). The owner ruled in the Glossa-Lab chat on
2026-11-27 (08:27 ET): cycle 2 proceeds, with a
conformance-and-ground-truth preflight built into
I-2's registration. The preflight is registered at §3
as a gate before any I-2 scoring, and the ruling is
recorded in the Round O adjudication record (§7,
appended in this landing). The alternative — halting
cycle 2 pending a prospectively registered corrected
I-1 simulation — is not taken. OD-O-2 (the E-1
conformance gaps) is not ruled at this landing; §4
carries its standing note.

**Drafting history (disclosed).** Two earlier
registration drafts of this cycle were prepared on
2026-11-27 by a coordinator that became unreachable
before landing: a pushed branch
(`spec-107-cycle-2-registration`, head `37833204`, two
commits) and an unpushed commit (`35a84635`) in a
second worktree, the second draft adding the Round O
duplication-conformance paragraph at §3 and marking
I-2's execution task held pending OD-O-1. No PR was
opened for either draft and nothing in either landed.
This landing adopts the later draft's package (its
claims bundle, claims.md, spec.md, and test-cases.md
verified byte-identical to the earlier draft's),
amended in the respects named here: the OD-O-1
preflight gate and duplication construction at §3,
the OD-O-2 standing note at §4, the I-2 hold lifted in
tasks.md on the OD-O-1 ruling, and the registration
cascade re-executed over the current ledger build
(1,110 lines at this landing's base). The unlanded
branch is deleted on this landing's completion; its
commits remain in the tower worktrees of record.

Cycle 2's test set, fixed by the commission and by
cycle 1's trace:

- **I-2 (Indus)** — the positional-recovery calibration
  re-specified at realistic restriction levels (§3).
- **C-E-15 completed, then E-2 if it proceeds
  (Eteocypriot)** — the accepted feasibility decision
  C-E-15 (Co-scientist recommendations ledger, Round C,
  2026-11-23) is completed to a proceed/stop result under
  the rule registered at §4; on PROCEED, the design
  queue's E-2 (control-corpus parallel derivation)
  executes under §5; on STOP, the stop is the cycle's
  Eteocypriot outcome.
- **M-2 (Meroitic)** — the phonotactic battery from the
  design's Meroitic queue (§6).

## 1. Ranking record (Step 3)

Elicited likelihoods (author: the cycle-2 coordinator,
Muse, 2026-11-27; stated before any cycle-2 execution):

- **I-2.** P(POSITIVE) 0.55, P(NEGATIVE) 0.20,
  P(INDETERMINATE) 0.25. Basis: at ρ = 0.95 the Meroitic
  donor's ground truth is expected to clear the
  five-mark measurability floor (the a-sign stands at
  98.4% in {final, sole} on the full stream, and the
  digit marks that never take a successor stand at 100%
  where their counts reach 20), so measurability is
  likely; recovery sensitivity at Indus sample sizes is
  the genuinely open term. The Latin donor is expected
  to be not measurable at either level, which the
  registered rule absorbs (the verdict at ρ* rests on
  the measurable donors; a not-measurable donor is filed,
  not a disagreement).
- **C-E-15.** P(STOP) 0.80, P(PROCEED) 0.20. Basis: on
  the filed record every candidate correspondence set is
  consumed by an executed test or fails independence
  (the ICS 196 name pair is a name and its patronymic —
  one trial, not two — and is consumed by Specs 096 and
  104; the Androkles Dedication A intake is consumed by
  the OD-10 controls; the ICS 194/195 material was
  consumed by Spec 101's occurrence test, which is not
  an alignment correspondence). The decision is the
  executor's, made by applying §4's rule to the
  inventoried record; this likelihood is the ranking's
  input, not the decision.
- **E-2** (conditional on PROCEED). No likelihood
  elicited; the test is gated and its registration (§5)
  stands either way.
- **M-2.** P(POSITIVE, either family) 0.25, P(NEGATIVE)
  0.45, P(INDETERMINATE) 0.30. Basis: the battery's
  calibration item is the filed Stage 4.2 statistic,
  whose filed result was null-consistent (within-word
  shuffle p = 0.474) with the NES reference rate (0.3038)
  close to Meroitic's own (0.3152); discrimination, if
  any, must come from the battery's range structure
  across five items and survive its leave-one-out
  control, which is a demanding bar by design.

Expected information gain, stated qualitatively as in
cycle 1 (no cardinal EIG model is validated for this
loop): I-2 decides whether an entire statistic family —
positional restriction, the family Spec 105's Indus
facts belong to — is measurable at the shapes this
program actually has; that is the highest decision value
in the cycle, at small compute cost. C-E-15 is desk work
and gates the whole Eteocypriot alignment line: a STOP
closes the line until external evidence exists, a
PROCEED opens E-2; highest value per unit cost in the
cycle. M-2 tests the only remaining typological argument
bearing on Meroitic affiliation short of Spec 102, at
moderate cost, with a registered falsifier that removes
the argument from the program's set on a negative.

**Order and sensitivity.** Execution order: C-E-15 first
(desk; its result gates E-2), I-2 and M-2 in parallel
(independent; tower-compute). All three run this cycle
regardless of order. Sensitivity: I-2's and C-E-15's
ranks do not flip under any plausible perturbation of
the likelihoods above (their value is outcome-symmetric:
each outcome changes what the program may claim or do
next). M-2's rank is sensitive to one named risk: if its
calibration STOP-gate fails (the Stage 4.2 basis cannot
be reconstructed to the filed figures), M-2 returns a
filed basis finding instead of a battery verdict; that
finding is itself decision-relevant (it bounds what the
Stage 4.2 record can support going forward) and is
recorded as the test's outcome, not absorbed silently.

## 2. Null-yield minimum for cycle 2

Cycle 2 counts as non-null for kill criterion 4
(spec.md §4) iff at least one of:

(a) a decided outcome among the cycle's tests — an I-2
    or M-2 verdict that is neither INDETERMINATE nor a
    non-execution, or the C-E-15 decision itself (a
    completed proceed/stop decision under its registered
    rule is a decided outcome for this clause, whether
    or not E-2 then executes);
(b) a licensed standings or trace effect (a claim
    standing, a program position, or an argument-set
    membership that a cycle-2 outcome record licenses
    changing);
(c) a cycle-3 lead change driven by a cycle-2 outcome
    (a lead named, re-specified, or closed because of
    what cycle 2 returned).

## 3. I-2 — positional recovery at realistic restriction levels (Indus)

**Question.** Are positional-restriction statistics
measurable at Indus shape at the restriction levels real
corpora actually show? I-1 (cycle 1) returned
INDETERMINATE because its positional clause (R2) was not
measurable for either donor at the registered 99%
definition: no donor's full stream contains five marks
restricted at 99%, and the strongest real case anywhere
in the program's corpora (the Meroitic a-sign) stands at
98.4%. I-2 re-specifies R2 at ρ = 0.95 and ρ = 0.90 and
re-runs the calibration; everything else about the
machinery is I-1's, unchanged.

**Machinery (I-1's, by reference and by code).** Target
shape, reshaping, cipher, duplicate-aware split, donors
and pins, grid (2 donors × scales 0.5×/1×/2× × 20
replications), and the R1 predictor clause are exactly
as registered for I-1 (cycle-1 registration §2) and as
implemented in the filed I-1 execution script
(`records/i1-execution.py`). The I-2 code derives from
that script; the diff between the I-1 script and the
I-2 script is filed with the I-2 run record. Seed
namespace: `spec107-i2-{donor}-{scale}-{rep}`, rep
1..20. R1 is recomputed and filed as description only;
I-2's verdict turns on R2 alone.

**Duplication construction (I-2).** The cycle-1
registration's duplication sentence (replace ⌊d × A′⌋
artifacts, chosen uniformly, each with an exact copy
of a uniformly chosen other artifact, "so the achieved
duplication rate matches d within ±0.01") does not
achieve its stated rate on donors whose spans repeat
naturally — that is the Round O finding (§3,
"Duplication conformance") — because replacement acts
on a sample whose distinct count is already far below
A′. I-2 therefore constructs the sample to the
registered rate directly: spans are drawn under the
registered reshaping rule, and a drawn artifact is
admitted only if its token sequence is not already in
the sample, drawing continuing until
U = A′ − ⌊d × A′⌋ distinct sequences are held; the
remaining ⌊d × A′⌋ artifacts are exact copies of
uniformly chosen held sequences, per the registered
sentence's copy rule. The achieved rate is then
⌊d × A′⌋/A′ by construction (exactly d at all three
registered scales: ⌊d × 835⌋ = 10, ⌊d × 1,670⌋ = 20,
⌊d × 3,340⌋ = 40). The draw cap is 200 × A′ draws per
replication; if the admission process cannot fill U
distinct sequences within the cap, that is a
preflight failure under check (2) below. Achieved
token counts are filed per replication, as in I-1;
the cipher and the duplicate-aware split then apply
to the constructed sample exactly as registered
for I-1.

**Duplication conformance (Round O).** The Co-scientist
Round O conformance annotation
(`records/round-o-conformance-annotations-2026-11-27.md`,
filed 2026-11-27) records that I-1's filed replications
did not achieve the registered duplication rate within
its ±0.01 tolerance. For I-2, the registered
specification governs over the I-1 script where the two
differ: the duplication step is executed as registered
(the count of duplicated artifacts is ⌊d × A′⌋ by
construction), the achieved rate is filed per
replication, and if any replication's achieved rate
falls outside ±0.01 the test halts and the failure is
filed as a deviation rather than scored over. The I-2
run record names the I-1 deviation and states the
correction; it is not carried into I-2 silently.

**The OD-O-1 preflight (registered gate, before any
scoring).** Before any I-2 scoring run, and before the
verdict machinery consumes any generated sample, the
following preflight is executed on tower-compute over
the full registered grid (2 donors × scales
0.5×/1×/2× × 20 replications, at the registered
seeds), and its results are filed in the I-2 run
record ahead of every scoring figure:

1. **Target shape.** The target shape parameters are
   recomputed from the Spec 105 custody datasets and
   must reproduce the registered values exactly:
   A = 1,670 artifacts (1,336 derivation + 334
   reserve); T = 7,002 tokens (5,611 + 1,391); the
   per-artifact token-count multiset; full-corpus
   inventory 390 marks; d = 20/1670 = 0.011976048 by
   the registered computation over the two datasets
   combined in their Stage 1 order.
2. **Duplication conformance.** For every replication
   in the grid, the generated sample's achieved
   duplication rate (A′ − U)/A′ is measured on the
   sample as generated (pre-cipher; the cipher is a
   bijection and cannot change it) and must fall
   within ±0.01 of d — 120 of 120 replications, the
   exact check I-1's filed output fails.
3. **Ground truth.** The R2 ground-truth restricted
   sets at ρ = 0.95 and ρ = 0.90, with the sole-only
   exclusion applied, are computed from each donor's
   full stream by both registered implementations
   (§3, "Two implementations"), and the two must
   agree exactly on every set and count — discharged
   here, before scoring, not after.

If any preflight check fails, I-2 does not proceed
to scoring: the failure, with its measured figures,
is filed as I-2's outcome (a preflight failure,
returning no verdict), and C107-7's outcome is
recorded on that basis. No sample that has not
passed the preflight is scored. The license any I-2
verdict carries is earned through the preflight as
filed: no "calibrated at Indus shape" language is
used for I-2 beyond the restriction level ρ* and the
measured sensitivity and false-positive terms of
§3's standings effects, and forward citations of I-2
name the preflight result they rest on.

**R2 re-specified.** For a level ρ ∈ {0.95, 0.90}:

- Ground truth (per donor, from its full stream): a mark
  is restricted-initial at ρ iff it occurs ≥ 20 times in
  the full stream and the share of its occurrences in
  {initial, sole} positions is ≥ ρ; restricted-final at
  ρ likewise for {final, sole}. A mark meeting both
  classes at ρ is assigned to the class with the larger
  non-sole share (the larger of its initial-only and
  final-only shares); if those are equal, to
  restricted-initial.
- Sole-only exclusion: a mark whose every occurrence is
  sole (it never occurs inside a multi-mark group) is
  excluded from R2 entirely — from the ground-truth
  sets, from sensitivity, and from the false-positive
  rate — at every level, and is filed as its own line in
  the run record. A mark that only ever appears alone
  has no positional distribution to recover.
- Sample classification: the same rule, at the same ρ,
  applied to a replication's full sample (as I-1
  defined the full sample). Marks below 20 occurrences
  in the sample are excluded from numerator and
  denominator and counted not-measurable for that
  replication, as in I-1.
- Sensitivity at ρ: the fraction of the donor's
  ground-truth restricted marks (at ρ) that the sample
  classifies with the same restriction. False-positive
  rate at ρ: the fraction of sample marks with ≥ 20
  occurrences that are not ground-truth restricted at ρ
  but are classified restricted at ρ. Both are computed
  per replication and summarised by their median over
  the 20 replications of a cell, as in I-1.
- Measurability: R2 is measurable for a donor at ρ iff
  its ground-truth restricted set at ρ (after the
  sole-only exclusion) has ≥ 5 marks, as in I-1.

**Verdict (at 1× cells only; other cells are filed as
the recovery curve, as in I-1).** Let M(ρ) be the set of
donors measurable at ρ, and let ρ* be 0.95 if
M(0.95) ≠ ∅, else 0.90 if M(0.90) ≠ ∅, else none.

- ρ* = none → **NEGATIVE**: positional restriction is
  not measurable at Indus shape even at the 90% level.
- At ρ*, a measurable donor PASSES iff its median
  sensitivity ≥ 0.50 and its median false-positive rate
  ≤ 0.10 (I-1's R2 thresholds, unchanged).
- **POSITIVE** iff every donor in M(ρ*) passes.
- **INDETERMINATE** iff some donor in M(ρ*) passes and
  some fails (the registered donor-disagreement case).
- **NEGATIVE** iff every donor in M(ρ*) fails.
- A donor not in M(ρ*) is filed as not measurable at ρ*;
  its results at any level where it is measurable are
  filed as part of the recovery curve (description),
  and do not enter the verdict.

**Two implementations.** Two independent implementations
of the R2 computation (ground-truth sets, per-replication
sensitivity and false-positive counts) must agree exactly
on every integer count and on the ground-truth sets, and
to 6 decimal places on every median, as TC-107-02
required for I-1; disagreement halts the test until
resolved, and the resolution is filed.

**Standings effects (registered in advance).** POSITIVE:
the trace records that Indus positional facts of the
Spec 105 line may be read at restriction level ρ* with
I-2's measured sensitivity and false-positive rate as
their error terms. NEGATIVE: the trace records
positional-restriction statistics as unmeasurable at
Indus shape at every registered level (99%, 95%, 90%),
and any program argument needing them is marked
unsupported-by-calibration. INDETERMINATE: no general
license; the donor-dependence is recorded. No anchor
standing moves under any outcome. IND-1's GOOD and its
Round N qualification are untouched by I-2 (R1 is
description here).

**Falsifier (C107-7).** As filed in claims.md: the claim
fails if the returned verdict is not the mechanical
consequence of this section's rule over the filed
per-replication values, or the two implementations
disagree on any ground-truth set or count.

## 4. C-E-15 — the alignment-line feasibility decision (Eteocypriot)

**The item.** Recommendations-ledger row C-E-15
(accepted, Round C, 2026-11-23): "a feasibility decision
for the alignment line — which independently
identifiable correspondences remain, exposure state,
whether enough independent items exist to beat simple
baselines; a stop decision if none." This section
registers the decision procedure; the decision itself is
desk work over filed records. No corpus bytes are scored
in making it.

**Inventory basis (filed records only).** The Spec 096
package and its freeze; the Spec 101 package and its
cycle-1 outcome record; the OD-10 Androkles intake and
controls record (recommendations ledger B-E-8); the
Spec 104 package (ICS 196 as its instance); the
recommendations ledger's Round C rows C-E-10..C-E-15;
the filed correspondence state for the second-reader
routes (Steele, Egetmeyer — pending replies are not
correspondences and cannot enter the inventory as
material).

**OD-O-2 standing note.** Round O also referred the
E-1 conformance gaps (O-E-1: the Spec 101 outcome
record filed late; O-E-2: the TC-101-06 closure path
never exercised, its gap standing) to the owner as
OD-O-2. That ruling is not given at this landing, and
the qualifications stand on the record as filed in
the Spec 101 package. Nothing in this cycle's
Eteocypriot work uses "all checks passed" or any
equivalent licensing language; the decision registered
here is a feasibility decision over the filed record,
not a conformance clearance.

**Registered rule.** A correspondence set counts toward
PROCEED iff all four hold:

(i) **Independently identifiable** — its
    Eteocypriot–Greek correspondences are fixed
    independently of the program's own candidate
    readings: by the bilingual's Greek side, or by
    sign-level identity with the Common syllabary; not
    by a proposed decipherment.
(ii) **Mutually independent items** — the set's items
    are independent trials; a name and its patronymic
    are one trial (C-E-10, as filed).
(iii) **Unconsumed** — the set has not served as the
    scored material of an executed test (consumption as
    filed in Specs 096, 101, and 104 and the OD-10
    controls).
(iv) **Arithmetically sufficient** — the number of
    independent items is enough that beating the
    alignment line's registered simple baselines is
    arithmetically possible; the decision record names
    the baseline of record and shows the arithmetic.

**Result.** PROCEED iff at least one inventoried set
satisfies (i)–(iv); STOP otherwise.

**The decision record files:** the inventory (every
candidate set considered, its exposure state, its
consumption state), the rule's application item by
item, the result, and the consequence — on PROCEED, the
set E-2's line proceeds from and the next alignment test
the set supports (registered separately when designed);
on STOP, the reasons and the recorded consequence: the
alignment line rests until external evidence exists (a
new bilingual, a legible unseen text, or a second-reader
return that itself supplies a qualifying set), and the
stop is this cycle's Eteocypriot outcome.

**Falsifier (C107-8).** As filed in claims.md: the claim
fails if a set satisfying (i)–(iv) exists in the filed
record while the decision returns STOP, or none exists
while it returns PROCEED.

## 5. E-2 — control-corpus parallel derivation (Eteocypriot; gated)

Executed only if C-E-15 returns PROCEED (§4). If C-E-15
returns STOP, E-2 does not execute; claim C107-9's
outcome is the recorded non-execution, and this section
stands as the registration that would have governed it.

**Test (the design queue's E-2, as filed).** Derive the
ICS 217 (Idalion tablet) Greek control excerpt's L2/L3
frequency and adjacency tables — face A lines 3–4, 66
signs, as reproduced in Chadwick 1987; held material —
alongside the filed development-set tables (the Spec 105
Eteocypriot derivation, ICS 196), same code, same
standards.

**Registered comparison.** By the same code, for both
corpora: (a) singleton share — the share of the inventory
occurring exactly once; (b) adjacency sparsity — distinct
observed adjacent pairs divided by possible pairs
(inventory²); (c) top-pair share — the largest pair
count divided by total adjacencies (description only).
The development set's own split-half variation on (a)
and (b) is computed the same way (split by artifact
line, halves as filed in the run record).

**Verdict.** POSITIVE iff (a) or (b) separates the
control from the development set by more than the
development set's split-half variation on that statistic
(the statistics carry kind-level signal at this size).
NEGATIVE iff both (a) and (b) fall within split-half
variation — the registered falsifier: the control's
tables are indistinguishable in kind from the
development tables, those statistics carry no language
signal at this size, and any argument resting on them is
withdrawn in the trace. INDETERMINATE iff the held
control excerpt cannot be prepared to the filed standard
(the run record states the reason; no new material is
acquired mid-test — an excerpt not locatable in held
custody returns INDETERMINATE on that ground).

**Standings effects.** None either way, as designed: the
calibration is the product. The trace records the
verdict and, on NEGATIVE, the withdrawal.

## 6. M-2 — the phonotactic battery (Meroitic)

**Question.** Do Meroitic's phonotactics, measured from
the secure stratum, discriminate between the two
registered affiliation families — the NES set (R1 of
Spec 097's freeze v2) and the Afroasiatic set (R2) — at
battery standard, with the battery's own permutation
nulls and a wrong-family control? M-2 is not the
Spec 102 test: it does not consume Spec 102's gates G-1
or G-2, cannot return the affiliation verdict, and does
not displace Spec 097 Stage 4.2's R3 position under any
outcome.

**Basis.** The Meroitic word basis of Spec 097 freeze
v2 §4, reconstructed exactly: the development partition
(335 distinct texts) and the 932 distinct example
phrases, from the pinned Kovetsky build only
(inscriptions source at SHA-256
`1e91e3a0c52626482bc4015b597df862e7818602dab48a7e870240ab2e567bc4`,
source commit
`145af0836c071e7c9796d37d4b36add00d347c8a`), under the
extraction conventions of the filed Stage 4.2 pipeline
(`pipeline-v2.py`, held in campaign custody) including
the freeze's §7 diacritic fold. Per-stratum battery
values are computed over the development texts only,
under M-1's strata (the filed M-1 strata derivation;
Population P partition). No Otten byte is consumed.

**Calibration STOP-gate.** Before any battery item is
scored, the reconstructed basis must reproduce the filed
Stage 4.2 calibration figures: 12,863 words; 13,406
word-internal consonant pairs separated by exactly one
vowel; the same-place rate 0.3152 (to 4 decimal places);
and the NES reference rate 0.3038 (to 4 decimal places)
computed on the R1 lists as filed. If any figure does
not reproduce, M-2 STOPS: the mismatch is filed as the
test's outcome (a basis finding), no battery statistic
is computed, and no silent basis substitution is made.

**Comparator data.** The ASJP lists in program custody
(`glossa-custody/spec097/`: forms.csv, languages.csv,
parameters.csv; source lexibank/asjp at commit
`cf4bf0d13c95256b1b48f440d07c5c098500a770`, CC BY 4.0;
the run record files the custody files' full SHA-256
hashes before scoring). Family sets exactly as freeze
v2 registers them — R1 (NES): OLD_NUBIAN, NOBIIN,
DONGOLESE_NUBIAN, KUNUZ_NUBIAN, MEIDOB_NUBIAN, NARA.
R2 (Afroasiatic): COPTIC, LATE_EGYPTIAN, MIDDLE_EGYPTIAN,
AKKADIAN, BIBLICAL_HEBREW, AMHARIC, HAUSA. One list per
language, as filed. A comparator "word" is one ASJP form
for the language, as a segment sequence under §6.1's
mapping.

### 6.1 Segment and place-class mapping

Meroitic place classes exactly as freeze v2 registers
them: labial {p, b, m}, velar {k, q, g, x}, coronal
{t, d, s, z, n, l, r}, other (every other consonant,
including h). Vowels a, e, i, o, u. For ASJP symbols, the
mapping table (ASJP symbol → vowel / labial / velar /
coronal / other) is derived from the ASJP codebook's
articulatory definitions and is **filed in the run
record before any battery statistic is computed** (the
Spec 101 candidate-registration-before-scoring pattern);
a symbol the table does not cover defaults to "other",
and every default is listed in the run record. The
Meroitic-side table is filed the same way, from
pipeline-v2.py's conventions.

### 6.2 Battery items

Each item is computed identically on the Meroitic basis
(pooled, and per stratum over development texts) and on
each comparator list:

1. **SP-CVC** (calibration item; freeze v2 §4 verbatim):
   among word-internal consonant pairs separated by
   exactly one vowel, the rate whose two consonants
   share a place class.
2. **LV-CO**: among words with ≥ 2 consonants, the rate
   containing at least one labial-class and at least one
   velar-class consonant.
3. **ONSET-CC**: among all words, the rate whose first
   two segments are both consonants.
4. **CODA-C**: among all words, the rate whose final
   segment is a consonant.
5. **LV-TRANS**: among the SP-CVC pair population
   (consonant pairs separated by exactly one vowel), the
   rate whose pair is labial→velar or velar→labial in
   sequence.

### 6.3 Nulls

- **Null W** (within-word consonant shuffle; items 1 and
  5): each word's consonants are permuted among its
  consonant slots, vowel skeleton and consonant multiset
  preserved; 10,000 shuffles; seed 20261127 (registered
  here, in advance). An item is NULL-CONSISTENT for
  Meroitic iff its observed value lies within the
  central 95% of its shuffle distribution.
- **Null X** (cross-word consonant permutation; item 2):
  consonants are permuted across words within the
  corpus, each word's skeleton and consonant count
  preserved, the corpus consonant frequency distribution
  preserved; 10,000 permutations; seed 20261127. Same
  NULL-CONSISTENT definition.
- Items 3 and 4 are invariant under both nulls by
  construction (they depend only on the vowel skeleton);
  no null applies, and they lean on ranges and the
  control alone. The registration states this rather
  than performing an empty test.
- Nulls guard the Meroitic observation only. Comparator
  lists are reference distributions; no null is applied
  to them.

### 6.4 Ranges, leans, control, verdict

- **Family range** per item: [min, max] over the
  family's lists' values, using only lists meeting the
  item's denominator floor (≥ 40 pairs for pair items,
  ≥ 40 words for word items, and the item's own
  denominator condition met). An item is SCOREABLE iff
  both families contribute ≥ 3 qualifying lists and
  Meroitic's pooled denominator meets its floor
  (≥ 100 pairs for pair items, ≥ 100 words for word
  items).
- **Lean**: a scoreable item leans to family F iff
  Meroitic's pooled value lies within F's range, outside
  the other family's range, and — where a null applies
  (items 1, 2, 5) — the item is not NULL-CONSISTENT for
  Meroitic. L_R1 and L_R2 count the leans.
- **Control (wrong-family, leave-one-out)**: each of the
  13 comparator lists is in turn scored as a target
  against both families' ranges (its own family's range
  computed without it; nulls not applied to control
  targets, as for comparators). C = the maximum, over
  the 13 targets, of the lean count toward either
  family.
- **Per-stratum values** are verdict-bearing only where
  the stratum meets the item's Meroitic floor (≥ 100
  pairs / ≥ 100 words in that stratum); below the floor
  they are description.
- **Split-half stability**: item values over the
  development partition split by inscription-ordinal
  parity are filed as description.
- **Verdict.** POSITIVE(F) iff ≥ 4 items are scoreable,
  L_F ≥ 3, L_F − L_other ≥ 2, and L_F > C. NEGATIVE iff
  ≥ 4 items are scoreable and POSITIVE fails for both
  families — the design's falsifier (the battery's
  discrimination falls inside its own permutation null,
  or the wrong-family control discriminates as strongly);
  the outcome record states which falsifier arm fired
  (control arm: C ≥ max(L_R1, L_R2); null arm: a majority
  of the null-bearing scoreable items NULL-CONSISTENT;
  or non-separation: Meroitic inside both or neither
  range on a majority of scoreable items).
  INDETERMINATE iff fewer than 4 items are scoreable, or
  a pooled POSITIVE(F) is contradicted in every
  adequate-floor stratum (each such stratum leans
  against F or neither).

**Contamination, stated in advance.** Egyptian loans in
Meroitic are a known stratum concern. They are NOT
excluded: no loan list exists on file to exclude by, and
constructing one for this test would be an unregistered
analysis. The basis is the corpus as filed, as Stage 4.2
used it; the limitation is recorded here and in the
outcome record.

**Standings effects (registered in advance).**
POSITIVE(F): the trace records phonotactic support for
F, labelled typological, weight below Spec 102's gates;
Spec 097's R3 position is not displaced. NEGATIVE: the
phonotactic leg is removed from the program's argument
set; Rowan's argument is recorded as not sustained at
battery standard. INDETERMINATE: no effect. No claim
standing moves under any outcome.

**Falsifier (C107-10).** As filed in claims.md: the
claim fails if the battery's verdict is not the
mechanical consequence of this section's rules over the
filed item values, or the calibration STOP-gate figures
were not reproduced before scoring and the battery
scored anyway.

## 7. Claims and test cases for cycle 2

Claims intaken with this registration: **C107-7** (I-2),
**C107-8** (C-E-15 decision), **C107-9** (E-2, gated),
**C107-10** (M-2), **C107-11** (cycle-2 trace discipline;
mirrors C107-5 for cycle 2). Each carries its falsifier
and its does-not-establish line in claims.md; their
bundle of record is the package's claims.json — the
package's second bundle file, on the Spec 097 precedent
(that package's claims were intaken from two bundle
files). A bundle file once intaken is never amended:
the ledger mirrors each bundle by the SHA-256 recorded
at its intake, so cycle 2's claims enter through a new
bundle path, and aee-claims.json (C107-1..C107-6) stands
exactly as intaken in 2026-11-26. C107-1 (the loop as
filed) and C107-6 (kill criteria at every cycle close)
already govern cycle 2 by their terms.

Test cases added: **TC-107-07** (I-2 conformance),
**TC-107-08** (C-E-15 decision conformance),
**TC-107-09** (E-2 conformance, or non-execution
conformance on STOP), **TC-107-10** (M-2 conformance,
including the calibration STOP-gate and the no-Otten-byte
condition), **TC-107-11** (cycle-2 trace discipline),
**TC-107-12** (kill-criteria evaluation for cycle 2).
TC-107-01 is re-run over the amended package at this
registration.

## 8. Execution discipline (all cycle-2 work)

Execution on tower-compute only, under
`~/.syncyard/worktrees/glossa/`; every job emits periodic
timestamped progress indicators with countable work done
against total. Raw outputs are saved to dated files in
the Spec 107 package's records (custody bytes never
committed). Deviations from this registration are
recorded as deviations with their reasons in the outcome
records, never silently absorbed. No standing moves
beyond §3, §5, and §6's registered effects; a
claim-standing change requiring the owner's adjudication
is reported as ready for adjudication, not applied.
