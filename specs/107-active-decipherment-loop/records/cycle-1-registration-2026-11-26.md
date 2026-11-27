# Spec 107 — Cycle 1 Registration: Ranking Record and
Test Registrations (2026-11-26)

**Status: REGISTERED 2026-11-26, before any cycle-1
execution.** This record files cycle 1's ranking (with
its sensitivity statements, per the loop's Step 3), the
minimum for the null-yield kill criterion, and the full
registrations of tests I-1 and M-1. Test E-1 is Spec 101
executed under its own registration (§4 below); nothing
in this record amends it. Commissioned by the owner's
act of 2026-11-26 22:48 ET (Glossa-Lab chat: "Adopt the
loop and commission cycle 1 as proposed"), which took
the design's five closing decisions as proposed.

## 1. The ranking record

The candidate queues are the design's Part 2 (Indus
I-1..I-7 plus the blocked and excluded items; Eteocypriot
E-1..E-5 plus the blocked items; Meroitic M-1..M-6 plus
the closed items). Cycle 1 takes the design's Part 3
proposal, which the owner's act adopted:

- **Indus — I-1, the scramble-simulation identifiability
  calibration** (tower compute). It prices the whole
  Indus queue: every other entry's value depends on what
  any method of the program's kind could extract from a
  corpus of this shape. Its outcomes discriminate among
  all five Indus hypotheses at once, including the
  non-linguistic one.
- **Eteocypriot — E-1, the Spec 101 test** (desk). The
  only Eteocypriot entry whose registration, falsifier,
  floors, and inputs are all complete today; its outcome
  decides whether the program holds any live positive
  claim about unseen Eteocypriot text.
- **Meroitic — M-1, the stratum-conditioned structural
  recomputation** (tower compute). Genre is the confound
  the research report flags first for this corpus, and it
  sits upstream of M-2 and M-3, which use the same join.

**Sensitivity, stated as the loop requires.** The I-1
ranking is robust to the donor-dependence fragility: the
registration carries two donors precisely so that donor
disagreement is itself a filed outcome (INDETERMINATE),
and even I-1's failure mode produces the queue's most
valuable fact. The M-1 ranking assumes the build's
stratum labels are reliable as filed; if they are not,
M-1's first product is that discovery (its Population P
validation either reproduces the filed strata counts or
stops the test). The E-1 ranking is the fragile one, and
the design says so: scored purely on family
discrimination, E-1 earns almost nothing (enrichment of
segment-final sequences distinguishes no family from any
other), and under a likelihood assignment weighting
family discrimination above all else, E-2 (the
control-corpus calibration) outranks it. The cycle-1
proposal rests on the judgment that the program's next
question is whether the Eteocypriot line holds any live
positive claim at all; the owner noted that judgment in
his act and did not override it. The judgment and its
fragility stand here on the record.

**Null-yield minimum for cycle 1** (kill criterion 4,
set in advance): the cycle's yield counts as non-null
iff at least one of the following holds at cycle close —
(a) at least one test returns a verdict that is neither
INDETERMINATE nor NOT TESTED; (b) at least one standings
effect is licensed by an outcome record; (c) the
re-ranking for cycle 2 changes any program's lead test
from its cycle-1 queue position on the basis of a cycle-1
outcome.

**Seed statement (Step 1).** Each test below names, in
its registration, at least one hypothesis under which its
registered prediction fails: I-1 fails under the
hypothesis that corpora of this shape are below
identifiability for methods of this kind (the
non-linguistic and indeterminate directions both predict
weak or absent discrimination); M-1 fails under the
hypothesis that the pooled Meroitic statistics are
funerary-formula artifacts; E-1 fails under its own
registered falsifier (every candidate below its floor).

## 2. Test I-1 — scramble-simulation identifiability calibration (Indus)

**Question.** What could any method of the kind this
program runs extract from a corpus shaped like the Indus
corpus — this many independent short artifacts, this
length distribution, this duplication rate?

**Target shape.** Computed from the Spec 105 custody
datasets at run preparation and filed in the run record
before any scoring: artifacts A = 1,670 (derivation
1,336 + reserve 334); tokens T = 7,002 (5,611 + 1,391);
the per-artifact token-count multiset of the 1,670
artifacts (each Indus artifact is one group; token
counts run 2–8 as filed); full-corpus inventory 390
marks; duplication rate d = (A − distinct artifact
token-sequences) / A, computed from the two datasets
combined in their Stage 1 order (derivation and reserve
interleaved by the registered index rule, i % 5 == 4 to
reserve). These are shape parameters of the target, not
outcomes; computing them reads the target's censuses,
not its structure.

**Donors (two, registered in advance).**

- **Donor A — Meroitic.** The Kovetsky build's
  `data/inscriptions.jsonl` at the pin Specs 097/103/105
  used (SHA-256
  `1e91e3a0c52626482bc4015b597df862e7818602dab48a7e870240ab2e567bc4`,
  source commit `145af0836c071e7c9796d37d4b36add00d347c8a`,
  CC BY 4.0). Stream: every row whose `text` is not null,
  in file order; groups = the text split on spaces; marks
  = the characters of each group, as recorded (the
  lacuna `.` stands as a mark, uninterpreted, as at
  Spec 105 Stage 1). Ground truth is computed over this
  full stream.
- **Donor B — Latin.** Julius Caesar, *De Bello Gallico*,
  public-domain text as published by Project Gutenberg.
  The exact file (URL and SHA-256) is pinned in the run
  record at acquisition, before any scoring, and the
  bytes are held in custody under `glossa-custody/spec107/`,
  never committed. Preparation, fixed here: lowercase;
  j → i and u → v (classical orthography); drop every
  character outside a–z (punctuation, numerals, spacing);
  groups = the whitespace-separated words of the prepared
  text, in order; marks = letters. Ground truth is
  computed over the full prepared stream.

The donors' native inventories (Meroitic 32 marks; Latin
at most 24 letters) are far below the Indus 390. The
simulation matches artifact count, token count, length
distribution, and duplication; it does not force the
inventory, and every conclusion is stated per donor with
its inventory as a covariate. A conclusion that holds at
both donors' inventories is evidence about the shape; the
Indus inventory being larger makes its recovery problem
harder, not easier, and the record says so where it
matters.

**Reshaping (per replication).** From the donor's group
stream (in source order, treated as circular): draw
target token counts L from the empirical Indus
per-artifact token-count distribution; for each
artifact, take a contiguous span of whole groups from a
uniform random start position, accumulating groups until
the artifact's mark count first reaches or exceeds L
(the final group is kept whole; achieved token counts
are reported, not forced). Generate A′ artifacts for the
cell's scale (A′ = A × scale, token counts drawn the
same way). Duplication: replace ⌊d × A′⌋ artifacts,
chosen uniformly, each with an exact copy of a uniformly
chosen other artifact, so the achieved duplication rate
matches d within ±0.01 (the achieved rate is filed).
Cipher: a uniform random permutation of the donor's mark
inventory maps every mark to an anonymous label; all
pipeline statistics run on the ciphered stream. Split
(duplicate-aware, per the registration checklist): the
distinct artifact sequences are enumerated in order of
first appearance in the generated multiset; a distinct
sequence belongs to the reserve iff its ordinal in that
enumeration satisfies ordinal % 5 == 4, and every copy of
a sequence follows its sequence's side, so no sequence
appears on both sides of the split. The achieved
derivation and reserve artifact and token counts are
filed per replication (they approximate, and need not
equal, the target's 1,336 / 334 and 5,611 / 1,391).

**The pipeline under test** is the program's own:
(a) the G-IND-form predictor comparison, implemented
exactly as Spec 105's Stage 6 registration §5 states it,
generically over any derivation/reserve pair — baseline
unigram P(m) = count(m)/N with the unseen-mark rule
ε = 1/(N + V) (N derivation tokens, V derivation
inventory); derived predictor by the registered rules in
order (unseen-mark rule; group-initial rule
initial_count(m)/(number of derivation groups) with
unigram backoff; attested-pair rule c/successors_total
with unigram backoff) — the weights as registered,
unnormalized as Round N established, because the
statistic under calibration is the program's statistic
as filed; and (b) the L3 positional statistics of
Spec 105 Stage 3 (per-mark sole / initial / final /
medial classification within groups; attested ordered
pairs within groups).

**Conditions (per replication).** RIGHT: predictor
weights derived from the replication's own derivation
set, scored on its own reserve. WRONG: weights derived
from the *other* donor's derivation set of the paired
replication (same scale, same replication index), its
inventory aligned to the target inventory by frequency
rank in the respective derivation sets (ties broken by
label order), applied to the target reserve; target
reserve tokens whose type has no aligned counterpart are
scored at ε. SHUFFLE: weights derived from the
replication's own derivation set with the tokens inside
each group shuffled (unigram counts and group lengths
preserved, adjacency destroyed), scored on the true
reserve.

**Statistics.** R1 (predictor): per condition, the mean
per-token log-loss over the reserve and the advantage
(baseline minus derived) in nats per token. R2
(positional): ground-truth restricted marks per donor —
marks with ≥ 20 occurrences in the full donor stream
whose occurrences are ≥ 99% in {initial, sole}
(restricted-initial) or in {final, sole}
(restricted-final); sensitivity = the fraction of those
marks the replication's full sample (derivation +
reserve) classifies with the same restriction (same
99% rule applied to the sample, marks below 20 sample
occurrences excluded from both numerator and denominator
and counted as not-measurable); false-positive rate =
the fraction of sample marks with ≥ 20 occurrences that
are not ground-truth restricted but are classified
restricted. If a donor's ground-truth restricted set has
fewer than 5 marks, R2 is NOT MEASURABLE for that donor
and is filed as such. R3 (adjacency): the fraction of
the donor's ground-truth top-100 attested ordered pairs
(full stream) present in the replication sample's
attested pair set.

**Cells and seeds.** Scales 0.5×, 1×, 2× (token totals
≈ 3,501 / 7,002 / 14,004); 20 replications per
(donor × scale); each replication's randomness derives
from `random.Random("spec107-i1-{donor}-{scale}-{rep}")`
with rep = 1..20, so the run is reproducible from this
record alone. Two independent implementations of the
predictor scoring (the run's primary implementation and
a second, separately written scorer) must agree on every
replication's advantages to six decimal places
(TC-107-02); disagreement stops the test and is filed.

**Verdict rule (registered, three outcomes).** Evaluate
at 1× per donor from the 20 replications' medians:
- **POSITIVE** iff for both donors: median R1 advantage
  (RIGHT) ≥ 0.05 (the frozen G-IND margin), and median
  R1 advantage (RIGHT) ≥ 2 × max(median WRONG, median
  SHUFFLE), and (where R2 is measurable) R2 sensitivity
  ≥ 0.50 with false-positive rate ≤ 0.10 at 1× (medians
  over replications). If R2 is measurable for exactly one
  donor, its clause is evaluated on that donor alone.
- **NEGATIVE** iff for either donor: median R1 advantage
  (RIGHT) < 0.05, or max(median WRONG, median SHUFFLE)
  ≥ 0.5 × median RIGHT.
- **INDETERMINATE** iff the donors' POSITIVE/NEGATIVE
  evaluations disagree, or R2 is measurable for neither
  donor while R1 is positive for both.
The 0.5× and 2× cells are filed as the recovery curve
and inform the trace's statement of how the conclusion
scales; the verdict is taken at 1× only.

**Standings effects (as the design provides).** POSITIVE
licenses the Indus structural queue (I-2, I-3, I-6) to be
read at face value in later cycles; no anchor standing
moves. NEGATIVE collapses the Indus line to
record-keeping, the anchor-sourcing problem, and external
wedges: the directions resting on positive
internal-structure claims at this corpus shape close as
**indeterminate at current evidence** in the trace, and
I-2/I-3/I-6 are re-ranked below the sourcing work.
INDETERMINATE is filed with the donor sensitivity as the
finding, and I-2 becomes the cycle-2 lead (it needs no
donor). No outcome of I-1 is a claim about the Indus
language.

**Cost class:** Tower. **Custody:** donor B's bytes and
all intermediates in `glossa-custody/spec107/`, never
committed; the filed raw output carries every
per-replication figure the verdict consumes.

## 3. Test M-1 — stratum-conditioned structural recomputation (Meroitic)

**Question.** Are the corpus-wide structural facts
(adjacency structure, positional classes, and the two
conformance rates) properties of the language, or
artifacts of pooling a formula-dominated funerary
majority with everything else?

**Source.** The Kovetsky build's
`data/inscriptions.jsonl` at the pin of §2 (SHA-256
`1e91e3a0…`), read from the pinned source tree, never
modified. No Otten-corpus byte is an input: the build is
the openly licensed (CC BY 4.0) component of the
program's corpus, and the Otten custody terms (aggregate
only, sharing paused) are not engaged by this test at
all.

**Strata.** The campaign pipeline's filed map
(Spec 097's Stage 4 pipeline, `STRATA`): `funerary` →
funerary; `royal or temple (stela, wall, cartouche,
label)` → royal_temple; `document (ostracon, papyrus,
wood, vessel)` → document; `graffito` → graffito; any
other or missing kind → other.

**Population S (the sandbox population; the join
validation).** Every row of the build whose `text` is
not null, in file order — the 376 artifacts of the
Spec 105 Meroitic dataset, each artifact's stratum taken
from its own row's kind. *Validation, run first:* the
pooled recomputation over S must reproduce the filed
Spec 105 figures exactly — 24,648 attested adjacencies;
448 distinct ordered pairs; top pair (t, e) at 1,352;
a-sign 737 occurrences, 725 group-initial-or-sole;
i-sign 2,880 occurrences, 2,857
neither-initial-nor-sole; the five digits 0, 5, 6, 8, 9
never with a successor; digit 8 with no neighbour on
either side. If any figure does not reproduce, the test
STOPS and the mismatch is filed (the join is wrong, and
no stratum figure from a wrong join enters the trace).

**Population P (the frozen partition; the filed strata
counts).** Distinct texts by the campaign rule: dedup by
stripped text string, first row wins; held out iff
int(SHA-256(text)) mod 10 == 0, else development;
stratum from the winning row's kind. *Validation:* the
counts must reproduce the filed counts exactly —
development 335 (funerary 223, royal_temple 41, document
42, graffito 22, other 7); held out 33 (funerary 16,
royal_temple 10, document 5, graffito 2, other 0). If
they do not, the test STOPS and the mismatch is filed.

**Computations.** Over Population S, pooled and per
stratum, and over Population P per arm per stratum:
the attested ordered-pair table (total adjacencies,
distinct pairs, top pair); the per-mark positional table
(sole / initial / final / medial within groups, as at
Spec 105 Stage 3); the two conformance rates — a-sign:
(group-initial + sole) / total occurrences; i-sign:
(neither-initial-nor-sole) / total occurrences — each
with its occurrence count. Out-of-stratum prediction
(Population P, development arm): the funerary stratum's
a- and i-conformance rates are the predictions for the
royal_temple stratum; the record states both strata's
rates and their difference. The full per-stratum
positional table is filed in the raw output, so later
cycles inherit it.

**Floors (registered in advance).** A stratum's
conformance rate is verdict-bearing for a sign only if
that sign's occurrences in the stratum number ≥ 30;
below that floor the rate is filed as description, not
verdict. (The graffito and other strata are expected to
fall below the floor for at least one sign; that is
registered here so it cannot be read as a surprise or
averaged away.)

**Verdict rule (registered, three outcomes).** The two
conformance facts are the verdict-bearing facts, each at
its filed threshold (rate ≥ 0.95, the registered
95-in-100 tolerance of MER-2/MER-3):
- **POSITIVE (stratum-stable)** iff both facts hold
  pooled (Population S) and hold in the funerary stratum
  and in every other stratum carrying an adequate floor
  for that sign.
- **NEGATIVE (genre artifact)** iff either fact holds
  pooled but fails in the funerary stratum, or holds in
  the funerary stratum but fails in every other
  adequate-floor stratum — the corresponding MER license
  (MER-2 or MER-3) narrows in the trace to the stratum
  where the fact holds.
- **INDETERMINATE** for any fact whose adequate-floor
  strata are only the pooled population and funerary
  (i.e., no second stratum carries the floor): filed per
  fact, not averaged into the other fact's verdict; the
  test's headline verdict is POSITIVE or NEGATIVE on the
  facts that could be evaluated, with the indeterminate
  fact named.
Adjacency and positional-class structure per stratum are
filed as description: any mark whose pooled positional
class (never-predecessor, never-successor) appears in no
single stratum, or only in funerary, is flagged in the
outcome record as a pooling artifact at description
level.

**Standings effects (as the design provides).** POSITIVE
converts the program's corpus-wide Meroitic statistics
from pooled claims into controlled ones; MER-2 and MER-3
stand as executed, now stratum-controlled, and M-2/M-3
inherit the control. NEGATIVE narrows the affected MER
license's practical scope in the trace and re-aims M-2
at the strata where the signal, if any, lives; the Stage
6 gate words themselves are historical and are not
rewritten. INDETERMINATE strata are filed per stratum.
No affiliation, gloss, or verdict of Spec 097 moves on
this test.

**Cost class:** Tower.

## 4. Test E-1 — Spec 101 executed as registered (Eteocypriot)

E-1 is Spec 101's postdictive occurrence test, executed
under Spec 101's registration and its binding floor
record, on the owner's commission in the act named
above, with the target standing as declared under OD-D-1
(enrichment, expressly not a recurrence finding). This
record adds nothing to that registration and amends
nothing in it. For the cycle's bookkeeping, the
registered shape is restated:

- **Stages in order** (Spec 101 tasks.md): Stage 1
  intake (T101) — Perna 2019's reading of ICS 194/195
  intaken as a new corpus state under Spec 101's own
  corpus directory, with its C095-3 identity record
  (per-inscription SHA-256 pins; provenance naming
  Perna 2019, *Les royaumes de Chypre à l'épreuve de
  l'histoire* (BCH Suppl. 60), pp. 213–220, DOI
  10.4000/books.efa.3031, as the edition of record and
  the OpenEdition Books route; custody
  `held_from_secondary_reproductions`; the transcription
  method and conventions stated in the identity record);
  the Spec 096 corpus file hashed before and after
  (must equal its version-1.1.1 value `2954283d…`).
  Stage 2 (T201, T202) — the candidate registration
  committed to the repository BEFORE any scoring load of
  the Perna-side state (TC-101-02), candidates derived
  from the ICS 196 development set alone under the
  mechanical rule (the floor record's §2 set: -se
  f = 3, segments 6, 7, 8; -na f = 2, segments 1, 5;
  -i f = 2, segments 3, 4; -ti f = 2, segments 9, 11;
  K = 4, D = 11), then the freeze addendum (P-3: every
  table the scoring uses, in full; floors F_i, E_i, q_i
  and the family-wise Q computed by the floor record's
  §1.3–§1.4 formulas from the registered inputs and the
  intaken census's segment-final position count M; a
  freeze whose Q is at or above 0.05 is defective and
  may not proceed; a candidate whose positions cannot be
  instantiated closes the study TOO THIN at its freeze,
  C101-1 NOT TESTED). Stage 3 (T301) — scoring, executed
  twice with byte-identical outcome records and an
  independent recount (TC-101-03). Stage 4 (T401) — the
  outcome record, carrying the exposure statement
  verbatim (floor record §5's canonical string;
  TC-101-04).
- **Verdict:** exactly the floor record's §1.5 —
  SUPPORTED (at postdictive strength) iff at least one
  candidate's count is at or above its computed floor
  AND Q < 0.05; NOT SUPPORTED iff every candidate is
  below its floor or absent; NOT TESTED on a TOO THIN
  closure. A positive is expressly not a recurrence
  finding (OD-D-1).
- **Standings effects (as the design provides).**
  SUPPORTED gives the program its first postdictively
  supported structural claim about unseen Eteocypriot
  text, at exactly the enrichment license; NOT SUPPORTED
  closes the segment-final line and leaves the
  Eteocypriot position as transliteration plus the
  ensemble record; NOT TESTED leaves C101-1 untested and
  the line open only on a future registration. No paper
  text changes on any outcome; the Spec 096 erratum route
  is untouched.

**Intake transcription conventions** (filed here so the
identity record's statement of method has its registered
source): the transcription is taken from the chapter's
closing plates, *ICS 194 (Perna 2018)* and
*ICS 195 (Perna 2018)*, as published on OpenEdition. A
segment is a maximal sign sequence bounded by the
printed separators (the vertical bar, the double bar,
the colon divider, and the printed corner mark) or by a
line boundary; the underscore in Perna's printing joins
two sequences into one segment, as printed (it marks a
boundary she does not print as a separator); an
underlined sign is transcribed at its printed value with
a changed-reading flag (the plates' underlining marks
Perna's new readings against Masson); each printed
bullet (•) is one unread sign position, transcribed as
an unread sign that carries no value and can be no
candidate's final sign, though its segment still counts
toward M; the numeral group in ICS 195 line 2 (printed
XX II) is one segment of numeral signs, counted in the
sign census as numeral signs and in M as one
segment-final position whose final sign is no candidate
value. Typographic line wraps inside a numbered line do
not break a segment. The identity record states the
resulting censuses (signs by inscription, segments,
M) as transcribed, beside the chapter's own stated
figure (48 new readings on 216 signs), without forcing
the two to agree: if the transcription's census differs
from the chapter's stated total, both figures are filed
and the difference is named, not reconciled silently.

**Cost class:** Desk.

## 5. What this registration does not do

It runs nothing. It does not amend Spec 101, Spec 102,
Spec 100, or any gate; it does not lower any floor; it
does not reopen Spec 103, T502/T503, or Spec 104's
quantum arm. Execution follows in Stage 1 under these
registrations, and any test that cannot be executed as
registered stops and records why, without improvising a
variant.

**AI disclosure:** executed by an AI agent (Muse, via Muse)
at the direction of Tristen Pierson, per constitution sec. VI.
