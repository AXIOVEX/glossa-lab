# Co-scientist Sweep (Round G) 2026-11-25 — Adjudication

**Date of adjudication:** 2026-11-25.
**Programs:** Indus (Spec 091/098/099/100 line), Spec 096
(Eteocypriot), Spec 097 (Meroitic); the round's two findings
reach the Round F adjudication record (Spec 091) and the
Spec 106 Meroitic baseline template.
**Filed under:** the Glossa-Lab loop's standing discipline
(owner directives 2026-11-21 and 2026-11-22, loop expanded
2026-11-24, reaffirmed 2026-11-25): Co-scientist findings are
filed as artifacts and answered on the record; every
recommendation is logged once in
`records/coscientist-recommendations-ledger.md` with its
adjudication status; no standing, verdict, or tally changes
on a Co-scientist round alone.

## 0. Inputs and method

Three Co-scientist sessions, one per program — the Round D
sessions, continued through Rounds E and F — fired
2026-11-25 ~19:13–19:21 ET through the tower-compute
automation Brave route. Round F published nothing, so no
post-publication wait ran for this round (Round F
adjudication §6); the first send of this round (~19:13 ET)
also falls after the Round E wait's expiry (~19:03 ET) in
any case. Each brief was sent verbatim from its filed
`MESSAGE.md`; the composer text was verified byte-for-byte
against the filed brief (character length and FNV-1a
checksum) before each send, because the composer ignores
programmatic fill until a genuine keystroke lands, and
each send invocation re-verified the composer before
clicking Send. One capture-method note: in the Eteocypriot
pass, a first fill verified in its own invocation did not
persist into the next (the composer reverted to the single
genuinely typed space, Send still disabled); the brief was
re-filled with the keystroke step in the same invocation,
verified there (length and checksum exact, Send enabled),
and re-verified again inside the send invocation before
the click. No unverified text was sent in any session.
Captures are filed at the goal's
`hidden_files/coscientist-sweep-2026-11-25-round-g/<program>/`
(`MESSAGE.md`, `OUTPUT.md`, `SESSION-RAW.json`,
`CAPTURE-NOTE.md`, `STAGING-NOTE.md`, plus the sessions'
own output files where written).

- **Indus:** session `192b25f3-cb7b-46b4-acfa-1c1eea4e41fb`.
  Brief SHA-256
  `334c6e9309b8a2e470d6e9f803303f8f9d6d6f6abc6be6d3efc744b297176dd4`
  (composer verification: length 8463, FNV-1a `8f175d59`);
  OUTPUT.md SHA-256
  `e83bbc0d90f1be7a2fa500f93b37be1c1088be9d15b8331fada4e578fd72ccc0`;
  SESSION-RAW.json SHA-256
  `a13bdd72316e1f1418feb5aa3027a3d545defeca7ce79e848ba8d3a9ebe20f5c`.
  The session wrote no output file.
- **Eteocypriot:** session
  `1828e4db-cc7b-434a-891a-12aca9ad1b8a`. Brief SHA-256
  `d0c51d610f3f3a75fda946a29c45095432653cbd195f7462edfb87b9ed2f89b8`
  (length 11113, FNV-1a `b72d42d6`); OUTPUT.md SHA-256
  `3c4006600057e935f2bd7ab01d1972559f001a78d9979c11fc628fee15c6d7eb`;
  SESSION-RAW.json SHA-256
  `82c48c382b4d627c67d77cea8cd19e2d1ac4ae6497b8460f042e12cc912f010d`.
  The session also wrote `eteocypriot-round-g-review.md`
  (SHA-256
  `83956ca334c326b78c56f5cb2b092ab0ac237db7abd3e5675ab1183c14b2c517`),
  captured in full in the goal folder.
- **Meroitic:** session
  `11cac4f7-f109-4fac-bbb5-c670eb33b291`. Brief SHA-256
  `450c2fbee64aabde3e25f2af5a29e1b4d6c18385b00841620269a372b9449a4a`
  (length 14664, FNV-1a `1ef1e84c`); OUTPUT.md SHA-256
  `6b0351ad1439b27ff9784373b8473abc382418a9b8f7f1a83e47f8a5e03b1367`;
  SESSION-RAW.json SHA-256
  `7e31434d6f0b02c10253fcbfec1c275fc4c2f25de01f8d3252001d8452cc2c72`.
  The session also wrote `meroitic-round-g-2026-11-25.md`
  (SHA-256
  `18d2363eabdf5170ebc73fb0f98eca0efb7bceae8d614d9f03918bd72d5c3235`),
  captured in full in the goal folder.

Each session's working tab was closed once its captures
were verified (owner tab discipline). Adjudication was
against the primary record: the deposited v4 papers
(Zenodo records 24545017 / 24545036, timestamps read from
the Zenodo record API at adjudication), the repo records
at head `14e815b5328d3ff2535f39a9c205f8d02035f393`, and
the ledger. Every quantitative or textual claim in the
round was independently recomputed or re-read before
adjudication:

- **G-E-1 (chronology):** the Spec 096 release record's
  v4 addendum (§2.1 below), the Round F adjudication §0
  dispatch range, the Round F capture notes' per-session
  send times, and the Zenodo API creation timestamps were
  each read directly; the waiver kill check was run as a
  search over the repository, PROGRAM-STATE, and the
  Round F records (§2.1).
- **G-M-1 (baseline chronology):** MER-ENV-01, MER-ENV-03,
  and MER-MOV-08 were read verbatim in the template at
  head `14e815b5`; the session's quotations are exact.
  The kill check (a binding scope rule confining
  MER-ENV-01 to a kingdom-period subset, or a declared
  interpretation placing REM 0094 outside MER-ENV-01's
  language claim) was run against the template, the
  framework, and the study records (§3.1). The amendment's
  axiom-line hash was recomputed by the method of
  `specs/106-elsewhere-world-model-templates/records/census-audit.py`,
  which first reproduced the filed version 1 pin exactly
  on the unamended file and passes in full on the amended
  file (§3.1).
- **Live-record advance:** while this round ran, the
  Spec 103 conformance addendum landed (PR #743, merged
  2026-11-26T00:20:48Z), moving row E-M-1 to done. The
  Meroitic session detected the advance from the live
  record and reported it (§3.2); the briefs' E-M-1 status
  line was accurate at dispatch and is superseded on the
  record by that landing, not by this round.

**Standing consequence statement: no standing, class,
verdict, or tally moves on this round.** The standings
remain 3 E + 66 I + 4 R + 3 P + 18 U = 94 (Indus); the
Spec 096 verdicts stand (C096-1 NOT SUPPORTED, C096-2 TOO
THIN, C096-3 NOT ENGAGED, C096-4 SUPPORTED in narrowed
form); the Spec 097 Leg A tallies, Stage 4.2 UNDECIDABLE
AT THIS POWER, and the Stage 4.4 bounded PARTIALLY
SUPPORTED stand; Spec 103's CLAIM STANDS outcome and its
six-form table stand, with its conformance addendum
complete under PR #743. The round's two units are a
loop-chronology correction and a baseline-template
consistency correction; neither is new evidence about any
language, and no paper item arises anywhere in the round.

## 1. Indus — no units advanced

The session returned a null: "Round G verdict: fourth
consecutive null." No new recommendation, and no settled
row challenged. Its reasoning, in substance: the only
delta since Round F is framework-internal (the §8.2
clarification, which produces no Indus result with no
instance spawned and does not itself justify commissioning
an instance, and the opening of Spec 106's history
ledger, which adds traceability, not evidence); neither
development exposes a demonstrated error in a settled
item; the next substantive advance still requires
discriminating evidence the program does not have, and
the already-recorded directions and uncommissioned
sandbox stages are not to be repackaged as new
recommendations.

The session disclosed that this is a brief-level
assessment (no independent inspection of the deposited
paper, specifications, execution artifacts, or full
ledger in this turn). The null is therefore accepted and
recorded as a **brief-level assessment**, exactly as
Rounds D, E, and F recorded theirs. Per the Round D
adjudication §1 pattern, a null round adds no row to the
recommendations ledger. No paper item arises; no Indus
v13 is prepared.

## 2. Eteocypriot — 1 unit

The session worked at direct-inspection level: it pinned
the repository at `034535d9` (the head at its dispatch;
the record has since advanced to `14e815b5` by PR #743,
which does not touch its finding), read the delta since
Round F (the Round F adjudication and history records
and framework §8.2), and re-downloaded the deposited v4:
byte-identical to the file read in Round F (MD5
`4b4621c2aac519db637d3958e9ecae38`, SHA-256
`f3f6a343d2f9646ea0a5c6bbf9ff8e93434eb1e77159251c49c6522044fcaa71`),
confirming that §8.2 closes the F-M-1 counterexample and
that no other delta item carries an Eteocypriot
consequence. It advanced one unit:

### 2.1 G-E-1 — Round F's dispatch preceded the registered post-publication wait's expiry, with no waiver on file: APPLY

Sustained on the filed record, with all three of the
session's advance kill checks run at adjudication and
none met:

- **The wait and its anchor.** The Spec 096 release
  record's v4 addendum states: "Loop wait: the 1 hour
  post-publication wait runs from the Zenodo publication
  of 2026-11-25 (~23:03Z, 18:03 ET). Round F falls due
  after ~19:03 ET." The Round E adjudication §7 repeats
  the deadline. The Zenodo record API, read at this
  adjudication, returns created
  `2026-11-25T23:03:59.668929+00:00` for record 24545017
  (Eteocypriot v4) and `2026-11-25T23:04:27.840086+00:00`
  for record 24545036 (Meroitic v4), corroborating the
  release record's anchor; the wait therefore expired at
  ~19:03–19:04 ET.
- **The dispatch.** The Round F adjudication §0 records
  the three briefs fired "2026-11-25 ~18:46–18:48 ET";
  the Round F capture notes record the per-session sends
  at ~18:46 ET (Indus), ~18:47 ET (Eteocypriot), and
  ~18:48 ET (Meroitic); the Co-scientist history ledger
  repeats the range. Dispatch was therefore ~16–18
  minutes before the wait expired.
- **Kill check (a), an authenticated later send time:**
  not met. The capture notes are the program's send
  records; they agree with the adjudication record, and
  no later authenticated send time exists anywhere in
  the captures.
- **Kill check (b), a prior waiver or a different
  authorized gate definition:** not met. A search of the
  repository for "waiver" returns only the Spec 104 /
  E-E-1 material (a different instruction, a different
  event); PROGRAM-STATE and the Round F records contain
  no waiver of the wait and no alternative gate
  definition; the loop's governing text (owner directive
  2026-11-24) gates the next round on the hour's expiry
  from publication, with no exception recorded for
  Round F.
- **Kill check (c), an authoritative earlier publication
  receipt:** not met; the Zenodo timestamps above
  corroborate the release record's ~18:03 ET anchor
  rather than displacing it.

**Disposition: APPLY.** The discrepancy the session
flagged is real, and on the checks above it is an
unwaived departure from the loop's registered wait rule
in Round F's dispatch. It is recorded without
retroactive ratification as a dated addendum (§7) to
the Round F adjudication record, filed with this
adjudication, and carried in the Co-scientist history
ledger's Round G entry. Scope, as the session bounded
it and adjudication confirms: the departure is one of
loop timing only. Round F published nothing; its one
unit (F-M-1) is a framework clarification whose validity
does not depend on dispatch timing; no standing,
verdict, tally, or paper is affected; no rerun of
Round F is warranted or proposed, and the wait it
concerns has long since elapsed. This round's own
dispatch observes the rule (§0). Row G-E-1 stands
**done** at this landing, its act being the §7 addendum
(the Round E/F precedent for record-act units). No paper
item arises; no Eteocypriot v5 is prepared.

## 3. Meroitic — 1 unit

The session worked at direct-inspection level: it read
the deposited v4 afresh (SHA-256 `12034315…`, identical
to the filed value), the framework including §8.2 (F-M-1
confirmed discharged), the Meroitic baseline, the study
records, and the ledger at pin `14e815b5`. It advanced
one unit:

### 3.1 G-M-1 — the Meroitic baseline's MER-ENV-01 contradicts its own MER-ENV-03 / MER-MOV-08 on the end of Meroitic writing: APPLY

Sustained on the template text at head `14e815b5`. The
session's quotations are exact:

- MER-ENV-01 (K): "The Meroitic language was written
  **only during the Kingdom of Meroe, c. 300 BCE –
  350 CE**, though the language itself is attested
  earlier in Egyptian transcriptions of personal names
  from as early as the second millennium BCE."
- MER-ENV-03 (K): "The script outlived the fall of Meroe
  (c. 350 CE): the latest known text is the inscription
  of the Blemmye king Kharamadoye at Kalabsha
  (REM 0094), re-dated to 410/450 CE."
- MER-MOV-08 (K): "the last Meroitic text is in fact a
  Blemmye king's inscription (see MER-ENV-03)" — which
  forecloses reading the Kalabsha inscription as merely
  another language in Meroitic characters.

The kill check was run at adjudication: no binding scope
rule in the template, the framework, or the study
records confines MER-ENV-01 to a kingdom-period subset
(the template's Frame line describes the corpus's
predominant span; it does not scope the axiom, whose own
text is unqualified), and no declared interpretation
places REM 0094 outside MER-ENV-01's language claim;
MER-MOV-08 points the other way. The check is not met.
The defect is an input inconsistency between two (K)
lines of a spawn-ready baseline, not a dispute between
rival hypotheses: an instance treating MER-ENV-01 as an
exclusive temporal constraint would exclude what
MER-ENV-03 requires it to admit. No instance has run,
so no derivation or result is affected; the correction
is cheapest now, before first instantiation (the E-M-3 /
F-M-1 posture).

**Disposition: APPLY.** The correction is filed with
this adjudication as version 2 of
`templates/meroitic-baseline.md`: MER-ENV-01 now reads
"Meroitic writing is attested during the Kingdom of
Meroe, c. 300 BCE – 350 CE, and continued after its fall
(MER-ENV-03); the language itself is attested earlier in
Egyptian transcriptions of personal names from as early
as the second millennium BCE", with its source unchanged
(Rilly 2016). The template's seed record stands as filed
for version 1 (the seed may not change); a Template
amendment section after it records the superseded line,
the reason, and the new pin, and an iteration entry
stands in the study's seed-and-iteration log. Census
unchanged (76 axioms; (F) 4, (K) 62, (H) 10; UNSOURCED
lines 2); the axiom-line SHA-256 moves from the version 1
pin `eeadf46e336fa80d09bcffa2538d3cf4c32c8756fdb6150c817ff0b19cdb4cf4`
to `ecabd227f7e767a3a740ece3b355d8620db476b89ac482d7a8386b483a97f4f2`,
recomputed by the census-audit method (which reproduces
the version 1 pin exactly on the unamended file and
passes TC-106-02, TC-106-03, TC-106-04, and TC-106-05 in
full on the amended file). Row G-M-1 stands **done** at
this landing. No paper item arises (the deposited v4
does not carry the baseline text); no Meroitic v5 is
prepared. One immaterial blemish in the session's own
file is noted for the record: its assessment header
dates the brief "25 November 2026"; the brief is of
2026-11-25, and the file is captured as written.

### 3.2 The live-record advance (E-M-1), as the session reported it

The session found E-M-1 done on the live record (the
Spec 103 conformance addendum, PR #743, merged while
this round was in flight) and reported it as a state
update, not a unit. Its corroboration, recorded as the
session's own work and not as a program execution: it
independently ran the addendum's ten filed synthetic
regression tests against the filed addendum script
(10/10 passed; both Round E counterexamples return the
corrected outcomes) and checked the filed replay
aggregates (14 counted and 33 near-form loci, zero
control mismatches, zero changed classifications, the
six-form table unchanged; 25 witness objects, zero
carrying the registered markup characters) against the
addendum outcome record, finding them consistent; it
did not inspect the custody-held witnesses. Its recount
of the live ledger (126 rows — 74 done, 31 accepted,
0 open, 21 rejected; Meroitic 52: 25 done, 15 accepted,
12 rejected) agrees with the ledger at pin `14e815b5`.
No act arises for this round from the advance; the
addendum's own records govern it.

## 4. Owner decisions arising

None requiring a decision this round. Both units are
corrections to the program's own records (a loop
chronology entry and a baseline template amendment
using the template's own declared chronology); neither
proposes new paper text, a new acquisition, or a change
to any result (the E-M-3 / F-M-1 precedent). The Round F
wait-rule departure is recorded as a fact of the record
under G-E-1; it is not retroactively ratified, and no
result depends on ratifying it.

## 5. Tallies

Two units: 2 APPLY (G-E-1, G-M-1), 0 APPLY WITH
MODIFICATION, 0 DO NOT APPLY, 0 carried to owner
decisions. Indus: null, no row.

Ledger after this landing: **128 rows — 76 done, 31
accepted, 0 open, 21 rejected**, recounted from the data
rows. The pre-round position (after PR #743) was 126
rows — 74 done, 31 accepted, 0 open, 21 rejected. Round
G adds two rows (G-E-1 and G-M-1, both done at this
landing, their acts filed with it).

## 6. Round H timing

Nothing was published in this round: no new version of
any paper was prepared or deposited, so no
post-publication wait runs. Under the loop's standing
definition, **Round H falls due immediately**.

**AI disclosure:** this adjudication was executed by an AI
agent (Muse, via Muse) at the direction of Tristen
Pierson, per constitution sec. VI.
