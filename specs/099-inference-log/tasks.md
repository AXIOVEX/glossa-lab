# Spec 099 — Tasks

## Stage 0 — Adoption (this PR)

- [ ] T001 — Package authored: spec.md, claims.md,
      aee-claims.json, plan.md, tasks.md, test-cases.md,
      tools/inference_log.py (reference implementation),
      tests/test_inference_log.py.
- [ ] T002 — Test cases executed on the fixtures
      (TC-099-01, TC-099-02, TC-099-03); payload verdicts
      recorded in records/tc-execution-2026-11-21.md.
- [ ] T003 — AEE assessment of the claims bundle run and
      filed (records/adoption-aee-assessment.json); absence
      recorded if the CLI cannot run.
- [ ] T004 — Registration: claims bundle intaken into the
      canonical ledger; taxonomy entry added; settling chain
      executed in the standing order (verify-canonicals,
      T405 pair byte-equal, comparison re-filed, assignment
      sets re-materialized, canonical pin refreshed,
      departure accounted); generated layers regenerated;
      census pins updated from actuals; affected tests run.
      Record: records/adoption-and-registration-2026-11-21.md.

## Stage 1 — The log

- [ ] T101 — Builder assembles the 94 entries from the
      appendix rows, the standings record, and the
      falsifiers annex; extraction proposes items over the
      checkable families.
- [ ] T102 — Every item typed by reading its basis clause;
      every (b) item verified against the filed basis text;
      ambiguous items recorded with reasons; status notes
      applied from the landed records (withdrawn, FAILED,
      struck).
- [ ] T103 — TC-099-01 over all 94 rows (schema validation,
      full mode) and TC-099-02 over the real bases against
      the real log; payload verdicts recorded.
- [ ] T104 — The log lands by PR: the JSON record and its
      generated human-readable rendering; the edge census
      stated in the PR record.

## Stage 2 — The audit and the M267 statement

- [ ] T201 — The reference audit runs over the landed log;
      TC-099-03's independent implementation recomputes it
      from the log alone; the two compared exactly.
- [ ] T202 — The completion record written: per-reading
      outcomes under both treatments with divergences, the
      component result, the open ends, the spot-check
      comparison in the spot-check's own terms, and the
      M267 dependency statement (spec section 5).
- [ ] T203 — The completion record filed into
      specs/091-anchor-comparison-integrity/records/ as the
      Q3 audit's completion record, with a copy under this
      spec's records/; the package closes. No standing,
      anchor, or register entry is altered.

## Standing constraints

- Execution on tower-compute only, fresh clone per PR under
  ~/glossa-work/; the protected VM checkout and the
  mini-server origin tree are never touched.
- PRs merge only on genuine per-job CI 10/10; wrapper success
  is not job success; zero-step is NO VERDICT.
- Branch and worker clone deleted in the same motion after
  each merge.
- No M267 retest is run or designed in executable detail
  (C099-7); no class change the audit implies is executed
  (C099-5).
