# Spec 107 — M-2 re-registration cascade record (2026-11-27)

Filed under T207. This record states what the M-2
re-registration cascade executed, over which build, and
what it found. The registration it serves:
`records/m2-re-registration-2026-11-27.md`. All cascade
work ran on tower-compute in the worktree
`m2-rereg-wt-20261127` (branch
`spec-107-m2-re-registration`, base main `394d15f8`,
the PR #798 merge). The package's cascade figures were
composed over main at `0d7c4f09` (PR #793's merge);
before the intake, the landing measured the claims
ledger fresh on the current main and found it
unchanged from that build (1,123 lines, canonical
SHA-256
`6c358631b742a52bde6e7371f667dabcc9d079271a172c93a2c4afe48121fe9e`;
PR #798 was a records-only landing that did not touch
the ledger), so the package's figures held as written
and no recomputation was needed. Every step below
emitted timestamped progress output while it ran.

## The package as landed

- `spec.md` §8 (M-2 re-registration), `test-cases.md`
  (TC-107-13), `claims.md` (C107-12), the third bundle
  file `claims-m2-reregistration.json`, `tasks.md`
  (T207–T208), the re-registration record, and the
  Spec 097 custody restoration record
  (`specs/097-meroitic-reproduction-benchmark/records/custody-restoration-2026-11-27.md`).
- The cycle-1 bundle (`aee-claims.json`) and the
  cycle-2 bundle (`claims.json`) are not amended;
  C107-12 rides the third bundle file, as the
  re-registration's §6 files it.
- One machinery amendment, made in this landing and
  recorded here: the intake's bundle discovery
  (`backend/glossa_lab/ledger_intake.py`,
  `build_bundle_entries`) read only the two registered
  bundle filenames (`claims.json`, `aee-claims.json`),
  so the standard intake command as it stood could not
  see a third bundle file. The discovery now also
  reads any further `claims-<name>.json` bundle file
  in a spec directory, of the same schema, through the
  same proposition grouping, fingerprinting, and
  validation path. No existing spec's intake changes:
  no other spec directory carries such a file.

## AEE assessment

`run_aee.py` over the new bundle: outcome **iterate**;
1 claim assessed, draft-capped below 0.70. Assessment
filed at
`records/aee-assessment-m2-reregistration-2026-11-27.json`,
with its assessment, evaluator-result, and ledger
files under `.specify/` as in the prior registration
landings. No claim's standing moves at registration;
the assessment is the bundle's intake record.

## TC-107-01 (bundle conformance) — PASS

Bundle ids and order equal across `aee-claims.json`,
`claims.json`, `claims-m2-reregistration.json`, and
`claims.md`: C107-1..C107-12. Every claim carries a
falsifier (the bundles' `falsification_tests` and the
claims.md prose) and a does-not-establish line (in the
bundle `text` and the claims.md prose).

## Claims intake

`tools/ledger/import_bundle.py --spec
specs/107-active-decipherment-loop --date 2026-11-27`:
**1 appended (C107-12), 11 already canonical, 12
propositions.** The ledger grew **1,123 → 1,124
lines**; canonical sha256 of the grown ledger
`dad4de2db2ecf2449288e975fa1c5ba730b72b04e49a1bcdd719a14c3c03b197`.
`validate_ledger.py`: **PASS**, no errors — 1,124
lines; 1,079 claims (bundle 1,056, extracted 23), 31
annotations, 14 reclassifications; falsifier coverage
1,070/1,079 (the same 9 pre-existing gaps, all in the
extracted population; C107-12 carries a falsifier).

## Settling canonicals over the grown build

- `run_settling.py verify-canonicals`: **6/6 PASS**
  (the five scenarios and the one comparison reproduce
  field-for-field).
- T405 pair re-executed over the grown build (scope
  extracted verbatim from the incumbent record: 286
  mahadevan signs; scenarios incumbent-over-subset and
  full-register-over-subset): runs
  `settling-20261127T182329Z-0cae4b` (incumbent) and
  `settling-20261127T182408Z-f2168b` (full-register).
  **Both result blocks are byte-equal to the
  superseded generation's**; candidate and s_r2 equal;
  the pair's input pins are identical to the
  superseded generation's except the ledger pin
  itself.
- The Stage 4 dual-run comparison was re-filed
  (`specs/086-winning-combination-adoption/records/stage-4-dual-run-comparison.json`);
  its diff against the previous filing is the ledger
  pin only.
- `materialize-sets` re-run
  (`settling-20261127T182440Z-f87253`): assignment
  sets unchanged — incumbent 94, full-register 286,
  H003 out of frame.
- Pin refreshed in
  `glossa-indus/ledger/settling-canonical.json`:
  re-derivation appended at index [29] under this
  registration's amendment discipline, and the
  `provenance.ledger` pin moved in the same motion
  (6c358631…/1,123 → dad4de2d…/1,124). Expectations
  unchanged; semantics glossa-settle-1 unchanged.

## Departures

The superseded generation's run records departed the
store in this landing (run-defs v3 §7.1), because the
map carries every scenario evaluation record in the
store and the old generation is pinned to the
superseded ledger build:

- `settling-20261127T155917Z-939f46.json` — sha256
  `91f2c9ac984dfb7b9eaad3d6c4719ab3bbbd102bc810f4e5139b5a41d70e0eb2`,
  git blob `f809e5a45c7087b674d2ce6ce510a2c03d8fd548`
- `settling-20261127T155918Z-ae2e92.json` — sha256
  `e47caaa7027a3d5effae110da3ed5d5267017be2563ec33600dfeddc0c20c6ff`,
  git blob `3f944be061ca68587ad7a570c1b64cc2fbdcc865`
- `settling-20261127T160138Z-65ba1d.json` — sha256
  `2451e368eb9c50a26635f15f6f8caa74fff35861b8c7e5412e7e1d6fbff177a9`,
  git blob `cc7b1d5a0e4d74a5ac7c63f5d85b7270cf43c69c`

Departure acts naming these records, their blob
hashes, and this landing's registration commit as the
superseding commit are appended to
`glossa-indus/ledger/runs/run-index.jsonl` in the
completion commit that immediately follows this
landing's registration commit, together with the
legacy-index entries the completion pass appends; the
finalization section of this record, added in that
commit, names the hashes.

## Matrix and maps regenerated

- `generate_matrix.py`: 1,602 cells; falsifier block
  1,070/1,079.
- `generate_map.py` (after the departures): falsifier
  census 1,070 of 1,079 claims, 9 gaps named; settling
  runs carried: 2; map elements 1,723; edges supports
  1,595, opposes 7.
- `tools/map/generate_program_map.py`: claims 1,079 ·
  studies 109 · unjudged studies 28 · judgment calls 0.

## Census pins updated from the regenerated actuals

- `backend/tests/test_program_map_conformance.py`:
  claims 1,078 → 1,079; bundle population 1,055 →
  1,056; open class 1,060 → 1,061; falsifier-present
  1,069 → 1,070; census-of-record note re-dated to
  this landing.
- `backend/tests/test_spec086_map.py`: claims total
  1,078 → 1,079; draft 1,054 → 1,055; ledger lines
  1,123 → 1,124; map elements 1,722 → 1,723; supports
  edges 1,594 → 1,595; falsifier census 1,069/1,078 →
  1,070/1,079; no-stage-recorded 34 → 35; claims
  untouched by any run 1,077 → 1,078.
- `backend/tests/test_spec086_ledger_gate.py`: matrix
  cells 1,601 → 1,602; claims counted 1,078 → 1,079;
  map edges 1,601 → 1,602; supports 1,594 → 1,595;
  claim nodes 1,078 → 1,079.
- `backend/tests/test_spec095_stage4_instantiation.py`:
  ledger lines 1,123 → 1,124; claims 1,078 → 1,079;
  falsifier coverage 1,069/1,078 → 1,070/1,079; matrix
  rows 1,078 → 1,079.
- `backend/tests/test_spec095_t403_dashboard.py`:
  claims 1,078 → 1,079; ledger lines 1,123 → 1,124;
  falsifier-present 1,069 → 1,070; matrix rows 1,078
  → 1,079; the T405 run of record re-pinned to
  `settling-20261127T182329Z-0cae4b`.
- `frontend/e2e/researcher-dashboard.spec.ts` and
  `frontend/e2e/system-graph.spec.ts`: census text
  1,078 → 1,079.

## Registration landing contents

The registration commit carries: the Spec 107 M-2
re-registration package (spec.md §8, test-cases.md,
claims.md, claims-m2-reregistration.json, tasks.md,
the re-registration and this cascade record, the AEE
assessment and its `.specify` files, the
history-ledger entry), the Spec 097 custody
restoration record, the bundle-discovery amendment in
`backend/glossa_lab/ledger_intake.py`, the grown
ledger and its validation state, the refreshed
settling canonicals and comparison, the new T405 run
records and materialization, the departed records'
removal, the regenerated matrix and maps, and the
census-pin updates above.

## Finalization (completion commit)

The registration commit of this landing is
`a9f3f22144f93931e1c4b7951aa9c3b380656a75` (branch
`spec-107-m2-re-registration`). The three departure
acts were appended to
`glossa-indus/ledger/runs/run-index.jsonl` in the
completion commit that carries this section, each
naming its record, its blob sha256 and git blob id
(as listed under Departures above), its run id, and
the registration commit as `superseded_by_commit`;
the `tools/ledger/build_legacy_index.py` completion
pass then appended the legacy entry act for
re-derivation [29] (folded census 124 entries). With
the departure accounting in place, the run store
carries exactly the new generation: runs
`settling-20261127T182329Z-0cae4b`,
`settling-20261127T182408Z-f2168b` and the
`settling-20261127T182440Z-f87253` materialization.
- Addendum (same landing, after the first CI run):
  the full backend suites single failure was
- Addendum (same landing, after the first CI run):
  the full backend suite's single failure was
  `test_spec086_ledger_migration.py::test_p2_reconciliation`
  (1 failed, 3,101 passed) — the migration test's own
  bundle-record helper (`_p2_records`) carried the
  same two-filename discovery the machinery amendment
  retired, so its expected fingerprint set lacked
  C107-12's. The helper's glob now includes
  `specs/*/claims-*.json`, the same discovery as the
  intake's; the test file passes 6/6 locally, and the
  fix rides this landing's third commit.
