# Spec 101 — Intake identity record (T101) — 2026-11-27

The C095-3 identity record for the Perna-side corpus
state intaken at Stage 1 of this study, executed under
Spec 107 cycle 1 (the owner's commission of
2026-11-26). The state lives at
`specs/101-eteocypriot-next-claim/corpus/corpus.json`.
It is a new corpus state under this study's own
directory; no Spec 096 file was edited.

## Identity

- corpus_id: `eteocypriot-perna-2019-ics194-195`
- version: 1.0.0
- Corpus file SHA-256:
  `9535108dfcbd93adb6b10ba8c2ca40cfd7a5710b02bb45f1c5768f00a54a631c`
- Per-inscription pins (SHA-256 over the canonical
  JSON serialization of the inscription object —
  sorted keys, separators (",", ":"), UTF-8):
  - ICS 194:
    `8a142eec3f885fe0d9d181a56149aad9ce8aea62599eba1aa6bd89ca7b407caf`
  - ICS 195:
    `0382b0ae00b2010f7f687c543a3feb6c80601e42e1f8fad86ae1050f4e835049`

## Provenance

- Edition of record: Perna 2019, "La grande
  inscription d'Amathonte (ICS 194 + 195): une
  nouvelle étude épigraphique. Rapport préliminaire",
  in *Cahiers du Centre d'Études Chypriotes* /
  BCH Suppl. 60, pp. 213–220.
  DOI 10.4000/books.efa.3031.
- Route: OpenEdition Books,
  https://books.openedition.org/efa/3031 (the
  program's held copy of the chapter).
- Transcription source: the chapter's printed
  plates of Perna's 2018 readings — plate image
  img-12 (ICS 194, Perna 2018) and img-14 (ICS 195,
  Perna 2018). The Masson 1961 plates printed
  alongside (img-11, img-13) are comparison only and
  are not intaken.
- Custody: `held_from_secondary_reproductions` —
  the state is a transcription of printed plates in
  a published chapter held by the program, not a
  collation of the stones.

## Transcription method and conventions

Transcribed sign by sign from the two Perna plates,
with zoomed crops for crowded lines; every line's
sign and segment counts were tallied independently
twice and reconciled before the state was built.
Conventions, as registered at Spec 107's cycle-1
registration §4:

- The printed separators `|`, `//`, `:` and the
  printed corner mark are segment boundaries.
- `_` is not a boundary; signs joined by it are
  recorded as printed, in one segment.
- Underlining is Perna's changed-reading flag. The
  sign counts at its printed value; the flag is
  recorded per sign index
  (`changed_reading_sign_indices`) and affects no
  count.
- `•` is one unread sign position. It counts in
  the sign census, and its segment counts toward
  M; it is no candidate's final sign.
- The ICS 195 line-2 group printed "XX II" is one
  segment of kind `numeral`; its signs (X, X, I, I)
  count in the census; its final sign is no
  candidate value (the capital labels are distinct
  from the syllabic sign labels).
- Typographic line wraps inside a numbered line
  are joined.

## Census of the intaken state

- Total: 331 signs, 84 segments; segment-final
  positions M = 84; unread positions 18.
- ICS 194: 104 signs, 33 segments, 4 unread
  positions, 2 changed-reading flags.
- ICS 195: 227 signs, 51 segments, 14 unread
  positions, 15 changed-reading flags, 1 segment of
  kind numeral.
- Changed-reading flags as transcribed: 17 sign
  positions. The chapter text states 48 changed
  sign readings against Masson 1961; the intake
  does not reconcile the two counts (the chapter's
  figure and the plates' underlining are not the
  same tally), and no count in this study depends
  on the flags.

## The stated-size difference, named

The chapter (¶35) and the program's earlier records
carry Perna's text as 216 signs. This intake's
transcription counts 331 signs. The difference is
named, not reconciled: Perna's counting convention
is not stated in the chapter (a count of a
restricted sign class, or of one face's edited
text, would each give a smaller figure), and the
registered design of this study does not require
the census to total any stated figure — M is
computed from the intaken census itself (M = 84
segment-final positions). The discrepancy is
recorded here so that no later record silently
equates the two counts.

## Spec 096 corpus integrity (C101-4)

- Spec 096 corpus file
  (`specs/096-eteocypriot-program/corpus/corpus.json`,
  version 1.1.1) SHA-256 before the intake:
  `2954283d6250803d25c98679174e2e534cb7a2c11e57b10711f9873198d23597`
- The same file's SHA-256 after the intake is
  computed and recorded in the execution landing
  (the intake writes only inside this study's own
  directory, so the value is expected identical;
  TC-101-01 recomputes both sides).
