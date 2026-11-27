# Spec 093 — Tasks

Acceptance modes per the Autonomous Execution Doctrine.
Each task's *this does not establish* line survives into
its stage record. T001 and T002 are drafting tasks, done
with this package; every later task waits on the owner's
block ratification (Stage 0, T003).

## Drafting (done with this package)

- [x] **T001 — Drafting.** This package (spec.md,
  claims.md, aee-claims.json, plan.md, tasks.md, the
  grounding record) drafted under the owner's commission
  of 2026-11-05 and opened as a draft PR. Acceptance:
  **test** (the draft PR exists and its files are the
  package). *This does not establish:* that the package's
  design is sound — only that it was drafted, grounded,
  and filed for ratification.
- [x] **T002 — AEE validation of the draft bundle.** The
  bundle was validated under the pinned AEE at drafting
  (`aee validate`); the invocation and verbatim reading
  are in `records/t002-note.md`. Acceptance: **test**.
  *This does not establish:* that the claims are true, or
  that an adoption-time `aee assess` will read as this
  draft's validation did — validation is a form check,
  and the adoption assessment is Stage 0's own act.

## Stage 0 — Ratification and adoption

- [x] **T003 — Ratification record and intake.** The
  owner's block act is recorded beside the package; the
  claims bundle is regenerated from claims.md by script,
  assessed under the pinned AEE (outcome recorded
  verbatim), and appended through the sanctioned intake;
  the spec directory receives its program-map assignment
  in the same landing; the gate runs before and after.
  Acceptance: **gate**. *This does not establish:* that
  the design is sound — only that it was ratified,
  recorded, and entered by the sanctioned path.

## Stage 1 — Inventory, normalization, join

- [x] **T101 — Census completion.** The grounding
  inventory is re-run against the repo at adoption state
  and amended for any source or field it missed (C093-2);
  the disjointness counts of C093-3 are re-counted on the
  pinned snapshot and stated in the stage record.
  Acceptance: **test** (every count recomputable from the
  pinned files). *This does not establish:* that the
  census's sources are all the culture-side data in the
  world — only completeness against the named sources. **Completion (2026-11-06):** census completed by `tools/spec093/stage1_census.py` over the pinned files; the grounding record is amended (A1–A7) in `records/t101-census-completion-2026-11-06.md`, where every count is stated.
- [x] **T102 — Material normalization register.** The
  material-class vocabulary and its mapping rules are
  filed; every distinct raw value in the pinned snapshot
  is dispositioned by rule (class, composite split,
  uncertainty handling, non-material exclusion), with the
  disposition counts stated. Acceptance: **test** (the
  register covers every distinct value; a raw value
  outside the register fails the check). *This does not
  establish:* that the classes are the right grain — only
  that the mapping is total, ruled, and frozen for the
  stages that consume it. **Completion (2026-11-06):** register v1 filed at `records/material-normalization-register-v1.json` (SHA-256 `fe8d4542…`) with its document; all 1,122 distinct values dispositioned (663 class, 370 composite, 15 alternatives, 49 non-material, 25 unmapped-named); the checker re-applies the rules from the artifact and passes (stage record).
- [x] **T103 — Join design, freeze, and precision audit.**
  The museum↔text join procedure is frozen; the
  hand-checked sample is drawn and checked; measured
  precision and the error census are recorded against the
  freeze's floor. Acceptance: **test** (sample,
  precision, and errors recomputable from the audit
  record). *This does not establish:* that the join is
  correct pair by pair — precision on the sample is the
  claim, and a join below its floor stops the material
  arm honestly (C093-8). **Completion (2026-11-06):** freeze v1 filed before the audit (`records/t103-join-freeze-v1.md`); audit by complete enumeration — K1 rejected (7 pairs, precision 0.000), K2 accepted (179 pairs, precision 1.000); join output at `records/t103-join-pairs-v1.jsonl`; audit record at `records/t103-join-audit-2026-11-06.md`. The material arm is not stopped.

## Stage 2 — Channel independence

- [x] **T201 — Channel definition.** The material-context
  projection is defined against G1 §2.1's state: the
  per-object tuple under Stage 1's vocabularies, the
  named population, and the bookkeeping feature set the
  prediction test may use, each stated so a second worker
  can implement from the definition alone. Acceptance:
  **human-as-oracle**. *This does not establish:* that
  the channel is independent — that is T202's question,
  and this task only makes it askable. **Completion (2026-11-19):** definition filed at `records/t201-channel-definition-2026-11-19.md`; populations P-seq 3,085 / P-site 966 / P-join 179 counted from the pinned files by `tools/spec093/stage2_counts.py` (output `records/t201-counts-2026-11-19.json`); bookkeeping set bounded to source system, sign-id scheme, rights status, crosswalk coverage.
- [x] **T202 — Freeze, administration, and standing.**
  The freeze is committed (fields, features, bars,
  controls, floors); the per-field prediction
  administration runs as Spec 089 runs; an independent
  auditor recomputes; C093-1's standing is recorded in
  §5's vocabulary with the per-field table. Acceptance:
  **human-as-oracle** (reviewer against freeze, runs,
  bar). *This does not establish:* that the surviving
  fields say anything about any reading — independence
  is about projections, and §5's vocabulary is the whole
  of what this task may conclude. **Completion (2026-11-19):** freeze v1 committed before any computation (`records/t202-freeze-v1.md`); site administered and NOT RECOVERED (κ 0.0297 against the 0.80 bar, controls valid); find context NOT YET (control battery's 99th-percentile κ 0.1322 at or above the 0.10 validity ceiling — the obstruction, named); material class, artifact type, and holding/provenance NOT ADMINISTERED at the freeze's floors, forcing counts stated. Independent audit verdict AGREE; C093-1's standing recorded as INDEPENDENT IN PART in `records/stage2-record-2026-11-19.md`, site the surviving field. **Successor (2026-11-19):** freeze v2 (`records/t202-findcontext-freeze-v2.md`, committed before any computation under it) repaired the evaluation design only — repeated stratified cross-validation in place of the single split, the bar and the control validity ceiling unmoved — and re-administered find context: independent audit AGREE, but the v2 control battery's 99th-percentile repeat-mean κ was 0.1106, still at or above the 0.10 validity ceiling, so the field's outcome remains NOT YET under freeze v2 §8 and v1's NOT YET stands; record at `records/stage2-findcontext-successor-record-2026-11-19.md`.

## Stage 3 — Comparanda register

- [x] **T301 — Register v1.** Entries seeded per D-093-7
  are committed, each carrying comparanda set,
  transmission mechanism with source, fixed window, and
  compared practice; the four-element check runs over the
  register. Acceptance: **gate**. *This does not
  establish:* that the seeded comparisons are the right
  ones — only that each was fixed, with its mechanism,
  before anything was computed under it. **Completion (2026-11-27):** register v1 filed at `records/comparanda-register-v1.md` (4 entries, CR-093-01..04; all 39 catalogue corpora accounted exactly once: 2 entered, 5 the subject corpus, 32 annexed as not entered for want of a mechanism of record); the four-element check (`tools/spec093/check_comparanda_register.py`) PASS; stage record at `records/stage3-record-2026-11-27.md`.

## Stage 4 — First computed passes

- [x] **T401 — Site pass.** Freeze, runs, controls,
  held-out arm as the counts allow, audit, outcome —
  per plan.md Stage 4(a). Acceptance: **test** (bar
  adjudged mechanically on audited runs). *This does not
  establish:* why any accepted regularity holds — the
  pass states a joint-distribution fact at channel
  strength (C093-7), and no cause, function, or reading
  may be read into it. **Completion (2026-11-27):**
  freeze v1 filed before any computation
  (`records/stage4-site-freeze-v1.md`); runs
  `study-20261127T095820Z-2c776c` (administration) and
  `study-20261127T095821Z-31eef3` (controls); independent
  audit AGREE; mechanical adjudication **NOT YET** —
  Q1 length fails clauses 1–3, Q2 sign choice meets
  clause 1 and fails the held-out clause 2; both
  pseudo-site controls behave; stage record at
  `records/stage4-record-2026-11-27.md` §2.
- [x] **T402 — Material pass (join-gated).** As T401,
  over the Stage 1 join's population, only if the join
  cleared its floor; otherwise the CANNOT BE
  ADMINISTERED record with the forcing counts is this
  task's deliverable. Acceptance: **test**. *This does
  not establish:* anything about material practice in
  the world if it stops — a stop is a finding about the
  record system, stated at its counts. **Completion
  (2026-11-27):** the join cleared its floor at Stage 1
  (precision 1.000 ≥ 0.90), and the freeze's §4
  administration rule was executed — the §2 counts
  recompute exactly (Steatite 176, Clay 1, Faience 1,
  1 empty sentinel, 179 total) and one class meets the
  floor of 10 where at least 2 are required: **CANNOT
  BE ADMINISTERED**, forcing counts on the face of
  `records/stage4-record-2026-11-27.md` §3.
- [x] **T403 — Contact-context administration.** The 14
  excavated seals and the Meluhha record administered
  as an evidence class under their Stage 3 entries'
  frozen expectations; the outcome states what the find
  contexts license and what they do not. Acceptance:
  **human-as-oracle**. *This does not establish:* a
  population claim of any kind — n=14 is an evidence
  class, and this task's record says so on its face.
  **Completion (2026-11-27):** freeze v1 filed before
  the administration (`records/stage4-contact-freeze-v1.md`,
  citing CR-093-01 and CR-093-02 only); expectations
  **E1–E4 all MET** (14/14 find periods, 12/14
  excavation spots; 11/14 outside the Indus region;
  11/14 inscription-bearing; Meluhha modal period
  Ur III with 1,155 in-window hits, filed aggregates
  agreeing); the freeze's two bounded licensed
  statements in force; machine record at
  `records/stage4-contact-counts-2026-11-27.json`;
  stage record at `records/stage4-record-2026-11-27.md`
  §4.

## Stage 5 — Machinery extension

- [x] **T501 — Matrix rows and map layer, generated.**
  The generators emit the material-context domain's
  matrix rows and the program map's material-context
  layer from the ledger family; no generated file is
  hand-edited. Acceptance: **gate** (regeneration
  reproduces the surfaces byte-for-byte from the
  ledger). *This does not establish:* that the layer's
  claims are true — only that the surface is the ledger,
  generated, citing ids. **Complete 2026-11-27** (Stage 5
  record): taxonomy amendment to program-map-taxonomy v2
  (new Material context domain; this study's assignment
  moved; same-motion copies and the conformance census
  pin moved with it); program map republished through
  the gated path; matrix republished byte-identical;
  gate full 32 PASS / 0 FAIL / 1 NOT-RUN, regen
  35 / 0 / 0; record at
  `records/stage5-record-2026-11-27.md`.
- [x] **T502 — Gate extension.** The ledger gate gains
  the culture-layer checks (citation existence, one-way
  flow, register-section counting support for Stage 6),
  with a seeded-violation proof that a bad citation
  fails. Acceptance: **test** (seeded violation fails;
  clean tree passes in both modes at the extended
  profile). *This does not establish:* that earlier
  layers' checks changed — the standing profile's
  existing counts are untouched, and the extension is
  additive. **Complete 2026-11-27** (Stage 5 record):
  gate class V12 landed with the three legs; the
  counting leg passes with the zero count on its face
  while the register carries no culture-side section
  (Stage 6 lands it); teeth battery
  test_spec093_stage5_gate_extension.py, ten tests,
  seeded violations failing each leg.

## Stage 6 — Gap register and closeout

- [x] **T601 — GR-093 entries and the completeness
  extension.** The culture-side entries (at least the
  five the plan names) are appended under the register's
  new section, each with its four elements (C093-12);
  the register's mechanical completeness checks are
  extended in the same landing to count the section.
  Acceptance: **gate**. *This does not establish:* that
  these are all the culture-side gaps there are — only
  that every entry carried is closable honestly.
  **Complete 2026-11-27** (Stage 6 outcome record): the
  GR-093 section is appended (7 entries, each with its
  four C093-12 elements); the gate's V12 counting leg
  counts the section in this same landing (7 entries
  counted, full gate PASS at the extended profile); one
  disclosed machinery fix in the same landing (entry
  headings count only at paragraph starts; regression
  test added). Record at
  `records/stage6-outcome-record-2026-11-27.md`.
- [ ] **T602 — Outcome record and VEXA report.** The
  closeout record states per stage what was
  administered, accepted, or stopped (with counts) and
  C093-1's standing as it finally stands; the outcome
  is reported to the VEXA chat in the record's own
  words, the send recorded. Acceptance: **test** (the
  recorded send matches the outcome record). *This does
  not establish:* the final word on the channel — later
  joins, later data, and the reader stand after it.
