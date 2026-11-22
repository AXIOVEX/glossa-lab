# Spec 097 — OD-20: Reassessment of soreyi Against Anchor-Only and Genre/Formula Baselines (Stage 4.4)

**Date: 2026-11-22. Commission:** owner decision OD-20 from
the Co-scientist refresh adjudication
(`specs/091-anchor-comparison-integrity/records/coscientist-refresh-adjudication-2026-11-22.md`,
unit M-17), commissioned by the owner 2026-11-22 13:44 ET.
**Venue:** tower-compute. **Method:** the frozen Stage 4
pipeline (`pipeline-v2.py`, campaign scratch, SHA-256
`74b831da221f0708b2c5a9f7e9f1a7772175fe2097783f101d33588769e1642e`)
imported as a module; Stages 4.3 and 4.4 were re-executed
through its own `stage43()` / `stage44()` functions and both
baselines were computed with its own `partition()`,
`tokens_of()`, and `build_vocab()`, so the tokenization, the
hash split, and the vocabulary are the frozen ones. Driver:
`tools/od20_soreyi_baselines.py`; full numeric output:
companion `od20-soreyi-baseline-results-2026-11-22.json`
(SHA-256
`6e1b022845ba82c30c2e0004abd5f25bfd1ba695902da7d84448381d8c6c41b9`).
**Scope:** soreyi, Stage 4.4's one PARTIALLY SUPPORTED
candidate (5 UNSUPPORTED, none SUPPORTED), under freeze v2.
The corpus computed on is the acquired Kovetsky inscription
corpus (CC BY 4.0 data, `inscriptions.jsonl` SHA-256
`1e91e3a0c52626482bc4015b597df862e7818602dab48a7e870240ab2e567bc4`),
the basis freeze v2 registers for Stages 4.2–4.4. No
Otten-derived text is read or published; every number below
is an aggregate. **This reassessment changes no verdict,
tally, or standing.** Its conclusion (§4) is that the
PARTIALLY SUPPORTED standing survives both baselines in
exactly the sense the Stage 4.4 adjudication stated it; no
item is flagged for adjudication.

## 0. Reproduction gate

Before any baseline was computed, the frozen path
reproduced the filed record exactly:

- Regenerated Stage 4.3 candidates are JSON-equal to the
  filed `stage-4-3-candidates.json` (SHA-256
  `4f1e7812488b7760003194153758915680d6d9a25f34c86d7e16daf8b4a86167`):
  6 candidates, all IDENTIFIABLE (provisional, for blind
  test); soreyi 137 development occurrences, funerary share
  1.0, route theonym_context_BD, filiation adjacency 0.0,
  frozen prediction presence in at least 3 held-out texts
  with held-out funerary share in [0.75, 1.0].
- Regenerated Stage 4.4 candidates are JSON-equal to the
  filed `stage-4-4-results.json` (SHA-256
  `11369924c0ad5568ea32f7ad7b55c11052eaa18ec88cc2dea3e3e2459d490e8f`),
  and the regenerated anchor controls equal the executed
  scratch controls exactly (held-out funerary: ato 11, qore
  2, kdi 1, ste 1, mk 1; royal/temple: qore 1). Held-out
  partition by stratum: funerary 16, royal/temple 10,
  document 5, graffito 2 — 33 texts, 335 development.

**What the filed support rests on.** soreyi's PARTIALLY
SUPPORTED score rests on three legs: (i) the Stage 4.3
generation profile (137 development occurrences, funerary
share 1.0, theonym-context route, filiation adjacency 0.0
defeating the proper-name rival at the screen); (ii) the
Stage 4.4 held-out leg (10 occurrences in 10 of the 16
held-out funerary texts, 0 in every other stratum, funerary
share 1.0 inside the predicted range — PASS); and (iii) the
adjudication's stated substantive fact, that soreyi behaves
exactly as a spelling variant of the anchored Osiris
theonym sorey should behave. The score was capped at
PARTIALLY SUPPORTED, not SUPPORTED, for two recorded
reasons: the held-out seal is procedural and unverifiable
by construction (freeze v2 §6), and leg (iii) — the reading
as generated ("theonym-adjacent cult or offering term") is
weaker than the variant fact the blind test actually
supports. The two baselines below test legs (ii) and (iii)
separately: §2 admits only the anchor evidence; §3 admits
only the corpus's genre and formula structure.

## 1. The anchor, as registered and as spelled in the corpus

Freeze v2 §3 registers the Class B anchor B1 as **wos
"Isis", sorey "Osiris"** (Rilly & de Voogt 2012, p. 10, gold
apparatus). The frozen vocabulary (182 forms) carries three
theonym-family entries, all certain, all gold-lexicon:
**wos** "Isis", **wosi** "Isis", and **sorey** "Osiris".
soreyi and asoreyi are not in the vocabulary — which is why
they entered the Stage 4.3 candidate pool at all.

In the inscription corpus itself, the anchor's base
spelling is absent and its variant spelling carries the
whole distribution:

| Form | Dev occ / texts | Held occ / texts | Funerary share (occ) |
|---|---|---|---|
| sorey (anchor, as registered) | 0 / 0 | 0 / 0 | — |
| soreyi | 137 / 124 | 10 / 10 | 1.0 dev and held |
| asoreyi | 23 / 19 | 2 / 2 | 1.0 dev and held |
| wosi (registered variant of wos) | 163 / 146 | 12 / 12 | 1.0 dev and held |
| wos (anchor, as registered) | 17 / 14 | 3 / 1 | 0.35 dev |

sorey occurs **0 times in all 368 distinct texts**, on
either side of the split, in any stratum. The variant class
{sorey, soreyi, asoreyi} totals 160 occurrences in 143
development texts and 12 occurrences in 12 held-out texts,
every occurrence funerary, funerary share 1.0 on both sides.

## 2. Anchor-only baseline

Admitting only the anchor evidence — the B1 pair, the
frozen vocabulary's own registrations, and soreyi's
behaviour relative to that anchor, with the candidate
machinery (generation routes, identifiability screen, the
other five candidates) removed — the numbers are:

- **Slot identity.** wosi opens the funerary text: 84.05%
  of its 163 development occurrences are text-initial.
  soreyi sits immediately after it: 94.89% of its
  development occurrences are medial (100% on held-out),
  and its single most frequent neighbour is wosi — 120 of
  137 development adjacency counts, an adjacency rate of
  0.8832 per occurrence. soreyi's theonym-set adjacency
  (neighbours in {wos, sorey, amni, wosi}) is 121 counts,
  identical to its wos-family count of 121: every theonym
  neighbour soreyi has, on the development set, is the Isis
  spelling. On held-out, 10 of 10 soreyi occurrences are
  wosi-adjacent (rate 1.0).
- **The invocation bigram.** The ordered pair wosi→soreyi
  occurs adjacently in 107 of the 223 development funerary
  texts and in **10 of the 16 held-out funerary texts —
  exactly soreyi's 10 held-out texts**. No held-out
  funerary text contains soreyi without wosi (conditional
  presence: P(soreyi | wosi) = 10/12 = 0.833 on held-out
  funerary texts, P(soreyi | no wosi) = 0/4 = 0.0;
  development funerary: 0.747 against 0.195).
- **The anchor cannot pass its own test.** Scored against
  soreyi's frozen prediction shape, the registered anchor
  spelling sorey fails trivially — it has no occurrences to
  score. The anchor's corpus distribution is carried
  entirely by the spelling soreyi (with asoreyi in the same
  slot: wosi's second most frequent right neighbour, 20
  development adjacency counts).

**What remains under anchor-only.** The proposition the
Stage 4.4 adjudication actually stated — soreyi behaves,
on texts the generation never used, exactly as the corpus
spelling of the anchored Osiris theonym behaves — retains
its full support: the held-out leg is itself an
anchor-behaviour observation (10 of 10 occurrences inside
the wosi invocation, funerary-only, at the invocation's
own recurrence rate). What anchor-only removes is any
residue of support for soreyi as a lexical item
*independent* of the anchor: as generated, "theonym-adjacent
cult or offering term" names a thing adjacent to the
theonym; the anchor evidence says the form is the theonym,
in the spelling this corpus uses. The distributional
machinery's contribution was the discovery route, not
independent evidence. This is the adjudication's own cap
rationale, now measured; it adds no new downgrade reason.


**Correction note — 2026-11-22, Red Team Round 6
correction (RT6-L8).** The first bullet of this §2 as
filed joins two counts in one sentence and attaches
the wrong rate to the first of them. Split, the
record is: soreyi's wosi neighbour count is 120, an
adjacency rate of 120/137 = 0.8759 per occurrence;
soreyi's theonym-set adjacency count (neighbours in
{wos, sorey, amni, wosi}) is 121, a rate of
121/137 = 0.8832. Both underlying numbers stand; the
joining sentence as filed does not.

## 3. Genre/formula baseline

The null tested here: soreyi's held-out profile is what
any frequent element of the funerary formula would show,
because the corpus is 239/368 funerary and the funerary
text is highly stereotyped. The baseline is built from the
corpus's own structure, in three parts.

**3.1 Pool base rate.** Applying the Stage 4.3 pool
criteria corpus-wide (development frequency ≥ 10, at least
3 letters, not in the frozen vocabulary) gives 32 forms.
Every one of the 32 has a development funerary share of at
least 0.80, and 27 of the 32 are funerary-only (share
exactly 1.0): the frequent non-vocabulary stratum of this
corpus is funerary through and through. Scoring each pool
form against its own frozen-shape prediction (at least 3
held-out texts; held-out funerary share within its
development share ± 0.25, the Stage 4.4 rule):

| Pool frame | n | Pass | Rate |
|---|---|---|---|
| All pool forms | 32 | 5 | 0.156 |
| Development funerary share = 1.0 | 27 | 3 | 0.111 |
| Development occurrences ≥ 50 | 5 | 4 | 0.800 |
| Development occurrences ≥ 100 | 1 | 1 | — (soreyi alone) |

The five passers are soreyi (137 dev occ → 10 held texts),
**terikelowi** (98 → 7), **tedxelowi** (90 → 9), **xmlol**
(77 → 4), and qowi (15 → 3). The two filiation passers are
the corpus's suffixed spellings of the anchored filiation
forms: as standalone tokens, terike occurs 2 times and
tedxe 1 time on the development set (0 held-out) — the
corpus realizes those anchors in suffixed spellings,
exactly the varietas pattern of §1. At soreyi's frequency
band (≥ 50 development occurrences), passing the
frozen-shape test is the genre norm for funerary-formula
elements: 4 of 5, the one failure (yetmdelowi, 63
occurrences) missing the 3-text bar at 2 texts.

**3.2 Recurrence expectation.** soreyi's development
funerary text-presence rate is 124/223 = 0.5561, which
predicts 8.9 of the 16 held-out funerary texts under genre
recurrence alone. Observed: 10. Its partner wosi predicts
10.5 (rate 0.6547) and shows 12. The held-out count that
constitutes the PASS is the genre-recurrence expectation
to within about one text.

**3.3 Formula carriage.** soreyi's held-out occurrences
are not merely funerary; they are inside one formula: 10
of 10 sit in the ordered wosi→soreyi invocation bigram
(§2), and on the development set 120 of 137 occurrences
are wosi-adjacent. The anchored control ato "water" shows
the same shape on held-out (11 occurrences in 11 funerary
texts, none elsewhere) — the offering-formula element
recurring at its formula rate.

**What the genre/formula baseline accounts for.** The
held-out PASS, as a pass: in full. Presence count (10
against 8.9 expected), funerary share (1.0 is the pool
norm — 27 of 32 pool forms are funerary-only on
development, and every pool passer shows a held-out share
of 1.0), and stratum exclusivity are each what the
corpus's formulaic structure predicts for a high-frequency
funerary formula element. The pass therefore carries no
discriminating weight for the as-generated reading beyond
the proposition "soreyi is a high-frequency element of the
funerary formula" — which is true, and which §2 identifies
precisely: it is the Osiris element of the invocation.

## 4. Net reassessment

The two baselines converge on the same fact from opposite
sides. Anchor-only: soreyi's entire profile is the
anchor's own profile in corpus spelling, and the held-out
leg is an observation of the anchor behaving as the anchor
should. Genre/formula: the held-out PASS is genre-generic
at soreyi's frequency and is fully accounted for by the
formula's recurrence, so it adds no weight beyond the
formula-element proposition. What survives both baselines
is exactly what the Stage 4.4 adjudication recorded:
**soreyi is PARTIALLY SUPPORTED as the corpus spelling of
the anchored Osiris theonym sorey, rediscovered by the
distributional route — a real, bounded result about the
method, and not a new reading.** The standing survives;
this record executes no change to it and flags nothing for
adjudication.

One citation caution follows from §3 and is recorded for
future use of the Stage 4.4 result: soreyi's held-out PASS
must not be cited as independent distributional
corroboration of a reading distinct from the anchor-variant
fact. Cited as the variant fact, it is accurate; cited as
more, it would claim a discriminating weight the genre
baseline shows the pass does not carry.

## 5. What this record does not do

It changes no verdict, tally, score, or standing (soreyi
remains PARTIALLY SUPPORTED; the other five candidates
remain UNSUPPORTED on held-out; the affiliation question
remains UNDECIDABLE AT THIS POWER). It re-opens no seal:
the held-out partition was already opened at Stage 4.4 and
is recomputed here under the same frozen hash rule. It
registers no new claim and touches no other program's
record. The seal caveat of freeze v2 §6 travels with the
Stage 4.4 score as before.

## Amendment 2026-11-22 — Round 6 correction (RT6-M13): custody and recomputability

**Date of amendment: 2026-11-22. Authority: Red Team
Round 6, finding RT6-M13.** The audit chain of which
this record is part is not recomputable from this
repository alone. The frozen pipeline
(`pipeline-v2.py`), the ASJP CLDF files, the
inscription corpus basis, and the example phrases are
held in campaign custody on tower-compute. As this
record's own head states them, the method ran the
frozen Stage 4 pipeline "`pipeline-v2.py`, campaign
scratch, SHA-256
`74b831da221f0708b2c5a9f7e9f1a7772175fe2097783f101d33588769e1642e`"
on "the acquired Kovetsky inscription corpus (CC BY
4.0 data, `inscriptions.jsonl` SHA-256
`1e91e3a0c52626482bc4015b597df862e7818602dab48a7e870240ab2e567bc4`)",
the basis freeze v2 registers for Stages 4.2–4.4;
none of those custody bases is in this repository.
The OD-15 simulation driver in the same chain is
likewise held in custody and is not in this
repository. No verdict, tally, or standing changes.
