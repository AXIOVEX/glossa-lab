# Co-scientist Sweep (Round K) 2026-11-25 — Adjudication

**Date of adjudication:** 2026-11-25.
**Programs:** Indus (Spec 091/098/099/100 line), Spec 096
(Eteocypriot), Spec 097 (Meroitic); the round's scope is the
record since Round J (PR #752), whose own record — the
J-E-1 and J-E-2 adjudications and their discharges in the
Spec 105 Stage 6 outcome record — is the round's new
assessable material. Spec 105's registered design is
complete and supplies no further stages.
**Filed under:** the Glossa-Lab loop's standing discipline
(owner directives 2026-11-21 and 2026-11-22, loop expanded
2026-11-24, reaffirmed 2026-11-25): Co-scientist findings
are filed as artifacts and answered on the record; every
recommendation is logged once in
`records/coscientist-recommendations-ledger.md` with its
adjudication status; no standing, verdict, or tally changes
on a Co-scientist round alone.

## 0. Inputs and method

Three Co-scientist sessions, one per program — the Round D
sessions, continued through Rounds E–J — fired 2026-11-25
~21:37 ET (Indus), ~21:44 ET (Eteocypriot), and ~21:50 ET
(Meroitic) through the tower-compute automation Brave
route. Round J published nothing, so no post-publication
wait ran for this round (Round J adjudication §6); the
timing discipline recorded under G-E-1 is carried forward.
Each brief was sent verbatim from its filed `MESSAGE.md`;
the composer text was verified exactly against the filed
brief (character length and FNV-1a checksum) before each
send, and each send invocation re-verified the composer
before clicking Send. In all three passes the programmatic
fill verified exactly but left Send disabled; a genuine
typed space followed by Backspace in the same invocation
enabled Send with the composer still verifying exactly
afterwards (the Round G/I/J combined-invocation pattern).
The MCP server re-enumerates pages per instance and the
indices shifted between invocations throughout the round;
before every pass the target page was located by its
session URL from a fresh page listing, and the checksum
verification inside the pass is the guard that the text
landed on the intended session — no text was filled or
sent on an unverified page. Each session's working tab was
closed once its captures were verified (owner tab
discipline). Captures are filed at the goal's
`hidden_files/coscientist-sweep-2026-11-25-round-k/<program>/`
(`MESSAGE.md`, `OUTPUT.md`, `SESSION-RAW.json`,
`CAPTURE-NOTE.md`, `STAGING-NOTE.md`, plus the Eteocypriot
session's own output file, whose content is carried in its
`OUTPUT.md`).

- **Indus:** session `192b25f3-cb7b-46b4-acfa-1c1eea4e41fb`.
  Brief SHA-256
  `34034a2b987aafa707a1356c7855ae001df4a8316d734207fad5b456dc7190f7`
  (composer verification: length 16515, FNV-1a `20e0181e`);
  OUTPUT.md SHA-256
  `a389ab171b7e393d439fd87bf501bce6aba46fcd153b14c9fcf93ed6748b7a31`;
  SESSION-RAW.json SHA-256
  `1f9aefdc858046a5a3c80cfd3f63cd09a97fc28bbbf01c82799ec488712fce17`.
  The session wrote no output file.
- **Eteocypriot:** session
  `1828e4db-cc7b-434a-891a-12aca9ad1b8a`. Brief SHA-256
  `2dbcc290e4d0035824505a15363aecec84ee16b3d396a6691a94760eeb27fcb3`
  (length 19887, FNV-1a `613c6430`); OUTPUT.md SHA-256
  `7c2aaa9c7bb3f97da8dbf9c099c48dd78b88be0fad5406aa67574622e2c0d1f6`;
  SESSION-RAW.json SHA-256
  `7c46083139e3a60cfeedb3c534e12ae5fccba5e1d8a25a75bd2b6488645adf44`.
  The session also wrote `eteocypriot-round-k-review.md`;
  its content is carried in full in the goal folder's
  `OUTPUT.md`.
- **Meroitic:** session
  `11cac4f7-f109-4fac-bbb5-c670eb33b291`. Brief SHA-256
  `ad16e22cd4ae0854d97386d2ab8e18c5941af6fae475bff51283a716373bf8fc`
  (length 24688, FNV-1a `f3bb61b7`); OUTPUT.md SHA-256
  `525c0cdf1140cf2699a6212a1b72af2ac567133646fbc21a4ac7cd43f160f59b`;
  SESSION-RAW.json SHA-256
  `dae47d8c60bb2f5387da43f4f6533c877641f7faa52bd16beca37189fad3a5a6`.
  The session wrote no separately retrievable output file;
  its assessment is captured in full in `OUTPUT.md`.

Adjudication was against the primary record at head
`c3d6e71b` (the Round J adjudication merge, PR #752) — the
head both inspecting sessions pinned. The sessions'
checkable claims were independently re-read before
adjudication:

- **Ledger (§§1–3):** recounted from the ledger's data
  rows at adjudication: 130 rows — 78 done, 31 accepted,
  0 open, 21 rejected (Indus 39 — 33/5/0/1; Eteocypriot 38
  — 19/11/0/8; Meroitic 53 — 26/15/0/12), agreeing with
  both inspecting sessions' recounts and with the briefs.
- **J-E-1 / J-E-2 discharges (§2):** the dated Round J
  addendum stands on the Stage 6 outcome record as landed
  by PR #752, recording the six-value discrepancy exactly,
  the provenance as UNRESOLVED, the verified nil impact on
  ETE-1, and the zero-opportunity certificate for ETE-2,
  with the qualification noted at the seed-and-iteration
  log's Iteration 6 entry; the registered table, script,
  and historical output are unaltered, as the Eteocypriot
  session verified at this round's pin.

**Standing consequence statement: no standing, class,
verdict, or tally moves on this round.** The standings
remain 3 E + 66 I + 4 R + 3 P + 18 U = 94 (Indus); the
Spec 096 verdicts stand; the Spec 097 Leg A tallies, Stage
4.2 UNDECIDABLE AT THIS POWER, and the Stage 4.4 bounded
PARTIALLY SUPPORTED stand; Spec 103's CLAIM STANDS outcome
stands. No paper item arises anywhere in the round: no new
version of any paper is prepared.

## 1. Indus — no units advanced (brief-level null)

The session returned a null: "Round K verdict: eighth
consecutive null." No new recommendation, and no settled
row challenged. Its reasoning, in substance: Round J's
recorded assessment adds no new experimental observation;
its acceptance does not independently corroborate IND-1
GOOD, strengthen a reading, or resolve a limitation; the
completed Spec 105 result retains its previously assessed
significance at its registered scope, and neither repeating
that conclusion nor recounting the ledger changes its
evidential scope; the two completed Eteocypriot rows supply
no Indus correction. For adjudicating readings, the next
substantive advance still requires discriminating evidence
the program does not yet have; corpus release or public
replication could separately address reproducibility
without validating readings, and those remain existing
directions, not Round K recommendations. The session also
recorded, in its own words, that eight brief-level nulls
are eight review outcomes, not eight independent
confirmations of the underlying record.

The session disclosed that this is a brief-level assessment
(it did not independently inspect the underlying artifacts
or conduct an external search in this turn, and the brief's
report of no newly arrived external evidence is not a
finding that none exists). The null is therefore accepted
and recorded as a **brief-level assessment**, as Rounds D
through J recorded theirs. Per the Round D §1 pattern, a
null round adds no row to the recommendations ledger. No
paper item arises; no Indus v13 is prepared.

## 2. Eteocypriot — no units advanced (scoped-audit null)

The session worked at direct-inspection level: at
repository pin `c3d6e71b` it verified both Round J closures
(J-E-1 and J-E-2 as adjudicated and discharged), the
preservation of the historical artifacts (the registered
table, script, and gate output unaltered), and the ledger
counts, and it re-downloaded the deposited v4 byte-identical
to the filed values (MD5 `4b4621c2…`, SHA-256 `f3f6a343…`,
the same bytes read in Round F). It found the complete
delta contains no newly filed external input or sandbox
result, held that neither J-E closure warrants reopening on
the inspected evidence, and noted that accepted rows C-E-15,
C-E-16, and C-E-18 remain outside the new-recommendation
list and that no external contact, ILL action, quantum
alternative, pin refresh, or additional sandbox stage is
proposed. It recorded expressly that earlier L2–L6
reconstruction results are not presented as new independent
replications: Round K verifies the delta and the
preservation of those records. Spec 096's four verdicts
remain unchanged in its assessment.

The null is accepted and recorded as a **scoped-audit null
on direct inspection**, the Round F/H/I/J pattern for this
session. It adds no row to the recommendations ledger. No
paper item arises; no Eteocypriot v5 is prepared.

## 3. Meroitic — no units advanced (direct-inspection null)

The session worked at direct-inspection level as a bounded
delta review: it verified that Round J is recorded
faithfully, that the deposited v4 is unchanged, and that
the intervening shared-record amendments concern
Eteocypriot, not the Meroitic computations or conclusions;
it recounted the recommendations ledger in agreement with
the brief (130 rows — 78/31/0/21; Meroitic 53 —
26/15/0/12) and confirmed no campaign result changes (Leg A
4 / 1 / 3 / 2; affiliation UNDECIDABLE AT THIS POWER;
soreyi's bounded PARTIALLY SUPPORTED; Stage 4.5
ANSWERED-BY-REDIRECT / NOT CONFIRMED; the parameter d is
the detection rate). It stated its limits plainly: a
bounded delta review, not a new raw-data replay,
archaeological-source audit, or literature search; the
Rilly and Otten correspondence states remain as supplied
by the brief; accepted work and acquisition gates remain
undisturbed; and Spec 105's completion does not authorize
another stage. It advanced no recommendation and flagged
no settled item for reopening.

The null is accepted and recorded as a **null on direct
inspection**. It adds no row to the recommendations
ledger. No paper item arises; no Meroitic v5 is prepared.

## 4. Owner decisions arising

None. Nothing in the round proposes an act that would need
the owner's decision, and no settled owner decision is
reopened.

## 5. Tallies

Zero units round-wide: 0 APPLY, 0 APPLY WITH MODIFICATION,
0 DO NOT APPLY, 0 carried to owner decisions — the third
all-null round of the sweep (after H and I; Round J broke
the run with its two Eteocypriot record units). Indus
returned a brief-level null (eighth consecutive);
Eteocypriot returned a scoped-audit null on direct
inspection; Meroitic returned a null on direct inspection.

Ledger after this landing: **130 rows — 78 done, 31
accepted, 0 open, 21 rejected**, unchanged, recounted from
the data rows at §0 (Indus 39 — 33/5/0/1; Eteocypriot 38 —
19/11/0/8; Meroitic 53 — 26/15/0/12).

Diminishing returns, Rounds D–K (units per round):

| Round | Indus | Eteocypriot | Meroitic | Total |
|---|---|---|---|---|
| D | 0 | 2 | 3 | 5 |
| E | 0 | 3 | 3 | 6 |
| F | 0 | 0 | 1 | 1 |
| G | 0 | 1 | 1 | 2 |
| H | 0 | 0 | 0 | 0 |
| I | 0 | 0 | 0 | 0 |
| J | 0 | 2 | 0 | 2 |
| K | 0 | 0 | 0 | 0 |

The read across D–K is now settled in shape. The sweep's
yield came in two kinds: record corrections found by direct
inspection of newly landed material (Rounds D–G, J), and
nothing else. With Spec 105 complete, the papers at their
current versions verified byte-identical round over round,
and the framework's clarifications closed, the current
record has been audited to the point where all three
sessions — including the two that inspect directly —
return nulls on a delta consisting of the previous round's
own record. Indus has returned eight consecutive nulls
(D–K) on the decipherment questions. The binding
constraints remain external and unchanged: correspondence
replies under watch (Rilly, Steele, Egetmeyer, Kolichala,
Miller, the ICS 196 loan), owner-gated acquisitions (Spec
102; the asoreyi Shablul witness), corpus release, and the
CODECHECK replay. A further sweep has something new to
assess when one of those moves or a new registered stage
lands; on unchanged evidence it will return what Round K
returned.

## 6. Round L timing

Nothing was published in this round: no new version of any
paper was prepared or deposited, so no post-publication
wait runs. Under the loop's standing definition, **Round L
falls due immediately**. Its briefs carry no new sandbox
material — Spec 105's registered design is complete — so
Round L's assessable delta is whatever lands between this
adjudication and its dispatch: external replies under
watch, any newly landed registered work, and the record of
this round itself.

**AI disclosure:** this adjudication was executed by an AI
agent (Muse, via Muse) at the direction of Tristen
Pierson, per constitution sec. VI.
