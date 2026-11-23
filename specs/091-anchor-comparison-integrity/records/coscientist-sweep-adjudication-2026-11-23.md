# Co-scientist Sweep (Round D) 2026-11-23 — Adjudication

**Date of adjudication:** 2026-11-23.
**Programs:** Indus (Spec 091/098/099/100 line), Spec 096
(Eteocypriot), Spec 097 (Meroitic).
**Filed under:** the Glossa-Lab loop's standing discipline
(owner directives 2026-11-21 and 2026-11-22): Co-scientist
findings are filed as artifacts and answered on the record;
every recommendation is logged once in
`records/coscientist-recommendations-ledger.md` with its
adjudication status; no standing, verdict, or tally changes
on a Co-scientist round alone.

## 0. Inputs and method

Three new Co-scientist sessions, one per program, fired
2026-11-23 ~16:10–16:20 ET through the tower-compute
desktop browser route, after the owner confirmed the route
was back. Each brief was sent verbatim from its filed
`MESSAGE.md`; the composer text was verified byte-for-byte
against the filed brief (byte length and checksum) before
each send. Captures are filed at the goal's
`hidden_files/coscientist-sweep-2026-11-23/<program>/`
(`OUTPUT.md`, `SESSION-RAW.json`, `CAPTURE-NOTE.md`).

- **Indus:** session `192b25f3-cb7b-46b4-acfa-1c1eea4e41fb`.
  OUTPUT.md SHA-256
  `34fd234eb6732a60e5efb3aa73c84738a0da0481f0bdc3533d4a8779fc34c9de`;
  SESSION-RAW.json SHA-256
  `1f3c2c5557ba3cd7542e28105070966444d63c5d9d7db5bb945b895150f67855`.
- **Eteocypriot:** session
  `1828e4db-cc7b-434a-891a-12aca9ad1b8a`; the session also
  wrote `eteocypriot-round-d-review.md`, whose full text is
  carried in the capture. OUTPUT.md SHA-256
  `cfd185f131e2e1b11821347fa545c7a247893bb5a4d782c8d7347d97e084e3f2`;
  SESSION-RAW.json SHA-256
  `35bd55185ead5164d4b4d46be6a43474e75736690458735b5d579ca988e86316`.
- **Meroitic:** session
  `11cac4f7-f109-4fac-bbb5-c670eb33b291`; the session also
  wrote `meroitic-round-d-2026-11-23.md`, carried in full in
  the capture. OUTPUT.md SHA-256
  `c128c9ab1f4bd7bea34fb3057cd6a0c4c8575803547b87c3e3d7f8b7ef0c49e8`;
  SESSION-RAW.json SHA-256
  `15be6386cced438da566afcaeb2e2252905d012bc92034a3c5502a1131540133`.

Each session's browser tab was closed once its capture was
verified (owner tab discipline, 2026-11-23). Adjudication
was against the primary record: the deposited papers, the
repo records at head `017cb353`, and the ledger. Two of the
round's quantitative claims were independently recomputed
before adjudication (§2, §3.1); both reproduced exactly.

**Standing consequence statement: no standing, class,
verdict, or tally moves on this round.** The standings
remain 3 E + 66 I + 4 R + 3 P + 18 U = 94 (Indus); the
Spec 096 verdicts stand (C096-1 NOT SUPPORTED, C096-2 TOO
THIN, C096-3 NOT ENGAGED, C096-4 SUPPORTED in narrowed
form); the Spec 097 Leg A tallies, Stage 4.2 UNDECIDABLE
AT THIS POWER, and the Stage 4.4 bounded PARTIALLY
SUPPORTED stand. One ledger row (B-M-9) is reopened
narrowly as to a justification sentence only (§3.1); its
execution and outcomes are not reopened.

## 1. Indus — no units advanced

The Indus session advanced **no new recommendation**. Its
conclusion, in its own words: the record "gives no reason
to reopen a settled item, but it also supplies no new
leverage on decipherment. Waiting for discriminating
evidence is the honest outcome here. No new specification,
class change, or v12 amendment is justified by this brief
alone."

Adjudication: the null outcome is **accepted as the
round's Indus result**. The session's three interpretation
boundaries (Spec 099's zero class changes do not establish
evidential independence; M375's discrimination stays
scoped to its design; the 22 NOT IDENTIFIABLE outcomes are
scoped to the registered design, and the 46 low-power
outcomes are not latent positive evidence) state the
program's existing position and request no act; they are
recorded here as confirmations, not units. The session
disclosed that it did not independently inspect the
deposited v12, the raw logs, or the full ledger in this
turn; its null result is therefore a brief-level result,
and is recorded as such.

Because the ledger logs recommendations, and none was
advanced, **no Indus ledger row is added for Round D**.
Disposition tally for Indus: 0 units.

## 2. Eteocypriot — 2 units

### D-E-1 — Resolve recurrence versus enrichment as Spec 101's target before execution: APPLY WITH MODIFICATION

The session demonstrates a real distinction: Spec 101 §1's
research question asks whether the development text's
recurring endings *recur* in the Amathus text, while the
binding floor rule (floor amendment §1.3) sets each floor
at the upper tail of a binomial whose rate is the
development frequency — a rule that detects occurrence
*above* that frequency. Under the registered rule, an
ending recurring at essentially its development rate will
usually return NOT SUPPORTED.

Verification: the session's synthetic check was recomputed
independently at adjudication (M = 40, K = 4, bound
0.05/4 = 0.0125). For development frequency 2/11 the
smallest qualifying floor is 14 with tail 0.008559
(preceding tail 0.021224 at 13); for 3/11 the floor is 18
with tail 0.012130 (preceding 0.027075 at 17). The
session's figures reproduce exactly. This is not C-E-18
(uncertainty and selection transparency): the distinction
survives with all frequencies known and all selections
disclosed. It is also not an error in the registered
calculation; it is a question about which proposition the
registered rule answers.

Disposition: **APPLY WITH MODIFICATION.** The
target-to-decision note is filed with this landing at
`specs/101-eteocypriot-next-claim/records/round-d-target-decision-note-2026-11-23.md`,
stating the distinction and that NOT SUPPORTED under the
current rule does not establish failure of recurrence. The
registered floor rule is **not** changed by this
adjudication: choosing the target — enrichment as
registered, or recurrence/rate transfer under a
prospectively amended rule — is **OWNER DECISION OD-D-1**
(§4). Spec 101 remains registered and unexecuted either
way.

### D-E-2 — Record Perna's explicit ICS 196 reading proposal: APPLY WITH MODIFICATION

The session shows, from the acquired Perna chapter's
publisher text (§§29–30), that the chapter does more than
re-edit ICS 194/195: it proposes a revised reading of
ICS 196's patronymic segment itself —
a-ra-to-wa-na-ka-so-we-o-se in place of the frozen
a-ra-to-wa-na-ka-so-ko-o-se — and questions the final sign
in the drawing. No inspected program record carries this
proposal: the corpus record's `reading_variants_carried`
lists a segment-2 variant and Gordon's conjecture, not
this one, and the OD-9 acquisition record does not record
the ICS 196 consequence. The distinction the session draws
is correct on the record: verification against Masson
would establish fidelity to that edition; it would not
adjudicate between Masson's reading and Perna's later
proposal.

Disposition: **APPLY WITH MODIFICATION.** The
source-conflict note is filed with this landing at
`specs/096-eteocypriot-program/records/perna-ics196-source-conflict-note-2026-11-23.md`:
the proposal is recorded as a proposal, the frozen corpus
bytes and ground truth are unchanged, and no reading is
adopted. The session's proposed paper sentence (for after
v2 §3.3's acquisition account) is a paper-text item for
the next version and is **not** executed here; it awaits
the owner's approval of the actual text, as every paper
item does. On the session's own showing, the ko → we
substitution alone changes no ending inventory and no
verdict; the final-sign doubt is recorded, not acted on.

## 3. Meroitic — 3 units

### D-M-1 — Resolve the binomial/permutation-law mismatch in the power audit: APPLY WITH MODIFICATION (narrow reopening of B-M-9)

The session recomputed the OD-15 power audit's own
100,000-draw permutation histograms
(`specs/097-meroitic-reproduction-benchmark/records/power-simulation-audit-2026-11-22.json`,
keys `null_R1_ext100000` / `null_R2_ext100000`) and showed
that the homogeneous-binomial law the audit's §3 invokes —
S is binomial(12, q) "to the accuracy the permutation null
confirms" — does not hold at the decision tail: the
histograms are underdispersed relative to the same-mean
binomial, and the binomial P(S ≥ 5) is 2.50× (R1) and
2.96× (R2) the histogram fraction.

Verification: recomputed independently at adjudication
from the same deposited JSON. R1: q0 = 0.1254717, histogram
variance 1.03803 vs binomial variance 1.31674, histogram
tail 0.00458 vs binomial 0.011466. R2: q0 = 0.1164483,
variance 0.94663 vs 1.23466, tail 0.00282 vs 0.008360.
Every figure reproduces exactly.

Scope, stated precisely: this finding strikes the audit's
**calibration justification sentence only**. The frozen
permutation p-values are computed from the permutation
null itself and do not pass through the binomial law; the
Stage 4.2 verdict (UNDECIDABLE AT THIS POWER), the Leg A
tally, and the audit's arithmetic all stand. The MDEs and
exclusion bounds stand as calculations under the binomial
model; what is withdrawn is the assertion that the
permutation null confirms that model's law.

Disposition: **APPLY WITH MODIFICATION.** Ledger row
B-M-9 is reopened narrowly, as to the justification
sentence only; its execution (PR #690) and outcomes are
not reopened. The annotation withdrawing the "confirms"
claim is appended to the power-audit record with this
landing. The session's alternative remedy — a registered
calibration extension — is a study act and is **not**
commissioned here. The session's proposed §4.4 paper
sentence is paper item **M-P8**, for the next version,
awaiting the owner's approval of the actual text.

### D-M-2 — Correct §1's "validated material" assurance: APPLY

Sustained on the v2 text as quoted in the assessment:
§1's narrative ("It then ran a preregistered campaign on
the validated material") transfers the benchmark's limited
reproduction results into a general assurance about the
campaign's inputs, which the body's own sections do not
support — the benchmark and the campaign inscription bases
are distinguished in §4.1 itself, and count reproduction
does not establish transcription fidelity. None of
M-P1–M-P7 addresses this sentence.

Disposition: **APPLY** as paper item **M-P9**: the
assessment's replacement passage is adopted as the item's
specified text for the next version. Paper text is not
changed by this landing; the item awaits the owner's
approval of the actual text.

### D-M-3 — Source-witness checks at sparse candidate decision boundaries: OWNER DECISION (OD-D-2)

The session proposes a new registered diagnostic: check
the six Stage 4.4 candidate forms' decision-bearing loci
and the extraction/tokenization rules against source
witnesses, before further interpretation of the sparse
failures. It is genuinely distinct from C-M-21
(evidential units) and C-M-22 (semantic calibration), and
it alleges no defect. It is also a new study act —
registration, execution, and possibly acquisition beyond
already-authorized material — and commissions of that kind
are the owner's. Disposition: **OWNER DECISION OD-D-2**
(§4). No work is started on it by this landing.

## 4. Owner decisions arising

- **OD-D-1 (from D-E-1): Spec 101's target.** Keep the
  registered upper-tail rule and declare the target to be
  enrichment above the development-frequency reference
  model (with NOT SUPPORTED expressly not a recurrence
  finding), or direct a prospective amendment/successor
  registration whose decision rule tests recurrence/rate
  transfer. The target-to-decision note filed with this
  landing records the distinction either way; Spec 101 is
  not executed before this is decided.
- **OD-D-2 (from D-M-3): commission the source-witness
  check**, or decline it. If commissioned, its
  registration must carry the session's stated claim and
  kill check, the fixed split membership, and the
  no-pooling rule for the xolkte family.

## 5. Tallies

Round D dispositions: Indus 0 units; Eteocypriot 2 units
(2 APPLY WITH MODIFICATION); Meroitic 3 units (1 APPLY,
1 APPLY WITH MODIFICATION, 1 OWNER DECISION). No DO NOT
APPLY units: no unit in this round re-recommended a
settled ledger item — each session worked from the
checked-off ledger state, and the Indus session expressly
declined to repackage settled work as new.

Ledger effect (rows added in this landing): D-E-1
accepted, D-E-2 accepted, D-M-1 accepted, D-M-2 accepted,
D-M-3 open. New totals: **119 rows — 62 done / 35 accepted
/ 0 adjudicating / 1 open / 21 rejected.**

Record-only acts landed with this record: this
adjudication; the five ledger rows and counts; the
Spec 101 target-to-decision note (D-E-1); the Perna
source-conflict note (D-E-2); the annotation to the OD-15
power-audit record (D-M-1). **Not** done in this landing,
by design: any paper-text change (D-E-2's sentence, M-P8,
M-P9 — all await the owner's approval of the actual text);
the OD-D-1 target choice; the OD-D-2 commission; any
calibration extension; any study execution.

## 6. Addendum — OD-D-1 decided (2026-11-23)

The owner decided OD-D-1 on 2026-11-23 (~17:05 ET):
Spec 101 keeps its registered upper-tail rule, and its
target is declared to be enrichment above the
development-frequency reference model, with NOT
SUPPORTED expressly not a recurrence finding. No
prospective amendment or successor registration is
directed. The decision and its consequence are recorded
in full in the Spec 101 target-to-decision note
(`specs/101-eteocypriot-next-claim/records/round-d-target-decision-note-2026-11-23.md`,
§Decision). Ledger row D-E-1 stands done on this
decision. Spec 101 remains unexecuted; OD-D-2 is
unaffected and still open.

## 7. Addendum — OD-D-2 commissioned (2026-11-23)

The owner commissioned OD-D-2 on 2026-11-23 (~17:14 ET):
the source-witness check proposed in unit D-M-3 is
registered as Spec 103
(`specs/103-meroitic-source-witness-check/`) and is
executed under the same act, in two landings
(registration first, execution second). The registration
carries the session's stated claim and its kill check,
the fixed split membership, and the no-pooling rule for
the xolkte-family variants (Spec 103 spec.md §2;
claims C103-1..C103-4). The diagnostic interprets the
provenance of the sparse Stage 4.4 failures; by its
registration it moves no standing, verdict, or tally by
itself. Ledger row D-M-3 stands accepted on this
commission and moves to done when the execution lands.

**AI disclosure:** this adjudication was compiled by an AI
agent (Muse, via Muse) at the direction of Tristen
Pierson, per constitution sec. VI. It compiles and answers
the Co-scientist's Round D findings against the record; it
changes no standing, class, verdict, or tally.
