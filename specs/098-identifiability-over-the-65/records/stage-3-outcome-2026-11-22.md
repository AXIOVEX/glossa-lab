# Spec 098 — Stage 3 Outcome Record (T301)

**Date:** 2026-11-22 · **Task:** T301 (the scoring run; the
seal opened once) · **Claims:** C098-5, C098-8 ·
**Venue:** tower-compute, fresh clone
`~/glossa-work/s098-stage3-20261122` at origin/main
`7a1e21740a8834e7ae2d724a17d1d54278c32511` ·
**Freezes:** freeze v1, the execution freeze annex
(estimator), the Stage 2 freeze ·
**Pre-release record:**
`records/stage-3-prerelease-2026-11-22.md` (eligibility
reconciliation, the M267 and M089 prerequisite checks,
the encoding decisions; committed at
`ea62163121bc8a300e1f821b66025ec823237cc8` before the
release) · **Runner:** `tools/stage3_run.py` ·
**Data:** `records/stage-3-outcome-2026-11-22.json`
(the archived raw scoring output, byte-identical to the
run directory's raw file).

## The release

The held-out list was released to the scoring path
exactly once, under freeze v1 §3: run
`study-20261122T163036Z-d32312`, 2026-11-22T16:30:36Z.
At release the custody list's seal hash recomputed to
the committed seal (SHA-256
`1974d83a5f667b71dbd53ecdb2e42a8221c6d4b91bdd32202b2a80579bf96cf9`),
its count was 517, and its set equalled the recomputed
frozen split; the release log cites the pre-release
commit above. At scoring time (run
`study-20261122T163043Z-c6e811`) the seal was verified
again from the custody list before any outcome was
computed. The seal is not re-struck and will not be
released a second time. Execution did not abort after
the release.

## Population, as executed

The frozen executed population of Stage 2: 69 signs —
Arm I, the 65; Arm E, four (M047, M124, M329, M330) —
reconciled against the current standings (3 E + 66 I +
4 R + 3 P + 18 U = 94) in the pre-release record §1:
M047 remains a member on its entry as filed (the F-9
act's move to class U is stated there, per the Stage 2
freeze §0 pre-ruling); M048, now class I, is not a
member and is not scored (no frozen grid row, rivals,
sheet, or accounting exists for it, and the freeze bars
creating them); the multiplicity family is these 69.

## What Stage 3 determined

Under spec §4's precedence on the **actual** held-out
counts established at this single release:

- **1 DISCRIMINATED ON PSEUDO-HELD-OUT — M375**
  (candidate value taṇ). Held-out tokens 11 (expected
  9.0); candidate log-likelihood −45.941 against the
  best rival's −62.165; penalized margin **16.224 nats**
  (0 free choices, so raw = penalized) against the
  frozen bar of 10; the margin exceeds the permutation
  null's 99th percentile (10.325); effect size 1.475
  nats per token; inscription-cluster bootstrap 95%
  interval [14.75, 19.17], entirely above the bar. The
  candidate also beats the structural-only rival R-D
  (under the Stage 2 freeze §6 assignment rule every
  per-sign rival, R-D included, is the unconditioned
  model whose total is the best rival's). This is the
  in-corpus arm's ceiling outcome: a reportable
  discrimination result on pseudo-held-out data. Under
  spec §3.3 and claim C098-7 it supports **no standing
  change and no identification claim**; the sign's
  class is untouched by this study.
- **22 NOT IDENTIFIABLE.** The 17 by construction at
  Stage 2 (no accepted sheet; M124 among them, its
  actual count 13 confirming the sheet arm governs),
  the two signs displaced from their in-expectation
  UNDECIDABLE outcomes by the count test (M018: expected
  3.25, actual 7; M054: expected 3.5, actual 5 — both
  sheetless, so rule 2's sheet arm finalizes them), and
  the three scored signs that did not pass:
  - **M089** (tu/tū): 39 held-out tokens; penalized
    margin −7.384 nats (raw −5.384, 1 free choice);
    null 99th percentile 30.600; bootstrap interval
    [−35.72, 19.76]. The candidate's signature model
    fits the held-out contexts worse than the
    unconditioned rival, before any penalty.
  - **M267** (iN/in): 61 held-out tokens; penalized
    margin −109.458 nats (raw −107.458, 1 free choice);
    null 99th percentile 65.148; bootstrap interval
    [−153.84, −63.82], entirely negative. The filed
    slot pattern mispredicts on the corpus of record,
    as the pre-release record's development-side
    anatomy anticipated (the pattern's left flank is
    absent from this corpus; the candidate model rests
    on 1 assigned development occurrence). This outcome
    is about the filed prediction under the frozen
    machinery; it neither cites nor repairs M267's
    DEDR 494 leg, whose F-4 standing (GENITIVE_MARGINAL,
    not promoted; the leg not verifying as filed) is
    unchanged.
  - **M347** (ka): 18 held-out tokens; penalized margin
    −0.788 nats (raw 1.212, 1 free choice — the penalty
    is what carries it below zero); null 99th
    percentile 0.673. The raw margin exceeds its null
    percentile but the penalized margin is far below
    the 10-nat bar: the second conjunct cannot rescue
    the first. Its bootstrap interval is degenerate,
    [−0.788, −0.788], because every held-out occurrence
    carries the same per-occurrence difference (for
    these contexts the two models differ only through
    the smoothing denominator).
- **46 UNDECIDABLE AT THIS POWER** on the binding count
  test: actual held-out tokens below the frozen floor
  of 5. This includes M374 (actual 0; the T102 frozen
  default confirmed by the count test), the Arm E signs
  M047 (actual 3), M329 (2), and M330 (1), and the five
  below-floor sheeted signs (M005 1, M030 0, M037 0,
  M068 1, M075 3), whose accepted sheets therefore never
  governed and for whom no margin was computed (Stage 2
  freeze §6 precedence). Against Stage 2's in-expectation
  distribution (48 / 17 / 4 proceed), the count test
  moved exactly two signs (M018, M054, above) and
  confirmed the rest.

**The premise falsifier, applied as written (spec §4).**
The study's premise — that the frozen machinery can
discriminate at least some candidates from serious
rivals out of sample — is falsified if no sign reaches
its arm's pass outcome while TC-098-02 passes. TC-098-02
passed at adoption (`records/tc-execution-2026-11-21.md`)
and M375 reached DISCRIMINATED ON PSEUDO-HELD-OUT.
**The premise is not falsified.**

**R-E, the global permutation, scored as one model**
(Stage 2 freeze §5; construction in the pre-release
record §4): total held-out log-likelihood over all 69
signs — candidate system −2884.402, permuted system
−2772.078, unconditioned system −2800.120; the
system-level margin (candidate minus permuted) is
**−112.323 nats**. At system level the assignment does
not beat its permutation; the deficit is dominated by
M267 (its candidate model contributes −252.731 against
−145.273 under the permutation, a 107.458-nat swing,
the same misprediction the per-sign test records), and
the permutation also outscores M375's own model on
M375's occurrences (−37.040 against −45.941, under
M267's signature) — a wrong assignment producing a
sharp small-sample model, which is what the per-sign
null and bar, not the system total, exist to police.
R-E conditions no per-sign outcome, and none was
conditioned on it.

**Standing consequences: none.** This study changes no
standing, no anchor, and no other program record
(spec §1, claim C098-7). M375's outcome is a
discrimination result on pseudo-held-out data; any
future standing act on it is a separate program act,
not part of this study and not a remainder of it. The
claims adjudication on this outcome is Stage 4 (T401),
not performed here.

## Per-sign record

Threshold is the penalized-margin threshold in nats
against a zero-free-choice rival (10 + 2 × free
choices); MDM is that threshold divided by the sign's
**actual** held-out count, in nats per token. Margins
and null percentiles exist only for the four scored
signs and are in the data file and the scored-signs
table below; every other row's outcome follows from its
actual count and sheet determination under §4
precedence, as its basis states.

| Sign | Arm | Candidate value | Free choices | Threshold (nats) | Dev tokens | Expected held-out | Actual held-out | MDM at actual (nats/token) | Sheet determination | Stage 3 outcome |
|---|---|---|---|---|---|---|---|---|---|---|
| M002 | I | kuṉ | 1 | 12 | 11 | 2.75 | 4 | 3.000 | NOT_CONSTRUCTIBLE | UNDECIDABLE AT THIS POWER |
| M004 | I | kēḷ | 1 | 12 | 2 | 0.50 | 0 | undefined (no held-out tokens) | NOT_CONSTRUCTIBLE | UNDECIDABLE AT THIS POWER |
| M005 | I | kōṉ | 1 | 12 | 1 | 0.25 | 1 | 12.000 | ACCEPTED | UNDECIDABLE AT THIS POWER |
| M006 | I | puli | 0 | 10 | 4 | 1.00 | 0 | undefined (no held-out tokens) | NOT_CONSTRUCTIBLE | UNDECIDABLE AT THIS POWER |
| M007 | I | aaL | 0 | 10 | 3 | 0.75 | 1 | 10.000 | NOT_CONSTRUCTIBLE | UNDECIDABLE AT THIS POWER |
| M009 | I | āṇ | 0 | 10 | 7 | 1.75 | 4 | 2.500 | NOT_CONSTRUCTIBLE | UNDECIDABLE AT THIS POWER |
| M010 | I | paṭ | 0 | 10 | 4 | 1.00 | 0 | undefined (no held-out tokens) | NOT_CONSTRUCTIBLE | UNDECIDABLE AT THIS POWER |
| M013 | I | nakaram | 0 | 10 | 0 | 0.00 | 1 | 10.000 | NOT_CONSTRUCTIBLE | UNDECIDABLE AT THIS POWER |
| M014 | I | tiru | 0 | 10 | 12 | 3.00 | 0 | undefined (no held-out tokens) | NOT_CONSTRUCTIBLE | UNDECIDABLE AT THIS POWER |
| M015 | I | mā | 1 | 12 | 64 | 16.00 | 16 | 0.750 | NOT_CONSTRUCTIBLE | NOT IDENTIFIABLE |
| M016 | I | kaḷiṟu | 0 | 10 | 1 | 0.25 | 0 | undefined (no held-out tokens) | NOT_CONSTRUCTIBLE | UNDECIDABLE AT THIS POWER |
| M017 | I | kai | 0 | 10 | 66 | 16.50 | 18 | 0.556 | NOT_CONSTRUCTIBLE | NOT IDENTIFIABLE |
| M018 | I | nēr | 1 | 12 | 13 | 3.25 | 7 | 1.714 | NOT_CONSTRUCTIBLE | NOT IDENTIFIABLE |
| M020 | I | kuṉ | 1 | 12 | 0 | 0.00 | 1 | 12.000 | NOT_CONSTRUCTIBLE | UNDECIDABLE AT THIS POWER |
| M023 | I | vaḷ | 0 | 10 | 1 | 0.25 | 0 | undefined (no held-out tokens) | NOT_CONSTRUCTIBLE | UNDECIDABLE AT THIS POWER |
| M025 | I | cem | 0 | 10 | 27 | 6.75 | 9 | 1.111 | NOT_CONSTRUCTIBLE | NOT IDENTIFIABLE |
| M026 | I | mā | 1 | 12 | 0 | 0.00 | 1 | 12.000 | NOT_CONSTRUCTIBLE | UNDECIDABLE AT THIS POWER |
| M027 | I | māṟ | 1 | 12 | 2 | 0.50 | 0 | undefined (no held-out tokens) | NOT_CONSTRUCTIBLE | UNDECIDABLE AT THIS POWER |
| M029 | I | yānai | 1 | 12 | 2 | 0.50 | 0 | undefined (no held-out tokens) | NOT_CONSTRUCTIBLE | UNDECIDABLE AT THIS POWER |
| M030 | I | kō | 0 | 10 | 2 | 0.50 | 0 | undefined (no held-out tokens) | ACCEPTED | UNDECIDABLE AT THIS POWER |
| M032 | I | koL | 0 | 10 | 8 | 2.00 | 1 | 10.000 | NOT_CONSTRUCTIBLE | UNDECIDABLE AT THIS POWER |
| M034 | I | tōḷ | 0 | 10 | 2 | 0.50 | 0 | undefined (no held-out tokens) | NOT_CONSTRUCTIBLE | UNDECIDABLE AT THIS POWER |
| M037 | I | kēḷ | 1 | 12 | 1 | 0.25 | 0 | undefined (no held-out tokens) | ACCEPTED | UNDECIDABLE AT THIS POWER |
| M038 | I | pōr | 0 | 10 | 5 | 1.25 | 1 | 10.000 | NOT_CONSTRUCTIBLE | UNDECIDABLE AT THIS POWER |
| M041 | I | pēr | 0 | 10 | 9 | 2.25 | 3 | 3.333 | NOT_CONSTRUCTIBLE | UNDECIDABLE AT THIS POWER |
| M045 | I | yānai | 1 | 12 | 2 | 0.50 | 0 | undefined (no held-out tokens) | NOT_CONSTRUCTIBLE | UNDECIDABLE AT THIS POWER |
| M047 | E | min/mīn | 2 | 14 | 11 | 2.75 | 3 | 4.667 | NOT_CONSTRUCTIBLE | UNDECIDABLE AT THIS POWER |
| M049 | I | pu | 0 | 10 | 2 | 0.50 | 0 | undefined (no held-out tokens) | NOT_CONSTRUCTIBLE | UNDECIDABLE AT THIS POWER |
| M050 | I | pār | 0 | 10 | 30 | 7.50 | 10 | 1.000 | NOT_CONSTRUCTIBLE | NOT IDENTIFIABLE |
| M051 | I | pū/puḷ | 1 | 12 | 58 | 14.50 | 22 | 0.545 | NOT_CONSTRUCTIBLE | NOT IDENTIFIABLE |
| M052 | I | ta | 0 | 10 | 1 | 0.25 | 0 | undefined (no held-out tokens) | NOT_CONSTRUCTIBLE | UNDECIDABLE AT THIS POWER |
| M053 | I | mi | 1 | 12 | 86 | 21.50 | 22 | 0.545 | NOT_CONSTRUCTIBLE | NOT IDENTIFIABLE |
| M054 | I | mi | 1 | 12 | 14 | 3.50 | 5 | 2.400 | NOT_CONSTRUCTIBLE | NOT IDENTIFIABLE |
| M055 | I | miN3 | 0 | 10 | 1 | 0.25 | 1 | 10.000 | NOT_CONSTRUCTIBLE | UNDECIDABLE AT THIS POWER |
| M057 | I | māṭu | 0 | 10 | 5 | 1.25 | 2 | 5.000 | NOT_CONSTRUCTIBLE | UNDECIDABLE AT THIS POWER |
| M060 | I | kāṇṭāmirukam | 0 | 10 | 40 | 10.00 | 9 | 1.111 | NOT_CONSTRUCTIBLE | NOT IDENTIFIABLE |
| M061 | I | ka | 1 | 12 | 0 | 0.00 | 1 | 12.000 | NOT_CONSTRUCTIBLE | UNDECIDABLE AT THIS POWER |
| M062 | I | erutu | 0 | 10 | 25 | 6.25 | 6 | 1.667 | NOT_CONSTRUCTIBLE | NOT IDENTIFIABLE |
| M063 | I | mutalai | 0 | 10 | 2 | 0.50 | 0 | undefined (no held-out tokens) | NOT_CONSTRUCTIBLE | UNDECIDABLE AT THIS POWER |
| M065 | I | kuTam | 1 | 12 | 139 | 34.75 | 36 | 0.333 | NOT_CONSTRUCTIBLE | NOT IDENTIFIABLE |
| M066 | I | cōḻ | 0 | 10 | 11 | 2.75 | 3 | 3.333 | NOT_CONSTRUCTIBLE | UNDECIDABLE AT THIS POWER |
| M067 | I | kōṭṭāṉ | 0 | 10 | 158 | 39.50 | 45 | 0.222 | NOT_CONSTRUCTIBLE | NOT IDENTIFIABLE |
| M068 | I | maṟi | 0 | 10 | 7 | 1.75 | 1 | 10.000 | ACCEPTED | UNDECIDABLE AT THIS POWER |
| M069 | I | nēr | 1 | 12 | 2 | 0.50 | 1 | 12.000 | NOT_CONSTRUCTIBLE | UNDECIDABLE AT THIS POWER |
| M070 | I | vēl | 0 | 10 | 56 | 14.00 | 9 | 1.111 | NOT_CONSTRUCTIBLE | NOT IDENTIFIABLE |
| M073 | I | kōṉ | 1 | 12 | 2 | 0.50 | 3 | 4.000 | NOT_CONSTRUCTIBLE | UNDECIDABLE AT THIS POWER |
| M074 | I | ker | 0 | 10 | 2 | 0.50 | 0 | undefined (no held-out tokens) | NOT_CONSTRUCTIBLE | UNDECIDABLE AT THIS POWER |
| M075 | I | māṟ | 1 | 12 | 10 | 2.50 | 3 | 4.000 | ACCEPTED | UNDECIDABLE AT THIS POWER |
| M076 | I | naN | 0 | 10 | 12 | 3.00 | 2 | 5.000 | NOT_CONSTRUCTIBLE | UNDECIDABLE AT THIS POWER |
| M078 | I | cēr | 0 | 10 | 4 | 1.00 | 3 | 3.333 | NOT_CONSTRUCTIBLE | UNDECIDABLE AT THIS POWER |
| M080 | I | vēṅkai | 0 | 10 | 4 | 1.00 | 0 | undefined (no held-out tokens) | NOT_CONSTRUCTIBLE | UNDECIDABLE AT THIS POWER |
| M082 | I | pa | 0 | 10 | 1 | 0.25 | 0 | undefined (no held-out tokens) | NOT_CONSTRUCTIBLE | UNDECIDABLE AT THIS POWER |
| M089 | I | tu/tū | 1 | 12 | 119 | 29.75 | 39 | 0.308 | ACCEPTED | NOT IDENTIFIABLE |
| M099 | I | kol/koḷ | 1 | 12 | 426 | 106.50 | 118 | 0.102 | NOT_CONSTRUCTIBLE | NOT IDENTIFIABLE |
| M124 | E | kuTam | 1 | 12 | 43 | 10.75 | 13 | 0.923 | NOT_CONSTRUCTIBLE | NOT IDENTIFIABLE |
| M128 | I | kaṇ | 0 | 10 | 6 | 1.50 | 2 | 5.000 | NOT_CONSTRUCTIBLE | UNDECIDABLE AT THIS POWER |
| M130 | I | mui | 0 | 10 | 37 | 9.25 | 8 | 1.250 | NOT_CONSTRUCTIBLE | NOT IDENTIFIABLE |
| M145 | I | miṭ | 0 | 10 | 21 | 5.25 | 7 | 1.429 | NOT_CONSTRUCTIBLE | NOT IDENTIFIABLE |
| M151 | I | viḷ | 0 | 10 | 0 | 0.00 | 1 | 10.000 | NOT_CONSTRUCTIBLE | UNDECIDABLE AT THIS POWER |
| M194 | I | kaṭ | 0 | 10 | 34 | 8.50 | 10 | 1.000 | NOT_CONSTRUCTIBLE | NOT IDENTIFIABLE |
| M220 | I | al | 0 | 10 | 1 | 0.25 | 0 | undefined (no held-out tokens) | NOT_CONSTRUCTIBLE | UNDECIDABLE AT THIS POWER |
| M267 | I | iN/in (genitive) | 1 | 12 | 226 | 56.50 | 61 | 0.197 | ACCEPTED | NOT IDENTIFIABLE |
| M329 | E | poṉ | 1 | 12 | 4 | 1.00 | 2 | 6.000 | NOT_CONSTRUCTIBLE | UNDECIDABLE AT THIS POWER |
| M330 | E | can | 0 | 10 | 6 | 1.50 | 1 | 10.000 | NOT_CONSTRUCTIBLE | UNDECIDABLE AT THIS POWER |
| M347 | I | ka | 1 | 12 | 73 | 18.25 | 18 | 0.667 | ACCEPTED | NOT IDENTIFIABLE |
| M351 | I | vī | 0 | 10 | 1 | 0.25 | 0 | undefined (no held-out tokens) | NOT_CONSTRUCTIBLE | UNDECIDABLE AT THIS POWER |
| M374 | I | kul | 0 | 10 | 0 | 0.00 | 0 | undefined (no held-out tokens) | NOT_CONSTRUCTED | UNDECIDABLE AT THIS POWER |
| M375 | I | taṇ | 0 | 10 | 36 | 9.00 | 11 | 0.909 | ACCEPTED | DISCRIMINATED ON PSEUDO-HELD-OUT |
| M391 | I | ka/kaṇ | 1 | 12 | 136 | 34.00 | 39 | 0.308 | NOT_CONSTRUCTIBLE | NOT IDENTIFIABLE |

## Scored signs (the Stage 3 quantities)

| Sign | Held-out tokens | LL candidate | LL best rival | Raw margin | Penalized margin | Per-token | Null p99 | Bootstrap 95% CI (penalized) | Outcome |
|---|---|---|---|---|---|---|---|---|---|
| M089 | 39 | −183.988 | −178.604 | −5.384 | −7.384 | −0.189 | 30.600 | [−35.72, 19.76] | NOT IDENTIFIABLE |
| M267 | 61 | −252.731 | −145.273 | −107.458 | −109.458 | −1.794 | 65.148 | [−153.84, −63.82] | NOT IDENTIFIABLE |
| M347 | 18 | −61.005 | −62.217 | 1.212 | −0.788 | −0.044 | 0.673 | [−0.788, −0.788] | NOT IDENTIFIABLE |
| M375 | 11 | −45.941 | −62.165 | 16.224 | 16.224 | 1.475 | 10.325 | [14.75, 19.17] | DISCRIMINATED ON PSEUDO-HELD-OUT |

Every per-sign rival (R-A, R-B, R-C, R-D, and the Arm E
additions where they exist) takes the unconditioned
assignment under the Stage 2 freeze §6, so each rival's
log-likelihood equals the best rival's total in its row;
the raw data file records the shared total once, with
that rule stated. Reporting follows Standards Part II:
effect sizes (per-token margins) and bootstrap intervals
above; multiplicity family 69; precision basis the
actual held-out token counts.

## Run index (Spec 089 discipline; every attempt, failures included)

| Run | Mode | Payload verdict |
|---|---|---|
| study-20261122T162904Z-559728 | prepare (development-side executability; custody not read) | exit 0 — corpus pin, seal recomputation from the rule, grid reproduction, guard, free-choice cross-check, and model construction all pass |
| study-20261122T163036Z-d32312 | release (the single recorded release) | exit 0 — released=True, seal_verify=True, held=517, custody set equals the recomputed split |
| study-20261122T163043Z-c6e811 | score | exit 0 — scored=True, signs_scored=4, distribution {UNDECIDABLE AT THIS POWER: 46, NOT IDENTIFIABLE: 22, DISCRIMINATED ON PSEUDO-HELD-OUT: 1} |
| (verify invocation, 2026-11-22, after the score run) | verify | exit 0 — all 69 outcomes recomputed from the archived raw output under the reference `decide()` rule; mismatches none; distribution matches |

No failed attempts occurred. Wrapper states are not
verdicts; each row's verdict is the run's own payload
verdict (its exit code and verdict line).

**AI disclosure:** executed by an AI agent (Muse, via
Muse) at the direction of Tristen Pierson, per
constitution sec. VI.
