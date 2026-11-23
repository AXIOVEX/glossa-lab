# Spec 103 — Meroitic Source-Witness Check: the Stage 4.4 Candidate Loci against the Acquired Build's Witnesses

**Status: REGISTERED 2026-11-23 — registration and
execution both commissioned by the owner's OD-D-2 act
of 2026-11-23 (~17:14 ET).** This package registers a
bounded diagnostic: a check of the six Stage 4.4
candidate forms' decision-bearing loci and of the
extraction/tokenization rules that produced their
counts, against the source witnesses held in the
acquired inscription build. Registration lands first;
execution follows in a separate landing under the same
commission, exactly as registered here. No stage of
the check has run at registration.

**Provenance.** The Co-scientist sweep adjudication of
2026-11-23 (PR #725;
`specs/091-anchor-comparison-integrity/records/coscientist-sweep-adjudication-2026-11-23.md`),
unit **D-M-3** (the Meroitic session's Round D
assessment, rank 3), proposed this diagnostic and the
adjudication carried it as **OWNER DECISION OD-D-2**
(§4 of that record). The owner commissioned it on
2026-11-23. The session's stated claim, its kill
check, the fixed split membership, and the no-pooling
rule for the xolkte family are carried into this
registration verbatim in substance (§3, claims.md
C103-1..C103-3), as OD-D-2 required.

## 1. What this spec is

Stage 4.4 of Spec 097 scored six frozen candidate
forms against the held-out partition and returned one
PARTIALLY SUPPORTED (soreyi) and five UNSUPPORTED on
held-out. Four of the five failures are sparse: their
held-out text counts sit at or near zero against a
registered bar of presence in at least 3 held-out
texts. Before those failures are given any further
scientific meaning, this diagnostic asks the prior
question: **are the frozen counts faithful to the
source?** The acquired build is a measured-accuracy
transcription (its own reported figure is 95.6%
against the modern edition on cursive type; corpus
completion record §2), and that aggregate figure is
not a candidate-specific error estimate. Nothing in
the frozen numbers alleges a transcription error; they
identify a bounded audit with a possible decision
consequence.

The claim under test is the session's, verbatim:
**"the frozen extraction preserves the source
distinctions and text-presence counts needed for
these candidate decisions."**

The diagnostic is deliberately narrow. It is not
C-M-21's evidential-unit audit (what constitutes a
unit, and whether units leak across splits) and not
C-M-22's semantic calibration (whether the method
distinguishes meanings). It asks only whether a string
and its token boundaries faithfully encode the source
witness, at the loci where the Stage 4.4 decisions
were actually borne.

## 2. The grounding, as counted at registration

**The frozen extraction, defined.** Stage 4.4 was
executed on tower-compute under Spec 097's campaign
freeze v2 by the program's pipeline
(`pipeline-v2.py`, campaign scratch, SHA-256
`74b831da221f0708b2c5a9f7e9f1a7772175fe2097783f101d33588769e1642e`).
Its extraction is exactly: (i) ingest
`data/inscriptions.jsonl` of the acquired build
(Kovetsky, pin
`145af0836c071e7c9796d37d4b36add00d347c8a`, data
CC BY 4.0), keeping each row's `text` field, deduplicated
exactly, first occurrence carrying the text's stratum
and REM id; (ii) split by freeze v2 §1 — a distinct
text is held out iff SHA-256(text) mod 10 == 0 —
giving 368 distinct texts, 335 development / 33 held
out (funerary 16, royal/temple 10, document 5,
graffito 2); (iii) tokenize by splitting on whitespace
and periods, lower-cased, dropping empty tokens and
tokens beginning with `#`; (iv) count each candidate
form by exact token match, per stratum. The frozen
prediction for every candidate (Stage 4.3 register,
freeze v2): presence in at least 3 held-out texts AND
held-out funerary share within [0.75, 1.0].

**The frozen outcome** (Stage 4.4 outcome record,
2026-11-20; `stage-4-4-results.json`):

| Form | Held-out occurrences | Held-out texts | Result | Margin to the 3-text bar |
|---|---|---|---|---|
| soreyi | 10 (funerary) | 10 | PASS — PARTIALLY SUPPORTED | would fall only if 8 of its 10 texts were lost |
| asoreyi | 2 (funerary) | 2 | FAIL | 1 text short |
| xolkete | 1 (funerary) | 1 | FAIL | 2 texts short |
| pxolkete | 0 | 0 | FAIL | 3 texts short |
| xolkte | 2 (funerary) | 1 | FAIL | 2 texts short (2 occurrences in 1 text; occurrences are not texts) |
| wisi | 0 | 0 | FAIL | 3 texts short |

**The witness scope, stated before any checking.**
The acquired build carries, inside itself, a second
representation of its inscriptions: each
`inscriptions.jsonl` row's `readings[]` array (per-reading
texts with their source apparatus) and the open
transcription files under `data/expansion/` (the
Griffith MI/Meroë sets, Karanòg, Faras, JEA sets; 516
files), joined to rows by the readings' keys. The
check's witnesses are those second representations.
The build's ultimate source — Griffith's printed
editions — is **not machine-readable here** (corpus
completion record §4, gap 5: the modern edition is the
settling record for a contested sign and is not held
in machine-readable form; edition images are not
held). This diagnostic therefore verifies the frozen
extraction against the acquired build's witnesses; it
does not verify the build against the printed page,
and §4's vocabulary carries the coverage consequence
where a locus's only settling witness would be the
page.

## 3. The registered protocol

### 3.1 Materials

- **W-0 — the frozen extraction of record:**
  `pipeline-v2.py` (SHA-256 as §2) and the committed
  `specs/097-meroitic-reproduction-benchmark/records/stage-4-4-results.json`.
  The pipeline's hard-coded custody paths are not
  part of the extraction; the extraction is its
  ingestion, dedup, split, tokenization, and counting
  rules as §2 states them.
- **W-1 — the acquired build:** MikeKovetsky/meroitic
  at pin `145af0836c071e7c9796d37d4b36add00d347c8a`
  (code MIT; data CC BY 4.0 over Griffith's
  public-domain editions), re-acquired openly at
  execution and verified against the pin before any
  computation. No Otten material is an input to this
  diagnostic in any part: the Stage 4.4 basis is the
  acquired build alone (freeze v2 §1).

### 3.2 Step 1 — Basis and counts reproduction

Recompute, from W-1, the ingestion, exact dedup,
split, and Stage 4.4 counting under the frozen rules.
Required equalities, all registered here in advance:
652 index rows; 368 distinct texts; 335 development /
33 held out; held-out strata funerary 16,
royal/temple 10, document 5, graffito 2; and the
per-form per-stratum occurrences and texts-with-form
of `stage-4-4-results.json`, including the anchor
controls. A failed equality is itself a finding: it
is filed, the affected form's check proceeds on the
recomputed basis with the divergence stated, and the
divergence is adjudicated under §3.5 like any other
discrepancy. (TC-103-02.)

### 3.3 Step 2 — Locus census

For each of the six forms, enumerate its
**decision-bearing loci**: (a) every held-out text in
which the frozen counting found the form, identified
by the REM id of the text's first-occurrence row,
with the occurrence count; and (b) the **near-form
census** over all 33 held-out texts — every token at
edit distance 1 from the form; every token properly
containing the form or properly contained in it; and
every occurrence of the form as a substring of a
held-out text's raw string not aligned to a token
boundary (the boundary cases: a form joined to a
neighbour, or split by a divider the tokenizer treated
as a separator). The census is filed in full in the
outcome record. A small inspected sample cannot
certify global absence: the census is exhaustive over
the held-out partition by construction, and the
outcome record states which classes of possible missed
occurrence the census can and cannot detect (it cannot
detect a missed occurrence whose witness token differs
from the form by more than the census's distance and
boundary rules).

### 3.4 Step 3 — Witness comparison

For each locus (counted or near-form), take the locus
inscription's witness token streams: (i) the texts of
the row's open `readings[]` other than the preferred
reading the row's `text` field carries, and (ii) the
`data/expansion/` transcription for the inscription's
preferred reading key, where a file entry exists.
Tokenize witness texts by the frozen rule. Compare
the candidate-relevant tokens — the counted token, or
the near-form token and its immediate neighbours —
and classify the locus:

- **FAITHFUL** — every available witness agrees with
  the ingested text at the locus.
- **DISCREPANCY** — a witness shows a different token
  at the locus; the direction is stated (witness
  carries the candidate form where the extraction
  does not, or the reverse, or both carry distinct
  non-candidate tokens).
- **UNCERTAIN** — the witness is itself damaged or
  ambiguous at the locus (lacuna dots, bracketed or
  partial signs), so it cannot settle the token.
- **WITNESS UNAVAILABLE** — no second representation
  of the inscription is held (no non-preferred open
  reading and no expansion entry).

Registered cautions: agreement of the preferred
reading with the row's `text` is by construction and
is **not** a witness pass; only (i) and (ii) witness.
A witness token that is a spelling variant of the
form is faithful source spelling under freeze v2 §7's
varietas discipline, not an error: it is recorded as
FAITHFUL (variant noted) and never counted toward the
form. **Do not pool xolkte-family variants**
(xolkete, pxolkete, xolkte) — each is checked and
reported as its own form, and no variant rescues
another (claim C103-3). **No character is corrected
by its effect on a desired score**: a correction
enters §3.5 only where this step demonstrates a
discrepancy, with its witness evidence filed.

### 3.5 Step 4 — Boundary adjudication (the kill check applied)

Apply adjudicated corrections — DISCREPANCY loci
only, direction as demonstrated — to the token counts
**within the frozen partition**: the 33 held-out
texts are the same texts throughout; a corrected
token does not rehash its text and no text changes
side (the fixed split membership; claim C103-2).
Recompute each form's texts-with-form and funerary
share under the corrections and state, per form,
whether either leg of the frozen prediction changes
(texts ≥ 3; share within [0.75, 1.0]).

The kill check, the session's verbatim: **a
demonstrated source/extraction discrepancy that
crosses a registered decision boundary kills the
claim for the affected candidate. If adjudicated
source corrections leave every relevant threshold
outcome unchanged, retire this as an explanation of
the failures within the checked scope. If witnesses
or search coverage are insufficient, return NOT
CHECKED / INCOMPLETE COVERAGE, not verified absence.**

## 4. Outcome vocabulary

Per candidate form, exactly one of:

- **CLAIM STANDS** — every decision-bearing locus was
  witness-checked, and no adjudicated correction
  changes either leg of the form's frozen prediction.
- **CLAIM KILLED** — a demonstrated discrepancy,
  adjudicated under §3.5, changes either leg of the
  form's frozen prediction.
- **NOT CHECKED — INCOMPLETE COVERAGE** — at least
  one decision-bearing locus is UNCERTAIN or WITNESS
  UNAVAILABLE, and resolving every such locus in the
  direction least favourable to the form's frozen
  outcome could change either leg. (For soreyi this
  reads on its PASS: unresolved loci count against it
  only in the numbers §2's margin states.)

The study outcome is the six-form table in this
vocabulary, the filed census and classifications, and
the interpretation consequence of §5 — nothing else.

## 5. What the outcome can and cannot change

- The diagnostic interprets the **provenance** of the
  sparse Stage 4.4 failures. It moves **no standing,
  verdict, or tally by itself** (claim C103-4): Spec
  097's frozen outcome — 1 PARTIALLY SUPPORTED,
  5 UNSUPPORTED on held-out — stands as executed,
  whatever this check finds.
- Where every failed candidate's claim stands, the
  input-error explanation of those failures is
  retired within the checked scope, and the failures
  stand as failures of the frozen predictions, as
  Stage 4.4 already records them.
- Where a candidate's claim is killed, the finding
  licenses exactly one next act: a **separately
  registered** corrected-input sensitivity result,
  preserving the historical tally. This spec registers
  no such result and computes none.
- A numerical held-out pass under corrected inputs
  would still not establish semantic discrimination
  or a new reading (the session's own limit, carried).
- NOT CHECKED forms carry no interpretation in either
  direction.

## 6. Hard limits

- **One commission, two landings.** The owner's
  OD-D-2 act commissioned registration **and**
  execution; execution follows in its own landing
  under this spec, exactly as registered. Any change
  to the protocol after this registration is a new
  registration, not an amendment executed mid-check.
- **Custody and venue.** All computation runs on
  tower-compute. The diagnostic's inputs are the
  openly licensed acquired build and the program's
  own frozen artifacts; outputs are record-form
  (counts, REM identifiers, classifications) and are
  filed in this spec's `records/`. No Otten-derived
  text is used, produced, or published by any stage
  (F-6 is not engaged; it is stated so the sweep of
  TC-103-05 has a registered line to check).
- **No external contact** is authorized by this spec.
- Spec 097's freezes, executed bytes, records, and
  adjudicated verdicts are not modified by this spec
  or by any stage of this study; this spec's outcome
  record lives in its own `records/`.
- **No standing is set by registration or by the
  diagnostic.** Any ledger standing change for
  C103-1..C103-4 remains a recorded adjudication by a
  named human approver. Automated actors never
  approve, verify, or promote.

## 7. Decisions

- **D-103-1 — number.** At the check of 2026-11-23
  the highest landed spec package on origin/main was
  102 (`specs/102-meroitic-fresh-affiliation-test/`);
  no 103 directory, branch, or open pull request
  carried 103. (The OD-D-1 recording in flight the
  same day is records-only and takes no spec number.)
  This package takes 103.
- **D-103-2 — claims.** C103-1..C103-4 (claims.md)
  are intaken at registration through
  `tools/ledger/import_bundle.py`, the only sanctioned
  path, inside this landing's PR, in the Spec
  096/098/099/100/101/102 pattern. Intake sets no
  standing.
- **D-103-3 — program-map placement.** The program is
  entered in
  `glossa-indus/map/program-map-taxonomy.json` under
  Sign inventory & corpus / Signary & corpus models —
  Spec 097's own placement, whose reasoning carries
  over (D-102-3): this study is the Meroitic program's
  diagnostic on its own executed campaign, not program
  infrastructure.
- **D-103-4 — the witness scope is the build's second
  representation.** Griffith's printed page is the
  settling record for a contested sign and is not
  machine-readable here (corpus completion record §4
  gap 5; §2 above). Registering the check against
  witnesses the program does not hold would register
  an unexecutable protocol; registering it without
  the coverage vocabulary would overclaim its reach.
  The design therefore checks against the witnesses
  held — the readings arrays and the expansion files —
  and carries NOT CHECKED — INCOMPLETE COVERAGE as a
  first-class outcome (§4).
- **D-103-5 — reproduction before witnesses.** Step 1
  (§3.2) precedes all witness work: a diagnostic that
  cannot first reproduce the frozen counts from the
  pinned build has no basis for adjudicating them, so
  the reproduction's equalities are registered as
  pass conditions (TC-103-02), and their failure is a
  finding of the check, not a precondition silently
  assumed.

**AI disclosure:** executed by an AI agent (Muse, via Muse)
at the direction of Tristen Pierson, per constitution sec. VI.
