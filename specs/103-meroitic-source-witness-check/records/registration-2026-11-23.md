# Spec 103 — Registration Record (2026-11-23)

**Commission.** Owner decision **OD-D-2**, decided by
the owner, Tristen Pierson, on **2026-11-23 at ~17:14
ET**: the source-witness check proposed in Round D
unit D-M-3 of the Co-scientist sweep adjudication
(`specs/091-anchor-comparison-integrity/records/coscientist-sweep-adjudication-2026-11-23.md`,
§4 and §7 addendum) is commissioned — registration
and execution in one act, in two landings: this
registration first, the execution second, as its own
record. The registration carries the session's stated
claim and kill check, the fixed split membership, and
the no-pooling rule for the xolkte family, as §4 of
the adjudication required.

- **Number decision (D-103-1).** At the check of
  2026-11-23 the highest landed spec package on
  origin/main was 102
  (`specs/102-meroitic-fresh-affiliation-test/`); no
  103 directory existed and no branch carried 103.
  This package takes 103. The branch was cut from
  origin/main `2b7eb59d` (the OD-D-1 recording
  landing); no rebase was needed.

## 1. What was registered

`specs/103-meroitic-source-witness-check/` — spec.md,
claims.md, aee-claims.json, plan.md, tasks.md,
test-cases.md (TC-103-01..TC-103-06), this record,
and the AEE assessment below. The diagnostic: for
the six Stage 4.4 candidate forms (soreyi, asoreyi,
xolkete, pxolkete, xolkte, wisi), check every
decision-bearing locus, and census the near-form
space, against the acquired build's own source
witnesses (each row's open alternative readings and
the build's `data/expansion/` transcriptions),
recompute the counts the witnesses support within
the frozen partition, and state per form whether
the frozen outcome's legs survive adjudicated
corrections (spec.md §3). The claim under test
(C103-1, the session's, verbatim in substance): the
frozen extraction preserves the source distinctions
and text-presence counts needed for these candidate
decisions. The kill check: a demonstrated
source/extraction discrepancy that crosses a
registered decision boundary kills the claim for
the affected candidate; if adjudicated source
corrections leave every relevant threshold outcome
unchanged, the input-error explanation of the
failures is retired within the checked scope; if
witnesses or search coverage are insufficient, the
outcome is NOT CHECKED / INCOMPLETE COVERAGE, not
verified absence. Fixed split membership (C103-2):
corrections apply to token counts within the frozen
partition; no corrected text is rehashed; no text
changes side. No pooling (C103-3): xolkete,
pxolkete, and xolkte are checked and reported as
distinct forms; no variant is pooled or counted
toward a candidate; no character is corrected by
its effect on a score. No standing moves (C103-4):
the frozen Stage 4.4 outcome (1 PARTIALLY
SUPPORTED, 5 UNSUPPORTED) stands whatever the check
finds; a kill licenses only a separately registered
corrected-input sensitivity.

Witness scope, stated plainly (spec.md §3, D-103-4):
the check is internal to the acquired build
(Kovetsky, pin
`145af0836c071e7c9796d37d4b36add00d347c8a`). The
settling record for a contested sign — Griffith's
printed editions and the modern REM edition — is
not machine-readable here and edition images are
not held (corpus completion record §4, gap 5), so
the check cannot certify the build against the
editions; that limit is registered, not discovered
mid-execution. No Otten material is an input at
all: the Stage 4.4 basis is the acquired build
alone.

## 2. The AEE outcome at registration

`records/aee-assessment-2026-11-23.json` — run_aee.py
assess --phase after_plan (aee 1.5.3) over the
bundle's aee-claims.json: outcome **iterate**; 4
claims assessed, all 4 draft-capped below the 0.70
confidence threshold — the expected shape for draft
claims at registration, the same shape Specs 101
and 102 returned. The assessment's own ledger
entries were written by the tool under
`.specify/extensions/aee/` and are carried in this
landing. (Venue note: the tower's relocated
`glossa-ci` venv's console scripts carry stale
shebangs from the 2026-11-23 home cleanup, so the
assessment ran through a PATH shim invoking the
venv's interpreter directly; the tool and version
are the program's own.)

## 3. Registration cascade (executed figures)

- Taxonomy: Spec 103 added to the program-map
  taxonomy under Sign inventory & corpus / Signary
  & corpus models (decision D-103-5, with Specs 097
  and 102); studies 103 → 104.
- Intake: the bundle's 4 claims appended through
  tools/ledger/import_bundle.py, dated 2026-11-23
  (4 appended, 0 already canonical). Ledger 1,072 →
  1,076 lines; claims 1,041 → 1,045; canonical
  SHA-256 `d04a481054269ff17c58f6fdb5189b6726fa6eb074d312193f55fb36e3833660`
  → `14c925e8750701976c7befb106f033e74f949379134820b3a25772a40584d576`.
  verify-canonicals over the grown build, before
  any pin moved: **6/6 PASS**.
- Settling layer: both T405 scenarios re-executed
  over the grown build (runs
  `settling-20261123T222738Z-c1c0ef` incumbent,
  `settling-20261123T222739Z-741a2f` full-register,
  same 286-sign full-frame scope, same registered
  scenario ids); both result blocks byte-equal to
  the superseded generation's, verified by direct
  comparison of the stored records. The Stage 4
  dual-run comparison re-filed from the new pair
  (its diff against the previous filing is the
  ledger pin only). Assignment sets re-materialized
  unchanged (run `settling-20261123T222752Z-fbc1dc`;
  incumbent 94, full-register 286, H003 out of
  frame). The canonical pin refreshed as
  re_derivations[19] of settling-canonical.json.
  The superseded generation
  (settling-20261122T190229Z-7ae82f,
  settling-20261122T190229Z-658afe,
  settling-20261122T190250Z-2f43b6) departed the run
  store in this landing; their departure acts are
  appended to the run index through
  `run_records.append_act` in the landing's
  completion commit, naming the registration commit
  as `superseded_by_commit` and each record's blob
  hash from the pre-landing tree. The run-index
  completion pass (build_legacy_index.py) entered
  the legacy events for re_derivations[17], [18],
  and [19] and named the departed records post-spec
  skips (folded census 81 entries).
- Generated layers, regenerated in dependency
  order: matrix 1,568 cells (supports 1,561,
  opposes 7) over 1,045 rows; map-data 1,689
  elements, 1,568 edges, settling runs carried 2;
  program map: 1,045 claims, 104 studies. Falsifier
  census 1,036 of 1,045 claims, the same 9 gaps.
- Census pins updated from the regenerated actuals
  in test_spec095_stage4_instantiation.py,
  test_spec086_ledger_gate.py,
  test_spec095_t403_dashboard.py (including the
  T405 run of record, re-pinned to
  settling-20261123T222738Z-c1c0ef, whose quantities
  are the superseded generation's, byte-equal),
  test_spec086_map.py,
  test_program_map_conformance.py (including the
  Sign inventory & corpus domain census 19 → 20),
  and the frontend e2e census texts
  (frontend/e2e/system-graph.spec.ts,
  frontend/e2e/researcher-dashboard.spec.ts):
  claims 1,041 → 1,045; bundle population 1,018 →
  1,022; open class 1,032 → 1,036; falsifier-present
  1,032 → 1,036; draft status 1,017 → 1,021; ledger
  lines 1,072 → 1,076; studies 103 → 104; matrix
  cells and map edges 1,564 → 1,568; map elements
  1,685 → 1,689; supports edges 1,557 → 1,561;
  claims untouched by any run 1,040 → 1,044.
- Sweep records: the §7 OD-D-2 addendum appended to
  the Round D sweep adjudication record; ledger row
  D-M-3 moved open → accepted, with the counts
  recounted from the rows (Meroitic Round D 0 done /
  3 accepted / 0 open; totals 119 rows — 63 done /
  35 accepted / 0 adjudicating / 0 open / 21
  rejected).

## 4. Standing

Spec 103 is REGISTERED. Its execution is
commissioned by the same owner act (OD-D-2) and
lands as the second landing under this
registration, filing its outcome record in this
spec's records/ and moving ledger row D-M-3 to
done. No standing, verdict, or tally is changed by
this registration.

**Venue.** All work for this package ran on
tower-compute in the fresh clone
`~/.syncyard/worktrees/glossa/sw103-reg` (branch
`spec-103-source-witness-check`). Nothing ran in
the coordination VM or on the mini-server.

**AI disclosure:** executed by an AI agent (Muse,
via Muse) at the direction of Tristen Pierson, per
constitution sec. VI.

## Completion pass (2026-11-23, same landing)

- **Departure acts appended.** The three superseded
  settling records named in §3 departed the run store
  in this landing; their departure acts were appended
  to the run index through `run_records.append_act`
  in this completion commit, naming the registration
  commit `3dea279b9a64eb31bd96cf1846872fd60241c448`
  as `superseded_by_commit` and each record's blob
  hash from the pre-landing tree, as §3 anticipated.
- **Final-tree verification.** The ledger gate on
  the final tree, both modes, run standalone:
  **default 29 PASS / 0 FAIL / 1 NOT-RUN (RESULT:
  PASS)** and **--regen 32 PASS / 0 FAIL / 0 NOT-RUN
  (RESULT: PASS)**. (The single NOT-RUN in default
  mode is the V7 lossless-regeneration check, which
  runs under --regen.) The five affected backend
  suites were run on the final tree: **114 tests,
  all passed**. One further census pin the intake
  moves was caught by these runs and updated in
  this completion commit: program-map study nodes
  103 → 104 (test_spec086_ledger_gate.py).
