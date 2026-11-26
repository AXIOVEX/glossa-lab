# Co-scientist Sweep (Round J) 2026-11-25 — Adjudication

**Date of adjudication:** 2026-11-25.
**Programs:** Indus (Spec 091/098/099/100 line), Spec 096
(Eteocypriot), Spec 097 (Meroitic); the round's scope is the
record since Round I (PR #750), with the Spec 105 Stage 4
(L4, substitution classes) outcome (PR #748), the Stage 5
(L5, derived meaning system) outcome (PR #749), and the
Stage 6 (L6, boundary gates) outcomes (PR #751) as the
round's new assessable material.
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
sessions, continued through Rounds E, F, G, H, and I — fired
2026-11-25 ~21:05 ET (Indus), ~21:12 ET (Eteocypriot), and
~21:20 ET (Meroitic) through the tower-compute automation
Brave route. Round I published nothing, so no
post-publication wait ran for this round (Round I
adjudication §6); the timing discipline recorded under
G-E-1 is carried forward. Each brief was sent verbatim from
its filed `MESSAGE.md`; the composer text was verified
byte-for-byte against the filed brief (character length and
FNV-1a checksum) before each send, and each send invocation
re-verified the composer before clicking Send. In all three
passes the programmatic fill verified exactly but left Send
disabled; a genuine typed space followed by Backspace in
the same invocation enabled Send with the composer still
verifying exactly afterwards (the Round G/I
combined-invocation pattern). The MCP server re-enumerates
pages per instance and the indices shifted between
invocations throughout the round; before every pass the
target page was located by its session URL from a fresh
page listing, and the checksum verification inside the pass
is the guard that the text landed on the intended session —
no text was filled or sent on an unverified page. Each
session's working tab was closed once its captures were
verified (owner tab discipline). Captures are filed at the
goal's `hidden_files/coscientist-sweep-2026-11-25-round-j/<program>/`
(`MESSAGE.md`, `OUTPUT.md`, `SESSION-RAW.json`,
`CAPTURE-NOTE.md`, `STAGING-NOTE.md`, plus the sessions' own
output files where written and retrievable).

- **Indus:** session `192b25f3-cb7b-46b4-acfa-1c1eea4e41fb`.
  Brief SHA-256
  `93c5a1d49021d44b6a30cda906f860f60acf9aecb35d9b13350ab3d7381c4874`
  (composer verification: length 14997, FNV-1a `a0a41c82`);
  OUTPUT.md SHA-256
  `0033c51b0a448dcd0089b039522fedb2416b521b9fba27df717c41c595a8d9b7`;
  SESSION-RAW.json SHA-256
  `0d9e0be7355f5d6d9544944dde2c4a16c4f7f47c446e3ee9c6dd245195ca927e`.
  The session wrote no output file.
- **Eteocypriot:** session
  `1828e4db-cc7b-434a-891a-12aca9ad1b8a`. Brief SHA-256
  `e63cfa0f7193276f2236f7d49aca126698242ad3d11232f8fdb6a805e6d1cb5d`
  (length 17456, FNV-1a `feb5b5b3`); OUTPUT.md SHA-256
  `a124bbb05661841861703e861829c593bd360105d03a92407339be474ca7791d`;
  SESSION-RAW.json SHA-256
  `05fa974c959975f7c9864f3c41e4e9e8c8d6ba51853ca453bab8c32d2cb09c4b`.
  The session also wrote `eteocypriot-round-j/review.md`
  (captured in full in the goal folder as
  `eteocypriot-round-j-review.md`, SHA-256
  `37237a99945f4c5a65035dc39de61982a15dc7a308a5ccd71289ea3f66071300`)
  and `eteocypriot-round-j/independent-checks.json`; the JSON
  sidecar's content is carried in the review's §3 and its
  witness statements — the Academia file view does not
  render the JSON as retrievable text, and that limitation
  is recorded in the capture note rather than filled in.
- **Meroitic:** session
  `11cac4f7-f109-4fac-bbb5-c670eb33b291`. Brief SHA-256
  `5874aeeb00d50c77150173b0d7a0da7e2e674e9208a829a7af0a5f57d7f363f1`
  (length 23674, FNV-1a `fbcb2289`); OUTPUT.md SHA-256
  `978010ec5157515ec123f5619e63721a6b7f2caa888050e1c09f31203f956e1f`;
  SESSION-RAW.json SHA-256
  `aea6c39187906c39372e3d8d44a2ff0d0e83799e494c2b9df9d8dc0895c7c7ca`.
  The session also wrote `meroitic-round-j-2026-11-25.md`
  (captured in full in the goal folder, SHA-256
  `2313e2b67e76fb963dfca98f489efd47d5b5d7581965a188127bac4cc805091a`)
  and `meroitic-round-j-verification-2026-11-25.json` (15
  checks, six L4/L5 fixtures, three gate fixtures, five
  threshold cases — contents as described in the session's
  assessment; the JSON file view carries the same rendering
  limitation as the Eteocypriot sidecar).

Adjudication was against the primary record at head
`c5c5f4bc` (the Round I adjudication merge, PR #750, on top
of the Stage 6 merge `0d235a75`) — the head both inspecting
sessions pinned. The sessions' checkable claims were
independently re-read or recomputed before adjudication:

- **Stage 6 registration table (§2.1):** the G-ETE outside
  material in
  `specs/105-elsewhere-sandbox/records/stage-6-registration-2026-11-25.md`
  §2 was read verbatim at adjudication: the Common syllabary
  value table is described there as "the checker's list of
  the sign values of that frame, as settled by the Idalion
  bilingual and carried in the edition of record's signary
  (Masson, *Les inscriptions chypriotes syllabiques*)", and
  the enumeration as filed runs `wa we wi wo`, `ya ye`,
  `za ze zi zo`, `xa xe xi xo` — 59 values, including `ye`,
  `ze`, `zi`, `xi`, `xo` and nowhere `yo`. The filed
  execution script carries the same enumeration in both
  implementations (`CYPRIOT_A` and the awk table).
- **ETE-2 class cardinalities (§2.2):** recomputed at
  adjudication from the filed Stage 4 and Stage 5 machine
  outputs: the Eteocypriot L4 joint partition has 35 classes,
  every one of size 1; the L5 identity partition has 35
  classes, every one of size 1; exactly one class in each
  partition contains the exempt mark `?`. The 70 classes
  ETE-2 checked therefore contain zero within-class pairs of
  value-carrying marks (68 value-carrying singletons and 2
  `?` singletons), exactly the session's certificate.
- **ETE-1 input impact (§2.1):** the filed Stage 6 output's
  ETE-1 table carries 33 distinct observed values; none of
  them is in the disputed set difference (`ye`, `ze`, `zi`,
  `xi`, `xo` registered-only; `yo` reference-only), so the
  observed inventory returns GOOD under the checked
  reference repertoire as well — the session's impact
  statement verified from the filed output.
- **Ledger (§§1–3):** recounted from the ledger's data rows
  at adjudication before this landing's rows were added:
  128 rows — 76 done, 31 accepted, 0 open, 21 rejected,
  with the per-program splits of the Round I adjudication
  (Indus 39 — 33/5/0/1; Eteocypriot 36 — 17/11/0/8; Meroitic
  53 — 26/15/0/12), agreeing with the Meroitic session's
  recount.

**Standing consequence statement: no standing, class,
verdict, or tally moves on this round.** The standings
remain 3 E + 66 I + 4 R + 3 P + 18 U = 94 (Indus); the
Spec 096 verdicts stand; the Spec 097 Leg A tallies, Stage
4.2 UNDECIDABLE AT THIS POWER, and the Stage 4.4 bounded
PARTIALLY SUPPORTED stand; Spec 103's CLAIM STANDS outcome
stands. No paper item arises anywhere in the round: no new
version of any paper is prepared. The round's two units are
record acts inside the Spec 105 package, discharged at this
landing by dated addenda to the Stage 6 outcome record
(§2).

## 1. Indus — no units advanced

The session returned a null: "Round J verdict: seventh
consecutive null — but a substantive new result." No new
recommendation, and no settled row challenged. Its
reasoning, in substance: IND-1 GOOD is supported by the
reported figures at its registered scope (the loss
difference 4.557943 − 4.178289 = 0.379654 nats per token
exceeds the frozen 0.05 margin; the predictor-use counts
sum to the 1,391 reserve tokens; the 26 unseen tokens
contributed identically under the symmetric rule and so
zero to the difference); conditional on the reported
registration and execution, the completed held-out
comparison is real progress within its stated scope and is
not to be dismissed for failing to adjudicate readings; it
does not isolate which predictor component produced the
advantage, establish linguistic rather than other
sequential structure, or validate a sign-to-language
mapping, and no further comparators or ablations are
automatically required to sustain the comparison actually
registered. On L4/L5 it records a definitional dependence:
once L4 assigns every mark a distinct class, an L5 role
that includes that class must also be unique, so the 372
identity classes are not independent corroboration of L4's
uniqueness — stated by the session itself as "not a
demonstrated error or a new correction request: the
construction is disclosed, and no independent semantic
claim is reported." That observation is recorded here as a
confirmation of the program's existing position (the L5
registration defines the role as the complete filed profile
including the L4 assignment, and no independence claim for
L5 over L4 stands anywhere on the record), not as a unit,
following the Round D §1 pattern for interpretation
boundaries. (The Eteocypriot session makes the same point
for its sandbox inside J-E-2's evidence, §2.2.)

The session disclosed that this is a brief-level assessment
(it did not independently inspect the registrations, code,
scored reserve, or full ledger). The null is therefore
accepted and recorded as a **brief-level assessment**, as
Rounds D through I recorded theirs. Per the Round D §1
pattern, a null round adds no row to the recommendations
ledger. No paper item arises; no Indus v13 is prepared.

## 2. Eteocypriot — two units, both record-level

The session worked at direct-inspection level: it pinned
the repository at `c5c5f4bc`, read the L4–L6 registrations,
implementations, and outcomes, reconstructed the
Eteocypriot input from the two public development records
under the previously audited strip rule (dataset SHA-256
again `2799d103…`), reproduced every filed L4 and L5 table
and the filed G-ETE canonical table exactly under the
registered table, and re-downloaded the deposited v4
byte-identical to the filed value (`f3f6a343…`). It
returned two ranked recommendations, both concerning the
Spec 105 gate record, neither proposing a paper or
Spec 096 verdict change. Both are sustained, on the
verification at §0, and both are discharged at this landing
by the dated addendum appended to
`specs/105-elsewhere-sandbox/records/stage-6-outcome-2026-11-25.md`
(the Stage 6 outcome record's Round J addendum), with a
qualifying note appended to the Spec 105 seed-and-iteration
log at its Iteration 6 entry. The registered table, the
filed script, and the historical gate output are NOT
altered: verdicts and registrations are appended to, never
overwritten.

### 2.1 J-E-1 — APPLY WITH MODIFICATION (done at this landing)

The unit: the registered 59-value Common syllabary table
does not match the checked Common-syllabary references —
the CREWS project Common-syllabary worksheet (Y row ya/yo,
Z row za/zo, X row xa/xe) and the Unicode Cypriot Syllabary
chart (55 encoded syllables; JA/JO, ZA/ZO, XA/XE) — the
exact set difference being registered-only `ye`, `ze`,
`zi`, `xi`, `xo` and reference-only `yo`; both checker
implementations copy the registered enumeration, so their
agreement is not an independent check of the shared
external table. The session's claim is bounded: the filed
attribution of this exact enumeration to the edition of
record's signary needs source reconciliation; it does not
infer from the charts alone that every disputed value is
impossible. Its advance kill check: a source passage or
signary with a checkable location and transliteration
mapping supporting this exact 59-value enumeration and
explaining the absent `yo` defeats the diagnosis.

Adjudication: the filed half of the claim is verified
verbatim (§0): the registration attributes the enumeration
to Masson's signary in the words quoted there, and the
enumeration as filed contains the five registered-only
values and no `yo`. No passage supporting the exact
enumeration was produced at adjudication, and none is on
file in the Spec 105 package; the kill check is therefore
not met on the present record. The modification: the
session's recommended act is taken in its record form —
the Stage 6 outcome record's Round J addendum states the
six-value discrepancy exactly, records the table's
provenance as UNRESOLVED (the attribution to the edition
of record's signary is not presently checkable to a
passage supporting the exact enumeration), and records
the verified input-impact result (§0: the 33 distinct
observed values lie in both repertoires and none is in
the set difference, so ETE-1's GOOD is unaffected under
either table). No corrected checker execution is run: any
such run follows its own §8 registration, and the
registered design's completion is not permission to rerun
it informally. ETE-1's word stands as registered. No
Spec 096 verdict and no deposited-paper sentence is
affected; no v5 arises.

### 2.2 J-E-2 — APPLY (done at this landing)

The unit: annotate ETE-2's guaranteed GOOD. All 70 checked
classes are singletons, leaving zero within-class pairs of
value-carrying marks that could expose a merger; the word
is forced by class cardinalities before the syllabary
values are consulted, and the outcome and solution-register
entries report the 70 homogeneous classes without stating
the zero-opportunity certificate. The session's advance
kill checks: any filed checked class with at least two
non-exempt marks defeats the calculation; a binding ETE-2
rule additionally testing cross-class correspondences or
actual value assignments could defeat the asserted
guarantee; an already-filed explicit annotation of the
guarantee would defeat the need to add one.

Adjudication: the certificate is recomputed from the filed
outputs at §0 and holds exactly (35 + 35 singleton classes;
one `?` class in each partition; Q = 0). The registered
ETE-2 predicate as filed in the Stage 6 registration and
script is the within-class distinct-value test only — no
cross-class or assignment term exists to defeat the
guarantee — and no annotation of the guarantee stands in
the Stage 6 outcome record or the seed-and-iteration log.
All three kill checks run, none met. The act: the Stage 6
outcome record's Round J addendum appends the certificate
in the session's formulation (ETE-2 returned GOOD under
its registered non-merger rule; all 70 checked classes are
singletons, leaving zero within-class pairs of
value-carrying marks; homogeneity is therefore guaranteed
by the partitions and supplies no nontrivial external
corroboration of a class merger or class-discovery
ability), and the seed-and-iteration log's Iteration 6
note carries the same qualification at the gate summary.
ETE-2's registered GOOD, its counts, and the historical
tables are retained unchanged. No looser partition, new
corpus, or new gate is commissioned to make the comparison
informative. Interpretation and record only; no Spec 096
consequence.

## 3. Meroitic — no units advanced (direct-inspection null)

The session worked at direct-inspection level: it pinned
the repository at `c5c5f4bc`, read the L4/L5 registrations
and outcomes and exercised their derivation functions,
read the L6 registration and outcome and exercised the
Meroitic checker functions in isolation, independently
reconstructed the Meroitic L4 partitions (successor 24,
predecessor 23, joint 31; the only non-singleton joint
class {6, 9}) and the L5 role, identity, and overlap tables
(32 identity classes; overlap degrees 242 / 235 / 18 / 1 /
0 over the 496 pairs; the sole degree-3 pair {6, 9},
separated by its counts 10 against 7) from the filed
L2–L3 outputs — all matching the filed results — and ran
six synthetic L4/L5 fixtures on both filed implementations
against independent oracles (agreement throughout,
including the fixture in which identical contexts with
unequal frequencies retain L4 identity and split L5
identity). For G-MER it checked the three words from the
registered rules as exact fractions against the 19/20
tolerance (MER-2 at 725/737 and MER-3 at 2,857/2,880
reproducing from the filed L3 rows), ran three synthetic
gate fixtures and five threshold cases (rejection below
95% and acceptance at exactly 95% and above), and found
the disclosed first-run implementation-B defect already
repaired in the filed script, with no evidence warranting
reopening it. It re-downloaded the deposited v4 (SHA-256
`12034315…`, byte-identical) and recounted the
recommendations ledger in agreement (§0). It stated its
evidence boundary plainly: aggregate consistency and
exercised code behaviour, not a custody-corpus replay or
semantic validation; the review does not adjudicate G-IND
or G-ETE. It advanced no recommendation, flagged no
settled item for reopening, and proposed no Round J ledger
row.

The null is accepted and recorded as a **null on direct
inspection**. It adds no row to the recommendations
ledger. No paper item arises; no Meroitic v5 is prepared.

## 4. Owner decisions arising

None. The round's two units are record acts inside the
Spec 105 package, discharged at this landing under the
loop's standing discipline; nothing is proposed that would
need the owner's decision, and no settled owner decision
is reopened.

## 5. Tallies

Two units: 1 APPLY (J-E-2), 1 APPLY WITH MODIFICATION
(J-E-1), 0 DO NOT APPLY, 0 carried to owner decisions —
**both Eteocypriot, both sustained and done at this
landing**. Indus
returned a brief-level null (seventh consecutive);
Meroitic returned a null on direct inspection.

Ledger after this landing: **130 rows — 78 done, 31
accepted, 0 open, 21 rejected** (the pre-landing 128 rows
recounted from the data rows at §0, plus J-E-1 and J-E-2,
both Eteocypriot and both done; Eteocypriot now 38 rows —
19 done, 11 accepted, 0 open, 8 rejected; Indus and
Meroitic splits unchanged).

Diminishing returns, Rounds D–J (units per round):

| Round | Indus | Eteocypriot | Meroitic | Total |
|---|---|---|---|---|
| D | 0 | 2 | 3 | 5 |
| E | 0 | 3 | 3 | 6 |
| F | 0 | 0 | 1 | 1 |
| G | 0 | 1 | 1 | 2 |
| H | 0 | 0 | 0 | 0 |
| I | 0 | 0 | 0 | 0 |
| J | 0 | 2 | 0 | 2 |

Round J breaks the all-null run, and the shape of the
break is the read: the round's yield came entirely from
the completed sandbox's boundary gate, the one place in
the new material where a sandbox-derived structure touched
an outside table — and what the session found there is
that one outside table's provenance does not reconcile
with its checked references (J-E-1) and that the second
comparison's GOOD was guaranteed by construction (J-E-2).
The derivation rungs themselves (L4, L5) reproduced exactly
under independent reconstruction in both inspecting
sessions, and the Indus gate's predictive result was
accepted at its registered scope by the Indus session
itself. Indus has now returned seven consecutive nulls
(D–J) on the decipherment questions, and the binding
constraints there remain external (correspondence replies,
owner-gated acquisitions such as Spec 102, corpus release).
On the pattern of Rounds F–J, a further sweep has something
new to assess when an external input moves or a new
registered stage lands; the completed Spec 105 design
supplies no further stages.

## 6. Round K timing

Nothing was published in this round: no new version of any
paper was prepared or deposited, so no post-publication
wait runs. Under the loop's standing definition, **Round K
falls due immediately**. Its briefs carry no new sandbox
material — Spec 105's registered design is complete and
its Stage 6 record now carries this round's addendum —
so Round K's assessable delta is whatever lands between
this adjudication and its dispatch: external replies under
watch, any newly landed registered work, and the record of
this round itself.

**AI disclosure:** this adjudication was executed by an AI
agent (Muse, via Muse) at the direction of Tristen
Pierson, per constitution sec. VI.
