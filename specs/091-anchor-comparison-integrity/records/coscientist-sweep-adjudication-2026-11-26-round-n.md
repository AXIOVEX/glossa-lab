# Co-scientist Sweep (Round N) 2026-11-26 — Adjudication

Round N was a full three-program sweep under the owner's
keep-working direction (reaffirmed in the Glossa-Lab chat
2026-11-26 ~14:23 ET: work all day without stopping, with
the Co-scientist work run where appropriate), briefed as a
fresh robustness pass over each program's current record:
any claim whose stated support does not match its filed
evidence, any record that contradicts another, and the
single highest-value next step with its falsifier. All
three sessions are the standing Round D sessions,
continued. Captures are filed verbatim at the goal's
`hidden_files/coscientist-sweep-2026-11-26-round-n/<program>/OUTPUT-round-n.md`.

## 0. Inputs and method

**Pin.** All three briefs pinned at AXIOVEX/glossa-lab
main `0b377f6f7a6cf3ba0f0e65f5e71193eb2b57873e` (PR #765's
merge). This adjudication was landed against the live
head `79e0e806` (PR #766, the ELSEWHERE methods paper's
release record); the intervening delta touches no record
any unit rests on.

**Sessions and sends.** Indus
`192b25f3-cb7b-46b4-acfa-1c1eea4e41fb` (brief 4,029
characters, FNV-1a `82dd3d04`); Eteocypriot
`1828e4db-cc7b-434a-891a-12aca9ad1b8a` (4,102 characters,
FNV-1a `a8a18d46`); Meroitic
`11cac4f7-f109-4fac-bbb5-c670eb33b291` (4,393 characters,
FNV-1a `a72b4ef8`). Each send was verified by length and
checksum in a separate invocation before sending, under
the standing composer discipline. Captures: Indus 46,510
bytes, SHA-256
`dd3c569150eddcce37c99619ee1f17a4e89b5a31c645d3d4f33dda06733cb048`;
Eteocypriot 40,495 bytes, SHA-256
`72c2e19c1a9b18ddc9a73d0735588e4fec180e802681042a2fa6f729a1ff3026`;
Meroitic 14,872 bytes, SHA-256
`f69836c959e1321f8978a45dc1c26478c556b1e82d271253bafb9fd09a48bdf4`.

**Method.** Each unit was adjudicated against the filed
records at the pin, not against the session's summary of
them: the Stage 6 registration, execution script, and
filed L2/L3 tables for N-I-1; the Stage 6 outcome's own
two passages for N-I-2; the deposited v12 text, the
Spec 099 amendment chain, and the register-wording
addendum for N-I-3; the ensemble seed, outcome, and
framework §§2/6/8 for N-E-1; the three baseline templates,
the registered test cases, and the filed census audit for
N-E-2 (the audit was re-run at adjudication, and the
corrected audit's rejection fixtures were executed); the
deposited v4 text, the pinned E1 driver, and the filed
RT5-05 correction for N-E-3. Advance kill checks stated by
the sessions were run in each case; the dispositions below
record which were met.

**Outcome in brief.** Indus returned four units — its
first non-null round since the brief-level nulls began
(Rounds D–K): N-I-1 APPLY, N-I-2 and N-I-3 APPLY WITH
MODIFICATION, N-I-4 DO NOT APPLY. Eteocypriot returned
three units: N-E-1 APPLY WITH MODIFICATION, N-E-2 and
N-E-3 APPLY. Meroitic returned an explicit null. Six
ledger rows are added, all done at this landing. No
standing, verdict, or tally in any program moves; no paper
is edited; nothing is published.

## 1. Standing positions, unchanged

Indus: the script is not deciphered and no correctness
probability is claimed for any reading; standings of
record 3 E + 66 I + 4 R + 3 P + 18 U = 94 strict core of
287 registered anchors. Eteocypriot: the script
transliterates, the language is not understood, and the
binding constraint is corpus size. Meroitic: the script
was deciphered by Griffith; the language's affiliation is
the open question; no decipherment of the language is
claimed.

## 2. Indus — four units (three landed, one not applied)

### 2.1 N-I-1 — APPLY (done at this landing)

**Unit.** Qualify G-IND's predictive interpretation: the
registered scoring weights are not normalized
probabilities. The session demonstrated, from the filed
Stage 2/Stage 3 tables and `stage-6-execution.py`, that
for a predecessor x the attested-successor pair weights
already sum to 1, and the rule then adds unigram backoff
mass for every known mark outside the successor set with
no discounting and no row normalizer before the
logarithms. Exact witnesses: group start row mass
1.152023; after M342, 1.279273; after M176, 1.287293 (over
the 372 derivation marks). Both checker implementations
implement the same registered construction, so their
agreement is not a normalization check.

**Adjudication.** Sustained on the filed record. The
session's advance kill check — a normalizer actually
applied before every logarithm, or a disjoint sample-space
construction under which the rows sum to one — was run
against the registration and the executed code at
adjudication and not met; the explicit mass sums
contradict normalization directly. Recomputation from the
filed case table reproduces the filed figures (baseline
4.557943, derived 4.178289, difference 0.379654), so no
arithmetic failure is alleged and the historical GOOD
stands as the frozen rule's correct mechanical
consequence. What is not established is an advantage of
0.379654 nats per token in normalized predictive log-loss.

**Discharge.** The dated conformance annotation appended
to `specs/105-elsewhere-sandbox/records/stage-6-outcome-2026-11-25.md`
at this landing: it preserves the registration, raw
output, figures, and historical GOOD; describes the result
as a comparison of the frozen unnormalized scoring rules;
withdraws the normalized predictive-log-loss
interpretation; and names itself the qualification of
record for IND-1's forward citation, including for the
ELSEWHERE methods paper (Zenodo record 24571025,
deposited 2026-11-26), which states the gate figures at
their registered license. The matching qualification is
appended to the Round J adjudication's §1 at the same
landing (that acceptance was brief-level, as it discloses,
and was not an independent normalization check). No silent
rewrite; no NOT-GOOD substitution. A normalized correction
is not commissioned here; if one is ever commissioned it
requires its own registration, must specify its unseen-mark
treatment and unit total explicitly, and must not be tuned
to recover GOOD — and the aggregate case table, which
discards predecessor identities, must not be used to invent
a corrected verdict.

### 2.2 N-I-2 — APPLY WITH MODIFICATION (done at this landing)

**Unit.** Reconcile the Stage 6 outcome's "opened once"
(§5) with its opening account of two full scoring
executions in which "the reserve was opened in both runs".
The session's modification: distinguish first
disclosure from unchanged replay, identify what governs
the replay, and do not recreate a missing first-run log.

**Adjudication.** Sustained as a wording conflict on the
face of one record; no independent finding about access
chronology is made, and nothing in the unit alleges
changed data, adaptive tuning, or a second fresh reserve.
The session's kill check — an already-filed governing
definition and contemporaneous run record reconciling both
passages unambiguously — was run and not met: the outcome
discloses the replay but supplies no such definition.

**Discharge.** The dated execution-chronology addendum
appended to the Stage 6 outcome record at this landing,
distinguishing (a) first release/disclosure (one: in the
stopped run, after the guard passed; nothing was available
to Stages 1–5 before it), (b) checker invocations/content
reads (two full scoring executions, each only through the
G-IND checker after the guard, the second changing no
input, rule, or margin — the sole correction was
implementation B's Meroitic stream read), and (c) the
replay's status as an unchanged re-scoring after first
disclosure. The addendum records as unresolved — rather
than settling by assertion — that no registration
provision expressly governs an unchanged replay after
first disclosure; whether future registrations should
permit or forbid such replays is a prospective question,
not decided here. Record only; the historical GOOD is
unaffected.

### 2.3 N-I-3 — APPLY WITH MODIFICATION (done at this landing)

**Unit.** Reconcile the census snapshots: the deposited
v12's Appendix D.10 states the census of record as 296
items (210 primary), while the current inference log at
the pin holds 299 items (213 primary) — and the two 299s
(original and current) differ in content. The residue: §11
of the register-wording addendum still gives 296/210 with
no forward pointer to the later three-item addition.

**Adjudication.** Sustained on the filed record, with the
modification that the reconciliation is filed as a dated
record and a forward pointer, and no historical record —
and not the paper — is rewritten. Independent recount at
the pin: claims ledger 1,091 entries (1,060 claims + 31
annotations); anchor register 287, strict set 94;
inference log 94 entries, 299 items (213 a + 61 b + 25
ambiguous); executed classes 3/66/4/3/18, agreeing with the
paper's p. 2 standings and its Appendix D.12 anchor count.
The amendment chain explains the drift exactly: original
299 (three duplicated DEDR citations) → deduplicated 296
(the paper's snapshot) → amended 299 (remainder amendment
of 2026-11-22 adding M202-03, M330-03, M124-04; 296 + 2 + 1
= 299, no class or graph-outcome change). The session's
kill checks were run and none met (the recount is not
296/210; the additions are governed by the filed remainder
amendment; §11 carried no pointer). Row B-I-22's recorded
completion is not undone: the residue is propagation after
a later addition, not a failure of the earlier act.

**Discharge.** `specs/099-inference-log/records/current-state-reconciliation-2026-11-26.md`,
filed at this landing: the three populations counted and
named, the amendment chain, the current census of record
(299 items: 213 primary / 61 candidate-system / 25
ambiguous), and the citation discipline (name the object;
items are not texts). A dated forward pointer (§12) is
appended to the register-wording addendum at the same
landing. The paper itself is not edited; any paper change
is a future version on the owner's approval of the actual
text, and any such version states the snapshot transition
explicitly.

### 2.4 N-I-4 — DO NOT APPLY (recorded; no ledger row)

**Proposed inference.** That the VEXA Spec 011 import's
measurement correction (the A3-era census 299 / standings
94 figures do not reproduce against the converted claims
ledger of 1,091 lines) shows a paper standings or census
error.

**Adjudication.** Not applied. The session's recount,
verified at adjudication, shows the three counts name
three different populations (claims-ledger entries,
anchors, inference-log basis items), and the paper's
standings (p. 2) and anchor count (Appendix D.12) agree
with the independently recounted current records. The one
paper/current-head discrepancy established is the
296 → 299 basis-item snapshot transition of §2.3, whose
cause is filed in Spec 099 — not the claims-ledger line
count. The disposition could be overturned only by a
checkable claim-ID/sign-ID crosswalk with the governing
aggregation rules showing the disputed A3 measurement
measured the same population; none is on file.

**Evidence boundary, recorded.** The session could not
access AXIOVEX/vexa (HTTP 404); the import figures (23,661
comparisons, EQUIVALENT-WITH-RECORDED-DIVERGENCES, 2,244
divergences, E2 FAILS) are program-reported to it, not
certified. **R-IP-04 remains the owner's adjudication**;
nothing in this round touches it.

## 3. Eteocypriot — three units, all landed

### 3.1 N-E-1 — APPLY WITH MODIFICATION (done at this landing)

**Unit.** Reconcile the first ensemble's dual use of the
same statements as instance axioms and as checker items
with the framework's evidence/axiom separation rule
(framework §2: the evidence set "is not an axiom of any
instance"; §6: no instance "treats a checker item as
derivable"; Spec 106 §2 repeats the separation). The
ensemble seed's §8 contact point 2 names ETE-CON-03,
ETE-CON-04, and ETE-ENV-03 — axioms in every declared
instance — as the exercised evidence items, and the
negation derivations' load-bearing premise is ETE-CON-03
itself.

**Adjudication.** Sustained, with the session's own
modification of scope: this is a record/method conformance
finding, not a verdict challenge. The reuse was disclosed,
not hidden (the outcome's §4 states the agreement with the
filed record accurately, and §6 disclaims new real-world
content). The session's kill checks were run and neither
met: no binding pre-pass rule permitting the dual role is
on file, and no scoring record shows contact point 2
comparing the derivation against separately identified
evidence. The filed tallies do select REFUTED-IN-ENSEMBLE
under §8.1 (§8.2 governs the positive row only and is not
engaged; coverage was complete), the seed precedes the
outcome in git history (`9bc4d0b8` before `401d4527`), the
translation matches the seed, and G-ETE is consistently
recorded as registered but not exercised. No Spec 096
verdict is proposed or made to change, and the ensemble is
not relabeled UNDERIVABLE.

**Discharge.** The dated conformance note appended to
`specs/106-elsewhere-world-model-templates/records/ensemble-1-outcome-2026-11-26.md`
at this landing, carried into the Spec 106
seed-and-iteration log as a conformance note on Iteration
2: contact point 2's agreement is an inherited-premise
consistency check, not a separate evidentiary test;
ETE-Q-1's REFUTED-IN-ENSEMBLE is retained as a conditional
logical result under the seed's declared translation; any
consistency-only contact distinction is prospective
registration only, not created here. No new ensemble is
commissioned.

### 3.2 N-E-2 — APPLY (done at this landing)

**Unit.** Correct the Eteocypriot baseline's false
domain-count metadata by dated erratum, and make the
census audit implement its registered checks. The
baseline's embedded seed record states 71 axioms with
domain counts GEO 0, POL 0, MOV 0, DNA 0, ECO 0, ENV 0,
CON 0; the numbered axiom lines count GEO 11, POL 12,
MOV 9, DNA 5, ECO 10, ENV 10, CON 14 = 71. TC-106-05
registers recomputation and comparison of counts "by
domain and by kind"; the filed `census-audit.py` compares
the total, kind counts, UNSOURCED count, and axiom hash
but never the domain counts, and its TC-106-02 label
condition admits one or more labels where the test case
requires exactly one. The session ran the unmodified
script at the pin: AUDIT PASS on the false metadata, with
two scratch negative fixtures (an altered domain figure;
a two-label axiom with its hash updated) also passing.

**Adjudication.** Sustained, and extended at landing to
the defect's full family: the identical zero-count
statement stands in all three baseline templates' seed
records (verified at adjudication from the filed files),
and TC-106-05's registered comparison runs over all three
templates, so the erratum and the corrected audit cover
all three. Actual counts, recomputed from the axiom lines
at adjudication: Indus GEO 14, POL 12, MOV 11, DNA 12,
ECO 13, ENV 11, CON 15 = 88; Eteocypriot GEO 11, POL 12,
MOV 9, DNA 5, ECO 10, ENV 10, CON 14 = 71; Meroitic
GEO 12, POL 12, MOV 10, DNA 8, ECO 10, ENV 11, CON 13
= 76. The session's kill checks were run and none met: no
binding erratum at the pin supersedes the zero census, no
registered alternative census rule makes the zeroes
correct, and no prior amendment excludes the comparisons.
The axiom-line hashes recompute unchanged (Eteocypriot
`fca1cc8a…`); no axiom line is touched, and the four
ensemble instance memberships and the aggregation are
unaffected.

**Discharge.** (1) Dated errata appended to all three
baseline templates at this landing, stating the correct
domain counts in prose and in a machine-readable erratum
census line; the historical seed records are preserved
unedited, the errata superseding their domain-count
figures only. (2) `records/census-audit-v2.py`, a
versioned audit implementing the TC-106-05 per-domain
comparison (governing census = the seed statement as
superseded by a dated erratum census line where one is
filed) and the TC-106-02 exactly-one-label check at the
label position (the head of the line must be exactly
`- ID (X)`, optionally followed by the UNSOURCED flag
word — the filed form of three UNSOURCED-sourced lines; a
label token in a line's prose, as in IND-MOV-11's
"retained as (H)", is not a second label). Version 1 is
preserved unedited. (3) Rejection fixtures, executed at
adjudication and filed with the run: an altered erratum
domain count is REJECTED; an axiom given two labels in
label position is REJECTED; the unmodified
errata-corrected templates PASS. The v2 run is filed at
`records/census-audit-v2-output-2026-11-26.txt`. (4) The
historical PASS is qualified, not rewritten: a dated
qualification appended to
`records/census-audit-output-2026-11-25.txt` records that
version 1 passed without implementing the two comparisons,
and the ensemble seed's reliance on "TC-106-02..05 PASS"
inherits that qualification. Record/checker conformance
only; no ensemble re-run follows from it.

### 3.3 N-E-3 — APPLY (done at this landing)

**Unit.** Carry the settled 15-entry STEMS correction
into the paper: deposited v4 §5.2 (p. 7) describes "a
consonant-stem table (sixteen entries, plus a special case
in its letter handling)", while the pinned E1 driver
(SHA-256 `9ec475fd…`, the A2-audit driver) carries a
literal STEMS dictionary of 15 entries and the filed
Round 5 correction RT5-05 (appended to
`outcome-record-amendment-2-correction-2026-11-21.md`)
already established 15, explaining the earlier
double-counting of ξ (whose k+s handling sits in
`letters_of`, outside the dictionary — the sentence's own
special-case clause).

**Adjudication.** Sustained. The session's kill check was
run and not met: no hash-matching executed driver carries
16 STEMS entries, and the deposited wording's "sixteen"
counts the table itself, separately from the special case
it names. This is a propagation residue of a correction
the program had already made, of the same kind as E-E-3's
repaired quotation; it challenges neither RT5-05's
adjudication nor any Spec 096 verdict, and it does not
reopen the owner's title ruling (which the session
verified as internally consistent across the decision
addendum, the C-E-5 annotation, and the deposited title).

**Discharge.** The dated paper erratum record
`specs/096-eteocypriot-program/records/paper-erratum-2026-11-26-stems-count.md`,
filed at this landing: "sixteen entries" is corrected of
record to "fifteen entries", the special-case clause
standing. The deposited v4 is NOT silently replaced; the
corrected wording is carried into the next authorized
paper version, which requires the owner's approval of the
actual text. Paper only; no numerical or verdict
consequence. The session's further confirmations need no
act and are recorded here as confirmations, not units:
the paper's silence on the ensemble is correct (it nowhere
calls ICS 196 a royal dedication, and the ensemble
establishes no new Eteocypriot reading), and its
highest-value next step — completing the already accepted
C-E-15 corpus/test-feasibility decision to a proceed/stop
result — is a priority judgment about existing accepted
work, not a new recommendation, and is not commissioned
by this round.

## 4. Meroitic — explicit null

The Meroitic session returned no new units and no
reopening flags, and the null is accepted as filed. What
it verified, on direct inspection at the pin:

- **M-M-1 is closed at the record level.** The §11
  addendum to the Spec 102 acquisition record documents
  the Appendix custody facts (Cambridge Core order
  1001421; 286,195 bytes; 42 pages, printed pp. 189–230;
  SHA-256 `0a0068de…`) and book 1's in-transit state
  (Peeters order `6b0851920a66f`, €55 total, no delivery
  estimate) in the terms Round M asked for. The custody
  facts are named there as program-reported; the session
  did not access or certify the custody PDF, receipts, or
  shipping records, and neither does this adjudication.
- **Stage 4.4 fresh pass: no mismatch.** Reapplying each
  candidate's registered rules to the filed aggregates
  reproduces one PASS (soreyi) and five FAIL (asoreyi,
  xolkete, pxolkete, xolkte, wisi), denominators reconciled
  (33 held-out texts); the OD-20 aggregates agree. No new
  support/evidence mismatch survives the existing citation
  restrictions.
- **Stage 4.5: no new contradiction.** ANSWERED-BY-REDIRECT
  / NOT CONFIRMED reads consistently once dated scopes and
  the filed supersessions are applied; the awaited Rilly
  reply remains outstanding correspondence, not a
  contradiction.
- **Spec 102 state.** Book 2's custody removes one
  acquisition uncertainty. Full S-1 still awaits book 1's
  arrival and inspection, digitisation authorisation,
  source-linked extraction and mapping, and G-1/G-2
  computed (at least 40 scored concepts per family test,
  at least 20 outside the earlier twelve, at least 80%
  registered injection power at θ = 0.30, d = 0.75) before
  any affiliation scoring. The test remains uncommissioned.

The session's single highest-value next step — register a
bounded source-to-gate scoping of the held Appendix,
labelled partial-S-1, its execution separately
owner-authorized, with its stated falsifier (if custody-side
inspection shows the Appendix holds no usable form–gloss
evidence or coverage information beyond what is already
documented and cannot change any preparation decision
before Rilly 2010 arrives, defer rather than create a
token scoping project) — is recorded as a priority
judgment, **NOT commissioned**, as the matching
suggestions of Rounds L and M were recorded. No ledger row
is added for the null or for the suggestion.

## 5. Owner decisions arising

None. No unit requires an owner decision; the two paper
surfaces touched (the Indus census snapshot, the
Eteocypriot STEMS count) are corrected by record and
erratum only, with any future paper version gated on the
owner's approval of the actual text, and R-IP-04 (§2.4)
remains the owner's from before this round.

## 6. Tallies

Units: 7 returned — Indus 4 (1 APPLY, 2 APPLY WITH
MODIFICATION, 1 DO NOT APPLY), Eteocypriot 3 (1 APPLY WITH
MODIFICATION, 2 APPLY), Meroitic 0 (explicit null).
Ledger rows added: 6 (N-I-1, N-I-2, N-I-3, N-E-1, N-E-2,
N-E-3), all done at this landing. Ledger recount from the
file at this landing: **139 rows — 87 done, 31 accepted,
0 open, 21 rejected** (Indus 42, Eteocypriot 41, Meroitic
56). No standing, verdict, or tally in any program moves;
no paper is edited; nothing is published, so no
post-publication wait runs.

## 7. What this round does not do

The normalized-correction replay for G-IND is not
commissioned (§2.1). The consistency-only contact
distinction is not registered (§3.1). The C-E-15
feasibility decision is not executed (§3.3). The Spec 102
source-to-gate scoping is not commissioned (§4). Spec 100's
permission gate, Spec 098 Stage 4, T502/T503, and the
owner's VEXA adjudication are untouched, as the sessions
themselves recorded.

**AI disclosure:** this adjudication was executed by an AI
agent (Muse, via Muse) at the direction of Tristen
Pierson, per constitution sec. VI.
