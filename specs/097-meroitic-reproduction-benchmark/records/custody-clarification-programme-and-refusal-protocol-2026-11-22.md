# Custody-Authority Clarification Programme and Refusal Protocol (Spec 097) — OD-14 Adopted

**Date:** 2026-11-22. **Program:** Spec 097 — Meroitic
Reproduction Benchmark. **Authority:** owner decision
OD-14 of the Co-scientist refresh adjudication of
2026-11-22
(`specs/091-anchor-comparison-integrity/records/coscientist-refresh-adjudication-2026-11-22.md`,
§5 unit M-7, §6 OD-14), **adopted by the owner, Tristen
Pierson, on 2026-11-22 at 13:12 ET**. This record drafts
and lands the two instruments OD-14 names: a
custody-authority clarification programme (§§2–3) and a
refusal protocol (§4), operative on adoption. **It
changes no verdict, no tally and no custody posture:**
the F-6 posture as restated in the citation-gloss
addendum of 2026-11-22
(`records/citation-gloss-addendum-2026-11-22.md` §4)
stands exactly as restated — retention permitted in
held custody, computation permitted, derived artifacts
aggregate-only, sharing paused, publication
aggregate-only with the custody caveat — and computation
and retention continue under the owner's risk
acceptance until a clarification or a refusal lands.
**No external contact is authorised by this record:**
every step in §3 that would contact a person is written
as a step only and is marked as requiring the owner's
explicit go naming the act and the destination when it
is reached.

## 1. Basis of record

The facts this programme works from, all from filed
records: the Otten corpus repository (pin
`c9158f6865325877112b6b9ceef83b3c80a93c56`) carries no
licence; the corpus is held under an **owner
risk-acceptance**, not a licensing finding and not the
rights holders' consent (custody record,
`records/custody-record-2026-11-20.md`); a permission
request was sent on 2026-11-20 to Joshua Otten
(jotten4@gmu.edu) and Antonios Anastasopoulos
(antonis@gmu.edu), George Mason University (Gmail
message id `1a1fb44214cf7994`), and stands **unanswered**
— silence is recorded as silence and is never treated
as permission. The objection undertaking of the custody
record §1, extended by the custody supplement of
2026-11-21 §2 as corrected by the custody erratum of
2026-11-21, names its objects: the benchmark outcome
record
(`records/meroitic-benchmark-outcome-record-2026-11-20.md`),
`records/leg-b-results.json`,
`records/leg-c-summary.json`, and citations of them.
The acquired corpus carries its own separate, licensed
basis (erratum §2) and is not Otten-derived.

## 2. The provenance and authority chain, element by element

Every element the program holds, examined, or derived,
with where it came from, the terms it is held under,
and what remains unclarified.

### Element 1 — the Otten corpus (the disputed element)

- **What:** the corpus repository accompanying Otten &
  Anastasopoulos (ACL Anthology 2025.alp-1.11), at pin
  `c9158f6865325877112b6b9ceef83b3c80a93c56`:
  mero-corpus.txt (18,090 lines — the paper's
  name-augmented training file, per the corpus
  completion record of 2026-11-20 §1), the
  Millet/Rilly/Lobban/Kalabsha example files, the seven
  bilingual dictionaries, and the published embeddings.
- **Provenance:** the authors' own public repository,
  taken at the pinned commit; the per-scholar example
  files descend from the named scholars' published
  materials as compiled by the authors.
- **Terms of holding:** no licence of any kind.
  Default copyright applies to the authors' compilation
  and code (custody record §1). Held in scratch custody
  on tower-compute; never committed to this repository;
  never redistributed.
- **Authority basis:** the owner's risk acceptance of
  2026-11-20, and nothing else. Permission requested
  2026-11-20; unanswered.
- **Unclarified:** whether permission will be granted
  at all; on what terms if granted; whether the
  authors' institution asserts any interest in the
  repository; and the standing of the underlying
  per-scholar materials as compiled. This is the
  element the clarification programme (§3) exists to
  resolve.

### Element 2 — the acquired corpus (licensed)

- **What:** MikeKovetsky/meroitic ("Meroitic with Opus
  5.5", 2026), pinned at commit
  `145af0836c071e7c9796d37d4b36add00d347c8a`, held on
  tower-compute at `~/glossa-work/meroitic-kovetsky-src`:
  396 inscriptions machine-readable under the open
  licence, 327 of them absent from the Otten corpus,
  with a 652-row REM-keyed inscription index and 488
  transcription data files (corpus completion record
  §2).
- **Provenance:** secondary transcription of Griffith's
  public-domain editions (*Meroitic Inscriptions* I–II,
  *Meroë*, *Karanòg*, 1911–12).
- **Terms of holding:** code MIT (`LICENSE`); data and
  write-ups CC BY 4.0 (`LICENSE-DATA.md`).
- **Authority basis:** the licences as filed. Clarified.
- **Unclarified / caveats:** transcription quality is
  the source's own measurement (95.6% sign accuracy
  against the modern edition on cursive type; 97.7% for
  the Karanòg material), carried as a quality caveat,
  not an authority gap. An Otten/Anastasopoulos refusal
  does not govern this element (custody erratum §2).

### Element 3 — examined, not acquired

- Zenodo "Meroitic Studies" I–III (records 1765414,
  2076873, 2332392; CC0): journal article PDFs —
  literature, not corpus data; not held as corpus.
- notofonts Meroitic fonts (OFL-1.1): typefaces, not
  texts; not held.
- Lackadaisical-Security/Meroitic-Script-Decipherment:
  licence NOASSERTION — no open licence granted; not
  acquired, and its logs would enter, if ever, as
  claims to test, not as corpus.
- Trismegistos Meroitic records: membership-gated;
  examined as a gap, not held.
- **Authority position:** nothing is held under this
  element, so nothing is unclarified. Any future
  acquisition from these sources is a new owner
  decision, not a step of this programme.

### Element 4 — absent material (named gaps, not custody)

The Ramses scrape material, the scanning-programme
material, and the Egyptian corpus text behind published
counts A3, A4 and A7 are **not held in any form**
(citation-gloss addendum §3). They are Leg A findings
(untestable for absence), not custody items: there is
nothing to clarify, retain, or withdraw.

### Element 5 — derived artifacts and citing records

- **The program's own code:** the program's own work;
  publishable without reference to Element 1.
- **Aggregate statistics** derived from Element 1:
  permitted in aggregate form only under the F-6
  restatement; no output may require redistributing
  Otten-derived text.
- **The undertaking's objects** (custody erratum §1):
  the benchmark outcome record,
  `records/leg-b-results.json`,
  `records/leg-c-summary.json`, and citations of them —
  Otten-derived derivatives already in this repository,
  governed on refusal by §4.
- **Freeze vocabularies and campaign records** insofar
  as they rest on Element 1 material
  (`records/freeze-v2-vocabulary-2026-11-20.json`,
  `records/freeze-v3-vocabulary-2026-11-22.json`, and
  the Stage 4 records citing corpus counts): derivative
  of Element 1's basis, governed on refusal by §4.
- **Authority position:** every derivative of Element 1
  inherits Element 1's unclarified state. That
  inheritance, stated here element by element, is what
  the refusal protocol's withdrawal and annotation
  duties attach to.

### Element 6 — copies and backups

The pinned Element 1 copy lives in scratch custody on
tower-compute. Executed runs have produced working
copies and run scratch on the same host. **The complete
inventory of copies — custody copy, working copies, run
scratch, and any backups — is not yet on the record**;
completing it is step 1 of the clarification programme,
because the refusal protocol's deletion duty (§4.3)
extends to backups and cannot be executed against an
unwritten inventory.

## 3. The clarification programme — ordered steps

The steps run in order. Steps 1–2 are internal record
work under this adoption. **Steps 3–4 contact persons
and are NOT authorised by this record: each requires
the owner's explicit go naming the act and the
destination when it is reached.**

1. **Complete the copy inventory (internal).** File, as
   a supplement to this record, an inventory of every
   copy of every §2 element: location, form, basis of
   holding, and — for Element 1 — the deletion route
   for that copy. Until this inventory is filed,
   Element 6 stands as the programme's one open
   internal item.
2. **Keep the permission watch live (internal).** The
   standing reply watch already reports any reply from
   the rights holders. A reply of any kind — grant,
   grant on terms, refusal, or a redirect to another
   authority — is filed by record promptly and moves
   the programme to step 5 or triggers §4, as its
   substance dictates. Continued silence continues to
   be recorded as silence.
3. **Follow-up to the rights holders (CONTACT — owner's
   explicit go required).** If the owner directs it, a
   single follow-up to Otten and Anastasopoulos
   restating the 2026-11-20 request, naming the held
   uses exactly as §2 Element 1 states them, and
   offering §4's terms in advance: on refusal, the
   disputed uses stop and the protocol executes without
   argument. Written as a step only; no send is
   authorised here.
4. **Institutional determination (CONTACT — owner's
   explicit go required).** If permission remains
   unresolved after step 3, seek a determination from
   the responsible institution — the authors'
   institution, George Mason University, through the
   office it designates — or from qualified counsel
   retained by the owner, as the owner directs
   (adjudication unit M-7's institutional route).
   Written as a step only; no approach is authorised
   here.
5. **Restate the posture on any clarification
   (internal).** A grant supersedes the risk acceptance
   for the uses it covers, on the terms it sets; terms
   narrower than the current posture apply from the
   date of the restating record; a grant covering only
   some uses leaves the rest under the risk acceptance
   or under §4, as its text dictates. The restating
   record is filed in the same motion as the reply is
   reported.

## 4. The refusal protocol — operative on adoption

**Trigger.** A refusal of permission, or an objection
to the held-custody use, from Otten, Anastasopoulos,
their institution, or a successor rights holder, in any
written form. On the trigger, the following execute
without waiting for further instruction, in this order:

1. **Stop.** All computation on Element 1 and on
   Otten-derived material stops immediately. All
   further citation of the benchmark verdict stops,
   except inside the withdrawal and annotation records
   themselves. Sharing is already paused under F-6 and
   remains paused; no redistribution occurs at any
   point, including during withdrawal.
2. **Review gate.** The disputed uses stay stopped
   pending review by the responsible institution or
   qualified counsel, as the owner directs (unit M-7).
   Nothing resumes on the program's own judgment, and
   no substitute data is introduced while the review is
   open.
3. **Withdraw and delete the corpus.** The pinned copy
   and every copy on the §3 step 1 inventory — custody
   copy, working copies, run scratch, and backups — are
   deleted or otherwise disposed of as the review
   directs. Deletion is verified copy by copy against
   the inventory, and the verification is filed by
   record.
4. **Derived artifacts.** The undertaking's objects —
   the benchmark outcome record,
   `records/leg-b-results.json`,
   `records/leg-c-summary.json`, and citations of them —
   are withdrawn, or annotated as withdrawn, in the
   same motion as the corpus withdrawal (custody
   supplement §2, as corrected by the custody erratum
   §1), and the §2 Element 5 derivatives are annotated
   the same way. It is stated plainly, as the
   supplement states it: git history cannot be
   retracted — prior commits remain in the repository's
   history, and this protocol governs the working
   record and all future citation, not the past.
   Aggregate statistics already published carry the
   refusal annotation; no new aggregate publication
   from Otten-derived material appears.
5. **Citing records.** Every Spec 097 record that cites
   the Otten corpus or its counts receives a dated
   annotation pointing to the refusal record, and the
   custody caveat sentence on those surfaces is replaced
   by the refusal statement.
6. **Preserve the audit record.** A non-infringing
   audit record is preserved where permitted: the
   program's own records and code, the inventory of what
   was held and what was deleted with its verification,
   and the fact and date of the refusal — containing no
   Otten-derived text (unit M-7).
7. **Rebuild only from authorised sources.** Affected
   analyses — the Leg A census over the Otten corpus,
   the freeze vocabularies, and Stage 4.2's inputs
   insofar as they rest on Element 1 — are rebuilt, if
   at all, only from independently authorised sources
   (Element 2's licensed corpus, or a later licensed
   acquisition), under a new freeze and a new record.
   Data is never quietly substituted under an existing
   freeze or verdict. An analysis that cannot be rebuilt
   from authorised sources stands withdrawn, not
   approximated.
8. **Timetable.** The stop (§4.1) is immediate on
   receipt of the trigger. The withdrawal, deletion,
   and annotation motions (§§4.3–4.5) complete within
   seven days of the trigger or on the timetable the
   §4.2 review sets, whichever the review directs. The
   refusal record — trigger, actions taken, deletion
   verification — is filed in the same motion as the
   withdrawal.
9. **Scope limit.** An Otten/Anastasopoulos refusal
   does not reach Element 2 (custody erratum §2): work
   on the acquired corpus continues under its own
   licences unless the refusal, by its own terms,
   reaches it — in which case §4 applies to the reached
   material in the same form.

## 5. Relation to the F-6 restatement — where this protocol extends it

This protocol sits under the F-6 restatement and does
not displace it: F-6 states what is permitted and
paused while permission is unresolved; this record
states what happens if the answer is no. Where §4
extends the restated posture, it is said explicitly:
F-6 and the custody record's undertaking state that on
objection the custody ends and the affected records are
annotated; §4 adds the operative mechanics F-6 does not
carry — **deletion of every inventoried copy including
backups, with filed verification (§4.3); the seven-day
timetable (§4.8); the review gate barring resumption
and substitution pending institutional or counsel
review (§4.2); the preservation of a non-infringing
audit record (§4.6); and the rebuild-only-from-
authorised-sources rule (§4.7)**. Those extensions are
the owner's by the OD-14 adoption and bind from
2026-11-22.

## 6. Adoption

Adopted by the owner, Tristen Pierson, 2026-11-22
13:12 ET, as adjudication item OD-14. The clarification
programme (§§2–3) and the refusal protocol (§4) are the
program's instruments of record from this filing. The
current posture does not change: computation and
retention continue under the owner's risk acceptance
until a refusal or a clarification lands.

**AI disclosure:** executed by an AI agent (Muse, via
Muse) at the direction of Tristen Pierson, per
constitution sec. VI.
