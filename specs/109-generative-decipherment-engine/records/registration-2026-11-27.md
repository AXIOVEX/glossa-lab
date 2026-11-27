# Spec 109 — Registration (2026-11-27)

The registrations for the shared preflight and the
five parts, in execution order. Every registration
follows the program's falsifiability checklist (Spec
107 §2 Step 2): the item set fixed in advance with its
effective N in the units that bind; the prediction
stated before scoring; the null stated, with a
wrong-family or wrong-language control wherever a
language model is involved; borrowing and contamination
strata handled before scoring, every split
duplicate-aware; the verdict rule stated in advance
with three outcomes always available — a registration
whose verdict rule has no indeterminate outcome is
refused, and none below lacks one. Constants the
checklist allows to be fixed at a part's freeze are
marked FREEZE; everything else is fixed here. Data
pins are stated by the records that carry them; the
execution records file the full hashes.

## 1. Execution order, with the ranking reasoning

**Stage 1 — Preflight (§2).** First, unconditionally:
nothing undeciphered is scored before the generators
pass on known ground truth. Cost: tower compute.

**Stage 2 — Part 2, structure induction (§3), and
Part 3, the context channel (§4).** Induction before
search, because Part 1 propagates from Part 2's
induced positional classes: running the search first
would either waste it on the filed L3 classes alone or
tempt it to tune the classes to its own output, which
the separation rule forbids. Part 3 in the same stage
because it is independent of both, desk-and-tower
cheap, and its site join is one of Part 2's
out-of-stratum validation inputs. Sensitivity, stated
plainly: this ordering assumes induced classes are
worth more to the search than the search's extra
compute would be; if Part 2 returns NEGATIVE (nothing
stable), Part 1 still runs, on the filed L3 classes,
and the trace records that the ordering's premise
failed and cost one stage. The ordering survives that
failure because Part 3's channel is needed either way.

**Stage 3 — Part 1, assignment search (§5).** After
both inputs exist. Cost: tower compute, the study's
largest.

**Stage 4 — Part 5, Eteocypriot candidates (§6).**
After the Indus legs: its generator reuses the Stage 1
harness, and at 69 development tokens it is the leg
most likely to return a null ranking — running it
after the harness is proven costs it nothing and
protects its null from being a harness artifact.
Sensitivity: scored purely on expected decipherment
yield, Part 5 ranks last among the executable parts
under almost any likelihood assignment; it is placed
fourth, not fifth, only because Part 4 cannot execute
at all until its input exists.

**Stage 5 — Part 4, Meroitic gloss induction (§7).**
Last because gated: it executes when Spec 102's
digitisation and freeze exist, and not before,
whatever the state of the other stages.

## 2. The shared conformance preflight

**Item set.** Per generator under test: (a) synthetic
cipher corpora built by the Spec 107 I-1/I-2 machinery
to the target system's profile (for Indus: 1,670
artifacts, 7,002 tokens, the empirical length
distribution, duplication rate d = 20/1670 as filed;
for Eteocypriot and Meroitic, their own filed
profiles), with planted assignments known to the
preflight record and to nothing the generator can
read; (b) the Latin and Meroitic deciphered controls
of Spec 107, at their custody pins. Effective N is the
planted-assignment sign count carrying ≥ 5 tokens in
each synthetic corpus, stated per corpus in the
preflight record.

**Prediction, stated in advance.** A generator that
can recover truth where truth is known will: (i) on
each synthetic corpus, return a top-ranked candidate
whose planted-value recovery — the share of
≥5-token signs assigned their planted values — is at
least the floor FREEZE (registered here as at least
0.80 at the Indus profile at 1× scale, the level
Spec 107's I-1 right-model condition demonstrated is
meaningful at this shape); (ii) on each synthetic
corpus, return a top candidate whose penalized margin
on the synthetic holdout clears the frozen bar form
(≥ 10 nats over the best rival, above the 99th
percentile of the synthetic permutation null, 2 nats
charged per free choice); (iii) on the Latin and
Meroitic controls, in the R1 predictor form, return
RIGHT-condition medians above the WRONG and SHUFFLE
medians, as cycle 2's I-2 preflight measured and
passed.

**The positional limitation, carried on the face.**
Cycle 2 filed that the re-specified positional
ground-truth sets for the Latin and Meroitic controls
hold 1 mark and 0 marks against the measurability
floor of 5: positional recovery on those controls is
NOT MEASURABLE, and no preflight record of this study
may claim a positional figure from them. The
preflight's positional clause therefore runs on the
synthetic corpora of (a), whose ground truth is
planted at counts above the floor by construction, and
the limitation is restated in every preflight record.

**Null and control.** The WRONG and SHUFFLE conditions
are the controls; a generator whose SHUFFLE recovery
approaches its RIGHT recovery has measured itself, and
fails.

**Two implementations.** Every ground-truth set and
recovery figure is produced by two independent
implementations in exact agreement (the I-2 preflight
standard); a disagreement is a preflight STOP, filed.

**Verdict rule.** PASSED (all measurable clauses at
their floors, both implementations agreeing);
FAILED (any measurable clause below its floor — the
generator produces no scoreable output; revision is of
the generator); NOT MEASURABLE IN PART (a clause's
floor unmet by the control material itself — filed
with the clause named; the generator may score only
the output kinds the passed clauses cover).

## 3. Part 2 — Structure induction (Indus)

**Item set.** The full corpus as filed: 390 marks,
1,670 artifacts, 7,002 tokens (Spec 105 Stage 1
census); the derivation set (1,336 artifacts, 5,611
tokens, 372 marks) for every statistic needing a
development side; the counted and stroke-series
contexts as filed in Spec 091's motif-numerical
evidence record (the NUMERAL_FORMULA population).
Effective N per family is stated at the part's freeze:
marks carrying ≥ 5 tokens for positional classes;
sequences carrying a candidate boundary for
segmentation; partials at the frequency floor for
recurrent partials; counted contexts for the numerical
family.

**Method, registered by family.** (a) *Positional
classes:* per mark, its positional distribution
(initial / medial / final / sole) over the corpus; a
mark is class-restricted at level ρ if its dominant
positional share is ≥ ρ, at ρ = 0.95 and ρ = 0.90 (the
realistic levels of Spec 107's I-2). The filed L3
table is the comparison of record: induction must
reproduce it where they overlap, and any divergence is
filed as a finding, not silently resolved. (b)
*Segmentation:* boundary scores from adjacent-pair
mutual information and boundary entropy over the
derivation set; candidate boundaries at the registered
local-minimum rule (constants FREEZE); the output is a
candidate segmentation per sequence, filed as a
hypothesis, never as the corpus's segmentation. (c)
*Recurrent partials:* all initial and final sign
strings of length 2–4 at or above the frequency floor
FREEZE, each with its positional-restriction statistic
at both ρ levels. (d) *Numerical / metrological
subsystem:* the counted-sign set as filed; three
arithmetic checks — bounded range (the count
distribution's support against the shuffle null),
positional restriction (as (a), restricted to the
counted set), and combination consistency (co-occurrence
structure scored against the registered place/count
model form and against the shuffle null). No language
assumption enters any of the four families.

**Stability, registered.** Every induced structure is
computed on both split halves of the derivation set
(duplicate-aware) and, for positional classes, per site
over Part 3's site join. A structure is filed STABLE
only if it reproduces in both halves at its registered
tolerance; otherwise it is filed UNSTABLE with its
figures. A structure tuned after a stability failure
may be refiled only under a new registration.

**Null.** Shuffle distributions preserving each
sample's length and sign frequencies, per family; the
numerical family's null is the unconstrained-tally
shuffle of the design queue's I-7.

**Prediction.** If the corpus carries inducible
structure beyond the filed tables, at least one family
returns STABLE structures not already in the filed
record. If none does, that is the outcome, and it
prices every later structural proposal.

**Verdict rule.** POSITIVE (at least one STABLE
structure filed to the gates); NEGATIVE (no structure
stable in any family — the induction at this corpus
returns nothing that survives its own checks);
INDETERMINATE (a family's stability not measurable at
its floors — filed per family, not averaged away).

**Falsifier and kill.** As C109-3. The leg's kill
instance is §9 criterion 1 in its structural form: a
NEGATIVE closes the induction design as filed; a
revised induction is a new registration, and no
stability tolerance is loosened to rescue a structure.

## 4. Part 3 — Context channel (Indus)

**Item set and joins.** (a) *Population site join:*
the tracked population files (phase100 and phase114,
keyed by `cisi_id`, both carrying a site field) over
the 1,670-seal population. Validation, registered: the
join must reproduce the filed site census of the
Spec 091 record; a mismatch is a STOP, filed, in the
M-1 validation pattern. (b) *Spec 093 census join:*
the 179 joined pairs (site, material, find context).
Validation: the join must reproduce Spec 093's filed
census exactly (179 pairs; Steatite 176, Clay 1,
Faience 1, 1 empty sentinel); a mismatch is a STOP.
The census's filed limits ride on every use: all 179
pairs are Mohenjo-daro, single stratum (C093-1,
INDEPENDENT IN PART), so the material channel is a
single-site channel and no record of this part may
present it as more. (c) *Iconography:* GATED, inactive
(spec.md §6 states what exists, what does not, and
what acquisition requires). No iconography input is
registered for Stage 2, and none may be used.

**Channel statistic.** For a candidate assignment, the
context term is the sum, over the candidate's scored
signs, of the log ratio of the sign's
context-conditional positional rate to its corpus-wide
positional rate, over the registered contexts (site,
from join (a); material and find context, from join
(b), each weighted by its join's effective N under the
formula FREEZE). The term is additive evidence for
other parts' scoring; it is not a margin and cannot
substitute for one.

**Null and cap.** The context null permutes context
labels within strata (B = 999; seed fixed at the
channel freeze and filed — a distinct null from
Spec 098's frozen permutation null, and the records
keep them distinct). The context term's contribution
to any candidate's penalized margin is capped at the
99th percentile of its own null distribution.

**Prediction.** If context carries signal about sign
behaviour beyond provenance, the term computed on
validation material (out-of-site prediction: fit on
one site's texts, applied to another's, duplicate-aware)
discriminates the filed positional classes beyond its
null. If it does not, the channel is null at this
corpus and Parts 1 and 5 run without the term.

**Verdict rule.** CHANNEL POSITIVE (validation
discrimination beyond the null, joins validated);
CHANNEL NULL (joins validated, no discrimination —
filed, and the term is withdrawn from this study's
scoring); INDETERMINATE (a join validation STOP, or
per-site effective Ns below the floors FREEZE).

**Falsifier and kill.** As C109-4. Kill instance:
criterion 4 in its gated form for the iconography
sub-channel (it activates only through Spec 100's
gate or an equivalent tracked join under its own
registration; it is not killed by waiting, it is
simply not open), and criterion 1 for the channel
proper (a CHANNEL NULL closes the context-term design
as filed).

## 5. Part 1 — Assignment search (Indus)

**Freeze sequence, registered in order.** (1) Part 2's
induced classes filed (or its NEGATIVE filed, in which
case the filed L3 classes stand as the constraint
source and the substitution is recorded). (2) The
constraint set versioned: the register's E-standing
anchor values listed by sign (3 anchors at
registration: the register stands 3 E + 66 I + 4 R +
3 P + 18 U over the 94 strict core, 287 anchors in
all), held as hard constraints; the induced positional
classes at their filed version. (3) The value inventory
filed: per unanchored sign, the phonetic value-classes
of the candidate families as filed in the World
Language Graph's dossiers at release WLG-R1 (148
nodes, 129 edges, 365 assertions, 7 sources; the
graph's Indus gap entry — script S0, language L0,
blocker INFORMATION — carried on the freeze record's
face as the bound on what the space can offer), plus
the structural class (logographic / numerical /
classifier). The inventory is closed at the freeze;
no value enters after any held-out observation
(Spec 098's selection control, carried over verbatim).
(4) The 109 reserve cut duplicate-aware from the
derivation set, its membership hash-committed in the
freeze record; its token count and per-sign counts
stated as the power denominator. (5) The search
schedule registered: restart count, seed list, and the
annealing schedule's form (constants FREEZE). Only
then does any search run.

**Search.** Constraint propagation first: an assignment
violating a hard constraint is inadmissible and is
never scored. Simulated annealing over admissible
assignments, under the registered schedule and seeds,
optimizing the mean duplicate-aware 5-fold
cross-validated predictive log-likelihood under the
frozen scoring rule's predictor form, computed on the
derivation set only. (The Round N qualification rides
on this objective's face: the filed scoring weights are
not row-normalized probabilities — row-mass witnesses
1.152023 / 1.279273 / 1.287293 — so the objective is a
search-internal ranking quantity under the frozen
rule as filed; adjudication margins are decide()'s,
which are defined on that rule as filed, and no
normalized predictive log-loss advantage is claimed
for either.) Every run is indexed, failures included
(Spec 089 run-scoped discipline), and every candidate
the search emits carries its full generation
provenance (spec.md §8).

**Candidate selection.** The top-K distinct admissible
assignments by objective, K = 20; distinctness at the
registered minimum Hamming distance FREEZE, so the
ranked set is a set and not twenty copies of one
optimum.

**Adjudication.** The reserve is opened exactly once,
and the opening is recorded. Each candidate is scored
under Spec 098's frozen decide() rule against the best
rival from the registered rival set: the other
candidates, the structural-only rival (the
assignment-free structural predictor, Part III's R-D
analogue), and the register's filed rival constructions
where they exist for a scored sign. Free choices are
charged at the frozen 2 nats per searched sign
assignment; the per-candidate free-choice count is
filed with its margin. The outcome vocabulary and bars
are Spec 098's, verbatim (spec.md §4).

**Prediction, stated in advance.** If the structure of
a corpus of this shape is identifiable by search of
this kind — the quantity Spec 107's I-1/I-2 calibrated,
at the levels they filed — at least one self-generated
candidate clears the frozen bar on the reserve. If
none does, SEARCH NEGATIVE AT THE FROZEN BAR is the
outcome, and it is a finding about the search and the
information available, filed as such.

**Verdict rule.** At least one candidate
DISCRIMINATED / IDENTIFIABLE ON HELD-OUT (the reserve
being a genuine holdout): the leg's positive outcome,
and the candidate enters adjudication as a candidate —
no standing moves on this study's act. No candidate at
the bar: SEARCH NEGATIVE. The reserve's per-sign
floors unmet for the candidate population: INDETERMINATE
AT THIS POWER, and no fallback scoring on derivation
material under a held-out label.

**Falsifier and kill.** As C109-2. Kill instance:
criterion 1, in the commission's own form — the bar is
never revised; the search design (space, constraints,
objective, schedule) is what a later registration
revises, informed by the filed margins and the null.

## 6. Part 5 — Eteocypriot reading candidates

**Item set.** The ICS texts as filed in Spec 096's
corpus state (ICS 196; ICS 194/195 at form level;
ICS 193's one form), the development stream (69
tokens, 35 derived marks, 18 singletons, 53 of 54
attested adjacencies occurring exactly once — the
corpus floor stated, not discovered later), and the
held-out forms: the 7 ICS 194/195 forms (45 signs) and
the ICS 193 form. Effective N is per-text sign count,
stated per text in the candidate records.

**Comparanda, registered and closed.** (a) The
bilingual's two scored Greek name anchors (the Spec
104 benchmark instance: ICS 196, 2 names × 11
segments, certified classical optimum 6). (b) The E1
derivation tables, when filed complete under Spec
101's precondition P-3. If (b) is not filed at this
part's freeze, the comparanda are (a) alone and the
reduction is stated on the freeze record's face. No
other comparanda enter; the set is closed at the
freeze.

**Generation and ranking.** For each text, candidate
readings are composed from the transliteration under
each registered comparanda mapping variant, and ranked
by a lexicographic rule, mechanical in this order:
(1) *held-out form prediction* — the candidate's
implied endings occurring in the held-out forms at
rates above the registered form-level null (the
design queue's E-4 count, mechanized); (2)
*comparanda coverage* — the share of the text's signs
carrying a comparanda-anchored value under the
candidate; (3) *distributional fit* — the candidate's
implied sequence statistics against the development
stream's, using only statistics the E-2 control
calibration (Spec 107 cycle 2, gated there on C-E-15,
which returned STOP, so E-2 did not execute) — since
E-2 did not execute, component (3) is DROPPED at
registration and the drop is stated here: the ranking
runs on components (1) and (2) until a calibration
exists under its own registration.

**Null.** The ranking recomputed under permuted
comparanda mappings (registered permutation, seed
FREEZE). A candidate set whose top ranks are
indistinguishable under permutation is filed as
null-indistinguishable.

**Prediction.** If the comparanda carry signal at
corpus level, the top-ranked candidates separate from
the permutation null on component (1). The honest
expectation is stated in advance, as the design queue
states it for this corpus: at these sizes the likely
product is a ranked set with a null result on
separation — which still replaces the consumed-pair
bottleneck (cycle 2's C-E-15 STOP: the ICS 196 pair
consumed, the remaining item failing condition (iv))
with a corpus-level instrument whose null is on the
record.

**Verdict rule.** RANKED SET FILED (the normal
outcome: the ranking is the product); RANKING NULL
(top ranks null-indistinguishable — filed, and the
comparanda set is recorded as carrying no rankable
signal at this corpus size); NOT EXECUTED (the part's
preflight clauses or its input precondition unmet —
filed with the reason). No positive or negative
decipherment verdict exists for this part, and none
may be filed under it.

**OD-O-2, stated.** OD-O-2 stands unruled. This part
neither resolves nor presumes it; its records carry no
licensing language; and cycle 2's position stands —
no "all checks passed" statement for Eteocypriot
appears anywhere in this study.

**Falsifier and kill.** As C109-6. Kill instance:
criterion 1 in ranking form (a RANKING NULL closes the
comparanda set as filed; new comparanda are a new
registration), and criterion 3 (a ranking that
survives its own permutation null is a pipeline
measurement, and the part closes until redesigned).

## 7. Part 4 — Meroitic gloss induction

**Gate, registered first.** This part executes only
when both exist: Spec 102's digitisation landed (the
Rilly 2010 lexique and NES apparatus, in transit at
registration — Peeters order of record, no delivery
estimate) and Spec 102's freeze filed (the filtered
vocabulary and family sets under Spec 102's own
registration). It consumes Spec 102's gates as filed —
G-1 (≥ 40 scored concepts per family test, ≥ 20
outside the twelve) and G-2 (≥ 80% injection power at
θ = 0.30, d = 0.75) — without changing them: the gates
decide whether Spec 102's test is administered, and
this part's vocabulary is whatever that freeze files.
If Spec 102 closes NOT ADMINISTERED, this part files
NOT ADMINISTERED — INPUT GATE UNMET and does not
execute; it does not source vocabulary elsewhere. The
Appendix in custody (Rilly & de Voogt 2012: 200
numbered concept entries printing no Meroitic form for
any concept; 82 of 100 ASJP concepts mapped; 0 usable
scored concepts from it alone, as Spec 102's
preparation filed) is not a substitute vocabulary and
is not used as one.

**Item set.** Spec 102's frozen filtered vocabulary
(forms and their concepts, as the freeze files them);
the frozen Meroitic partition (335 development / 33
held out, Kovetsky build at its pin, strata as M-1
filed them stratum-stable); the candidate families'
lexicons as the freeze files them (the R1 Northern
East Sudanic set and the R2 Afroasiatic set of Spec
102's registration), with the World Language Graph's
family dossiers (WLG-R1; the Meroitic gap entry —
S3/L2 unmerged, blocker POWER — carried on the
face). Effective N: scored forms per family, as the
freeze states them; the held-out denominator is the
33 held-out texts.

**Generation.** Per frozen form: a distributional
profile from the development partition (positional
class under M-1's stratum-stable tables; adjacency
profile; stratum distribution). Candidate glosses are
the candidate families' lexicon entries whose
structural profile — computed from the lexicon forms
as filed, under the similarity rule FREEZE — matches
the form's profile; ranked per form, top-M candidates
retained (M = 10, FREEZE), each with full generation
provenance.

**Scoring.** Held-out prediction: a gloss candidate
scores by how well its assigned gloss-class predicts
the form's contexts in the 33 held-out texts, against
(a) the permutation null (gloss labels permuted across
forms, B = 999, seed FREEZE, filed, and kept distinct
from Spec 098's frozen null) and (b) the wrong-family
control — the identical pipeline run against the other
family's lexicon. A pipeline that discriminates in
both directions has measured its own flexibility, and
the part closes under kill criterion 3. Borrowing
stratum handled before scoring: Egyptian loans in
Meroitic, as Spec 102's freeze identifies them, are
scored as their own stratum or excluded per the
freeze's own treatment — this part adopts the
freeze's treatment and does not invent its own.

**Prediction.** If distributional induction carries
gloss signal at this vocabulary size, at least one
form's top candidate beats both the null and the
control at the registered bar (margin form FREEZE,
stated in decide()-comparable terms at the freeze:
penalized margin, null percentile, per-form held-out
token floor). If none does, the distributional route
at this vocabulary size is closed as non-evidence,
which is a material finding about the route, filed as
such.

**Verdict rule.** POSITIVE (at least one form's top
candidate at the bar against null and control);
NEGATIVE (none — filed, route closed as above);
INDETERMINATE (the frozen vocabulary below the
freeze's own floors for this part, stated per family);
NOT ADMINISTERED — INPUT GATE UNMET (the §7 gate
closes unmet). A POSITIVE files gloss candidates to
the program's candidate adjudication machinery (the
Spec 097 Stage 4.4 pattern) under a separate filing;
it is not an affiliation verdict, which remains
Spec 102's alone, and it is not a gloss.

**Falsifier and kill.** As C109-5. Kill instances:
criterion 4 (the gate), criterion 3 (the control),
criterion 1 (a NEGATIVE closes the induction design
as filed).

## 8. Information requirements, per part

| Part | New information consumed | Information re-used | Standing effect it can ever have |
|---|---|---|---|
| Preflight (§2) | None — controls are known-truth material, held or pinned | Spec 107's simulation machinery, donors, and preflight pattern | None; it gates the other parts |
| Part 2 (§3) | None | The full corpus and derivation set as filed; the filed L3 tables as comparison | None directly; files hypotheses to the existing gates |
| Part 3 (§4) | None at Stage 2. The gated iconography sub-channel would consume custody information into the tracked record, only through Spec 100's gate | Spec 093's outputs; the population files' site field | None; its term is an input to other parts' scoring |
| Part 1 (§5) | None — the 109 reserve is a re-partition of held material, not new information | Corpus, register, induced classes, the graph as filed | Can put a candidate before Spec 098's gate, and no further |
| Part 5 (§6) | None | Transliteration, registered comparanda, held-out forms | None; ranks candidates only |
| Part 4 (§7) | **Yes** — the Rilly 2010 digitisation, shared with Spec 102; the only input in this study that did not exist in the program before | Spec 102's freeze; the frozen partition; the graph's dossiers | Can file gloss candidates to candidate adjudication, and no further |

The table is itself a registered statement of this
study: a part's outcome may not claim an effect its
row does not license (C109-9).

## 9. Kill criteria

The study-level criteria are spec.md §9. Their
instances per part are registered in §§3–7 above. Two
discipline statements bind every instance: the bar is
never revised in response to a negative outcome — the
design is revised, under a new registration, with the
filed margins and nulls as its evidence; and a part
that closes under a kill criterion files its closing
outcome in the study's stage-close record, with the
criterion named.
