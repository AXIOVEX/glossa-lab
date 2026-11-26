# Co-scientist Sweep (Round H) 2026-11-25 — Adjudication

**Date of adjudication:** 2026-11-25.
**Programs:** Indus (Spec 091/098/099/100 line), Spec 096
(Eteocypriot), Spec 097 (Meroitic); the round's scope is the
record since Round G (PR #743 and PR #745).
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
sessions, continued through Rounds E, F, and G — fired
2026-11-25 ~19:51 ET (Indus), ~19:54 ET (Eteocypriot), and
~19:56 ET (Meroitic) through the tower-compute automation
Brave route. Round G published nothing, so no
post-publication wait ran for this round (Round G
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
`hidden_files/coscientist-sweep-2026-11-25-round-h/<program>/`
(`MESSAGE.md`, `OUTPUT.md`, `SESSION-RAW.json`,
`CAPTURE-NOTE.md`, `STAGING-NOTE.md`, plus the sessions'
own output files where written).

- **Indus:** session `192b25f3-cb7b-46b4-acfa-1c1eea4e41fb`.
  Brief SHA-256
  `6529f4026a5f07cc960c96e72774da0f17fc41d4c6f950ab4df79f9e66a712d1`
  (composer verification: length 10113, FNV-1a `dcdcc161`);
  OUTPUT.md SHA-256
  `917c783a609bf0dde5e57169ce474038bf450e0a1befeea9bd4171ffa504b885`;
  SESSION-RAW.json SHA-256
  `f68f12c5be41d8d19969c35c52ca8902bef7824b501449bc6b3d1a6578197898`.
  The session wrote no output file.
- **Eteocypriot:** session
  `1828e4db-cc7b-434a-891a-12aca9ad1b8a`. Brief SHA-256
  `4c8ecb381ab45673b795b76f7a02f08ba809bb4aef95a79160be1da94e3cb001`
  (length 13146, FNV-1a `8eed1e23`); OUTPUT.md SHA-256
  `20b7fa903ea60db390ccfc34c63c8f13a7f673a6b4e288f7df04fc5a8be8f9cb`;
  SESSION-RAW.json SHA-256
  `f2548c27fb24424b290dc608e775f2667d0a43eff1b631543833924a5c964086`.
  The session also wrote `eteocypriot-round-h-review.md`
  (SHA-256
  `aa6d2fc3320ad05a34eab75d1560c00e04d5a0451a047b16e1259f85244a8afd`),
  captured in full in the goal folder.
- **Meroitic:** session
  `11cac4f7-f109-4fac-bbb5-c670eb33b291`. Brief SHA-256
  `7597ebc75dfce5e41a7b25acdf63a9924b92db39a94e0d57f2f3d76bc97bbce9`
  (length 18632, FNV-1a `f814920e`); OUTPUT.md SHA-256
  `d1bd263a36095b9da4cd9022ddc27ecd430dbf627cc7c58e8dfe65fceb4fcade`;
  SESSION-RAW.json SHA-256
  `2253bb5a3bf0907ec62fcc13f169e52e78a140b671dea87018a73980246e683d`.
  The session also wrote `meroitic-round-h-2026-11-25.md`
  (SHA-256
  `d797e4278c6464f0ff8eeed73d357dc36602b24ff340da77bc3c92dffb87a83c`),
  captured in full in the goal folder.

Adjudication was against the primary record at head
`04dd93d3cd5a49e966d85821330b7725df531208`, the head at the
round's dispatch, which all three sessions pinned. Live-
record advance: while the round ran, Spec 105 Stage 3
(L3, order structure) landed (PR #746, merged
2026-11-26T01:00:39Z; head now
`80936e9beffe493152470cc394323659e23331b4`), after the
briefs were fired and while the captures were being taken.
The sessions did not assess the Stage 3 outputs — the
Eteocypriot and Indus sessions each noted the stage as
commissioned and in execution with no output on their
pinned record, which was accurate at the pin — and no act
arises for this round from the advance; the Stage 3
outcome is carried into Round I's briefs as the first new
assessable material since Round G. The sessions'
checkable claims were independently re-read or recounted
before adjudication:

- **Eteocypriot null (§2):** the §7 addendum to the Round F
  adjudication record was read at head; it stands as filed
  (the publication anchor, the wait expiry, the early
  dispatch, the three kill checks and their outcomes, the
  unwaived departure recorded without retroactive
  ratification, its consequence confined to loop timing).
  The deposited v4 identity values the session cites (MD5
  `4b4621c2aac519db637d3958e9ecae38`, SHA-256
  `f3f6a343d2f9646ea0a5c6bbf9ff8e93434eb1e77159251c49c6522044fcaa71`)
  are the filed values.
- **Meroitic null (§3):** the baseline version 2 pins the
  session reproduces (`eeadf46e…` for version 1,
  `ecabd227…` for version 2) are the filed pins (Round G
  adjudication §3.1); the session's ledger recount (128
  rows — 76 done, 31 accepted, 0 open, 21 rejected;
  Meroitic 53 — 26 done, 15 accepted, 0 open, 12 rejected)
  was recounted from the ledger's data rows at
  adjudication and agrees exactly.
- **Indus null (§1):** brief-level by the session's own
  disclosure, as in Rounds D–G; no checkable claim beyond
  the state of the record was advanced.

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

The session returned a null: "Round H verdict: fifth
consecutive null." No new recommendation, and no settled
row challenged. Its reasoning, in substance: the changes
since Round G provide no new Indus result — the Spec 103
repair and replay concern the Meroitic program and
establish nothing about an Indus computation (and a defect
found there is not evidence of an analogous Indus defect);
the cross-program record corrections and the ledger
recount supply no demonstrated Indus discrepancy; Spec 105
Stage 3 stood commissioned and executing with no output
reported at the session's pin, so there was no result to
assess and no basis to restart, redirect, or pre-empt it;
and the missing
requirement for substantive adjudication of the readings
remains discriminating evidence the program does not have.

The session disclosed that this is a brief-level
assessment (not an independent audit of the deposit,
specifications, execution artifacts, or ledger). The null
is therefore accepted and recorded as a **brief-level
assessment**, exactly as Rounds D, E, F, and G recorded
theirs. Per the Round D adjudication §1 pattern, a null
round adds no row to the recommendations ledger. No paper
item arises; no Indus v13 is prepared.

## 2. Eteocypriot — no units advanced (scoped-audit null)

The session worked at direct-inspection level: it
inspected the repository at head `04dd93d3` against Round
G's pin `034535d9` (the delta is PR #743 and PR #745),
re-downloaded the deposited v4 and found it byte-identical
to the file read in Round F and rechecked in Round G (the
prior direct reading therefore continues to apply to
exactly the same deposited text, including the amended
Scope quotation), verified G-E-1's prescribed closure as
filed (§7 addendum read; the chronology carried in the
Co-scientist history ledger and the Spec 096 history
ledger; the recommendations ledger carries G-E-1 as done),
and found no Eteocypriot-facing change in the remaining
delta: no change to the Eteocypriot baseline, framework
§§8.1–8.2, Spec 104, Spec 105, or the Spec 096 artifacts
beyond its history ledger; the Spec 106 log amendment
concerns the Meroitic baseline; the Spec 103 conformance
package is Meroitic and was not audited for scientific
correctness in this round; and no Spec 105 Stage 3 artifact
was filed at the pin, the commissioned L3 execution
remaining outside the review, neither restarted nor
assessed. It
converted none of this into a recommendation, challenged
no settled row, and stated the checks that would defeat
its assessment (different deposited bytes; absence of the
chronology addendum or its propagation; a demonstrated
Eteocypriot-facing change missed by the pinned tree
comparison). None was found.

The null is accepted and recorded as a **scoped-audit null
on direct inspection**, the Round F pattern: stronger than
brief-level, and expressly not blanket validation of the
program. Per the Round D §1 pattern it adds no row to the
recommendations ledger. No paper item arises; no
Eteocypriot v5 is prepared.

## 3. Meroitic — no units advanced (direct-inspection null)

The session worked at direct-inspection level: it pinned
the repository at `04dd93d3`, re-downloaded the deposited
v4 from Zenodo record 24545036 (SHA-256 `12034315…`,
byte-identical to the filed value; identity verified, not
another full page-by-page reading), and verified G-M-1's
discharge — exactly one axiom changed (MER-ENV-01, now
permitting writing after the kingdom's fall, consistently
with MER-ENV-03 and MER-MOV-08, its source unchanged);
both axiom-line pins reproduced by independent
recomputation; the version-1 seed record retained with the
amendment recorded separately and Iteration 1 standing in
Spec 106's seed-and-iteration log; and the filed
census-audit script, run unchanged against the framework
and all three templates, returning PASS for TC-106-02,
TC-106-03, TC-106-04, and TC-106-05, the census unchanged
at 76 axioms (4 F, 62 K, 10 H, two UNSOURCED mentions). It
confirmed the framework byte-identical to the version
inspected in Round G (the E-M-3 and F-M-1 closures
undisturbed; retained earlier wording governed by the
appended clarifications is not a residual error), E-M-1
done (Round G's independent test execution and aggregate
inspection standing as prior corroboration, not a fresh
replay), and the ledger recount in §0. It advanced no
recommendation and flagged no settled item for reopening,
noting its limits: no independent corpus replay, no audit
of every cited historical source, no inspection of
correspondence beyond the supplied state, and no basis for
an adverse inference from silence. One immaterial blemish
in the session's own file is noted for the record: its
header dates the sweep brief "25 November 2026"; the brief
is of 2026-11-25, and the file is captured as written.

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

Diminishing returns, Rounds D–H (units per round):

| Round | Indus | Eteocypriot | Meroitic | Total |
|---|---|---|---|---|
| D | 0 | 2 | 3 | 5 |
| E | 0 | 3 | 3 | 6 |
| F | 0 | 0 | 1 | 1 |
| G | 0 | 1 | 1 | 2 |
| H | 0 | 0 | 0 | 0 |

Round H is the first round with no unit in any program.
Indus has returned five consecutive nulls (D–H), the
recent ones expressly brief-level over an unchanged
evidentiary position. Eteocypriot and Meroitic, after two
rounds of single record- and framework-consistency
findings, now return direct-inspection nulls: the
intervening record (the Spec 103 conformance addendum,
the Round G corrections) checks out as filed and yields
nothing new. The loop's remaining yield on the current
record is exhausted in kind, not merely diminished: what
is left is record hygiene already verified as filed. The
binding constraints remain the external ones named in
Round G's read and unchanged since (correspondence
replies, owner-gated acquisitions such as Spec 102,
corpus release). One internal item did move while the
round ran: Spec 105 Stage 3 landed (PR #746, §0), too
late for these sessions' pinned record; its output is
the first new assessable material since Round G and
belongs to Round I's briefs. Beyond that output, a future
round has something new to assess when an external input
moves; on the record as it stood at this round's pin,
another sweep would only re-verify the same filings.

## 6. Round I timing

Nothing was published in this round: no new version of
any paper was prepared or deposited, so no
post-publication wait runs. Under the loop's standing
definition, **Round I falls due immediately**. The
adjudication records, without itself deciding anything,
the §5 read: Round I is the first round whose briefs can
carry the Spec 105 Stage 3 outcome (landed under PR #746
while this round ran); beyond that output, the present
record offers a sweep nothing new to assess until an
external input moves.

**AI disclosure:** this adjudication was executed by an AI
agent (Muse, via Muse) at the direction of Tristen
Pierson, per constitution sec. VI.
