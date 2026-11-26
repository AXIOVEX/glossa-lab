# Co-scientist Sweep (Round F) 2026-11-25 — Adjudication

**Date of adjudication:** 2026-11-25.
**Programs:** Indus (Spec 091/098/099/100 line), Spec 096
(Eteocypriot), Spec 097 (Meroitic); the round's one finding
reaches Spec 106.
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
2026-11-25 ~18:46–18:48 ET through the tower-compute
automation Brave route. Each brief was sent verbatim from
its filed `MESSAGE.md`; the composer text was verified
byte-for-byte against the filed brief (character length
and FNV-1a checksum) before each send, because the
composer ignores programmatic fill until a genuine
keystroke lands. Captures are filed at the goal's
`hidden_files/coscientist-sweep-2026-11-25-round-f/<program>/`
(`MESSAGE.md`, `OUTPUT.md`, `SESSION-RAW.json`,
`CAPTURE-NOTE.md`, `STAGING-NOTE.md`, plus the sessions'
own output files where written).

- **Indus:** session `192b25f3-cb7b-46b4-acfa-1c1eea4e41fb`.
  Brief SHA-256
  `53c506d730f5d31b474f448623152dae2a963f864d8b7a7912b828384b25e0a3`;
  OUTPUT.md SHA-256
  `66f0e4daa5b2efb9f9b79db5f4f11c6008483481c3f607cc28443cff83cbd2dc`;
  SESSION-RAW.json SHA-256
  `c5f91d926850ac3205831a0c84183c5f956f3e2f85c3eac387751a02311bd6f6`.
  The session wrote no output file.
- **Eteocypriot:** session
  `1828e4db-cc7b-434a-891a-12aca9ad1b8a`. Brief SHA-256
  `cbd6a32a36715c5b7ab17a149a632e0827f58b0d20c9a6377e7e750a05893a27`;
  OUTPUT.md SHA-256
  `a0b1e6b71f4990fe70fa08d5b59df82473d7cd59f87f21d7f30ad28a24003d82`;
  SESSION-RAW.json SHA-256
  `e11990b5855ab4b073431c87f4176c569c287b76c194054a2ced2a592c7c89f9`.
  The session also wrote `eteocypriot-round-f-review.md`
  (SHA-256
  `4f2b3f137617d6220ed5488dd26392f53a797fa190f18e612fd12f6958e61676`),
  captured in full in the goal folder.
- **Meroitic:** session
  `11cac4f7-f109-4fac-bbb5-c670eb33b291`. Brief SHA-256
  `2eb4f6a91c028259853d35d7f3a5e760c10ac1be1df78374b255ff98d9628bae`;
  OUTPUT.md SHA-256
  `8259ec360a67714c0f93863a5e278f43fac290159e0418eb73aefda80c4ffcc9`;
  SESSION-RAW.json SHA-256
  `82993231c0d2748ee8cbdc4eca5d7f40b9a1f40fdb52e2a3a77db20902d4425f`.
  The session also wrote `meroitic-round-f-2026-11-25.md`
  (SHA-256
  `a67e8c9eb19faecfa0312c0c34b87df9124f7c7be3ff80d47b661873805bd48b`),
  captured in full in the goal folder.

Each session's working tab was closed once its captures
were verified (owner tab discipline). Adjudication was
against the primary record: the deposited v4 papers
(Zenodo records 24545017 / 24545036), the repo records at
head `8088c06a`, and the ledger. Every quantitative or
textual claim in the round was independently recomputed
or re-read before adjudication:

- **Eteocypriot null:** the deposited v4 PDF was
  downloaded from Zenodo record 24545017 at adjudication:
  SHA-256
  `f3f6a343d2f9646ea0a5c6bbf9ff8e93434eb1e77159251c49c6522044fcaa71`
  (the filed v4 value) and MD5
  `4b4621c2aac519db637d3958e9ecae38` (the value the session
  states, and the checksum the Zenodo record itself
  publishes). The Spec 105 Stage 2 outcome record's
  Eteocypriot dataset hash (`2799d103…`) and L2 table
  (69 tokens, 35 marks, 18 singletons, top 5 = 21,
  top 10 = 36) match the session's independent
  reconstruction and recount exactly.
- **Meroitic checks:** the deposited v4 PDF was
  downloaded from Zenodo record 24545036 at adjudication:
  SHA-256
  `1203431526ba7eea9828e86941bea96e14f7e0b455c577df6755f041ee30aa81`,
  the value the session states and the filed v4 value.
  The Spec 105 Stage 2 outcome record's Meroitic table
  (32 marks, 29,843 tokens, top 1 / 5 / 10 = 4,484 /
  15,229 / 21,657, zero singletons) matches the session's
  independent sums.
- **F-M-1:** framework §§7–8 and the §8.1 clarification
  read verbatim at head (§3.1 below). The session's
  quotations are exact. Its kill check was run against
  §§7, 8, and 8.1 as filed: §8's condition 1 speaks of
  derivation "in every surviving instance", but §8.1
  declares itself governing the reading of §§7–8, and its
  positive row substitutes the translatable-survivor
  condition; no other filed text imposes a
  full-translation-coverage requirement on the positive
  row or restricts ROBUST-IN-ENSEMBLE to a translatable
  subset for SOLUTION purposes. The kill check is not
  met.

**Standing consequence statement: no standing, class,
verdict, or tally moves on this round.** The standings
remain 3 E + 66 I + 4 R + 3 P + 18 U = 94 (Indus); the
Spec 096 verdicts stand (C096-1 NOT SUPPORTED, C096-2 TOO
THIN, C096-3 NOT ENGAGED, C096-4 SUPPORTED in narrowed
form); the Spec 097 Leg A tallies, Stage 4.2 UNDECIDABLE
AT THIS POWER, and the Stage 4.4 bounded PARTIALLY
SUPPORTED stand; Spec 103's CLAIM STANDS outcome and its
six-form table stand. The round's one unit is a framework
finding about a rule registered before any scored
instance has run; it is not new evidence about any
language, and no paper item arises anywhere in the round.

## 1. Indus — no units advanced

The session returned a null: "Round F verdict: third
consecutive null." No new recommendation, and no settled
row challenged. Its reasoning, in substance: the Spec 105
Stage 2 execution adds a reproducibility result for the
sandbox's frequency tables (two implementations in
agreement on the recorded input), but matching
implementations verify the computation, not the input,
the mark segmentation, or any linguistic interpretation;
the frequency summaries describe the derivation set and do
not discriminate among proposed readings; the G-IND
baseline is a filed model, not an evaluated prediction,
and its zero filed mass outside the derivation inventory
is a conditional property the already-registered
unseen-mark gate stage exists to settle, so recommending
it again would duplicate registered work; and the sealed
reserve's existence still does not justify spending it.

The session disclosed that this remains a brief-level
assessment, not an independent inspection of v12, the
implementations, their outputs, or the full ledger. The
null is therefore accepted and recorded as a
**brief-level assessment**, exactly as Rounds D and E
recorded theirs. Per the Round D adjudication §1 pattern,
a null round adds no row to the recommendations ledger.
No paper item arises; no Indus v13 is prepared.

## 2. Eteocypriot — no units advanced

The session returned no new recommendation, challenged no
settled row, and proposed no verdict change — but unlike
the Indus null, this one rests on direct inspection, and
is recorded as a **scoped-audit null**:

- It read the complete deposited v4 PDF from the
  deposited record (checksum as verified in §0) and
  confirmed that p. 9 carries the canonical description
  in its amended form, including the clause whose absence
  was unit E-E-3; E-E-3's discharge on the deposited v4
  is confirmed by direct reading.
- It inspected the repository at the pinned commit
  `8088c06a2c79876d4d22b3294edbee08825ff038` and confirmed
  the Spec 104 outcome record's Round E adjudication note
  closes E-E-1 and E-E-2 as filed (pin-refresh instruction
  withdrawn; pin conjunct FAILED and matrix conjunct
  PASSED; continuation recorded as an unwaived departure;
  the analytical supplement in place).
- It independently reconstructed the Eteocypriot sandbox
  dataset from the two public development records under
  the filed strip rule: the reconstructed dataset hashes
  to the filed Spec 105 dataset hash, and its independent
  count and exact rational-frequency calculation
  reproduced every ordered row of the filed L2 table
  (§0). The check ran in the session's own review
  environment, not under Spec 105's commission; it is
  recorded here as corroboration of the filed Stage 2
  result, not as a program execution.
- It inspected framework §8.1 and found no Eteocypriot
  consequence (the Meroitic session's §8.1 finding is
  §3.1 below; it is a framework matter, carried there).

No row arises. No paper item arises; no Eteocypriot v5
is prepared. The session's stated falsifiers of its own
verification findings (a checksum mismatch, absence of
the amended quotation in the checksum-matching PDF,
absence of the supersession language in the pinned Spec
104 record, a source-pin or dataset-hash mismatch, any
differing count, fraction, or table order) were each run
at adjudication against the primary record and none was
met.

## 3. Meroitic — 1 unit

The session confirmed, by direct reading of the deposited
v4 (checksum as verified in §0), that p. 12 prints the
OD-C-5 summary credited as adopted 2026-11-23 superseding
the 2026-11-22 summary — E-M-2's discharge, already
recorded — and that §1 and §4.4 retain the M-P9 and M-P8
repairs, with no numerical tail ratios asserted in the
§4.4 caveat sentences, matching the Round E
brief-fidelity correction. Its independent sums of the
filed Spec 105 Meroitic L2 table match the filed values
(§0). It advanced one unit:

### F-M-1 — §8.1's positive row turns partial translation coverage into full-ensemble support: APPLY (narrow reopening flag on E-M-3, mixed-coverage case only)

Sustained on the framework text. Section 7's positive
reading is full-coverage: "The claim derives in every
surviving instance. It depends on no contested premise in
the varied set." The §8.1 clarification appended under
Round E unit E-M-3 — which declares itself governing the
reading of §§7–8 — states its positive row as: "At least
one survivor, and **every translatable survivor derives
the claim** → ROBUST-IN-ENSEMBLE (the SOLUTION gates of
§8 then apply as written)." Its coverage-failure row
covers only the case where *every* surviving instance is
UNTRANSLATABLE. The mixed case is therefore awarded the
full-ensemble label: in the session's two-instance
counterexample, instance A (carrying hypothesis H)
survives and derives claim C, while instance B (the
declared alternative to H) survives the evidence checker
but is UNTRANSLATABLE for C; no §8.1 row blocks the
positive row, so C is ROBUST-IN-ENSEMBLE although C was
never tested in B. Had B returned UNDERIVABLE instead,
the positive row would not have applied — losing the
ability to translate a claim cannot strengthen a
full-ensemble conclusion. The session's kill check (a
binding rule already requiring every survivor to
translate the claim before the positive row is eligible,
or an explicit restriction of ROBUST-IN-ENSEMBLE to the
translatable subset for SOLUTION purposes) was run
against the filed framework and not met (§0).

Scope, as the session bounded it and as adjudication
confirms: E-M-3's repairs of the all-UNDERIVABLE,
all-UNTRANSLATABLE, and zero-survivor cases are not
impeached by this finding and stand closed; the defect
is only the positive row's mixed-coverage case. No
instance has been spawned under Spec 106, so no result,
status, or tally anywhere is affected; the correction is
prospective, to the framework's rules, and is cheapest
now — the same posture as E-M-3 itself.

**Disposition: APPLY.** A dated clarification is
appended to the framework at §8.2 with this adjudication,
governing the reading of §8.1's positive row:
ROBUST-IN-ENSEMBLE requires at least one surviving
instance, the claim translatable in every surviving
instance, and the claim derived in every surviving
instance; mixed translation coverage returns no
full-ensemble status and is recorded in the iteration
log as partial coverage with both denominators
(surviving instances; translatable instances), any
translatable-subset result being reportable only as an
explicitly scoped subset result, never as
ROBUST-IN-ENSEMBLE and never SOLUTION-eligible for the
full-ensemble claim; the remaining §8.1 rows stand as
written. Row E-M-3 gains a dated annotation recording
this narrow reopening flag, carried here; its status is
not reopened, because the aggregation table it filed
stands for the cases it addressed and the open case is
exactly this unit's act (the Round E precedent: D-M-3
stands done, its narrow reopening carried at E-M-1).
This unit's row stands **done** at this landing, its act
being the §8.2 clarification filed with it (the Round E
precedent: E-E-1, E-E-2, and E-M-3 done at their landing).
No paper item arises; no Meroitic v5 is prepared.

## 4. Owner decisions arising

None requiring a decision this round. The round's one
act (F-M-1) is a clarification of the program's own
framework instrument, registered before any scored
instance has run, correcting a rule the program itself
wrote in Round E; it proposes no new paper text, no new
acquisition, and no change to any result. It is recorded
here as an adjudicated correction, not as an owner
decision (the E-M-3 precedent).

## 5. Tallies

One unit: 1 APPLY (F-M-1), 0 APPLY WITH MODIFICATION, 0
DO NOT APPLY, 0 carried to owner decisions. Indus: null,
no row. Eteocypriot: null, no row.

Ledger after this landing: **126 rows — 73 done, 32
accepted, 0 open, 21 rejected**, recounted from the data
rows. Round F adds one row (F-M-1, done at this landing)
and one annotation (E-M-3). Row E-M-1 remains accepted on
the Spec 103 conformance addendum, which this round does
not touch.

## 6. Round G timing

Nothing was published in this round: no new version of
any paper was prepared or deposited, so no
post-publication wait runs. Under the loop's standing
definition, **Round G falls due immediately**.

**AI disclosure:** this adjudication was executed by an AI
agent (Muse, via Muse) at the direction of Tristen
Pierson, per constitution sec. VI.
