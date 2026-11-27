# Spec 107 — Cycle-2 registration cascade record (2026-11-27)

Filed under T201. This record states what the cycle-2 registration cascade
executed, over which build, and what it found. The registration it serves:
`records/cycle-2-registration-2026-11-27.md`. All cascade work ran on
tower-compute in the worktree `spec107-c2-reg3` (branch
`spec-107-cycle-2-registration-b`, base main `132cffbf`, the PR #792 merge);
drafting and source reading only ran in the coordinator's VM. Every step
below emitted timestamped progress output while it ran.

## The package as landed

- `spec.md` §8 (cycle 2), `test-cases.md` (TC-107-07..12), `claims.md`
  (C107-7..C107-11), and the second bundle file `claims.json` — adopted
  from the later of the two unlanded registration drafts the first
  coordinator left on tower-compute on 2026-11-27 (verified byte-identical
  package files across both drafts; the adopted draft's registration text
  carried the duplication-conformance paragraph the earlier draft lacked),
  amended for the owner's OD-O-1 ruling of 2026-11-27 08:27 ET as recorded
  in the registration's §3 and in the Round O adjudication record's §7.
- The cycle-1 bundle (`aee-claims.json`) is not amended; the five new
  claims ride the second bundle file, per the cycle-1 precedent.

## AEE assessment

`run_aee.py` over the cycle-2 bundle: outcome **iterate**; 5 claims
assessed, all draft-capped below 0.70. Assessment filed at
`records/aee-assessment-cycle-2-2026-11-27.json`. No claim's standing
moves at registration; the assessment is the bundle's intake record.

## TC-107-01 (bundle conformance) — PASS

Bundle ids and order equal across `claims.json`, `aee-claims.json` (the
cycle-1 claims) and `claims.md`: C107-1..C107-11. Every claim carries a
falsifier (the bundle's `falsification_tests` and the claims.md prose) and
a does-not-establish line (in the bundle `text`).

## Claims intake

`tools/ledger/import_bundle.py --spec specs/107-active-decipherment-loop
--date 2026-11-27`: **5 appended (C107-7..C107-11), 6 already canonical,
11 propositions.** The ledger grew **1,110 → 1,115 lines**; canonical
sha256 of the grown ledger `ec8f262bb9e2d5653a664adc824b8d25dcac03d854a42fe17007adfad0e0bb2a`.
`validate_ledger.py`: **PASS**, no errors — 1,115 lines; 1,078 claims
(bundle 1,055, extracted 23), 31 annotations, 6 reclassifications;
falsifier coverage 1,069/1,078 (the same 9 pre-existing gaps; the five new
claims all carry falsifiers).

## Settling canonicals over the grown build

- `run_settling.py verify-canonicals`: **6/6 PASS** (the five scenarios
  and the one comparison reproduce field-for-field).
- T405 pair re-executed over the grown build (scope extracted verbatim
  from the incumbent record: 286 mahadevan signs; scenarios
  incumbent-over-subset and full-register-over-subset): runs
  `settling-20261127T133744Z-907cb1` (incumbent) and
  `settling-20261127T133744Z-92af7b` (full-register). **Both result blocks
  are byte-equal to the superseded generation's**; candidate and s_r2
  equal; the pair's input pins are identical to the superseded
  generation's except the ledger pin itself.
- The Stage 4 dual-run comparison was re-filed
  (`specs/086-winning-combination-adoption/records/stage-4-dual-run-comparison.json`);
  its diff against the previous filing is the ledger pin only.
- `materialize-sets` re-run (`settling-20261127T133827Z-ea29e2`):
  assignment sets unchanged — incumbent 94, full-register 286, H003 out
  of frame.
- Pin refreshed in `glossa-indus/ledger/settling-canonical.json`:
  re-derivation appended at index [27] under this registration's
  amendment discipline, and the `provenance.ledger` pin moved in the
  same motion (bc601e86…/1,110 → ec8f262b…/1,115). Expectations
  unchanged; semantics glossa-settle-1 unchanged.

## Departures

The superseded generation's run records departed the store in this
landing (run-defs v3 §7.1), because the map carries every scenario
evaluation record in the store and the old generation is pinned to the
superseded ledger build:

- `settling-20261127T102311Z-ad74e8.json` — sha256
  `bfe16e683021a11c80c1cea509f470f6f6eb9e0d9309b26936f924fce7b8352b`,
  git blob `e628933228479527eb7573c638d6419097529013`
- `settling-20261127T102312Z-07ef78.json` — sha256
  `9500d54cee6d36e04d878b4ee2d4a723822af779e4f2368380d4be4e25515380`,
  git blob `c570ee6be39bfcf788a8d0faf48ab78d73b6c4be`
- `settling-20261127T102325Z-ebb5ff.json` — sha256
  `75cdca140f29a7dfca6e36ad9c6695c6fc2f97625fb340cb868ab1ec944cd1a0`,
  git blob `5742aed7c8a830df0065b24521a65623743584e8`

Departure acts naming these records, their blob hashes, and this
landing's registration commit as the superseding commit are appended to
`glossa-indus/ledger/runs/run-index.jsonl` in the completion commit that
immediately follows this landing's registration commit, together with
the legacy-index entries the completion pass appends; the finalization
section of this record, added in that commit, names the hashes.

## Matrix and maps regenerated

- `generate_matrix.py`: 1,601 cells; falsifier block 1,069/1,078.
- `generate_map.py` (after the departures): falsifier census 1,069 of
  1,078 claims, 9 gaps named; settling runs carried: 2; map elements
  1,722; edges supports 1,594, opposes 7.
- `tools/map/generate_program_map.py`: claims 1,078 · studies 109 ·
  unjudged studies 28 · judgment calls 0.

## Census pins updated from the regenerated actuals

- `backend/tests/test_program_map_conformance.py`: claims 1,073 → 1,078;
  bundle population 1,050 → 1,055; open class 1,063 → 1,068;
  falsifier-present 1,064 → 1,069.
- `backend/tests/test_spec086_map.py`: claims total 1,073 → 1,078; draft
  1,049 → 1,054; ledger lines 1,110 → 1,115; map elements 1,717 → 1,722;
  supports edges 1,589 → 1,594; falsifier census 1,064/1,073 →
  1,069/1,078; claims untouched by any run 1,072 → 1,077.
- `backend/tests/test_spec095_stage4_instantiation.py`: ledger lines
  1,110 → 1,115; claims 1,073 → 1,078; falsifier coverage 1,064/1,073 →
  1,069/1,078.
- `backend/tests/test_spec095_t403_dashboard.py`: claims 1,073 → 1,078;
  ledger lines 1,110 → 1,115; falsifier-present 1,064 → 1,069; the T405
  run of record re-pinned to `settling-20261127T133744Z-907cb1`.
- `frontend/e2e/researcher-dashboard.spec.ts` and
  `frontend/e2e/system-graph.spec.ts`: census text 1,073 → 1,078.

## Registration landing contents

The registration commit carries: the Spec 107 cycle-2 package (spec.md
§8, test-cases.md, claims.md, claims.json, tasks.md, the registration and
this cascade record, the AEE assessment and its ledger files, the
history-ledger entries), the Round O adjudication record's §7 (the
OD-O-1 ruling), the grown ledger and its validation state, the refreshed
settling canonicals and comparison, the new T405 run records and
materialization, the departed records' removal, the regenerated matrix
and maps, and the census-pin updates above.

## Finalization (completion commit)

The registration commit of this landing is
`85a9b2b4344ac24f3fd48f953bd6a371e9b058dc` (branch
`spec-107-cycle-2-registration-b`). The three departure acts were
appended to `glossa-indus/ledger/runs/run-index.jsonl` in the completion
commit that carries this section, each naming its record, its blob
sha256 and git blob id (as listed under Departures above), its run id,
and the registration commit as `superseded_by_commit`; the
`tools/ledger/build_legacy_index.py` completion pass then appended the
legacy entry act for re-derivation [27] (folded census 113 entries).
With the departure accounting in place, the run store carries exactly
the new generation: runs 907cb1, 92af7b and the ea29e2 materialization.
- Addendum (same landing): the gate-evidence text pins in
  `backend/tests/test_spec086_ledger_gate.py` (matrix cells 1,596 →
  1,601; supports 1,589 → 1,594) and the remaining pins in
  `backend/tests/test_spec086_map.py` (no-stage-recorded 29 → 34;
  supports 1,589 → 1,594; one further claims-total 1,073 → 1,078) were
  updated from the same regenerated actuals.
