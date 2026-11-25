# Spec 104 — Tasks

## Stage 0 — Registration

- [x] **T001 — Package lands, benchmark frozen.**
  spec.md, claims.md, aee-claims.json, plan.md,
  tasks.md, test-cases.md and records/ committed as
  `specs/104-quantum-alignment-benchmark/`; the
  instance and score matrix (spec.md §2), the QUBO
  formulation and its lemma (§3), the three arms and
  their registered parameters (§4), the scaling
  generation (§5), and the verdict vocabulary (§6)
  frozen. Acceptance: **test** (TC-104-01:
  aee-claims.json parses; claims.md and aee-claims.json
  carry the same four claim ids in the same order;
  every claim has a falsifier and a does-not-establish
  line). *This does not establish:* that the benchmark
  has run — Stage 0 registers and freezes it.
- [x] **T002 — Owner act recorded.** The owner's
  order of 2026-11-25 (Glossa-Lab chat: "do the
  quantum alignment benchmark after the program doc",
  following his decipherment gap analysis of the same
  day) is the adoption act of record, filed in
  `records/registration-2026-11-25.md`. The act
  commissions registration **and** execution
  (spec.md, D-104-5). Acceptance: **record**.
- [x] **T003 — Ledger intake and full registration.**
  The C104-1..C104-4 bundle intaken into the canonical
  ledger through `tools/ledger/import_bundle.py`; the
  taxonomy entry added (Program infrastructure /
  Governance, lifecycle & generated layers, per
  D-104-3); the settling chain refreshed in the
  standing order; the generated layers regenerated;
  census pins updated from the regenerated actuals.
  No recommendations-ledger row (D-104-4).
  Acceptance: **test** (the ledger gate and the
  program-map conformance checks pass on the landed
  tree). The intake figures stand in
  `records/registration-2026-11-25.md` as executed.

## Stage 1 — Execution (second landing, under the same owner commission)

- [ ] **T101 — Instance build and fidelity gate.**
  The score matrix recomputed from the freeze-pinned
  Spec 096 corpus by the E1 driver's own functions,
  development records only, and checked against the
  filed E1 run record before any solving. Claims:
  C104-1. Test: TC-104-02. A failure stops the
  execution under plan.md's stop rule.
- [ ] **T102 — Classical arms.** The EXACT arm
  certifies the real instance (exhaustive QUBO
  enumeration + ILP to zero MIP gap) and every
  synthetic size (ILP); the SA arm runs on every
  instance under the registered parameters, with the
  determinism check. Claims: C104-1, C104-2. Tests:
  TC-104-03, TC-104-04, TC-104-05.
- [ ] **T103 — Quantum arm attempt and outcome
  record.** The connector route re-probed once, the
  response filed; if it authenticates, QAOA runs as
  registered (spec.md §4), otherwise the arm closes
  NOT EXECUTED — ROUTE DEAD on the filed evidence.
  The outcome record filed in spec.md §6's vocabulary
  (V-104-A, V-104-B) with the per-size table and the
  raw solver outputs saved to a dated file. Claims:
  C104-2, C104-3, C104-4. Tests: TC-104-06,
  TC-104-07.
