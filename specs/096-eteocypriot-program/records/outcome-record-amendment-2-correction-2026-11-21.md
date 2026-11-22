# Eteocypriot Program — Amendment 2 Correction Note (Red Team Round 2, RT2-11)

**Date:** 2026-11-21. **Program:** Spec 096 — Eteocypriot
Program. **Corrects:** `records/outcome-record-amendment-2-2026-11-21.md`
§4, in one sub-point. Amendment 2 is not edited; this note
governs where the two differ. Adjudication:
`RED-TEAM-ROUND-2-ADJUDICATION.md` (goal record), RT2-11.

## The correction

Amendment 2 §4 charges that two components of the E1 driver's
frozen GREEK_TO_CYPRIOT table "appear nowhere in freeze §5's
rules R1–R3": the consonant-stem table and the dead-vowel
default. The charge stands for the consonant-stem table
(β→p, γ→k, θ→t, ζ→s, φ→p, χ→k, ξ→k+s), which is indeed nowhere
in the freeze.

The dead-vowel sub-point is **withdrawn**. Freeze §5 rule R3
states, on its face, that a consonant not followed by a vowel
"maps to C plus a dead vowel copying the *preceding* vowel of
the name **(default a)**". The driver's initial
`prev_vowel = "a"` implements exactly that stated default. The
default was registered; the citation in amendment 2 §4 does
not contain what it was filed as containing.

## Provenance of the error

The overstatement originated in Red Team Round 1's finding
RT1-22 and was repeated by the Round 1 adjudication's
verification of it. It is corrected here, in the program's own
correction record, because a correction record's citations are
themselves part of the record. RT1-22's closure is not
disturbed: its registered condition was the four binding
conditions on any E1 re-run, which stand in amendment 2 §4
unchanged. Any E1 re-run registers the consonant-stem table
explicitly; the dead-vowel default needs no registration,
being already in freeze R3.
