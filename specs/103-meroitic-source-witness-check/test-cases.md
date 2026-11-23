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
