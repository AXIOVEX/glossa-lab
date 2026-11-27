# Spec 109 — G1 Identifiability-Scale Study Registration (2026-11-27)

**Amendment to the registration of 2026-11-27, for one
generator only: G1, the Part 1 assignment search, in its
revised design G1-R.** Filed under the discipline the
registration, C109-7, and spec.md §9 state in advance:
a negative search result is a finding about the search
and the information available; the program iterates on
design, never on the bar. Authorization: the owner's
discovery directive of 2026-11-27 ~13:54 ET and his
standing blanket approval for Glossa work of 2026-11-27
04:05 ET. This amendment registers a diagnostic study.
It licenses nothing, moves no floor, runs nothing on
the real corpus, and changes no generator design: the
generator, the objective, the admissibility
construction, the scoring rule, and the clause
structure are identical to the G1 revision amendment
(`records/g1-revision-registration-2026-11-27.md`),
and every figure is judged against the same floors
that amendment and registration §2 file.

## 1. The question

G1-R failed clause (i) of its re-preflight on five
fresh 1× corpora (`records/g1-revision-preflight-2026-
11-27.md`): median recovery **0.737** against the 0.80
floor, with no basin failure — its candidates beat the
planted truth's objective on all five corpora (+20.0
to +57.2 nats) while missing 11–21 of 57 scored signs,
exclusively edge values (stems 0 misses in all five).
The filed conclusion is that at the Indus profile's
1× scale the objective may not identify enough edge
values for any search over it to clear 0.80. Two
explanations are live, and they prescribe different
next designs:

- **(A) Information.** Identifiability is a function
  of corpus scale: recovery rises with scale and
  crosses the floor. The real corpus is fixed at 1×,
  so under (A) Part 1's blocker is information, and
  this study quantifies it — the recovery-vs-scale
  curve and the scale at which the floor is crossed.
- **(B) Objective design.** Identifiability stays
  below the floor even at scale: the objective's
  edge-value evidence is itself the defect, and an
  objective revision is the next design problem.

This study decides between them by running the
identical preflight at 2× and 4× the Indus profile's
scale, five replications each, on fresh synthetic
corpora. The 1× point of the curve is G1-R's filed
draw (median 0.737, seeds `spec109-s1r-synth-{1..5}`);
the Stage 1 filed search's 0.772 is a different
generator's draw and is context, not a curve point.
1× is not re-run. What "scale" can mean for this
profile turns out to be constrained by the planted
grammar's own combinatorics; §2 registers the two
accommodations that constraint forces, with the
arithmetic on the record, before any corpus is built
for the verdict.

## 2. Scale, defined (the only changes, all in corpus construction)

Scale k ∈ {2, 4} multiplies the extensive quantities
of the Indus profile, and nothing else:

- **Length multiset:** the empirical multiset with
  each length's count × k — 1,670k artifacts,
  7,002k tokens.
- **Duplication:** 20k copies imposed by the filed
  replacement mechanism (the rate d = 20/1670 held
  exactly).
- **Counted slots:** 60k (the proportion held).
- **Stem pools:** the length-3 pool scales to 100k
  (of 23³ = 12,167 possible stems; never binding).
  The length-2 pool **saturates**: a length-2 stem
  is a pair of the 23 stem values, so at most
  23² = **529** distinct length-2 stems exist; the
  filed 1× pool of 300 is a random 300-subset of
  those 529, and the scaled target min(300k, 529)
  is 529 at both study scales — the full pair
  inventory. No pool larger than the inventory it
  draws from can be registered, and none is.

Every intensive parameter is unchanged: the value
inventory (60 syllable values), the role partition
(8 openers, 8 closers, 12 context values, 9 affix
values, 23 stem values), the collocation signature
size (15 preferred stems per edge value), the
preference probabilities (0.7 opener preference,
6.0 closer weight), the Zipf exponent (0.7), the
sequence template, the anchors (3 stem values), and
the split rule (duplicate-aware, distinct sequences
by first-appearance ordinal, ordinal % 5 == 4 to the
reserve). **The family corpus is fixed at 4,000
sequences at every scale:** it is the frozen
predictor's value-side reference, not part of the
corpus whose scale is under study; scaling it would
confound corpus information with predictor sharpness.

**Distinctness at scale, and the fallback.** The
filed construction enforces distinctness per slot
by rejection sampling (500 attempts per slot) and
the filed 1× admission gate counts exactly 1,650
distinct sequences. At scale that gate is
combinatorially unattainable: a length-2 sequence
is a single length-2 stem, distinct length-2
sequences are therefore capped at 529, and length-2
demand is 269k — at 2× at least 9 sequences beyond
the cap, at 4× at least 547. The construction
therefore keeps the filed rejection loop and its
filed 500-attempt cap unchanged, and where a slot
exhausts them it accepts the next draw as a
**fallback**: the slot is recorded, the fallback
count F is filed per corpus, and every fallback
must occur at a length-2 slot — a fallback at any
other length would falsify the combinatorics filed
here and is a STOP. The distinct count is then a
measured quantity, not a gate: it is filed per
corpus together with the **effective scale**,
distinct / 1,650. All downstream machinery — the
duplicate-aware split, the objective, the margins,
the null — is the program's filed duplicate-aware
machinery, built for corpora whose duplication is
measured rather than assumed; the imposed 20k
copies above are additional to, and accounted
separately from, the fallback duplicates.

**Implementation.** The corpus is built by the Stage
1 harness's own `Language` and `build_corpus` code
(pin SHA-256 `f4e84285…`), executed from a source in
which exactly five textual substitutions carry this
section: `N_ART = 1670k`, `N_DUP = 20k`, the
counted-slot cap `60k`, the pool targets in their
saturation form `((2, 529), (3, 100k))`, and the
rejection loop's cap-exhaustion raise replaced by
the fallback acceptance above (which appends the
draw and records the slot in a FALLBACK_SLOTS list
the harness reads after each build). The study
harness asserts each substitution target occurs
exactly once in the filed source before replacing,
and stops if any assertion fails. Everything else
in the run — the objective, the scorers, the
margins, the permutation null, the recovery
computation, the positional detection, the split —
is the filed code of the Stage 1 harness at its
pin, and the search is the filed code of the G1
revision harness (pin SHA-256 `a15c8c57…`), whose
only adaptation is that its Stage 1 import is
directed at this worktree's byte-identical copy of
the filed Stage 1 harness (the pin is asserted
before any run).

## 3. Fresh material and seeds

Ten fresh synthetic corpora, seeds
**`spec109-scl2-synth-{1..5}`** at 2× and
**`spec109-scl4-synth-{1..5}`** at 4×, built and
admitted under the G1-R admission gates in their
scale form: profile exact at scale (the length
multiset); the two ground-truth constructions in
agreement; every value at ≥ 5 tokens; every
fallback at a length-2 slot, with F and the
distinct count filed; a rejected build rebuilt
under the `-try{n}` suffix and the seed of record
filed. Derived seeds are constructed from the
corpus seed exactly as the G1 revision harness
constructs them (`-g1r…` for the search,
`-g1rshuf…` for the shuffle control's search; the
shuffle, derangement, shuffled-assignment, and null
seeds as in Stage 1). The search budget is the
registered G1-R budget, identical at every scale
(40 restarts × 160,000 steps): if recovery rises,
it rises at fixed search effort, so the curve reads
as information, not as compute.

## 4. What is reported, per scale

Per replication: the seed of record; the fallback
count F, the distinct count, and the effective
scale; planted-value recovery (hits / denominator
— the denominator is 57 at every scale: the 60
signs less the 3 anchors, all carrying ≥ 5 tokens
by construction at scale); the shuffle-control
recovery; the penalized margin and the permutation
null's 99th percentile, with the clause (ii) pass
in the frozen form; the candidate's objective and
the planted truth's objective under the identical
objective construction, and their difference (the
objective gap); and the miss anatomy over the
scored signs — miss counts split stems vs edge
values, the edge values split openers / closers /
context / affixes. Per scale: the medians, the
clause (ii) outcome under the registered
median-replication rule, and the shuffle outcome
under the registered control form (median shuffle
recovery < 0.5 × median right recovery).

## 5. Decision rule (registered before any run)

**Anatomy intact at a scale:** stem misses = 0 in
every replication at that scale — the filed 1×
anatomy (stems 0 in all ten 1× replications across
both generators' draws).

- **(A) SUPPORTED** — median recovery at 4× ≥ 0.80,
  anatomy intact at 4×, and the shuffle control
  passes at 4×. The study record then files the
  recovery-vs-scale curve (1× 0.737 filed; 2× and
  4× measured here) and the implied information
  threshold as a bracket between measured points:
  the floor is crossed between the largest measured
  scale whose median is below 0.80 and the smallest
  whose median is at or above it, stated in nominal
  terms and in effective terms (each nominal
  point's median effective scale). No interpolation
  beyond the measured points is claimed.
- **(B) SUPPORTED** — median recovery at 4× < 0.80
  and median recovery at 2× < 0.80, with the shuffle
  control passing at both scales.
- **MIXED** — any of: median at 2× ≥ 0.80 but
  median at 4× < 0.80 (crossing at 2× but not 4×);
  median at 4× ≥ 0.80 with the anatomy not intact
  at 4× (the character of the misses changed); or
  the shuffle control failing at either scale. A
  shuffle failure voids that scale's recovery
  figure for the decision — a pipeline whose
  scramble recovery approaches its right recovery
  has measured itself (kill criterion 3's form),
  and the figure cannot be read as recovery — and
  the outcome is filed MIXED with the void named.

Clause (ii) is reported at both scales and is not
part of the decision: the question this study
answers is the identifiability of the assignment
under the objective, which clause (i) and the
anatomy measure; clause (ii) has passed 5/5 in both
1× draws by margins near a thousand nats and is not
the binding constraint under either explanation.

**What no outcome does.** No outcome licenses G1 or
G1-R, at any scale: a preflight verdict exists only
at the registered 1× profile, and G1-R's filed
FAILED state stands whatever this study finds. No
outcome runs or scores anything on the real corpus.
If (A) is supported, whether Part 1 proceeds on the
real corpus under a candidate-with-margins filing —
knowing the real corpus sits below the synthetic
identifiability threshold the curve measures — is a
separate registration question, which the study
record poses and does not answer. If (B) is
supported, the next design problem is the
objective's edge-value evidence, for a future
registration. The floor of 0.80 does not move under
any outcome.

## 6. Claim determination

No new claim is intaken for this amendment, and the
claims ledger does not move in its landing. The
basis, stated so it can be checked against the filed
texts: this study asserts no new proposition. It
measures the filed generator against the filed
floors on new synthetic material, under the
preflight discipline C109-7 registers; C109-2's
subject is Part 1's Stage 3 execution on the real
corpus under registration §5, which this study does
not touch and does not advance. TC-109-02, by its
own text the preflight conformance test re-run for
each later generator, is re-run in verification form
over this study's figures at the close. As with the
G1 revision amendment (§6 of its registration), a
new claim would assert a new proposition; this
amendment asserts none — it registers a measurement
under the claims as filed.

## 7. Kill-criteria posture (spec.md §9, pre-registered)

1. **Null yield at the frozen bar** — not engaged;
   it binds at Part 1's own stage over its
   candidates, which do not exist while the
   generator is unlicensed.
2. **Preflight failure** — not engaged by this
   study, which issues no licensing verdict; G1-R's
   fired state under this criterion stands.
3. **Control failure** — engaged only through §5's
   shuffle-void rule: a shuffle failure at a scale
   voids that scale's figure and files the outcome
   MIXED with the void named. It does not close
   Part 1, whose closure state is already filed.
4. **Gate dependence** — not engaged.
5. **Integrity tripwire** — standing; any breach
   halts the study on the program's rule.

## 8. Provenance

Study harness: `records/g1-scale-harness.py` (its
SHA-256 is carried in the raw outputs and the study
record). Raw outputs: `records/g1-scale-raw-output-
2x.json` and `records/g1-scale-raw-output-4x.json`,
byte-identical to the custody originals under
`glossa-custody/spec109/g1-scale/`; the synthetic
corpora and run logs are in custody there, never
committed, reproducible from the filed seeds. Every
figure in the study record is recomputed
independently by the TC-109-02 verification script
(`records/g1-scale-tc109-02-verification.py`) from
the custody corpora and the filed candidate
assignments. No undeciphered-system output is
produced or scored anywhere in this study.

**AI disclosure:** executed by an AI agent (Muse, via Muse)
at the direction of Tristen Pierson, per constitution sec. VI.
