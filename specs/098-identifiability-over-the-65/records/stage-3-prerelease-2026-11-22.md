# Spec 098 — Stage 3 Pre-Release Record (2026-11-22)

**Commission:** the owner's act in the Glossa-Lab chat,
2026-11-22 11:19 ET, adopting adjudication item OD-3
(`specs/091-anchor-comparison-integrity/records/coscientist-refresh-adjudication-2026-11-22.md`,
unit I-19): Stage 3 runs with the eligibility reconciliation
and the M267 and M089 checks as prerequisites, and the seal
released once under the custody rules. **Task:** T301.
**Claims:** C098-5, C098-8. **Venue:** tower-compute, fresh
clone `~/glossa-work/s098-stage3-20261122` at origin/main
`7a1e21740a8834e7ae2d724a17d1d54278c32511` (PR #673 merge),
branch `study/098-stage3-2026-11-22`. **Runner:**
`tools/stage3_run.py`. **Status at this record:** the seal
is unopened; the custody file has not been read by any
Stage 3 process; everything below is established from the
frozen records and development data only. This record is
committed before the release, and the release log cites
its commit.

## 1. Eligibility reconciliation

The Stage 3 population is the frozen executed population
of Stage 2: **69 signs — Arm I, the 65 of the population
annex; Arm E, four (M047, M124, M329, M330)** — per spec
§3.1, freeze v1 as amended (population 71 → 70 → 69), and
the Stage 2 freeze §0. Reconciled against the current
standings (3 E + 66 I + 4 R + 3 P + 18 U = 94, Spec 091
standings supplement as amended by the F-9 act, PR #663,
and the M048 act, PRs #671/#672):

- **The four PROCEED signs stand eligible.** M089, M267,
  M347, M375 are class I at the current standings, as they
  were at Stage 2 execution; no act since Stage 2 (F-9,
  M048, F-4, or any refresh-adjudication landing) touches
  their classes, their candidate values, their sheets, or
  their free-choice accounting. Each carries an ACCEPTED
  prediction sheet and was eligible in expectation; each
  proceeds to the binding count test on actual held-out
  counts, and to scoring if the floor is met.
- **M047 remains a member, as the Stage 2 freeze §0
  pre-ruled.** The F-9 act (landed after Stage 2) moved
  M047 to class U in the standings and Arm E of the
  standings is now M124, M329, M330. Stage 2 freeze §0
  states, of exactly this event: an F-9 amendment "would
  not change its membership, its class for this study's
  purposes, its candidate value, or this population; if it
  lands before Stage 3, Stage 3's record states it." It
  has landed, and this record states it: M047 is scored
  through the same rules as every member (count test;
  sheet arm — its sheet is NOT_CONSTRUCTIBLE), on its
  entry exactly as filed (min/mīn, DEDR 4897, 2 free
  choices).
- **M048 is not a member and is not scored.** The M048
  act moved M048 to class I and recorded that the
  identifiability population "is 69 for any future stage
  (66 I + 3 E)". That statement governs future studies
  and freezes. For this frozen execution it cannot
  operate: M048 has no Stage 1 grid row, no Stage 2
  rivals, no prediction sheet, and no free-choice
  accounting, and the freeze bars creating them now
  (spec §3.1: candidate values frozen as recorded in the
  annex, where M048 does not appear; §3.5: sheets are
  pre-unsealing Stage 2 documents; §3.6: the search space
  is closed). The adjudication's own framing of this
  commission is "the four historically eligible signs
  (not a fresh scoring over today's 69)". M048's
  identifiability under Spec 098 therefore remains
  untested by this study; the population coincidence
  (69 = 69) is one of count only, exactly as the M048
  act itself records.
- **The 17 non-testable models are retained** (I-19):
  the sheetless signs' by-construction determinations
  stand as Stage 2 recorded them, finalizing under spec
  §4 precedence on the actual counts (rule 1's count arm
  precedes the sheet arm).
- **The 48 low-power outcomes and the token floor are
  retained:** every member's outcome is re-derived at
  Stage 3 under §4 precedence on actual held-out counts;
  an in-expectation outcome is displaced in the direction
  the actual counts dictate (Stage 2 freeze §6).
- **Frozen parameters kept, verbatim:** penalized margin
  at least 10 nats over the best rival; flexibility
  penalty 2 nats per free choice, candidates and rivals
  alike; the margin must exceed the permutation null's
  99th percentile (B = 999, seed 9801); minimum held-out
  tokens 5; bootstrap B = 999, seed 9802; the ceiling is
  DISCRIMINATED ON PSEUDO-HELD-OUT (the genuine-holdout
  subset is empty, T101). Multiplicity family: the 69
  signs of the frozen population.
- **Refresh-adjudication landings L-1..L-4** (PRs #674,
  #675, #676 open at this record; L-2 in preparation) are
  wording and citation records; none changes any class,
  value, sheet, or count, and none affects this
  reconciliation. The tip is re-read before the landing
  push and any merge is noted in the outcome record.

## 2. Prerequisite check — M267 (OD-3 / I-19)

The check has two arms, both satisfied on the record
before release:

- **Method arm.** M267's Stage 3 model must not count the
  excluded slot-pattern argument as independent
  confirmation. Verified by construction and by
  inspection of the scoring path: `tools/stage3_run.py`
  contains no slot-pattern statistic, no enrichment
  figure, and no input derived from one. The candidate
  model is built solely by the frozen estimator
  (execution freeze annex §3) from the development
  occurrences the sheet's signature assigns, the
  signature read strictly as a statement about sign
  identities, exactly as the sheet itself files it
  ("the observable is used here strictly as a statement
  about sign identities"). The withdrawn figures (4.3×,
  z = 8.038) appear nowhere in the scoring path.
- **Dictionary-leg arm.** M267's eligibility does not
  rehabilitate its failed dictionary leg, and this
  record states the leg's standing so Stage 3 cannot be
  read as repairing it: the F-4 dependency-aware retest
  (PR #665) records the DEDR 494 leg as not verifying as
  filed (entry 494 = il "house, home, place, wife" in
  tree and print; iṉ is not a DEDR headword) and the
  battery verdict as GENITIVE_MARGINAL, not promoted.
  Both stand unchanged. Stage 3 tests identifiability
  only; it neither cites nor repairs the leg.
- **Signature anatomy, from development data (a finding
  of this check, recorded before unsealing).** Under the
  frozen context definition on the corpus of record's
  development clusters, M267's 226 occurrences are
  inscription-initial in 179 (left neighbour BOS); the
  right neighbour is M099 in 180; occurrences meeting
  the sheet's left set {M176, M328} number 1, and
  occurrences meeting both sides of the filed pattern
  number **1**. The filed pattern's left flank, as
  computed on the Phase-era corpus representations the
  sheet's basis rests on, does not reproduce on the
  corpus of record: on this corpus M267 is an initial
  sign followed by M099. The candidate model at scoring
  is therefore built from a single assigned development
  occurrence. That is the frozen machinery operating on
  the filed prediction, not a defect of the run: the
  sheet is the prediction, the corpus of record is the
  test bed, and their disagreement is a Stage 3 finding.
  (Orientation cross-check, same data: the sheets'
  right-side statements agree with the stored sequence
  order — M267's right set carries M099 in 180 of 226,
  and M375's right-neighbour M342 in 6 of 36 against 1
  on the left — so no reversal convention is in play.)

## 3. Prerequisite check — M089 (OD-3 / I-19)

M089's filed upgrade counts are internally inconsistent
(Tranches 2/3 record: the M342 collocation filed at n=15
and n=13; the M176 collocation at n=6 and n=12). The
check reconciles them with the actual Stage 3 inputs:

- The Stage 3 inputs for M089 are (a) the sheet's partner
  **identities** {M342, M267, M176} — the sheet, as
  accepted at Stage 2, already cites identities, not the
  contested counts — and (b) counts computed fresh by
  the runner from the pinned corpus of record. **No
  filed collocation count enters the scoring path.**
- The operative development counts, computed by
  `stage3_run.py prepare` over the deduplicated
  development clusters of the corpus of record: of
  M089's 119 development occurrences, the neighbours
  include M342 in 3, M267 in 2, M176 in 0; the signature
  assigns **5** development occurrences to the candidate.
  These differ from every filed figure because the
  bases differ (filed: raw co-occurrence over the full
  historical corpus; operative: deduplicated development
  clusters under the frozen split) — the inconsistency
  in the filed record is thereby bypassed, not resolved,
  and the filed figures stand on their own records as
  filed.

## 4. Encoding decisions (recorded before release)

Each is the mechanical reading of the frozen texts; the
runner's docstring carries the same statements.

- **Contexts.** The ordered pair (left neighbour, right
  neighbour) of canonical grapheme ids within the same
  inscription, BOS/EOS sentinels at the sequence ends;
  sequences are the deduplicated clusters' representative
  records (execution freeze annex §3; freeze v1 §2).
- **Signatures** (Stage 2 sheets' own words; side-specific
  where the record is side specific, per Stage 2 freeze
  §6): M005, M030, M068 — at least one neighbour is M342;
  M037, M075 — at least one neighbour is M267; M089 — at
  least one neighbour in {M342, M267, M176} (the record
  does not split the set by side); M347 — at least one
  neighbour in {M342, M293, M028, M367, M211, M099} (not
  split by side); M267 — left neighbour in {M176, M328}
  AND right neighbour in {M099, M073} (the filed pattern
  is the conjunction [AGENT]-M267-[TITLE], the reading
  the F-4 record's "flanked" anatomy also uses); M375 —
  right neighbour is M342.
- **Rivals.** Every per-sign rival takes the unconditioned
  assignment (Stage 2 freeze §6): each per-sign rival's
  context model is the sign's unconditioned development
  model, identically for R-A, R-B, R-C, R-D and the Arm E
  additions, and the best rival is that model. Per-rival
  log-likelihoods are recorded individually in the raw
  output; their identity is the §6 rule.
- **Permutation null.** The null permutes value
  assignments over the sign's held-out occurrences
  (execution freeze annex §3): for the per-occurrence
  differences d_i = log P_candidate(c_i) −
  log P_rival(c_i), a permuted assignment credits each
  occurrence's difference to either side at random, so
  null margins are Σ ε_i·d_i with ε_i iid Rademacher —
  fresh `random.Random(9801)` stream per sign, B = 999,
  replicate-major, occurrences in collected order
  (sorted cluster id, then sequence position).
  Percentiles by linear interpolation on the sorted
  replicates.
- **Bootstrap.** Inscription-cluster bootstrap over the
  clusters carrying the sign's held-out occurrences,
  fresh `random.Random(9802)` stream per sign, B = 999;
  the reported interval is the 2.5th–97.5th percentile
  band of the penalized margin.
- **R-E.** Scored as one model (Stage 2 freeze §5): each
  sign's held-out occurrences under the model its
  received value induces — the value's own sign's
  signature where that sign carries an accepted sheet,
  the unconditioned model otherwise; totals over all 69
  signs against the candidate system's totals; penalties
  cancel (the free-choice multiset is unchanged by the
  permutation). R-E conditions no per-sign outcome.
- **Scoring scope.** Margins, nulls, and intervals are
  computed for exactly the signs with an accepted sheet
  whose actual held-out count meets the floor. A sheeted
  sign below the floor finalizes UNDECIDABLE AT THIS
  POWER under rule 1 with no margin computed (the
  Stage 2 freeze §6 precedence; M374's "unscored"
  treatment is the pattern). Sheetless signs finalize
  under rule 1 (count arm) or rule 2 (sheet arm) on the
  actual counts. Every outcome is produced by the
  reference `decide()` rule (`tools/seal_and_score.py`)
  from its recorded inputs, and the verify mode
  recomputes every outcome from the archived raw output.

## 5. Executability verification (prepare run)

Run `study-20261122T162904Z-559728` (mode `prepare`,
tower-compute, payload exit 0):

```
PAYLOAD VERDICT T301-PREPARE: corpus_pin=True
seal_recompute_ok=True grid_reproduced=True
guard_pass=True free_choices_match=True models_built=9
smoke_ok=True custody_read=False
```

Corpus pin verified (SHA-256 `08fc96c8…`); the frozen
split recomputes to 2,413 clusters / 517 held out and
its seal hash recomputes to the committed seal
(`1974d83a…`) **without reading the custody file**; the
TC-098-01 guard passes the 1,896-row development export;
the Stage 1 grid reproduces for all 69 signs; the
free-choice accounting matches the Stage 2 outcome data
for all 69 signs. Candidate models (assigned development
occurrences / unconditioned): M005 0/1, M030 0/2, M037
0/1, M068 0/7, M075 0/10, M089 5/119, M267 1/226, M347
68/73, M375 6/36. The five below-floor sheeted signs'
candidate models rest on zero assigned development
occurrences; the count test governs them, as §4 states.
Each eligible candidate's prediction and rival comparison
is verified executable, with no unrecorded free choice:
the signatures above are the only encodings, and they
are recorded here, before the release (I-19).

## 6. Release protocol

In order: (1) this record and the runner are committed
in the worker clone; (2) `stage3_run.py release` reads
the custody file for the first time, verifies its seal
hash and count against the committed seal record and the
recomputed split, and writes the release log citing this
record's commit — the release happens exactly once, and
the mode refuses any second release; (3)
`stage3_run.py score` re-verifies the seal at scoring
time (a mismatch voids the run: SEAL FAILURE, no
per-sign outcomes), establishes the actual held-out
counts, scores, and archives the raw output before
verdicts; (4) `stage3_run.py verify` recomputes every
outcome from the raw output under `decide()`. Every
attempt is indexed in the outcome record, failures
included (Spec 089 discipline, claim C098-8). If
execution aborts after the release, that fact is stated
on the face of the outcome record; the seal is never
re-struck and never released a second time.

**AI disclosure:** executed by an AI agent (Muse, via
Muse) at the direction of Tristen Pierson, per
constitution sec. VI.
