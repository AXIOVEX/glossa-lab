# Spec 103 — Stage 1 Outcome Record (2026-11-23)

**Execution.** Stage 1 of Spec 103, executed
2026-11-23 under the OD-D-2 commission (registration
PR #727, merge `9d1321c6`), on tower-compute in the
fresh clone `~/.syncyard/worktrees/glossa/sw103-exec`,
against the pinned acquired build (MikeKovetsky/
meroitic @ `145af0836c071e7c9796d37d4b36add00d347c8a`,
checked out at `~/.syncyard/worktrees/glossa/kovetsky-src`).
Executor: `records/stage-1-execution-script.py`;
full machine results: `records/stage-1-results-2026-11-23.json`.
The protocol is spec.md §3 as registered; the two
mechanical clarifications the execution required are
stated where they bite (§2: the funerary-share
convention at zero texts; §3: sub-3-letter containment
fragments). No Otten material was an input at any
point: the Stage 4.4 basis is the acquired build
alone, non-open readings were never read for text
(they carry none in the build), and this record and
its results file carry REM ids, token forms, counts,
and witness keys only — no witness text.

## 1. Step 1 — basis and counts reproduction

The frozen pipeline's basis and partition reproduce
**exactly** from the pinned build: 652 index rows;
368 distinct texts; 335 development / 33 held out;
held-out strata funerary 16, royal/temple 10,
document 5, graffito 2 (development: funerary 223,
royal/temple 41, document 42, graffito 22, other 7).
Every Stage 4.4 figure in
`specs/097-meroitic-reproduction-benchmark/records/stage-4-4-results.json`
recomputes identically: all six candidate forms'
per-stratum occurrences and texts-with-form, all
funerary shares, and the anchor controls on held-out
(ato 11, qore 2 funerary + 1 royal/temple, kdi 1,
ste 1, mk 1). One convention note: for the two
zero-count forms (pxolkete, wisi) the frozen record
carries the funerary share as null (undefined at
zero texts); the recomputation carries 0.0; the
counts themselves are identical, and the frozen FAIL
for both forms rests on the texts leg either way.

## 2. Steps 2–3 — loci, witnesses, classifications

Witness coverage of the held-out partition: **25 of
33 held-out texts carry at least one witness** (an
open alternative reading and/or an expansion
transcription of the preferred reading's source).
Eight carry none: B.O. 1, F.O. 7, F.O. 17, F.O. 29,
F.O. 39, Meroe 40, Sh. 9, Sh. 16. For the two
Shablul texts the reason is structural: the build's
expansion coverage for Shablul is formula fragments
(`data/expansion/karanog/refs/by_inscription/`),
not a transcription of the text, and each Shablul
row's only reading is its preferred one. The
remaining six are rows whose only reading is their
preferred one and which no expansion file reaches.

**No locus, counted or near, produced a DISCREPANCY
or an UNCERTAIN classification.** Every
witness-covered counted locus is FAITHFUL: the
expansion transcription of the same source attests
the counted form as a token. Every witness-covered
near-form locus is FAITHFUL in the registered sense
that the source carries the distinct near form, so
the extraction's distinction is the source's own:
soreyi and asoreyi are distinguished at every
witnessed locus (REM 0135, 0221, 0226, 0232, 0250,
0256, 0281, 0527, 0529 carry soreyi in their
witnesses; REM 0240 carries asoreyi); wosi, not
wisi, is what the witnesses carry at ten loci;
xolkte at REM 0250 is attested as xolkte (2
occurrences), xolkete at REM 0221 as xolkete; the
token psxolkete at REM 0240 is attested as its own
form. No variant was pooled into any candidate at
any point (C103-3): the xolkte family stands in the
witnesses exactly as it stands in the extraction,
three distinct forms with three distinct counts.

Per form (counted loci / near-form loci):

| Form | Frozen (texts, share) | Counted loci | Near-form loci | Outcome |
|---|---|---|---|---|
| soreyi | 10, 1.0 — PASS | 9 FAITHFUL, 1 WITNESS UNAVAILABLE (Sh. 16) | 2 FAITHFUL, 1 UNAVAILABLE (Sh. 9: asoreyi) | **CLAIM STANDS** |
| asoreyi | 2, 1.0 — FAIL | 1 FAITHFUL (REM 0240), 1 WITNESS UNAVAILABLE (Sh. 9) | 10 FAITHFUL, 1 UNAVAILABLE (Sh. 16: soreyi) | **NOT CHECKED — INCOMPLETE COVERAGE** |
| xolkete | 1, 1.0 — FAIL | 1 FAITHFUL (REM 0221) | 2 FAITHFUL | **CLAIM STANDS** |
| pxolkete | 0, — — FAIL | none | 3 FAITHFUL | **CLAIM STANDS** |
| xolkte | 1, 1.0 — FAIL | 1 FAITHFUL (REM 0250, 2 occ) | 2 FAITHFUL | **CLAIM STANDS** |
| wisi | 0, — — FAIL | none | 10 FAITHFUL, 2 UNAVAILABLE (Sh. 16, Sh. 9: wosi) | **CLAIM STANDS** |

Coverage limit, stated per the session's own
instruction: the near-form census detects
edit-distance-1 tokens and containment with a
contained side of at least 3 letters. Containment
fragments shorter than 3 letters (single letters
and digraphs such as "e", "yi", "xo") occur in most
held-out texts (9 to 17 per form; enumerated in the
results file); a fragment that short cannot be
identified with any particular form, so the census
reports them as a class it cannot resolve rather
than as loci. A missed occurrence hiding inside
such a fragment, or inside any of the eight
unwitnessed texts at a point no near token marks,
is outside what this search could detect.

## 3. Step 4 — boundary adjudication and the kill check

With no DISCREPANCY at any locus, there are no
corrections to adjudicate: the corrected counts are
the frozen counts for all six forms (soreyi 10 texts
at share 1.0; asoreyi 2 at 1.0; xolkete 1 at 1.0;
pxolkete 0; xolkte 1 text at 1.0; wisi 0), and no
form's prediction legs change. **The kill check is
not triggered for any form**: no demonstrated
source/extraction discrepancy exists in the checked
scope, so nothing crosses a registered decision
boundary, and no corrected-input sensitivity is
licensed.

The NOT CHECKED outcome for asoreyi is mechanical,
not a judgment call: asoreyi sits exactly 1 text
short of its bar; one of its two counted loci
(Sh. 9) is unwitnessed, and the unwitnessed Sh. 16
carries soreyi, an edit-distance-1 neighbor, as its
counted token. Resolving those two loci in the
direction least favourable to the frozen outcome —
the Sh. 16 token reading as asoreyi in the source —
yields 3 held-out texts at funerary share 1.0, which
crosses the boundary. The held witnesses therefore
cannot exclude the crossing, and the registered
vocabulary returns NOT CHECKED / INCOMPLETE
COVERAGE rather than verified absence. For wisi the
same unwitnessed wosi loci (Sh. 9, Sh. 16) cannot
cross: two resolutions yield at most 2 texts against
a bar of 3, so wisi's outcome is CLAIM STANDS with
the coverage gap filed. For soreyi, neither removing
its one unwitnessed locus (9 texts remain) nor any
resolution of its unwitnessed near locus moves
either leg.

## 4. Interpretation consequence (within the registered limits)

For five of the six candidates — soreyi, xolkete,
pxolkete, xolkte, wisi — the claim stands: on every
witness the program holds, the frozen extraction
preserves the source distinctions and text-presence
counts the decisions turn on. Under the registered
kill check, the input-error explanation of those
forms' sparse held-out failures is **retired within
the checked scope**: the failures read as failures
of the frozen predictions, not as artifacts of
transcription or tokenization in the extraction.
For asoreyi the explanation is neither retired nor
sustained: the check is incomplete at exactly the
decision-bearing loci (the two Shablul texts), and
closing it would need a source witness for Sh. 9
and Sh. 16 that the held build does not contain —
the modern REM edition is the settling record for
such a question and is not held in machine-readable
form (corpus completion record §4, gap 5); any
acquisition toward it is a separate, owner-gated
act, not part of this execution.

Nothing in this outcome moves any standing, verdict,
or tally (C103-4): Spec 097's frozen Stage 4.4
outcome — 1 PARTIALLY SUPPORTED (soreyi), 5
UNSUPPORTED on held-out — stands unchanged on its
own record, and the historical tally is preserved.

## 5. Test-case dispositions

- TC-103-01 (package form): passed at registration.
- TC-103-02 (Step 1 equality): **passed as executed**
  — exact equality with the frozen record, §1.
- TC-103-03 (unavailable-witness path): **exercised**
  — eight held-out texts carry no witness; their
  loci are filed WITNESS UNAVAILABLE with reasons,
  and the outcome vocabulary absorbed them (§2–§3).
- TC-103-04 (kill machinery): the adjudication ran
  with zero discrepancies; the kill condition was
  evaluated for every form and not met. The
  boundary-crossing branch is exercised in the
  negative only; the NOT CHECKED branch, which
  shares its machinery, fired for asoreyi.
- TC-103-05 (no pooling): **passed as executed** —
  xolkete, pxolkete, xolkte, and the attested
  psxolkete were kept distinct at every locus; no
  variant was counted toward any candidate.
- TC-103-06 (limits): this record states the
  outcome's limits in §4; no citing record may treat
  it as a re-score of Stage 4.4.

**AI disclosure:** executed by an AI agent (Muse,
via Muse) at the direction of Tristen Pierson, per
constitution sec. VI.

## Conformance annotation — Round E, 2026-11-25 (the executed checker deviates from §3.4 in two places)

Appended 2026-11-25 under the Round E adjudication
(`specs/091-anchor-comparison-integrity/records/coscientist-sweep-adjudication-2026-11-25.md`,
unit E-M-1), which reopens ledger row D-M-3 in the narrow
scope of checker conformance only. The outcome recorded
above — no discrepancy at any witness-covered locus, CLAIM
STANDS for the five witnessed forms, asoreyi NOT CHECKED —
is preserved and is not reopened by this annotation.

The executed checker (this record's Stage 1 execution
script, SHA-256
`661f0afc1e5e993c9536be5f42fb4f5ac9e86ea5bac1de80f7c31afc8017531a`)
deviates from spec §3.4 as written, in two places. Both
were demonstrated on synthetic witnesses against the filed
functions, isolated without editing their logic, and
reproduced independently at adjudication on tower-compute:

1. **Any-witness FAITHFUL.** `classify_counted_locus()`
   returns FAITHFUL as soon as any witness verdict is
   `attests_form`. Section 3.4 defines FAITHFUL as "every
   available witness agrees with the ingested text at the
   locus", and DISCREPANCY to include a witness showing a
   different token at the locus. Counterexample: extraction
   token `soreyi`, witnesses {`soreyi`, `ato`} — the filed
   code returns FAITHFUL with witness verdicts
   {attests_form, absent}.
2. **Uncertainty erasure in preprocessing.**
   `expansion_tokens()` replaces `[`, `]`, `?`, `!` and
   other markup with separators before classification, so
   a qualified witness token becomes an unqualified exact
   match with no uncertainty flag retained. Section 3.4's
   UNCERTAIN covers the witness that "is itself damaged or
   ambiguous at the locus (lacuna dots, bracketed or
   partial signs)". Counterexample: expansion record
   `[soreyi?]` tokenizes to `["soreyi"]`, which attests the
   form as an exact match.

Scope bounds, as established at adjudication: the filed
aggregate results contain no counted locus with a mixed
witness-verdict set (the 14 counted loci were scanned), so
deviation 1 is not shown to have masked any actual
disagreement in the executed payload. Whether deviation 2
affected any historical classification is indeterminate
from the filed aggregate, which does not preserve raw
uncertainty markup; near-form loci are carried there as
census counts, not per-locus verdicts.

Follow-on act, recorded at adjudication and executed as a
conformance addendum to this study: correct the witness
aggregation so disagreement is explicit (no any-witness
pass); retain uncertainty markers through classification;
add both counterexamples as regression tests; audit the
already-held witnesses for uncertainty-bearing candidate
loci and replay only affected classifications under the
corrected implementation. No new witness acquisition, no
split change. Where the frozen tokenization and §3.4's
classification definitions conflict, the addendum states
the adjudicated treatment before any revised execution;
the filed execution and this outcome record are not
rewritten.
