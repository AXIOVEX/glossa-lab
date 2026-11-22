# Spec 099 — Plan

## Grounding (read before this plan was written)

- `specs/091-anchor-comparison-integrity/records/coscientist-audit-94-adjudication-2026-11-21.md`
  — the adjudication: Q3's twelve items and their executed
  outcomes (sections of record for 17 readings), the blocked
  graph-audit unit, the class vocabulary, the source-diversity
  flags for all 94.
- `specs/091-anchor-comparison-integrity/records/dependency-record-2026-11-21.md`
  — the dependency chains of record and the closure list this
  package executes items (1) and (2) of.
- `specs/091-anchor-comparison-integrity/records/standings-relabel-execution-2026-11-21.md`
  — the executed standings for all 94 (the log's coverage
  source of record) and the addendum reclassification rule the
  audit's class recomputation applies.
- `specs/091-anchor-comparison-integrity/records/standings-supplement-2026-11-21.md`
  — the E decomposition, the M267 withdrawal and slot markers
  of record, the motif and numerical annotations the log
  carries as status notes.
- `specs/091-anchor-comparison-integrity/records/per-reading-falsifiers-2026-11-21.md`
  — the falsifiers annex: each reading's evidence line as
  filed, the cross-check source for extraction.
- The audit package brief and appendix
  (`coscientist-audit-94` package of 2026-11-20/21): the
  appendix's per-reading basis text as filed from the register
  is the log's primary extraction source; its Q3 framing is
  the audit's question.
- `glossa-corpus/indus/ANCHOR_STATUS_AUDIT.csv` — the frozen
  register snapshot the appendix was filed from; the
  extraction cross-check.
- Spec 098's package (`specs/098-identifiability-over-the-65/`)
  — the form this package follows: adoption record, claims
  bundle, registration machinery, census pins.

## Adoption mechanics

1. This package (spec, claims, plan, tasks, test cases, the
   reference implementation and its tests, the adoption
   records) lands by PR on a fresh clone on tower-compute.
2. Registration, in the standing order (Spec 098's D-098-2
   pattern): the claims bundle is intaken through
   `tools/ledger/import_bundle.py`; the taxonomy gains the
   study entry; the settling chain runs in order —
   verify-canonicals over the grown build before the pin
   moves, the T405 scenario pair re-executed with byte-equal
   result blocks, the comparison re-filed, the assignment
   sets re-materialized, the canonical pin refreshed with its
   `re_derivations` entry, the superseded generation's
   departure accounted; the generated layers regenerate in
   dependency order (matrix, map data, program map); every
   census pin in the conformance and dashboard tests is
   updated from the regenerated actuals and the affected
   tests run before the PR opens.
3. The AEE assessment of the bundle is run and filed under
   `records/` (the draft-stage reading is expected; an
   inability to run it is recorded, never papered over).

## Stage plan

- **Stage 1 — the log.** A builder under this spec's `tools/`
  assembles the 94 entries from the appendix rows (the basis
  text as filed), the standings record (reading, class,
  flag), and the falsifiers annex (cross-check). Extraction
  proposes items programmatically (the checkable families of
  `tools/inference_log.py`); the typing of every item, and
  above all every (b) item, is settled by reading the basis
  clause it cites. Ambiguous cases are recorded ambiguous
  with their reason. TC-099-01 runs over all 94 rows;
  TC-099-02 runs the completeness checker over the real bases
  against the real log. The log lands by PR as JSON plus its
  human-readable rendering.
- **Stage 2 — the audit.** The reference implementation runs
  over the landed log; TC-099-03's independent implementation
  recomputes the audit from the log alone and the two are
  compared exactly. The completion record — the audit table
  for all 94, the component result, the open ends, the
  spot-check comparison in the spot-check's own terms, and
  the M267 dependency statement — is filed into the Spec 091
  records as the Q3 audit's completion record, with a copy
  under this spec's `records/`. The package closes when the
  completion record is on the record. No standing moves.

## Verification

- Every stage's checks run on tower-compute in the stage's
  own fresh clone; each run's raw output is filed or hashed
  in the stage record, and the verdict reported is the run's
  own payload verdict (C099-8).
- PRs merge only on genuine per-job CI green across all ten
  jobs; a zero-step or cancelled run is NO VERDICT, never
  green.
- The log's human-readable rendering is generated from the
  JSON, never edited separately, so the two cannot drift.

## Risks and limits

- **Basis truncation.** Eight appendix rows are truncated
  mid-clause. The log records the truncation on the affected
  items (ambiguous where the truncated text is the item's
  evidence); the audit's result is a result over the bases as
  filed, and the completion record says so.
- **Extraction judgment.** The checkable families are
  mechanical, but item boundaries in prose bases are judgment
  calls; the discipline that bounds them is C099-2's second
  direction (nothing in the log the basis does not state) and
  the verbatim-span requirement, which makes every judgment
  call auditable against the filed text.
- **Unnamed targets.** (b) items whose bases name no target
  bound the component result; the completion record lists
  them as open ends rather than letting the component result
  read as complete (C099-6).
