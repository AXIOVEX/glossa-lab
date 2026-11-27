# Spec 101 — outcome record (filed late, 2026-11-27)

**Filing note.** This is the narrative outcome record that T401 and
the Spec 101 history ledger name. It was not filed with the scoring
commit `be6c5f41`; the scoring commit carried the scorer and
`scoring-outcome.json` only. This record was compiled later on
2026-11-27, after that commit, and is filed in the Co-scientist
Round O landing (PR reference in the Round O adjudication record,
`specs/091-anchor-comparison-integrity/records/coscientist-sweep-adjudication-2026-11-27-round-o.md`,
unit O-E-1). It is dated by its filing, not backdated to the
scoring run. The preserved numerical artifact of the execution is
`scoring-outcome.json` (SHA-256
`6e22675e8e807bfb6cd2e2bc034dbd59f2879afa6224a0e842b17aea3f555d78`);
nothing in this record changes any filed figure.

## Exposure statement (C101-2)

Exposure: that Perna 2019's chapter including its printed reading
of ICS 194/195 was read in full on 2026-11-22 (OD-9) before any
candidate was registered. The study is postdictive: ICS 194 and
ICS 195 are already-exposed text, and no blind or held-out
prediction is claimed anywhere in this study's records.

## Outcome

Candidate counts against the floors instantiated at the freeze
(floor record §1.5 basis; Q = 0.031153):

| Candidate | Count | Floor | At or above floor |
|---|---|---|---|
| -se | 0 | 33 | no |
| -na | 9 | 25 | no |
| -i | 1 | 25 | no |
| -ti | 14 | 25 | no |

Per-inscription counts: ICS 194 (104 signs, 33 segments):
-se 0, -na 8, -i 0, -ti 3. ICS 195 (227 signs, 51 segments):
-se 0, -na 1, -i 1, -ti 11. Census of record: 331 signs,
84 segments. The ICS 194 sign count carries the intake correction
filed in the intake identity record (a doubled *a* in L3
segment 1, settled by zoomed crops); the identity record names,
without reconciling, the difference against the chapter's stated
216 signs.

**Verdict: C101-1 NOT SUPPORTED.** The target of the registered
rule is enrichment, per OD-D-1: NOT SUPPORTED is expressly not a
recurrence finding. Three candidates visibly recur; every count
falls below its registered floor.

## Test crosswalk (TC-101-01..06)

- TC-101-01 (candidate derivation from the development corpus
  only): satisfied; derivation and freeze scripts replay to their
  filed JSON byte-for-byte (Round O check).
- TC-101-02 (intake identity and pins): satisfied; corpus and
  per-inscription pins match the intake identity record.
- TC-101-03 (double scoring, byte-identical): satisfied on the
  filed record; the filed scorer replays byte-identical to the
  filed scoring JSON.
- TC-101-04 (exposure statement present verbatim in the outcome
  record; no blind-prediction description): satisfied by this
  record, late. The scoring artifact itself carries no exposure
  statement; that gap is the subject of Round O unit O-E-1.
- TC-101-05 (floor arithmetic): satisfied; floors 33/25/25/25
  recompute exactly at the registered threshold.
- TC-101-06 (TOO THIN closure exercised): QUALIFIED. See
  `records/tc101-06-qualification-2026-11-27.md` (Round O unit
  O-E-2). The study's four registered candidates all
  instantiated, so the closure path was not needed for this
  outcome; the historical claim that the path was exercised is
  qualified there, and the behavioral coverage gap stands on the
  record.

## Standing effect

None in this record. C101-1's ledger standing was moved by the
owner's adjudication of 2026-11-27 (reclassification entry
`101-eteocypriot-next-claim/C101-1/reclassification-2026-11-27`,
draft → unsupported), recorded in
`records/adjudication-2026-11-27.md`.
