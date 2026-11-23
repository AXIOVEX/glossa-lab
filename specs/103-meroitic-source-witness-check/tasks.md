# Spec 103 — Tasks

## Stage 0 — Registration

- [x] **T001 — Package lands, protocol frozen.**
  spec.md, claims.md, aee-claims.json, plan.md,
  tasks.md, test-cases.md and records/ committed as
  `specs/103-meroitic-source-witness-check/`; the
  claim and kill check, the protocol (Steps 1–4),
  and the outcome vocabulary frozen in spec.md
  §§3–4. Acceptance: **test** (TC-103-01: aee-claims.json
  parses; claims.md and aee-claims.json carry the
  same four claim ids in the same order; every claim
  has a falsifier and a does-not-establish line).
  *This does not establish:* that the check has run —
  Stage 0 registers and freezes it.
- [x] **T002 — Owner act recorded.** The owner's
  OD-D-2 act of 2026-11-23 (~17:14 ET; sweep
  adjudication unit D-M-3: commission the
  source-witness check) is the adoption act of
  record, filed in
  `records/registration-2026-11-23.md`, with the
  append-only §OD-D-2 addendum in the sweep
  adjudication record in the same landing. The act
  commissions registration **and** execution
  (spec.md §6). Acceptance: **record**.
- [x] **T003 — Ledger intake and full registration.**
  The C103-1..C103-4 bundle intaken into the
  canonical ledger through
  `tools/ledger/import_bundle.py`; the taxonomy entry
  added (Sign inventory & corpus / Signary & corpus
  models, per D-103-3); the settling chain refreshed
  in the standing order; the generated layers
  regenerated; census pins updated from the
  regenerated actuals; the recommendations ledger's
  D-M-3 row moved open → accepted. Acceptance:
  **test** (the ledger gate and the program-map
  conformance checks pass on the landed tree). The
  intake figures stand in
  `records/registration-2026-11-23.md` as executed.

## Stage 1 — Execution (second landing, under the same OD-D-2 commission)

- [ ] **T101 — Basis and counts reproduction.** The
  acquired build re-acquired openly, verified at pin
  `145af0836c071e7c9796d37d4b36add00d347c8a`; the
  ingestion, dedup, split, and Stage 4.4 counting
  recomputed under the frozen rules (spec.md §3.2).
  Claims: C103-1, C103-2. Test: TC-103-02.
- [ ] **T102 — Locus census and witness comparison.**
  The decision-bearing loci and near-form census
  enumerated over the 33 held-out texts (spec.md
  §3.3); each locus classified against the witnesses
  (spec.md §3.4) as FAITHFUL / DISCREPANCY /
  UNCERTAIN / WITNESS UNAVAILABLE. Claims: C103-1,
  C103-3. Tests: TC-103-03, TC-103-04.
- [ ] **T103 — Boundary adjudication and outcome
  record.** Adjudicated corrections applied within
  the frozen partition (spec.md §3.5); the kill check
  applied per candidate; the outcome record filed in
  spec.md §4's vocabulary with the full census,
  classifications, and §5 interpretation limits; the
  recommendations ledger's D-M-3 row moved to done
  if the execution completes. Claims: C103-1,
  C103-2, C103-3, C103-4. Tests: TC-103-05,
  TC-103-06.
