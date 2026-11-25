# Co-scientist Sweep (Round E) 2026-11-25 — Adjudication

**Date of adjudication:** 2026-11-25.
**Programs:** Indus (Spec 091/098/099/100 line), Spec 096
(Eteocypriot), Spec 097 (Meroitic); the round's findings also
reach Specs 103, 104, and 106.
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
sessions, continued — fired 2026-11-25 ~17:31–17:36 ET
through the tower-compute automation Brave route, after the
loop's one-hour post-publication wait on the v3 releases of
2026-11-25 had expired (~09:44 ET). Each brief was sent
verbatim from its filed `MESSAGE.md`; the composer text was
verified byte-for-byte against the filed brief (character
length and FNV-1a checksum) before each send, because the
composer ignores programmatic fill until a genuine keystroke
lands. Captures are filed at the goal's
`hidden_files/coscientist-sweep-2026-11-25/<program>/`
(`MESSAGE.md`, `OUTPUT.md`, `SESSION-RAW.json`,
`CAPTURE-NOTE.md`, `STAGING-NOTE.md`, plus the sessions'
own output files where written).

- **Indus:** session `192b25f3-cb7b-46b4-acfa-1c1eea4e41fb`.
  Brief SHA-256
  `4feb3f8e21261e59ddfd62f2ee3d53550c4987d06fce9751a24ad65cb81d7ace`;
  OUTPUT.md SHA-256
  `c0e56cc0844c5c8e6f791d36e02571137d7808a9f9b7d7d77223fbc33caf1bfe`;
  SESSION-RAW.json SHA-256
  `e411a44be83b7107c02a997780002a3843282c6d3bf33f86c4cf6693858940c1`.
  The session wrote no output file.
- **Eteocypriot:** session
  `1828e4db-cc7b-434a-891a-12aca9ad1b8a`. Brief SHA-256
  `5821986ba37778d7b8e987771f860942d1263926f47df3191d42ea193c2a2be7`;
  OUTPUT.md SHA-256
  `ce73f65ea7745cf5ef4976b97921309654c0413cfa3fb3256d565d02e171f3b0`;
  SESSION-RAW.json SHA-256
  `b8aeab52f22b0a5c045b3f846724be41ba223dd88f378fb0cefed78b94b0d52e`.
  The session also wrote `eteocypriot-round-e-review.md`
  and `eteocypriot-round-e-independent-checks.json`, both
  captured in full in the goal folder.
- **Meroitic:** session
  `11cac4f7-f109-4fac-bbb5-c670eb33b291`. Brief SHA-256
  `5e06e14130d574867c7bc7ae626f1b5df211dddff3f3ebd7cf13fe725b713837`;
  OUTPUT.md SHA-256
  `a5d3142d4ea5e77ce0d45311bd853c2dc70d02c1ec6807780e794775b0645fde`;
  SESSION-RAW.json SHA-256
  `3cebdbc690ee9551d718739158942993a757422c9c2155f6efb9e2b28678a1d4`.
  The session also wrote `meroitic-round-e-2026-11-25.md`
  and `meroitic-round-e-checker-tests-2026-11-25.json`,
  both captured in full in the goal folder.

Each session's working tab was closed once its captures
were verified (owner tab discipline). Adjudication was
against the primary record: the deposited v3 papers (release
sources and Zenodo records 24533693 / 24533707), the repo
records at head `d0704843` (the head both inspecting
sessions worked from), and the ledger. Every quantitative
or code-level claim in the round was independently
recomputed or re-read before adjudication:

- **E-E-1:** Spec 104's plan.md Stage 1 stop rule and
  TC-104-02 read verbatim; the Spec 104 registration
  record, plan, test cases, and history ledger searched
  for any pre-execution waiver, deviation provision, or
  "content gate" language — none exists; the phrase
  appears only in the outcome record itself. The
  Eteocypriot v3 paper's §5.4 was read in the release
  source: the freeze pin "was deliberately not re-set,
  because the pin names the executed bytes."
- **E-E-2:** recomputed on tower-compute from the filed
  generator. The raw-output file checked is SHA-256
  `c7b634d7f8bf6d13b85149ac7e305568d771f07d38ba6d2b45cadda997f3881e`,
  the same bytes the session checked. All six synthetic
  witnesses verify: distinct columns, every selected score
  equal to its row maximum, totals equal to the
  row-maxima bound and to the filed ILP optima
  (10 / 14 / 24 / 32 / 40 / 48). The largest single-bit
  flip deltas at the returned solutions reproduce exactly
  (−38 / −75 / −159 / −259 / −371 / −565). Two hundred
  random feasible points on the 12×48 instance show no
  nonnegative single-bit flip, consistent with the
  barrier algebra.
- **E-E-3:** the v3 release source's Scope-section
  quotation compared clause by clause with the OD-C-1
  amended wording (refresh adjudication record §14). The
  added clause is absent from the quotation; no
  superseded label is present.
- **E-M-1:** the filed Spec 103 execution script is
  SHA-256
  `661f0afc1e5e993c9536be5f42fb4f5ac9e86ea5bac1de80f7c31afc8017531a`,
  the bytes the session tested. Spec §3.4's definitions
  read verbatim. Both counterexamples reproduced on
  tower-compute against the filed functions, isolated
  without editing their logic: (1) witnesses
  {soreyi, ato} at a counted locus classify FAITHFUL
  with witness verdicts {attests_form, absent};
  (2) `expansion_tokens` on the record `[soreyi?]`
  returns `["soreyi"]`, which attests the form as an
  exact match. The filed aggregate results were scanned:
  the 14 counted loci carry no mixed witness-verdict
  set; near-form loci are carried as census counts, not
  per-locus verdicts, in the filed results.
- **E-M-2:** the v3 release source's closing canonical
  block compared with OD-22 (refresh adjudication §12)
  and OD-C-5 (§13). The block quotes OD-22 and presents
  it as the current canonical wording; no historical
  designation appears anywhere in the paper.
- **E-M-3:** Spec 106 framework §§7–8 read at head; the
  overlap is as the session states (§2 below, §3.3).

**Standing consequence statement: no standing, class,
verdict, or tally moves on this round.** The standings
remain 3 E + 66 I + 4 R + 3 P + 18 U = 94 (Indus); the
Spec 096 verdicts stand (C096-1 NOT SUPPORTED, C096-2 TOO
THIN, C096-3 NOT ENGAGED, C096-4 SUPPORTED in narrowed
form); the Spec 097 Leg A tallies, Stage 4.2 UNDECIDABLE
AT THIS POWER, and the Stage 4.4 bounded PARTIALLY
SUPPORTED stand; Spec 103's CLAIM STANDS outcome and its
six-form table stand; Spec 104's certified optimum (6)
and its scaling measurements stand as measurements. One
ledger row (D-M-3) is reopened in a narrow scope (§3.1),
and two settled rows (C-E-2, C-M-26) gain dated
annotations recording an incomplete propagation leg
(§2.3, §3.2). The round's six units are all record,
checker, framework, or paper-propagation findings; none
is new evidence about any language.

## 1. Indus — no units advanced

The session returned a null: "Round E verdict: second
consecutive null." No new recommendation, and no settled
row challenged. Its reasoning, in substance: the T501
recomputation is a provenance advance, not reading
validation (the limit recorded at D11); Spec 105's
sandbox derivation is not an external test, and the
sealed reserve's existence alone does not justify
spending it; Spec 106 is a framework with no instance
spawned, so "run something in the framework" would be
activity, not a motivated recommendation; the history
ledgers improve traceability, not evidence.

The session disclosed that it did not independently
inspect the v12 paper, the T501 recomputation, the new
specs, or the full ledger. The null is therefore accepted
and recorded as a **brief-level assessment**, exactly as
Round D recorded the Round D Indus null. Per the Round D
adjudication §1 pattern, a null round adds no row to the
recommendations ledger. No paper item arises; no Indus
v13 is prepared.

## 2. Eteocypriot — 3 units

### E-E-1 — The Spec 104 pin deviation: stop-rule departure and the F-104-1 framing: APPLY WITH MODIFICATION

The session's priority-1 finding, sustained on the filed
record in every part:

1. Spec 104's registered plan made pin verification a
   stop condition ("if a step cannot be performed as
   registered — the corpus pin fails … — execution stops
   at that step … and no substitute procedure is
   improvised"), and TC-104-02's pass condition is
   conjunctive: "the pin verifies; the recomputed matrix
   equals the filed E1 run record's `lccs_by_segment`."
2. The execution logged the pin mismatch and proceeded
   on the matrix agreement, recording TC-104-02 as
   "PASS WITH DEVIATION F-104-1". No pre-execution
   waiver, amendment, or registered "content gate"
   exists in the Spec 104 package or its history ledger;
   the outcome record's phrase "the registered content
   gate" names no text in the registration. The
   continuation was therefore a departure from the
   registered stop rule, recorded here as such. (The
   program's own report to the owner on 2026-11-25
   described the deviation as filed and accepted; that
   acceptance was post-execution and is not a registered
   waiver, and this record does not retroactively make
   it one.)
3. The historical pin is not stale and is not erroneous.
   It identifies the original frozen bytes: the session
   recovered the blob from commit `173882a2` and rehashed
   it to `5077285e…`, agreeing with F-104-1's own evidence
   chain. F-104-1's disposition — that "refreshing it
   (and the driver's constant) is a Spec 096
   housekeeping act" — conflicts with the adjudicated
   F-2 / OD-C-2 design and with the deposited v3 paper's
   §5.4 ("the freeze pin was deliberately not re-set,
   because the pin names the executed bytes"). A pin
   refresh would make the historical record less exact,
   not more.

**Disposition: APPLY WITH MODIFICATION.** The acts land
with this adjudication as a dated note appended to the
Spec 104 outcome record: (a) TC-104-02 is recorded in two
conjuncts — pin conjunct FAILED, matrix conjunct PASSED
(cell for cell) — superseding the "PASS WITH DEVIATION"
label; (b) the continuation is recorded as a departure
from the registered stop rule, with no waiver on file;
(c) F-104-1's refresh instruction is withdrawn; the
historical freeze pin stands, and no Spec 096
housekeeping refresh is owed. A future benchmark that
consumes a corpus registers a pin for the bytes it
consumes; it does not re-point a historical freeze pin.
The modification to the session's ask is form only:
program records are corrected by dated notes, never by
rewriting the filed text, so F-104-1 itself stands with
this note governing its reading. No numerical result is
affected: the consumed bytes are proven identical in
every driver-read field to the E1 run's bytes by the
recomputed matrix and the field-level diff, so the
certified optimum and the Spec 096 verdicts are
untouched. The session's kill check (a pre-execution
authorized amendment) was run and not met.

### E-E-2 — The Spec 104 benchmark's assignment structure: APPLY

Sustained, and verified by independent recomputation
(§0). The benchmark's problem is a rectangular max-weight
assignment. All six synthetic optima attain the elementary
sum-of-row-maxima bound, so each carries a search-free
optimality certificate (witnesses in the session's
independent-checks file, each re-verified at adjudication
against the regenerated matrices). The real instance does
not attain its bound (8 against the certified 6), which is
why it alone needed the exhaustive and ILP certification
it received. Separately, under the registered penalty
P = 1 + Σs and single-bit proposals, every feasible
assignment is a strict one-bit local maximum: removing a
selected bit changes F by −s−P, adding a bit in an unused
column by s−P, and adding one in an occupied column by
s−2P, all negative for nonnegative scores. The measured
SA decline with size is therefore a property of the
encoding and proposal set acting on these instances, not
evidence that the underlying assignment problem hardens.

**Disposition: APPLY.** An analytical supplement carrying
the witnesses, the bound argument, and the barrier
calculation is appended to the Spec 104 outcome record
with this adjudication, in the session's suggested form
and with its scope limits stated: the supplement does not
apportion the observed SA gap between barrier-escape
difficulty and the fixed proposal budget, and the
assignment-easiness statement is a property of this
benchmark's score matrices, not of assignment problems
generally. No new timing campaign is commissioned. The
outcome record's measurements stand as measurements of
the registered implementation; the supplement governs
their interpretation.

### E-E-3 — The deposited v3 paper quotes the superseded canonical description: APPLY WITH MODIFICATION

Sustained. The v3 paper's Scope-section quotation (p. 9)
carries the OD-12 form of the canonical public
description. The OD-C-1 amendment (adopted 2026-11-23,
refresh adjudication §14) added the clause stating that
the executable leg recovered one of two correspondences
against its two-correspondence criterion and was executed
under a deviation from the registered A2. That clause is
absent from the deposited quotation, and the quotation is
nowhere labelled superseded. The amendment did reach the
repository records and the Zenodo v3 record description;
its propagation into the paper's own quotation — the
surface §14 named ("takes effect on the v3 release
surfaces") — is incomplete. The session's kill check
(the checksum-matching PDF containing the clause, or a
superseded label) was run against the release source and
not met.

**Disposition: APPLY WITH MODIFICATION.** Row C-E-2 gains
a dated annotation recording the incomplete PDF leg, with
this unit as its pointer; C-E-2's status is not reopened,
because the adoption it records stands and the open leg
is exactly this unit's act. The paper act is filed as
this unit's own row: Eteocypriot v4 substitutes the
amended quotation, dated in the paper as amended
2026-11-23, with no other text change. The substituted
text is the already-adopted OD-C-1 wording, not new text;
under the loop's standing publish instruction the v4
release proceeds (Zenodo first, then Academia;
ResearchGate trailing under the shared daily budget, the
2026-11-26 budget being fully committed). The row stands
**accepted** at this landing and is marked done when the
v4 deposit verifies, by addendum to this record.

## 3. Meroitic — 3 units

### E-M-1 — The Spec 103 checker does not implement §3.4 as written: APPLY WITH MODIFICATION (narrow reopening of D-M-3, checker conformance only)

Sustained on reproduction (§0). Two deviations from the
registered classification rule, both in the executed
checker (filed script SHA-256 `661f0afc…`):

1. `classify_counted_locus()` returns FAITHFUL as soon as
   any witness attests the form. Section 3.4 defines
   FAITHFUL as "every available witness agrees with the
   ingested text at the locus" and DISCREPANCY to include
   a witness showing a different token at the locus. A
   locus whose witnesses disagree (verdicts attests_form
   and absent) is classified FAITHFUL by the code.
2. `expansion_tokens()` replaces `[`, `]`, `?`, `!` and
   other markup with separators before classification, so
   an explicitly qualified witness token (`[soreyi?]`)
   becomes an unqualified exact match and can attest the
   form as FAITHFUL, with no uncertainty flag retained.
   Section 3.4's UNCERTAIN covers exactly the damaged or
   ambiguous witness, "bracketed or partial signs"
   included.

Scope, as the session bounded it and as adjudication
confirms: the filed aggregate results contain no counted
locus with a mixed witness-verdict set (14 counted loci
scanned), so deviation 1 is not shown to have masked any
actual disagreement in the executed payload. Whether
deviation 2 affected any historical classification is
indeterminate from the filed aggregate, which does not
preserve raw uncertainty markup. The unit supplies no new
evidence about the unwitnessed Shablul texts, and the
Stage 4.4 table is untouched.

**Disposition: APPLY WITH MODIFICATION.** D-M-3 is
reopened in the narrow scope of checker conformance only;
its CLAIM STANDS outcome and the six-form table are
preserved and are not reopened. The acts: (a) a
conformance annotation is appended to Spec 103's outcome
record with this adjudication, carrying both deviations,
the counterexamples, and the scope bounds above; (b) the
checker repair is recorded as the follow-on act, to be
executed as a Spec 103 conformance addendum under this
adjudication: witness aggregation corrected so
disagreement is explicit (no any-witness pass);
uncertainty markers retained through classification;
both counterexamples added as regression tests; an audit
of already-held witnesses for uncertainty-bearing
candidate loci, replaying only affected classifications
under the corrected implementation. No REM acquisition,
no split change, no new witness source. Where the frozen
tokenization and §3.4's classification definitions
conflict, the addendum states the adjudicated treatment
before any revised execution; nothing is silently
rewritten. The row stands **accepted** until the addendum
executes. The session's kill check (a different deciding
script, a licensing registered rule, or non-reproduction)
was run and not met.

### E-M-2 — The deposited v3 paper still presents the superseded OD-22 summary as canonical: APPLY

Sustained. The v3 paper's closing canonical block (p. 12)
introduces "The program's canonical public wording for
this work, adopted on 2026-11-22…" and quotes the OD-22
summary. OD-C-5 (2026-11-23) adopted the replacement
summary in whole, and the Zenodo v3 record description
carries the OD-C-5 text; the paper block does not, and
nothing in the paper designates the block historical.
Section 13 of the refresh adjudication named the v3
release as the vehicle for surfaces still carrying OD-22;
the paper's own block was missed. This is a propagation
failure of settled row C-M-26, not a re-recommendation,
and the session asks for no re-adoption.

**Disposition: APPLY.** Row C-M-26 gains a dated
annotation recording the incomplete paper leg, with this
unit as its pointer. The paper act is filed as this
unit's own row: Meroitic v4 replaces the p. 12 canonical
block with the OD-C-5 text, credited as adopted
2026-11-23 superseding the 2026-11-22 summary, with no
other text change. The substituted text is the
already-adopted OD-C-5 wording, not new text; under the
loop's standing publish instruction the v4 release
proceeds (Zenodo first, then Academia; ResearchGate
trailing, as for E-E-3). The row stands **accepted** at
this landing and is marked done when the v4 deposit
verifies, by addendum to this record.

### E-M-3 — Spec 106's §7/§8 status aggregation is not mutually exclusive: APPLY

Sustained on the framework text. Section 7's "dead"
outcome ("the claim derives in no surviving instance, or
every instance deriving it has died") is mapped by §8 to
REFUTED-IN-ENSEMBLE, while §8 separately defines
UNDERIVABLE as "the tested axiom sets do not settle it".
A nonempty surviving ensemble in which every instance
returns UNDERIVABLE satisfies §7's dead condition while
nothing has refuted the claim; an all-UNTRANSLATABLE
ensemble is likewise swept into "derives in no surviving
instance"; and with zero survivors the §8 conditions that
quantify over surviving instances are vacuous while
UNTESTED also speaks to "no surviving instance". No
precedence or aggregation rule in the framework or the
templates resolves the three cases. No instance has been
spawned, so no result is affected; the defect is in the
instrument, found before first use — the cheapest moment
to fix it.

**Disposition: APPLY.** A dated clarification is appended
to the framework at §8 with this adjudication, registering
a mutually exclusive aggregation table before any scored
instance runs: no surviving instance returns no ensemble
status (model exhaustion is recorded, never refutation;
the claim stays UNTESTED); an all-UNTRANSLATABLE ensemble
is a coverage failure, preserved as such; REFUTED-IN-
ENSEMBLE requires at least one surviving instance and a
surviving instance deriving the claim's negation; a
surviving ensemble deriving neither the claim nor its
negation returns UNDERIVABLE; mixed derivation splits are
AXIOM-TRACKING only where a named axiom set discriminates
them exactly, otherwise UNDERIVABLE with the split tallied
in the iteration log. The framework's original text is
untouched; the clarification governs its reading. The
session's kill check (a binding pre-existing aggregation
rule covering all three cases) was run against the
framework and templates and not met.

## 4. A brief-fidelity correction, recorded against the program

The Round E Meroitic brief stated that paper item M-P8's
two v3 sentences state the binomial-to-permutation tail
ratios (2.50 / 2.96) explicitly. The session read all 13
pages of the deposited v3 and reports the sentences carry
the model-conditionality caveat without the numeric
ratios; adjudication confirms this against the release
source (the ratios appear nowhere in the v3 text; they
stand in the Round D adjudication record and the Spec 097
record). The session treated the substantive caveat as
adequate and did not reopen D-M-1; this record agrees,
and no act arises. The overstatement came from the
program's own v3 summary in PROGRAM-STATE, which is
corrected in its Round E entry. The correction is recorded
here because the brief is a program artifact: the round's
inputs are part of its record.

## 5. Owner decisions arising

None requiring a decision this round. The two paper items
(E-E-3, E-M-2) substitute wording the owner already
adopted (OD-C-1, OD-C-5) into the one surface that missed
it, and proceed under the loop's standing publish
instruction; no new paper text is proposed anywhere in
this round. The Spec 103 conformance addendum (E-M-1) is a
correction of the program's own checker against its own
registration, on already-held material, and is recorded
here as commissioned follow-on work, not as an owner
decision. The E-E-1 stop-rule departure is reported as a
fact of record: it is not ratified retroactively, and no
number in any study depends on ratifying it, because the
matrix identity — not the pin — is what the results rest
on, and the matrix identity is independently verified.

## 6. Tallies

Six units: 3 APPLY (E-E-2, E-M-2, E-M-3), 3 APPLY WITH
MODIFICATION (E-E-1, E-E-3, E-M-1), 0 DO NOT APPLY, 0
carried to owner decisions. Indus: null, no row.

Ledger after this landing: **125 rows — 70 done, 34
accepted, 0 open, 21 rejected.** The count is recounted
from the data rows. This landing also corrects the
ledger's Counts table, which was stale: it showed 64 done
/ 34 accepted, predating the 2026-11-25 moves of D-E-2,
D-M-1, and D-M-2 to done on the v3 deposits (recounted
pre-round position: 119 rows — 67 done, 31 accepted, 21
rejected). Round E adds six rows: E-E-1, E-E-2, and E-M-3
done at this landing (their acts are the dated notes and
supplements filed with it); E-E-3 and E-M-2 accepted,
moving to done when the v4 deposits verify (addendum to
this record); E-M-1 accepted, moving on the conformance
addendum's execution.

**AI disclosure:** this adjudication was executed by an AI
agent (Muse, via Muse) at the direction of Tristen
Pierson, per constitution sec. VI.

## 7. Addendum — the v4 releases (2026-11-25)

The two paper items discharged the same day, under the
loop's standing publish instruction (venue order: Zenodo,
then Academia, ResearchGate last under the shared daily
budget).

- **Eteocypriot v4** (unit E-E-3): Zenodo record 24545017,
  DOI 10.5281/zenodo.24545017 (concept
  10.5281/zenodo.24449059), file
  `eteocypriot-alignment-v4.pdf`, 10 pages, PDF SHA-256
  `f3f6a343d2f9646ea0a5c6bbf9ff8e93434eb1e77159251c49c6522044fcaa71`.
  The single change from v3 is the Scope-section quotation,
  which now carries the amended (2026-11-23) form of the
  canonical description. Academia work 181628208 updated
  in place (v4 attachment, DOI field, listing text set to
  the Zenodo v4 description) and verified on the live page
  the same day. Release record: v4 addendum in
  `specs/096-eteocypriot-program/records/release-record-2026-11-22.md`.
- **Meroitic v4** (unit E-M-2): Zenodo record 24545036,
  DOI 10.5281/zenodo.24545036 (concept
  10.5281/zenodo.24449061), file
  `meroitic-reproduction-benchmark-v4.pdf`, 13 pages, PDF
  SHA-256
  `1203431526ba7eea9828e86941bea96e14f7e0b455c577df6755f041ee30aa81`.
  The single change from v3 is the closing canonical
  block, which now prints the OD-C-5 summary adopted
  2026-11-23. Academia work 181628423 updated in place and
  verified on the live page the same day. Release record:
  v4 addendum in
  `specs/097-meroitic-reproduction-benchmark/records/release-record-2026-11-22.md`.
- **ResearchGate trails:** publications 418211795 and
  418214318 are scheduled to receive their v3 updates on
  2026-11-26 under the shared account-wide budget (that
  day's three changes are fully committed: the Riemann
  retry and the two v3 updates). The v4 updates therefore
  trail to a later day under the same budget and are
  recorded here as trailing, not forced. Zenodo is the
  record of record.
- **Ledger:** rows E-E-3 and E-M-2 stand done on this
  evidence. Totals after this addendum: **125 rows — 72
  done, 32 accepted, 0 open, 21 rejected.** Row E-M-1
  remains accepted on the Spec 103 conformance addendum.
- **Loop wait:** the 1 hour post-publication wait runs
  from the Zenodo publications of 2026-11-25 (~23:03Z /
  18:03 ET). **Round F falls due after ~19:03 ET on
  2026-11-25.**

## 8. Addendum — the Spec 103 conformance addendum executed (2026-11-25)

Unit E-M-1's follow-on act is discharged the same day.
The conformance addendum was registered before any
revised execution ran
(`specs/103-meroitic-source-witness-check/records/conformance-addendum-registration-2026-11-25.md`,
stating the adjudicated treatment where the frozen
tokenization and §3.4's definitions conflict), then
executed on tower-compute against the pinned build
(outcome record:
`specs/103-meroitic-source-witness-check/records/conformance-addendum-outcome-2026-11-25.md`;
machine results: `conformance-addendum-results-2026-11-25.json`
in the same records folder).

- **Repairs.** The corrected checker
  (`records/conformance-addendum-script.py`; the filed
  Stage 1 script is not edited) aggregates witnesses so
  disagreement is explicit — FAITHFUL only on unanimous
  unqualified attestation, an attestation coexisting
  with an absence is DISCREPANCY — and retains
  uncertainty markup as a per-token flag through
  classification, an attestation resting only on flagged
  tokens being an uncertain attestation.
- **Regression tests.** 10 tests, all PASS
  (`records/conformance-addendum-tests.py`): both
  counterexamples classify as filed under the control
  implementation and as §3.4 requires under the
  corrected one; the preserved behaviours are asserted
  for both.
- **Replay.** Step 1 reproduces the filed basis and
  counts exactly; the control implementation reproduces
  the filed classifications and verdicts at all 47 loci
  (14 counted, 33 near) with 0 mismatches; the corrected
  classifications are identical at every locus.
- **Bounds.** Deviation 1: 0 of the 14 counted loci
  carry a mixed filed witness-verdict set — the
  any-witness pass masked no actual disagreement.
  Deviation 2: markup incidence across all 25 held-out
  witnesses is 0 — its historical impact, indeterminate
  from the filed aggregate at adjudication, is bounded
  at zero within the held witnesses.
- **Outcome.** The unchanged Step 4 machinery on the
  corrected classifications returns the filed six-form
  table exactly (CLAIM STANDS for soreyi, xolkete,
  pxolkete, xolkte, wisi; asoreyi NOT CHECKED —
  INCOMPLETE COVERAGE). D-M-3's outcome is preserved on
  replay evidence.
- **Ledger:** row E-M-1 stands done on this evidence.
  Totals after this addendum, recounted from the data
  rows at its landing (which follows the Round F
  landing, PR #744): **126 rows — 74 done, 31 accepted,
  0 open, 21 rejected.** No OWNER DECISION arises; no
  standing, verdict, or tally moved.
