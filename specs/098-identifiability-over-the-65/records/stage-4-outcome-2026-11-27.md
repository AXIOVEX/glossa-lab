# Spec 098 — Stage 4 Outcome Record and Closeout (T401 + T402)

**Date:** 2026-11-27 · **Tasks:** T401 (outcome record),
T402 (closeout) · **Claims adjudicated:** C098-1..C098-8
(T401 names C098-5, C098-6, C098-7; the plan's Stage 4
adjudicates this spec's claims on the outcome, and all
eight are adjudicated in §7) · **Commission:** the owner's
act in the Glossa-Lab chat, 2026-11-27 04:05 ET ("Yes do
all these things now or take my approval now to do at the
best time"), lifting the not-commissioned state under
which Stages 1–3 were completed · **Venue:**
tower-compute, worktree
`~/.syncyard/worktrees/glossa/s098-stage4-20261127` at
origin/main `80484f4d054ef867bb7545db26215bb13b9cccd5` ·
**Basis records:** `records/stage-3-outcome-2026-11-22.md`
and its archived raw output
`records/stage-3-outcome-2026-11-22.json`;
`records/stage-3-prerelease-2026-11-22.md`;
`records/stage-2-freeze-2026-11-22.md`;
`records/stage-2-outcome-2026-11-22.md`;
`records/stage1-provenance-audit-2026-11-21.md`;
`records/stage1-grapheme-gap-resolution-2026-11-21.md`;
`records/seal-record-2026-11-21.md`;
`records/tc-execution-2026-11-21.md`.

## 1. What Stage 4 is, as registered

Stage 4 of `tasks.md` is the outcome and closeout stage,
in full:

- **T401 — Outcome record.** "Per-sign outcomes per arm
  in the frozen vocabulary; family counts; the premise
  falsifier applied as written; the contamination ceiling
  restated; this spec's claims adjudicated on the
  outcome. Claims: C098-5, C098-6, C098-7. Acceptance:
  record."
- **T402 — Closeout.** "Tasks ticked to the record;
  remainders named (any standing act on the outcomes is
  a separate program act, not a remainder of this study).
  Acceptance: record."

Stage 4 is a record stage. It runs no scoring, opens no
seal, and reads no custody material: its inputs are the
filed records of Stages 1–3. No precondition of the filed
spec requires a second release of the held-out list, and
none was made (§2).

## 2. Preconditions, verified from the record

1. **Stage 3 is complete and its outcome is filed.** The
   Stage 3 outcome record and its archived raw output are
   on main. On 2026-11-27, on tower-compute, the archived
   raw output was recounted mechanically: the per-sign
   outcomes reproduce the filed distribution exactly
   (46 UNDECIDABLE AT THIS POWER / 22 NOT IDENTIFIABLE /
   1 DISCRIMINATED ON PSEUDO-HELD-OUT over the 69-sign
   executed population), the per-arm counts of §3
   reproduce, the four scored signs' penalized margins
   reproduce the Stage 3 record's table to the filed
   precision (M089 −7.384; M267 −109.458; M347 −0.788;
   M375 +16.224 nats), and a per-row rule spot-check
   (every below-floor row UNDECIDABLE; every sheetless
   row at or above the floor NOT IDENTIFIABLE) found no
   exception. This recount is a Stage 4 verification of
   the filed record, additional to Stage 3's own verify
   invocation, which recomputed all 69 outcomes from the
   raw output under the reference `decide()` rule with no
   mismatches.
2. **The seal discipline is intact and unspent beyond its
   single registered use.** The seal record (517 held-out
   clusters, SHA-256
   `1974d83a5f667b71dbd53ecdb2e42a8221c6d4b91bdd32202b2a80579bf96cf9`)
   was committed 2026-11-21, before any scoring; the list
   was released to the scoring path exactly once (run
   `study-20261122T163036Z-d32312`, 2026-11-22T16:30:36Z),
   the hash recomputed at release and again at scoring,
   and the Stage 3 record states the seal will not be
   released a second time. Stage 4 neither requested nor
   made any further release, and no Stage 4 process read
   the custody list.
3. **The contamination precondition is settled on the
   record.** The Stage 1 provenance audit (T101)
   established that the genuine-holdout subset is empty
   and recorded its absence; the ceiling of §5 follows
   from that finding, not from any Stage 4 judgement.
4. **The premise falsifier's fixture precondition holds.**
   TC-098-02 passed at adoption
   (`records/tc-execution-2026-11-21.md`, payload verdict
   on fixtures), so the falsifier of §4 can be applied as
   written.
5. **The executed population is reconciled.** The frozen
   annex population is 71 (65 I + 6 E). M202 and M044
   left the population before Stage 2 execution by the
   two recorded addendum-rule strikes (the execution
   freeze annex amendment, 71 → 70, on M202's exit; the
   Round 2 amendment, 70 → 69, on M044's adjudication),
   restated in the Stage 2 freeze §0 and the Stage 3
   pre-release record §1. The executed population is 69:
   Arm I, the 65; Arm E, four (M047, M124, M329, M330).
   M048 is not a member and was not scored (pre-release
   record §1). M044 and M202 therefore carry **no
   per-sign outcome under this spec**; their exits are
   part of this study's record, stated here so the
   frozen 71 and the executed 69 are never conflated.

## 3. Per-sign outcomes, per arm (frozen vocabulary)

Outcomes are as determined at Stage 3 under spec §4's
precedence on the actual held-out counts of the single
release, restated here per arm as T401 requires. The
full per-sign record (counts, sheets, thresholds, bases)
is the Stage 3 outcome record's table and the archived
raw output; the scored signs' quantities are restated in
§3.3.

### 3.1 Arm I — the 65 internally motivated candidates

- **UNDECIDABLE AT THIS POWER — 43:** M002, M004, M005,
  M006, M007, M009, M010, M013, M014, M016, M020, M023,
  M026, M027, M029, M030, M032, M034, M037, M038, M041,
  M045, M049, M052, M055, M057, M061, M063, M066, M068,
  M069, M073, M074, M075, M076, M078, M080, M082, M128,
  M151, M220, M351, M374. Each on the binding count test
  (actual held-out tokens below the frozen floor of 5);
  M374's is the T102 frozen default, confirmed by its
  actual count of 0. Five of the 43 (M005, M030, M037,
  M068, M075) held ACCEPTED prediction sheets that never
  governed, the count arm preceding the sheet arm.
- **NOT IDENTIFIABLE — 21:** M015, M017, M018, M025,
  M050, M051, M053, M054, M060, M062, M065, M067, M070,
  M089, M099, M130, M145, M194, M267, M347, M391. Of
  these, 18 are by construction (no accepted prediction
  sheet): the 16 Arm I sheet determinations of Stage 2,
  plus M018 and M054, displaced from their in-expectation
  UNDECIDABLE outcomes by their actual counts (7 and 5)
  and finalized by the sheet arm; and 3 are scored
  failures (M089, M267, M347; §3.3).
- **DISCRIMINATED ON PSEUDO-HELD-OUT — 1:** M375 (§3.3).

### 3.2 Arm E — the four executed externally credited readings

- **UNDECIDABLE AT THIS POWER — 3:** M047 (actual 3),
  M329 (actual 2), M330 (actual 1), each on the count
  test.
- **NOT IDENTIFIABLE — 1:** M124, by construction (no
  accepted sheet; its actual count of 13 confirms the
  sheet arm governs).
- **Pass outcomes — 0.** No Arm E sign reached scoring:
  the three count-test outcomes precede it and M124's
  sheet determination precedes it. Arm E's rerun under
  stronger alternatives therefore returns no
  discrimination result for any of its signs; the desk
  exercise of record (Spec 095 Stage 3: all six NOT
  IDENTIFIABLE) is neither confirmed nor displaced by a
  predictive pass here, because no Arm E sign was
  scored. That is the arm's outcome, stated at its exact
  strength.

### 3.3 The scored signs (Stage 3 quantities, restated)

| Sign | Arm | Held-out tokens | Penalized margin (nats) | Null p99 | Outcome |
|---|---|---|---|---|---|
| M089 | I | 39 | −7.384 | 30.600 | NOT IDENTIFIABLE |
| M267 | I | 61 | −109.458 | 65.148 | NOT IDENTIFIABLE |
| M347 | I | 18 | −0.788 | 0.673 | NOT IDENTIFIABLE |
| M375 | I | 11 | +16.224 | 10.325 | DISCRIMINATED ON PSEUDO-HELD-OUT |

M375 (candidate value taṇ): candidate log-likelihood
−45.941 against the best rival's −62.165; 0 free choices,
so raw margin = penalized margin = 16.224 nats against
the frozen bar of 10; the margin exceeds the permutation
null's 99th percentile (10.325); effect size 1.475 nats
per token; inscription-cluster bootstrap 95% interval
[14.75, 19.17], entirely above the bar; the candidate
also beats the structural-only rival R-D (under the
Stage 2 freeze §6 assignment rule every per-sign rival,
R-D included, is the unconditioned model whose total is
the best rival's). M267's outcome is about the filed
prediction under the frozen machinery; it neither cites
nor repairs M267's DEDR 494 leg, whose F-4 standing is
unchanged. M347's raw margin (1.212) exceeds its null
percentile but its penalized margin is below zero and
far below the bar.

**R-E, the global permutation, scored as one model:**
candidate system −2884.402, permuted system −2772.078,
unconditioned system −2800.120 held-out log-likelihood
over the 69 signs; system-level margin (candidate minus
permuted) **−112.323 nats**, dominated by M267's
misprediction (a 107.458-nat swing). R-E conditions no
per-sign outcome, and none was conditioned on it.

## 4. Family counts

Counts of per-sign outcomes only (spec §4), multiplicity
family the 69 executed signs:

| Outcome | Arm I (65) | Arm E (4) | Total (69) |
|---|---|---|---|
| UNDECIDABLE AT THIS POWER | 43 | 3 | 46 |
| NOT IDENTIFIABLE | 21 | 1 | 22 |
| DISCRIMINATED ON PSEUDO-HELD-OUT | 1 | 0 | 1 |
| IDENTIFIABLE ON HELD-OUT | 0 | 0 | 0 |

## 5. The premise falsifier, applied as written

Spec §4: the study's premise (the frozen machinery can
discriminate at least some candidates from serious
rivals out of sample) "is falsified if, on the
genuine-holdout subset or the pseudo-held-out arm, **no**
sign reaches its arm's pass outcome while the
planted-discrimination fixture of TC-098-02 passes."

TC-098-02 passes (adoption record), and M375 reached
DISCRIMINATED ON PSEUDO-HELD-OUT on the pseudo-held-out
arm. **The premise is not falsified.** The machinery
demonstrably discriminates where discrimination exists
(the fixture) and discriminated once in 69 on the real
population; the remaining 68 outcomes are properties of
the candidates and of power, not of the test.

## 6. The contamination ceiling, restated

The 65 candidate readings were historically derived
using the program's full corpus; no in-corpus split is
pristine against that derivation. The Stage 1 provenance
audit found no sequence-bearing source demonstrably
absent from every candidate-generation input, so **the
genuine-holdout subset is empty** and the outcome
IDENTIFIABLE ON HELD-OUT is unavailable to this study as
constituted. Every result of this study is therefore
capped at the in-corpus arm: M375's DISCRIMINATED ON
PSEUDO-HELD-OUT is a reportable discrimination result on
pseudo-held-out data. It supports **no standing change
and no identification claim beyond the corpus** (spec
§3.3, claim C098-6). M375's class in the standings is
untouched by this study.

## 7. Claims adjudication on the outcome

Each claim is adjudicated against its own falsifier, on
the filed record. These adjudications are this study's
record under T401. They do not themselves move the
canonical ledger: a ledger standing change for any
C098 claim is a separate cascade act under the program's
standing-change discipline (the Spec 101 precedent,
where the outcome record and the ledger act were
separate landings), is not performed by this stage, and
stands ready on the basis of this record.

- **C098-1 (nothing scored before the freeze and the
  seal) — SUPPORTED.** The freeze and the seal record
  were committed 2026-11-21; the first scoring-path run
  is the Stage 3 run index of 2026-11-22; the held-out
  list was released exactly once, at scoring, and the
  release is recorded; the seal hash recomputed from the
  released list at release and at scoring. No falsifier
  event (no pre-seal scoring artifact, no second
  release, no seal mismatch) is on the record.
- **C098-2 (the population and its values are the frozen
  annex's, exactly) — SUPPORTED, in its amended form of
  record.** The executed population is the annex
  population as amended before Stage 2 by the two
  recorded addendum-rule strikes (M202, M044; §2 item
  5); every scored or determined sign is an annex sign
  carrying its annex value exactly as recorded (variants
  scored as the recorded disjunctions, penalties charged
  per alternation); M374's default applied as frozen.
  No value was resolved, split, respelled, or re-glossed
  after the freeze. The falsifier (a scored sign absent
  from the annex, or a scored value differing from the
  annex's) does not fire.
- **C098-3 (every scored sign faces the full frozen
  rival set under matched conditions) — SUPPORTED, in
  its frozen executed form, which is stated here in
  full.** Rivals R-A..R-E were constructed for all 69
  signs under the Stage 2 freeze §5, one deterministic
  construction pass per competitor over the same
  development data and the same frozen search space (WP8
  matched budget); the Arm E additions were constructed
  as the spec names them (M124's comparandum-as-value
  from M044's package; M329's comparandum-as-value;
  M330's cross-sign rival carrying M202's evidence
  package; M047's comparanda-as-value). Two properties
  of the executed form are on the face of the Stage 2
  freeze and are restated here, not smoothed: (a) R-B
  was drawn from the Sanskrit lexicon of record for
  every sign, because no Munda lexicon is carried in the
  repository, and the frozen space was not widened to
  fill that absence; (b) under the Stage 2 freeze §6
  assignment rule, a value with no filed signature takes
  the unconditioned assignment, and every per-sign rival
  is such a value, so each scored sign's per-sign rivals
  share the unconditioned model's held-out total (the
  Stage 3 record states this openly, and the raw output
  records the shared total once, with the rule stated);
  R-E was scored as one model (§3.3). The claim's
  falsifier (a scored sign whose outcome record lacks
  any of the five rival scores; a rival constructed
  using held-out data; a tuning-budget asymmetry) does
  not fire: the guard of TC-098-01 ran over the actual
  development export at Stage 2, and the budget is one
  construction pass for every competitor, candidate
  included.
- **C098-4 (success must be value-relevant) —
  SUPPORTED.** Prediction sheets were constructed and
  reviewed before unsealing; acceptance required a
  neighbour-identity or neighbour-class prediction
  stated on the frozen record that the rivals do not
  state; 9 sheets were accepted (M005, M030, M037, M068,
  M075, M089, M267, M347, M375) and the study's only pass
  (M375) rests on an accepted sheet. The Stage 2 freeze
  §6 answered the spec's motif category in the open: the
  corpus of record carries no motif or iconography field
  the estimator can score, so a sheet resting on a motif
  association alone was not accepted, with the reason
  recorded per sign. Signs with no accepted sheet are
  NOT IDENTIFIABLE by construction, as the claim
  provides (19 of the 22 NOT IDENTIFIABLE outcomes,
  counting M124).
- **C098-5 (the decision rules are applied as frozen) —
  SUPPORTED.** Outcomes follow §4's precedence on the
  actual held-out counts; the bars are the frozen ones
  (minimum 5 held-out tokens; penalized margin at least
  10 nats; above the permutation null's 99th percentile,
  B = 999, seed 9801; flexibility penalty 2 nats per free
  choice, candidates and rivals alike). Stage 3's verify
  invocation recomputed all 69 outcomes from the
  archived raw output under the reference `decide()` rule
  with no mismatches, and Stage 4's recount (§2 item 1)
  reproduces the distribution and the per-arm counts.
  The family reporting of §4 is counts of per-sign
  outcomes only.
- **C098-6 (the contamination ceiling is honoured) —
  SUPPORTED.** The Stage 1 record carries the provenance
  audit's result (the genuine-holdout subset is empty,
  its absence recorded); no IDENTIFIABLE ON HELD-OUT
  outcome was scored or reported on in-corpus material;
  the single pass is reported at its capped strength,
  DISCRIMINATED ON PSEUDO-HELD-OUT, in the Stage 3
  record and here (§6).
- **C098-7 (no outcome of this study moves any other
  program record) — SUPPORTED.** This study changed no
  reading's standing, anchor, or class: M375 remains
  class I on its prior basis; M047's membership was
  carried on its entry as filed under the Stage 2 freeze
  §0 pre-ruling, stated in the pre-release record, and
  the F-9 act that moved M047 in the standings was a
  separate program act, not this study's. No record of
  this study converts an identifiability outcome into a
  support disposition.
- **C098-8 (execution discipline: venue, index, payload
  verdicts) — SUPPORTED.** Every execution ran on
  tower-compute in a fresh clone (Stages 1–3 as their
  records state; Stage 4's verification in the worktree
  named above); the Stage 3 run index is complete —
  prepare, the single release, score, and the verify
  invocation, each with its payload verdict, no failed
  attempts and no gaps; every reported verdict in the
  study's records is the run's own payload verdict.

## 8. Closeout (T402)

- Tasks T401 and T402 are ticked in `tasks.md` by this
  landing. With Stage 4, Spec 098 is complete: Stages
  0–4 all executed and recorded. **Final disposition:**
  of the 69 executed signs, 46 UNDECIDABLE AT THIS
  POWER, 22 NOT IDENTIFIABLE, and 1 DISCRIMINATED ON
  PSEUDO-HELD-OUT (M375), the study's premise not
  falsified, its contamination ceiling stated on the
  face of the record, and no standing changed.
- **Remainders named, as T402 requires:**
  1. Any standing act on M375's outcome is a separate
     program act, not a remainder of this study
     (tasks.md T402, claim C098-7). None is taken here.
  2. The canonical-ledger cascade giving effect to §7's
     adjudications in the ledger's standings for
     C098-1..C098-8 is a separate act under the
     standing-change discipline; it is not performed by
     this landing and stands ready on this record.
  3. Not remainders of this study, stated so they are
     not mistaken for open Stage 4 work: M048's
     identifiability is untested by this study and is
     governed by future studies and freezes (the M048
     act, via the pre-release record §1); M044 and M202
     carry no outcome under this spec (§2 item 5).

**AI disclosure:** executed by an AI agent (Muse, via
Muse) at the direction of Tristen Pierson, per
constitution sec. VI.
