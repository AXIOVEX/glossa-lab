# Spec 109 — Stage 1 Preflight Record (T101)

**Date:** 2026-11-27. **Stage:** Stage 1 — the shared
conformance preflight of registration
`records/registration-2026-11-27.md` §2, executed for
the Indus generators (Part 1 assignment search, Part 2
structure induction, Part 3 context channel — the three
share this harness; Parts 4 and 5 run their own
preflight clauses at their stages, per spec.md §10).
**Execution:** `records/stage-1-preflight-harness.py`
(SHA-256 `f4e84285…`, 51,362 bytes), run on
tower-compute 2026-11-27; raw output at
`records/stage-1-preflight-raw-output.json` (custody
original SHA-256 `dd5fc76d…`); synthetic corpora and
intermediates in custody under `glossa-custody/spec109/`
(pins at §7). **No undeciphered-system output was
produced or scored anywhere in this stage.**

**Verdicts (mechanical, over the figures at §5;
TC-109-02 recomputation at the stage-close record):**

| Generator | Verdict | Licensed for Stage 2+ work |
|---|---|---|
| G1 — Part 1 assignment search | **FAILED** (clause i) | No — Stage 3 blocked until a revised generator passes under a new registration |
| G2 — Part 2 structure induction | **FAILED in part** (segmentation; partials control) | Positional classes and the numerical family only |
| G3 — Part 3 context channel | **PASSED** | Yes — Stage 2, under its registered cap and label |

The preflight as a whole additionally carries the
registered positional limitation of §4: positional
recovery on the Latin and Meroitic controls is NOT
MEASURABLE, and no positional figure is claimed from
them anywhere in this record.

## 1. The harness as built

Five synthetic replications (seeds
`spec109-s1-synth-{1..5}`; replication 4's first build
was rejected by the admission gates below and rebuilt
under seed `spec109-s1-synth-4-try1`, which is the seed
of record for that replication). Each corpus is built
to the Indus profile exactly — 1,670 artifacts (one
sequence each), 7,002 tokens, the empirical length
multiset of the Spec 105 custody datasets (lengths
2–8: {2:269, 3:330, 4:415, 5:330, 6:164, 7:116, 8:46};
multiset SHA-256 `146998f1…`, as recomputed by the
clause (iii) re-run's shape check), duplication exactly
d = 20/1670 (1,650 distinct sequences, 20 equal-length
copies) — with planted structure in value space,
ciphered to signs by a seeded permutation: 60 syllable
values with planted roles (8 openers, 8 closers, 12
site-conditioned context values, 9 affix values forming
the planted partials P1/P2/S1/S2, 23 stem values forming
400 planted stems); sequences composed as [prefix?]
[opener?] core (1–2 stems) [closer?] [suffix?], with
planted word boundaries at every join; 60 counted
sequences per corpus carrying a run of 2–5 repetitions
of one of 5 numeral signs. A value-side family corpus
(4,000 sequences, same grammar) supplies the predictor
weights in the frozen predictor form (Spec 105 Stage 6
§5 weighting, Spec 107's scorer form). The split is
duplicate-aware (distinct sequences by first-appearance
ordinal, ordinal % 5 == 4 to the synthetic holdout).
Three anchors are revealed to the search, mirroring the
register's 3 E-standing anchors. A corpus is admitted
only if its profile gates hold exactly and the two
ground-truth constructions of §3 agree; a disagreement
on an admitted corpus is a preflight STOP (none
occurred; one build was rejected at admission, above).

The generators under test are the registered designs in
miniature: G1 = constraint propagation (anchors fixed;
positional admissibility from G2's ρ = 0.95 detection:
a sign detected initial-restricted may take only values
whose family initial share ≥ 0.95, final likewise; where
detection made a pool infeasible the restriction was
relaxed for the excess signs and the relaxation is
filed per replication in the raw output — 1–3 signs per
replication) plus simulated annealing (25 restarts ×
80,000 swap steps, geometric temperature 30 → 0.1;
restart 0 frequency-initialized, restarts 1–24 random
admissible) optimizing the duplicate-aware
cross-validated predictive log-likelihood under the
frozen form — computed exactly, since with weights
fixed on the value side the fold scores sum to the full
derivation score. G2 = the four induction families of
registration §3 as mechanized in the harness header
(positional shares at ρ = 0.95/0.90, floor 5; the
segmentation boundary rule of §2 below; recurrent
partials at frequency ≥ 5; the numerical run checks).
G3 = the context term of registration §4 in per-sign
form, with its label-permutation null (B = 999, within
length strata).

## 2. Development findings (filed, with their remedies)

The harness was developed against a smoke replication
before the filed run; three findings changed the build,
and all three are findings about the harness and the
planted grammar, not about the floors, which were not
moved:

1. **Exchangeable edge values.** In the first planting,
   opener, closer, and context values were drawn
   uniformly with no individual co-occurrence signature;
   the search then recovered stems 20/20 and affixes 9/9
   but edge roles 3/28, and the found assignment scored
   *above* the planted truth on the objective
   (−16,158.0 vs −16,280.5 nats): the edge values were
   unidentifiable in principle. Remedy, in the planting:
   every edge value carries its own preferred stem
   subset, in the corpus and the family corpus alike —
   as in any real system, where a value's identity is
   its distribution.
2. **Label-invariant margins.** The first margin
   construction trained the predictor on the mapped
   derivation; every permutation then scores identically
   and the penalized margin came out identically the
   null's (−114.0 nats = −2 × 57 exactly). Remedy: all
   margin scoring is under the fixed value-side family
   predictor, the same asymmetry the search objective
   uses.
3. **Segmentation mechanization.** The registered
   statistics (adjacent-pair MI; boundary entropy) were
   mechanized in every faithful form the development
   run tried — PMI < 0 (F1 0.205), PMI below the corpus
   median (0.574), PMI below the sequence mean (0.628),
   the local-minimum forms (0.485–0.618), type-level
   successor entropy (0.595), string-level Harris
   branching (0.585–0.616), and the pairwise
   combinations (0.528–0.599). The family plateaus at
   F1 ≈ 0.55–0.63 on this profile; the harness files
   the strongest faithful form (PMI below the
   sequence's own mean pair PMI) and the filed run's
   result (§5) is what it is. A fourth, minor finding:
   counted runs planted at lengths 1–5 put the
   numerical run-token ratio exactly at its 0.80
   threshold (recovery 0.800 by construction artifact);
   runs are planted at 2–5.

## 3. Two-implementation agreement (clause c)

Every ground-truth set was produced twice: the
positional restricted set from the planted role lists
and independently from the value-space corpus by the
Spec 107 ground-truth construction (≥ 20 occurrences,
share ≥ 0.99) — exact agreement on all five admitted
corpora. Every recovery figure was computed by two
independent implementations inside the harness
(asserted equal at computation; a disagreement raises
and stops the run — none occurred), and every margin
figure by Spec 107's two scorers (agreement to 1e-9
per token, asserted per figure, the null's 999 margins
included). TC-109-02 then recomputed the filed figures
from the custody corpora independently: 38/38 checks
pass (stage-close record).

## 4. Clause (iii) — the deciphered controls, and the positional limitation carried on the face

Spec 107's filed I-2 execution was re-run unchanged in
this stage (raw output in custody, SHA-256
`526fe7f9…`). At 1×, medians over 20 replications, in
the R1 predictor form: **Meroitic RIGHT 0.6822 /
WRONG −0.0438 / SHUFFLE 0.2263; Latin RIGHT 0.4338 /
WRONG −0.5388 / SHUFFLE 0.1019** — RIGHT above WRONG
and SHUFFLE for both donors, reproducing cycle 2's
filed figures to four decimals. **Clause (iii)
PASSES** for the shared predictor the three Indus
generators score under. The run's own preflight gates
passed (target shape exact; duplication exact in
120/120 replications), its donor evaluations are
POSITIVE for both donors, and its test verdict is
INDETERMINATE — the registered configuration, R1
positive with R2 measurable for neither donor.

**The positional limitation, restated as registered:**
the re-specified positional ground-truth sets for
these controls hold **1 mark (Meroitic: *a*, initial,
at both ρ levels) and 0 marks (Latin)** against the
measurability floor of 5 — reproduced in this stage's
re-run (its `ground_truth_r2` is exactly {a: initial}
and {}). Positional recovery on the Latin and
Meroitic controls is therefore NOT MEASURABLE, no
preflight record of this study may claim a positional
figure from them, and none here does: the preflight's
positional clause ran on the synthetic corpora of
clause (a), whose ground truth is planted above the
floor by construction.

Control pins: Kovetsky inscriptions source SHA-256
`1e91e3a0…` (commit `145af083…`); Latin bytes (Caesar,
Gutenberg 218) SHA-256 `84ac8411…`, 169,899 bytes,
from Spec 107 custody; Spec 105 custody datasets
`indus-derivation.json` SHA-256 `84476daa…`,
`indus-reserve.json` SHA-256 `bfbe79cb…`.

## 5. Results per generator per clause

Floors (registration §2, as fixed in the harness
before the filed run): recovery clauses at median
≥ 0.80 across the 5 replications; the margin clause
clears in the median replication (per-replication
pass: penalized margin ≥ 10 nats and above the null's
99th percentile); a shuffle/control recovery at or
above half the true recovery fails the control clause.

### G1 — Assignment search (Part 1)

| Rep | Recovery (i) | Shuffle rec. | Penalized margin (nats) | Null p99 | Margin pass |
|---|---|---|---|---|---|
| 1 | 0.825 (47/57) | 0.281 | 999.7 | −525.0 | yes |
| 2 | 0.772 (44/57) | 0.018 | 933.2 | −525.4 | yes |
| 3 | 0.702 (40/57) | 0.088 | 853.6 | −492.9 | yes |
| 4 | 0.789 (45/57) | 0.333 | 1,120.7 | −479.2 | yes |
| 5 | 0.614 (35/57) | 0.246 | 837.9 | −546.6 | yes |
| **Median** | **0.772** | 0.246 | 933.2 | — | **5/5** |

- Clause (i) recovery: **FAILED** — median 0.772 below
  the 0.80 floor, with a wide per-replication spread
  (0.614–0.825).
- Clause (ii) margin: **PASSED** — 5/5 replications,
  median penalized margin 933.2 nats against null
  99th percentiles near −500.
- Shuffle control: **PASSED** — 0.246 < 0.5 × 0.772.
- **Verdict: FAILED.** The anatomy matters and is
  filed: where the search converges, its candidate is
  discriminated by ~900 nats — the objective identifies
  the planted truth decisively — but the annealing
  search itself is unreliable across corpora at this
  design (restarts, schedule, swap moves as built).
  The failure is a search-reliability failure, not an
  identifiability failure. Under the kill discipline
  the floor stands; the generator's design is what a
  new registration revises (candidate directions the
  record supports: stronger move sets or an
  EM/refinement stage, more restarts, schedule
  redesign — each a new registration's to register,
  none improvised here). **G1 produces no scoreable
  output; Stage 3 does not run on this generator.**

### G2 — Structure induction (Part 2)

| Family | Recovery per rep | Median | Floor | Shuffle median | Control | Clause |
|---|---|---|---|---|---|---|
| Positional (ρ=0.95) | 1.000 ×5 | 1.000 | 0.80 | 0.000 | pass | **PASSED** |
| Positional (ρ=0.90) | 1.000 ×5 | 1.000 | (filed) | — | — | filed |
| Segmentation (F1) | 0.570/0.573/0.551/0.569/0.567 | 0.569 | 0.80 | 0.443 | **fail** | **FAILED** |
| Recurrent partials | 1.000 ×5 | 1.000 | 0.80 | 0.500 | **fail** | **FAILED (control)** |
| Numerical | 1.000/1.000/1.000/0.800/0.800 | 1.000 | 0.80 | 0.000 | pass | **PASSED** |

- Positional classes: **PASSED** at both ρ levels,
  no false restriction surviving its control.
- Segmentation: **FAILED** on both its clauses —
  recovery 0.569 at the floor, and the statistic
  fires on shuffled material at 0.443, which is 78%
  of its true rate and far above the control bound
  (kill criterion 3's form: the pipeline substantially
  measures itself). The registered MI/boundary-entropy
  statistics, in every faithful mechanization tried
  (§2), do not recover planted segmentation at this
  profile. The family is closed as filed; a revised
  segmentation design is a new registration.
- Recurrent partials: recovery **PASSED** (1.000 in
  every replication) but the shuffle control **FAILED
  at the boundary**: control recovery median 0.500
  against the required < 0.500 (per replication
  0.250/0.750/0.750/0.500/0.500). The mechanism is
  filed: the frequency-≥5 extraction threshold is
  within reach of chance co-occurrence of the
  high-frequency affix signs on shuffled material, so
  the extraction as built cannot distinguish its true
  yield from its shuffle yield at the registered
  control form. The family is not licensed on this
  preflight; its revision (a threshold or a
  significance form stated against the shuffle
  distribution) is a new registration.
- Numerical/metrological: **PASSED** (median 1.000;
  the two 0.800 replications each miss one of five
  planted numeral signs; control 0.000).
- **Licensing: G2 is licensed for Stage 2 for its
  positional-class and numerical output kinds only.
  Its segmentation and recurrent-partial families
  produce no scoreable output until revised
  generators pass under new registrations.** (The
  registration's verdict rule speaks of generators;
  this record applies its licensing per output kind,
  as the registration's own NOT MEASURABLE IN PART
  clause does, and as this stage's commission
  directs. The tension is noted, not hidden.)

### G3 — Context channel (Part 3)

Recovery 1.000 (12/12 planted context signs) in every
replication; label-permutation control 0.000 in every
replication; median statistic positive in the planted
direction throughout. **Verdict: PASSED** — licensed
for Stage 2, its term entering scoring only under
registration §4's cap (its own null's 99th
percentile) and carrying the no-iconography label.

## 6. What this stage licenses, and what it does not

Stage 2 (T201/T202) may proceed for: Part 2's
positional-class induction and numerical/metrological
family, and Part 3's context channel (joins, term,
null, out-of-site validation as registered). Stage 2
may NOT execute Part 2's segmentation or
recurrent-partial families on the corpus under this
preflight, and Stage 3 may not run Part 1's search.
Parts 4 and 5 are untouched by this stage: their
preflight clauses run at their stages as registered.
Nothing in this stage scored, ranked, or produced any
output on any undeciphered system; no standing,
verdict, or tally in any program moved.

## 7. Provenance and pins

- Harness: `records/stage-1-preflight-harness.py`,
  SHA-256 `f4e84285d38f39f25d46547d9d435a32ad46506513b588ae061be7a974bc3485`.
- Raw output: custody
  `glossa-custody/spec109/stage-1-preflight-raw-output.json`,
  SHA-256 `dd5fc76dba3e096e336ba24c63d7f1f416ef5c2babdac8189ef9f4f478c8315b`;
  a byte-identical copy is filed in this records
  directory.
- Synthetic corpora (custody, never committed):
  rep1 `0752da62…`, rep2 `f4a78a70…`, rep3
  `c61bb9ec…`, rep4 `ae78c5ac…`, rep5 `6dc2fc7d…`
  (full hashes in the stage-close record's custody
  table and reproducible from the filed seeds).
- I-2 re-run raw output: custody
  `glossa-custody/spec109/i2-rerun-raw-output.json`,
  SHA-256 `526fe7f96f65973766f26e623a1a046ae5ad1fdc8bb87f699dcbf3182f17dfa9`.
- Seeds: corpus seeds as §1; per-replication derived
  seeds (search restarts, shuffle controls, nulls) are
  constructed from them in the harness as filed.
- Payload verdicts: harness run exit 0 with the
  verdict block above as its output; I-2 re-run exit
  0, verdict INDETERMINATE as §4; TC-109-02 exit 0,
  PASS 38/38 (stage-close record).

**AI disclosure:** executed by an AI agent (Muse, via Muse)
at the direction of Tristen Pierson, per constitution sec. VI.
