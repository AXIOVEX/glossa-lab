# Spec 103 — Conformance Addendum Outcome Record (2026-11-25)

**Execution.** The conformance addendum commissioned by
Round E unit E-M-1, executed 2026-11-25 under its
registration (`records/conformance-addendum-registration-2026-11-25.md`,
committed on this branch before any revised execution
ran), on tower-compute in the fresh clone
`~/.syncyard/worktrees/glossa/sw103-addendum`, against
the pinned acquired build (MikeKovetsky/meroitic @
`145af0836c071e7c9796d37d4b36add00d347c8a`, unchanged at
`~/.syncyard/worktrees/glossa/kovetsky-src`). Executor:
`records/conformance-addendum-script.py`; regression
tests: `records/conformance-addendum-tests.py`; full
machine results: `records/conformance-addendum-results-2026-11-25.json`.
The filed Stage 1 script and the Stage 1 outcome record
are not edited; the filed script's classification
functions are re-implemented in the addendum script
unchanged, as the control. No new witness was acquired;
no split changed; no Otten material was an input.

## 1. The repairs

Both deviations named in the conformance annotation are
repaired in the corrected checker, implementing the
adjudicated treatment stated in the registration record:

1. **Witness aggregation.** A counted locus is FAITHFUL
   only when every available witness attests the form
   (or its spelling variant) without qualification. An
   unqualified attestation coexisting with an unqualified
   absence is DISCREPANCY — disagreement is explicit, and
   there is no any-witness pass. The filed all-absent rule
   (DISCREPANCY when the expansion witness is among the
   absent; otherwise UNCERTAIN) is retained. The
   near-locus aggregation is corrected in the same sense:
   a missed count requires the expansion witness's
   unqualified attestation, or an unqualified attestation
   no witness contradicts by carrying the near token;
   witness disagreement at a near locus is UNCERTAIN.
2. **Uncertainty retention.** Token identity is the
   frozen tokenization's unchanged; alongside it, each
   witness token now carries an uncertainty flag — for an
   expansion record, when a character of the filed markup
   set stood immediately adjacent to the token's span in
   the folded record text (so `[soreyi?]` yields the token
   `soreyi`, flagged); for an open alternative reading,
   when the token chunk contained any of `[`, `]`, `?`,
   `!`. An attestation resting only on flagged tokens is
   an uncertain attestation (`attests_form_uncertain` /
   `attests_variant_uncertain`) and classifies its locus
   UNCERTAIN unless a discrepancy is established.

## 2. Regression tests (TC-103-07, TC-103-08)

`records/conformance-addendum-tests.py`: 10 tests, all
PASS on tower-compute (run 2026-11-25, output in the
execution transcript of this landing). Both
counterexamples are exercised against both
implementations: witnesses {`soreyi`, `ato`} classify
FAITHFUL under the filed control (the deviation, as
filed) and DISCREPANCY under the corrected code;
`[soreyi?]` tokenizes to an unqualified exact match
under the filed control and to a flagged token with
verdict `attests_form_uncertain` and locus classification
UNCERTAIN under the corrected code. The preserved
behaviours are asserted for both implementations:
unanimous attestation → FAITHFUL; variant attestation →
FAITHFUL (variant noted); all-absent with the expansion
witness → DISCREPANCY; all-absent from alternative
readings only → UNCERTAIN; no witnesses → WITNESS
UNAVAILABLE; near-locus missed count → DISCREPANCY
(missed count); near-locus distinct form → FAITHFUL
(source carries the distinct near form). One test
expectation was corrected during the run and is recorded
here rather than smoothed over: an intra-token bracketed
token (`so[re]yi`) fragments under the filed
preprocessing into three tokens (`so`, `re`, `yi`), not
two; all three fragments carry the flag, which is what
the corrected test asserts.

## 3. Replay (TC-103-09)

- **Step 1 reproduces exactly.** The corrected script's
  basis, per-form counts, anchor controls, strata, and
  witness coverage equal the filed Stage 1 record field
  for field (`step1_matches_filed: true` in the results
  file). TC-103-02 re-run: PASS.
- **The control is faithful.** The re-implemented filed
  rules reproduce the filed Stage 1 classifications and
  witness verdicts at every locus — 14 counted loci and
  33 near-form loci, 0 mismatches. The replay machinery
  is therefore proven against the filed record before
  any corrected figure is read from it.
- **The corrected classifications are identical at every
  locus.** The per-locus diff between the filed and
  corrected classifications is empty (0 of 47 loci).
  Per form, the corrected classifications are the filed
  ones: soreyi 9 FAITHFUL + 1 WITNESS UNAVAILABLE counted,
  2 FAITHFUL + 1 UNAVAILABLE near; asoreyi 1 + 1 counted,
  10 + 1 near; xolkete 1 counted, 2 near; pxolkete 0
  counted, 3 near; xolkte 1 counted, 2 near; wisi 0
  counted, 10 FAITHFUL + 2 UNAVAILABLE near.

## 4. The audit bounds (the addendum's new evidence)

- **Deviation 1 never fired on a disagreeing locus.**
  Mechanically recounted over the executed payload: 0 of
  the 14 counted loci carry a mixed filed witness-verdict
  set. The any-witness pass therefore masked no actual
  disagreement in the Stage 1 execution — the
  adjudication's scan, now confirmed by the replay
  control.
- **Deviation 2's historical impact is bounded at zero.**
  At adjudication this was indeterminate from the filed
  aggregate, which does not preserve raw uncertainty
  markup. The audit scans the raw text of every witness
  the check holds for the held-out partition — 25 witness
  objects (the expansion records and open alternative
  readings behind the 25 witnessed held-out texts) — for
  any character of the filed markup set. Incidence: **0**.
  No held witness carries markup at all, so no historical
  classification rested on a token whose uncertainty
  markup was erased. The bound is exact within the held
  witnesses, which are the only witnesses the check has
  ever used; it says nothing about witnesses the program
  does not hold (the eight unwitnessed texts, Sh. 9 and
  Sh. 16 among them, are untouched by this addendum, as
  registered).
- Four near-form loci carry a `partial_or_containment`
  corrected verdict (soreyi and asoreyi at REM 0056,
  token `reyi`; xolkete at REM 0240, token `psxolkete`;
  xolkte at REM 0092, token `kte`). That verdict class is
  a by-product of the containment relation — the witness
  carries the near token itself — and each of the four
  classifications rests on the near token's unqualified
  presence, so all four stand FAITHFUL under both
  implementations, as filed.

## 5. Outcome preservation (TC-103-10)

The unchanged Step 4 machinery, applied to the corrected
classifications, returns the filed six-form table
exactly: **CLAIM STANDS for soreyi, xolkete, pxolkete,
xolkte, wisi; asoreyi NOT CHECKED — INCOMPLETE
COVERAGE.** No form's corrected texts-with-form, share,
or boundary evaluation differs from the filed record.
D-M-3's outcome is therefore preserved on replay
evidence, not by preservation fiat: the corrected
checker, run over the same witnesses, reaches the same
classifications and the same outcomes. The kill check
is not triggered for any form, as filed. Nothing in
this addendum moves any standing, verdict, or tally
(C103-4): Spec 097's frozen Stage 4.4 outcome stands
unchanged on its own record.

## 6. Disposition

Unit E-M-1 is discharged: the checker is repaired, both
counterexamples are regression tests, and the
affected-case audit and replay on the already-held
witnesses are executed and filed here. Ledger row E-M-1
moves to done in this landing; the conformance
annotation on the Stage 1 outcome record stands as the
pointer to this record. The study returns to its closed
state, with the checker-conformance scope of the D-M-3
reopening closed with it.

**AI disclosure:** executed by an AI agent (Muse, via
Muse) at the direction of Tristen Pierson, per
constitution sec. VI.
