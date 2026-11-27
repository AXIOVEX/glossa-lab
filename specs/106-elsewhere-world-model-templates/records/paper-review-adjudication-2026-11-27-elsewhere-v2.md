# Paper review adjudication — ELSEWHERE methods paper, version 2 candidate (2026-11-27)

**Kind:** CO-SCIENTIST PAPER REVIEW ROUND + ADJUDICATION. **Actor:** the
Glossa-Lab chat's paper-round worker, under the owner's orders of
2026-11-27: every paper iterates through Co-scientist review before any
deposit finalizes (03:31 ET), and the deposits of both candidates are
approved (04:05 ET) but execute only after the rounds. Claim-changing
items are referred to the owner, not applied. Nothing in this round was
deposited anywhere.

## 1. Material and route

Candidate under review: the version 2 candidate of "Elsewhere: A
Framework for Testing Claims About Worlds That Cannot Be Observed,
Built and Exercised on Three Undeciphered Scripts" (8 pages, SHA-256
`dd5aa034ccbd3b732f54709e4686db804784d4650a02e3ad3ab4736408e0b864`;
preparation record
`records/preparation-record-2026-11-27-elsewhere-v2-candidate.md`,
PR #775). Its one substantive change from the deposited v1 (Zenodo
record 24571025) is the Round N unit N-I-1 normalization qualification
at the statement of the Indus gate result in §5.

Route: the tower-compute automation Brave (Academia Co-scientist),
the three standing sessions — Indus
`192b25f3-cb7b-46b4-acfa-1c1eea4e41fb`, Eteocypriot
`1828e4db-cc7b-434a-891a-12aca9ad1b8a`, Meroitic
`11cac4f7-f109-4fac-bbb5-c670eb33b291`. Every brief was filed before
sending at the goal's
`hidden_files/coscientist-paper-round-2026-11-27/` and sent under the
standing composer discipline: probe (composer empty in every case; no
stray draft found in any session), upload, placeholder-matched verify
by length and FNV-1a over UTF-8 bytes, and a guarded send re-checking
session URL, length, and hash in the same invocation. No unverified
text was sent at any point in the round.

Briefs (canonical text = filed file content minus one trailing
newline):

| Iteration | Session | Brief | Chars | FNV-1a |
|---|---|---|---|---|
| 1 | Indus | `elsewhere-v2/indus/BRIEF-elsewhere-v2-indus.md` | 3,984 | `6d23562d` |
| 1 | Eteocypriot | `elsewhere-v2/eteocypriot/BRIEF-elsewhere-v2-eteocypriot.md` | 4,333 | `9ee43aef` |
| 1 | Meroitic | `elsewhere-v2/meroitic/BRIEF-elsewhere-v2-meroitic.md` | 4,072 | `6f6ec45a` |
| 2 | all three | `BRIEF2-elsewhere-v2-<session>.md` | 3,407 | `10147e91` |
| 3 | Indus | `elsewhere-v2/indus/BRIEF3-elsewhere-v2-indus.md` | 979 | `eb53f6dd` |

Captures (full session output, chat summary plus the session's filed
review where one was written; UI chrome trimmed):

| Iteration | Session | Capture file | Bytes | SHA-256 |
|---|---|---|---|---|
| 1 | Indus | `elsewhere-v2/indus/OUTPUT-elsewhere-v2-indus.md` | 17,698 | `60266b6ac54bdd7217ef50cdde6d83b07f1383546f13a2b89e4af0d38cd56c4c` |
| 1 | Eteocypriot | `elsewhere-v2/eteocypriot/OUTPUT-elsewhere-v2-eteocypriot.md` | 16,108 | `bfdff9b843bbeaa735cfa5ca82a059dacdc6fed863bad631b3cdffcd5f4eb7f4` |
| 1 | Meroitic | `elsewhere-v2/meroitic/OUTPUT-elsewhere-v2-meroitic.md` | 15,914 | `272dc4a3f9be1ceb40799836e68d2bb60c875affd29dbf5e405629660e80dd51` |
| 2 | Indus | `elsewhere-v2/indus/OUTPUT2-elsewhere-v2-indus.md` | 2,046 | `bfd9d5bcc4a83307288fe371e3c32f013fe140ee9a044ea2771666fb42ff9bb6` |
| 2 | Meroitic | `elsewhere-v2/meroitic/OUTPUT2-elsewhere-v2-meroitic.md` | 1,271 | `8f793ea6c6372d36ada7e66c3e50c562440d5f9df517ab17454037d7a0e80378` |
| 2 | Eteocypriot | `elsewhere-v2/eteocypriot/OUTPUT2-elsewhere-v2-eteocypriot.md` | 2,603 | `8d46857f8fd8953850f02240134597d4892fedbaa00c5000a56c425bbd3fb960` |
| 3 | Indus | `elsewhere-v2/indus/OUTPUT3-elsewhere-v2-indus.md` | 376 | `3b562eb674c64588545a4b387ede4eff65f5a605999028a494be297d29242e23` |

**File-identity finding (disclosed).** The review file the Eteocypriot
session filed in iteration 1 (`elsewhere-v2-paper-review/review.md`)
is byte-identical (15,062 chars) to the Indus session's `review.md`:
the sessions share a global workspace, and the Eteocypriot session
adopted the Indus session's review as its filed copy. Its chat summary
is its own and converges with that review's substance, and at
iteration 2 it identified a further unit of its own (PV2-E3, §3
below) that its iteration-1 summary had counted among its "seven
ranked, passage-specific comments" but which does not appear in the
filed copy. The units below are therefore adjudicated once, on the
substance, with each session's position noted; the filed-copy identity
is recorded here rather than treated as two independent reviews.

## 2. The headline question — all three sessions

All three sessions answer the brief's central questions the same way:
**the N-I-1 qualification is correct and stated at the right
strength.** The gate's GOOD survives as the correct mechanical
consequence of the frozen, unnormalized rule exactly as registered;
the normalized predictive log-loss reading does not survive and is
withdrawn; no other passage of the paper asserts the withdrawn reading
(the abstract's GOOD wording and §7's bounded comparison stand at the
mechanical license). The Meroitic session independently recomputed
the filed figures (row totals 1.1520228123 / 1.2792728569 /
1.2872928177; mean scores 4.5579430544 and 4.1782887204; difference
0.3796543340) and the Indus session confirmed the same at iteration 1.
Two precision suggestions (identifying the three example rows by
context; rewording "the gate was predictive") were expressly marked
not required by the sessions raising them and are adjudicated DO NOT
APPLY: the owner-approved qualification passage is retained as
prepared, and the passage does not misidentify the rows (the first is
a group-start row, as both sessions note the paper's "example rows"
wording correctly allows). Round O's two Indus records-side items
need no paper change (Indus session, confirmed again at iteration 2).

## 3. Units and adjudications

**U1 — Ensemble conformance qualification (Indus P1; Meroitic
comment 1; Eteocypriot headline item 2). OWNER DECISION, referred as
OD-P-1.** §6 and the abstract present the first ensemble's
refuted-in-ensemble result without the conformance qualification
filed at Round N unit N-E-1: the load-bearing statement was both an
axiom in every instance and a checker item, so the pass checked
consistency with an inherited premise and did not satisfy the
framework's literal evidence/axiom separation rule; the status stands
as a conditional logical result, not an independent evidentiary test.
Both raising sessions supply insertion text (Indus: a §6 paragraph
plus an abstract "conditional refutation" qualifier; Meroitic: a §6
paragraph after the result tally with the abstract's
"first full exercise" description carrying the same scope). The
underlying qualification is already on the program record (N-E-1,
landed); whether and in which words the paper itself carries it
changes the paper's characterization of a result and is the owner's
decision. Not applied.

**U2 — Execution chronology (Indus P2; Meroitic comment 3). APPLY.**
§5's "unsealed exactly once" asserts the simpler account against the
filed chronology (Round N unit N-I-2): one first disclosure, two
complete scoring executions (the stopped run and the corrected
full-stage re-execution), replay ungoverned by the registration, the
stopped run's outputs not separately filed. Applied in two places:
the Indus gate sentence now reads "first disclosed only to the
checker after the registration guard passed, with the reserve's hash
identical as sealed and as scored", and the defect paragraph that
reports the re-execution now carries the two-executions account with
the registration gap and the retention statement. No number, score,
or verdict changes. Confirmed as rendered by both raising sessions
at iteration 2. Ledger rows P-I-1 and P-M-1.

**U3 — Aggregation definition (Meroitic comment 2; Indus P5;
Eteocypriot headline item 3). APPLY (two sentences).** (a) §2.2's "It
is dead if it derives in no surviving instance, or every instance
deriving it has died" permits refutation by silence, against the
registered §8.1 condition. It now reads: "It is dead only when no
surviving instance derives it and at least one surviving instance
derives its negation. Mere non-derivation is not death: a claim no
survivor resolves remains underivable, translation failures are
recorded as coverage failures, and an ensemble with no survivors is
exhaustion of the model, not a refutation." The first ensemble's
result is unaffected (all four instances derive the negation).
(b) §2.2's "A study that never kills an instance is not testing
anything" conflates possible contradiction with observed deaths; it
now reads: "A study whose registered evidence contacts cannot
contradict any instance is not exposing those instances to a test."
Both confirmed at iteration 2 by all three sessions. Ledger rows
P-M-3 (a) and P-I-3 (b).

**U4 — Title and abstract classification of Meroitic (Indus P3;
Meroitic comment 4). OWNER DECISION, referred as OD-P-2.** The title
("Three Undeciphered Scripts") and the abstract classify Meroitic as
an undeciphered script, against the paper's own §8 (the script's
decipherment is a century old; the open problem is the language). The
sessions propose different replacement titles ("Three
Ancient-Script Research Programs"; "Three Ancient Writing Systems"
with a matching abstract phrase). A title change to a deposited
paper is the owner's decision. Not applied.

**U5 — §7 superlative (Indus P4; Meroitic comment 6; Eteocypriot
filed review P4). APPLY.** "The strongest comparison available" is
an unsupported comparative claim. The sentence now reads: "The Indus
gate compares the derived system against the sandbox's own baseline
under the frozen, unnormalized scoring rule, and it licenses nothing
beyond that comparison." Confirmed at iteration 2 by all three
sessions. Ledger rows P-I-2 and P-M-2.

**U6 — §4.2 digit sentence (Indus P6). APPLY WITH MODIFICATION.**
As written, "one of them having no neighbour at all across 178
one-token groups" can be read as attaching the 178 groups to the
digit; the Meroitic session read the sentence as the aggregate
context and confirmed the figures, and the applied rewrite preserves
every number and the neighbourlessness statement: "...five recorded
digits never have a successor, one of them having no neighbour at
all; the sandbox contains 178 one-token groups in all." Confirmed at
iteration 2 (Indus: "correctly attaches the 178 one-token groups to
the sandbox total"; Meroitic: "clearly identifies 178 as the total
number of one-token groups"). Ledger row P-I-4.

**U7 — §5 Eteocypriot inventory sentence (Meroitic comment 5).
APPLY.** The sentence as written omits the registered exemption of
the unread mark. Verified against the filed record before applying
(`specs/105-elsewhere-sandbox/records/stage-6-outcome-2026-11-25.md`:
"All 35 derived marks were checked: 1 exempt (`?`), 34 carrying
values"). It now reads: "Both returned good: every value-carrying
inventory mark is accounted for by the known syllabary, with the
unread mark ? exempt, and the class and role structure nowhere
collapses two known distinct signs into one structural unit."
Confirmed at iteration 2 by all three sessions. Ledger row P-M-4.

**U8 — §2.2 enumeration (Indus iteration-2 unit). APPLY.** The
revised aggregation paragraph distinguishes underivable, coverage
failure, and model exhaustion alongside the three outcomes, so "For
one claim, the ensemble reading has three outcomes" no longer
matches. Replaced with the session's own proposed sentence: "For one
claim, the ensemble is read as follows." Applied verbatim after the
iteration-2 confirmations and confirmed by the Indus session at
iteration 3. Ledger row P-I-5.

**PV2-E3 — §6 Amathus characterization (Eteocypriot session,
iteration 1 in substance; identified by name at iteration 2). OWNER
DECISION, referred as OD-P-3.** §6 calls the text "the Amathus
bilingual, the longest Eteocypriot inscription, whose Greek half can
be read", and §6/abstract-derived wording speaks of "a named private
citizen". The session's points: the seed's identification of "the
long Amathus text" with ICS 196 was a declared study-level
assumption, not a plain fact; the tested proposition concerned a
royal dedicator and an act of dedication (the operational
definition); the "longest" superlative and the "private citizen"
characterization are not supported by the cited record. Proposed
fix: state the seed's identification and operational definition,
remove the superlative, and remove or replace "a named private
citizen". The session itself frames this as an author/owner
decision; it also overlaps OD-P-1's §6 territory. Not applied.

## 4. Iterations and the revised candidate

Iteration 2 (briefs §1) submitted the revised candidate carrying
U2, U3, U5, U6, U7 (interim revised build, SHA-256
`ced02470893667e0c75aa22f13c13ec9219658285a6a37e67a98274169ffa3e4`,
8 pages) to all three sessions. Meroitic confirmed it correct and
complete from its side apart from the two referred items; Indus
confirmed all six applied changes and raised U8; Eteocypriot
confirmed all six applied changes and identified PV2-E3 as a third
referred item. U8 was then applied and the Indus session confirmed
the final text at iteration 3: "from my side, the revised text is
now correct and complete within the reviewed scope, apart from the
two author-referred items".

**Final revised candidate:** `elsewhere-methods-paper-v2-candidate-revised-2026-11-27.pdf`
(goal files), 8 pages, SHA-256
`089f905388b98dc31f92ed1049bd5be2d5daaa7842ebb0e702f29ab7b7477be9`.
Built on tower-compute from the v2 candidate source (three pdflatex
passes, zero errors, page count unchanged); every changed sentence
verified in the rendered PDF, and every replaced sentence verified
absent. No number in the paper changed except as the applied items
state; the N-I-1 qualification passage itself is byte-identical to
the prepared candidate.

**Round verdict for this paper: clean apart from three owner
decisions (OD-P-1, OD-P-2, OD-P-3), which are referred to the owner
with the sessions' proposed texts and are not applied.** The deposit
step waits on those decisions; nothing was deposited, sent, or
published in this round, and no program standing, verdict, or tally
moved.

**AI disclosure:** this record was compiled by an AI agent (Muse,
via Muse) at the direction of Tristen Pierson, per constitution
sec. VI. It compiles the round's dispositions of record; it
adjudicates nothing beyond the paper-text items named above and
changes no standing, class, verdict, or tally.
