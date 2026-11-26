# History ledger - Spec 103

Study: Spec 103 — Meroitic Source-Witness Check: the Stage 4.4 Candidate Loci against the Acquired Build's Witnesses

**BACKFILLED 2026-11-25** from the filed records of this spec package only (spec.md, the records folder, and the package's run index where present), under the owner's order of 2026-11-25 that every study carry a history ledger. Entries are in chronological order. Each entry states the event or decision as the cited record states it and names the record it rests on. Where the filed record does not say how something started or why a decision was made, the gap is marked GAP rather than filled. This ledger narrates the study; it changes no result, verdict, or standing.

## Entries

### 2026-11-23 - Spec 103 — Registration Record (2026-11-23)

**Commission.** Owner decision **OD-D-2**, decided by the owner, Tristen Pierson, on **2026-11-23 at ~17:14 ET**: the source-witness check proposed in Round D unit D-M-3 of the Co-scientist sweep adjudication (`specs/091-anchor-comparison-integrity/records/coscientist-sweep-adjudication-2026-11-23.md`, §4 and §7 addendum) is commissioned — registration and execution in one act, in two landings: th

Rests on: `records/registration-2026-11-23.md`

### 2026-11-23 - Spec 103 — Stage 1 Outcome Record (2026-11-23)

**Execution.** Stage 1 of Spec 103, executed 2026-11-23 under the OD-D-2 commission (registration PR #727, merge `9d1321c6`), on tower-compute in the fresh clone `~/.syncyard/worktrees/glossa/sw103-exec`, against the pinned acquired build (MikeKovetsky/ meroitic @ `145af0836c071e7c9796d37d4b36add00d347c8a`, checked out at `~/.syncyard/worktrees/glossa/kovetsky-src`). Executor: `records/stage-1-exe

Rests on: `records/stage-1-outcome-record-2026-11-23.md`

### Closed (at backfill, 2026-11-25)

Registered and executed in one commission in two landings on 2026-11-23; the Stage 1 outcome record closes the study (no DISCREPANCY and no UNCERTAIN classification at any witness-covered locus; one form, asoreyi, NOT CHECKED for incomplete witness coverage, as that record states).

Rests on: the latest records cited above, as filed in this package.

### 2026-11-25 - Round E conformance annotation (narrow reopening)

Round E of the Co-scientist loop (Meroitic session, unit E-M-1) found the executed checker deviates from spec §3.4 in two places (any-witness FAITHFUL; uncertainty erasure in expansion preprocessing), both reproduced at adjudication against the filed script. A conformance annotation was appended to the outcome record; ledger row D-M-3 stands reopened in the narrow scope of checker conformance only (carried as row E-M-1), with this study's outcome (CLAIM STANDS for the five witnessed forms; asoreyi NOT CHECKED) preserved. The conformance addendum (checker repair, regression tests, affected-case audit and replay on already-held witnesses) is recorded as the follow-on act.

Rests on: `records/stage-1-outcome-record-2026-11-23.md` (conformance annotation, 2026-11-25) and `specs/091-anchor-comparison-integrity/records/coscientist-sweep-adjudication-2026-11-25.md` §3.1.

### 2026-11-25 - Conformance addendum registered (Round E unit E-M-1)

The conformance addendum was registered before any revised execution ran: `records/conformance-addendum-registration-2026-11-25.md` states the scope (checker repair, regression tests, affected-case audit and replay on the already-held witnesses; no new acquisition, no split change) and, where the frozen tokenization and §3.4's classification definitions conflict, the adjudicated treatment the corrected implementation follows (token identity unchanged; uncertainty markup retained as a per-token flag; witness disagreement explicit in the aggregation, with the precedence stated in advance). Test cases TC-103-07..TC-103-10 were added to `test-cases.md` in the same registration landing. D-M-3's outcome and the six-form table stand under a preservation rail: if the replay evidence itself contradicted an outcome, the addendum would stop and report, not rewrite.

Rests on: `records/conformance-addendum-registration-2026-11-25.md`; `test-cases.md` (TC-103-07..TC-103-10).

### 2026-11-25 - Conformance addendum executed — replay verdict

The corrected checker (`records/conformance-addendum-script.py`; the filed Stage 1 script untouched, its functions re-implemented unchanged as the control) ran on tower-compute against the pinned build. Regression tests: 10, all PASS, both counterexamples exercised against both implementations (TC-103-07, TC-103-08). Replay (TC-103-09): Step 1 reproduces the filed basis and counts exactly; the control reproduces the filed classifications and verdicts at all 47 loci (14 counted, 33 near) with 0 mismatches; the corrected classifications are identical at every locus (diff 0). Audit bounds: 0 of the 14 counted loci carry a mixed filed witness-verdict set, so deviation 1 masked no actual disagreement in the executed payload; markup incidence across all 25 held-out witnesses is 0, so deviation 2's historical impact, indeterminate at adjudication, is bounded at zero within the held witnesses. Verdict (TC-103-10): the unchanged Step 4 machinery on the corrected classifications returns the filed six-form table exactly — CLAIM STANDS for soreyi, xolkete, pxolkete, xolkte, wisi; asoreyi NOT CHECKED — INCOMPLETE COVERAGE — so the study's outcome is preserved on replay evidence. Ledger row E-M-1 moves to done in the same landing. No standing, verdict, or tally moved.

Rests on: `records/conformance-addendum-outcome-2026-11-25.md`; `records/conformance-addendum-results-2026-11-25.json`; `records/conformance-addendum-tests.py`.

### Closed (2026-11-25, conformance addendum complete)

The study is closed again: Stage 1 executed 2026-11-23 (CLAIM STANDS for the five witnessed forms; asoreyi NOT CHECKED for incomplete witness coverage), and the checker-conformance scope of the Round E reopening is discharged by the addendum above. The eight unwitnessed held-out texts, and any acquisition toward a witness for them, remain outside this study, as registered.

Rests on: the latest records cited above, as filed in this package.

### 2026-11-26 - REM witness acquisition: channel verified, print purchase prepared

The owner approved the witness acquisition in the Glossa-Lab chat on 2026-11-26 ("For everything else, execute now to your recommendations", 01:54 ET). The modern REM edition was identified exactly: Leclant (dir.) et al., *Répertoire d'Épigraphie Méroïtique: Corpus des inscriptions publiées* (Académie des Inscriptions et Belles-Lettres, Paris, 2000; 3 volumes; ISBN 2-87754-113-4), whose chapter map covers all eight unwitnessed texts (the Karanog/Shablul chapter of Tome I carries Sh. 9 and Sh. 16). The edition's open-access deposit on Persée was verified to the exact issue and document identifiers for all three tomes, but automated PDF download is gated by the platform's Altcha bot protection (verified twice from tower-compute); bulk page-image harvesting was considered and not used, as defeating the platform's bot protection at scale is not a legitimate-channel acquisition. The print set (€124 via Peeters) is prepared to the point of purchase, with the payment checkout as its blocker (owner: the owner). Custody home designated at `~/.syncyard/worktrees/glossa/glossa-custody/spec103/`; nothing is held yet. The asoreyi check was not run; this study's outcome stands exactly as filed.

Rests on: `records/rem-witness-acquisition-record-2026-11-26.md`.
