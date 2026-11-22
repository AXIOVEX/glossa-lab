# Q3 graph audit — completion record

Filed 2026-11-21 into the Spec 091 records. This record closes the one adjudicated-but-blocked unit of the Co-scientist audit adjudication of 2026-11-21 (`coscientist-audit-94-adjudication-2026-11-21.md`, Q3): the inference-log graph audit, blocked at adjudication because no inference log existed, and recorded as blocked again in the Round 1 dependency record (`dependency-record-2026-11-21.md`, PR #645).

**Inputs.** The inference log, Spec 099 Stage 1 (`specs/099-inference-log/records/inference-log.json`, landed by PR #651, merge `0d867479`): 94 entries, 299 items — 213 (a) primary, 61 (b) other-reading / candidate-system, 25 ambiguous. Executed classes are the post-Round-2 standings, 4 E + 65 I + 4 R + 3 P + 18 U (M044 adjudicated to U on 2026-11-21, `m044-addendum-adjudication-2026-11-21.md`). The audit is a pure function of the log (Spec 099 section 4): the full machine-readable result is `specs/099-inference-log/records/q3-graph-audit-2026-11-21.json`.

**Determinism (TC-099-03 at full scope).** The reference audit and the test file's independent implementation (written from the spec text; SCCs by pairwise reachability, not Tarjan) were both run over the real log: per-reading outcomes equal exactly, cycle sets equal exactly. Payload verdict of the reference run: DONE (class_changes_primary=0, weakened_primary=44, cycles=0, open_ends=38).

## Headline

- **Class changes implied: none.** Under the primary treatment (remove all (b) items), 0 of 94 readings would change class. Under the sensitivity treatment (remove (b) and ambiguous items), also 0. Every class-I reading retains at least one (a) item under both treatments.
- **Bases weakened: 44 of 94** under the primary treatment (by executed class: E 1, I 31, P 3, R 1, U 8); **63 of 94** under the sensitivity treatment. Losses are named per reading in the table below and in the audit JSON.
- **Cycles: none.** Over the named-target (b) edges (23 items, 34 named targets, 31 of them inside the 94), the strongly connected components are all singletons and there are no self-loops: the premise graph as filed is acyclic (computed, Spec 099 C099-6). Most-depended-on readings: M342 (10 in-edges), M267 (6 in-edges), M176 (6 in-edges).
- **Open ends: 38** (b) items name no target reading: 2 internal_label, 1 interpreted_anchor, 28 self_assertion, 7 slot_label. They are removed by the treatment like every (b) item; they simply contribute no graph edge.

## Does the spot-check hold?

The Co-scientist audit's Q3 spot-check reported: removing other-readings-as-evidence links changes no class, and weakens 12 named signs' bases (the adjudication executed that result over 12 items covering 17 readings). At full scope:

- **No class changes: HOLDS**, under both treatments, for all 94 readings, not only the spot-check's sample.
- **Weakened bases: the direction holds and the count grows, for stated reasons.** All 17 readings of the spot-check family are weakened at full scope. Counting only the spot-check's own premise family (interpreted-anchor and slot-label losses), the full-scope weakened count is 20: the 17, plus M165, M202 and M330, whose /su/ slot premises the spot-check items did not enumerate as removals for those readings themselves. The full primary count of 44 is larger because the log also counts two premise kinds the adjudication itself ruled on but the spot-check did not enumerate per reading: the 'has specific PDR reading' self-assertion (an input, not corroboration; 28 readings) and the internal functional labels of M176 and M342.

## Per-reading outcomes

Outcome vocabulary (Spec 099 section 4): class unchanged / basis weakened (lost items named) / class would change (destination named). No reading falls in the third category under either treatment. 'Lost' lists the item ids removed by that treatment.

| Sign | Class | Primary outcome | Lost (primary) | Sensitivity outcome | Lost (sensitivity) |
|---|---|---|---|---|---|
| M044 | U | unchanged | — | unchanged | — |
| M047 | E | unchanged | — | unchanged | — |
| M124 | E | unchanged | — | unchanged | — |
| M202 | U | unchanged, weakened | M202-02 | unchanged, weakened | M202-02 |
| M329 | E | unchanged | — | unchanged | — |
| M330 | E | unchanged, weakened | M330-02 | unchanged, weakened | M330-02 |
| M002 | I | unchanged, weakened | M002-02 | unchanged, weakened | M002-02 |
| M004 | I | unchanged, weakened | M004-02 | unchanged, weakened | M004-02 |
| M005 | I | unchanged, weakened | M005-02, M005-04 | unchanged, weakened | M005-02, M005-04 |
| M006 | I | unchanged | — | unchanged | — |
| M007 | I | unchanged | — | unchanged | — |
| M009 | I | unchanged, weakened | M009-02 | unchanged, weakened | M009-02 |
| M010 | I | unchanged, weakened | M010-02 | unchanged, weakened | M010-02 |
| M013 | I | unchanged | — | unchanged | — |
| M014 | I | unchanged, weakened | M014-02 | unchanged, weakened | M014-02 |
| M015 | I | unchanged, weakened | M015-02 | unchanged, weakened | M015-02 |
| M016 | I | unchanged | — | unchanged | — |
| M017 | I | unchanged, weakened | M017-02 | unchanged, weakened | M017-02 |
| M018 | I | unchanged, weakened | M018-02 | unchanged, weakened | M018-02 |
| M020 | I | unchanged, weakened | M020-02 | unchanged, weakened | M020-02 |
| M023 | I | unchanged, weakened | M023-02 | unchanged, weakened | M023-02 |
| M025 | I | unchanged, weakened | M025-02 | unchanged, weakened | M025-02 |
| M026 | I | unchanged, weakened | M026-02 | unchanged, weakened | M026-02 |
| M027 | I | unchanged, weakened | M027-02 | unchanged, weakened | M027-02 |
| M029 | I | unchanged | — | unchanged, weakened | M029-02 |
| M030 | I | unchanged, weakened | M030-02, M030-04 | unchanged, weakened | M030-02, M030-04 |
| M032 | I | unchanged | — | unchanged, weakened | M032-01 |
| M034 | I | unchanged, weakened | M034-02 | unchanged, weakened | M034-02 |
| M037 | I | unchanged, weakened | M037-02, M037-04 | unchanged, weakened | M037-02, M037-04 |
| M038 | I | unchanged, weakened | M038-02 | unchanged, weakened | M038-02 |
| M041 | I | unchanged, weakened | M041-02 | unchanged, weakened | M041-02 |
| M045 | I | unchanged | — | unchanged | — |
| M049 | I | unchanged | — | unchanged, weakened | M049-01 |
| M050 | I | unchanged, weakened | M050-02 | unchanged, weakened | M050-02 |
| M051 | I | unchanged | — | unchanged | — |
| M052 | I | unchanged | — | unchanged, weakened | M052-01 |
| M053 | I | unchanged | — | unchanged, weakened | M053-01 |
| M054 | I | unchanged | — | unchanged, weakened | M054-01 |
| M055 | I | unchanged | — | unchanged, weakened | M055-01 |
| M057 | I | unchanged | — | unchanged | — |
| M060 | I | unchanged | — | unchanged | — |
| M061 | I | unchanged | — | unchanged, weakened | M061-01 |
| M062 | I | unchanged | — | unchanged | — |
| M063 | I | unchanged | — | unchanged | — |
| M065 | I | unchanged | — | unchanged | — |
| M066 | I | unchanged, weakened | M066-02 | unchanged, weakened | M066-02 |
| M067 | I | unchanged | — | unchanged | — |
| M068 | I | unchanged, weakened | M068-01, M068-03 | unchanged, weakened | M068-01, M068-03 |
| M069 | I | unchanged, weakened | M069-02 | unchanged, weakened | M069-02 |
| M070 | I | unchanged, weakened | M070-02 | unchanged, weakened | M070-02 |
| M073 | I | unchanged | — | unchanged | — |
| M074 | I | unchanged | — | unchanged | — |
| M075 | I | unchanged, weakened | M075-02, M075-04 | unchanged, weakened | M075-02, M075-04 |
| M076 | I | unchanged | — | unchanged, weakened | M076-01 |
| M078 | I | unchanged, weakened | M078-02 | unchanged, weakened | M078-02 |
| M080 | I | unchanged | — | unchanged | — |
| M082 | I | unchanged | — | unchanged | — |
| M089 | I | unchanged, weakened | M089-03, M089-05, M089-07 | unchanged, weakened | M089-03, M089-05, M089-07 |
| M099 | I | unchanged | — | unchanged | — |
| M128 | I | unchanged | — | unchanged, weakened | M128-02 |
| M130 | I | unchanged | — | unchanged, weakened | M130-01 |
| M145 | I | unchanged | — | unchanged, weakened | M145-01, M145-03 |
| M151 | I | unchanged | — | unchanged | — |
| M194 | I | unchanged | — | unchanged, weakened | M194-01, M194-03 |
| M220 | I | unchanged | — | unchanged | — |
| M267 | I | unchanged, weakened | M267-05 | unchanged, weakened | M267-04, M267-05 |
| M347 | I | unchanged, weakened | M347-01, M347-03 | unchanged, weakened | M347-01, M347-03 |
| M351 | I | unchanged | — | unchanged | — |
| M374 | I | unchanged, weakened | M374-03 | unchanged, weakened | M374-03 |
| M375 | I | unchanged, weakened | M375-04 | unchanged, weakened | M375-04 |
| M391 | I | unchanged | — | unchanged | — |
| M087 | R | unchanged | — | unchanged, weakened | M087-01 |
| M165 | R | unchanged, weakened | M165-03 | unchanged, weakened | M165-01, M165-03 |
| M264 | R | unchanged | — | unchanged, weakened | M264-01 |
| M311 | R | unchanged | — | unchanged, weakened | M311-01 |
| M222 | P | unchanged, weakened | M222-01 | unchanged, weakened | M222-01, M222-02 |
| M362 | P | unchanged, weakened | M362-03 | unchanged, weakened | M362-03 |
| M398 | P | unchanged, weakened | M398-03, M398-05 | unchanged, weakened | M398-03, M398-05, M398-06 |
| M012 | U | unchanged | — | unchanged | — |
| M039 | U | unchanged | — | unchanged | — |
| M042 | U | unchanged | — | unchanged, weakened | M042-01 |
| M046 | U | unchanged | — | unchanged, weakened | M046-01 |
| M048 | U | unchanged, weakened | M048-03, M048-05, M048-07 | unchanged, weakened | M048-03, M048-05, M048-07 |
| M059 | U | unchanged | — | unchanged | — |
| M077 | U | unchanged, weakened | M077-02 | unchanged, weakened | M077-02 |
| M108 | U | unchanged | — | unchanged, weakened | M108-01 |
| M162 | U | unchanged | — | unchanged | — |
| M176 | U | unchanged, weakened | M176-01 | unchanged, weakened | M176-01 |
| M233 | U | unchanged | — | unchanged | — |
| M305 | U | unchanged, weakened | M305-02, M305-04, M305-06 | unchanged, weakened | M305-02, M305-04, M305-06 |
| M328 | U | unchanged | — | unchanged | — |
| M336 | U | unchanged, weakened | M336-03, M336-05, M336-06 | unchanged, weakened | M336-03, M336-05, M336-06 |
| M342 | U | unchanged, weakened | M342-01 | unchanged, weakened | M342-01 |
| M367 | U | unchanged, weakened | M367-03, M367-05, M367-06 | unchanged, weakened | M367-03, M367-05, M367-06 |

Divergent readings (sensitivity outcome differs from primary, in every case only by additionally losing ambiguous score items): 23 — M029, M032, M042, M046, M049, M052, M053, M054, M055, M061, M076, M087, M108, M128, M130, M145, M165, M194, M222, M264, M267, M311, M398.

## M267 dependency statement (deliverable 4 of the F-4 commission)

From the log, M267's filed basis carries exactly one (b)-type premise and one ambiguous premise:

- **(b) M267-05, the slot-label premise.** The filed pattern [AGENT]-M267-[TITLE] reads M267 as the genitive between an AGENT slot and a TITLE slot. The slots are constructs of the candidate system, and the pattern's markers are themselves readings: the AGENT markers of record include M176 and M328, the TITLE markers M099 and M073 (standings supplement section 2). The adjudication's words stand: conditional circularity — not independent confirmation unless the labels are independently justified. Under the primary treatment this item is lost (M267-05); under sensitivity, M267-04, M267-05 are lost. M267's outcome under both: class unchanged, basis weakened.
- **Ambiguous M267-04, the Phase-64 score=7.0.** An internal candidate-system score whose inputs the filed basis does not state.

What survives removal, and what a dependency-aware retest must therefore hold fixed or exclude:

1. The retest may not use the [AGENT]-[TITLE] pattern statistic as confirmation of the genitive reading while the slot labels rest on M176, M328, M099 and M073 under their current readings; either the markers' readings are independently justified first, or the pattern is recomputed over uninterpreted sign positions only.
2. The surviving (a) inputs are: the raw corpus counts (freq=400 in the Holdat corpus, across all motif types — subject to the Holdat custody position: the corpus is unheld in every working clone and no written Miller permission is on file), DEDR 494, and the raw pattern counts as they stand in the supplement (26 observed against a null mean of 6). The Phase-74 figures as originally filed (4.3x lift, z = 8.038) remain withdrawn as evidence and may not re-enter as retest inputs.
3. The Phase-64 score may not be used as a retest input until its inputs are stated in the record.
4. No retest is run or designed in executable detail by this record (Spec 099 C099-7); the retest is a separate commission.

## Non-effects

This audit reports; it moves nothing. No standing, class, anchor, or register entry is altered by this record, and no class change is implied that would need executing: the audit implies none. The adjudication's Q3 unit is closed by this filing; the standings-basis acts the adjudication already executed (premises struck, counts retained as unverified observations) are untouched.

## Round 4 scope note (2026-11-21, Red Team Round 4 — RT4-01, RT4-08)

Appended by the Round 4 adjudication; the record above is
unedited. Two qualifications govern every future citation
of this audit's headline.

**The honest citation form for the Q3 result is:**
*stripping every reading-on-reading premise changes no
class under the audit's class rules (0 of 94 under both
treatments) and weakens 44 of 94 bases (63 counting
ambiguous premises); the E quarter of the no-change result
is structural, since §4.2 makes E immovable, and M047's
logged basis contains no external-support item.*

On M047: class E's landed definition is register-level
(external-support claims on file, unverified, NOT
IDENTIFIABLE), and a claim is on file for M047 — its
Parpola 1994 §10.1 leg was re-verified VERIFIED AS FILED
(provenance only), with the limits stated in the
re-verification record (the proposal is class-level for
the fish-sign family; the step from the crosswalk's sign
identity to that proposal is the program's own step). But
M047's derivation, as itemized in the log, contains no
external-support item: one superseded positional item and
one crosswalk identity. Whether the register-level or the
derivation-level reading of the definition governs is a
definition question the landed rule does not settle; it is
flagged for the owner (Round 4 flag F-9) with a
recommendation, and **no standing is moved by this note**.
M330 is the second exposure under the same question.

On the census: the Inputs paragraph above states the log
as first landed (299 items). The log has since been
repaired under `specs/099-inference-log/records/inference-log-amendment-2026-11-21.md`
(three DEDR double-citations merged per spec section 3.2)
and counts 296 items; the audit was regenerated over the
repaired log and every outcome in this record is unchanged
(0 class changes under both treatments; weakened 44 / 63;
acyclic), because every merged item is an (a) item.

**F-9 note (2026-11-22).** The definition question flagged
above is settled: on 2026-11-22 the owner adopted the
itemization test, and the directed re-examination
reclassed M047 from E to U — its filed basis holds no
itemized external-support item, and no internal motivation
for the reading remains on it
(`specs/091-anchor-comparison-integrity/records/f9-itemization-adjudication-2026-11-22.md`).
The standings of record are now 3 E + 65 I + 4 R + 3 P +
19 U = 94. The audit was regenerated over the amended log
(`specs/099-inference-log/records/inference-log-amendment-2026-11-22.md`)
and every outcome in this record is unchanged (0 class
changes under both treatments; weakened 44 / 63;
acyclic), because M047's entry holds no (b) or ambiguous
item under either class.

**M048 note (2026-11-22).** The standings moved once
more: M048's corrected battery result (F-4 commission;
score 2, promotion threshold met) triggered the
re-adjudication RT2-08 had attached to that outcome,
and M048 was reclassed from U to I
(`specs/091-anchor-comparison-integrity/records/m048-readjudication-2026-11-22.md`).
The standings of record are now 3 E + 66 I + 4 R + 3 P
+ 18 U = 94. The audit was regenerated over the amended
log
(`specs/099-inference-log/records/inference-log-amendment-2026-11-22.md`)
and every outcome in this record is unchanged (0 class
changes under both treatments; weakened 44 / 63;
acyclic): M048's outcome is unchanged and weakened
under both treatments under either class, its entry's
item shape being the same as M089's, whose class I
rests on a filed corrected-battery result at the same
threshold.
