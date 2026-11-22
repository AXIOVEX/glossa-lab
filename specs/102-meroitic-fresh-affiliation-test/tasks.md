# Spec 102 — Tasks

## Stage 0 — Registration

- [x] **T001 — Package lands, design frozen.**
  spec.md, claims.md, aee-claims.json, plan.md,
  tasks.md, test-cases.md and records/ committed as
  `specs/102-meroitic-fresh-affiliation-test/`; the
  design, its material gates (G-1, G-2), its power
  profile, and its adjudication vocabulary frozen in
  spec.md §§3–5. Acceptance: **test** (aee-claims.json
  parses; claims.md and aee-claims.json carry the
  same five claim ids in the same order; every claim
  has a falsifier and a does-not-establish line).
  *This does not establish:* that the study has run —
  Stage 0 registers and freezes it.
- [x] **T002 — Owner act recorded.** The owner's
  OD-21 act of 2026-11-22 13:51 ET (adjudication unit
  M-18: commission, after the preceding checks, a
  genuinely fresh discriminating test for Meroitic
  on new or independent material) is the adoption
  act of record, filed in
  `records/registration-2026-11-22.md`. Acceptance:
  **record**.
- [x] **T003 — Design-stage counting and power
  simulation.** The held-material ceiling, comparator
  coverage, reconstruction pool, and the design's
  power profile computed on tower-compute by the
  program's own frozen pipeline code, and filed at
  `records/design-stage-counts-2026-11-22.md` with
  the script at `tools/design_power_sim.py`.
  Acceptance: **test** (the counts recompute from
  the custody holdings; the simulation's Stage 4.2
  validation figures reproduce the executed record's
  asymmetry).
- [ ] **T004 — Ledger intake and full registration.**
  The C102-1..C102-5 bundle intaken into the
  canonical ledger through
  `tools/ledger/import_bundle.py`; the taxonomy entry
  added (Sign inventory & corpus / Signary & corpus
  models, per D-102-3); the settling chain refreshed
  in the standing order; the generated layers
  regenerated; census pins updated from the
  regenerated actuals. Acceptance: **test** (the
  ledger gate and the program-map conformance checks
  pass on the landed tree). The intake figures stand
  in `records/registration-2026-11-22.md` as executed.

## Stage 1 — Wordlist acquisition — GATED (fresh owner commission; the acquisition itself is a separate owner-gated act)

- [ ] **T101 — S-1 acquired and digitised.** The
  fuller published wordlist (spec §3.1, S-1)
  acquired by the route the owner directs and
  digitised into a vocabulary file with per-entry
  source apparatus (author, year, pages), in the
  gold lexicon's form. Claims: C102-5. Test:
  TC-102-05.

## Stage 2 — Vocabulary build and attestation — GATED

- [ ] **T201 — Expanded vocabulary built.** The
  digitised wordlist mapped under a complete
  gloss→concept table; attestation filter run
  against the S-2 corpus under the §3.6 split
  construction; excluded forms counted and listed.
  Claims: C102-1, C102-2, C102-4, C102-5. Tests:
  TC-102-04, TC-102-05.

## Stage 3 — Freeze and gates — GATED

- [ ] **T301 — Freeze filed, gates computed.** The
  freeze carries the complete mapping table, the
  per-concept denominators with labels verified
  against parameters.csv, the registered seed, and
  the G-1/G-2 computations. If either gate fails,
  the study closes NOT ADMINISTERED here. Claims:
  C102-3, C102-4. Tests: TC-102-01, TC-102-02,
  TC-102-04.

## Stage 4 — Scoring — GATED (only on both gates passing)

- [ ] **T401 — Leg A scored.** Both family tests and
  the comparability subset scored; Arm R computed
  and filed separately as exploratory; the run
  executed twice with byte-identical outcomes and
  an independent recomputation. Claims: C102-1,
  C102-2. Tests: TC-102-03, TC-102-05.

## Stage 5 — Outcome — GATED

- [ ] **T501 — Outcome record and adjudication
  package.** The outcome stated in spec §5's
  vocabulary only, with the consistency boundary in
  numbers; Leg B recorded as executed on its
  clarification or NOT ADMINISTERED (custody gate);
  the adjudication package prepared for the owner's
  approval act. Claims: C102-1, C102-2, C102-3,
  C102-5. Test: TC-102-06.
