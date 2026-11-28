# Spec 110 — Revision registration cascade

Filed 2026-11-27 with the revised battery's registration
(`records/revision-registration-2026-11-27.md`), executed in the
standing order over the landing base (main `4d57d8c9`, merge of
PR #810; the base is re-checked at landing and this record is
completed by addendum if it moves). Worker worktree
`~/.syncyard/worktrees/glossa/spec110-rev-wt-20261127`, branch
`spec-110-revised-battery`. All cascade tooling ran under the fleet
venv python (`venvs/glossa-ci`), which carries the intake
validator's dependencies; the system python lacks them and the
import refused cleanly before any append (ledger untouched at
1,139 lines on that attempt, verified).

## AEE assessment

- The AEE assessment over the five-claim revision bundle
  (`claims-revision.json`) returned **iterate** (the standard
  registration outcome): 5 claims assessed, 19 failure modes found,
  all 5 draft-capped below the 0.70 confidence threshold. Filed at
  `records/aee-assessment-revision-2026-11-27.json`; the tool's own
  outputs land under `.specify/extensions/` in the same commit.

## Intake

- `tools/ledger/import_bundle.py --spec
  specs/110-obfuscation-hypothesis --date 2026-11-27`: **5 appended**
  (C110-7, C110-8, C110-9, C110-10, C110-11), **6 already canonical**
  (C110-1..C110-6, reported not duplicated), 11 propositions in the
  spec's bundles.
- Ledger: 1,139 → **1,144 lines**; canonical SHA-256
  `a914984740310a301cb3e1c1a8780a58d5edc212bf9998772a4114f37f1d62fa`
  → **`0933a9d5175a505029ae45de6c182ab377f39eec8e2d5020419e84fdcbbfce63`**.
- `tools/ledger/validate_ledger.py`: **PASS**, errors none (1,144
  lines; 1,099 claim entries; falsifier coverage 1,090 of 1,099).

## Settling chain

- `verify-canonicals` over the grown build, before the pin was
  refreshed: **6/6 registered canonicals reproduce** (the five
  scenarios and the one comparison), field-for-field.
- T405 pair re-executed over the grown build with the scope taken
  verbatim from the incumbent record's key: incumbent
  `settling-20261128T014954Z-39a330`, full-register
  `settling-20261128T014955Z-d01d59`. Both result blocks are
  **byte-equal** to the superseded generation's
  (`settling-20261128T003231Z-486124`,
  `settling-20261128T003231Z-5502ae`) except the pins blocks, which
  carry the new ledger pin.
- The dual-run comparison was re-filed at
  `specs/086-winning-combination-adoption/records/stage-4-dual-run-comparison.json`;
  its diff against the previous filing is exactly the ledger pin
  (sha256 + lines).
- `materialize-sets` re-executed
  (`settling-20261128T014955Z-81da8e`): the assignment sets are
  unchanged (incumbent 94 assignments, full-register 286, H003 out
  of frame); the only difference in its record is the producing-run
  reference and the artifact hash covering it.
- Pin refreshed as **`re_derivations[32]`** in
  `glossa-indus/ledger/settling-canonical.json` (prior pin
  `a9149847…` / 1,139 lines; new pin `0933a9d5…` / 1,144 lines;
  expectations_changed false), and the file's live
  `provenance.ledger` pin refreshed to the same values. The refresh
  was verified surgical: 17 insertions, 0 deletions in the canonical
  file (an initial whole-file rewrite that reflowed non-ASCII lines
  was reverted and redone format-preserving).

## Generated layers and census pins

- `generate_matrix.py` and `generate_map.py` re-run;
  `tools/map/generate_program_map.py` re-run. Matrix columns
  645 → **648**; map columns by class: studies 10, **documents
  317 → 320**, research_checks 31, anchors 287.
- Census pins updated from the regenerated actuals:
  `backend/tests/test_spec095_stage4_instantiation.py` (matrix
  columns 645 → 648) and
  `backend/tests/test_spec095_t403_dashboard.py` (documents
  317 → 320). Study-count pins are unchanged (111 studies; the
  revision adds claims to an existing study).
- Ledger gate (`check_ledger_gate.py`) at this point: **31 PASS /
  1 FAIL / 1 NOT-RUN**. The FAIL is V11 run-binding, naming exactly
  the three departed records of the superseded T405 generation;
  their departure acts land in the completion commit (they name the
  registration commit), as in the first battery's cascade. The
  NOT-RUN is V7, which runs under `--regen` in the push CI job.

## Departures

The superseded generation's three run records depart the store in
the registration commit (`git rm`); the completion commit appends
their departure acts and the legacy-index entry act for
`re_derivations[32]`, and this record is completed there.
