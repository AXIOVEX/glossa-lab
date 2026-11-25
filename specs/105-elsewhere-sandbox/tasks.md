# Spec 105 — Tasks

## Stage 0 — Registration

- [x] **T001 — Package lands, sandbox frozen.**
  spec.md, claims.md, aee-claims.json, plan.md,
  tasks.md, test-cases.md and records/ committed as
  `specs/105-elsewhere-sandbox/`; the primitives
  census (spec.md §2), the three build procedures
  with their pins, strip rules, exclusions, and
  partitions (§3), the derivation ladder (§5), the
  boundary gates (§7), and the Stage 1 outcome
  vocabulary (§6) frozen. Acceptance: **test**
  (TC-105-01: aee-claims.json parses; claims.md and
  aee-claims.json carry the same five claim ids in
  the same order; every claim has a falsifier and a
  does-not-establish line). *This does not
  establish:* that any sandbox has been built — Stage
  0 registers and freezes the study.
- [x] **T002 — Owner act recorded.** The owner's
  order of 2026-11-25 (Glossa-Lab chat: the
  ELSEWHERE direction quoted in spec.md's status
  block, given after he set the Spec 104 quantum arm
  aside) is the adoption act of record, filed in
  `records/registration-2026-11-25.md`. The act
  commissions registration **and** Stage 1 execution
  (spec.md, D-105-4); L2 and above and all gates are
  not commissioned. Acceptance: **record**.
- [x] **T003 — Ledger intake and full registration.**
  The C105-1..C105-5 bundle intaken into the
  canonical ledger through
  `tools/ledger/import_bundle.py`; the taxonomy entry
  added (Sign inventory & corpus / Signary & corpus
  models, per D-105-2); the settling chain refreshed
  in the standing order; the generated layers
  regenerated; census pins updated from the
  regenerated actuals. No recommendations-ledger row
  (D-105-3). Acceptance: **test** (the ledger gate
  and the program-map conformance checks pass on the
  landed tree). The intake figures stand in
  `records/registration-2026-11-25.md` as executed.

## Stage 1 — Execution (second landing, under the same owner commission)

- [ ] **T101 — Builds.** Per sandbox: the source pin
  verified; the dataset built by the registered
  strip rule (spec.md §3) into custody on
  tower-compute, its SHA-256 and the
  position-to-source mapping filed in the build
  record; the Indus reserve built and sealed by its
  hash. Claims: C105-1, C105-2, C105-4. Tests:
  TC-105-02, TC-105-03, TC-105-04. A pin or census
  failure stops that sandbox under plan.md's stop
  rule.
- [ ] **T102 — L0–L1 derivations.** Per sandbox: the
  L0 census as recorded and the L1 derived inventory
  produced from the derivation dataset only, under
  two independently written implementations that
  must agree exactly; the inventories filed in the
  outcome record beside, never merged into, the
  working sign lists. Claims: C105-3, C105-4, C105-5.
  Tests: TC-105-05, TC-105-06, TC-105-07.
- [ ] **T103 — Outcome record.** The Stage 1 outcome
  record filed in `records/` returning, per sandbox,
  COMPLETED or STOPPED exactly as registered
  (spec.md §6), with the source pins as verified,
  the dataset hashes, the recorded censuses as
  reproduced, the derived inventories, and the raw
  outputs saved to a dated file in the same landing.
  Claims: C105-2, C105-3, C105-4, C105-5. Tests:
  TC-105-02..TC-105-07 as they apply.
