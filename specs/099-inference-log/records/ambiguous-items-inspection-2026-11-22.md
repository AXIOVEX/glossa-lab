# Spec 099 ambiguous-items inspection — basis-survival view

Filed 2026-11-22. Commission: adjudication item OD-6 (from
I-23) of `specs/091-anchor-comparison-integrity/records/`
`coscientist-refresh-adjudication-2026-11-22.md`, the owner's
act of 2026-11-22 11:37 ET. Venue: tower-compute, fresh clone
`~/glossa-work/od6-inspect-2026-11-22`, built on main
`8c272479`. The standing glossa-lab clone-processing approval
(owner, 2026-11-22 11:26 ET) covers the clone work.

## Population

The 25 `ambiguous` items of the Spec 099 census, exactly as
filed in the current inference log
(`records/inference-log.json` at the base above: 296 items —
210 (a) primary, 61 (b) candidate-system, 25 ambiguous; the
log's executed classes are the current standings, 3 E + 66 I
+ 4 R + 3 P + 18 U = 94). The 25 items sit in 23 entries:
M029-02, M032-01, M042-01, M046-01, M049-01, M052-01,
M053-01, M054-01, M055-01, M061-01, M076-01, M087-01,
M108-01, M128-02, M130-01, M145-01, M145-03, M165-01,
M194-01, M194-03, M222-02, M264-01, M267-04, M311-01,
M398-06. Every one is a `consistency_score` item. No item
was re-typed by this inspection (spec section 3.4); this
record states the inputs as a supplementary record and flags
consequences. No standing or class changes are made here.

## Checks run (the same battery for every item)

1. **Log extraction.** The item's statement, basis span,
   filed reason, and its entry's full filed basis and sibling
   items, read from the current log.
2. **Definition search.** The score's definition located in
   the phase script of record in this repo (all five
   families found; citations below).
3. **Recorded-output search.** The phase's recorded run
   output read for the item's own sign (all five families'
   outputs are in `outputs/`; every population sign found).
4. **Removal outcome.** The Spec 099 audit
   (`tools/inference_log.py audit`) re-run over the current
   log in this clone: **PAYLOAD VERDICT: DONE
   (class_changes_primary=0, weakened_primary=44, cycles=0,
   open_ends=38), payload exit 0**; under the sensitivity
   treatment (remove (b) and ambiguous items) class changes
   are likewise 0, and the 23 population entries are exactly
   the audit's 23 divergent readings — each loses its
   ambiguous item(s) and is weakened, none changes class.
5. **Use search.** Where else the score does work: the
   Phase-116 / Phase-216 upgrade acts themselves (the basis
   strings are those acts' own appended notes, format-
   identical to the scripts); the Spec 098 Stage 2
   prediction sheets; the staging verify endpoint's own
   record.

## Family 1 — the SA-cons scores (20 items)

**Definition (as coded).** `backend/scripts/`
`phase116_sa_recalibration.py` and
`phase216_sa_recal_410anchors.py`. SA-cons is the modal
share of an ensemble of simulated-annealing decipherment
runs: each run decipheres the Holdat corpus sign sequences
under a Dravidian word-symbol language model with the
register's HIGH + MEDIUM readings pinned as its anchors
argument (131 pinned at Phase-116, 161 at Phase-216 —
including the evaluated sign's own filed reading, since the
evaluated signs are MEDIUM), surjective mapping, 6,000 /
8,000 iterations, 4 restarts, 8 seeds (Phase-116) / 6 seeds
(Phase-216). SA-cons = (seeds proposing the modal value for
the sign) / (seeds proposing any value).

**The unstated inputs, stated.** (i) The Holdat corpus
sign sequences (primary data). (ii) The Dravidian
word-symbol language model — the candidate language itself,
as an input. (iii) The pinned candidate anchor system —
other readings' values, and the sign's own. (iv) The
ensemble's parameters. None of these is stated in any filed
basis; the basis states only the number.

**What the recorded outputs show.** Both phases applied an
upgrade test (a DEDR leg, and a consistency leg satisfied
by SA-cons ≥ 0.40 **or** by a source-string fallback — the
sign's recorded source containing a listed token such as
"Parpola" or any "Phase-NNN") and, on a pass, upgraded the
sign MEDIUM → HIGH and appended the SA-cons note to its
basis. The recorded eval logs (`outputs/`
`phase116_sa_recalibration.json`,
`outputs/phase216_sa_recal_410anchors.json`) give, for
every one of the 20 population items:

- the ensemble's modal proposal is **not the filed
  reading** — in 20 of 20 cases. The filed SA-cons value is
  the modal share for a different value (table below);
- the consistency leg was carried by the **source-string
  fallback in 19 of 20 cases** (every value but M042's is
  below 0.40). M042's 0.62 cleared the bar on the value —
  the value being 'ko''s modal share, not vaN's.

| Item | Sign (reading, class) | SA-cons as filed | Ensemble modal (recorded) | Consistency leg carried by |
|---|---|---|---|---|
| M032-01 | M032 (koL, I) | 0.12 | tetam | source fallback |
| M049-01 | M049 (pu, I) | 0.12 | nalna | source fallback |
| M052-01 | M052 (ta, I) | 0.12 | nalavar | source fallback |
| M061-01 | M061 (ka, I) | 0.25 | vil | source fallback |
| M076-01 | M076 (naN, I) | 0.12 | paadu | source fallback |
| M128-02 | M128 (kaṇ, I) | 0.12 | vinathaa | source fallback |
| M130-01 | M130 (mui, I) | 0.12 | campan | source fallback |
| M194-01 | M194 (kaṭ, I) | 0.12 | tiruttam | source fallback |
| M087-01 | M087 (veL, R) | 0.12 | kovan | source fallback |
| M264-01 | M264 (peN, R) | 0.12 | untaaka | source fallback |
| M311-01 | M311 (vaTamiin, R) | 0.12 | viriyu | source fallback |
| M042-01 | M042 (vaN, U) | 0.62 | ko | the value (0.62 ≥ 0.40) |
| M046-01 | M046 (kaL, U) | 0.12 | machchan | source fallback |
| M108-01 | M108 (kaL, U) | 0.12 | annai | source fallback |
| M029-02 | M029 (yānai, I) | 0.17 | allaar | source fallback |
| M053-01 | M053 (mi, I) | 0.17 | ayini | source fallback |
| M054-01 | M054 (mi, I) | 0.17 | colvai | source fallback |
| M055-01 | M055 (miN3, I) | 0.17 | tittam | source fallback |
| M145-01 | M145 (miṭ, I) | 0.17 | munnu | source fallback |
| M165-01 | M165 (cul, R) | 0.17 | neermai | source fallback |

**Verdict, all 20 items: DOES NOT SURVIVE AS FILED.** As
filed — a consistency score sitting with a ✓ in the basis
of an upgrade act — the item presents ensemble agreement
behind the filed reading. With the inputs stated, the
number measures agreement on a different value, computed
over interpreted material (the pinned system and the
Dravidian model), and in 19 of 20 cases it was not even
the operative leg of the act that wrote it into the basis.
The item may not be cited as consistency support for its
reading. The entries' classes are unaffected (check 4):
each entry's class rests on its (a) items, and removal of
the ambiguous item changes no class.

## Family 2 — the Phase-95 expansion scores (M145-03, M194-03)

**Definition (as coded).** `backend/scripts/`
`phase95_retroflex_expansion.py`: evidence_score = a base
by the phase's own candidate-table confidence tier (HIGH
2.1, MEDIUM 1.6, LOW 0.8) + 0.3 if the candidate reading
contains a retroflex consonant + 0.1 if the sign's corpus
frequency is ≥ 10. The recorded output
(`outputs/phase95_retroflex_expansion.json`): M145
(miṭ) and M194 (kaṭ) both score 1.90 = 1.6 (their MEDIUM
tier in the phase's candidate table) + 0.3 (retroflex ṭ);
corpus frequencies 3 and 4, so no frequency term. The
score gated their entry into the anchor register as
MEDIUM anchors (threshold 1.5).

**The unstated inputs, stated.** The phase's own prior
confidence tier for the candidate (an assigner's judgment,
filed only inside the script's candidate table); the
retroflex bonus; the corpus frequency (primary data). No
other reading's value enters the score.

**Verdict, both items: SURVIVES INTACT as a citation;
evidentiary content nil.** The filed statement ("Phase-95
retroflex expansion score=1.90") is accurate, and the item
never presented itself as a measurement of the reading.
Once its inputs are stated it is bookkeeping: the number
restates the tier the phase itself assigned, plus bonuses.
It is not evidence for miṭ or kaṭ; both entries rest on
their (a) dictionary items, and removal changes no class
(check 4).

## Family 3 — the Phase-64 score (M267-04)

**Definition (as coded).** `backend/scripts/`
`phase64_morphological_boundary.py`,
`score_m267_candidates`: a hand-weighted ranking of
M267's four candidate readings against its corpus context.
The recorded output (`outputs/`
`phase64_morphological_boundary.json`) gives iṉ 7.0 —
the filed value — as 2.0 (medial position consistent with
a genitive) + 2.5 (M267 precedes M099 strongly: 84
co-occurrences) + 2.0 (M328 precedes M267: the
agent–genitive–title pattern) + 0.5 (multisyllabic
candidate). The rival col scores 6.5 on the same terms.

**The unstated inputs, stated.** (i) M267's positional
and bigram counts in the Holdat corpus (primary data).
(ii) The interpretations of the neighbouring signs that
give the two largest terms their meaning: M099 read as
kol 'lord' (the +2.5 term) and M328 read as the agentive
ā/āl (the +2.0 term) — other readings' values, nowhere
stated in M267's filed basis. (iii) The weights
themselves (2.0 / 2.5 / 2.0 / 0.5), set by the phase
author, not derived. (iv) The four-candidate set the
score ranks.

**Use check.** The Spec 098 Stage 2 prediction sheet for
M267 states of this item, verbatim in substance: the
Phase-64 score "is unusable until its inputs are stated",
and Stage 2 relied instead on the slot pattern restated
over bare sign identities (item M267-05). The score fed
no Stage 2 determination, and Stage 3's design descends
from those sheets.

**Verdict: SURVIVES AS CITATION ONLY.** The statement
("Phase-64 score=7.0 for this reading") is accurate —
iṉ did score 7.0, first of four. With the inputs stated
the item is candidate-system material: a ranking inside
an interpreted pattern, not primary evidence for the
genitive reading. M267's class I rests on its (a) items
(dictionary, corpus count, positional statistic);
removal changes no class (check 4). This record states
the inputs the Stage 2 sheet required; the score's
status as non-evidence is unchanged by that statement.

## Family 4 — the staging score (M222-02)

**Definition (as coded).** `backend/glossa_lab/`
`pipelines/research_loop.py`, template
`compound_semantic_coherence`: a staged candidate's
evidence_score = the loop experiment's global `valid_pct`
/ 100 — a whole-system percentage (compounds judged valid
across the first 200 corpus sequences under the
then-current anchor assignments), not a measurement of
the candidate sign. The candidate's proposed reading is
produced by a fixed partner/complement table
(`_compound_partner`) applied to the anchor reading of a
HIGH neighbour sign, gated on a DEDR vocabulary gloss
lookup for the proposed partner. M222's score=1.00 is
valid_pct = 100 at that run; its reading 'min' is the
table's partner for a neighbour's reading. The Phase-108
provenance register records the same act from the other
side: the reading was "proposed by the automated research
loop … from fixed partner/complement tables", and
"promoted via /staging/verify-sa, which performs no SA
test despite its name" — the endpoint has since been
renamed (`/staging/verify-archive`) with the no-SA-test
fact stated in its own docstring, and the Spec 094
named-human gates now on that transition postdate the
2026-06-07 promotion. The 'verified' in the filed basis
is that status transition.

**The unstated inputs, stated.** The system-global
valid_pct; the neighbour sign's anchor reading; the
fixed partner table; a gloss lookup as the only lexical
gate; a verification step that performed no test of the
reading.

**Verdict: DOES NOT SURVIVE AS FILED.** As filed —
"staging score=1.00, status=verified" — the item
presents a per-sign coherence measurement, verified.
With the inputs stated, the number is a property of the
whole assignment system at a moment, the reading is a
table lookup off another reading, and the verification
tested nothing. M222's class P (provisional, no
documented expert or referral) is a workflow state and
does not rest on this item; removal changes no class
(check 4). The entry's remaining basis is its (b)
slot-label premise and its (a) dictionary item.

## Family 5 — the Phase-103 name score (M398-06)

**Definition (as coded).** `backend/scripts/`
`phase103_name_lexicon.py`: name_score = (3 ×
genitive-pattern count + 2 × animal-pattern count + 3 ×
name-pattern count) / (the sign's total name-slot
patterns), where the patterns are corpus contexts
defined by sign-role sets — GENITIVE = {M267};
SUFFIX_SIGNS including M342 and M176; ANIMAL_CLASSIFIERS
and TITLE_SIGNS as sign sets. The recorded output
(`outputs/phase103_name_lexicon.json`) gives M398:
5 name slots (1 GENITIVE_NAME_SUFFIX, 1 NAME_AY_AN, the
rest HIGH_CONTEXT), name_score = (3 + 3) / 5 = 1.2 —
the filed value. Phase-103 proposed no reading for M398
(its row: sa_modal empty, proposed_reading null); the
reading kuṟi was assigned at Phase-105 on iconography
and DEDR 1769.

**The unstated inputs, stated.** (i) Corpus pattern
counts over sign identities (primary data). (ii) The
role sets that define the patterns — above all M267 in
the genitive role (its own candidate reading) and
M342 / M176 as the oblique / masculine suffix signs
(their candidate readings): the GENITIVE_NAME_SUFFIX
pattern instance in M398's basis, [M267]-[M398]-[M342],
is the interpreted 'of-kuṟi-belonging' frame. (iii) The
hand-set weights (3 / 2 / 3). The score measures
name-slot pattern fit; it does not measure the reading
kuṟi at all.

**The truncation.** The filed basis truncates the
item's own statement mid-clause: "Score 1.2 (hi". The
source record completes the clause — the Phase-105
record (`outputs/phase105_name_signs.json`) files the
basis sentence whole: "Score 1.2 (highest name_score in
Phase-103 top candidates)." Section 3.4 bars completing
a filing by inference, so the item is **not** repaired
here; the completion is recorded as a check result only.

**Verdict: DOES NOT SURVIVE AS FILED.** The item as
filed is an incomplete statement of a score whose
definition the basis nowhere states. With the inputs
stated from the records, the score is a name-slot
pattern statistic resting in part on other readings'
roles; it is not evidence for kuṟi. M398's class P is a
workflow state; removal changes no class (check 4).

## Aggregate

- **Unstated inputs found: 25 of 25.** Every family's
  definition and recorded run output is in this repo;
  there is no item whose inputs could not be stated.
- **Item verdicts:** survives intact (as a citation,
  evidentiary content nil): 2 (M145-03, M194-03).
  Survives as citation only (candidate-system material,
  not evidence for the reading): 1 (M267-04). Does not
  survive as filed: 22 (the 20 SA-cons items, M222-02,
  M398-06).
- **Entry bases:** all 23 entries keep their executed
  class with every ambiguous item removed (Spec 099
  audit re-run on the current log, check 4: 0 class
  changes under both treatments; the 23 entries are the
  audit's divergent set, weakened under the sensitivity
  treatment by exactly these losses). **No entry's class
  rests on an ambiguous item.** In the stronger sense,
  no entry whose basis presents a score as corroboration
  survives intact: 22 of the 25 items were filed in
  forms their stated inputs contradict or cannot
  complete, and every one of the 23 entries carries at
  least one such item except — none: M145 and M194,
  whose Phase-95 items survive as citations, also carry
  SA-cons items (M145-01, M194-01) that do not.
- **Promotions and Stage 3 (the I-23 concentration):**
  the SA-cons items are the residue of real promotion
  acts (Phase-116 and Phase-216 MEDIUM → HIGH upgrades),
  and the Phase-95 scores gated two register entries;
  in every case the act's operative legs were other
  than the score's evidentiary value (the DEDR leg and
  the source fallback; the tier the phase itself had
  assigned). No ambiguous item feeds a Spec 098 Stage 2
  determination — the one Stage 3 sign in the population,
  M267, has its Phase-64 item expressly quarantined by
  the Stage 2 sheet — and no other population sign is in
  the Stage 3 population (M089, M267, M347, M375).

## Consequences flagged for the owner (nothing executed)

1. **Citation bar.** The 20 SA-cons values, the staging
   score, and the Phase-103 score must not be cited —
   in the paper, the research pages, or future sheets —
   as consistency or coherence support for their
   readings. Where an SA-cons value is cited at all, its
   ensemble modal (a different value in 20 of 20 cases)
   must be stated alongside.
2. **M222's staging leg.** The 'min' reading's staging
   provenance (a system-global score, a table-lookup
   derivation, a no-test verification) should travel
   with any future statement of M222's basis, as the
   Phase-108 register already begins to do.
3. **M398-06's truncation.** The Phase-105 record
   completes the clause on file. Repairing the log item
   itself would be an act citing new filed evidence
   under section 3.4; this inspection does not perform
   it.
4. **M267-04 and Stage 3.** The inputs the Stage 2
   sheet required are now stated in this record. The
   score remains candidate-system material (its two
   largest terms rest on the M099 and M328
   interpretations); whether Stage 3 may now treat it
   as usable on those terms is for the Stage 3 record,
   not this one.

No standing, class, or log item was changed by this
inspection.
