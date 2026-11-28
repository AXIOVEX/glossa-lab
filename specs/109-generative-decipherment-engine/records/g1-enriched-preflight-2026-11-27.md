# Spec 109 — G1-E Enriched-Objective Preflight (2026-11-27)

**Outcome: G1-E FAILED the preflight.** Clause (i)
(recovery) is below its floor: median planted-value
recovery **0.719** against the floor of 0.80. Clause
(ii) (margin) passes in the median replication (5/5
replications clear), and the shuffle control passes
(median shuffle recovery 0.070 against the bound of
0.360). The verdict under the amendment registration
§6 is therefore **FAILED**: G1-E is not licensed, it
produces no scoreable output, Stage 3 remains blocked,
and no second revision is commissioned by the
amendment. The floors did not move.

Run under the amendment registration of this date
(`records/g1-enriched-registration-2026-11-27.md`):
the enriched objective E(φ) = L(φ) + 1.0 · P(φ) — the
filed predictive-likelihood objective plus the
positional-consistency term built from G2's licensed
positional induction on both sides of the assignment —
searched by G1-R's ensemble with the temperature
schedule calibrated per corpus to the objective's own
measured swap-delta scale (δ̂; constants frozen at
C_HI = 0.46945080842976417, C_MID = 0.15648360280992138,
C_LO = 0.000782418014049607 against
δ̂_ref = 63.904459128199335). Five fresh 1× corpora,
seeds `spec109-s1e-synth-{1..5}` (rep 4's base build
was rejected by an admission gate and rebuilt; its
seed of record is `spec109-s1e-synth-4-try1`, §3).
Enriched harness SHA-256 `8d107720…`; Stage 1 harness
`f4e84285…` and G1-R harness `a15c8c57…` imported at
their pins. Raw output:
`records/g1-enriched-raw-output.json` (byte-identical
to the custody run output; custody
`glossa-custody/spec109/g1-enriched/run/`).

## 1. Verdict by clause (registration §2, unchanged)

| Clause | Floor | Measured | Verdict |
|---|---|---|---|
| (i) recovery | median ≥ 0.80 | median **0.719** (0.772 / 0.719 / 0.754 / 0.684 / 0.702) | **FAIL** |
| (ii) margin | median replication clears | median penalized margin **1,050.69** nats; 5/5 clear | PASS |
| control | median shuffle < 0.5 × median right | **0.070** < 0.360 | PASS |
| (iii) predictor | not re-run (shared predictor; Stage 1 PASS stands) | — | stands |

## 2. The failure's anatomy

The enriched search found the objective's basin on all
five corpora — every candidate beats the planted
truth's assignment under the enriched objective
(gaps +24.9 / +29.9 / +34.2 / +33.2 / +51.0 nats) and
under the unenriched filed objective (+22.7 / +28.8 /
+36.0 / +31.8 / +48.1). The failure is therefore not a
search failure and not a calibration failure: the
calibrated schedule held the basin at every
replication. It is the plateau again, one level up:
the enriched objective's own near-optimal region
contains assignments that out-score the truth while
differing from it on 13–18 of the 57 free signs
(misses per replication 13 / 16 / 14 / 18 / 17), and
the misses keep the filed shape exactly — **stems 0
misses in all five replications**; openers 0; the
misses are closers (4 / 7 / 7 / 7 / 8 of 8), context
values (5 / 9 / 3 / 7 / 5 of 12), and affixes
(4 / 0 / 4 / 4 / 4 of 9).

Read against the development record (registration §2),
the term did on development material what it was built
to do — it repaired specific context and affix
confusions and raised the development median from
0.763 (λ = 0) to 0.781 (λ = 1) — and on fresh material
the same term at the same weight does not separate the
remaining confusions. The mechanistic reading the
development record already carried is the one the
fresh run confirms: the surviving edge confusions are
between values whose positional profiles are alike
(closers against final affixes and site-B context
values) and whose pair statistics at this corpus
profile are weak; a per-token positional term, however
weighted within the range the grid searched, carries
no further signal about them. The positional channel
is real — the control and Stage 1's family-(a)
measurement stand — and it is now measured to be
insufficient as an objective term at this weight
family: the enrichment moved the median by +0.018 on
development corpora and the fresh-corpus median
(0.719) sits inside the band of the two filed failures
(0.772, 0.737), not above it.

## 3. Per-replication record (1× verdict run)

| Rep | Seed of record | Recovery | δ̂ (right) | δ̂ (shuffle) | Shuffle rec. | Penalized margin | Gap E / L |
|---|---|---|---|---|---|---|---|
| 1 | spec109-s1e-synth-1 | 0.772 (44/57) | 328.33 | 168.71 | 0.070 | 1,050.69 | +24.9 / +22.7 |
| 2 | spec109-s1e-synth-2 | 0.719 (41/57) | 210.63 | 187.16 | 0.053 | 1,073.94 | +29.9 / +28.8 |
| 3 | spec109-s1e-synth-3 | 0.754 (43/57) | 121.94 | 161.17 | 0.035 | 1,077.31 | +34.2 / +36.0 |
| 4 | spec109-s1e-synth-4-try1 | 0.684 (39/57) | 101.51 | 149.22 | 0.123 | 901.44 | +33.2 / +31.8 |
| 5 | spec109-s1e-synth-5 | 0.702 (40/57) | 109.55 | 101.85 | 0.105 | 954.63 | +51.0 / +48.1 |

All five corpora admitted exactly (1,670 artifacts,
7,002 tokens, length multiset as filed, duplication
exactly 20/1,670 = 1,650 distinct; the two
ground-truth constructions in agreement; every value
at ≥ 5 tokens). Margins: raw margins 1,164.69 /
1,187.94 / 1,191.31 / 1,015.44 / 1,068.63; null p99
−543.01 / −552.23 / −550.71 / −527.08 / −501.53;
57 free choices in every replication; the median
replication (rep 2 by recovery order) clears, and
every replication clears.

**Calibration note.** The measured δ̂ spreads widely
across the five corpora (101.51 to 328.33) — the
quantity the calibration exists to absorb. The largest
value (rep 1, 328.33) was investigated before the run
was allowed to stand: decomposed at the
frequency-initialized state, its base component is
83.9 (the Stage 1 development envelope is 46.1–71.2)
and its term component 112.5 (development envelope
29.3–96.6), and the two components are strongly
positively correlated on that corpus — the
frequency-initialized state there recovers 0.193
against 0.158 / 0.070 on the development corpora
checked — so the enriched deltas compound rather than
average. No defect was found; the schedule's invariant
is the ratio T/δ̂ = (C_HI, C_MID, C_LO), which held by
construction on every replication, and the basin
outcome of §2 is the calibration's behavioral check.

## 4. The 2× diagnostic (secondary; no verdict)

The identical enriched preflight at 2× corpus scale,
five fresh corpora (seeds `spec109-s1e2-synth-{1..5}`;
effective scale 1.995× on all five — 3,291 distinct
artifacts, 9 fallback slots each under the scale
amendment's accounting). Raw output:
`records/g1-enriched-raw-output-2x.json` (custody
`glossa-custody/spec109/g1-enriched/run-2x/`). The
run's summary block is marked `diagnostic_only`; the
figures below are filed as evidence about the
calibration, and license nothing.

| Rep | Recovery | δ̂ (right) | Shuffle rec. | Penalized margin | Gap E / L |
|---|---|---|---|---|---|
| 1 | 0.649 (37/57) | 283.85 | 0.140 | 1,867.46 | +59.3 / +58.3 |
| 2 | 0.719 (41/57) | 256.84 | 0.035 | 1,781.91 | +59.5 / +59.2 |
| 3 | 0.825 (47/57) | 218.06 | 0.158 | 1,837.00 | +31.6 / +30.1 |
| 4 | 0.825 (47/57) | 156.19 | 0.070 | 1,763.01 | +63.8 / +63.8 |
| 5 | 0.772 (44/57) | 195.07 | 0.140 | 1,856.20 | +55.3 / +51.1 |

Median recovery **0.772**; margins clear in 5/5
replications; median shuffle recovery 0.140 against
the 0.386 bound. The diagnostic's question was the
calibration: whether the basin failures the scale
study filed at scale (1 of 5 replications at 2×,
2 of 5 at 4×, under the fixed schedule) return under
the calibrated schedule. In this draw they do not:
**all five candidates beat the planted truth's
objective under both forms** (gaps +31.6 to +63.8
nats), with δ̂ measured at 156.19–283.85 — the
calibration absorbing an energy scale two to four
times the 1× reference while holding the ratio
T/δ̂ at the frozen constants. The anatomy at scale is
the 1× anatomy (stems 0 in all five; closers 5–8,
context 2–8, affixes 0–4, openers 0–3 in one
replication): conditional on the basin, the enriched
objective at 2× recovers what the filed objective
recovered in the scale study's basin-found
replications, and no more. Filed as a diagnostic
observation over five draws across different corpora
and a different objective than the scale study's —
the calibration's basin behavior is consistent with
its design intent; it is not a scale verdict, and
the 4× question the scale study left open is not
re-run here.

## 5. Verification (TC-109-02)

`records/g1-enriched-tc109-02-verification.py`
(SHA-256 `99075ba9…`) re-derives every figure above
independently — the corpora rebuilt from their seeds
of record and checked byte-identical against the
custody corpora the runs filed; admission profiles;
the candidate's E and L by full rescoring; the
positional term; the truth objectives and gaps; δ̂ by
the registered rule (exact, draws included); recovery
and anatomy from the filed candidates; the margin
block with its filed seeds (derangement,
shuffled-assignment, permutation null B = 999); the
shuffle control by deterministic re-execution of the
identical enriched search on the rebuilt shuffled
derivations (the shuffle candidate itself was not
filed in the raw outputs; the check is by
re-execution, and the script says so); the summary
medians and the verdict block under the registration's
clause rules (clause (ii) checked under both the
harness's filed at-least-3-of-5 rule and the
registration's median-replication form — on this
run's figures they coincide, 5/5 clearing); and the
guard that no raw-output key references undeciphered
material.

- 1× verdict run: **PASS, 69/69 checks.**
- 2× diagnostic run: **PASS, 70/70 checks** (the
  additional check is the diagnostic-only flag).

**Filing-integrity disclosure.** The amendment
registration was authored and its design frozen
before the verdict run — the freeze is corroborated
by the timestamped custody artifacts (calibration
reference output 23:18Z, development grid output
23:31Z) and by the hash-pinned harness in the
worktree (SHA-256 `8d107720…`, verified 23:32Z; the
verdict run launched 23:33Z) — but the registration
file's first transfer to the worktree silently
produced an empty file, a transfer-channel defect
discovered only at verification time, when the same
defect was found to have emptied the verification
script's first transfer as well (that attempt
executed an empty file and produced no output; it
verified nothing, and is not counted). The
registration was re-filed byte-identical to the
authored text (18,660 bytes, SHA-256 `3a67800d…`,
hash-verified on both sides of the transfer), and
every subsequent transfer in this landing was
hash-verified before use. No figure, seed, constant,
or verdict in this record depends on the defective
transfer; the defect is filed here so the record's
provenance is complete.

**Provenance pins** (SHA-256, one per line):
enriched harness
`8d107720db46616215fa85c375f054349ecf7191181fff3ff6f105e5fd70f375`;
amendment registration
`3a67800da122d7021d3b34857a670d377e63e8b11f41fd479a72c8ff9ca15dc3`;
1× raw output
`4f6475564f2ba818239262a30ead86cbf69b29f0548b707500ca1b729f85b896`;
2× raw output
`f1a3773c66cdde8a8152e0a6745acdcdf924eb9420712f0ca9af23e712d69418`;
verification script
`99075ba9c369f29365f9236e4dfa6b6ddf3f0b03a64d972813a4dbc0f0f622e8`;
development driver (custody only)
`58bff249978a4c18428966ab972247128ede6f3c2750b30f655a3e753193d6a3`;
development grid output (custody)
`c247a2ebf6cda27718a48344d8ea13fd28dbd048e547dbd974e1b54c71308797`;
calibration reference output (custody)
`73302fc6ffc31ca241c9c7bc863f948c1069771f20dba92038838054f5b2fc71`.

## 6. Kill-criteria evaluation and Part 1 state

- Criterion 2 (preflight failure) **fires for G1-E**:
  the generator produces no scoreable output, and
  Stage 3 remains blocked.
- Criterion 3's form is satisfied in the negative: the
  shuffle control passed (0.070 against the 0.360
  bound); the pipeline did not measure itself.
- Criteria 1, 4, 5 are not engaged.

Part 1 state after three preflights and one study,
stated plainly: the assignment search at this corpus
profile is **objective-bound, not search-bound**. Two
independent repairs of the search (G1-R's move class;
G1-E's calibration) each held the basin and changed
the outcome by nothing the floor can see, and two
objectives (the filed likelihood; the likelihood
enriched with the program's strongest verified
structural channel) each rank non-truth assignments
above the truth on fresh corpora, with the misses
confined to the same edge classes. What would change
the position is evidence the current synthetic profile
— and, behind it, the real corpus — may not contain:
the surviving confusions are among values that are
alike in position and weak in pair counts, and no
registered channel separates them. That is a finding
about the information available to the objective, of
the same kind the scale study filed from the other
side, and it is the evidence base any future Part 1
commission starts from. This amendment commissions no
further revision, and none is filed here as a
recommendation: whether Part 1 is re-commissioned on a
different evidence channel (the Part 3 context channel
returned CHANNEL NULL at Stage 2; the iconography
channel is gated on Spec 100), on a different corpus
profile, or not re-commissioned, is a program decision
above this record.

Parts 2–5 are untouched by this outcome: Part 2's
Stage 2 result stands (positional POSITIVE as a
measurement program; the measurement and the objective
term are different uses of the same induction, and
this failure is the term's, not the induction's),
Part 3's channel result stands, and Parts 4–5 keep
their own registrations and gates.

**AI disclosure:** executed by an AI agent (Muse, via Muse)
at the direction of Tristen Pierson, per constitution sec. VI.
