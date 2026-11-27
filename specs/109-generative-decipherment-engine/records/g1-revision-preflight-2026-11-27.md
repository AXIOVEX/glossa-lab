# Spec 109 — G1 Revision Preflight Record (T102)

**Date:** 2026-11-27. **Scope:** the re-preflight of the
revised assignment-search generator (design G1-R) under
`records/g1-revision-registration-2026-11-27.md`, judged
under registration §2's clauses (i) and (ii) and the
shuffle control at the Stage 1 floors, on five fresh
synthetic corpora. **Execution:**
`records/g1-revision-harness.py` (SHA-256 `a15c8c57…`,
21,556 bytes), run on tower-compute 2026-11-27
(21:51–22:06 UTC); raw output at
`records/g1-revision-raw-output.json` (SHA-256
`a8209ce0…`; byte-identical to the custody original);
corpora and intermediates in custody under
`glossa-custody/spec109/g1-revision/run/` (pins at §5).
The harness imports the filed Stage 1 harness
(SHA-256 `f4e84285…`) for the corpus construction, the
objective, the scorers, the margins, the null, and the
recovery computation; only the search is new code.
**No undeciphered-system output was produced or scored
anywhere in this run.**

**Verdict (mechanical, over the figures at §3;
TC-109-02 recomputation at the close record):**

| Generator | Verdict | Licensed for Stage 3 |
|---|---|---|
| G1-R — Part 1 assignment search, revised | **FAILED** (clause i) | No — Stage 3 remains blocked; G1 produces no scoreable output |

Clause (ii) passed 5/5 and the shuffle control passed;
the failure is clause (i) alone, as Stage 1's was. The
floor was not moved, and no second revision is
commissioned by the amendment.

## 1. The run as executed

Five fresh corpora, seeds `spec109-s1r-synth-{1..5}`;
replication 5's first build was rejected by the
admission gates and rebuilt under
`spec109-s1r-synth-5-try1`, the seed of record for that
replication. Each corpus is built to the Indus profile
exactly (1,670 artifacts, 7,002 tokens, the empirical
length multiset, duplication exactly 20/1670), admitted
only if the profile gates hold and the two ground-truth
constructions agree (they did, on all five admitted
corpora). The search per replication: constraint
propagation identical to Stage 1 (anchors fixed;
admissibility from G2's ρ = 0.95 detection on the
derivation; relaxations filed per replication in the
raw output — 2 signs per replication), then 40 restarts
× 160,000 steps of annealing with swaps (p = 0.7) and
3-cycle rotations (p = 0.3) under exact deltas,
geometric schedule 30 → 0.05 with one reheat to 10 at
step 80,000, each restart's best-visited state
swap-polished to a local optimum; the candidate is the
best polished state. The harness's internal gate ran
before the search: the 3-cycle delta agreed with full
rescoring on 200/200 random triples. The shuffle
control is the identical revised pipeline on the
shuffled derivation, per replication.

## 2. Clause (iii) and the positional limitation

Clause (iii) was not re-run, as the amendment
registers: the predictor form and the scorers are
unchanged from Stage 1, whose clause (iii) PASS stands
for the shared predictor (Meroitic RIGHT 0.6822 /
WRONG −0.0438 / SHUFFLE 0.2263; Latin 0.4338 / −0.5388 /
0.1019, reproduced there to four decimals). The
positional limitation is restated as registered:
positional recovery on the Latin and Meroitic controls
is NOT MEASURABLE (re-specified ground-truth sets of 1
mark and 0 marks against the floor of 5), no positional
figure is claimed from them here, and G1's clauses in
this run are assignment recovery on the synthetic
corpora, whose truth is planted above the floor.

## 3. Results per clause

| Rep | Seed | Recovery (i) | Shuffle rec. | Penalized margin (nats) | Null p99 | Margin pass |
|---|---|---|---|---|---|---|
| 1 | spec109-s1r-synth-1 | 0.632 (36/57) | 0.175 | 1,004.7 | −520.8 | yes |
| 2 | spec109-s1r-synth-2 | 0.684 (39/57) | 0.088 | 983.2 | −487.2 | yes |
| 3 | spec109-s1r-synth-3 | 0.807 (46/57) | 0.088 | 990.1 | −495.9 | yes |
| 4 | spec109-s1r-synth-4 | 0.737 (42/57) | 0.175 | 966.0 | −481.0 | yes |
| 5 | spec109-s1r-synth-5-try1 | 0.772 (44/57) | 0.298 | 1,017.5 | −533.1 | yes |
| **Median** | | **0.737** | 0.175 | 990.1 | — | **5/5** |

- Clause (i) recovery: **FAILED** — median 0.737 below
  the 0.80 floor (per-replication spread 0.632–0.807).
- Clause (ii) margin: **PASSED** — 5/5 replications,
  median penalized margin 990.1 nats against null 99th
  percentiles near −500.
- Shuffle control: **PASSED** — median 0.175 < 0.5 ×
  0.737.
- **Verdict: FAILED.** G1-R is not licensed; Stage 3
  does not run on this generator.

## 4. Anatomy of the fresh run (post-hoc, from the custody truths)

Measured after the verdict, filed so the next design
starts from evidence rather than from the summary:

- **No basin failure occurred on any fresh corpus.**
  The candidate's objective exceeds the planted truth's
  on all five replications, by +57.2 / +25.3 / +24.0 /
  +20.0 / +34.1 nats. The mechanism-B defect the
  revision targeted (Stage 1's replication 5: best found
  497.7 nats below truth, at a swap-local optimum) is
  repaired, and the repair held on fresh material.
- **The binding constraint is the plateau, on fresh
  material as on the Stage 1 corpora.** Candidates that
  beat the planted truth's objective by 20–57 nats miss
  21 / 18 / 11 / 15 / 13 of 57 signs, and the misses are
  again exclusively edge values — closers 8/6/5/4/8,
  context values 9/10/2/7/5, affixes 4/0/4/4/0, openers
  0/2/0/0/0, stems 0 in all five. At this profile the
  objective's near-optimal region contains assignments
  differing from the truth on a fifth to a third of the
  edge values, and recovery — a per-sign count — prices
  exactly those directions. No search over this
  objective recovers information the objective does not
  carry; the floor of 0.80 sits above the level the
  objective identifies at 1× scale.
- Against Stage 1's draw, the revised search's median
  (0.737 over this draw) and the filed search's median
  (0.772 over its draw) are two draws of a
  high-variance quantity (per-corpus ranges 0.632–0.807
  and 0.614–0.825); on the one corpus where the filed
  search failed by basin (Stage 1 replication 5), the
  revised search in development recovered 0.807. The
  revision's evidenced effect is reliability of
  basin-finding, not a higher plateau level, and the
  record does not claim more for it.

## 5. Provenance and pins

- Revision harness: `records/g1-revision-harness.py`,
  SHA-256 `a15c8c578b0599b3ab6b44564361d191b8375028fbb43ee3ad6e0a6f63cdb15a`.
- Raw output: custody
  `glossa-custody/spec109/g1-revision/run/raw-output.json`,
  SHA-256 `a8209ce0533f82e3df6017711f0c65dffed000a065bbe0708bcbc8c3dd1b3b71`;
  a byte-identical copy is filed in this records
  directory.
- Synthetic corpora (custody, never committed):
  rep1 `d8e205d1…`, rep2 `8dd2d2c7…`, rep3 `f6500fe5…`,
  rep4 `4ecdc958…`, rep5 `839a0524…` (full hashes in the
  close record's custody table; reproducible from the
  filed seeds).
- Amendment registration:
  `records/g1-revision-registration-2026-11-27.md`,
  carrying the diagnosis, the design, the claim
  determination, and the verdict rule this run executed.
- Payload verdict: harness run exit 0 with the verdict
  block above as its output (the run's own verdict is
  FAILED, clause (i)); TC-109-02 verification exit 0,
  PASS 45/45 (close record).

**AI disclosure:** executed by an AI agent (Muse, via Muse)
at the direction of Tristen Pierson, per constitution sec. VI.
