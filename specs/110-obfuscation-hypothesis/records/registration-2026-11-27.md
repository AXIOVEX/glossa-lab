# Spec 110 — Registration (2026-11-27)

The full registration of the deliberate-obfuscation
battery: statistics, directions, threshold derivation,
nulls, floors, the control gate, verdict rules, and
kill criteria, frozen before any run. The directive
and hypothesis are as spec.md states them. Where this
record and spec.md differ in any figure, this record
governs.

## 1. Common machinery

- A **corpus** is a list of sequences; a sequence is a
  list of tokens (signs) in reading order. Within-
  sequence bigrams only; no bigram crosses a sequence
  boundary.
- **Nulls.** Every permutation null runs B = 999 draws
  under seed **11001** (per-test seed derived as
  11001 + test index, filed in the raw output).
  Percentiles are the empirical ranks of the draws.
- **Two implementations.** Every headline statistic is
  computed by the harness and recomputed by the
  independent verification script (TC-110-02,
  TC-110-03) from the filed raw tables; the verdicts
  are the mechanical consequence of the registered
  rules over the recomputed figures.
- **Progress.** Every run emits timestamped, countable
  progress lines (corpora built, statistics computed,
  null draws completed) to its run log in custody.

## 2. Statistics (per corpus)

Let V be the inventory size, N the token count,
c(s) the count of sign s, p(s) = c(s)/N.

- **A1 — normalized unigram entropy.**
  H = −Σ p(s) log2 p(s); A1 = H / log2(V).
- **A2 — top-sign share.** A2 = max c(s) / N.
- **A3 — conditional-entropy ratio.** Over all
  within-sequence bigrams (x, y): H2 = −Σ p(x,y)
  log2 p(y|x); A3 = H2 / H.
- **A4 — bigram mutual information.** A4 = H − H2
  (bits).
- **B — stratum divergence.** For strata with sign
  profiles p_i (over the corpus inventory): the
  omnibus statistic is the token-weighted mean
  pairwise Jensen–Shannon divergence (base 2) over
  strata meeting the floor.
- **C2 — cross-part permutation.** Parts P and Q (two
  strata, or two halves of one corpus by seeded
  alternating split, seed 11001). For each sign, a
  label-free feature vector: (log frequency share;
  initial, medial, final position shares; successor
  entropy; predecessor entropy; context diversity =
  distinct successors + distinct predecessors, log).
  Features standardized over the union inventory.
  Matching: greedy mutual-best assignment on cosine
  distance, then swap polish minimizing the JSD
  between Q's profile mapped through the candidate
  permutation and P's profile (at most 200 polish
  passes). Statistics: **gain** = JSD(identity) −
  JSD(best); **self-agreement** = share of Q signs
  mapped to the identically-labelled P sign (over
  signs present in both parts); **stability** = two
  independent split resamples (seeds 11002, 11003)
  recover mappings whose agreement with the primary
  mapping is measured over shared signs.
- **D — inventory.** V; **hapax-type share** = (types
  with c(s) = 1) / V; **hapax-token share** = (types
  with c(s) = 1) / N; and V against a size-matched
  band (§3).

## 3. Bands and thresholds (controls only)

- **Natural-control sample set.** (i) Five synthetic
  natural corpora at the Indus profile, built by the
  Spec 109 Stage 1 harness machinery (pin
  `f4e84285…`) under seeds `spec110-nat-{1..5}`;
  (ii) the Latin control in four quarter samples;
  (iii) the Meroitic corpus in three samples (whole,
  first half, second half) — used only in its control
  role for the Indus and Eteocypriot bands, never in
  Meroitic's own band (leave-target-out, §5).
- **Family A / C1 band.** For each statistic, the band
  is [min, max] over the applicable control samples.
  Leave-one-out for the gate's false-positive leg:
  each control sample is scored against the band of
  the remaining samples.
- **Family B baseline band.** The omnibus JSD of the
  synthetic natural corpora under their planted site
  split (the builder's site mechanism), 5 values;
  baseline max is the band edge.
- **Family C2 natural band.** The gain and
  self-agreement of the natural control samples under
  split-half C2 (synthetic reps and Meroitic halves;
  Latin quarters paired), band = range over samples.
- **Family D size-matched band.** For a target of N
  tokens: 20 subsamples of the synthetic natural
  corpora drawn to N tokens (whole sequences, seeded),
  giving bands for V and hapax-type share at that N.

## 4. The control gate (all legs must pass)

Transformations, applied to the five synthetic natural
corpora (seeds `spec110-ctl-{1..5}`, built by the same
machinery):

- **T-HOM** — homophonic expansion: each of the 10
  most frequent signs is split into 2 variant labels;
  its tokens are reassigned to the variants by seeded
  coin flip.
- **T-POLY** — polyalphabetic substitution: sign
  labels permuted by sequence-position mod 3 (three
  seeded permutations).
- **T-SUB-D** — differential substitution: one planted
  site stratum (or, for the C2 leg, the second split
  half) is rendered under one seeded fixed permutation
  of the sign labels.
- **T-SUB-U** — uniform substitution: the whole corpus
  under one seeded fixed permutation.

Gate legs (detection counts over the 5 replications):

- **G-A.** Family A fires the flattening pattern on
  T-HOM in ≥ 4/5; fires the structure pattern on
  T-POLY in ≥ 4/5.
- **G-B.** Family B fires on T-SUB-D (site form) in
  ≥ 4/5.
- **G-C.** Family C2 detects T-SUB-D (half form) in
  ≥ 4/5, with the recovered mapping inverting the
  planted permutation on ≥ 0.80 of shared signs in
  each detecting replication; C1 fires (structure
  destroyed) on T-POLY in ≥ 4/5.
- **G-D.** Family D fires on T-HOM in ≥ 4/5.
- **G-INV.** On T-SUB-U, no family fires in ≥ 4/5
  replications (the invariance leg of spec.md §2).
- **G-FP.** On the natural controls, each family fires
  on at most 1 sample under leave-one-out bands
  (family B: on at most 1 of the 5 synthetic natural
  site splits).

If any leg fails, the battery has failed: the failure
is filed, the real-corpus runs are NOT scoreable, and
the study stops (kill criterion 1). Thresholds are
never adjusted after the gate runs; a failed gate is
a finding about the battery.

## 5. Verdict rules (per corpus per family)

Floors first: a family whose floor is unmet returns
**NOT TESTABLE AT THIS POWER** with the census that
shows it.

- **Family A** (floor N ≥ 1,000). PRESENT if the
  flattening pattern (A1 above band AND A2 below
  band) or the structure pattern (A3 above band AND
  A4 below band) holds in full. ABSENT otherwise; a
  single-statistic excursion is filed as an excursion,
  not a pattern.
- **Family B** (floors: ≥ 2 strata, each ≥ 300 tokens
  and ≥ 30 texts). PRESENT if the omnibus JSD exceeds
  its label-permutation null's 99th percentile AND
  exceeds the genre-baseline band max. ABSENT if at or
  below the null's 99th percentile; ABSENT with the
  excursion filed if above the null but at or below
  the baseline band.
- **Family C** (floors: C1 as family A; C2: each part
  ≥ 500 tokens and ≥ 20 shared signs). PRESENT if C2
  fires on at least one registered part pair (strata
  pair, or split-half): self-agreement < 0.50, gain
  above the natural C2 band max, and stability ≥ 0.80
  across the two resamples. ABSENT if C2 fires on no
  pair and C1's structure statistics are within band.
  If C1's structure statistics fall outside band in
  the destruction direction while C2 does not fire,
  the verdict is PRESENT under the structure pattern,
  cross-filed with family A. The registered limit of
  spec.md §2 stands: a uniform whole-corpus
  substitution is NOT TESTABLE by this family, by
  construction, and no ABSENT verdict in this family
  speaks to that class.
- **Family D** (floor N ≥ 1,000). PRESENT if V is
  above its size-matched band AND hapax-type share is
  above its band. ABSENT otherwise; single excursions
  filed.

## 6. Corpora and handling (pins)

- **Synthetic natural corpora.** Spec 109 Stage 1
  harness (SHA-256 `f4e84285…`), Indus profile
  (1,670 artifacts / 7,002 tokens target profile,
  empirical length multiset), seeds as §3–§4 state.
  The sequences used are the harness's sign sequences.
- **Indus.** Custody `glossa-custody/spec105/
  indus-derivation.json`, SHA-256
  `84476daa3a1d9ded33ee7c3eeaffb29fac0290ecf3507873206d4d60ac8b948b`
  (1,336 artifacts, 5,611 tokens). Site join: tracked
  `outputs/phase100_full_corpus.json`, SHA-256
  `c2b14e94971f438cfd25f24123db975de6c02980e0e425cffb91fbc4de4d578c`,
  matched by exact flattened sequence; sequences with
  conflicting sites are excluded from family B and
  counted. The 109 reserve is not used (D-110-5).
- **Eteocypriot.** `specs/096-eteocypriot-program/
  corpus/corpus.json`, SHA-256
  `2954283d6250…` (full hash in the raw output).
  Corpus = inscriptions with stratum
  `primary-amathus`; sequences from
  `eteocypriot_lines` segments (and the
  `eteocypriot_side` of the Androkles pair in the same
  segment form); the `[sa]` bracketed token is carried
  as its own sign, the `?` token is carried as its own
  sign — both handlings registered here, applied
  uniformly, and their token counts filed. The Greek
  control inscription (ICS 217) is not part of the
  corpus.
- **Meroitic.** Custody
  `glossa-custody/spec105/meroitic.json`, SHA-256
  `a8f551e5cc52…` (full hash in the raw output);
  376 texts. The `.` token (damage / unreadable
  marker) is excluded from all sequences before any
  statistic; sequences left empty are dropped and
  counted.
- **Latin.** Custody `glossa-custody/spec107/
  de-bello-gallico-gutenberg-218.txt`; sequences =
  whitespace-delimited words as letter sequences,
  letters a–z only, lowercased; four quarter samples
  by word order.

## 7. Execution order

1. Registration and claims intake (the cascade).
2. Harness build; synthetic corpora; transformations.
3. Control gate (§4). On failure: file and stop.
4. Real-corpus runs (Indus, Eteocypriot, Meroitic),
   per family, verdicts by §5.
5. Independent verification (TC-110-02, TC-110-03),
   trace (TC-110-04), kill evaluation (TC-110-05),
   close record.

## 8. Information and standing

This study consumes no new external information; it
measures the program's held corpora against controls
built from the program's own machinery and one public
-domain control text. Its PRESENT verdicts are
candidate findings for the existing gates. Its ABSENT
verdicts are bounded by the floors and by §2's
invariance limit, both stated wherever the verdicts
are filed. No part of this study converts its own
output into a standing.

## 9. Kill criteria

The study-level criteria of spec.md §7 apply verbatim.
Per-family instances: gate failure (criterion 1)
closes the whole battery; a family's success on its
natural control beyond the G-FP rate (criterion 2)
closes that family.
