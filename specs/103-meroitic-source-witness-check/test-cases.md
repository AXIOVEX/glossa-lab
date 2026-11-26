# Spec 103 — Test Cases

Each test case names the claim it exercises, its
procedure, and its pass condition. TC-103-01 is
Stage 0's acceptance test and is recorded in
`records/registration-2026-11-23.md`; TC-103-02..
TC-103-06 execute with Stage 1.

**TC-103-01 — Package form (C103-1..C103-4; Stage 0).**
Parse `aee-claims.json`; compare its claim ids and
order against claims.md; check every claim carries a
falsifier and a does-not-establish line.
*Pass:* the JSON parses; the same four claim ids in
the same order in both files; every falsifier and
does-not-establish line present.

**TC-103-02 — Basis and counts reproduction (C103-1,
C103-2; Stage 1, protocol Step 1).** From the acquired
build verified at pin
`145af0836c071e7c9796d37d4b36add00d347c8a`, recompute
the ingestion, exact dedup, freeze v2 §1 split, and
Stage 4.4 counting under the frozen rules of
spec.md §2.
*Pass:* 652 index rows; 368 distinct texts; 335
development / 33 held out; held-out strata funerary
16, royal/temple 10, document 5, graffito 2; and every
per-form per-stratum occurrence and texts-with-form
figure, and the anchor controls, equal
`stage-4-4-results.json` exactly. Any inequality is
filed as a finding of the check (spec.md §3.2), not
silently absorbed.

**TC-103-03 — Split fixedness (C103-2; Stage 1).**
Inspect the execution tool and its working artifacts:
the partition it scores against is the recomputation
of TC-103-02 over the uncorrected texts; corrections
are applied as token-level adjudications keyed to
loci, never by editing a text and rehashing it.
*Pass:* the held-out text set in the execution's
working basis is identical (same 33 texts, by hash)
to TC-103-02's; no code path in the execution tool
recomputes a split assignment from a corrected text.

**TC-103-04 — No pooling, no uncorrected-by-score
corrections (C103-3; Stage 1).** Read the outcome
record's census, classification, and adjudication
tables.
*Pass:* xolkete, pxolkete, and xolkte are reported as
three distinct forms everywhere, with no pooled count
in any table; every correction in the adjudication
table cites a witness divergence (inscription, both
token readings, classification DISCREPANCY); no token
is counted toward a candidate form as its spelling
variant.

**TC-103-05 — Custody and output sweep (C103-1,
C103-4; Stage 1).** Inspect every input the execution
loaded and every output it filed.
*Pass:* inputs are the pinned acquired build and the
program's frozen artifacts only; no Otten-derived
text appears in any input or output; outputs are
record-form (counts, REM identifiers, classifications)
and are filed only in this spec's `records/`; the
execution ran on tower-compute.

**TC-103-06 — Outcome vocabulary and standing
discipline (C103-4; Stage 1).** Read the outcome
record and search the landing's citing records.
*Pass:* every candidate form carries exactly one
outcome in spec.md §4's vocabulary (CLAIM STANDS /
CLAIM KILLED / NOT CHECKED — INCOMPLETE COVERAGE);
no record states a changed Stage 4.4 score, verdict,
or tally; a CLAIM KILLED outcome, if any, is followed
only by the §5 licence statement (a separately
registered sensitivity), never by a recomputed score
presented as Stage 4.4's.

**TC-103-07 — Aggregation disagreement (C103-1;
conformance addendum, deviation 1).** Drive the
corrected checker's counted-locus classification with
synthetic witnesses: extraction token `soreyi`, witness
token lists {`soreyi`} and {`ato`} (verdicts
attests_form and absent).
*Pass:* the classification is DISCREPANCY, not
FAITHFUL; and the preserved behaviours hold on their
synthetic cases (unanimous attests_form → FAITHFUL;
unanimous variant attestation → FAITHFUL (variant
noted); all-absent with the expansion witness present
→ DISCREPANCY; no witnesses → WITNESS UNAVAILABLE).

**TC-103-08 — Uncertainty retention (C103-1;
conformance addendum, deviation 2).** Tokenize the
synthetic expansion record `[soreyi?]` under the
corrected tokenization, and classify a counted locus
whose only witness it is.
*Pass:* the token `soreyi` is produced with its
uncertainty flag set; the witness verdict is
attests_form_uncertain; the locus classification is
UNCERTAIN, not FAITHFUL. An unqualified record
(`soreyi`) tokenizes with the flag clear and attests
unqualified.

**TC-103-09 — Replay integrity (C103-1, C103-2;
conformance addendum).** Run the corrected script
against the pinned build
`145af0836c071e7c9796d37d4b36add00d347c8a`.
*Pass:* Step 1 reproduces the frozen basis and counts
exactly (TC-103-02's figures); the control
implementation of the filed rules reproduces the
filed Stage 1 classifications locus for locus; every
locus whose corrected classification differs from its
filed classification is one the audit flags (mixed
witness verdicts or uncertainty markup at the locus).

**TC-103-10 — Outcome preservation (C103-4;
conformance addendum).** Apply the unchanged Step 4
machinery to the corrected classifications.
*Pass:* the six-form outcome table equals the filed
table (CLAIM STANDS for soreyi, xolkete, pxolkete,
xolkte, wisi; asoreyi NOT CHECKED — INCOMPLETE
COVERAGE). Any difference stops the addendum and is
reported, not absorbed: no outcome is rewritten by
this addendum's hand.
