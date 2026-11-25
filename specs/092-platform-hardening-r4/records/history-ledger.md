# History ledger - Spec 092

Study: Feature Specification: Platform Hardening R4 — Credential Encryption at Rest, Verified Writes, and the Test-Harness Remainder

**BACKFILLED 2026-11-25** from the filed records of this spec package only (spec.md, the records folder, and the package's run index where present), under the owner's order of 2026-11-25 that every study carry a history ledger. Entries are in chronological order. Each entry states the event or decision as the cited record states it and names the record it rests on. Where the filed record does not say how something started or why a decision was made, the gap is marked GAP rather than filled. This ledger narrates the study; it changes no result, verdict, or standing.

## Entries

### 2026-11-05 - Spec 092 — Commission and grounding record (2026-11-05)

**Commission.** The owner commissioned the Audit R4 hardening spec from the decision queue presented in the Glossa-Lab chat on 2026-11-05 (item 15, "Commission the R4 hardening spec"; the recommendation was adopted as presented: commission, with the `.keys.json` encryption first). The bundle is the standing audit-R4 remainder: (a) encryption at rest for stored outbound service credentials; (b) a v

Rests on: `records/commission-and-grounding-2026-11-05.md`

### 2026-11-05 - T002 — AEE verification of the C092 bundle (2026-11-05)

The bundle was assessed with the same assessor, the same way, as Spec 089's T002: the pinned AEE in the CI-faithful venv (`glossa-ci`, aee 1.5.3), run from the package directory.

Rests on: `records/t002-note.md`

### 2026-11-06 - Ratification + adoption record — Spec 092 (ratified 2026-11-06; adoption executed 2026-11-10)

**Scope:** tasks.md Stage 0 adoption runs (T003–T004), executed on branch `adopt/092-r4` after the owner's block ratification. This record covers the ratification act, the AEE assessment at adoption, the program-map assignment, and the claims-ledger intake (T004) with its settling-chain refresh, the generated-layer regeneration, the index completion, and the gate profiles over the refreshed tree. 

Rests on: `records/ratification-2026-11-06.md`

### 2026-11-14 - Spec 092 Stage 1 — stage record (2026-11-14)

Stage 1 (credential encryption at rest) is complete: the code legs (T101–T103) landed in PR #569 (merge `3cb7382c`, CI 10/10, delivery-checker RESOLVED on the parent's own run), and the live leg (T104) was executed by the parent against the one production store the same day, after the merge. Claims discharged: C092-1..5 and the store leg of C092-7 (its library leg is Stage 2's, per the plan).

Rests on: `records/stage-1-record-2026-11-14.md`

### 2026-11-16 - Spec 092 — Stage 2 record (2026-11-16)

Stage 2 (T201, T202, T203) of `specs/092-platform-hardening-r4/`. Branch `spec/092-s2-verified-write` (the commissioning brief's name; the tasks.md stage header says `feat/092-s2-verified-write` — the brief governed, noted here as a deviation). Built and tested on the mini-server, the program's execution home since 2026-11-16, in a fresh full clone at HEAD `d94197cc` (= origin/main, the PR #571 me

Rests on: `records/stage-2-record-2026-11-16.md`

### 2026-11-19 - Amendment — run-defs v3: the tray teardown mechanism recorded (2026-11-19)

**Spec 092 lineage.** This record is the amendment act for the run definitions under D-092-3: it registers **run-defs v3**, propagated in this same landing to every registered copy (run-defs §9): `glossa-indus/ledger/RUN-DEFINITIONS.md`, the library's machine copy (`backend/glossa_lab/run_records.py`), and the gate's V11 copies (`backend/glossa_lab/ledger_gate.py`). Nothing else in the definitions

Rests on: `records/amendment-run-defs-v3-tray-teardown-mechanism-2026-11-19.md`

### 2026-11-19 - Spec 092 closeout record (T401) — 2026-11-19

Spec 092 (platform hardening R4) closes here. Per-claim dispositions C092-1..14 at stage-evidence strength, with stage and PR pointers; the standing gate profile restated verbatim from the gate's own output on the final tree; C092-14 verified by diff census over the spec's stage branches. Nothing below states a claim at more than the strength its stage earned.

Rests on: `records/closeout-record-2026-11-19.md`

### 2026-11-19 - Spec 092 Stage 3 record — suite determinism (2026-11-19)

Stage 3 of Spec 092 (platform hardening R4): the four suite-determinism legs. Each leg landed on its own PR against main, merged only on per-job CI green (10 jobs, read per job). The stage's evidence is stated per task; the closeout record carries the per-claim dispositions.

Rests on: `records/stage-3-record-2026-11-19.md`

### Closed (at backfill, 2026-11-25)

The closeout record of 2026-11-19 (T401) closes the study; the run-defs v3 tray-teardown amendment was recorded the same day.

Rests on: the latest records cited above, as filed in this package.
