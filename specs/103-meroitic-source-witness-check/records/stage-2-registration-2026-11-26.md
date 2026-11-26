# Spec 103 — Stage 2 Registration: Witness Completion for asoreyi (2026-11-26)

**Commission.** The owner's order in the Glossa-Lab chat,
2026-11-26 10:27 ET: "do 1-3. Lets put all focus on
Meroitic" — item 1 being: register and execute the
asoreyi witness check against the REM witness now held
in custody. The same order directs that, while doing
it, all learnings about mechanisms transferable to the
Indus and Eteocypriot programs be filed explicitly; that
direction is discharged by a mechanism note filed with
the execution landing
(`records/stage-2-mechanism-note-2026-11-26.md`), not by
this registration. This registration is filed, and its
commit lands, before any transliteration is transcribed
from the witness and before any locus is classified
under it; the branch's git history proves the order
(TC-103-11).

**Where the study stands at registration.** Stage 1
(executed 2026-11-23, PR #728) and the conformance
addendum (executed 2026-11-25, PR #743) agree on the
six-form table: **CLAIM STANDS for soreyi, xolkete,
pxolkete, xolkte, wisi; asoreyi NOT CHECKED —
INCOMPLETE COVERAGE.** Five forms are closed. Exactly
one form remains open, and it is open for one stated
reason: two of its decision-bearing loci sit in the
two Shablul texts that carry no witness in the pinned
acquired build. This stage completes the witness
coverage for those loci from the edition of record and
restates the table whole. It changes no other form's
evidence and no other form's outcome machinery.

## 1. The claim under test

Claim C103-1, verbatim: **"the frozen extraction
preserves the source distinctions and text-presence
counts needed for these candidate decisions"** — as it
applies to the one form whose check is incomplete,
**asoreyi** (frozen outcome on held-out: 2 texts,
funerary share 1.0, FAIL against the registered bar of
presence in at least 3 held-out texts with share
within [0.75, 1.0]; exactly 1 text short).

The kill check, the session's verbatim, registered at
spec.md §3.5 and carried here unchanged: **a
demonstrated source/extraction discrepancy that
crosses a registered decision boundary kills the claim
for the affected candidate. If adjudicated source
corrections leave every relevant threshold outcome
unchanged, retire this as an explanation of the
failures within the checked scope. If witnesses or
search coverage are insufficient, return NOT CHECKED /
INCOMPLETE COVERAGE, not verified absence.**

Outcomes are read in spec.md §4's vocabulary only:
CLAIM STANDS / CLAIM KILLED / NOT CHECKED — INCOMPLETE
COVERAGE, per form. Under C103-4 and spec.md §5, no
outcome of this stage moves Spec 097's frozen Stage 4.4
outcome (1 PARTIALLY SUPPORTED, 5 UNSUPPORTED), its
verdicts, or its tallies; a CLAIM KILLED outcome for
asoreyi would license exactly one next act, a
separately registered corrected-input sensitivity
result, which this stage does not compute.

## 2. The loci in scope

The witness-covered loci of Stage 1 (41 of 47) keep
the corrected classifications of the conformance
addendum's replay; the execution re-verifies them by
control re-run (TC-103-12) and changes none of them.
The stage's new evidence bears on exactly the six
loci filed WITNESS UNAVAILABLE, all in the two
Shablul texts:

| Form | Kind | Text | Extraction token | Frozen bearing |
|---|---|---|---|---|
| asoreyi | counted | Sh. 9 | asoreyi (1 occ) | 1 of asoreyi's 2 counted texts |
| asoreyi | near (edit distance 1) | Sh. 16 | soreyi | if the source token is asoreyi, asoreyi reaches 3 texts and crosses its bar |
| soreyi | counted | Sh. 16 | soreyi (1 occ) | 1 of soreyi's 10 counted texts; no resolution moves either of soreyi's legs (Stage 1 record §3) |
| soreyi | near (edit distance 1) | Sh. 9 | asoreyi | the same token as asoreyi's counted locus, from soreyi's side |
| wisi | near (edit distance 1) | Sh. 9 | wosi | two resolutions yield at most 2 texts against a bar of 3; cannot cross (Stage 1 record §3) |
| wisi | near (edit distance 1) | Sh. 16 | wosi | as the preceding |

The remaining six unwitnessed held-out texts (B.O. 1,
F.O. 7, F.O. 17, F.O. 29, F.O. 39, Meroe 40) carry no
counted or near-form locus for any of the six forms in
the filed census; their witnesses are identified and
transcribed under the same protocol so the completed
coverage is a fact of the record, and the completeness
scan of §4.5 applies to them.

## 3. Materials

- **W-2 — the edition-of-record witness:** Leclant
  (dir.), Heyler, Berger-El-Naggar, Carrier, Rilly,
  *Répertoire d'Épigraphie Méroïtique: Corpus des
  inscriptions publiées* (Académie des Inscriptions et
  Belles-Lettres, Paris, 2000; ISBN 2-87754-113-4),
  held in custody at
  `~/.syncyard/worktrees/glossa/glossa-custody/spec103/`
  on tower-compute as the Académie's Persée
  open-access deposit (acquisition record
  `records/rem-witness-acquisition-record-2026-11-26.md`
  §8, PR #759):
  - Tome I: `rem-tome-1-rem0001-0387.pdf`, 215,556,263
    bytes, 714 pp., SHA-256
    `f20d9f955ff2a74d391d894f65958c3d2848d5282a26a5c5ba5ae70dd591afce`
  - Tome II: `rem-tome-2-rem0401-0851.pdf`,
    174,384,353 bytes, 658 pp., SHA-256
    `55b13325bad738b8e2e53b3fc41f8340162625c8c5a2a3e982da811115dff167`
  - Tome III: `rem-tome-3-rem1001-1278.pdf`,
    182,222,445 bytes, 712 pp., SHA-256
    `cc24ffe691c6522b71cc56cc812554c41786fe0654742abed4238bbcb5ebe6a1`
  The custody hashes are re-verified at execution
  before any page is read (TC-103-12).
- **The corrected checker:**
  `records/conformance-addendum-script.py`, SHA-256
  `070a5c4d12bdfd65fdfbaf2bb27d082dd3dc14d45afd3bf52adbc8b28be883a8`,
  implementing the adjudicated treatment of
  `records/conformance-addendum-registration-2026-11-25.md`
  (witness disagreement explicit; uncertainty markup
  retained as a per-token flag; Step 4 machinery
  unchanged). The filed Stage 1 script (SHA-256
  `661f0afc…`) is not used and not edited.
- **W-1 — the acquired build:** MikeKovetsky/meroitic
  @ `145af0836c071e7c9796d37d4b36add00d347c8a`,
  unchanged at
  `~/.syncyard/worktrees/glossa/kovetsky-src`; the
  frozen basis, split, and counts are Stage 1's,
  re-verified by the control re-run. No text is
  edited, nothing is rehashed, no text changes side
  (C103-2). No Otten material is an input in any part.

## 4. Witness identification and treatment (stated before extraction)

### 4.1 Identification of the eight texts in the REM

Each unwitnessed text is identified with the REM entry
whose "Désignation originelle" is the text's Griffith
publication number, cross-checked against the entry's
monument description and, for the Shablul texts,
against Tome III's Index B. Identification metadata
(entry numbers and page positions) was gathered from
the PDFs' embedded OCR text layer as a locating aid
before this registration; the OCR layer is never the
witness (§4.2), and no transliteration had been
transcribed and no locus classified at registration
time.

| Text | REM entry | Tome (chapter) | Custody PDF page of entry head |
|---|---|---|---|
| Sh. 9 | REM 0376 | I (ch. 3, Karanog et Shablul) | 692 |
| Sh. 16 | REM 0383 | I (ch. 3, Karanog et Shablul) | 706 |
| Meroe 40 | REM 0440 | II (ch. 4, Méroé) | 84 |
| F.O. 7 | REM 0557 | II (ch. 6, Ostraca de divers sites) | 216 |
| F.O. 17 | REM 0567 | II (ch. 6) | 236 |
| F.O. 29 | REM 0579 | II (ch. 6) | 260 |
| F.O. 39 | REM 0589 | II (ch. 6) | 280 |
| B.O. 1 | REM 0591 | II (ch. 6) | 284 |

One correction to the acquisition record is filed
here: its §3 chapter map, drawn from the edition's
Sommaire général, placed the Faras ostraca in Tome
II ch. 5 (REM 0501–0546). The entries themselves sit
in ch. 6, "Ostraca de divers sites" (REM 0551–0597),
with B.O. 1 among them at REM 0591 (its entry
describes the Buhen ostracon found west of the South
Temple, and B.O. 2 follows at REM 0592). Entry-level
identification governs over the sommaire map. Every
identification is verified against the rendered page
image at execution (TC-103-13): entry head, REM
number, and original designation read off the page,
not the OCR layer.

### 4.2 What the witness is

The witness for a text is the transliteration printed
in its REM entry, transcribed from the rendered page
image of the custody PDF. The transcription preserves
the printed editorial markup (brackets, `?`, `!`,
lacuna dots, parentheses) in the filed witness data
(`records/stage-2-witness-data-2026-11-26.json`: per
text, its REM number, tome, PDF page, and the
transcribed token stream with per-token uncertainty
flags). The edition's French apparatus is not filed;
the witness data is the transliteration token stream
of eight short published inscriptions, in record form.

### 4.3 Tokenization and uncertainty

Witness token identity is the frozen tokenization's
(splitting on whitespace and periods, lower-cased,
empty tokens and `#`-initial tokens dropped), with the
addendum's uncertainty retention: a transcribed chunk
containing any of `[`, `]`, `?`, `!` has those
characters removed for identity and carries the
uncertainty flag. One stated addition, registered
here in advance: before tokenization, the transcribed
text is folded (Unicode NFD, combining marks
stripped), because the REM prints its transliteration
with typographic diacritics that the build's witness
streams do not carry; folding is the identity on the
ASCII tokens the candidate decisions turn on, and it
is the same fold the filed expansion preprocessing
applies.

### 4.4 The REM witness's place in the aggregation

For its text, the REM witness is the sole witness,
and it takes the expansion witness's role in the
corrected checker's aggregation (its witness id
carries the `expansion:` prefix, as
`expansion:rem-edition-REM0376` etc.): it is the
edition-of-record transcription of the inscription's
source, the same witness class as the build's
expansion files, which are transcriptions of the
printed editions. Classification is by the corrected
checker's functions unchanged
(`classify_counted_corrected`, `classify_near_corrected`,
and the Step 4 machinery of
`records/conformance-addendum-script.py`, imported,
not re-implemented). Consequences, stated in advance:
an unqualified REM attestation of a counted form
classifies its locus FAITHFUL; a counted locus whose
REM witness carries neither the form nor a variant
nor a containment is DISCREPANCY under the filed
all-absent-with-expansion rule (direction stated);
a near locus whose REM witness attests the candidate
form unqualified and does not carry the near token is
DISCREPANCY (missed count); a near locus whose REM
witness carries the near token unqualified and does
not attest the form is FAITHFUL (source carries the
distinct near form); attestations resting only on
uncertainty-flagged tokens classify UNCERTAIN, as
registered in the addendum.

### 4.5 Completeness scan

The transcribed REM token streams of all eight texts
are scanned for the six candidate forms and for
tokens at edit distance 1 from, or in a containment
relation (contained side at least 3 letters) with, a
candidate form. An attestation that falls inside the
filed census classes is classified under §4.4. An
attestation outside them (a form token in a text with
no filed locus, at a point no extraction-side near
token marks) is filed in the outcome record as a
coverage observation, outside the classification
machinery: the registered census bounds what the
check can detect (spec.md §3.3), and this stage does
not silently extend it.

## 5. Test cases

TC-103-11..TC-103-16, added to `test-cases.md` in
this same registration landing: registration-before-
execution order; control and custody integrity
(Step 1 equality, the 41-locus control re-run, the
custody hashes); witness identification on the
rendered page; decision-token verification on the
rendered page; no pooling and no score-driven
correction under the completed coverage; outcome
vocabulary and standing discipline for the restated
table.

## 6. Hard limits

- The Stage 1 outcome record and the conformance
  addendum's records are not edited by this stage;
  the new outcome is a new dated record.
- The frozen partition is fixed throughout (C103-2);
  corrections, if any, are token-level adjudications
  keyed to loci under spec.md §3.5, never rehashing.
- No variant is pooled into any candidate (C103-3);
  the xolkte family is untouched by this stage's loci
  and stands as classified.
- Venue: tower-compute only. Outputs are record-form
  and are filed only in this spec's `records/`.
- No external contact, no purchase, no other
  program's work is authorized by this registration.
  The transfer-learnings mechanism note is an
  observation record; it starts no work elsewhere and
  moves no standing or verdict anywhere.

**AI disclosure:** executed by an AI agent (Muse, via
Muse) at the direction of Tristen Pierson, per
constitution sec. VI.
