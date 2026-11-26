# Spec 103 — Conformance Addendum Registration (2026-11-25)

**Commission.** Round E of the Co-scientist loop, Meroitic
unit **E-M-1** (adjudication:
`specs/091-anchor-comparison-integrity/records/coscientist-sweep-adjudication-2026-11-25.md`
§3.1, landed PR #741, merge `e2f683ec`), which reopens
ledger row D-M-3 in the narrow scope of checker conformance
only. This addendum is that adjudication's recorded
follow-on act. It is registered here, before any revised
execution runs; the branch's git history proves the order.

**Scope.** The executed Stage 1 checker
(`records/stage-1-execution-script.py`, SHA-256
`661f0afc1e5e993c9536be5f42fb4f5ac9e86ea5bac1de80f7c31afc8017531a`)
deviates from spec.md §3.4 as written, in two places, both
demonstrated at adjudication and annotated on the outcome
record:

1. **Any-witness FAITHFUL.** `classify_counted_locus()`
   returns FAITHFUL as soon as any witness verdict is
   `attests_form`. Section 3.4 defines FAITHFUL as "every
   available witness agrees with the ingested text at the
   locus". Counterexample: extraction token `soreyi`,
   witnesses {`soreyi`, `ato`} — verdicts {attests_form,
   absent} — classified FAITHFUL by the filed code.
2. **Uncertainty erasure in preprocessing.**
   `expansion_tokens()` replaces `[`, `]`, `?`, `!` and
   other markup with separators before classification, so
   a qualified witness token becomes an unqualified exact
   match with no uncertainty flag retained. Section 3.4's
   UNCERTAIN covers the witness that "is itself damaged or
   ambiguous at the locus (lacuna dots, bracketed or
   partial signs)". Counterexample: expansion record
   `[soreyi?]` tokenizes to `["soreyi"]`, attesting the
   form as an exact match.

**What this addendum does.** (a) A corrected checker,
filed as a new script (`records/conformance-addendum-script.py`);
the filed Stage 1 script is not edited. (b) Regression
tests for both counterexamples plus the preserved
behaviours (`records/conformance-addendum-tests.py`).
(c) An audit of the already-held witnesses for
uncertainty-bearing candidate loci and mixed witness
verdicts, and a replay of the affected classifications
under the corrected implementation, against the same
pinned build (MikeKovetsky/meroitic @
`145af0836c071e7c9796d37d4b36add00d347c8a`) and the same
frozen basis. No new witness acquisition, no split
change, no new witness source.

**Preservation rail.** D-M-3's outcome — CLAIM STANDS
for soreyi, xolkete, pxolkete, xolkte, wisi; asoreyi NOT
CHECKED — INCOMPLETE COVERAGE — and the six-form table
are preserved. If the replay evidence itself contradicts
an outcome, execution stops and reports; no outcome is
rewritten by this addendum's hand. Nothing in this
addendum moves any standing, verdict, or tally (C103-4).

## The adjudicated treatment (stated before any revised execution)

Where the frozen tokenization and §3.4's classification
definitions conflict, the following treatment governs the
corrected implementation. It is stated here, in advance,
and the corrected script implements exactly this.

1. **Token identity is unchanged.** The frozen
   tokenization still decides what a token is: for
   expansion records, the filed preprocessing set
   (`[`, `]`, `?`, `!`, `|`, `:`, `=`) still becomes
   separators; for open alternative readings, splitting
   is still on whitespace and dots. The basis, the split,
   and every text are untouched; no text is edited and
   nothing is rehashed. The repair changes only (a) the
   retention of uncertainty markup alongside each token
   and (b) the aggregation of witness verdicts into a
   locus classification.
2. **Uncertainty retention.** Each witness token carries
   an uncertainty flag. For an expansion record: a token
   is uncertainty-bearing if a character of the filed
   markup set stood immediately adjacent to its span in
   the folded record text (this covers `[soreyi?]` — the
   token `soreyi` flagged by the adjacent `[` and `?` —
   and the fragments of an intra-token bracketed token
   such as `so[re]yi`, both fragments flagged). For an
   open alternative reading: a token chunk containing
   any of `[`, `]`, `?`, `!` has those characters removed
   for identity and carries the flag.
3. **Witness verdicts, extended.** A witness verdict of
   `attests_form` or `attests_variant` becomes
   `attests_form_uncertain` / `attests_variant_uncertain`
   when every token on which the verdict rests is
   uncertainty-bearing. `partial_or_containment` is
   unchanged (it is already an uncertainty-class verdict:
   the witness cannot settle the token). `absent` is
   unchanged.
4. **Counted-locus aggregation** (the counted token is
   the form the extraction counted in the text), in
   precedence order:
   - no witnesses → **WITNESS UNAVAILABLE**;
   - an unqualified attestation (form or variant) and an
     unqualified absence coexist → **DISCREPANCY**
     (witness disagreement is explicit; direction: a
     witness does not carry the form the extraction
     counted);
   - every witness verdict is `absent` and the expansion
     witness is among them → **DISCREPANCY** (the filed
     all-absent rule, retained);
   - any verdict is uncertainty-bearing, or absence
     appears only from alternative readings without an
     unqualified attestation, or absence coexists with
     uncertainty-bearing verdicts → **UNCERTAIN** (an
     uncertainty-bearing witness cannot settle the
     locus, and FAITHFUL requires every available
     witness to agree);
   - all verdicts are unqualified attestations, at least
     one a variant → **FAITHFUL (variant noted)**;
   - all verdicts are `attests_form` → **FAITHFUL**.
5. **Near-locus aggregation** (the extraction did not
   count the form; a near-form token occurs), in
   precedence order:
   - no witnesses → **WITNESS UNAVAILABLE**;
   - the expansion witness attests the form unqualified,
     or some witness attests the form unqualified and no
     witness carries the near token unqualified →
     **DISCREPANCY (missed count)**;
   - witnesses disagree about the locus (one attests the
     form, another carries the near token), or the only
     attestation of the form or of the near token is
     uncertainty-bearing → **UNCERTAIN**;
   - the near token is carried unqualified by at least
     one witness, no witness attests the form, and no
     relevant verdict is uncertainty-bearing →
     **FAITHFUL (source carries the distinct near
     form)**;
   - all remaining cases → **UNCERTAIN**.
6. **Step 4 is unchanged.** The filed execution's
   boundary machinery — corrections on DISCREPANCY loci
   only, and the NOT CHECKED least-favourable scenarios —
   is applied without modification to the corrected
   classifications, and the corrected outcomes are
   compared against the filed six-form table.

## Replay protocol

The corrected script recomputes Step 1 (basis and counts)
and asserts exact equality with the frozen record
(TC-103-02 re-run). It then classifies every counted and
near-form locus under both the filed rules (re-implemented
unchanged, as a control) and the corrected rules, and
files the per-locus diff. The audit scans every witness
of every held-out text (expansion records and open
alternative readings) for characters of the markup set,
and reports their incidence at candidate loci. The replay
reports: any locus whose classification changes; any form
whose corrected Step 4 outcome differs from the filed
table; and the bound the replay evidence supports on
deviation 2's historical impact (the set of historical
classifications whose witnesses carry uncertainty markup
at the locus).

## Test cases

TC-103-07..TC-103-10, added to `test-cases.md` in this
same registration landing: aggregation disagreement
(counterexample 1); uncertainty retention
(counterexample 2); replay integrity (Step 1 equality,
control-rule reproduction of the filed results, diff
confined to loci the audit flags); outcome preservation
(the six-form table under the corrected rules).

**Venue.** Tower-compute, fresh clone
`~/.syncyard/worktrees/glossa/sw103-addendum`, against
the pinned build at
`~/.syncyard/worktrees/glossa/kovetsky-src` (unchanged).

**AI disclosure:** executed by an AI agent (Muse, via
Muse) at the direction of Tristen Pierson, per
constitution sec. VI.
