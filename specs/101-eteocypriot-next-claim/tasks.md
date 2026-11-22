# Spec 101 — Tasks

## Stage 0 — Registration

- [x] **T001 — Package lands, claim frozen.** spec.md,
  claims.md, aee-claims.json, plan.md, tasks.md,
  test-cases.md and records/ committed as
  `specs/101-eteocypriot-next-claim/`; the claim, its
  preconditions (P-1..P-3), its success criteria, and
  its independence assessment frozen in spec.md §3.
  Acceptance: **test** (aee-claims.json parses;
  claims.md and aee-claims.json carry the same four
  claim ids in the same order; every claim has a
  falsifier and a does-not-establish line). *This does
  not establish:* that the study has run — Stage 0
  registers and freezes it.
- [x] **T002 — Owner act recorded.** The owner's OD-10
  act of 2026-11-22 12:23 ET (adjudication unit E-8:
  specify a realistic next Eteocypriot claim) is the
  adoption act of record, filed in
  `records/registration-2026-11-22.md`. Acceptance:
  **record**.
- [x] **T003 — Ledger intake and full registration.**
  The C101-1..C101-4 bundle intaken into the canonical
  ledger through `tools/ledger/import_bundle.py`; the
  taxonomy entry added (Program infrastructure /
  Governance, lifecycle & generated layers, per
  D-101-3); the settling chain refreshed in the
  standing order (verify-canonicals 6/6; the T405 pair
  re-executed, result blocks byte-equal; the
  comparison re-filed; sets re-materialized unchanged;
  the canonical pin refreshed as re_derivations[17];
  the superseded generation departed with its
  accounting); the generated layers regenerated;
  census pins updated from the regenerated actuals.
  Acceptance: **test** (the ledger gate and the
  program-map conformance checks pass on the landed
  tree). The intake figures stand in
  `records/registration-2026-11-22.md` as executed.

## Stage 1 — Intake — GATED (fresh owner commission)

- [ ] **T101 — Perna-side corpus state built.**
  Perna 2019's reading of ICS 194/195 intaken as a new
  corpus state with its C095-3 identity record
  (per-inscription pins, provenance, custody); the
  Spec 096 corpus hash verified unchanged before and
  after. Claims: C101-4. Test: TC-101-01.

## Stage 2 — Candidate registration — GATED

- [ ] **T201 — Candidates registered.** Recurring-ending
  candidates derived from the ICS 196 development set
  alone under spec §3.1 P-2's mechanical rule; the
  candidate set, predicted positions, and occurrence
  floors committed before any scoring load. Claims:
  C101-1. Test: TC-101-02.
- [ ] **T202 — Freeze addendum filed.** Every
  derivation, stem table, and sign table written in
  full; floors instantiated against the intaken
  census. Claims: C101-3. Tests: TC-101-05.

## Stage 3 — Scoring — GATED

- [ ] **T301 — The registered test scored.** Each
  candidate counted at its registered positions in
  the Perna-side state; the run executed twice with
  byte-identical outcomes and an independent recount.
  Claims: C101-1. Test: TC-101-03.

## Stage 4 — Outcome — GATED

- [ ] **T401 — Outcome record and adjudication
  package.** The outcome record carries the exposure
  statement verbatim and each candidate's count
  against its floor; the adjudication package is
  prepared for the owner's approval act if the
  outcome carries anything to adjudicate. Claims:
  C101-1, C101-2. Test: TC-101-04.
