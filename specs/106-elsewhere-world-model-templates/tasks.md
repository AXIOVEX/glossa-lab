# Spec 106 — Tasks

## Stage 0 — Registration

- [x] **T001 — Package lands, framework and templates
  frozen.** framework.md, spec.md, claims.md,
  aee-claims.json, plan.md, tasks.md, test-cases.md,
  templates/ (three baseline templates, each carrying its
  seed record), records/elsewhere-seed-and-iteration-log.md
  (opened, seed entry only), and records/census-audit.py
  committed as `specs/106-elsewhere-world-model-templates/`.
  Acceptance: **test** (TC-106-01: aee-claims.json parses;
  claims.md and aee-claims.json carry the same six claim ids
  in the same order; every claim has a falsifier and a
  does-not-establish line). *This does not establish:* that
  any instance exists — Stage 0 registers the framework and
  the baselines.
- [x] **T002 — Owner acts recorded.** The owner's orders of
  2026-11-25 (Glossa-Lab chat, 12:39 ET and 12:44 ET) are the
  adoption acts of record, filed in
  `records/registration-2026-11-25.md`. Acceptance:
  **record**.
- [x] **T003 — Mechanical audits.** TC-106-02..TC-106-05 run
  over the assembled package through
  `records/census-audit.py`; output filed as
  `records/census-audit-output-2026-11-25.txt`. Acceptance:
  **test** (zero violations; every stated count and hash
  recomputes).
- [x] **T004 — Ledger intake and full registration.** The
  C106-1..C106-6 bundle intaken into the canonical ledger
  through `tools/ledger/import_bundle.py`; the taxonomy
  entry added (Program infrastructure / Governance, per
  D-106-2); the settling chain refreshed in the standing
  order; the generated layers regenerated; census pins
  updated from the regenerated actuals. No
  recommendations-ledger row (D-106-3). Acceptance:
  **test** (the ledger gate and the program-map conformance
  checks pass on the landed tree). The intake figures stand
  in `records/registration-2026-11-25.md` as executed.

## Stage 1 — First ensembles (not commissioned)

- [ ] **T101 — First instance spawning.** Under a separate
  owner commission: spawn the first ensemble from one
  baseline template under the framework's seeding and
  iteration protocols, with the study's log carrying every
  iteration. Claims: none of C106-1..C106-6 (a Stage 1 study
  registers its own). *This task is a placeholder naming the
  stage boundary; it is not authorized by this
  registration.*
