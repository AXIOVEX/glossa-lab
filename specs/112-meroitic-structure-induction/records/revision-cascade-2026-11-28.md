# Spec 112 — Revision registration cascade — 2026-11-28

The record of the claims-ledger intake cascade that carried the
four revision claims (C112-8..C112-11) onto the canonical ledger,
executed 2026-11-28 in the revision worktree
(`spec112-rev-wt-20261128`, branch `spec-112-revision`, base main
`63408e1c`, the merge of PR #814). The discipline followed is the
standing one (run-defs v3 §7; the Spec 112 registration cascade is
the procedure of record, the Spec 110 revision cascade its
revision-form instance): intake, canonical verification, the T405
pair re-executed over the grown build, the pin refreshed as a new
re-derivation, the generated layers regenerated, the superseded
generation departed, and every census pin updated from the
regenerated actuals. Every figure below was measured in the
worktree at execution time.

## Serialization disclosure

Main did not advance during this landing: the branch was taken
from `63408e1c` and origin/main still stood at `63408e1c` when the
pull request opened, so the cascade executed exactly once, over
the merged build described below. Three execution incidents are
disclosed on their face: (1) the pin-append script's first version
matched the wrong array close in `settling-canonical.json` and
wrote a malformed file; the file was restored from git before any
commit and the append was redone as a surgical text insertion,
parse-validated before the write — the landed bytes are the
validated ones, and the diff is 19 insertions / 2 deletions as in
the established form. (2) The dual-run comparison was first
re-serialized in sorted key order (a 45/45 reformat diff); it was
restored and re-filed by surgical substitution of the two pin
values, so its landed diff is exactly the ledger pin. (3) The
gated matrix publication was refused mid-cascade, correctly (the
gate stood red on the stale generated layers and the V11
run-binding); the layers were regenerated ungated for the census
actuals, and both gated publications are re-run over the final
tree in the completion step, as in the Spec 112 cascade. The
census pins, the departure acts, the legacy-index act and this
record land across the registration and completion commits in the
established split.

## The baseline and the growth

- Baseline (main at `63408e1c`): ledger 1,163 lines, canonical
  SHA-256 `7f01d66eaff2e3e2fae55c208db3344706b92844e0da9dddbd2ee9446025ba32`;
  settling generation of record `settling-20261128T092257Z-31e57c`
  (incumbent), `settling-20261128T092422Z-7b9cea` (full-register),
  `settling-20261128T092534Z-fe9b95` (materialization); pin
  re_derivations[35].
- AEE assessment: outcome **iterate**, four claims assessed, 23
  failure modes, 8 residual unknowns; all four claims draft-capped
  below the 0.70 threshold, all below 'explained' under the stage
  cap. Filed at `records/aee-assessment-revision-2026-11-28.json`
  (schema 1.0, methodology 2.1, project
  `112-meroitic-structure-induction`, phase after_plan), computed
  by the repo's own AEE engine (`aee` 1.6.0) over
  `claims-revision.json`, in the same form as Spec 110's filed
  revision assessment.
- TC-112-09 (revision package form): **PASS** — bundle ids and
  order equal claims.md C112-8..C112-11; every revision claim
  carries a falsifier and a does-not-establish line in both files;
  the revision registration names the three filed failure
  mechanisms and the design answers and states that no floor,
  ground-truth set, or scoring rule changed. The check is filed
  at `records/tc112-09-package-form.py` and was run with payload
  exit 0.
- Intake: **4 appended, 7 already canonical, 11 propositions.**
  Ledger 1,163 → **1,167 lines**. `validate_ledger` PASS, errors
  none: **1,118 claims** (bundle 1,095, extracted 23); falsifier
  coverage 1,109 of 1,118, the same 9 pre-existing gaps.
- Canonical verification before the pin moved: `verify-canonicals`
  **6/6 PASS** over the grown build.
- The T405 pair, re-executed with the canonical invocations (scope
  verbatim from the incumbent records' `run.key.command`, 286
  Mahadevan signs): incumbent run `settling-20261128T104041Z-9c65d4`,
  full-register run `settling-20261128T104041Z-5585a9`. **Both
  result blocks are byte-equal to the superseded generation's, and
  the records are equal in every block except `run` and `pins` —
  the only difference is the ledger pin itself.** The Stage 4
  dual-run comparison was re-filed at
  `specs/086-winning-combination-adoption/records/stage-4-dual-run-comparison.json`;
  its diff against the previous filing is exactly the ledger pin
  (sha256 + lines).
- Materialization re-run: `settling-20261128T104053Z-c68cfb`; the
  assignment sets are unchanged (incumbent 94 assignments,
  full-register 286, H003 out of frame).
- Canonical hash of the grown ledger:
  `0eb3f3ffe82bcf35304f01b1be52a203643814971aefe1b7c0fad3be22e16039`
  (1,167 lines).
- Pin refresh: re_derivations entry **[36]** appended to
  `glossa-indus/ledger/settling-canonical.json` in the established
  form (prior pin 7f01d66e…/1,163 → new pin 0eb3f3ff…/1,167,
  expectations_changed false, verification naming the pair, the
  comparison and the materialization), and `provenance.ledger`
  moved in the same motion; the append was surgical (19
  insertions, 2 deletions — the deletions are the provenance pin's
  two lines) and entry [35] is byte-untouched.

## The generated layers and the census

- Matrix: 1,641 cells (matrix.json SHA-256 `33167f2a…`), 1,118
  rows, 649 columns.
- Evidence map: 1,767 elements (1,118 claims); edges 1,641;
  falsifier census 1,109 of 1,118 claims carry a falsifier, the
  same 9 pre-existing gaps (the four revision claims all carry
  falsifiers); settling runs carried: 2 (the new pair).
- Program map: 1,118 claims · 113 studies · 28 unjudged studies ·
  0 judgment calls; claims by governing class: positive 10,
  negative 7, open 1,099, closed_other 2.
- Census pins updated from the regenerated actuals (33 updates):
  `backend/tests/test_program_map_conformance.py`,
  `backend/tests/test_spec086_map.py`,
  `backend/tests/test_spec086_ledger_gate.py`,
  `backend/tests/test_spec095_stage4_instantiation.py`,
  `backend/tests/test_spec095_t403_dashboard.py` (including the
  T405 run of record, now `settling-20261128T104041Z-9c65d4`), and
  the two frontend e2e census texts (1,118). The first census run
  over the grown tree read **19 failed / 95 passed** — every
  failure a census pin read from the regenerated actuals, or the
  V11 run-binding state the completion acts clear.
- Ledger gate mid-cascade: **31 PASS / 1 FAIL / 1 NOT-RUN** — the
  FAIL is V11 run-binding, naming exactly the three departed
  records of the superseded T405 generation; the NOT-RUN is V7,
  which runs under `--regen` in the push CI job.

## Finalization

- Registration commit: `e5ee35f7ed6db61e1f8ba00c663ab5b3e6dc5db0` (the Spec 112
  revision package, the AEE assessment and its ledger files, the
  grown ledger, the refreshed canonical, the re-filed comparison,
  the new run records, the assignment sets, the matrix, the
  evidence map, the program map, and the departure of the
  superseded generation's three run records from the store).
- Departures (the completion commit): the superseded generation's
  three run records (31e57c, 7b9cea, fe9b95) depart the store
  under run-defs v3 §7.1; their departure acts in `run-index.jsonl`
  name the records, their blob hashes, and the registration
  commit as `superseded_by_commit`. The legacy-index completion
  pass appended the legacy entry act for re-derivation [36] (1 act; folded census 152 entries).
  Both gated publications were re-run over the final tree and
  passed the full gate, so the published bytes are the gated
  bytes; the ledger gate over the final tree reads **32 PASS /
  0 FAIL / 1 NOT-RUN — RESULT: PASS**.
- No standing, verdict or tally moved anywhere in the program:
  the four claims entered at stage `created`, status `draft`, and
  the cascade's only ledger effect is their intake. No induction
  was executed under the revision, and no corpus output exists.

*This record was executed by an AI agent (Muse, via Muse) at the
direction of Tristen Pierson, per constitution sec. VI.*
