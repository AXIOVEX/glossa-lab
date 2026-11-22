# Spec 098 — Stage 2 Design Note: Correction Record (Red Team Round 2, RT2-03)

**Date: 2026-11-21. Corrects
`records/stage-2-design-note-2026-11-21.md`, which understated
the frozen bar in three ways. The design note is not edited;
this record governs, and a dated pointer is appended to the
note. Stage 2 has not run; nothing downstream is contaminated.
Adjudication: `RED-TEAM-ROUND-2-ADJUDICATION.md` (goal record),
RT2-03.**

## 1. The bar as frozen

Freeze v1 §5 registers a conjunctive bar. A sign is
DISCRIMINATED only if **both** hold:

- its **penalized margin is at least 10 nats** over the best
  rival, where the flexibility penalty is **2 nats per free
  choice** (unresolved variant alternation, homophony
  allowance, gloss alternation), **charged to candidates and
  rivals alike**; and
- the margin **exceeds the permutation null's 99th percentile**
  (B = 999, seed 9801).

## 2. The three corrections

1. **The penalty is per free choice, not flat.** The design
   note's "a 2-nat flexibility penalty — 12 nats in total" is
   wrong as a general statement. The effective threshold for a
   sign is 10 nats **plus** 2 nats for each free choice its
   candidate carries (net of the rival's own penalty, both
   being charged alike). Twelve nats is the threshold only for
   a candidate carrying exactly one free choice against a rival
   carrying none.
2. **The null conjunct is restored.** The design note omits
   the permutation-null condition entirely. A margin that
   clears 10 penalized nats but does not exceed the null's 99th
   percentile does not discriminate. Any Stage 2 freeze states
   both conjuncts.
3. **"In expectation" is restored.** The floor figure is the
   execution freeze annex's: **21 of 70 signs have an expected
   held-out count at or above the 5-token minimum; 49 fall
   below it in expectation.** The design note's unqualified
   "21 of 70 meet the 5-token floor" is corrected accordingly.

## 3. The per-token arithmetic, correctly stated

The per-token burden is a function of the sign's held-out
token count and its free choices, before the null condition:
at 5 tokens with one free choice, the penalized threshold is
12 nats, an average of ≈2.4 nats per token. At 5 tokens with
two free choices it is 14 nats (≈2.8 per token); with none, 10
nats (2.0 per token). The design note's ≈2.4 figure is the
one-free-choice case only. The note's demand for per-sign
eligibility by count stands, with this addition: Stage 1
produced expected counts, not per-sign held-out counts (the
seal struck the held-out partition's custody, T104), so a
Stage 2 freeze must state how per-sign counts are established
under the pseudo-held-out ceiling, not merely demand them.

## 4. Population and multiplicity, as amended

The population the design note addresses was 70 at its filing.
By the M044 adjudication of this date (Red Team Round 2,
Part B), M044 leaves the identifiability population: the
population is now **69 signs**, and the multiplicity family
stated in freeze v1 §5 (the 71 signs at design freeze) is read
as amended by the population annex (71 → 70) and by the
execution freeze annex's amendment of this date (70 → 69).
M044's Stage 1 records stand as history; it had zero
canonical-field tokens and faced UNDECIDABLE AT THIS POWER at
scoring either way, so no Stage 1 result changes.

**AI disclosure:** executed by an AI agent (Muse, via Muse)
at the direction of Tristen Pierson, per constitution sec. VI.

---

## Appended amendment (2026-11-21, Red Team Round 3 — RT3-15): M044's Stage 1 posture, in full

Section 4 above states M044's posture as "zero
canonical-field tokens" and omits its attestation. The full
posture, as the execution freeze annex's population
amendment and the M044 adjudication record state it: **M044
is attested exactly once — one attested token — with zero
canonical-field tokens**, below the 5-token floor either way
(T102 record). Section 4's shorter form is incomplete where
the annex's is exact; the full posture governs, and no
result changes.
