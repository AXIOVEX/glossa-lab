# Spec 111 — Registration cascade record (2026-11-27)

The standing claims-intake cascade for the eight Spec 111 bundle claims
(C111-1..C111-8), executed on branch `spec-111-registration` from base
main `b4408dff`. Registration commit `73caa906`; this record lands in
the completion commit.

## Intake

- Taxonomy: the 111 entry appended to
  `glossa-indus/map/program-map-taxonomy.json` (domain "Program
  infrastructure", subdomain "Governance, lifecycle & generated
  layers"); the studies array now carries 111 entries.
- `tools/ledger/import_bundle.py --spec specs/111-deep-antiquity-evaluation --date 2026-11-27`:
  8 appended, 0 already canonical, 8 propositions. (A first attempt
  under the system python failed on a missing `jsonschema` module
  BEFORE any append — the ledger was verified still at 1,133 lines —
  and the intake was re-run cleanly under the worktree venv.)
- `tools/ledger/validate_ledger.py`: PASS, errors none; 1,096 claims
  (was 1,088); does_not_establish coverage 755/1096. Ledger: 1,133 →
  1,141 lines; canonical SHA-256 `542c7fa2…` →
  `29b53ed146da5aea20b31729a0cf27b8706d37979e4b302aca6b968b1e9f6440`.

## Settling layer

- `run_settling.py verify-canonicals` over the grown build: 6/6 PASS.
- T405 pair re-executed with the canonical invocations (scope extracted
  programmatically, verbatim from each incumbent record's
  `run.key.command`; 286 Mahadevan signs): incumbent
  `settling-20261128T003423Z-8e82a3`, full-register
  `settling-20261128T003424Z-59ceaa`, both over the grown build. Both
  result blocks verified byte-equal to the superseded generation's
  (`settling-20261127T194911Z-13948f` / `-c44e3e`); candidate and s_r2
  equal; the only pin difference against the superseded generation is
  the ledger pin itself. The pair's mutual comparison was re-filed at
  `specs/086-winning-combination-adoption/records/stage-4-dual-run-comparison.json`.
- Materialization re-run `settling-20261128T003444Z-5b926e`: assignment
  sets unchanged (incumbent 94 assignments, full-register 286, H003
  out of frame).
- Pin refreshed: `re_derivations[31]` appended to
  `glossa-indus/ledger/settling-canonical.json` in the established
  form, `provenance.ledger` moved in the same motion,
  expectations_changed false.

## Generated layers

- Matrix regenerated: 1,619 cells. Program map regenerated: 1,740
  elements, 1,619 edges, falsifier census 1,087 of 1,096 claims (the
  same 9 pre-existing gaps), settling runs carried 2 (the new pair).
  Program-map artifacts (program-map.json / -finds.json / .html)
  regenerated: 1,096 claims, 111 studies.
- Departures (completion commit): the superseded generation's three
  run records (`settling-20261127T194911Z-13948f`,
  `settling-20261127T194911Z-c44e3e`,
  `settling-20261127T194943Z-6d174a`) depart the store under run-defs
  v3 §7.1; their departure acts in `run-index.jsonl` name the records,
  their blob hashes, and the registration commit `73caa906` as
  `superseded_by_commit`. The legacy-index completion pass
  (`build_legacy_index.py`) appended the legacy entry act for
  re_derivations[31]; folded census 132 entries.
- Census pins updated from the regenerated actuals in
  `backend/tests/test_program_map_conformance.py`,
  `test_spec086_map.py`, `test_spec086_ledger_gate.py`,
  `test_spec095_stage4_instantiation.py`,
  `test_spec095_t403_dashboard.py` (including the T405 run of record,
  now `settling-20261128T003423Z-8e82a3`).

## Verification over the final tree

- Ledger gate (`tools/ledger/check_ledger_gate.py`): 32 PASS / 0 FAIL /
  1 NOT-RUN, RESULT PASS.
- The five pin-carrying backend test files: 114 passed (after two
  disclosed pin-correction rounds: 19 failures → 6 → 0, each failure a
  census pin read from the regenerated actuals).
- Both gated publications re-ran over the final tree before
  completing: matrix RESULT PASS, map published; both byte-identical
  to the committed artifacts.

## Serialization disclosure

Main advanced during this landing: PR #807 (Spec 109 Stage 4) merged
as `ecaa022b` while this branch was in flight. That landing touched
only Spec 109 files; the claims ledger did not move on main, so the
cascade above stands without re-execution, and main is merged into
this branch before the pull request opens.

## Serialization addendum — second execution (2026-11-27)

The first execution above was completed and its pull request reached
CI 10/10, but before it merged, main advanced twice more: PR #807
(Spec 109 Stage 4, no ledger movement) and PRs #808/#810 (Spec 109
G1-E and the Spec 110 cascade), the latter moving the ledger to 1,139
lines / canonical `a9149847…` / 1,094 claims with pin
re_derivations[31]. The merge was therefore blocked on conflicts in
every cascade artifact, and per the standing rule the cascade was
re-executed in full over the merged build rather than reconciled by
hand. The first execution's commits were discarded; its figures above
stand as the record of that execution.

Second execution, over base main `4d57d8c9` (merge of PR #810):

- Intake: 8 appended, 0 already canonical; ledger 1,139 → 1,147
  lines; canonical SHA-256 `a9149847…` →
  `70097435f564959f5e3e20e9b8dd5a1d96aea096ba1d7d61c0d1eb42b3f564b9`;
  validate PASS, 1,102 claims; verify-canonicals 6/6.
- T405 pair re-executed: incumbent `settling-20261128T011943Z-1449ae`,
  full-register `settling-20261128T011943Z-5ff36b`; both result blocks
  byte-equal to the superseded generation's
  (`settling-20261128T003231Z-486124` / `-5502ae`); comparison
  re-filed; materialization `settling-20261128T012044Z-8c4e4c`, sets
  unchanged (94 / 286, H003 out of frame).
- Pin refreshed at re_derivations[32]; provenance.ledger moved in the
  same motion; expectations_changed false.
- Generated layers: matrix 1,625 cells; map 1,747 elements, 1,625
  edges; falsifier census 1,093 of 1,102; program map 1,102 claims,
  112 studies. Departures: the Spec 110 generation's three run records
  depart under §7.1, their acts naming registration commit `d054b8c5`;
  legacy folded census 136 entries.
- Ledger gate over the final tree: 32 PASS / 0 FAIL / 1 NOT-RUN,
  RESULT PASS. Census pins updated from the regenerated actuals in
  the same five backend test files (T405 run of record now
  `settling-20261128T011943Z-1449ae`) and in the two frontend e2e
  census texts (1,102 claims). Both gated publications re-ran over
  the final tree before completing.
