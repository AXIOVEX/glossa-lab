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

## Round 3 note: the stem-table enumeration (RT3-19)

The enumeration of the charged consonant-stem mappings
above (β→p, γ→k, θ→t, ζ→s, φ→p, χ→k, ξ→k+s) is incomplete by
one mapping. The driver's STEMS table
(`records/eteocypriot-e1-driver.py`, lines 36–40) also
contains **δ→t**, of the same voiceless-stop class as the
listed θ→t and γ→k. The charged enumeration, completed, is:
β→p, γ→k, δ→t, θ→t, ζ→s, φ→p, χ→k, ξ→k+s. This note
completes the enumeration; the correction above (the
dead-vowel withdrawal) is unaffected, and RT2-11's closure
is not reopened.

## Round 4 clarification: what the enumeration is (RT4-10)

The Round 3 note above calls its 8-mapping list "the
charged enumeration, completed". Stated precisely: the 8
are the charged, non-obvious subset of the driver's STEMS
table, not the whole table. STEMS
(`records/eteocypriot-e1-driver.py`, lines 36–40) has 16
entries: the 8 listed, plus κ→k, λ→l, μ→m, ν→n, π→p, ρ→r,
σ→s, τ→t. And ξ→k+s is not a STEMS entry at all: it is a
special case in the driver's `letters_of` function (the
`ch == "ξ"` branch, which emits k then s). The δ→t repair
of the Round 3 note stands; only its completeness wording
is qualified by this clarification.

## Round 5 correction: the STEMS count (RT5-05)

The Round 4 clarification above states that STEMS "has 16
entries". That count is wrong, and this appended section
corrects it; the clarification's text is not rewritten.
Counted first-hand by literal evaluation of the driver
dict (`records/eteocypriot-e1-driver.py`, lines 36–40),
STEMS has **15 entries**: β, γ, δ, ζ, θ, κ, λ, μ, ν, π,
ρ, σ, τ, φ, χ. The clarification's arithmetic double-counts
ξ: its "8 listed" (β→p, γ→k, δ→t, θ→t, ζ→s, φ→p, χ→k,
ξ→k+s) include ξ→k+s, which the clarification's own next
sentence correctly places outside STEMS as a `letters_of`
special case — so the STEMS-resident subset of the 8 is 7,
and 7 + 8 (κ→k, λ→l, μ→m, ν→n, π→p, ρ→r, σ→s, τ→t) = 15.
The clarification's other arms stand: the 8 are the
charged, non-obvious subset, and ξ→k+s is not a STEMS
entry. No verdict, run or standing turns on the count; the
driver is the executed code and is untouched.
