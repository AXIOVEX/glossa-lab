# Spec 107 — Cycle 1 outcome record — 2026-11-27

Cycle 1 of the active decipherment loop, adopted
and commissioned by the owner on 2026-11-26 and
registered in `records/cycle-1-registration-2026-11-26.md`,
is complete. Three tests were registered before
execution and executed exactly as registered; no
gate was lowered and no custody term exceeded.
Progress as run: tests executed 3 of 3 (E-1, M-1,
I-1), each with its own filed progress record.

## The three verdicts, against their registered falsifiers

**E-1 (Eteocypriot) — Spec 101 executed as
registered: C101-1 NOT SUPPORTED.** The registered
falsifier was the floor rule itself: SUPPORTED
required at least one candidate at or above its
floor with Q < 0.05. Counts: -se 0 against floor
33; -na 9 against 25; -i 1 against 25; -ti 14
against 25; Q = 0.031153. Every candidate fell
below its floor, so the claim is NOT SUPPORTED.
The target is ENRICHMENT (OD-D-1); this is
expressly not a recurrence finding. Records:
Spec 101's package (intake identity record,
candidate registration, freeze addendum, scoring
outcome, outcome record of 2026-11-27).

**M-1 (Meroitic) — POSITIVE: both conformance
facts are stratum-stable.** The registered
falsifier was the genre-artifact rule: a fact
holding pooled but failing in funerary, or
holding in funerary but failing in every other
adequate-floor stratum, would have returned
NEGATIVE. Neither occurred: a-conformance holds
pooled (0.9837), in funerary (0.9837), in
royal_temple (0.9831) and in document (0.9762);
i-conformance holds pooled (0.9920), in funerary
(0.9960), in royal_temple (0.9645), in document
(0.9500) and in graffito (0.9889). Both
validation gates reproduced the filed figures
exactly before any computation. Record:
`records/m1-outcome-record-2026-11-27.md`.

**I-1 (Indus) — INDETERMINATE.** The registered
falsifier had three exits. The predictor clause
was positive for both donors at 1× (Meroitic
median RIGHT 0.7588, Latin 0.4308; each ≥ 0.05
and ≥ 2 × the larger of the WRONG and SHUFFLE
medians, which were ≤ 0.2440), so the test is not
NEGATIVE. But the positional-restriction clause
(R2) was measurable for neither donor — at the
registered 99% ground-truth definition, neither
donor's full stream contains a restricted mark
(Meroitic's strongest, the a-sign, stands at
98.4%) — and the registered rule returns
INDETERMINATE in exactly that case. Record:
`records/i1-outcome-record-2026-11-27.md`.

## Custody and integrity notes

- M-1 consumed no Otten byte (the Kovetsky build
  only); I-1's Indus inputs are the program's own
  custody datasets, read under their existing
  terms; donor B is public-domain text, pinned in
  custody before scoring.
- One integrity control fired and worked: a
  mirror fetch of donor B returned the wrong book;
  the script's identity check rejected it, the
  bytes were destroyed, and the correct edition
  (Gutenberg #218) was acquired and pinned before
  any scoring. No result rests on the bad fetch.
- E-1's commit order is on the record: intake
  (3fa7387f) → candidate registration (9dc5de7f)
  → freeze (b8c2001a) → scoring and outcome
  (be6c5f41). The candidate registration strictly
  precedes the first scoring load.

## Cycle close

The posterior trace, the kill-criteria
evaluation, and the cycle-2 re-ranking are filed
at `records/cycle-1-trace-2026-11-27.md`. No
claim standing in the canonical ledger is moved
by this cycle's records; the one verdict that
carries a possible standing change (C101-1) is
reported to the owner for adjudication under
Spec 101's registered discipline.
