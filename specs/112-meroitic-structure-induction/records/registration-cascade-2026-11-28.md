# Spec 112 registration cascade — 2026-11-28

The record of the claims-ledger intake cascade that carried the seven
Spec 112 claims (C112-1..C112-7) onto the canonical ledger, executed
2026-11-28 in the registration worktree (`spec109-reg-20261127`,
branch `spec-112-registration`, base main `db88fbd4`, the merge of
PR #811). The discipline followed is the standing one (run-defs v3 §7;
the Spec 109 registration cascade record is the procedure of record,
the E6 cascade on this same clone the most recent instance): intake,
canonical verification, the T405 pair re-executed over the grown build,
the pin refreshed as a new re-derivation, the generated layers
regenerated, the superseded generation departed, and every census pin
updated from the regenerated actuals. Every figure below was measured
in the worktree at execution time.

## Serialization disclosure

Main did not advance during this landing: the branch was taken from
`db88fbd4` and origin/main still stood at `db88fbd4` when the pull
request opened, so the cascade executed exactly once, over the merged
build described below. Two execution incidents are disclosed on their
face: (1) the first T405-pair driver died on a stdout parse after the
incumbent run had already executed and landed its record
(`settling-20261128T092257Z-31e57c`); the pair step was re-run with
store-based identification, reused that record, and executed only the
full-register leg — no duplicate run exists. (2) The evidence-map
regeneration was first attempted while the superseded generation
still stood in the store and was refused on that ground (a run pinned
to the prior build cannot be carried); the superseded records were
departed first and the regeneration then ran clean, in the Spec 110
order. The census pins, the departure acts, the legacy-index act and
this record land in the completion commit; in the Spec 109/111 form
the census pins rode the registration commit — the split here is a
sequencing artefact of the pin-correction pass and changes nothing
the pins pin.

## The baseline and the growth

- Baseline (main at `db88fbd4`): ledger 1,156 lines, canonical
  SHA-256 `a09fb02f61a62a5d3952ade640c6820626da42a89cac3677049385a5297dc632`;
  settling generation of record `settling-20261128T030313Z-22d2a2`
  (incumbent), `settling-20261128T030313Z-459a6b` (full-register),
  `settling-20261128T030334Z-9e1d17` (materialization); pin
  re_derivations[34].
- AEE assessment: outcome **iterate**, seven claims assessed, 31
  failure modes, 14 residual unknowns; all seven claims draft-capped
  below the 0.70 threshold, all below 'explained' under the stage
  cap. Filed at `records/aee-assessment-2026-11-28.json` (schema
  1.0, methodology 2.1, project `112-meroitic-structure-induction`,
  phase after_plan), computed by the repo's own AEE engine
  (`aee` 1.6.0) over `aee-claims.json`, in the same form as Spec
  110's filed assessment.
- TC-112-01 (package form): **PASS** — bundle ids and order equal
  claims.md C112-1..C112-7; every claim carries a falsifier and a
  does-not-establish line in both files; spec.md states the corpus
  pins, the three targets, the preflight with its floors, the
  Stage-5 relation, the execution sequence, and the kill criteria.
  The check is filed at `records/tc112-01-package-form.py` and was
  run with payload exit 0.
- TC-112-02 (corpus pins): **PASS**, from the custody objects. The
  Kovetsky build stands at commit
  `145af0836c071e7c9796d37d4b36add00d347c8a`, and its
  `data/inscriptions.jsonl` recomputes to the registered source
  SHA-256 `1e91e3a0c52626482bc4015b597df862e7818602dab48a7e870240ab2e567bc4`
  (the source hash as Specs 097/102/105 define it). The Otten pin
  `c9158f6865325877112b6b9ceef83b3c80a93c56` is the pinned commit of
  the authors' public repository (Spec 097 step-0 identity record),
  not a file hash: the restoration staging clone stands at that
  commit (tree `76138c53118dbc273068f1ad1e5d411b3e3362fd`), and its
  `Data/mero-corpus.txt` (SHA-256
  `b7f3350c2f2118a8223854462a8e881c424cba6b26c01ebfb676efa92ea253ce`,
  18,090 lines) is byte-identical to the custody copy.
- Taxonomy: Spec 112 placed in `program-map-taxonomy.json` under
  Program infrastructure / Governance, lifecycle & generated
  layers, alongside Spec 109 — the taxonomy carries no same-family
  Meroitic-study placement, its studies being flat under
  domain/subdomain; studies count 113.
- Intake: **7 appended, 0 already canonical, 7 propositions.**
  Ledger 1,156 → **1,163 lines**. `validate_ledger` PASS, errors
  none: **1,114 claims** (bundle 1,091, extracted 23); falsifier
  coverage 1,105 of 1,114.
- Canonical verification before the pin moved: `verify-canonicals`
  **6/6 PASS** over the grown build.
- The T405 pair, re-executed with the canonical invocations (scope
  verbatim from the incumbent records' `key.command`, 286 Mahadevan
  signs): incumbent run `settling-20261128T092257Z-31e57c`,
  full-register run `settling-20261128T092422Z-7b9cea`. **Both
  result blocks are byte-equal to the superseded generation's, and
  the records are equal in every block except `run` and `pins` —
  the only difference is the ledger pin itself.** The Stage 4
  dual-run comparison was re-filed at
  `specs/086-winning-combination-adoption/records/stage-4-dual-run-comparison.json`;
  its diff against the previous filing is exactly the ledger pin
  (sha256 + lines).
- Materialization re-run: `settling-20261128T092534Z-fe9b95`; the
  assignment sets are unchanged (incumbent 94 assignments,
  full-register 286, H003 out of frame).
- Canonical hash of the grown ledger:
  `7f01d66eaff2e3e2fae55c208db3344706b92844e0da9dddbd2ee9446025ba32`
  (1,163 lines).
- Pin refresh: re_derivations entry **[35]** appended to
  `glossa-indus/ledger/settling-canonical.json` in the established
  form (prior pin a09fb02f…/1,156 → new pin 7f01d66e…/1,163,
  expectations_changed false, verification naming the pair, the
  comparison and the materialization), and `provenance.ledger`
  moved in the same motion.

## The generated layers and the census

- Matrix: 1,637 cells (matrix.json SHA-256 `014f6635…`).
- Evidence map: 1,762 elements (1,114 claims); edges 1,637;
  falsifier census 1,105 of 1,114 claims carry a falsifier, the
  same 9 pre-existing gaps (the seven Spec 112 claims all carry
  falsifiers); settling runs carried: 2 (the new pair).
- Program map: 1,114 claims · 113 studies · 28 unjudged studies ·
  0 judgment calls; claims by governing class: positive 10,
  negative 7, open 1,095, closed_other 2.
- Census pins updated from the regenerated actuals:
  `backend/tests/test_program_map_conformance.py`,
  `backend/tests/test_spec086_map.py`,
  `backend/tests/test_spec086_ledger_gate.py`,
  `backend/tests/test_spec095_stage4_instantiation.py`,
  `backend/tests/test_spec095_t403_dashboard.py` (including the
  T405 run of record, now `settling-20261128T092257Z-31e57c`), and
  the two frontend e2e census texts (1,114). Over the final tree
  the five files pass: **114 passed** (pin-correction rounds over
  the cascade trees: 20 failed / 94 passed, then 8 failed / 106
  passed, then 0 — every failure a census pin read from the
  regenerated actuals, or the expected V11 run-binding state the
  completion acts clear).
- Ledger gate over the final tree: **32 PASS / 0 FAIL / 1 NOT-RUN —
  RESULT: PASS.**

## Finalization

- Registration commit: `3bc03038081c3a4170eacc73f3c52d1746a7a3cf`
  (the Spec 112 package, the AEE assessment and its ledger files,
  the taxonomy placement, the grown ledger, the refreshed
  canonical, the re-filed comparison, the new run records, the
  assignment sets, the matrix and the program map).
- Departures (this completion commit): the superseded generation's
  three run records (22d2a2, 459a6b, 9e1d17) depart the store under
  run-defs v3 §7.1; their departure acts in `run-index.jsonl` name
  the records, their blob hashes, and the registration commit as
  `superseded_by_commit`. The legacy-index completion pass appended
  the legacy entry act for re-derivation [35] (folded census 148
  entries). Both gated publications were re-run over the final
  tree and passed the full gate, so the published bytes are the
  gated bytes.
- No standing, verdict or tally moved anywhere in the program: the
  seven claims entered at stage `created`, status `draft`, and the
  cascade's only ledger effect is their intake. No induction was
  executed under Spec 112, and no corpus output exists.

*This record was executed by an AI agent (Muse, via Muse) at the
direction of Tristen Pierson, per constitution sec. VI.*
