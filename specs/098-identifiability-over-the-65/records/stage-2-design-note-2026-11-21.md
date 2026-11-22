# Spec 098 — Stage 2 Design Note: the Bar Arithmetic and Per-Sign Eligibility

**Date: 2026-11-21. Filed under Red Team Round 1, finding
RT1-17, adjudicated APPLY WITH MODIFICATION on 2026-11-21.
Stage 1 executed 2026-11-21 (PRs #639–#641). No Stage 2 is
commissioned by this note; it fixes what any Stage 2 freeze
must answer on its face.**

## Where Stage 1 left the population

T101 found **no genuine holdout exists**: both sequence
sources are the candidate-generation inputs, so every sign's
ceiling is **DISCRIMINATED ON PSEUDO-HELD-OUT**. The amended
population is **70 signs; 21 of 70 meet the 5-token floor**;
UNDECIDABLE is the expected majority outcome.

## The bar arithmetic, stated

The registered bar is a 10-nat advantage over the best
rival, with a 2-nat flexibility penalty — 12 nats in total —
scored over a sign's held-out tokens. At the 5-token floor,
that is an average advantage of **≈2.4 nats per held-out
token** over the best rival, sustained across every token
the sign has. The bar does not scale down for signs with
fewer tokens; for a sign at the floor it is at its most
demanding per token. Any Stage 2 design that does not reckon
with this arithmetic on its face will return UNDECIDABLE for
the floor population by construction, and should say so in
advance rather than discover it in the outcome record.

## What a Stage 2 freeze must state

1. The bar arithmetic above, answered on the freeze's face:
   either the bar stands with the ≈2.4 nats/token consequence
   acknowledged, or the bar is re-registered with its reasons
   — before any scoring.
2. **Per-sign eligibility by count**: for each of the 70
   signs, its held-out token count and its resulting
   eligibility, stated in the freeze — not computed for the
   first time in the outcome record.
3. The ceiling, carried verbatim: every result is
   DISCRIMINATED ON PSEUDO-HELD-OUT at best, because no
   genuine holdout exists (T101).

**AI disclosure:** executed by an AI agent (Muse, via Muse)
at the direction of Tristen Pierson, per constitution sec. VI.

**Correction pointer (2026-11-21, Red Team Round 2 — RT2-03):**
this note's bar arithmetic is corrected by
`records/stage-2-design-note-correction-2026-11-21.md`: the
penalty is 2 nats per free choice (not a flat 12 nats in
total), the permutation-null 99th-percentile conjunct is part
of the frozen bar, and the floor figure is 21 of 70 **in
expectation**. The population is 69 since the M044 act of the
same date.

**F-9 pointer (2026-11-22):** the population is 68 since
the F-9 act of this date: M047 was reclassed from E to U
under the itemization test the owner adopted
(`specs/091-anchor-comparison-integrity/records/f9-itemization-adjudication-2026-11-22.md`).
The Stage 1 figures in this note stand as executed at the
populations they state.

**M048 pointer (2026-11-22):** the population for future
stages is 69 since the M048 re-adjudication of this date:
M048 was reclassed from U to I on its filed
corrected-battery result (score 2, the threshold RT2-08
named), so the population is the 66 class I readings plus
the 3 class E readings
(`specs/091-anchor-comparison-integrity/records/m048-readjudication-2026-11-22.md`).
The count matches the Stage 2 executed population by
coincidence of number only: Stage 2 executed over 65 I +
4 E, with M047 in the E arm and M048 outside the
population, and the Stage 1 and Stage 2 figures in this
note stand as executed at the populations they state. No
stage is commissioned by this pointer.
