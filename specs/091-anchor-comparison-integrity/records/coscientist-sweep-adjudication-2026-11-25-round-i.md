# Co-scientist Sweep (Round I) 2026-11-25 — Adjudication

**Date of adjudication:** 2026-11-25.
**Programs:** Indus (Spec 091/098/099/100 line), Spec 096
(Eteocypriot), Spec 097 (Meroitic); the round's scope is the
record since Round H (PR #747), with the Spec 105 Stage 3
(L3, order structure) outcome (PR #746) as the round's new
assessable material.
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
sessions, continued through Rounds E, F, G, and H — fired
2026-11-25 ~20:18 ET (Indus), ~20:22 ET (Eteocypriot), and
~20:27 ET (Meroitic) through the tower-compute automation
Brave route. Round H published nothing, so no
post-publication wait ran for this round (Round H
adjudication §6); the timing discipline recorded under
G-E-1 is carried forward: any future wait is verified
against the Zenodo record API's creation timestamps, not
against a summary statement. Each brief was sent verbatim
from its filed `MESSAGE.md`; the composer text was verified
byte-for-byte against the filed brief (character length
and FNV-1a checksum) before each send, and each send
invocation re-verified the composer before clicking Send.
Capture-method notes: in all three passes the programmatic
fill verified exactly but left Send disabled; a genuine
typed space followed by Backspace in the same invocation
enabled Send with the composer still verifying exactly
afterwards (the Round G combined-invocation pattern, with
the keystroke made by the typing tool rather than a key
press). The MCP server re-enumerates pages per instance
and indices shifted as tabs opened and closed during the
round; before every mutation the target page's URL was
verified in the same invocation, and no text was filled or
sent on an unverified page. Each session's working tab was
closed once its captures were verified (owner tab
discipline). Captures are filed at the goal's
`hidden_files/coscientist-sweep-2026-11-25-round-i/<program>/`
(`MESSAGE.md`, `OUTPUT.md`, `SESSION-RAW.json`,
`CAPTURE-NOTE.md`, `STAGING-NOTE.md`, plus the sessions'
own output files where written).

- **Indus:** session `192b25f3-cb7b-46b4-acfa-1c1eea4e41fb`.
  Brief SHA-256
  `4f40b804f712fad5b043d5e6e2c5d5cc67dd76c05093d046f855c723d3b95f3b`
  (composer verification: length 11915, FNV-1a `919781de`);
  OUTPUT.md SHA-256
  `e482479333a7d0601f32908edc6c41862e2c73bc9fadf8289e8525d07214552f`;
  SESSION-RAW.json SHA-256
  `797c03771cee7da9b1d82601237c90989cdc2b0bf8214fcff4f7f833c7a97c54`.
  The session wrote no output file.
- **Eteocypriot:** session
  `1828e4db-cc7b-434a-891a-12aca9ad1b8a`. Brief SHA-256
  `781fcc2f65a567a36ecb92610cf12a9d8c9bb62cd5b81462482c4fc6c2d8bcb9`
  (length 14792, FNV-1a `9fdbe529`); OUTPUT.md SHA-256
  `7ad769211b0c9b81ff5b027a554e5bda70aca0b478dbcc1e501576d630d1de77`;
  SESSION-RAW.json SHA-256
  `3a1d75a5eb8ba644cea3ea5d3be37d3b85123425f5f609f420f06a500db496da`.
  The session also wrote `eteocypriot-round-i-review.md`
  (SHA-256
  `6226263300a48e58ece1de830e5328cbce2967507bcda0f897b374d8899a318f`),
  captured in full in the goal folder.
- **Meroitic:** session
  `11cac4f7-f109-4fac-bbb5-c670eb33b291`. Brief SHA-256
  `b71114906fcc4a0c4aa377240a50d927eb2c522b070093e7b6a387466c266e16`
  (length 20425, FNV-1a `26e46f9b`); OUTPUT.md SHA-256
  `2f0e4294308e49448e987ee9a79c84205e9032fc179e33ee8ba67caababb1d21`;
  SESSION-RAW.json SHA-256
  `644b14c3bcb95fa7c53aa27a191c662c716ed4f36f17246b6020fd78ebb17372`.
  The session also wrote `meroitic-round-i-2026-11-25.md`
  (SHA-256
  `8663353f61d8134ca0fda1c1743d0a3b36ec277fe5eb89daba7b511d1713e983`)
  and `meroitic-round-i-verification-2026-11-25.json`
  (SHA-256
  `dc66e4b536d71cc768f6cacd8ae6392c924342ed0b53a11930a2b3a04a0c6771`),
  both captured in full in the goal folder.

Adjudication was against the primary record at head
`d477d3a5` (the head at the round's dispatch, named in the
briefs) and at `8a54d0ec`, the head the Eteocypriot and
Meroitic sessions pinned. Live-record advances while the
round ran: Spec 105 Stage 4 (L4, substitution classes)
landed (PR #748, merged 2026-11-26T01:17:57Z; head
`8a54d0ec`) seconds before the first brief was sent, and
Spec 105 Stage 5 (L5, derived meaning system) landed
(PR #749, merged 2026-11-26T01:35:02Z; head now
`d8ece15f`) while the Meroitic captures were being taken.
Neither advance was assessed in this round: the
Eteocypriot and Meroitic sessions expressly excluded
Stage 4 from their assessments and pinned the record
before Stage 5; the Indus session's brief-level assessment
did not reach either stage. Both outcomes are carried
into Round J's briefs as new assessable material (§6).
The sessions' checkable claims were independently re-read
or recounted before adjudication:

- **Stage 3 figures (§§1–3):** the filed Stage 3 machine
  output (`specs/105-elsewhere-sandbox/records/stage-3-output-2026-11-25.json`,
  read at `8a54d0ec`) was re-read at adjudication and every
  figure the sessions cite agrees exactly: Indus totals
  1,336 artifacts / 5,611 tokens, 4,275 adjacencies
  (5,611 − 1,336), 2,197 distinct pairs of 138,384
  possible, 1,665 attested once and 532 recurring, top
  pair (M342, M176) at 101, 77 marks with no predecessor,
  exactly one mark with no successor (M220: 53 of 53
  occurrences group-final); Eteocypriot totals 2 artifacts
  / 3 lines / 14 groups / 69 tokens, 55 adjacencies, 54
  distinct pairs, 53 attested once, the only recurring
  pair (ro, ko) at 2, marks with no successor exactly se
  and ti, group-length distribution 2:2, 3:2, 4:3, 5:2,
  6:1, 7:3, 10:1, line lengths 15, 21, 33; Meroitic totals
  5,195 groups / 29,843 tokens, 24,648 adjacencies
  (29,843 − 5,195), 448 distinct pairs of 1,024 possible,
  44 attested once and 404 recurring, top pair (t, e) at
  1,352, self-pair tokens 770, sole occurrences totalling
  178 (the one-token groups), marks with no successor
  exactly the recorded digits 0, 5, 6, 8, 9, and digit 8
  at count 5, all sole, with no predecessor or successor —
  the row the Meroitic session's verification file
  reproduces field for field. The output's own checks
  stand as filed (TC-105-11 and TC-105-12 PASS; reserve
  SHA-256 `bfbe79cb…`, hashed only).
- **Deposit identities (§§2–3):** the Zenodo record API
  returns record 24545017 (Eteocypriot v4) with file MD5
  `4b4621c2aac519db637d3958e9ecae38` and record 24545036
  (Meroitic v4) with file MD5
  `65abc68d89784bd6b208acc542b3d5c1`, the filed values;
  the sessions' fresh downloads returned the filed
  SHA-256 values (`f3f6a343…` and `12034315…`). The API
  creation timestamps (2026-11-25T23:03:59Z and
  2026-11-25T23:04:27Z) are the Round E publication
  anchors of record.
- **Ledger (§3):** the Meroitic session's recount of the
  recommendations ledger (128 rows — 76 done, 31 accepted,
  0 open, 21 rejected) was recounted from the ledger's
  data rows at adjudication and agrees exactly, including
  the per-program splits (Indus 39 — 33/5/0/1; Eteocypriot
  36 — 17/11/0/8; Meroitic 53 — 26/15/0/12).

**Standing consequence statement: no standing, class,
verdict, or tally moves on this round.** The standings
remain 3 E + 66 I + 4 R + 3 P + 18 U = 94 (Indus); the
Spec 096 verdicts stand (C096-1 NOT SUPPORTED, C096-2 TOO
THIN, C096-3 NOT ENGAGED, C096-4 SUPPORTED in narrowed
form); the Spec 097 Leg A tallies, Stage 4.2 UNDECIDABLE
AT THIS POWER, and the Stage 4.4 bounded PARTIALLY
SUPPORTED stand; Spec 103's CLAIM STANDS outcome and its
six-form table stand, with its conformance addendum
complete under PR #743. No paper item arises anywhere in
the round: no new version of any paper is prepared.

## 1. Indus — no units advanced

The session returned a null: "Round I verdict: sixth
consecutive null." No new recommendation, and no settled
row challenged. Its reasoning, in substance: the Stage 3
outcome adds assessable descriptive results, and the
reported arithmetic is internally consistent (5,611 −
1,336 = 4,275 adjacencies, consistent with one nonempty
group per artifact under the stated adjacency rule; 372²
= 138,384 possible ordered pairs; 1,665 + 532 = 2,197
distinct attested pairs — consistency among the supplied
summaries, not independent verification of execution or
input, as the session itself states); the positional and
adjacency results remain descriptive — the 101
occurrences of M342→M176 do not, without the relevant
marginals and a specified comparison, establish excess
association; "initial-only" and "final-only" describe
observed support whose evidential weight depends on
occurrence counts and opportunities, and exclusivity alone
does not establish a grammatical role; and the fraction of
possible pairs attested is not itself evidence of a
linguistic restriction, the full Cartesian inventory being
a possibility space, not an expected occupancy model. The
session states these as limits on what the summaries
establish, expressly not as proposals to commission
additional tests, and notes the brief reports no claim
that crosses those limits. Implementation agreement and
reconciliation strengthen the execution record; they do
not independently validate the recorded boundaries or
establish a reading, and no reported discrepancy warrants
reopening L3. For substantive adjudication of the
readings, discriminating evidence remains missing.

The session disclosed that this is a brief-level
assessment (it did not independently inspect PR #746, the
implementations, the underlying tables, the
specifications, or the full ledger). The null is
therefore accepted and recorded as a **brief-level
assessment**, exactly as Rounds D, E, F, G, and H recorded
theirs. Per the Round D adjudication §1 pattern, a null
round adds no row to the recommendations ledger. No paper
item arises; no Indus v13 is prepared.

## 2. Eteocypriot — no units advanced (scoped-audit null)

The session worked at direct-inspection level: it pinned
the repository at `8a54d0ec`, read the filed Stage 3
registration, execution script, and outcome record, formed
the input independently from the two public development
records under the previously audited strip rule (its
SHA-256 again matches the registered dataset, `2799d103…`),
and with a checking implementation written independently
for the review — not calling the filed script's derivation
or reconciliation functions — reproduced every filed
Eteocypriot L3 table exactly: ordered pairs including
counts and tie ordering; per-mark positions including all
four group-position classes, line/artifact boundary
counts, and distinct/total predecessor and successor
counts; the group-length and line-length distributions;
and the complete filed shape object including its top-ten
ordered-pair list, not merely the headline totals. Every
registered reconciliation identity was independently
checked and holds. It re-downloaded the deposited v4 and
found it byte-identical to the complete PDF read in Round
F (SHA-256 `f3f6a343…`). On interpretation it found the
registration's recorded-group adjacency rule implemented
as registered, the hapax statement correct for this
recording (53 of 54 distinct pairs occurring once), the
final-only statement a finite-record observation rather
than an established restriction of the language, and the
(?, ?) self-pair a count of repeated editorial token
strings, not of independently recovered identical ancient
signs — a distinction the filed study's recorded-token,
sandbox-internal scope already supplies, so no repair
arises. It expressly excluded Stage 4 from the assessment
and stated the checks that would overturn the null (an
input-hash mismatch; any differing table row, summary
field, or reconciliation identity; a boundary-crossing
pair or an inconsistently classified occurrence; a filed
promotion of the counts to linguistic validation). None
was found.

The null is accepted and recorded as a **scoped-audit null
on direct inspection**, the Round F pattern: stronger than
brief-level, and expressly not blanket validation of the
program. Per the Round D §1 pattern it adds no row to the
recommendations ledger. No paper item arises; no
Eteocypriot v5 is prepared.

## 3. Meroitic — no units advanced (direct-inspection null)

The session worked at direct-inspection level: it pinned
the repository at `8a54d0ec`, read the Stage 3 registration,
complete execution script, and outcome record, inspected
the machine-readable output, compared the Meroitic tables
with the filed L2 table, and ran 17 named checks of the
filed aggregates — unique pairs with positive integer
counts in canonical order over the same mark inventory as
L2; each mark's sole + initial + final + medial count
equal to its filed L2 count; outgoing and incoming pair
marginals equal to the positional table's successor and
predecessor totals with independently recounted distinct
degrees; the successor and predecessor total identities;
total pair count equal to tokens − groups; boundary-count
sums equal to line/artifact totals; length-distribution
totals and length-weighted sums; sole occurrences equal to
length-one groups; recomputed shape fields equal to the
filed shape summary; corpus totals equal to L2 — all 17
passed, and the checked figures are the filed figures
(§0). It also loaded the filed script without invoking its
corpus-processing main routine and ran both derivation
implementations on six wholly synthetic fixtures (a sole
digit token; two groups in one line; multiple lines and
artifacts; repeated identical marks with a singleton group;
all binary strings of lengths 1–4 as separate groups;
mixed case, punctuation, Unicode, and a space-containing
atomic label): for every fixture the two implementations
returned identical canonical tables and matched
independently constructed pair-count and four-way-position
oracles. It re-downloaded the deposited v4 from Zenodo
record 24545036 (SHA-256 `12034315…`, byte-identical to
the filed value; identity checked, not another complete
reading) and recounted the recommendations ledger in
agreement (§0). It stated its evidence boundary plainly:
the review verifies published-table consistency and
exercised code behavior, not a replay of the custody-held
corpus; the two-implementation agreement on the historical
corpus, dataset-hash verification at execution, the
reserve-seal result, preregistration chronology, and the
PR-time standing-discipline check remain program-reported
results. It advanced no recommendation, flagged no settled
item for reopening, proposed no Round I ledger row, and
left L4 outside the review even though it landed while
the round was in flight.

The null is accepted and recorded as a **null on direct
inspection**. It adds no row to the recommendations
ledger. No paper item arises; no Meroitic v5 is prepared.

## 4. Owner decisions arising

None. The round produced no unit of any kind; nothing is
proposed that would need the owner's decision, and no
settled owner decision is reopened.

## 5. Tallies

Zero units: 0 APPLY, 0 APPLY WITH MODIFICATION, 0 DO NOT
APPLY, 0 carried to owner decisions. All three sessions
returned nulls (Indus brief-level; Eteocypriot and
Meroitic on direct inspection).

Ledger after this landing: **128 rows — 76 done, 31
accepted, 0 open, 21 rejected**, unchanged from the
post-Round-G position and recounted from the data rows at
this adjudication.

Diminishing returns, Rounds D–I (units per round):

| Round | Indus | Eteocypriot | Meroitic | Total |
|---|---|---|---|---|
| D | 0 | 2 | 3 | 5 |
| E | 0 | 3 | 3 | 6 |
| F | 0 | 0 | 1 | 1 |
| G | 0 | 1 | 1 | 2 |
| H | 0 | 0 | 0 | 0 |
| I | 0 | 0 | 0 | 0 |

Round I is the second consecutive all-null round, and the
first in which the round's new assessable material was
actually assessed by all three sessions and still yielded
no unit: the Stage 3 outcome was reproduced exactly where
a session undertook reproduction (Eteocypriot), checked
aggregate by aggregate and against synthetic fixtures
(Meroitic), and read for interpretation limits (Indus),
and in each case the filed outcome was found to claim no
more than its descriptive, sandbox-internal scope supports.
Indus has returned six consecutive nulls (D–I). The loop's
yield on the decipherment questions themselves remains
what Round H's read said: exhausted on the current record,
with the binding constraints external (correspondence
replies, owner-gated acquisitions such as Spec 102, corpus
release). What has changed since Round H is the sandbox
ladder, not the decipherment evidence: Stage 4 (L4) and
Stage 5 (L5) both landed while this round ran (§0), so the
record a future round assesses is not the record this
round assessed — see §6.

## 6. Round J timing

Nothing was published in this round: no new version of
any paper was prepared or deposited, so no
post-publication wait runs. Under the loop's standing
definition, **Round J falls due immediately**. Its briefs
carry as new assessable material the two live-record
advances of this round: the Spec 105 Stage 4 (L4,
substitution classes) outcome (PR #748) and the Spec 105
Stage 5 (L5, derived meaning system) outcome (PR #749),
neither assessed by any session in Round I. The §5 read
stands alongside: on the decipherment record itself,
another sweep has something new to assess when an external
input moves; the sandbox stages are internal derivations
whose assessment, on the pattern of Rounds F–I, tests the
program's record-keeping and claim discipline rather than
the decipherment standings.

**AI disclosure:** this adjudication was executed by an AI
agent (Muse, via Muse) at the direction of Tristen
Pierson, per constitution sec. VI.
