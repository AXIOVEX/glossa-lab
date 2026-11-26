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

### 2026-11-26 - REM witness acquisition completed: all three tomes held

Acting on the owner's direction of 2026-11-26 (~02:24 ET), the Persée route was run through the tower-compute automation Brave browser. All three tome PDFs of the REM were downloaded free of charge through each document page's own PDF control and are held in the designated custody home (`~/.syncyard/worktrees/glossa/glossa-custody/spec103/`): Tome I (215,556,263 bytes, 714 pp., SHA-256 f20d9f95…), Tome II (174,384,353 bytes, 658 pp., SHA-256 55b13325…), Tome III (182,222,445 bytes, 712 pp., SHA-256 cc24ffe6…); page counts sum to the edition's stated 2,084. The platform's Altcha check passed invisibly in the genuine desktop session on fresh page loads (one scripted checkbox click on Tome II errored and was not repeated; a fresh load then passed unaided). The print-set purchase is no longer needed. The asoreyi check was not run and this study's outcome stands exactly as filed; a check against the held witness needs its own registration.

Rests on: `records/rem-witness-acquisition-record-2026-11-26.md` §8; the custody note at `~/.syncyard/worktrees/glossa/glossa-custody/spec103/CUSTODY.md`.

### 2026-11-26 - Stage 2 registered: witness completion for asoreyi

The owner commissioned the asoreyi witness check in the Glossa-Lab chat on 2026-11-26 (10:27 ET: "do 1-3. Lets put all focus on Meroitic", item 1), the REM witness having been acquired and held the same day. Stage 2 is registered before any extraction or classification runs: `records/stage-2-registration-2026-11-26.md` states the claim under test (C103-1 as it applies to asoreyi, the one form NOT CHECKED), the exact witness (the three custody tome PDFs by SHA-256), the corrected checker by hash, the six WITNESS UNAVAILABLE loci in scope (all in Sh. 9 and Sh. 16), the identification of all eight unwitnessed texts with their REM entries (Sh. 9 = REM 0376; Sh. 16 = REM 0383; Meroe 40 = REM 0440; F.O. 7 = REM 0557; F.O. 17 = REM 0567; F.O. 29 = REM 0579; F.O. 39 = REM 0589; B.O. 1 = REM 0591), the witness treatment (transliteration transcribed from the rendered page; the PDFs' OCR layer is a locating aid only, never the witness; the REM witness takes the expansion witness's role in the corrected aggregation), and the kill condition in spec.md §3.5's registered form. The registration also files a correction to the acquisition record's chapter map: the Faras and Buhen ostraca sit in Tome II ch. 6 (REM 0551–0597), not ch. 5 as the sommaire-based map suggested; entry-level identification governs. Test cases TC-103-11..TC-103-16 are added in the same landing. The owner's same order directs that transferable mechanism learnings for the Indus and Eteocypriot programs be filed explicitly; that is discharged by a mechanism note filed with the execution landing.

Rests on: `records/stage-2-registration-2026-11-26.md`; `test-cases.md` (TC-103-11..TC-103-16); `records/rem-witness-acquisition-record-2026-11-26.md` §8.

### 2026-11-26 - Stage 2 executed: the REM carries no transliteration witness for the eight texts; asoreyi remains NOT CHECKED on the new ground

Stage 2 was executed the day it was registered, under `records/stage-2-registration-2026-11-26.md` (registration commit `25cbf825`, PR #761). Custody verified: the three tome PDFs hash-match the registration. Control verified: the filed conformance-addendum script replayed untouched and regenerated its results byte-identical to the filed results (41 of 47 loci reproduced under the corrected checker; the filed script hardcodes its original clone's path, so the executor staged its two inputs at that path and removed the staging). Identification verified on the rendered pages for all eight texts (REM 0376 / 0383 / 0440 / 0557 / 0567 / 0579 / 0589 / 0591), with two annotations: REM 0440's chapter is ch. 5 (Inscriptions de Méroé), not ch. 4 as the registration's table labelled it, and each entry's plate page is now filed alongside its notice page. The execution's central finding: **none of the eight REM entries prints a transliteration of its inscription** — the entry form is a notice plus plates (a photograph and, where one exists, the original publication's hand copy or facsimile; for Sh. 9 and Sh. 16 the copies are Griffith 1911a's own, the publication the build's extraction derives from). There is therefore no REM token stream to transcribe, the REM verdict set for Sh. 9 and Sh. 16 is empty, and under the corrected checker all six open loci remain WITNESS UNAVAILABLE. The six-form table restates unchanged: CLAIM STANDS for soreyi, xolkete, pxolkete, xolkte, wisi; **asoreyi NOT CHECKED — INCOMPLETE COVERAGE**, now on the ground that the held edition of record carries no transliteration witness for the two Shablul texts. The kill check does not fire: no discrepancy is demonstrated, and the input-error explanation for asoreyi is neither confirmed nor retired. The REM route for these two texts is closed on the record; what would settle them (a separately registered sign-level re-reading, or a modern re-edition printing a transliteration) is named in the outcome record and not started. Spec 097's Stage 4.4 outcome stands unreopened (C103-4). The transfer-learnings mechanism note directed by the commissioning order is filed at `records/stage-2-mechanism-note-2026-11-26.md`.

Rests on: `records/stage-2-outcome-record-2026-11-26.md`; `records/stage-2-results-2026-11-26.json`; `records/stage-2-witness-data-2026-11-26.json`; `records/stage-2-execution-script.py`; `records/stage-2-mechanism-note-2026-11-26.md`.
