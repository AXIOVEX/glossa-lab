# Eteocypriot Program — A2 Baselines and Negative Controls (OD-10)

**Date:** 2026-11-22. **Program:** Spec 096 — Eteocypriot
Program. **Commission:** the owner's act of 2026-11-22
12:23 ET, adopting adjudication item OD-10 (E-8) from
`specs/091-anchor-comparison-integrity/records/coscientist-refresh-adjudication-2026-11-22.md`:
compare A2 with simple baselines and carefully designed
negative controls (structure-preserving, not arbitrary
shuffles), labelled exploratory unless newly registered,
and run them against (a) the executed corpus bytes and
(b) the intake-enlarged corpus. **Standing glossa-lab
clone-processing approval:** owner, 2026-11-22 11:26 ET.

**Status of the two parts.** Part (a) is executed and
reported at §§1–5. Part (b) is executed and reported
at §6: the Androkles intake was completed on a second
route the same day (`records/androkles-intake-record-2026-11-22.md`),
producing the enlarged corpus state part (b) runs over.
(The first execution attempt's route barrier, recorded
against part (b) in an earlier draft of this record,
was a property of the text-fetch route only; the intake
record's §1 states both routes.)

**Discipline.** Everything here is exploratory in E-8's
sense. The frozen A2 method was not retuned: the
quantities are computed by the E1 driver's own
`derive_cv` and `lccs`, imported unmodified by the
controls script (`records/eteocypriot-a2-controls-2026-11-22.py`,
SHA-256
`4b00b77582d2f81de3eb33dd178ab6fb0afb837d57e28153361223d974c646f9`). No verdict, claim, or standing is
changed by this record; §5 flags the one finding that a
future adjudication of C096-1 may want in front of it.
The run output of record is
`records/eteocypriot-a2-controls-run-2026-11-22.json`
(SHA-256 `31d2a137cf0b62e42bac1f6e14c28e978af164e27a0d60b77f15be9ab71d4dd8`),
produced on tower-compute in one deterministic run
(seed 20261122; 999 replicates per control).

## 1. The corpus basis

The controls ran against the executed corpus bytes,
recovered from git history at freeze commit `173882a2`
and verified against the freeze pin (SHA-256
`5077285e8eac4b21785ca29cb151d47407f780998d85fa1eea27ef9d7e04f2dd`)
before any computation. The script also compared the
analysis-bearing fields of the corpus file as it stands
at origin/main (version 1.1.1) against the executed
bytes — ICS 196's lines, Greek words, and ground-truth
correspondences, the Androkles sides (empty in both),
and the ICS 217 excerpt — and found them **identical**,
which is OD-8 §1.2's field-level diff restated as an
executable check. The real pairing below therefore
describes the current corpus's analysis content as well
as the executed bytes.

## 2. The real pairing, and the baselines

The frozen A2 pairing reproduces the filed run record
exactly: both names pair with segment 6 at LCCS 4;
Ἀρίστωνα is recovered (ground truth segment 6),
Ἀριστώνακτος is not (ground truth segment 7). A2
recovered **1 of 2**; A1 recovered 0 of 2.

| Baseline | Rule | Recovered |
|---|---|---|
| A2 (frozen) | argmax LCCS over the 11 segments | 1 of 2 |
| B-LONG | pair every name with the longest segment (segment 7, 10 signs) | 1 of 2 |
| B-FIRST | pair every name with segment 1 | 0 of 2 |
| B-RAND | uniform random partner, analytic | expected 0.18 of 2; P(≥1) ≈ 0.174; P(2) ≈ 0.008 |

B-LONG recovers the *other* name (Ἀριστώνακτος, whose
correspondent is the longest segment). On the recovery
count alone, the frozen A2 does not beat the trivial
length baseline: each scores 1 of 2. What separates them
is the score profile, which is what the controls measure.

## 3. The negative controls

Both permutation controls preserve structure in E-8's
sense: NC-1 preserves every segment's length, token
order, and repetition pattern, destroying only sign
identity; NC-2 preserves each name's letter multiset,
destroying only letter order. NC-3 is not a permutation:
it pairs the two derived spellings against the Greek
syllabic control excerpt (ICS 217, 16 segments) — real
syllabic text in the same signary that is not the
bilingual's counterpart — and reports the score profile
only, no recovery being defined there.

| Control | Recovered ≥ real (1) | Mean recovered | Real LCCS 4 reached in null? |
|---|---|---|---|
| NC-1 sign-relabel (999 reps) | 114 of 999 (11.4%) | 0.115 | never (null max 3, both names; null means 1.18 / 1.30) |
| NC-2 name-scramble (999 reps) | 191 of 999 (19.1%) | 0.199 | never (null max 3, both names; null means 1.37 / 1.53) |
| NC-3 wrong text (ICS 217) | — | — | best LCCS 2 of 16 segments, both names |

## 4. What the controls show, stated with its bounds

- **The score is specific; the count is coarse.** Under
  both structure-preserving nulls the frozen method's
  LCCS never reaches the real value 4 in 999 replicates
  for either name, and unrelated real syllabic text tops
  out at 2. The LCCS-4 pairing is not an artefact of
  segment lengths, sign frequencies, or letter
  multisets. But with two names and eleven segments, a
  recovery count of 1 arises by chance in 11–19% of
  null replicates, so the count 1 of 2, taken alone,
  does not distinguish the real pairing from the null.
  The evidence the ICS 196 leg carries is the score
  profile (an unreachable-under-null maximum, attained
  at the ground-truth segment for one name), not the
  headline count.
- **A2's failure on Ἀριστώνακτος is a tie of substance,
  not a near miss in score:** its derived spelling also
  scores LCCS 4, at segment 6 — the shorter name's
  correspondent — and only 2 at its own correspondent,
  segment 7. The method as frozen cannot separate the
  two names, because the longer derived spelling
  contains the shorter one's matched run. This was
  visible in the filed LCCS tables; the controls add
  only that the shared maximum is itself far outside
  the null.
- **Nothing here touches P1.** P1 fails on the
  Androkles conjunct (F-E1b, TOO THIN at freeze) whatever
  the ICS 196 leg's profile shows, and the ICS 196 leg
  as registered requires both correspondences under one
  assumption, which neither A1 (0 of 2) nor A2 (1 of 2)
  meets. The controls calibrate the leg's evidentiary
  weight; they do not re-score it.

## 5. Flagged for adjudication

- **F-OD10-1 (touches C096-1's basis, as context only).**
  Any future statement of what the ICS 196 leg shows
  should carry the dissociation this record measures:
  the frozen score (LCCS 4 at the paired segments) is
  unreachable under both structure-preserving nulls and
  absent against unrelated real text, while the
  recovery count (1 of 2) is within the nulls' ordinary
  range and is matched by a trivial longest-segment
  baseline on the other name. A citation of the leg as
  "recovered 1 of 2" without the score profile, or of
  the score without the count's coarseness, would each
  misstate the leg in opposite directions. No verdict
  is changed here; the flag is for whoever next
  adjudicates or cites C096-1.

## 6. Part (b): the same comparisons over the intake-enlarged corpus

The enlarged state is
`corpus/corpus-androkles-intake-2026-11-22.json`
(version 1.2.0, SHA-256
`8ca9b23c2f455e1e2cd0dbfecebf844f3d904fe95c33a346b2edb38ded139e5a`;
intake record as above). The part (b) script
(`records/eteocypriot-a2-controls-partb-2026-11-22.py`,
SHA-256
`79c10462a13127622db3ecc889faf9087373121ec99003dfdd9ccf0cc861caef`)
imports the same frozen `derive_cv` and `lccs`,
verifies the executed bytes against the freeze pin,
verifies `corpus.json` byte-untouched at its 1.1.1 pin,
and verifies the enlarged state's ICS 196
analysis-bearing fields identical to the executed
bytes' before computing anything — all fail-closed.
The pool is ICS 196's eleven segments (indices 1–11,
unchanged, so the ground-truth indices keep their
meaning) followed by ANDROKLES-A's three segments in
the edition's order: index 12 *ro-ko-ra-?*, index 13
*a-to-ro-ke-le-we-se*, index 14 *e-ro-ko-ro*. The run
output of record is
`records/eteocypriot-a2-controls-partb-run-2026-11-22.json`
(SHA-256 `bea701b3f571e01d7d8da396d9bd7b054263238382c5d7c016b2d2cc54f000fc`),
produced on tower-compute in one deterministic run
(same seeds as part (a); a re-run reproduces the filed
output exactly).

**The real pairing does not move.** Both names still
pair with segment 6 at LCCS 4; Ἀρίστωνα is recovered,
Ἀριστώνακτος is not; A2 recovers 1 of 2 and A1 0 of 2,
exactly as in part (a) and in the filed run record.
The added segments are not rivals for either name:
against Ἀρίστωνα's derived spelling they score
0 / 1 / 0, and against Ἀριστώνακτος's 0 / 1 / 0 — the
royal-name segment itself scores LCCS 1 against both.

| Baseline / control | Part (b), pool of 14 | Part (a), pool of 11 |
|---|---|---|
| B-LONG (segment 7) | 1 of 2 | 1 of 2 |
| B-FIRST | 0 of 2 | 0 of 2 |
| B-RAND expected / P(≥1) / P(2) | 0.143 / 0.138 / 0.005 | 0.182 / 0.174 / 0.008 |
| NC-1 recovered ≥ real | 100 of 999 (10.0%) | 114 of 999 (11.4%) |
| NC-1 mean recovered | 0.102 | 0.115 |
| NC-2 recovered ≥ real | 191 of 999 (19.1%) | 191 of 999 (19.1%) |
| NC-2 mean recovered | 0.199 | 0.199 |
| NC-1 / NC-2 null max LCCS | 3 / 3, real 4 never reached | 3 / 3, real 4 never reached |
| NC-3 (ICS 217) best LCCS | 2, both names | 2, both names |

**What part (b) shows, with its bound.** Part (a)'s
dissociation is stable under the enlarged pool: the
frozen score (LCCS 4 at the paired segments) remains
unreachable under both structure-preserving nulls and
absent against unrelated real text, and the recovery
count remains within the nulls' ordinary range. The
bound is structural and is stated, not buried: the
two names' ground truth lives in ICS 196 by
construction of the test, so the added segments could
only ever dilute or disturb the pairing, never supply
a rival answer — part (b) is a pool-size robustness
check on part (a)'s calibration, not an independent
pairing test, and the Androkles material's own
evidentiary questions (what *e-ro-ko-ro* is, whether
the name's case form can be tested) belong to future
registered studies, not to this one. No new flag is
raised by part (b); F-OD10-1 stands as the record's
one flag for adjudication.

**AI disclosure:** executed by an AI agent (Muse, via Muse)
at the direction of Tristen Pierson, per constitution sec. VI.
