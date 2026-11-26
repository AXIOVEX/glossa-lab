# Spec 103 — Stage 2 Outcome Record: Witness Completion for asoreyi (2026-11-26)

Executed 2026-11-26 under
`records/stage-2-registration-2026-11-26.md` (registration
commit `25cbf825`, PR #761, landed before any extraction
or classification ran). Executor:
`records/stage-2-execution-script.py`; machine results:
`records/stage-2-results-2026-11-26.json`; witness data:
`records/stage-2-witness-data-2026-11-26.json`. The
Stage 1 outcome record and the conformance addendum's
records are untouched by this stage.

## 1. Outcome in one paragraph

The witness completion ran and the coverage gap did not
close, for a reason the record now states exactly: **the
REM entries for the eight unwitnessed texts print no
transliteration of their inscriptions.** The edition's
entry form for these texts is a notice (location,
original designation, monument identification,
dimensions, inscription description, bibliography) plus
plates reproducing a photograph and, where one exists,
the original publication's hand copy or facsimile. There
is no REM transliteration token stream to transcribe for
any of the eight texts, so under the corrected checker
the six open loci keep the classification WITNESS
UNAVAILABLE with the completed witness set, and the
six-form table restates unchanged: **CLAIM STANDS for
soreyi, xolkete, pxolkete, xolkte, wisi; asoreyi NOT
CHECKED — INCOMPLETE COVERAGE** — now on the new ground
that the held edition of record carries no
transliteration witness for Sh. 9 or Sh. 16. The kill
check does not fire: no discrepancy is demonstrated at
any locus, and the input-error explanation is neither
confirmed nor retired for asoreyi. The REM route for
these two texts is closed on the record (§7).

## 2. Control and custody (TC-103-12: PASS)

- The three custody tome PDFs hash-match the Stage 2
  registration's values exactly (Tome I `f20d9f95…`,
  Tome II `55b13325…`, Tome III `cc24ffe6…`).
- The filed conformance-addendum script was replayed
  untouched and its regenerated results are deep-equal
  and byte-identical to the filed addendum results:
  Step 1 equality holds, all 47 loci reproduce, the 41
  witness-covered loci keep their corrected
  classifications (filed-vs-corrected diff empty), and
  the corrected Step 4 table is as filed. (The filed
  script hardcodes the repo path of the clone it was
  executed in, `sw103-addendum`, since deleted; the
  Stage 2 executor stages the two input files at that
  path from this clone, runs the script, and removes
  the staging. The script itself is not edited.)

## 3. Identification of the eight texts (TC-103-13: PASS, with annotations)

Every identification was verified on the rendered page
image of the custody PDF: the entry head, the REM
number, and the "Désignation originelle" line read off
the page, not the OCR layer. Plate pages were also
inspected for all eight entries.

| Text | REM | Tome, chapter | Notice page (edition / PDF) | Plate page (edition / PDF) |
|---|---|---|---|---|
| Sh. 9 | REM 0376 | I, ch. 3 Karanog et Shablul | 691 / 692 | 690 / 691 |
| Sh. 16 | REM 0383 | I, ch. 3 | 705 / 706 | 704 / 705 |
| Meroe 40 | REM 0440 | II, ch. 5 Inscriptions de Méroé | 797 / 84 | 796 / 83 |
| F.O. 7 | REM 0557 | II, ch. 6 Ostraca de divers sites | 929 / 216 | 928 / 215 |
| F.O. 17 | REM 0567 | II, ch. 6 | 949 / 236 | 948 / 235 |
| F.O. 29 | REM 0579 | II, ch. 6 | 973 / 260 | 972 / 259 |
| F.O. 39 | REM 0589 | II, ch. 6 | 993 / 280 | 992 / 279 |
| B.O. 1 | REM 0591 | II, ch. 6 | 997 / 284 | 996 / 283 |

Annotations against the registration's table, filed
here per TC-103-13: (1) REM 0440's chapter is ch. 5
(Inscriptions de Méroé), not "ch. 4" as the
registration's table labelled it — a label error only;
the entry, tome, and pages were correct. (2) The
registration's page column named the notice page; each
entry's plate page (the preceding page) is now filed
above. (3) B.O. 1's identification is confirmed
directly on its notice page ("Désignation originelle:
B.O. 1"; Buhen, nine fragments of a red ostracon found
west of the South Temple), not only by sequence.

## 4. What the REM carries for these texts, and why it is not the registered witness

Per-entry plate contents (from the witness data file):
Sh. 9 — photograph (Randall-MacIver et Woolley 1909,
pl. 34) and Griffith 1911a's hand copy (p. 178).
Sh. 16 — photograph (1909, pl. 37) and Griffith 1911a's
hand copy (p. 180). Meroe 40 — photograph and hand copy
(Garstang, Sayce et Griffith 1911, pls. LVII,3 and
LXXII). F.O. 7, F.O. 17, F.O. 29 — Ashmolean Museum
photographs only. F.O. 39 — Ashmolean photograph and
Griffith 1925a's facsimile (pl. XXIX,4). B.O. 1 —
Griffith 1925a's facsimile (pl. XXIX,1) only.

The Stage 2 registration (§4.2) defines the witness as
the transliteration printed in the REM entry,
transcribed from the rendered page. No such
transliteration exists for any of the eight entries, so
there is nothing to transcribe and no witness verdict
can be formed. For the two decision-bearing texts the
point is sharper: the plates' hand copies are Griffith
1911a's own — the very publication whose transliteration
the build's extraction carries for Sh. 9 and Sh. 16.
The REM, for these texts, is a repertory that catalogues
and reproduces the original publication; it does not
re-read the inscriptions, and it supplies no token
stream independent of the extraction's own source.
Reading Griffith's hand copies sign by sign would be a
different instrument — a sign-level re-reading with its
own protocol and error treatment — not the witness this
registration names, and under spec.md §6 it would be a
new registration, not a mid-check substitution. It is
not performed here. The notices' descriptive name
readings (for example "Sidokeneye" for Sh. 9, "Se.m.tsi"
for Sh. 16) are not transliterations of the texts and
bear on none of the six loci, whose tokens are the
formula words soreyi / asoreyi / wosi.

## 5. The six loci under the completed witness set

Classified by the corrected checker
(`conformance-addendum-script.py`, SHA-256 `070a5c4d…`,
imported unchanged) with the Stage 2 witness set, in
which the REM verdict set for Sh. 9 and Sh. 16 is empty
because no REM transliteration exists:

| Form | Kind | Text (REM entry) | Token | Stage 1 | Stage 2 |
|---|---|---|---|---|---|
| asoreyi | counted | Sh. 9 (REM 0376) | asoreyi | WITNESS UNAVAILABLE | WITNESS UNAVAILABLE |
| asoreyi | near, edit distance 1 | Sh. 16 (REM 0383) | soreyi | WITNESS UNAVAILABLE | WITNESS UNAVAILABLE |
| soreyi | counted | Sh. 16 (REM 0383) | soreyi | WITNESS UNAVAILABLE | WITNESS UNAVAILABLE |
| soreyi | near, edit distance 1 | Sh. 9 (REM 0376) | asoreyi | WITNESS UNAVAILABLE | WITNESS UNAVAILABLE |
| wisi | near, edit distance 1 | Sh. 9 (REM 0376) | wosi | WITNESS UNAVAILABLE | WITNESS UNAVAILABLE |
| wisi | near, edit distance 1 | Sh. 16 (REM 0383) | wosi | WITNESS UNAVAILABLE | WITNESS UNAVAILABLE |

The completeness scan (registration §4.5) is vacuous:
there are no REM token streams to scan, and the
extraction-side census stands exactly as filed. No
adjudication arises; no token is corrected; no variant
is pooled (TC-103-15: PASS). TC-103-14 is NOT
APPLICABLE: no locus classification rests on a REM
token, because none exists.

## 6. The six-form table, restated whole

Counts are the control-verified corrected Step 4
counts of the conformance addendum (§2); Stage 2
changes none of them.

| Form | Frozen (texts, share) | Corrected (texts, share) | Outcome |
|---|---|---|---|
| soreyi | 10 texts, share 1.0, PASS | unchanged | **CLAIM STANDS** |
| asoreyi | 2 texts, share 1.0, FAIL | unchanged | **NOT CHECKED — INCOMPLETE COVERAGE** |
| xolkete | 7 texts, share 0.714, PASS | unchanged | **CLAIM STANDS** |
| pxolkete | 3 texts, share 1.0, PASS | unchanged | **CLAIM STANDS** |
| xolkte | 3 texts, share 1.0, PASS | unchanged | **CLAIM STANDS** |
| wisi | 9 texts, share 1.0, PASS | unchanged | **CLAIM STANDS** |

Kill check (spec.md §3.5, the session's verbatim):
Stage 2 demonstrates no source/extraction discrepancy
at any locus, so the claim is not killed for any form.
For asoreyi the check returns NOT CHECKED — INCOMPLETE
COVERAGE, not verified absence: the held witnesses
still cannot exclude the least-favourable resolution
of Sh. 16's soreyi token, and the input-error
explanation of asoreyi's failure is not retired. The
five CLAIM STANDS outcomes stand on Stage 1 and
addendum evidence, control-verified here; they are not
re-derived from any new witness.

## 7. What would settle asoreyi, and the state of the REM route

The REM route is closed for Sh. 9 and Sh. 16 on this
record: the edition of record has been held, inspected
entry by entry, and found to carry no transliteration
witness for either text. Two routes could still settle
the two loci, neither commissioned by this stage and
neither started here: (a) a separately registered
sign-level re-reading of the monuments (Philadelphia
5108 and 5116) or of the published plates, with its own
reading protocol, uncertainty treatment, and
registration before any reading is taken; (b) a modern
re-edition of the two texts that prints a
transliteration, acquired and witnessed under a new
registration. Until one of those exists, asoreyi's
Spec 103 outcome remains NOT CHECKED — INCOMPLETE
COVERAGE, and Spec 097's frozen Stage 4.4 outcome
(1 PARTIALLY SUPPORTED, 5 UNSUPPORTED) stands exactly
as filed, unreopened by this check (C103-4;
TC-103-16: PASS).

## 8. Provenance

Registration commit `25cbf825` precedes this execution
in the branch history (TC-103-11: PASS). Venue:
tower-compute, fresh clone
`~/.syncyard/worktrees/glossa/sw103-stage2`. The
executor prints timestamped progress lines with step
counters as it runs; its payload verdict line reads:
"STAGE 2 EXECUTED - asoreyi NOT CHECKED - INCOMPLETE
COVERAGE (witness held, no transliteration in the
edition for Sh. 9 / Sh. 16); five forms CLAIM STANDS
unchanged; kill check not fired", exit 0. The
transfer-learnings mechanism note directed by the
commissioning order is filed as
`records/stage-2-mechanism-note-2026-11-26.md`.

**AI disclosure:** executed by an AI agent (Muse, via
Muse) at the direction of Tristen Pierson, per
constitution sec. VI.
