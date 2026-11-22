# Spec 100 — Tasks

## Stage 0 — Registration

- [x] **T001 — Package lands, design frozen.** spec.md,
  claims.md, aee-claims.json, plan.md, tasks.md,
  test-cases.md, tools/, tests/ and records/ committed as
  `specs/100-motif-claims-rerun/`; the design frozen in
  `records/preregistration-2026-11-22.md` (the 13 claims
  and their filed motifs and threshold, the frozen
  definitions, the gate statement). Acceptance: **test**
  (aee-claims.json parses; claims.md and aee-claims.json
  carry the same seven claim ids in the same order; every
  claim has a falsifier and a does-not-establish line).
  *This does not establish:* that the study has run —
  Stage 0 registers and freezes it.
- [x] **T002 — Test cases executed.** TC-100-01..
  TC-100-06 run on tower-compute against the pipeline of
  record; payload verdicts (the test process's own exit
  code and output) recorded in
  `records/tc-execution-2026-11-22.md`. Acceptance:
  **test**.
- [x] **T003 — Proof run in custody.** The pipeline's
  proof mode executed end to end on tower-compute over
  synthetic labels keyed to the real population (join,
  both paths, cells, lifts, odds ratios, verdicts), plus
  a record-mode invocation without a deposit confirming
  the GATE CLOSED refusal; payload verdicts recorded in
  `records/tc-execution-2026-11-22.md`. No real label was
  read; no output of the proof is a result. Acceptance:
  **test**. Claims: C100-1, C100-7.
- [x] **T004 — Owner act recorded.** The owner's OD-5 act
  of 2026-11-22 11:36 ET (rerun authorised; deposit held
  until Miller's reply) and this package's assignment to
  adjudication unit I-21 are the adoption act of record,
  filed in `records/adoption-and-registration-2026-11-22.md`.
  Acceptance: **record**.
- [x] **T005 — Ledger intake and full registration.** The
  C100-1..C100-7 bundle intaken into the canonical ledger
  through `tools/ledger/import_bundle.py`; the taxonomy
  entry added (Anchors & readings / Validation batteries
  for the SA-lineage anchors); the settling chain
  refreshed in the standing order (verify-canonicals 6/6;
  the T405 pair re-executed, result blocks byte-equal;
  the comparison re-filed; sets re-materialized unchanged;
  the canonical pin refreshed as re_derivations[16]; the
  superseded generation departed with its accounting);
  the generated layers regenerated; census pins updated
  from the regenerated actuals. Acceptance: **test** (the
  ledger gate and the program-map conformance checks pass
  on the landed tree).

## Stage 1 — The deposit — GATED (spec section 4)

- [ ] **T101 — Deposit produced and landed.** The pinned
  corpus bytes produced in custody and their full SHA-256
  verified against the pin of record;
  `tools/deposit_extract.py` run; the deposit CSV and its
  deposit record (provenance, permission basis, coverage,
  join-defect check) landed by pull request. Claims:
  C100-1, C100-5, C100-6. *Gate: Miller's granting reply
  on record (F-1). A pin that does not verify stops this
  task and is recorded.*
- [ ] **T102 — Coverage verification.** The deposit's
  coverage read back from the landed record: rows against
  the 1,670-seal population, missing seals enumerated by
  count, out-of-population rows zero. Acceptance:
  **test**. Claims: C100-3, C100-5.

## Stage 2 — The rerun — GATED on Stage 1

- [ ] **T201 — Record-mode run.** `tools/motif_rerun.py`
  run in record mode against the landed deposit on
  tower-compute in a fresh clone; the run's exit code is
  its payload verdict; both paths' agreement or the
  disagreement recorded. Claims: C100-2, C100-3.
- [ ] **T202 — Outcome record landed.** Full tables for
  all 13 claims (cells, lift, odds ratio, verdict), the
  labeled-population denominator on its face, M063's
  filed 4.35 carried beside its recomputed row, landed
  by pull request. Acceptance: **record**. Claims:
  C100-2, C100-4.

## Closure without execution

- [ ] **T901 — GATE REFUSED closure (only on a refusal
  reply).** A closure record under this spec recording
  the refusal and the study's unexecuted state; Stages
  1–2 are struck as not run. Claim: C100-6.
