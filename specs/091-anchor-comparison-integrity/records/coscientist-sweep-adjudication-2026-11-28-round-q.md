# Co-scientist sweep adjudication — Round Q (2026-11-28)

Round Q of the standing Co-scientist loop. Scope: the records
only. No paper text is edited anywhere in this landing, nothing
is deposited, no claim standing, verdict, or tally in any
spec's claims ledger changes, and no new study is registered.
All three briefs were pinned at
`37213fa78846234d296ac50f44a8830332ceec5c` (current main at the
round's opening, the PR #817 merge). The briefs and the three
sessions' verbatim responses are the evidence of record for
this round and are held at the goal's
`hidden_files/round-q-2026-11-28/` (`brief-indus.txt`,
`brief-eteocypriot.txt`, `brief-meroitic.txt`;
`resp-indus.txt`, `resp-eteo.txt`, `resp-meroitic.txt`).

## Census outcome

The census preceding the round found no unledgered
post-Round P lists: every post-Round P recommendation list on
the record is already ledgered, and all three Round Q sessions
ended at Round P confirmations in their prior rounds — that
is, each session's settled state entering Round Q was the
Round P confirmation state, with the ledger standing at
158 rows (114 done, 23 accepted, 0 open, 21 rejected, as
recounted in the plans-census closing note of 2026-11-27).
All three sessions independently confirmed that census
(158 rows: 114 done, 23 accepted, 0 open, 21 rejected) from
the record they inspected. No settled item is re-recommended
in this round, and no gated row is discharged except on its
own terms as recorded below.

## The three briefs' substance

Common ground in all three briefs: paper text is not under
review; the owner's ruling of 2026-11-28 makes Meroitic the
program's sole active front, with Indus and Eteocypriot in
maintenance (correspondence watches and already-deposited
papers continue; no new studies are commissioned on either
until the owner reopens them); the ELSEWHERE methods paper
version 2, confirmed in Round P, is deposited (Zenodo record
24590521).

- **Indus brief.** The obfuscation battery as revised has
  scored the real corpus under per-system control bands: the
  structure family returns SIGNATURE PRESENT (two structural
  statistics outside the size-matched natural band), filed as
  a candidate for adjudication with the registered
  alternatives named first (genre and length effects,
  editorial sequence construction), expressly not evidence of
  encryption and proclaiming nothing about intent, the band
  being synthetic natural corpora; the substitution family is
  the same measurement under a more sensitive rule, not an
  independent second finding; stratum asymmetry is ABSENT;
  the inventory family carries no verdict (its gate leg
  failed). The deep-antiquity evaluation is complete: all
  four registered predictions NOT SUPPORTED, the paleographic
  leg separately UNTESTABLE; the single most
  decision-changing evidence is named (a sealed,
  independently dated pre-3400 BCE written artifact
  demonstrably ancestral to a program script). The generative
  engine's assignment search remains blocked at its
  generator: three successive designs failed the same frozen
  conformance floor (median recoveries 0.772, 0.737, 0.719
  against 0.80); no fourth revision; the real-corpus stage is
  not commissioned. The Indus paper stands at version 12
  (Zenodo record 24441587); no version 13 is prepared.
- **Eteocypriot brief.** The generative engine's
  candidate-ranking stage for the ICS texts has executed:
  conformance preflight filed as met in full (filed-anchor
  reproduction 9 of 9; synthetic recovery 1.000 in all five
  replications, shuffle control far below); the ranked
  candidate set for the Amathus bilingual (ICS 196) returns
  RANKING NULL (the top candidate's two of eight held-out
  matches, on its [na] ending, matched by the permutation
  null's 99th percentile; 107 of 999 permutations tying the
  observed top score, one exceeding it); no reading is
  proclaimed and no standing moved; the comparanda were
  closed at the anchor set alone. The deep-antiquity
  evaluation for this program: inheritance NOT SUPPORTED
  (the Cypriot syllabary descends from Cypro-Minoan, itself
  from the Linear A tradition); the content-residue leg
  treats the Amathus bilingual as an ordinary
  civic-religious dedication. The obfuscation battery found
  every family NOT TESTABLE AT THIS POWER for Eteocypriot
  (11 texts, 54 tokens), filed as a power statement. The
  continuation license stands with its conformance
  qualifications on the record as ruled by the owner on
  2026-11-27; the binding constraint remains corpus size.
  The Eteocypriot paper stands at version 5 (Zenodo record
  24590530).
- **Meroitic brief.** A structure-induction study (Spec 112)
  was registered and executed twice against frozen preflight
  floors; both designs failed all three legs (first design:
  segmentation median boundary F1 = 0, slot match 1 of 95,
  partial precision 4 of 36; revised design: median F1 still
  0, slot model 73 of 95 against the 90 percent floor,
  partial precision 5 of 14 against 0.80); the study is
  closed as filed, the floors never lowered, no third attempt
  commissioned. The affiliation test (Spec 102) stands armed
  and gated on the arrival of Rilly 2010 in print; a custody
  extraction from custody sources only shows the first gate
  cannot be fed early (most custody sources inadmissible as
  the registered vocabulary source; attested forms cover
  only 14 scored concepts, 7 outside the twelve anchor
  concepts, against the gate's requirement of 40 scored
  concepts with at least 20 outside the twelve). The
  obfuscation battery revision returned no verdicts for
  Meroitic (invariance leg failed on control-band coverage;
  the stratum family is not testable). The gloss-induction
  stage remains gated on the affiliation test's freeze.

Each session was asked for numbered units in its established
format, each with its ground and what would discharge it,
within its scope, and for a red-team pass on the newest
filings. The sessions' units, grounds, and the coordinator's
adjudication follow. Dispositions use the ledger vocabulary;
the rows are entered in
`records/coscientist-recommendations-ledger.md` as Q-I-1 to
Q-I-4, Q-E-1 to Q-E-4, and Q-M-1 to Q-M-2.

## 1. Indus units

### Q-I-1 — APPLY; done, discharged by the Spec 110 / Spec 111 entropy correction

The session's finding, sustained algebraically and from the
filed aggregates: the entropy quantities are misidentified.
Spec 110's A4 is `H_all - H(Y|X)`, not bigram mutual
information; it equals mutual information only if
`H_all = H_Y`, which need not hold. A4 is also algebraically
linked to A3, `A4 = H_all(1 - A3)`, so A3 and A4 are not
independent findings. Spec 111's filed conditional entropy
subtracts `H_all` instead of `H_X`. The session's recomputed
Indus values and its two-sequence counterexample
(`[a,b]`, `[a,c]` returning A4 = 0.5 and filed conditional
entropy = -0.5 against true mutual information 0 and true
conditional entropy 1 bit) are carried in full in the
correction record. Adjudication: APPLY as proposed.
Discharged by
`specs/110-obfuscation-hypothesis/records/correction-2026-11-28.md`
and the cross-reference note at
`specs/111-deep-antiquity-evaluation/records/correction-2026-11-28.md`.
All frozen outputs are preserved; A4 is not to be described
as mutual information in any adjudication, and A3/A4 are not
to be counted as two independent findings.

### Q-I-2 — APPLY WITH MODIFICATION; done as modified, discharged by the Spec 111 correction and adjudication record

The session's finding, sustained: Spec 111 section 6.1's
description of ICS 196 contradicts the program's own
ETE-CON-03 — the city honouring Ariston, son of Aristonax,
not "honoring the goddess" — and the negative content
inference drawn there is broader than its evidence. The
modification to the session's candidacy: the pooled P4 grade
is retained only under the bounded "no demonstrated positive
instance" meaning recorded in the Spec 111 record, and the
Indus content position (UNTESTABLE; absence of extended
texts a format observation, not a refutation of short-form
residue) is recorded there rather than re-graded here.
Discharged by
`specs/111-deep-antiquity-evaluation/records/correction-and-adjudication-2026-11-28.md`
§§(a)–(b).

### Q-I-3 — APPLY WITH MODIFICATION; done as modified, discharged by the Spec 111 correction and adjudication record

The session's finding, sustained as a matter of logical
scope: the broad transmission hypothesis does not entail
every registered prediction without auxiliary assumptions,
and the evaluation's strongest statements overreach what the
registered predictions test (different immediate script
parents do not prove unrelated ultimate origins; one early
artifact would not by itself establish the broader
catastrophe/transmission account). The modification: the
frozen predictions and their historical grades are
preserved; what is filed is the adjudication note naming the
auxiliary assumptions per prediction, describing proximal
derivations as such, and narrowing the section 7
decisive-find statement to the chronology/ancestry claims
such an artifact would actually establish. Discharged by
`specs/111-deep-antiquity-evaluation/records/correction-and-adjudication-2026-11-28.md`
§(c).

### Q-I-4 — APPLY; done, discharged by the Spec 111 correction and adjudication record

Two numerical narrative errors, both sustained from the
evaluation's own numbers: the chronology gap implied by the
stated dates is roughly 6.3–7.7 millennia, not over eight;
and the closest listed pair is the Indus–synthetic null at
2.0865, with Meroitic–Latin at 3.1301 the closest among
real-system pairs only. Discharged by
`specs/111-deep-antiquity-evaluation/records/correction-and-adjudication-2026-11-28.md`
§(d). The original matrix is preserved.

### Indus red-team findings carrying no unit

On the obfuscation candidate, the session's red team holds
the filing's principal adjudication framing to be already
right, with two sharpenings the coordinator adopts as the
round's reading. First, the leading alternative is
generator/observation-unit mismatch — the synthetic
generator's idea of natural writing, including its realized
inventory (declared V0 372 against realized band inventories
of 316–325 versus the real 372) and the fact that a recorded
Indus inscription need not be a word-like unit — ahead of
genre and editorial sequence construction. Second, the
named alternative "length effects" needs the
matched-multiset caveat: the generator already matches the
sequence-length multiset, so a bare difference in mean
length is not an uncontrolled explanation; boundary meaning
and length-dependent interactions can still differ. The
structure and substitution families are one
target-versus-model measurement under two rules, not
independent corroboration, and no encryption or intent
conclusion follows. On the deep-antiquity grades, the red
team's grade-by-grade scope assessment (P1 descriptive, not
a calibrated ancestry test; P2/P3 bounded NOT SUPPORTED
readings standing conditionally on their cited sources; P4
as treated at Q-I-2) is recorded at §§(b)–(c) of the Spec 111
record. No fourth generator, new Indus study, or version 13
is proposed by the session or adopted here.

## 2. Eteocypriot units

### Q-E-1 — APPLY; accepted — the conformance addendum is filed; the label/license disposition is referred to the owner

The session's finding, sustained on reconstruction of the
seeded mappings: the Stage 4 shuffle controls are not the
registered derangements in 3 of 5 replications. The harness
shuffles the label list and rotates once if any fixed point
exists, which does not guarantee a derangement and is never
finally checked; the fixed points are replication 1: lo, so
(so active in the planted anchored set); replication 4:
o, ma, mi; replication 5: re. The verifier repeats the same
construction, so verifier agreement verifies reproducibility
of the figures, not the missing property. "Preflight met in
full" must therefore be qualified. Adjudication: APPLY; the
conformance addendum is filed at
`specs/109-generative-decipherment-engine/records/stage-4-round-q-addenda-2026-11-28.md`
§(a), replacing reliance on "preflight met in full" with
"numerical floors met on the executed controls; the
registered derangement construction not met". The
disposition of the clause-S / full-conformance labels and
any license consequence is referred to the owner and is not
decided in this round; the row therefore stands accepted,
not done. The observed recoveries and the RANKING NULL
arithmetic are expressly preserved; this defect is not proof
that a correctly deranged control would fail.

### Q-E-2 — APPLY WITH MODIFICATION; accepted as modified — the factual correction is discharged; the P4 grade-basis disposition is referred to the owner

The session's finding, sustained: Spec 111 sections 5–6
carry the ICS 196 honoree error (as at Q-I-2) and a
categorical corpus-content negative ("No Eteocypriot text
encodes knowledge beyond its culture's documented level")
that the unread state of the Eteocypriot language cannot
support. The factual correction and the bounded replacement
statement are discharged by
`specs/111-deep-antiquity-evaluation/records/correction-and-adjudication-2026-11-28.md`
§§(a)–(b). The disposition of the Eteocypriot P4 grade basis
(whether P4 remains NOT SUPPORTED for a clearly limited
evidential claim or requires an explicit
untestable-content qualification) is referred to the owner
and recorded as referred, not decided; the row therefore
stands accepted as modified.

### Q-E-3 — APPLY WITH MODIFICATION; done as modified, discharged by the Stage 4 addenda

The session's finding, sustained against the pinned ranking
input: the filed "real skeleton" lengths
[2,3,5,4,3,6,9,7,7,2,5] (total 53) are wrong; the actual
lengths are [2,3,5,4,3,6,10,7,7,2,5] (total 54, segment 7
having ten signs). The session further establishes the
pool-versus-realized-types distinction (a 35-label sampling
pool is not 35 realized types) and that the five fixtures
are isomorphic under relabeling — five label realizations of
one construction, not five distinct structural difficulties
— so the perfect synthetic recovery is a planted
implementation control, not evidence of detection power at
real-corpus sparsity. The modification: no revised fixtures,
power estimate, or additional study is commissioned; the
act is the dated correction and the inference-scope limit.
Discharged by
`specs/109-generative-decipherment-engine/records/stage-4-round-q-addenda-2026-11-28.md`
§(b). The observed five 1.000 recoveries stand as filed.

### Q-E-4 — APPLY; done, discharged by the Spec 111 correction and adjudication record

The chronology gap arithmetic error, the same error as
Q-I-4 ground A: the evaluation's stated intervals imply
roughly 6.3–7.7 millennia (the session computes the endpoint
envelope at about 6,350–7,650 years on the BP convention),
not "more than eight thousand years", in both passages
where it appears. Discharged by
`specs/111-deep-antiquity-evaluation/records/correction-and-adjudication-2026-11-28.md`
§(d).

### Eteocypriot red-team findings carrying no unit

The session's ranking red team confirms, and the coordinator
adopts, that RANKING NULL is arithmetically correct on the
filed figures, with the full null distribution reproduced by
the session's independent calculation: null maximum
distribution 0: 888, 1: 3, 2: 107, 4: 1 over 999
permutations; the registered 99th percentile is 2; the
observed top score 2 does not exceed it. The permutation
null over the same candidate set is the right null for the
narrow frozen-template question (one common permutation of
the development labels applied to every candidate, the
maximum taken across the closed candidate set), with its
stated limit: it is a conditional ending-label
correspondence null, not a full search-pipeline null. The
perfect synthetic recovery against a null real-corpus result
supplies no additional positive or negative linguistic
conclusion beyond what Q-E-1 and Q-E-3 record. The
obfuscation power statement (NOT TESTABLE AT THIS POWER)
and the inheritance record are retained without new
recommendations.

## 3. Meroitic units

### Q-M-1 — APPLY WITH MODIFICATION; done, discharged by the Spec 112 calibration account

The session's finding, sustained on the filed harness and
reference sets: the Spec 112 reference labels are
rule-constructed. `extract_ground_truth` performs
longest-suffix matching against the reference suffix
inventory; the filed 1,719 reference items carry the
provenances suffix-alone 1,703, suffix+filiation 12,
suffix+theonym 3, filiation-alone 1. A valid suffix inventory
does not by itself establish per-form morphological truth,
and P-3 precision is membership in the reference suffix
inventory, not the proportion of proposals independently
demonstrated to be genuine morphemes. A calibration account
must therefore be filed before the two closures are read as
a corpus information limit. The modification: the account
marks the absence of per-form independent warrant as absent;
no new annotation exercise is performed, and neither
historical run is rescored. Discharged by
`specs/112-meroitic-structure-induction/records/reference-calibration-account-2026-11-28.md`.
Both closures stand as failures of the specified designs on
the pinned inputs and operational references.

### Q-M-2 — APPLY WITH MODIFICATION; accepted as modified — design direction adopted; no execution commissioned

The session's conditional successor direction, adopted as a
design direction only: a joint, role-conditioned,
order-sensitive semi-Markov-style design in which
segmentation and role assignment constrain one another, the
actual ordered span path is emitted as the statistic (the
revised design's reported sequence discards realized order,
returning the global grammar order restricted to detected
slots), with fixture/null contrasts (reversed anchors,
repeated and optional roles, ambiguous suffix-like stem
endings, count-/length-matched controls), a fixed complexity
control, and an ablation against the uncoupled design. The
existing numerical success floors and both revised shuffle
constraints are preserved in any proposal. No third
execution is commissioned by this row: any corpus execution
requires a separate owner commission and prospective
registration, and the design's discharge condition (an
owner-adjudicable design proposal stating objective, priors,
actual path statistic, fixture/null contrasts, complexity
control, evaluation separation, and its dependence on Q-M-1)
remains outstanding. The row stands accepted as modified.

### Meroitic red-team findings carrying no unit

Two red-team findings are adopted as the round's reading and
carried in the records named, without ledger rows.

First, the Spec 102 arithmetic sharpening. Conditional on
the custody extraction's counts as filed (14 total scored
concepts, 7 outside the twelve, 7 inside), the separate
threshold deficits are 26 total and 13 outside; but any
40-concept set contains at most 12 inside concepts and
therefore at least 28 outside concepts, so at least 21
additional OUTSIDE concepts are required even if all five
missing inside concepts become eligible — adding only 13
outside plus those five inside would yield 32, not 40. This
supersedes the custody extraction's "13 outside" shortfall
framing. The per-family evaluation further means a union
count does not demonstrate 40 usable concepts in each test.
Filed at
`specs/102-meroitic-fresh-affiliation-test/records/g1-arithmetic-addendum-2026-11-28.md`;
the extraction's counts themselves remain brief-level as
filed, and no gate state changes.

Second, the Spec 112 fixture correction: the revised
design's 2,193-form planted-form comparison was against the
all-single-character fallback, not the whole-form fallback.
Whole-form candidates were removed from the revised search
and occur zero times in its top-five fixture candidates.
"Revise the design, never the bar" is the right discipline,
with the session's two qualifications adopted: revision is
not automatically commissioned, and failure against these
references is not an information-theoretic impossibility
result. Filed at
`specs/112-meroitic-structure-induction/records/reference-calibration-account-2026-11-28.md`.

The session's remaining dispositions are noted without rows:
the sole-active-front ruling accepted; the obfuscation
revision leaves Meroitic unscored (passed detection legs are
not a verdict); gloss induction remains gated on the
affiliation freeze; no settled work or paper decision is
reopened.

## Closing totals

Ten rows are added by this round: Indus Q-I-1 to Q-I-4
(4 done), Eteocypriot Q-E-1 to Q-E-4 (2 done, 2 accepted),
Meroitic Q-M-1 to Q-M-2 (1 done, 1 accepted). Totals after
Round Q: 168 rows — 121 done, 26 accepted, 0 open,
21 rejected (Indus 54, Eteocypriot 50, Meroitic 64).

Two items are referred to the owner and are recorded, not
decided, in this round: (1) the Q-E-1 disposition of the
clause-S / full-conformance labels and any license
consequence; (2) the Q-E-2 / Q-I-2 disposition of the P4
grade basis. Nothing in this landing moves a standing,
verdict, or tally; no paper text is edited; nothing is
deposited; no new study is registered.
