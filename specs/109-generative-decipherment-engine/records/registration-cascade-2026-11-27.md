# Spec 109 registration cascade — 2026-11-27

The record of the claims-ledger intake cascade that carried the nine
Spec 109 claims (C109-1..C109-9) onto the canonical ledger, executed
2026-11-27 in the registration worktree
(`spec109-reg-20261127`, branch `spec-109-registration`). The
discipline followed is the standing one (run-defs v3 §7; the Spec 107
cycle-2 cascade record is the immediate precedent): intake, canonical
verification, the T405 pair re-executed over the grown build, the pin
refreshed as a new re-derivation, the generated layers regenerated,
the superseded generation departed, and every census pin updated from
the regenerated actuals. Every figure below was measured in the
worktree at execution time.

## Serialization disclosure

This cascade executed twice. The first execution ran over the
1,123-line build (ledger canonical `6c358631…`, pin
re_derivations[28]) and completed both its commits (registration
`ee2c141f`, completion `c733454f`) on this branch. Before its pull
request opened, main advanced under PR #799 (Spec 107 M-2
re-registration; the ledger to 1,124 lines; its own re-derivation at
re_derivations[29]; the settling generation of record replaced) and
PR #800 (the M-2 execution). The first cascade was therefore
superseded unmerged, the branch was rebuilt from the new main, and
the whole cascade was re-executed over the merged build, which is
the landing this record documents. The first execution's two
mis-invoked settling runs (a no-scenario incumbent run and a refusal
absence record, from a scope-extraction error) and the junction they
raised — adjudicated with the explanation on its face and its
quarantine lifted — exist only in the superseded commits and never
entered main's store; the re-execution extracted the scope correctly
and produced no junction.

## The baseline and the growth

- Baseline (main at `9e00c08f`, the merge of PR #800): ledger 1,124
  lines, canonical SHA-256 `dad4de2db2ecf2449288e975fa1c5ba730b72b04e49a1bcdd719a14c3c03b197`;
  settling generation of record `settling-20261127T182329Z-0cae4b`
  (incumbent), `settling-20261127T182408Z-f2168b` (full-register),
  `settling-20261127T182440Z-f87253` (materialization); pin
  re_derivations[29].
- AEE assessment: outcome **iterate**, nine claims assessed, all
  draft-capped below 0.70, filed at
  `records/aee-assessment-2026-11-27.json`.
- TC-109-01 (package form): **PASS** — bundle ids and order equal
  claims.md C109-1..C109-9; every claim carries a falsifier and a
  does-not-establish line in both files; spec.md states the five
  parts, the preflight, the judging rule, the iconography statement
  and the kill criteria.
- Taxonomy: Spec 109 placed in `program-map-taxonomy.json` under
  Program infrastructure / Governance, lifecycle & generated layers.
- Intake: **9 appended, 0 already canonical, 9 propositions.** Ledger
  1,124 → **1,133 lines**. `validate_ledger` PASS, errors none:
  **1,088 claims**.
- Canonical verification before the pin moved: `verify-canonicals`
  **6/6 PASS** over the grown build.
- The T405 pair, re-executed with the canonical invocations (scope
  verbatim from the incumbent record's key.command, 286 Mahadevan
  signs): incumbent run `settling-20261127T194911Z-13948f`,
  full-register run `settling-20261127T194911Z-c44e3e`. **Both result
  blocks are byte-equal to the superseded generation's; candidate and
  s_r2 are equal; the only pin difference against the superseded
  generation is the ledger pin itself.** The Stage 4 dual-run
  comparison was re-filed at
  `specs/086-winning-combination-adoption/records/stage-4-dual-run-comparison.json`;
  its diff against the previous filing is exactly the ledger pin
  (sha256 + lines).
- Materialization re-run: `settling-20261127T194943Z-6d174a`; the
  assignment sets are unchanged (incumbent 94 assignments,
  full-register 286, H003 out of frame).
- Canonical hash of the grown ledger:
  `542c7fa2316f9236f3fbeb2e60e3020f2d8b93652cdce28ec235f7f0b42ab77e`
  (1,133 lines).
- Pin refresh: re_derivations entry **[30]** appended to
  `glossa-indus/ledger/settling-canonical.json` in the established
  form (prior pin dad4de2d…/1,124 → new pin 542c7fa2…/1,133,
  expectations_changed false, verification naming the pair, the
  comparison and the materialization), and `provenance.ledger` moved
  in the same motion. The entry's act text carries the serialization
  on its face.

## The generated layers and the census

- Matrix: 1,611 cells (matrix.json SHA-256 `ab711f6c…`).
- Evidence map: 1,732 elements (1,088 claims); edges 1,611 (supports
  1,604, opposes 7); falsifier census 1,079 of 1,088 claims carry a
  falsifier, the same 9 pre-existing gaps (the nine Spec 109 claims
  all carry falsifiers); settling runs carried: 2 (the new pair);
  claims untouched by any run 1,087; claims with no stage recorded 35.
- Program map: 1,088 claims · 110 studies · 28 unjudged studies · 0
  judgment calls; claims by status: draft 1,064, untested 12,
  contradicted 4, partially_supported 3, strongly_supported 2,
  partially_falsified 1, superseded 1, unsupported 1.
- Ledger gate over the final tree: **32 PASS / 0 FAIL / 1 NOT-RUN —
  RESULT: PASS.**
- Census pins updated from the regenerated actuals:
  `backend/tests/test_program_map_conformance.py`,
  `backend/tests/test_spec086_map.py`,
  `backend/tests/test_spec086_ledger_gate.py`,
  `backend/tests/test_spec095_stage4_instantiation.py`,
  `backend/tests/test_spec095_t403_dashboard.py` (including the T405
  run of record, now `settling-20261127T194911Z-13948f`), and the two
  frontend e2e census texts (1,088).

## Finalization

- Registration commit: `ab783146` (the Spec 109 package, the AEE
  assessment and its ledger files, the taxonomy placement, the grown
  ledger, the refreshed canonical, the re-filed comparison, the new
  run records, the assignment sets, the matrix and the program map).
- Departures (this completion commit): the superseded generation's
  three run records (0cae4b, f2168b, f87253) depart the store under
  run-defs v3 §7.1; their departure acts in `run-index.jsonl` name
  the records, their blob hashes, and the registration commit as
  `superseded_by_commit`. The legacy-index completion pass appended
  the legacy entry act for re-derivation [30] (folded census 128
  entries). Both gated publications were re-run over the final tree
  and passed the full gate, so the published bytes are the gated
  bytes.
- No standing, verdict or tally moved anywhere in the program: the
  nine claims entered at stage `created`, status `draft`, and the
  cascade's only ledger effect is their intake.
