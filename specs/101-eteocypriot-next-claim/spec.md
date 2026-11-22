# Spec 101 — Eteocypriot Next Claim: A Postdictive Occurrence Test of ICS 196 Ending Candidates in ICS 194/195 under Perna 2019

**Status: REGISTERED 2026-11-22 — NOT EXECUTED.** This
package registers the next Eteocypriot claim specified
under adjudication item OD-10 (E-8). Registration freezes
the claim, its preconditions, its success criteria, and
its independence assessment. No stage of the study has
run: no Perna-side corpus state has been built, no
candidate has been registered, and nothing has been
scored. Execution requires a fresh owner commission; it
is not authorized by this registration.

**Provenance.** The Co-scientist refresh adjudication of
2026-11-22 (PR #673;
`specs/091-anchor-comparison-integrity/records/coscientist-refresh-adjudication-2026-11-22.md`),
unit E-8, asked for a realistic next Eteocypriot claim
specified on verified holdings, with explicit success
criteria and an independence assessment; the owner's
OD-10 act of 2026-11-22 12:23 ET commissioned the
specification. The holdings it rests on were verified by
OD-9 (PR #682;
`specs/096-eteocypriot-program/records/od9-acquisition-2026-11-22.md`):
Perna 2019's re-edition of ICS 194/195 is openly readable
in full on OpenEdition Books. The derivation-completeness
precondition (P-3 below) answers the OD-8 audit's
finding F-4 (PR #681): freeze §5's R1–R3 underdetermine
the executed derivation, and amendment 2 §4 of the
Spec 096 outcome record already binds any future E1
re-run on a freeze containing the full table; this spec
generalizes that binding to its own machinery.

## 1. What this spec is

A single occurrence test. Spec 096 closed its E2 leg at
freeze (floor F-E2 NOT MET): the program held zero signs
of held-out continuous text against a floor of 100
legible signs. That state has changed in exactly one
respect — the held-out text's edition of record,
Perna 2019, is now lawfully readable in full (216 signs;
48 read differently from Masson, altering 24 words). It
has also changed in one respect that weakens the test
relative to the frozen design: the reading has been
*read*, by this program, before any candidate exists
(§3.3). This spec registers the strongest claim that
survives both facts: a **postdictive** occurrence test —
candidates registered from the development set alone,
then counted in the Perna text — with the exposure
stated on the face of the claim (C101-2) rather than
discovered later.

The research question: do the recurring endings the
ICS 196 development text actually contains recur, at the
positions the development text predicts, in the great
Amathus inscription under its edition of record? A yes
is a distributional fact about two texts. It is not a
translation, not a decipherment, and not evidence that
any ending's proposed meaning is correct.

## 2. The grounding, as measured at registration time

- **Development holdings (unchanged from Spec 096):**
  ICS 196 complete as transmitted, 11 segments, 54 signs
  (51 legible, 1 restored, 2 damaged), held from
  secondary reproductions; the Greek syllabic control
  excerpt (ICS 217, 66 signs); the Androkles dedications
  at zero Eteocypriot signs (the OD-10 intake was not
  executed — route barrier,
  `specs/096-eteocypriot-program/records/androkles-intake-record-2026-11-22.md`).
- **Held-out holdings:** ICS 194/195 form attestations
  only — 7 forms, 45 signs, keyed to Masson's readings
  through Duhoux 2009's discussion. The continuous text
  is not intaken.
- **Readable but not intaken:** Perna 2019 (BCH Suppl.
  60, pp. 213–220; DOI 10.4000/books.efa.3031), read in
  full on OpenEdition Books on 2026-11-22 under OD-9:
  the complete re-edition from autopsy, its reading
  printed at a glance at the chapter's end.
- **The floor arithmetic:** F-E2's floor was 100 legible
  signs of held-out continuous text. Perna's text, at
  216 signs, would meet the floor's size if intaken.
  The floor's other half — that the text be *unseen* —
  cannot be met (§3.3), and this spec does not pretend
  otherwise: it registers a different, weaker test
  instead of silently weakening the frozen one. Spec
  096's E2 stays closed exactly as frozen.

## 3. The registered design

### 3.1 Preconditions (all three, in this order)

- **P-1 — Intake with identity.** Perna 2019's reading
  of ICS 194/195 is intaken as a NEW corpus state under
  a new spec directory's corpus (never as an edit to
  Spec 096's corpus file), with a C095-3 identity
  record: per-inscription SHA-256 pins, provenance
  naming Perna 2019 as edition of record and the
  OpenEdition route, custody
  `held_from_secondary_reproductions`, and the
  transcription method stated. The Spec 096 corpus file
  must hash to its version-1.1.1 value
  (`2954283d…`) before and after the intake (C101-4).
- **P-2 — Candidate registration before scoring.**
  Recurring-ending candidates are derived from the
  ICS 196 development set alone, by a stated mechanical
  rule (a sign sequence recurring at segment-final
  position in at least two development segments, or an
  ending registered with its development occurrences
  enumerated), and the candidate set — each candidate's
  sequence, its predicted positions, and its occurrence
  floor — is committed to the repository BEFORE the
  Perna-side state is loaded by any scoring code. The
  registration commit's precedence over the first
  scoring run is a test case (TC-101-02), not an
  assertion.
- **P-3 — Complete tables.** Every derivation, stem
  table, or sign table any scoring run uses is written
  in full in the study's freeze addendum before the
  run. Where the E1 machinery is reused, the addendum
  reproduces the E1 driver's tables verbatim (the
  vowel map, the consonant stems, the ξ expansion, the
  diacritic and final-sigma handling, the R3 dead-vowel
  default) — the tables amendment 2 §4 and OD-8 F-4
  found missing from freeze §5 (C101-3).

### 3.2 The test

Each registered candidate is counted in the Perna-side
corpus state at its registered positions. A candidate
**meets its side** iff its occurrence count is at or
above its registered floor. The claim C101-1 is
SUPPORTED (at postdictive strength, §3.3) iff at least
one candidate meets its side; NOT SUPPORTED iff every
candidate is below its floor or absent. There is no
third outcome and no partial credit: a candidate whose
positions cannot be instantiated against the intaken
census closes the study as TOO THIN at its freeze,
in Spec 096's floor discipline, rather than being
scored on a weakened position set.

### 3.3 Independence assessment (E-8's requirement)

- **Textual independence: real.** ICS 194/195 is a
  different object and a different text from ICS 196.
  Candidates derived from ICS 196 alone are tested
  against material that played no part in deriving
  them; this is the one clean independence the design
  has, and P-2 exists to keep it clean.
- **Editorial dependence: real, and stated.** Perna
  2019 is a re-edition of the same stone Masson
  edited. The forms the program already holds derive
  from Duhoux's discussion of Masson. Agreement
  between the intaken Perna text and the held forms
  would not independently corroborate either edition,
  and no outcome of this study may be cited as doing
  so.
- **Exposure: the design's governing limit.** Perna's
  chapter — including the at-a-glance reading — was
  read in full on 2026-11-22 (OD-9) before this
  registration and before any candidate exists. The
  test is therefore postdictive: it can show that
  development-derived candidates are consistent with
  a text the program has seen; it cannot show that
  they predicted an unseen text. Every outcome record
  of this study carries the exposure statement
  (C101-2), and the claim's strength is registered
  here, in advance, as postdictive.
- **Why not the Androkles form.** A second E1 leg on
  the Androkles dedications would test the alignment
  procedure on a second bilingual; but the two
  dedications are related Amathus texts, not
  independent replications (the adjudication's E-7
  caution), and their syllabic sides are not held in
  any case (the OD-10 intake record). This study does
  not rest on them.

## 4. Hard limits

- No execution under this landing. Stages 1–4 of
  `tasks.md` are gated on a fresh owner commission.
- No external contact, no purchases, no external
  filing — Spec 096 §3's limits carry over unchanged.
- The Spec 096 freeze, its executed bytes, its corpus
  file, and its adjudicated verdicts are not modified
  by this spec or by any stage of this study.
- No standing is set by registration. Any ledger
  standing change for C101-1..C101-4 remains a recorded
  adjudication by a named human approver (Spec 096
  §2's route). Automated actors never approve, verify,
  or promote.
- Golgoi remains a separate stratum, never merged.

## 5. Decisions

- **D-101-1 — number.** At the check of 2026-11-22 the
  highest landed spec package on origin/main was 100
  (`specs/100-motif-claims-rerun/`); no 101 directory,
  branch, or open pull request carried 101. This
  package takes 101.
- **D-101-2 — claims.** C101-1..C101-4 (claims.md) are
  intaken at registration through
  `tools/ledger/import_bundle.py`, the only sanctioned
  path, inside this landing's PR, in the Spec
  096/098/099/100 pattern. Intake sets no standing.
- **D-101-3 — program-map placement.** The program is
  entered in `glossa-indus/map/program-map-taxonomy.json`
  under Program infrastructure / Governance, lifecycle &
  generated layers — the placement D-096-4 fixed for
  Spec 096, whose reasoning carries over: this study's
  claims are a separate target's and are not placed
  under an Indus claim family.
- **D-101-4 — the postdictive form.** The claim is
  registered in postdictive form rather than as a
  blind-prediction claim, because the blind form's
  precondition (an unseen held-out text) is false on
  the record (§3.3) and registering it anyway would
  repeat, in a new spec, the exact defect the
  adjudication exists to catch. If a genuinely unseen
  primary-stratum text is ever intaken, a blind
  successor claim is a new registration, not an
  amendment of this one.

**AI disclosure:** executed by an AI agent (Muse, via Muse)
at the direction of Tristen Pierson, per constitution sec. VI.
