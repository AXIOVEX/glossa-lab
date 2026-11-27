# Spec 109 — G1 Identifiability-Scale Study Record (T103)

**Date:** 2026-11-27. **Scope:** the identifiability-scale
study of the revised assignment-search generator (design
G1-R) under `records/g1-scale-registration-2026-11-27.md`:
the G1-R preflight — generator, objective, admissibility,
scoring, floors, and clause structure identical to the G1
revision amendment — run on five fresh synthetic corpora
at each of 2× and 4× the Indus profile's scale, to decide
between (A) information and (B) objective design as the
explanation of G1-R's clause (i) failure at 1×.
**Execution:** `records/g1-scale-harness.py` (SHA-256
`80663a03…`), run on tower-compute 2026-11-27 (2×:
22:36:32Z–22:51:24Z; 4×: 22:37:19Z–22:52:45Z); raw outputs
at `records/g1-scale-raw-output-2x.json` (SHA-256
`5e2b4deb…`) and `records/g1-scale-raw-output-4x.json`
(SHA-256 `1f4d2239…`), byte-identical to the custody
originals; corpora and logs in custody under
`glossa-custody/spec109/g1-scale/` (pins at §6). The
harness executes the filed Stage 1 harness's corpus
construction, objective, scorers, margins, null, and
recovery code (pin `f4e84285…`) with the amendment §2's
five registered scale substitutions, and the filed G1
revision harness's search (pin `a15c8c57…`). Development
validation, filed for provenance: before any study run,
the harness's anatomy and objective-gap code was run
against the G1 revision's custody corpora and filed
candidates and reproduced that record's anatomy exactly
(gaps +57.2 / +25.3 / +24.0 / +20.0 / +34.1 nats; misses
21 / 18 / 11 / 15 / 13; role splits cell-for-cell), and a
smoke build at each scale confirmed the §2 combinatorics
(fallbacks exactly 9 at 2× and 547 at 4×, the registered
minimum 269k − 529 in both cases). **No
undeciphered-system output was produced or scored
anywhere in this study.**

**Outcome (the amendment §5 decision rule, evaluated
mechanically over the figures at §2; TC-109-02
recomputation at the close record):**

| Scale | Median recovery | Clause (i) form at scale | Decision |
|---|---|---|---|
| 1× (filed, G1-R) | 0.737 | below the 0.80 floor | — |
| 2× (effective 1.995×) | **0.807** | at or above the floor | crossing |
| 4× (effective 3.676×) | **0.772** | below the floor | crossing not held |

**MIXED** — neither explanation is supported in its
clean form. Two registered MIXED triggers fire: the
median crosses the floor at 2× but not at 4×, and the
anatomy changed character at scale (stem misses in 3 of
the study's 10 replications, against 0 in all ten 1×
replications across both generators' draws). The shuffle
control passes at both scales, so no scale's figure is
void. What the anatomy shows underneath the medians is
filed at §4: the study's replications split into basin
failures, a search phenomenon that returns at scale, and
plateau replications, the 1× phenomenon persisting at
scale — and the medians are carried substantially by
which kind each replication is.

## 1. The run as executed

Ten fresh corpora, seeds `spec109-scl2-synth-{1..5}` and
`spec109-scl4-synth-{1..5}`; no build was rejected and
no `-try{n}` rebuild was needed. Each corpus was built
to the Indus profile at its scale (3,340 artifacts /
14,004 tokens at 2×; 6,680 / 28,008 at 4×; the length
multiset replicated exactly; 40 / 80 imposed duplicate
copies; 120 / 240 counted slots; the family corpus fixed
at 4,000 sequences), with the amendment §2's two
combinatorial accommodations in force: the length-2
stem pool saturated at the inventory maximum of 529
pairs, and distinctness falling back at length-2 slots
only — F = 9 fallbacks at every 2× replication and
F = 547 at every 4× replication, in both cases exactly
the registered minimum (269k length-2 sequences against
the 529 cap). Distinct counts measured: 3,291–3,292 at
2× (effective scale 1.995×) and 6,058–6,069 at 4×
(effective 3.671–3.678×, median 3.676×). Admission gates held on
all ten corpora (profile exact; the two ground-truth
constructions in agreement; every value at ≥ 5 tokens;
every fallback at a length-2 slot). The search per
replication is the registered G1-R search at its
registered budget (40 restarts × 160,000 steps, swaps
and 3-cycle rotations, the filed schedule and polish),
with constraint propagation identical to the earlier
preflights (anchors fixed; admissibility from G2's
ρ = 0.95 detection on the derivation; relaxations filed
per replication in the raw outputs). The harness's
internal gate ran before each scale's search: the
3-cycle delta agreed with full rescoring on 200/200
random triples. One execution disclosure: the study's
first launch was stopped minutes in, before any
replication completed, to add the harness's own SHA-256
to the raw outputs as amendment §8 requires; the runs
were relaunched clean under the final harness
(`80663a03…`) and no figure from the stopped launch is
used anywhere in this record.

## 2. Results per scale

**2×** (seeds `spec109-scl2-synth-{1..5}`):

| Rep | Recovery (i) | Shuffle | Penalized margin | Null p99 | Objective gap | Misses (S/O/C/X/A) |
|---|---|---|---|---|---|---|
| 1 | 0.807 (46/57) | 0.333 | 1,837.6 | −946.5 | +31.0 | 11 (0/0/5/2/4) |
| 2 | 0.684 (39/57) | 0.158 | 1,747.3 | −911.6 | **−551.7** | 18 (1/1/7/5/4) |
| 3 | 0.860 (49/57) | 0.140 | 1,701.6 | −854.8 | +60.8 | 8 (0/0/8/0/0) |
| 4 | 0.737 (42/57) | 0.175 | 1,789.9 | −883.9 | +30.3 | 15 (0/2/5/4/4) |
| 5 | 0.807 (46/57) | 0.193 | 1,906.7 | −912.8 | +45.7 | 11 (0/0/7/4/0) |
| **Median** | **0.807** | 0.175 | 1,789.9 | — | — | — |

**4×** (seeds `spec109-scl4-synth-{1..5}`):

| Rep | Recovery (i) | Shuffle | Penalized margin | Null p99 | Objective gap | Misses (S/O/C/X/A) |
|---|---|---|---|---|---|---|
| 1 | 0.772 (44/57) | 0.088 | 3,219.9 | −1,360.2 | **−1,415.9** | 13 (1/0/7/1/4) |
| 2 | 0.702 (40/57) | 0.175 | 3,363.9 | −1,393.5 | **−1,495.0** | 17 (1/1/8/3/4) |
| 3 | 0.860 (49/57) | 0.193 | 3,455.9 | −1,463.9 | +52.2 | 8 (0/0/8/0/0) |
| 4 | 0.754 (43/57) | 0.439 | 3,558.4 | −1,533.1 | +79.9 | 14 (0/0/8/2/4) |
| 5 | 0.860 (49/57) | 0.175 | 3,446.3 | −1,528.8 | +97.3 | 8 (0/0/8/0/0) |
| **Median** | **0.772** | 0.175 | 3,446.3 | — | — | — |

(Miss anatomy over the 57 scored signs: S = stems,
O = openers, C = closers, X = context values, A =
affixes. The objective gap is the candidate's objective
minus the planted truth's, under the identical objective
construction.)

- Clause (i) form at scale: **met at 2×** (median
  0.807 ≥ 0.80), **not met at 4×** (median 0.772).
  These are the study's threshold comparisons at the
  registered value, not licensing verdicts — a
  preflight verdict exists only at the 1× profile
  (amendment §5).
- Clause (ii): **passed 5/5 at both scales** (median
  penalized margins 1,789.9 and 3,446.3 nats against
  null 99th percentiles near −900 and −1,500).
  Reported per the registration; not part of the
  decision.
- Shuffle control: **passed at both scales** (median
  0.175 < 0.5 × the median right recovery at each
  scale). One per-replication figure is filed for the
  record: the 4× replication 4 shuffle recovery of
  0.439 is the study's highest; the control's
  registered form is the median form, and it passes.
- Relaxations: 1–3 signs per replication, filed in
  the raw outputs.

## 3. The recovery-vs-scale curve

| Scale (nominal) | Effective scale (median) | Median recovery | Basin failures |
|---|---|---|---|
| 1× (filed G1-R draw) | 1.000× | 0.737 | 0 of 5 |
| 2× | 1.995× | 0.807 | 1 of 5 |
| 4× | 3.676× | 0.772 | 2 of 5 |

The curve is non-monotone, and its two scale points are
each mixtures of the two mechanisms at §4, in different
proportions. Read as a pure information curve it would
say identifiability rises then falls, which the anatomy
contradicts: nothing about the objective's information
falls between 2× and 4× — what falls is the share of
replications in which the registered search finds the
basin the objective's optimum occupies. The threshold
bracket the amendment's (A) branch would have filed is
therefore not filed: there is no measured crossing that
holds.

## 4. Anatomy of the scale runs (post-hoc, from the custody truths)

- **Basin failure returns at scale.** At 1×, G1-R's
  repair of the filed search's mechanism B held on all
  five fresh corpora (every candidate's objective above
  the planted truth's). At scale it does not: one of
  five 2× replications and two of five 4× replications
  end far **below** the truth's objective (−551.7;
  −1,415.9 and −1,495.0 nats) — the mechanism-B
  signature, at magnitudes that grow with the corpus,
  as a token-sum objective's inter-basin distances do.
  The interpretation the anatomy supports, filed as
  interpretation and not as a separately measured
  claim (the study did not vary the schedule): the
  objective's per-swap deltas grow with the token
  counts while the registered temperature schedule
  (30 → 0.05, one reheat) is a fixed constant of the
  generator, so the identical search explores a
  landscape of growing energy scale at a fixed
  temperature — relatively colder at every scale, and
  likelier to freeze outside the truth's basin. The
  search's calibration, not only the data, is
  scale-bound.
- **The stem misses are exactly the basin failures'.**
  Across the study's ten replications, stem misses
  occur in precisely the three basin-failure
  replications (one stem each) and nowhere else.
  Conditional on the search finding the basin, the
  anatomy at scale is the filed 1× anatomy: stems 0,
  misses exclusively edge values.
- **The plateau persists where it can be measured.**
  In the seven basin-found replications, candidates
  beating the planted truth's objective by +30.3 to
  +97.3 nats still miss 8–15 edge values, and their
  recoveries straddle the floor (2×: 0.807 / 0.860 /
  0.737 / 0.807, median 0.807; 4×: 0.860 / 0.754 /
  0.860, median 0.860). More data did not dissolve
  the plateau in this sample: the two 0.860
  replications at 4× beat the truth by +52.2 and
  +97.3 nats while missing the same 8 closers. Nor
  did the plateau hold every basin-found replication
  at the 1× level — the best scale replications
  (0.860) exceed G1-R's best 1× replication (0.807).
  Both statements are in the numbers; neither is the
  whole curve.

## 5. Decision-rule evaluation (amendment §5, as registered)

- **(A) information — NOT SUPPORTED.** Its condition
  is median recovery at 4× ≥ 0.80 with the anatomy
  intact and the shuffle control passing at 4×. The
  4× median is 0.772 and the 4× anatomy is not intact.
- **(B) objective design — NOT SUPPORTED.** Its
  condition is both scale medians below 0.80 with the
  shuffle control passing at both. The 2× median is
  0.807. Independently of the arithmetic, the (B)
  reading — the objective's edge-value evidence
  failing at scale — is not what the basin-failure
  replications measure: in those replications the
  objective was never optimized to its optimum
  region, so they carry no evidence about what the
  objective identifies at scale.
- **MIXED — the filed outcome,** on two registered
  triggers: crossing at 2× but not 4× (0.807, then
  0.772), and the anatomy changing character at scale
  (stem misses and negative objective gaps in 3 of 10
  replications, against the filed 1× anatomy of stems
  0 in ten of ten and gaps positive in five of five
  for this generator). The shuffle-void rule is not
  triggered at either scale.

## 6. What this does and does not establish; provenance

The study establishes the curve and its mechanism
split: at the registered generator, recovery at 2× and
4× is a mixture of a returning search failure and a
persisting identifiability plateau, and neither of the
two explanations the study was built to separate
describes the mixture. It does not disturb the 1×
record: there the basin was found in five of five fresh
replications, so the G1 revision record's plateau
conclusion at 1× stands as filed, and G1-R's FAILED
licensing state stands with it — this study licenses
nothing, at any scale. The question the result poses
for a future registration, posed and not answered
here: whether a search whose temperature schedule is
calibrated to the objective's energy scale — which
grows with the corpus — finds the basin reliably at
scale, and only under such a search, whether the
plateau at scale binds below the floor. The
real-corpus candidate-with-margins question, which the
amendment made conditional on (A), is not advanced by
this outcome. The floor of 0.80 was not moved.

- Study harness: `records/g1-scale-harness.py`,
  SHA-256 `80663a0391cc3ebe877f484e14a02c95be4d5107c0d9d745332ed49da5748337`.
- Amendment registration:
  `records/g1-scale-registration-2026-11-27.md`,
  SHA-256 `7d6a16ef6dfcd6135ed5af899fccee97321ddeaa15228428cae4e47916705795`.
- Raw outputs: custody
  `glossa-custody/spec109/g1-scale/run-2x/raw-output.json`,
  SHA-256 `5e2b4deb341efd4b1fa336b6ba51d9662e8663cd1b505dc710c842dd75fe121e`,
  and `run-4x/raw-output.json`, SHA-256
  `1f4d2239f1677e6e1934b2337a239445f7396d832c4f53ee4b2429f148fce892`;
  byte-identical copies are filed in this records
  directory.
- Synthetic corpora (custody, never committed): 2×
  rep1 `83383ce8…`, rep2 `529a5ba0…`, rep3 `8dff8b76…`,
  rep4 `68448924…`, rep5 `3f3b325a…`; 4× rep1
  `ae7cf848…`, rep2 `13d390fe…`, rep3 `f2f48562…`,
  rep4 `aaf751b8…`, rep5 `abcb9d32…` (reproducible
  from the filed seeds).
- Payload verdicts: both harness runs completed with
  their raw outputs written and the summaries above as
  their final logged output; TC-109-02 verification
  completed at PASS 119/119 (close record).

**AI disclosure:** executed by an AI agent (Muse, via Muse)
at the direction of Tristen Pierson, per constitution sec. VI.
