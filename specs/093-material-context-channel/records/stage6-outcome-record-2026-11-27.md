# Spec 093 outcome record — closeout (Stage 6: T601, T602)

**Date:** 2026-11-27. **Spec:** 093 — the
material-context channel, a second projection for the
Indus record system, ratified as a block by the owner
2026-11-05 (decisions D-093-1..8). Stages 3–6 were
executed 2026-11-27 under the owner's commission of
that day ("Yes do all these things now or take my
approval now to do at the best time"); the history
ledger holds no commission record, so the filed spec
text was the only authority throughout, and each stage
was executed exactly as registered and recorded
against its registered rule before the next began.
This record closes the spec: per stage, what was
administered, accepted, or stopped, with counts
(T602), and C093-1's standing as it finally stands.
No claim's status, stage, or score was changed at any
stage (C093-13).

## 1. Per-stage outcomes

**Stage 0 — Ratification and adoption (2026-11-05).**
The block was ratified with its eight decisions; the
claims C093-1..14 were intaken into the ledger the
same day, after the Spec 089 machinery gap that first
held the intake was discharged (PR #532; the executed
intake is filed verbatim at Appendix A of the
ratification record).

**Stage 1 — Inventory, normalization, join
(2026-11-06).** Administered and accepted. The T101
census completed over the pinned snapshot; the T102
normalization register v1 covers all 1,122 distinct
material values; the T103 join was frozen before
computation and precision-audited on a hand-checked
sample: key K2 (CISI catalogue concordance) ACCEPTED,
179 pairs produced, 179 correct, precision 1.000
against the 0.90 floor (D-093-4). Coverage bound
stated on the record at the time: 179 of 3,085
text-bearing records (5.8%), one site (Mohenjo-daro).

**Stage 2 — Channel independence (2026-11-19/20,
closure qualifier 2026-11-21).** Administered under
successive freezes. Site and find context were formed
and administered; material class, artifact type, and
holding/provenance were NOT ADMINISTERED at the
stage's floors. Site was administered validly and NOT
RECOVERED (κ 0.0297 against the 0.80 recovery bar) —
under the freeze's §9 mapping to spec.md §5's
vocabulary, a validly administered non-recovery is
the independence result: the sequence does not
determine the field. Find context stood NOT YET while
its control batteries were invalid, and at freeze v3
(2026-11-20) its controls ran valid for the first
time and it likewise survived (κ̄ −0.0466, BĀ
0.1846), joining site in the surviving set. The
stage's verdict on C093-1 is in §2 below.

**Stage 3 — Comparanda register (2026-11-27).**
Administered and accepted. Register v1 filed: 4
entries (CR-093-01 the 14 seals in Mesopotamian
contexts, window 2334–1600 BCE; CR-093-02 the Meluhha
documentary record, 1,462 hits, 2500–1600 BCE;
CR-093-03 the Gulf/Dilmun Laursen Table 1 population,
121 rows, 2100–1750 BCE; CR-093-04 the Sumerian Ur III
and Akkadian receiving corpora, 2112–2004 BCE), each
with its comparanda set, transmission mechanism with
source, fixed window, and compared practice frozen
before any Stage 4 computation (H2). All 39 catalogue
corpora are accounted exactly once: 2 entered, 5 the
subject corpus, 32 annexed as not entered, no
mechanism of record. The four-element check passed
after a disclosed first-run failure on name-string
mismatches, corrected to the catalogue's verbatim
names. Record: `records/stage3-record-2026-11-27.md`
(PR #779; freezes PR #781).

**Stage 4 — First computed passes (2026-11-27).**
Record: `records/stage4-record-2026-11-27.md`
(PR #787).

- **T401 site pass: NOT YET.** Administered under
  freeze v1 over P-site (966 sequence-bearing site
  records: Mohenjo-daro 839 and Harappa 110 adjudged;
  Chanhu-Daro 7, Sutkagen-Dor 6, Lothal 3, Kalibangan
  1 below the 50-record floor, excluded and named in
  the freeze; arms Mohenjo-daro 587 discovery / 252
  held-out, Harappa 77 / 33). Runs
  study-20261127T095820Z-2c776c and
  study-20261127T095821Z-31eef3; independent audit
  AGREE. Q1 length (KS) fails freeze §6 clauses 1–3
  (discovery 0.0702 vs p99 0.1649; held-out 0.1281 vs
  p95 0.2146; direction +1 discovery / −1 held-out).
  Q2 sign choice (TV) meets clause 1 (0.3308 vs p99
  0.3285) and fails the held-out clause 2 (0.4288 vs
  p95 0.4456). Both pseudo-site controls behave. No
  re-administration under this freeze repairs a
  NOT YET (C093-8); nothing was accepted, and nothing
  is cited downstream at channel strength.
- **T402 material pass: CANNOT BE ADMINISTERED.** The
  join gate was met at Stage 1, so the stop is not a
  join failure. The freeze §4 census over the pinned
  join output (SHA-256 `7107f738…`) reproduces
  exactly: Steatite 176, Clay 1, Faience 1, 1 empty
  sentinel, 179 total — 1 class at or above the floor
  of 10 where at least 2 are required. No threshold
  was adjusted.
- **T403 contact administration: E1–E4 all MET.**
  Under CR-093-01 and CR-093-02 (machine record
  `records/stage4-contact-counts-2026-11-27.json`,
  SHA-256 `55a5fb2b…`): E1 14/14 find periods and
  12/14 excavation find spots (bar ≥ 12); E2 11/14
  outside the Indus region (bar ≥ 10); E3 11/14
  inscription-bearing (bar ≥ 10); E4 modal Meluhha
  period Ur III (850 hits) with 1,155 in-window hits
  (bar ≥ 1,000), the recomputation agreeing with the
  filed aggregates. The freeze §4's two bounded
  licensed statements are in force, with their
  bounds: n = 14 is an evidence class, not a
  population claim; the Meluhha counts describe the
  surviving textual record as rebuilt, not trade
  volume; and the Meluhha = Indus identification is
  the mechanism's premise, not proven.

**Stage 5 — Machinery extension (2026-11-27).**
Administered and accepted. Record:
`records/stage5-record-2026-11-27.md` (PR #789).
T501: taxonomy amendment as a new version
(program-map-taxonomy v2: the Material context
domain, this study's assignment moved to it,
same-motion copies per PROGRAM-MAP-DEFINITIONS.md
§8/§12, the conformance census pin moved as data);
the program map republished through the gated path;
the matrix republished byte-identical (14 family rows
of 1,073); gate full 32 PASS / 0 FAIL / 1 NOT-RUN,
regen 35 / 0 / 0. T502: gate class V12 (citation
existence, one-way flow, register-section counting
support), additive only, with a ten-test teeth
battery. A disclosed mid-motion refusal (the first
matrix publish refused while the published map still
carried the old grouping) is on the stage record.

**Stage 6 — Gap register and closeout (2026-11-27).**
T601: the GR-093 section is appended to the gap
register under its own section (D-093-5(a)) — 7
entries, §3 below — and the register's mechanical
completeness check counts it in this same landing:
the gate's V12 counting leg reads "7 GR-093 entries
counted in the culture-side section; every entry
carries what is not known, its candidate (acceptance
test), its falsifier, and its honesty type
(C093-12)", and the full gate at the extended profile
passes (full 32 PASS / 0 FAIL / 1 NOT-RUN; regen
35 / 0 / 0). One machinery fix landed with this
stage, disclosed here: the counting leg's entry
detection originally matched any line beginning
"GR-093-NN.", and the landed section's own text
exposed the case — a wrapped line inside GR-093-07
beginning with a cross-reference ("GR-093-05.") was
counted as an entry head and split that entry's
block, failing the leg. Entry headings now count
only at paragraph starts; a regression test
(wrapped cross-reference inside an entry) joins the
teeth battery, which stands at eleven tests. T602 is
this record and the report in §4; its acceptance test
(the recorded send matches this record) is discharged
by the send record filed after the send.

## 2. C093-1's standing, as it finally stands

**C093-1 stands INDEPENDENT IN PART for site and find
context.** Every citation of the standing carries the
closure qualifier of 2026-11-21 verbatim:

"Population: 179 joined pairs, all Mohenjo-daro;
single stratum; no cross-site inference."

Material class, artifact type, and holding/provenance
carry no independence standing: they were NOT
ADMINISTERED at Stage 2's floors, and Stage 4's
material pass stopped at CANNOT BE ADMINISTERED on
the forcing counts in §1. The two surviving fields
stand on validly administered non-recoveries (site at
freeze v1; find context at freeze v3, the first valid
controls) — the registered sense of independence
here: the sequence does not determine either field.
Stage 4's site pass returned NOT YET and changed no
standing. Nothing in Stages 3–6 raised, lowered, or
re-scoped the standing (H1).

## 3. The register as it now stands

The GR-093 section (`glossa-indus/map/gap-register.md`)
carries 7 entries, each with its four C093-12
elements: GR-093-01 the ductus / writing-style arm
(no field exists); GR-093-02 iconography (no coding
exists); GR-093-03 artifact typology beyond
seal/unknown; GR-093-04 period per record;
GR-093-05 the material join's residual coverage (179
of 3,085 text-bearing records); GR-093-06 the
material field's single usable class (named by
Stage 4's T402 outcome); GR-093-07 site coverage
beyond the two adjudged sites (named by Stage 4's
freeze and T401 outcome). Census of the section: by
kind, missing node 4, thin evidence 3; by status,
DATA-BLOCKED 5, UNMEASURED 2; by honesty type,
in-house re-derivation 7, independent confirmation 0.
The GR-088 census stands as ratified for its own 37
entries and is not rewritten. T601's own limit
stands: this does not establish that these are all
the culture-side gaps there are — only that every
entry carried is closable honestly.

## 4. The VEXA report (T602)

The outcome is reported to the VEXA chat in the
following words, exactly; the send is recorded in the
send record filed with this spec's records after the
send, and that record is T602's acceptance evidence.

---

Spec 093 (the material-context channel) is complete:
all six stages executed exactly as registered under
Tristen's 2026-11-27 commission, and the spec closes
with its outcome record filed at
specs/093-material-context-channel/records/stage6-outcome-record-2026-11-27.md
in AXIOVEX/glossa-lab.

Per stage: Stage 1 — census, normalization register
v1 (1,122 distinct material values), and the audited
join (K2 accepted: 179 pairs, precision 1.000 against
the 0.90 floor). Stage 2 — C093-1 INDEPENDENT IN PART
for site and find context; material class, artifact
type, and holding/provenance NOT ADMINISTERED.
Stage 3 — comparanda register v1 (4 entries,
CR-093-01..04; all 39 catalogue corpora accounted
exactly once). Stage 4 — T401 site pass NOT YET; T402
material pass CANNOT BE ADMINISTERED (one material
class at the floor of 10 where two are required:
Steatite 176, Clay 1, Faience 1 of 179); T403 contact
administration E1–E4 all MET, with its two bounded
evidence-class statements in force. Stage 5 —
program-map-taxonomy v2 (the Material context
domain) and gate class V12. Stage 6 — the gap
register's GR-093 section (7 entries, each carrying
its four C093-12 elements, counted by the gate) and
this closeout.

C093-1's standing as it finally stands: INDEPENDENT
IN PART for site and find context. Population: 179
joined pairs, all Mohenjo-daro; single stratum; no
cross-site inference.

No claim's status, stage, or score changed at any
stage (C093-13). The honest position is unchanged:
the channel is real but narrow — two of its five
fields carry independence standing, on a 179-pair,
single-site population — and the GR-093 entries name
what would widen it.

---

## 5. What this spec does not establish

This closeout is not the final word on the channel:
later joins, later data, and the reader stand after
it (T602's own limit). Nothing here is a decipherment
result, and no reading, sign value, or language claim
is made or strengthened by anything in this spec. The
channel's two surviving dimensions are independence
results over a 179-pair, single-site, single-stratum
population, and they are citable only with the
closure qualifier in §2.
