# Spec 109 — G1 Enriched-Objective Registration (2026-11-27)

**Amendment to the registration of 2026-11-27, for one
generator only: G1, the Part 1 assignment search.** Filed
under the discipline the registration and C109-7 state in
advance: two preflights have now failed G1 on clause (i);
the generator produces no scoreable output until a revised
generator passes a preflight under a new registration; the
revision is of the generator's design, never of any bar.
Authorization: the owner's directive of 2026-11-27
~13:54 ET and his standing blanket approval for Glossa
work of 2026-11-27 04:05 ET. This amendment changes
nothing outside G1's objective and search calibration:
the admissibility construction, the scoring rule, the
margins, the permutation null, every floor, and the
verdict rule are identical to the Stage 1 registration,
and the re-preflight below is judged under registration
§2's clauses (i) and (ii) and the shuffle control, at
the same floors, on fresh corpora.

## 1. The failure being revised

Two filed preflights and one filed study bound the
design space:

- **The plateau (Stage 1; G1-R re-preflight).** The
  filed search failed clause (i) at median 0.772; the
  revised search G1-R repaired the basin defect (its
  candidates beat the planted truth's objective on all
  five fresh corpora, +20.0 to +57.2 nats) and still
  failed clause (i) at median **0.737**
  (`records/g1-revision-preflight-2026-11-27.md` §4):
  candidates above the truth's objective miss 11–21 of
  57 signs, the misses exclusively edge values (closers,
  context values, affixes; stems 0 in all five). At this
  profile the objective's near-optimal region contains
  assignments differing from the truth on a fifth to a
  third of the edge values: the binding constraint is
  the objective's edge-value evidence, not the search.
- **The scale study's MIXED outcome (T103).**
  Identifiability is not purely information-bound:
  conditional on the search finding the basin, recovery
  rises with scale (basin-found medians 0.807 at 2×,
  0.860 at 4×), and the basin failures that return at
  scale are a calibration phenomenon — the objective's
  per-swap deltas grow with the token counts while the
  registered temperature schedule (30 → 0.05) is a fixed
  constant, so the identical search runs relatively
  colder at every scale
  (`records/g1-scale-study-2026-11-27.md` §4). The
  study poses, and does not answer, the question of an
  energy-scale-calibrated search.
- **The unused evidence.** Stage 2's licensed
  positional-class induction is the program's strongest
  verified structure on the real corpus (131 restricted
  marks against a shuffle-null maximum of 9; 108 stable
  structures), and positional restriction is edge-shaped
  by nature: it is evidence about exactly the value
  classes the plateau cannot separate. G1's filed
  design consumes that induction only as a threshold —
  the ρ = 0.95 detection feeding admissibility. The
  induction's full output, the per-sign and per-value
  positional distributions, enters the objective
  nowhere.

This amendment's design follows from those three
findings and from nothing else: enrich the objective
with the positional evidence in its full distributional
form (§3), and calibrate the search's temperature
schedule to the objective's own energy scale (§4). The
floors do not move.

## 2. Development (executed on development material only)

All development ran on the ten development-visible
corpora — the Stage 1 filed corpora (seeds
`spec109-s1-synth-{1..5}`, rep 4 of record
`spec109-s1-synth-4-try1`) and the G1-R fresh corpora
(seeds `spec109-s1r-synth-{1..5}`, rep 5 of record
`spec109-s1r-synth-5-try1`) — rebuilt from their filed
seeds under the filed admission gates. No verdict
corpus of §5 existed during development. The
development driver and its outputs are in custody
(`glossa-custody/spec109/g1-enriched/dev/`).

**The weight λ.** The enriched search (term of §3,
calibration of §4) was run search-only over the ten
development corpora at λ ∈ {0, 0.25, 0.5, 1, 2, 4}.
Median planted-value recovery across the ten corpora:

| λ | Median recovery | Median edge misses | Median stem misses |
|---|---|---|---|
| 0.0 | 0.763 | 13.5 | 0 |
| 0.25 | 0.772 | 13.0 | 0 |
| 0.5 | 0.772 | 13.0 | 0 |
| **1.0** | **0.781** | **12.5** | **0** |
| 2.0 | 0.781 | 12.5 | 0 |
| 4.0 | 0.754 | 14.0 | 0 |

Selection rule, fixed before the grid was read:
λ* is the smallest grid value attaining the maximal
median recovery — the least enrichment that achieves
the development optimum, so the frozen objective keeps
primacy wherever the term adds nothing. The rule
returns **λ* = 1.0** (λ = 1 and λ = 2 return identical
recoveries on all ten corpora; at λ = 4 the term begins
to override pair evidence and the median falls). The
development effect is real and modest, and is filed as
such: the term repairs specific edge confusions (on
Stage 1 rep 1, context misses 4 → 0 and affix misses
4 → 0, recovery 0.754 → 0.895; on G1-R rep 2, affix
misses 4 → 0), it does not move the hardest corpora
(Stage 1 rep 3 holds at 0.702 at every λ ≤ 2), and
closers remain the largest miss class at λ* — a
closer's positional profile (final) is shared with the
final affix values and the site-B context values, so
position alone cannot separate them, and their identity
rides on the pair statistics that stay weak at low
counts. The development median at λ* (0.781) stands
below the floor the verdict run is judged at; the
design is filed on the grid and the rule, not on a
development promise, and the fresh-corpus run of §5 is
the verdict.

**The calibration reference.** δ̂ (the median |ΔE| over
2,000 admissible swaps sampled at the
frequency-initialized state, §4's rule) measured under
the unenriched objective (λ = 0) on the five Stage 1
corpora: 71.1830 / 46.0534 / 66.0398 / 62.4345 /
63.9045, median **δ̂_ref = 63.9045**. The per-corpus
spread (46.1 to 71.2) is itself the calibration's
motivation at 1×: the filed fixed schedule runs at a
different effective temperature on every corpus. The
λ = 0 row of the grid is the calibration's band check:
the calibrated-but-unenriched search returns median
0.763 over the pooled ten development corpora, in the
band of the two filed generators' draws (0.772, 0.737)
— the calibration is near-neutral at 1×, as its
construction requires, and its effect is reserved for
scale (§6's diagnostic).

**Two-implementation and delta gates.** The harness's
internal gates ran before every development and verdict
run: the enriched swap delta and the enriched 3-cycle
delta each agree with full rescoring on 200/200 random
states, and the term's matrix form agrees with its
direct per-token form to 1e-9 — a disagreement is a
STOP, and none occurred.

## 3. The enriched objective (registered)

The objective the search optimizes is

**E(φ) = L(φ) + λ · P(φ)**, with λ = 1.0 frozen,

where **L** is the filed objective unchanged (the
duplicate-aware cross-validated predictive
log-likelihood under the frozen predictor form, the
Stage 1 harness's code at its pin, SHA-256
`f4e84285…`), and **P** is the positional-consistency
term, constructed exactly as follows:

- *Sign side.* Run G2's positional induction — the
  Stage 1 harness's `positional_counts` mechanization
  (registration §3 family (a): per-sign counts over
  initial / medial / final / sole) — on the derivation
  under analysis, numeral-truncated exactly as L's
  token stream is. This gives each sign s its counts
  n_s(p) over the four position classes.
- *Value side.* Run the same induction on the
  value-side family corpus (the frozen predictor's
  reference corpus, 4,000 sequences). This gives each
  value v its counts m_v(p); its positional
  distribution is q_v(p) = (m_v(p) + α) / (M_v + 4α)
  with M_v = Σ_p m_v(p) and the smoothing constant
  α = 0.5, a design constant fixed here a priori (the
  Jeffreys form), not fitted on any corpus.
- *Term.* P(φ) = Σ_tokens log q_{φ(s(token))}(pos(token))
  over the derivation's tokens — in matrix form
  P(φ) = Σ_s M[s][φ(s)] with
  M[s][v] = Σ_p n_s(p) · log q_v(p), so every swap and
  3-cycle delta of the term is exact and O(1).

**No-leakage statement.** The term's two inputs are
the corpus under analysis and the family corpus — the
two inputs the pipeline has on real material (the
Indus derivation set; the candidate families' reference
material that also supplies the predictor weights). On
synthetic corpora the positional evidence is produced
by the induction pipeline itself, run on the corpus
under analysis; the planted assignment, the planted
roles, and every truth-side quantity are never read by
the term or by the search. (Truth-side quantities
appear in the run's raw output only as scoring and
anatomy, computed after the candidate exists, exactly
as in the scale study.) The term is distinct from the
admissibility construction it complements: admissibility
thresholds the same induction's output at ρ = 0.95 into
hard constraints; the term scores the full,
untresholded distributions of every sign and value,
including the signs no threshold fires on. It is also
distinct from Part 3's context term, which Stage 2
returned CHANNEL NULL and withdrew: that term scored
site/material context labels, this one scores
within-sequence position, the channel Stage 1's
preflight measured at recovery 1.000 for the positional
family in every replication.

**What does not change.** The corpus construction, the
split, the anchors, the admissibility construction
(G2's ρ = 0.95 detection on the derivation, the filed
relaxation rule), the candidate selection rule (the
best polished state by the search objective), the
margin construction, the permutation null, and the
recovery computation are the filed code of the Stage 1
and G1-R harnesses, imported at their pins (Stage 1
SHA-256 `f4e84285…`; G1-R SHA-256 `a15c8c57…`, whose
exact 3-cycle delta and rotation the harness reuses).
The margins are decide()-form figures under the frozen
scorers, computed on the candidate the enriched search
selects; the enrichment enters candidate selection
only, never the adjudication arithmetic — the Round N
qualification rides unchanged: the search objective,
enriched or not, is a search-internal ranking quantity,
and no normalized predictive log-loss advantage is
claimed for it.

## 4. The calibrated schedule (registered)

The search is G1-R's ensemble exactly — 40 restarts ×
160,000 steps, admissible swaps (p = 0.7) and admissible
3-cycle rotations (p = 0.3) under exact deltas, restart
0 frequency-initialized, one reheat at step 80,000,
each restart's best-visited state swap-polished to a
local optimum (the polish now under E) — with the
single registered change that the temperature schedule
is calibrated per corpus:

- Before the ensemble phase, on a copy of the
  constraint state (the measurement is read-only; the
  search's own admissibility evolution is G1-R's,
  untouched), build the frequency-initialized
  assignment (restart 0's start, seed
  `{prefix}-init0`) and sample admissible swaps
  uniformly from the free sign pairs (rng seeded
  `{prefix}-calib`) until 2,000 admissible swaps are
  collected (draw cap 40,000; a short sample is a
  STOP). **δ̂** is the median |ΔE| over the sample,
  ΔE under the enriched objective at the frozen λ.
- The schedule is G1-R's two-segment geometric form
  with its temperatures scaled by δ̂: segment 1
  (steps 0–80,000) from T_hi = C_HI·δ̂ to T_lo =
  C_LO·δ̂; one reheat at step 80,000 to T_mid =
  C_MID·δ̂; segment 2 (steps 80,000–160,000) from
  T_mid to T_lo. The constants are frozen here:
  **C_HI = 0.46945080842976417,
  C_MID = 0.15648360280992138,
  C_LO = 0.000782418014049607** — that is, 30 / 10 /
  0.05 each divided by δ̂_ref = 63.904459128199335
  (§2's development measurement), so a corpus whose
  measured δ̂ equals the reference runs G1-R's filed
  schedule exactly, and any other corpus runs the same
  schedule in units of its own energy scale.

## 5. Fresh material and seeds

The verdict run uses five fresh synthetic corpora,
seeds **`spec109-s1e-synth-{1..5}`**, built and
admitted under the Stage 1 gates exactly (profile
exact; the two ground-truth constructions in agreement;
every value at ≥ 5 tokens; a rejected build rebuilt
under the `-try{n}` suffix and the seed of record
filed). Derived seeds are constructed from the corpus
seed as the harness files them (`-g1e-init{r}`,
`-g1e-restart{r}`, `-g1e-calib` for the search;
`-g1eshuf-…` for the shuffle control's search; the
shuffle, derangement, shuffled-assignment, and null
seeds as in Stage 1). The development corpora of §2 are
not re-used for the verdict; the design above was
frozen on the development of §2 before any fresh corpus
was built.

**Secondary diagnostic (not a licensing clause).** The
identical enriched preflight is also run at 2× corpus
scale on five fresh corpora (seeds
**`spec109-s1e2-synth-{1..5}`**), built under the scale
amendment's registered substitutions and fallback
accounting (`records/g1-scale-registration-2026-11-27.md`
§2), to check the calibration where the scale study
found the regression: whether basin failures return
under the calibrated schedule, and what the enriched
objective's recovery and anatomy are at scale. The
diagnostic files its figures in the preflight record;
it issues no verdict, licenses nothing, and its
outcome does not enter the verdict rule of §6 in
either direction.

## 6. Verdict rule (registration §2, unchanged)

- Clause (i): median planted-value recovery across the
  five verdict replications **≥ 0.80**.
- Clause (ii): the top candidate's penalized margin on
  the synthetic holdout clears the frozen bar form
  (≥ 10 nats over the best rival and above the
  permutation null's 99th percentile, B = 999, 2 nats
  per free choice) in the median replication.
- Control: the identical enriched pipeline on the
  shuffled derivation (its own detection, term tables,
  and calibration measurement) returns a median shuffle
  recovery below 0.5 × the median right recovery.
- Clause (iii) is not re-run: the predictor form and
  the scorers are unchanged from Stage 1, whose clause
  (iii) PASS stands for the shared predictor. The
  positional limitation is restated as registered:
  positional recovery on the Latin and Meroitic
  controls is NOT MEASURABLE (ground-truth sets of 1
  and 0 marks against the floor of 5); no positional
  figure is claimed from them here. The term's own
  conformance is exercised where positional truth is
  planted above the floor — the synthetic corpora of
  clauses (i) and the control — and the induction that
  feeds it is the family Stage 1's preflight passed at
  recovery 1.000 in every replication.
- **PASSED** (all three clauses at their floors, the
  two implementations in agreement): G1-E is licensed,
  and Stage 3 may run Part 1's search under
  registration §5 with this generator. **FAILED** (any
  clause below its floor): the outcome is filed with
  its anatomy, G1 produces no scoreable output, Stage
  3 remains blocked, and no second revision is
  commissioned by this amendment. No floor moves under
  any outcome.

## 7. Claim determination

No new claim is intaken for this amendment, and the
claims ledger does not move in its landing. The basis,
stated so it can be checked against the filed texts:
C109-7 as filed already carries the revised-generator
pattern ("the generator produces no scoreable output
until a revised generator passes under a new
registration"), and its falsifier set is untouched by
this amendment — no bar is lowered, no margin is
computed under any rule but the frozen one, no output
is scored before the preflight record is filed.
C109-2's subject is Part 1's Stage 3 execution under
registration §5, which marks the search schedule itself
— restart count, seed list, schedule form — as the
search's own FREEZE constants; this amendment revises
the objective the schedule serves and the schedule's
calibration, under a new registration, before any
Stage 3 run exists. TC-109-02 by its own text is the
preflight conformance test "re-run for each later
generator", and it is re-run for this one (the
verification record at the close). A new claim would
assert a new proposition; this amendment asserts none —
it registers a generator design under the claims as
filed, as the G1 revision amendment (§6 of its
registration) and the scale study amendment (§6 of
its registration) determined before it. The contrast
with Spec 107's M-2 stands as those records state it:
that re-registration changed its test's basis and did
need C107-12; this one changes a generator's design
under an unchanged basis, floors, and verdict rule,
and does not.

## 8. Kill-criteria posture (spec.md §9, pre-registered)

1. **Null yield at the frozen bar** — not engaged; it
   binds at Part 1's own stage over its candidates,
   which do not exist while the generator is
   unlicensed.
2. **Preflight failure** — engaged, and fires for
   G1-E if the verdict of §6 is FAILED: the generator
   produces no scoreable output and Stage 3 remains
   blocked. This amendment commissions no further
   revision; a further design is a new commission
   under a new registration, on the evidence this
   record, the preflight record, and the two filed
   failures provide.
3. **Control failure** — engaged through the shuffle
   control of §6: a shuffle recovery at or above half
   the right recovery fails the control clause and the
   verdict with it (kill criterion 3's form: the
   pipeline will have measured itself).
4. **Gate dependence** — not engaged.
5. **Integrity tripwire** — standing; any breach
   halts the study on the program's rule.

## 9. Provenance

Enriched harness: `records/g1-enriched-harness.py`
(SHA-256 `8d107720…` at filing; the preflight record
carries the executed pin). Development driver and
outputs: custody `glossa-custody/spec109/g1-enriched/
dev/` (driver SHA-256 and output pins in the preflight
record), never committed. Raw outputs and corpora to
custody under `glossa-custody/spec109/g1-enriched/run/`
(1× verdict) and `…/run-2x/` (diagnostic), never
committed; byte-identical copies of the raw outputs
are filed with the preflight record. Every figure in
the preflight record is recomputed independently by
the TC-109-02 verification script from the custody
corpora and the filed candidate assignments.

**AI disclosure:** executed by an AI agent (Muse, via Muse)
at the direction of Tristen Pierson, per constitution sec. VI.
