# CHANGELOG — Indus preprint v12 (against v11)

**Base.** v12 is built from the v11 text in its credit-corrected form,
the version of record: Zenodo version DOI 10.5281/zenodo.24376384
(credit-corrected deposit, 2026-11-19). Base source SHA-256
`66097f071a970c01ed745863814287bdedd8fceb4b181007af51574bc5675d99`
(the credit-fixed source held in the program's credit-fix records,
`hidden_files/credit-fix-2026-11-19/`).

**Base discrepancy, disclosed.** The tip of branch
`preprint-v11-deposit` (commit
`3ba222066f980ae042d35cc01a04d17bf9445737`) carries the FIRST v11
deposit's text (its §6 names version DOI 10.5281/zenodo.24351957)
and does not contain the credit corrections. The diff between that
text and the credit-corrected source is exactly the credit fixes and
nothing else. v12 is therefore built from the credit-corrected
source, so the living source again matches the deposited line. The
credit corrections themselves (§2.1.1 Shakti corpus identification,
§3.10 CISI identification, §7 acknowledgment of William Miller Sr,
References 36–38) are v11 content, carried unchanged; they are not
v12 changes.

**Build.** LuaLaTeX (TeX Live 2026, VM toolchain), two passes, zero
errors, zero undefined references. 50 pages as amended (48 pages as
first built; v11 deposited build: 39 pages; credit-corrected v11
build: 40 pages).

**Identity of the v12 review build (as amended, 2026-11-22).**
- Source: `pierson_2026_indus_decipherment_preprint_v12.tex`,
  SHA-256 `13f4f23047c45c18f49ab3041c752d6a1d6dbf159906a4e626b04c332355dd17`.
  (As first built: `e2084881f1492365692c92c21b7ec1ed6a6005f9331cc21fef72bc69df4e48e2`.)
- PDF: `pierson_2026_indus_decipherment_preprint_v12.pdf`,
  SHA-256 `b4a965dcef44f5529c0ab4c1b447d59db6780f19aa3dc50945dc23bd6db19758`.
  (As first built: `f4e62eb814d2dc6be462c6a600d0dd1d9bd00f642b62b33c37dc4eb97785628e`.)
- The review PDF was compiled from a build copy differing from the
  source in exactly one string: the §6 placeholder
  `%%VERSION_DOI%%` rendered as "assigned at deposit" (a literal
  percent token comments out the rest of the §6 line in LaTeX — the
  same placeholder rendering defect the v11 version note discloses
  for the v11 freeze builds). At deposit, the pin procedure
  substitutes the assigned version DOI, per
  `v11_version_note_DEPOSIT.md`.
- Word count: the printed figure, 28,580, is the amended review
  build's measured fixed point (method: `pdftotext | wc -w`,
  rebuilt to the fixed point, per the v11 note's method; as first
  built: 27,337). The DOI pin at deposit
  changes the count by −2 ("assigned at deposit" is three tokens;
  the DOI is one); the figure is re-verified on the rebuilt deposit
  PDF at that step, per the v11 note's remaining-steps procedure.
  Note, for the record: v11's printed figure (22,051) measures
  22,206 against its own credit-corrected PDF by the same method —
  a pre-existing discrepancy of the credit-corrected deposit, not
  restated or repaired by v12.

## Substantive changes

1. **Version identification.** Version line and end matter read
   "Preprint v12" / "End of Preprint v12"; header comment rewritten
   to describe the v12 revision. (Version practice:
   `v11_version_note_DEPOSIT.md`.)

2. **Front note — new paragraph.** Announces the November 2026
   post-deposit audit cycle, states that §5 and Appendix D carry it,
   that the standings there supersede earlier versions' standings
   language, and that "supported" is no longer used of the 94.
   (Records: `coscientist-audit-94-adjudication-2026-11-21.md`;
   `standings-relabel-execution-2026-11-21.md`.)

3. **Abstract — new closing paragraph.** The external audit and its
   adjudicated verdict (a candid research-management register, not a
   calibrated scale of reading correctness; no correctness
   probability warranted for any reading); the E/I/R/P/U classes;
   the current partition 3 E + 65 I + 4 R + 3 P + 19 U = 94
   (as first built: 4 E + 65 I + 4 R + 3 P + 18 U; amended
   2026-11-22, see the amendment section below);
   "supported" retired; the two strikes (M202, M044); falsifiers
   filed for 93 of 94; the Indus script remains undeciphered.
   (Records: the audit adjudication; the standings supplement.)

4. **§5, audit paragraph — standings sentence replaced.** The
   October 2026 classes are now stated as the October audit's
   (historical) classes, followed by the November relabeling
   statement: the E/I/R/P/U class definitions in brief and the
   current partition. The revalidation narrative that follows
   (37 → 33 retested: 28 battery + 5 site-statistics; the 4
   remaining R readings M087, M165, M264, M311) is unchanged.
   (Records: `standings-supplement-2026-11-21.md`;
   `standings-relabel-execution-2026-11-21.md`.)

5. **§5 — the "71 of the 94 as supported at all" sentence
   replaced.** Replaced by the retired-vocabulary statement: the
   class letters are the whole of what is claimed; E and I are never
   summed as supported; current standings; two of the six October
   outside claims struck on re-verification.
   (Record: `adjudication-supplement-2026-11-21.md`, which retires
   "supported" for the 94.)

6. **§5, identifiability paragraph — attribution and closing
   sentences.** "The six readings credited as independently
   supported" is now "the six readings the October audit classed as
   independently supported"; the paragraph now closes by recording
   that two of the six (M202, M044) have had their outside claims
   struck and stand in class U, the other four in class E, all six
   remaining NOT IDENTIFIABLE.
   (Records: `standings-relabel-execution-2026-11-21.md` §4;
   `m044-addendum-adjudication-2026-11-21.md`.)

7. **§6 — version sentence.** Now reads as the v12 text with the
   `%%VERSION_DOI%%` placeholder, prepared from the deposited v11
   text in its credit-corrected form (10.5281/zenodo.24376384),
   identified by `v12_version_note_DEPOSIT.md`. One disclosed
   deviation from v11's §6 form: v11's §6 named its freeze commit;
   v12's §6 defers the freeze-commit string to the version note,
   which records it at deposit (the freeze and pin commits are
   created by the deposit pin procedure, which has not run).
   (Record: the pin procedure in `v11_version_note_DEPOSIT.md`.)

8. **New Appendix D — "Post-Deposit Audit Cycle (November 2026)".**
   Twelve subsections, each stated as its landed record states it:
   - **D.1** The external audit of the 94 and its adjudication:
     summaries-only scope; 121 units (118 APPLY / 2 APPLY WITH
     MODIFICATION / 0 DO NOT APPLY / 1 blocked, since discharged);
     the overall verdict; the audit's honest public formulation
     quoted verbatim with its audit-time counts, followed by the
     current counts; Q4 sourcing flags (75 S + 13 N + 5 M + 1 A);
     the Q5 ranking in brief.
     (`coscientist-audit-94-adjudication-2026-11-21.md`.)
   - **D.2** The relabeled standings: class definitions as landed;
     the partition with the E, R and P membership; "supported"
     retired; E and I never summed.
     (`standings-supplement-2026-11-21.md`;
     `standings-relabel-execution-2026-11-21.md`.)
   - **D.3** The addendum rule and the two strikes: the rule as
     landed (contradiction strikes; partial verification and
     non-verifiability do not); M202 (Mahadevan 2009 read in full,
     claim not in the source, no remaining basis → U); M044 (DEDR
     1638 = kucukucu in the restored tree; the multi-leg
     interpretation stated expressly as an interpretation; the
     symmetry clause).
     (`standings-relabel-execution-2026-11-21.md` §4;
     `m044-addendum-adjudication-2026-11-21.md`, with its Round 3
     amendment on the M329 distinction.)
   - **D.4** Re-verification of the outside claims: the pass, its
     instruments and its four outcome labels; M047 VERIFIED AS
     FILED (provenance only, class-level proposal, the crosswalk
     step the program's own); M124 PARTIALLY VERIFIED (DEDR leg
     only, 2nd ed. p. 151); M329 PARTIALLY VERIFIED (DEDR leg
     only, 2nd ed. p. 404; the Sanskrit pura leg fails; the
     tree/print numbering divergence at entry 4524 unresolved);
     M330 NOT VERIFIABLE with the negative finding and the OCR
     caveat; M202 CONTRADICTED; M044 NOT VERIFIABLE at the pass.
     (`external-support-reverification-2026-11-21.md`.)
   - **D.5** The definition question (flag F-9) and its adopted
     resolution path: the register-level vs derivation-level
     question stated with M047's log position; the owner's
     adoption (2026-11-22) of the itemization test prospectively;
     the directed M047 Parpola §10.1 itemization re-examination,
     stated as in progress with its outcome to be reported — **no
     result is pre-stated** (the re-examination was executed and
     its outcome is carried by the 2026-11-22 amendment below,
     which rewrites D.5); M330's second-exposure position
     (survives the itemization test; would fall only under a finer
     rule requiring partial verifiability, not adopted).
     (Records: the Round 4 red-team adjudication, flag F-9; the
     Round 5 report's M330 sharpening; the owner's adoption in
     chat, 2026-11-22.)
   - **D.6** Motif and numerical evidence: all 13 animal-motif
     claims NOT REPRODUCIBLE FROM THE RECORDS, with the reason
     (the Holdat iconography CSV gitignored and unheld; no tracked
     per-seal sign-to-motif join over the 1,670-seal population;
     sign-side marginals replicated exactly by two independent
     paths); the eleven annotated motif-motivated rows named; the
     deposit gated on Miller's outstanding permission; all 3
     numerical claims WEAKENED with the counts (NUMERAL_FORMULA
     1/141, 1/210, 2/187; M012 short-inscription share 30.5% vs
     the 35.9% population baseline; M391 SUFFIX_ONLY 74/187).
     (`motif-numerical-evidence-2026-11-21.md`.)
   - **D.7** Dependency-aware reruns: Tranche 1 REPRODUCE EXACTLY
     (M342 n = 584, terminal 70, 12.0%, p = 0.0656; M176 68/356,
     19.1%, p = 0.0626; both remain U); Tranche 2 (collocations
     verified at n = 4 for M005→M342, M030→M342, M037→M267 as
     co-occurrences with the named signs; single-source only for
     M068, M075; M089's counts internally inconsistent; M347's
     residue; M375's translated pattern deleted; M267 NOT
     EXECUTABLE AS SPECIFIED, the 4.3× and z = 8.038 figures
     withdrawn); Tranche 3 (M063's motif claim FAILS as specified,
     lift 4.35 < 5.0, exclusivity also fails, the both-ways note
     on the historical motif table).
     (`q5-reruns-tranche1-2026-11-21.md`;
     `q5-reruns-tranche2-2026-11-21.md`;
     `q5-reruns-tranche3-2026-11-21.md`.)
   - **D.8** Per-reading falsifiers: filed for 93 of 94; M099
     flagged as too thin to draft one; M099's value recorded as not
     load-bearing.
     (`per-reading-falsifiers-2026-11-21.md`.)
   - **D.9** Spec 098 Stage 1: the frozen bar stated as frozen
     (penalized margin ≥ 10 nats AND above the permutation null's
     99th percentile; penalty 2 nats per free choice); T101 — the
     genuine-holdout subset is empty, every sign's ceiling
     DISCRIMINATED ON PSEUDO-HELD-OUT; T102 (M044 one attestation,
     zero canonical-field tokens; M374 unattested, UNDECIDABLE AT
     THIS POWER, unscored); T103 (population 70 at execution, 21
     of 70 meeting the 5-token floor in expectation, 49 below;
     population now 69 after M044, no Stage 1 result changes);
     T104 (seal struck: 2,413 clusters, 517 held out, custody
     outside the repository, released exactly once at Stage 3);
     Stage 2 commissioned 2026-11-22, not yet run at writing
     (executed 2026-11-22; its outcome is carried by the amendment
     below, which extends D.9).
     (Records: the Spec 098 Stage 1 records — provenance,
     grapheme-gap resolution, population annex, execution freeze
     annex, seal record.)
   - **D.10** Spec 099 and the Q3 graph audit: the log census as
     rebuilt, 296 items (210 primary / 61 other-reading or
     candidate-system / 25 ambiguous), with the rebuild reason
     (three DEDR double-citations merged); the honest citation
     form quoted verbatim, including the class-E structural
     qualification and the M047 scope note; 44 of 94 bases weakened
     (63 counting ambiguous premises); the graph acyclic; the
     most-depended-on counts (M342 10, M267 6, M176 6); the named
     targets and open ends (23 items, 34 targets, 31 inside the
     94; 38 open ends); the M267 dependency statement in brief.
     (Records: `spec099` stage-1 execution record as amended;
     `q3-graph-audit-completion-2026-11-21.md`;
     `dependency-record-2026-11-21.md`.)
   - **D.11** Expert engagement, Stage 4 state: the 2026-11-19
     letters; Chevillard declined (2026-11-20) and thanked;
     Kobayashi and Kolichala engaged as replacement coders
     (2026-11-20); Kobayashi's two replies (the fuller blinding
     description sent 2026-11-21; his second reply the same day —
     hospitalized, time short, the packet invited); the 9-entry
     blind packet and no-pressure cover sent 2026-11-21, his
     decision on his own time; Kolichala, Kenoyer, Wells and Mitra
     not replied; the record's plain statement that no coding
     product has been received.
     (Records: `stage-4-status-record-2026-11-21.md` with its
     Round 2 supplement; `t401-coder-engagement-record-2026-11-20.md`.)
   - **D.12** Exposure: the four points of the red team's F-15
     finding, in the finding's order, with their register
     pointers. **Flag:** F-15 exists as a recommended change /
     specification in the delegated-package red-team record
     (`hidden_files/delegated-package-2026-11-20/red-team.md`),
     not as pre-written paper text; D.12 was written to that
     specification. The four points: (1) the Dravidian premise
     assumed, not tested, over the strict core under equal
     budgets; (2) sign-inventory dependence on the Mahadevan frame
     (Spec 077: 527–584; GR-088-28 unruled); (3) the corpus
     provenance chain ("NOT PINNABLE" in November 2026; the only
     copy fleet-wide located in a VM custody-search directory;
     GR-088-08/10 open; capped at "internally documented");
     (4) the 605 → 287 → 161 → 94 lineage and the "shrinking
     claims" narrative.

## Pre-deposit amendment (2026-11-22)

The owner approved v12 for deposit on 2026-11-22 "as long as we
have all things resolved prior to deposit". Four items resolved
after the build; this amendment carries their outcomes, and a
fifth (item E, the M048 re-adjudication) resolved after the
amendment was drafted and is carried before deposit. Every
partition surface in the paper (abstract, §5, Appendix D.2) now
agrees at **3 E + 66 I + 4 R + 3 P + 18 U = 94**.

A. **The F-9 outcome — M047 reclassed E → U.** Appendix D.5 is
   rewritten ("The Itemization Test and the Reclassification of
   M047"): the adopted test stated prospectively; the directed
   re-examination's determination (M047's filed basis states no
   published proposal of the reading; the Parpola name is the
   crosswalk's catalogue sourcing; the crosswalk's phoneme field
   is the program's own curation, per-entry unattributed; the
   basis truncates and cannot be completed by inference); no
   internal candidate motivation remains, so M047 takes class U;
   Arm E is M124, M329, M330; the reopen clause for production of
   the untruncated basis is carried. The abstract, §5 and D.2
   partitions and the §5 identifiability paragraph's closing
   sentences are corrected to the three-E position.
   (Record: `specs/091-anchor-comparison-integrity/records/f9-itemization-adjudication-2026-11-22.md`;
   PRs #663, #668.)

B. **Spec 098 Stage 2 executed.** Appendix D.9 (retitled "Stages
   1 and 2") now carries the executed outcome: population 69 as
   executed (the standings at the execution commit, before the
   F-9 act; M047 a member as class E as its entry then stood);
   48 UNDECIDABLE AT THIS POWER; 17 NOT IDENTIFIABLE by
   construction; 4 PROCEED TO STAGE 3 (M267, M347, M375, M089);
   0 DISCRIMINATED; margins and permutation-null percentiles not
   computed by design (Stage 3 quantities); the seal stays
   sealed; the population for any future stage is 69 after the
   F-9 act and the M048 re-adjudication (item E below), the
   count matching Stage 2's executed population by coincidence
   of count only; Stage 3 is not commissioned.
   (Record: the Spec 098 Stage 2 outcome record,
   `stage-2-outcome-2026-11-22.md`; PRs #664, #666, #667.)

C. **The F-4 study package.** (Records: PRs #665, #669, #670.)
   - *M267 dependency-aware retest* — a new passage in Appendix
     D.7, and D.10's "no such retest has been run" corrected:
     verdict GENITIVE_MARGINAL, not promoted; the slot-pattern
     statistic excluded as confirmation per the dependency
     statement (the markers' readings are not independently
     justified); the uninterpreted recompute supports a medial
     particle statement only; the DEDR 494 leg fails as filed
     (entry 494 = Ta. il "house"; the claimed word is not a DEDR
     headword); the from-raw permutation null not recomputed
     (the pinned Holdat corpus is not held on the execution
     venue; the gap is named; the withdrawn figures are not
     revived). The tranche-2 NOT EXECUTABLE AS SPECIFIED framing
     stands as that rerun's history; it is not erased.
     (`m267-dependency-aware-retest-2026-11-22.md`.)
   - *DEDR digital-edition pass* — Appendix D.4's M329 item
     corrected: no tree-vs-print divergence; poṉ is entry
     **4570** in print and tree alike (print 4524 = tree 4524,
     bobbaḍe "rind, bark"); the filed 4524 citation was the
     program's error; the "numbering divergence unresolved"
     framing is removed. Appendix D.3's M044 symmetry clause is
     closed on the same pass: print 1638 = tree 1638 (kucukucu),
     the clause is NOT triggered, and the M044 strike stands
     unreopened. (`dedr-digital-edition-pass-2026-11-22.md`.)
   - *M048's corrected battery result* — a new passage in
     Appendix D.7: score 2 (positional PASS, DEDR PASS, bigram
     NOT_RUN — corpus not held on the venue), promotion
     threshold MET; the class re-adjudication it triggers is a
     separate act, performed the same day and carried as
     item E below. (`m048-corrected-battery-result-2026-11-22.md`.)
   - *Meroitic items NOT carried:* the 662-count reproduction
     (reproduces exactly) and freeze v3 are Meroitic-program
     results; the Indus paper's text does not touch them, and no
     Meroitic material was added to it.

D. **Mechanics.** Printed word count re-measured to the fixed
   point: **28,765** (placeholder mechanics as disclosed above;
   expected 28,763 after the deposit DOI pin). Recompiled two
   passes, zero errors, zero undefined references; **50 pages**.
   Page 1 and the Appendix D opening page rendered and read.

E. **The M048 re-adjudication — M048 reclassed U → I.**
   (Executed 2026-11-22 on the owner's commission, after item C
   was carried; the deposit was gated on this act.) The
   re-adjudication the corrected battery result triggered under
   RT2-08 was performed: M048's class U had rested on the
   absence of a qualifying filed corrected-battery result, and
   that ground no longer holds; on the parity the register set
   up with M089 (class I on a filed score of 2), M048 takes
   class I. Appendix D.7's M048 passage now states the act, its
   ground, and its reopen clause; D.2 records the move; the
   standings of record become **3 E + 66 I + 4 R + 3 P + 18 U =
   94** on every current partition surface (abstract, §5, D.2);
   D.9's future-stage population is corrected to 69 (66 I +
   3 E). Appendix D.5's executed-partition sentence stands as
   the F-9 act's own outcome, exactly as that act's record
   states it. The act does not establish the reading mu/muṉ,
   executes no further leg, corrects no counts, and does not
   speak to M367.
   (Record: `specs/091-anchor-comparison-integrity/records/m048-readjudication-2026-11-22.md`.)

## What was NOT changed

- §§1–4, the §3 study reports, Appendices A–C, the bibliography,
  and every reading, value, and number outside the items listed
  above stand as in the credit-corrected v11.
- §3.32 remains absent; the Roif gate stands (§3.5's withheld-study
  paragraph unchanged).
- No standing was moved by this version: the standings it reports
  are the record's standings of 2026-11-22 as amended the same
  day — the F-9 act (M047 → U) is reported in D.5 as executed,
  and the M048 re-adjudication (M048 → I) is reported in D.7 as
  executed.

## Status

Deposit-ready draft. **Not deposited.** Deposit follows the
standing order — the owner's approval of the actual text, then
Zenodo first, then the other venues — and the pin procedure in
`v12_version_note_DEPOSIT.md`.
