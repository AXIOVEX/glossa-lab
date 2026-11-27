# Spec 109 — G1 Revision Registration (2026-11-27)

**Amendment to the registration of 2026-11-27, for one
generator only: G1, the Part 1 assignment search.** Filed
under the discipline the registration and C109-7 state in
advance: the Stage 1 preflight failed G1 on clause (i);
the generator produces no scoreable output until a revised
generator passes a preflight under a new registration; the
revision is of the generator's design, never of any bar.
Authorization: the owner's directive of 2026-11-27
~13:54 ET and his standing blanket approval for Glossa
work of 2026-11-27 04:05 ET. This amendment changes
nothing outside G1's search design: the objective, the
scoring rule, the admissibility construction, every
floor, and the verdict rule are identical to the Stage 1
registration, and the re-preflight below is judged under
registration §2's clauses (i) and (ii) and the shuffle
control, at the same floors, on fresh corpora.

## 1. The failure being revised

Stage 1 (`records/stage-1-preflight-2026-11-27.md` §5):
clause (i) recovery per replication 0.825 / 0.772 /
0.702 / 0.789 / 0.614, median **0.772** against the 0.80
floor — FAILED. Clause (ii) passed 5/5 (median penalized
margin 933.2 nats against null 99th percentiles near
−500); the shuffle control passed (median 0.246 against
0.5 × 0.772). Kill criterion 2 fired for G1; Stage 3 is
blocked at its generator.

## 2. Diagnosis (executed on the Stage 1 custody corpora)

The filed run was reproduced restart-by-restart under
its filed seeds (the reproduction's best states return
the filed hits exactly: 47 / 44 / 40 / 45 / 35 of 57 —
the run replays). Over that reproduction, and over the
planted truths the custody corpora carry:

- **The constraints are not the cause.** In all five
  replications, **zero** scored signs have their planted
  value excluded by the admissibility sets: the recovery
  ceiling under the registered constraints is 1.000 on
  every corpus.
- **The objective identifies; its optimum is not the
  truth.** The planted truth's objective against the best
  state the filed search found: the found state scores
  **above** truth by +26.5 / +42.2 / +48.2 / +49.5 nats on
  replications 1–4, and **below** truth by −497.7 nats on
  replication 5. Two distinct mechanisms follow.
- **Mechanism A — the plateau (replications 1–4).** The
  near-optimal region of the objective is wide in exactly
  the per-sign directions recovery counts. The filed best
  states' errors are exclusively edge values — closers
  6/7/8/5, context values 0/2/0/7, affixes 4/4/4/6 per
  replication, stems 0 in replications 1–4 — arranged in
  short permutation cycles (2-cycles predominating;
  lengths 2–5), at mostly low token counts (medians
  24–47). The planted truth is not a swap-local optimum
  in any replication; steepest-ascent swap polish from
  truth gains +3 to +48 nats and lands at recovery
  0.895 / 0.860 / 0.772 / 0.825 / 0.860. The filed best
  states are already swap-local optima (polish moves
  none of them). Per-restart recovery medians are
  0.544–0.754 against best-of-25 values of 0.614–0.825;
  restarts reaching 0.80: 1, 6, 0, 0, 0 of 25.
- **Mechanism B — the basin failure (replication 5).**
  No restart found the truth's basin: the best state is
  497.7 nats below truth and is itself a swap-local
  optimum, so no single swap escapes it; the
  best-recovery restart (0.737) sits 700.2 nats below
  truth. Errors reach stems (2) and context values (9),
  with a 9-cycle. Swap-only annealing at 25 × 80,000
  steps cannot leave a local optimum whose improving
  directions are multi-sign.
- **The refinement stage, evaluated and set aside.**
  The Stage 1 record names an EM/refinement stage among
  the candidate directions. Two forms were built and
  measured on these corpora (development only):
  (a) per-sign marginals from fixed-temperature sampling
  chains (T* = 10) seeded at the best optima — the chains
  wander, the marginals dilute, and the refined candidate
  loses to the ensemble's own best state on both smoke
  corpora (0.649 against 0.702; 0.772 against 0.807);
  (b) per-sign modal aggregation over the polished optima
  (elite band, top-10, top-12, all-40; softmax-weighted
  and unweighted) — the polished ensemble concentrates in
  one basin family (elite-band pairwise Hamming distance
  median 3–4 signs), and every one of the 11 aggregation
  cells probed returned the argmax state itself, while
  the ensemble's spread shows the objective ranking among
  near-optima uncorrelated with recovery at this
  resolution (replication 2: ranks 5–7 by objective
  recover 0.842 against ranks 1–4's 0.772–0.789, and no
  selector over the ensemble reaches them). The
  refinement is therefore not part of the registered
  design; its negative development result is filed here
  so the direction is not silently retried.
- **The enriched ensemble, measured.** The design of §3,
  run in development on the same corpora: replication
  5's basin failure is repaired — best polished state
  recovery **0.807**, objective −16,259.4, which is 24.5
  nats **above** the planted truth's and alone in its
  50-nat band. Replications 1, 2, 4 return the filed best
  recoveries (0.825, 0.772, 0.789). Replication 3 returns
  0.702 at an objective equal to the filed best
  (−16,353.9): on that corpus no local optimum any search
  here found — the filed ensemble's, the enriched
  ensemble's, or polish-from-truth's — exceeds 0.772.
  That is stated plainly as this profile's identifiability
  ceiling pressing on the floor: the revision repairs
  the search-reliability defect the diagnosis proves;
  it does not manufacture information the objective does
  not carry, and the fresh-corpus run of §5 is the verdict
  on whether the repaired search clears the floor.

Diagnosis artifacts (custody, never committed):
`glossa-custody/spec109/g1-revision/` — `diag.py`
SHA-256 `c01ac842…`, `diag-output.json` `74616f3d…`,
`diag2.py` `f57b117d…`, `diag2-output.json` `5c40a4ee…`,
`probe.py` `7c03578f…`, development run logs under
`dev-smoke/` and `dev-smoke2/`.

## 3. The revised design (G1-R), registered

Identical to Stage 1, and stated so the identity is
checkable: the corpus construction, the split, the
anchors, the admissibility construction (G2's ρ = 0.95
detection on the derivation, the filed relaxation rule),
the objective, the margin construction, the permutation
null, and the recovery computation are the Stage 1
harness's own code, imported from the filed file at its
pin (SHA-256 `f4e84285…`) by the revision harness
(`records/g1-revision-harness.py`). The candidate
selection rule is Stage 1's: the best state by objective.

What changes is the search that produces the states:

- **Restarts:** 40 (was 25). Restart 0 is
  frequency-initialized; restarts 1–39 are random
  admissible assignments, as before.
- **Steps:** 160,000 per restart (was 80,000).
- **Move set:** admissible swaps with probability 0.7
  and admissible **3-cycle rotations** with probability
  0.3 (new), every delta exact (the 3-cycle delta is
  asserted against full rescoring on 200 random triples
  before any run; a disagreement is a STOP). The cycle
  moves are the mechanism-B repair: the filed error
  anatomy is short permutation cycles, and a stuck state
  that no swap improves can still be left by a rotation.
- **Schedule:** geometric 30 → 0.05 over the first
  80,000 steps; one reheat to 10 at step 80,000;
  geometric 10 → 0.05 over the second 80,000 (the reheat
  is the second mechanism-B repair: a restart that has
  frozen into a local optimum gets one registered second
  descent).
- **Polish:** each restart returns its best-visited
  state, then steepest-ascent swap polish to a local
  optimum (new; canonicalizes the ensemble the selection
  rule reads — the filed run's returned states were
  already local optima on these corpora, and the polish
  makes that a property of the design rather than of
  the trajectory).

## 4. Fresh material and seeds

The verdict run uses five fresh synthetic corpora, seeds
**`spec109-s1r-synth-{1..5}`**, built and admitted under
the Stage 1 gates exactly (profile exact; the two
ground-truth constructions in agreement; every value at
≥ 5 tokens; a rejected build rebuilt under the `-try{n}`
suffix and the seed of record filed). Derived seeds are
constructed from the corpus seed as the harness files
them (`-g1r-init{r}`, `-g1r-restart{r}` for the search;
`-g1rshuf-…` for the shuffle control's search; the
shuffle, derangement, shuffled-assignment, and null
seeds as in Stage 1). The Stage 1 corpora are development
material for this amendment and are not re-used for the
verdict; the design above was frozen on the diagnosis of
§2 before any fresh corpus was built.

## 5. Verdict rule (registration §2, unchanged)

- Clause (i): median planted-value recovery across the
  five replications **≥ 0.80**.
- Clause (ii): the top candidate's penalized margin on
  the synthetic holdout clears the frozen bar form
  (≥ 10 nats over the best rival and above the
  permutation null's 99th percentile, B = 999, 2 nats per
  free choice) in the median replication.
- Control: the identical revised pipeline on the shuffled
  derivation returns a median shuffle recovery below
  0.5 × the median right recovery.
- Clause (iii) is not re-run: the predictor form and the
  scorers are unchanged from Stage 1, whose clause (iii)
  PASS stands for the shared predictor. The positional
  limitation is restated as registered: positional
  recovery on the Latin and Meroitic controls is NOT
  MEASURABLE (ground-truth sets of 1 and 0 marks against
  the floor of 5); no positional figure is claimed from
  them here, and G1's clauses in this run are assignment
  recovery on synthetic corpora whose truth is planted
  above the floor.
- **PASSED** (all three clauses at their floors, the two
  implementations in agreement): G1 is licensed, and
  Stage 3 may run Part 1's search under registration §5
  with this generator. **FAILED** (any clause below its
  floor): the outcome is filed, G1 produces no scoreable
  output, Stage 3 remains blocked, and no second revision
  is commissioned by this amendment. No floor moves under
  any outcome.

## 6. Claim determination

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
exactly those constants and the move set, under a new
registration, before any Stage 3 run exists. TC-109-02
by its own text is the preflight conformance test "re-run
for each later generator", and it is re-run for this one
(the verification record at the close). A new claim
would assert a new proposition; this amendment asserts
none — it registers a generator design under the claims
as filed, as the M-2 re-registration's new claim
(C107-12) did not need to do only because that
re-registration changed its test's basis, which this one
does not.

## 7. Provenance

Revision harness: `records/g1-revision-harness.py`
(SHA-256 `a15c8c57…` at filing; the preflight record
carries the executed pin). Raw output and corpora to
custody under `glossa-custody/spec109/g1-revision/run/`,
never committed; a byte-identical copy of the raw output
is filed with the preflight record. Every figure in the
preflight record is recomputed independently by the
TC-109-02 verification script from the custody corpora
and the filed candidate assignments.

**AI disclosure:** executed by an AI agent (Muse, via Muse)
at the direction of Tristen Pierson, per constitution sec. VI.
