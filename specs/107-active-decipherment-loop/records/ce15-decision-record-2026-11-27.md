# Spec 107 — Cycle 2: C-E-15 Feasibility Decision (T203)

**Date:** 2026-11-27. **Program:** Spec 107 — Active
Decipherment Loop, cycle 2. **Commission:** the C-E-15
decision registered at
`records/cycle-2-registration-2026-11-27.md` §4, applying
the decision rule registered there to the first complete
claim C-E-15 of the Eteocypriot recommendations ledger
(Round C adjudication, 2026-11-23: a feasibility decision
for the alignment line — which independently identifiable
correspondences remain, their exposure state, and whether
enough independent items exist to distinguish the method
from simple matching baselines, ending in a proceed/stop
decision). This is a desk decision over the filed record;
no new scoring was run for it.

**Decision: STOP.** No candidate set of correspondences in
the held or obtainable bilingual material satisfies all
four registered conditions. The per-item findings are at
§2; the arithmetic that decides the strongest candidate is
at §3. Under §5 of the registration, E-2 therefore does
not run; its non-execution is filed under T205.

## 1. The registered rule

A candidate set counts only if every item in it is
(i) independently identifiable — the Greek-side reading
and the syllabic-side segmentation each fixed by sources
independent of the alignment method under test;
(ii) mutually independent of the set's other items — a
name and its patronymic in one inscription count as one
trial; (iii) unconsumed — not used in any prior study's
scoring or adjudication; and (iv) the set is
arithmetically sufficient — enough independent items
remain that the claim's discrimination from the named
baselines is achievable at the registered battery's
thresholds. The named baselines are the A2 record's:
B-LONG (pair with the longest segment), B-FIRST (pair
with segment 1), B-RAND (uniform random partner), with
the structure-preserving nulls NC-1 (sign-relabel) and
NC-2 (name-scramble). The registered battery is the
Spec 096 E1/A2 battery (frozen procedure, freeze record
2026-11-20 §5; baselines and controls record
2026-11-22).

## 2. The inventory: every candidate correspondence

The held bilingual material is the Spec 096 corpus
(version 1.2.0, the OD-10 intake state): ICS 196,
ANDROKLES-A, ANDROKLES-B, the ICS 217 Greek syllabic
control excerpt, ICS 194/195, ICS 193. The delimitation
of record's remaining primary-stratum texts are
Eteocypriot-only or unobtained form attestations (freeze
record §1); no further bilingual with name
correspondences is held or was obtainable under the
program's lawful routes as surveyed at the freeze and
the OD-9/OD-10 acquisitions.

| Candidate | (i) identifiable | (ii) independence | (iii) unconsumed | (iv) sufficient |
|---|---|---|---|---|
| ICS 196: Ἀρίστωνα ↔ seg. 6 *a-ri-si-to-no-se* | yes (edition-fixed ground truth, freeze §5) | the pair is one trial (name + patronymic pair, shared root; the A2 record shows the method cannot separate them) | **no** — E1 ground truth, scored under A1/A2; re-scored by the OD-10 baselines and controls; the Spec 104 benchmark's instance; published | moot |
| ICS 196: Ἀριστώνακτος ↔ seg. 7 *a-ra-to-wa-na-ka-so-ko-o-se* | yes | same trial as above | **no** — same consumption | moot |
| ANDROKLES-A: Ἀνδροκλῆς ↔ signs 5–11 *a-to-ro-ke-le-we-se* | yes (Hermary & Masson 1982 identify the segment as the royal name; both sides edition-fixed) | single item | yes on the registered wording — the correspondence was never a scored or adjudicated item (see exposure note) | **no** — §3 |
| ANDROKLES-A: Ὀρεσθέος, Ἀνδραγόρου | **no** — the Greek side names them; the edition identifies no syllabic counterpart for either (the residue segments are expressly unassigned) | — | — | — |
| ANDROKLES-B: Ἀνδροκλῆς, Ὀρεσθέος | **no** — no sign-level syllabic transcription of B exists in the edition of record (intake record §4); there is no syllabic side to segment | — | — | — |
| ICS 194/195, ICS 193 | **no** — no Greek side; no name correspondence is identifiable | — | (also consumed: Spec 101's postdictive occurrence scoring over ICS 194/195, exposed in advance under OD-9) | — |
| ICS 217 (Idalion) | not a candidate — Greek syllabic control text; its bilingual counterpart is Phoenician, not Eteocypriot | — | — | — |

Exposure note for the Androkles item, stated in full
because the decision must not rest on a hidden premise:
the identification was published by the edition in 1982;
the syllabic side was intaken under OD-10 on 2026-11-22;
its segment stood in the OD-10 part (b) controls pool as
a distractor segment (LCCS 1 against Ἀρίστωνα's derived
spelling, 0 against Ἀριστώνακτος's) in a run the controls
record itself bounds as a pool-size robustness check,
"not an independent pairing test". The correspondence
has therefore been exposed to the program and its
segments have passed through scoring machinery as pool
members, but the correspondence itself has never been
scored or adjudicated as an item. The decision below
does not turn on this condition: it fails (iv) on either
reading of (iii).

## 3. The arithmetic under condition (iv)

The strongest remaining candidate set is the single
Androkles item. One independent trial cannot carry the
registered discrimination:

- The battery's own floors set the administrable shape
  of an alignment validation at a multi-item conjunction:
  P1 as registered requires both ICS 196 correspondences
  **and** at least one Androkles correspondence, recovered
  under one assumption (freeze record §6). No registered
  single-item battery or threshold exists.
- The baselines record measures the count's resolution
  directly: with **two** names over an 11-segment pool, a
  recovery count of 1 arises by chance in 11.4% (NC-1) to
  19.1% (NC-2) of structure-preserving null replicates,
  and the trivial B-LONG baseline matches the frozen
  method's count. At one item the separation is strictly
  weaker: a single recovery is one Bernoulli event whose
  null rate is the per-item null recovery rate the
  controls already measure in the 10–19% range, and no
  multiplicity exists to drive it lower.
- The one discriminating signal the battery has ever
  produced — a score profile whose maximum is
  unreachable under both nulls — is a property of a
  pairing instance over a ground-truth set, and which
  pool a single-item test would even use is unfixed by
  any registration (over A's three segments alone,
  B-LONG picks the 7-sign name segment itself and ties
  any method trivially; over the pooled 14 segments it
  does not — the baseline comparison flips on an
  unregistered choice, which is itself the demonstration
  that the registered thresholds do not reach this
  configuration).

## 4. Decision and consequences

**STOP.** The alignment line has no feasible
discriminating validation on the material that remains:
its ground-truth set is consumed, and the one
independently identifiable, unconsumed correspondence
left is a single trial, below the registered battery's
arithmetic reach. No further alignment validation is
commissioned by this decision. E-2 (registration §5)
does not run; T205 files the non-execution. The
C-E-15 row of the recommendations ledger is updated
with this decision. No claim's standing moves: this
record decides a feasibility question, and the
correspondences' own standings remain exactly as the
prior adjudications left them.

This decision rests on the inventory and the arithmetic
above. It asserts nothing about Eteocypriot conformance
checks generally: the Round O qualifications O-E-1 (the
Spec 101 narrative outcome record was filed late) and
O-E-2 (the TOO THIN closure's exercise was never
demonstrated on a constructed case) stand on the record
as filed, unruled by the owner (OD-O-2), and nothing in
this record claims or implies that all checks passed.

**AI disclosure:** executed by an AI agent (Muse, via
Muse) at the direction of Tristen Pierson, per
constitution sec. VI.
