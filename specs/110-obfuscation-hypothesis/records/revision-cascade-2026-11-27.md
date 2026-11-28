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

## Addendum — cascade re-executed over the merged build

Main moved after the cascade above was first executed: PR #809
(Spec 111 registration) merged as `3ab43e40` while this branch was
in flight (ledger 1,147 lines, canonical `70097435…`, pin
`re_derivations[32]`). Under the program's standing pattern for
concurrent landings, this branch merged main (merge commit
`b8af893d`) and **the cascade was re-executed in full over the
merged build**; the figures below supersede the first execution's
for the landing, and the first execution's figures above stand as
its record over the `4d57d8c9` base.

Process disclosure, in full: the first merge attempt produced
rename/rename conflicts in the settling run store (both branches
had renamed the same superseded generation to their own), and a
first resolution of it was committed (`88162b4f`) carrying conflict
markers in the three run records of Spec 111's generation, because
the unmerged-path check that cleared it did not enumerate
rename/rename states. That merge was **reset before any push** and
redone path-by-path; a T405 pair run in between executed against
the markered store with an empty scope and its records were
discarded with the reset. None of that state lands: the landed
merge is `b8af893d`, verified free of conflict markers, with the
run store holding Spec 111's generation intact at the merge point.

Re-executed figures over the merged build:

- Import: **5 appended** (C110-7..C110-11), 6 already canonical;
  ledger 1,147 → **1,152 lines**; canonical SHA-256
  **`18369a65f0f4b5f3f199abed194f47e8b65b0af9eb733fc7854fbe50a1a32026`**.
- `validate_ledger.py`: **PASS**, errors none (1,152 lines; 1,107
  claim entries).
- `verify-canonicals` over the merged grown build: **6/6**.
- T405 pair re-executed with the scope verbatim from Spec 111's
  incumbent record: incumbent `settling-20261128T020148Z-9f5fe0`,
  full-register `settling-20261128T020148Z-75cdce`; both result
  blocks **byte-equal** to Spec 111's generation
  (`settling-20261128T011943Z-1449ae`,
  `settling-20261128T011943Z-5ff36b`) except the pins blocks.
  Comparison re-filed; its diff is exactly the ledger pin.
  Materialization re-run (`settling-20261128T020148Z-1d5c35`):
  sets unchanged (94 / 286 / H003 out of frame).
- Pin refreshed as **`re_derivations[33]`** (prior `70097435…` /
  1,147; new `18369a65…` / 1,152), appended **surgically**:
  Spec 111's entry carries literal `\u2026` escapes that a
  whole-file rewrite would have reflowed, so the append was a text
  insertion verified to leave entry [32] byte-untouched (19
  insertions, 2 deletions — the deletions are the provenance pin's
  two lines). The first execution's pin (its `re_derivations[32]`
  in commit `a4d66bf3`) remains in this branch's history as the
  record of the first execution.
- Generated layers regenerated over the merged build; census pins
  updated from the merged actuals: studies **112** (Spec 111's
  count, unchanged by this revision), claims **1,107**, ledger
  lines **1,152**, falsifier-present **1,098**, bundle population
  **1,084**, matrix rows **1,107**, matrix columns **648**,
  documents by class **320**; the dashboard T405 re-run pin now
  names the new incumbent run (`settling-20261128T020148Z-9f5fe0`).
  Pin sites: `test_spec086_ledger_gate.py`, `test_spec086_map.py`,
  `test_program_map_conformance.py`,
  `test_spec095_stage4_instantiation.py`,
  `test_spec095_t403_dashboard.py` — all passing after the update.
- Departure accounting: Spec 111's T405 generation
  (`settling-20261128T011943Z-1449ae`,
  `settling-20261128T011943Z-5ff36b`,
  `settling-20261128T012044Z-8c4e4c`) departs the store in the
  re-execution commit; its departure acts and the legacy-index
  entry act for `re_derivations[33]` land in the completion
  commit. The `003231Z` generation's departures were already
  accounted on main by Spec 111's completion acts and are not
  duplicated. This revision's first-execution generation
  (`settling-20261128T014954Z-39a330`,
  `settling-20261128T014955Z-d01d59`,
  `settling-20261128T014955Z-81da8e`) never stands on the merged
  tree — removed in the merge resolution; its records remain in
  commit `a4d66bf3`'s tree in this branch's history, and its
  run-index entry acts were superseded with the merge resolution
  (the index on the merged tree carries main's acts plus the
  re-execution's).
