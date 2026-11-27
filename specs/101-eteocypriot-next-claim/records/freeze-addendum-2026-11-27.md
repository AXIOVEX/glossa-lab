# Spec 101 — Freeze addendum (T202) — 2026-11-27

Filed under Spec 107 cycle 1, after the candidate
registration commit and before any scoring. The
floors below are computed, never chosen: the floor
record's §1.3 formula applied mechanically by
`records/freeze-computation.py` to the
T201-registered inputs and the intaken census's M.
Full machine output:
`records/freeze-computation-output.json`.

## Complete tables the scoring run uses (P-3)

This scoring uses no E1 driver machinery. The
candidates and the Perna-side state share the
standard transliteration, and the only tables the
scoring run (T301) uses are the three stated here
in full. No other table is used; a scoring run
using an unstated table falsifies C101-3.

**Table 1 — the candidate set** (from
`records/candidate-registration-2026-11-27.md`):

| Candidate | Signs | f_i | Development occurrences (ICS 196 segments) |
|---|---|---|---|
| -se | [se] | 3 | 6, 7, 8 |
| -na | [na] | 2 | 1, 5 |
| -i | [i] | 2 | 3, 4 |
| -ti | [ti] | 2 | 9, 11 |

D = 11 development segments; K = 4.

**Table 2 — the segment-final position
definition.** A segment-final position is the last
sign position of a segment of the intaken census,
where segments are delimited exactly as intaken
(boundaries at the printed separators `|`, `//`,
`:` and the printed corner mark; `_` not a
boundary). The census carries M = 84 segment-final
positions (ICS 194: 33; ICS 195: 51). The one
segment of kind `numeral` contributes its final
position to M like every segment.

**Table 3 — the final-sign extraction rule.** A
candidate's Perna-side count is the number of
segments of the intaken state whose final sign's
label equals the candidate's sign label exactly
(`se`, `na`, `i`, `ti`). The unread marker `•` is
no candidate's final sign. The numeral segment's
final label `I` (capital) is not the syllabic
label `i`. Changed-reading flags do not alter a
sign's label. No other extraction is performed.

## Floors (§1.3 applied; M = 84, per-candidate α = 0.05/4 = 0.0125)

| Candidate | p_i = f_i/11 | E_i = 84·p_i | F_i | q_i = P(X ≥ F_i) |
|---|---|---|---|---|
| -se | 0.272727 | 22.909 | **33** | 0.011213 |
| -na | 0.181818 | 15.273 | **25** | 0.006647 |
| -i | 0.181818 | 15.273 | **25** | 0.006647 |
| -ti | 0.181818 | 15.273 | **25** | 0.006647 |

Family-wise Q = Σ q_i = **0.031153 < 0.05**. The
freeze is not defective under §1.4 and the study
proceeds to scoring.

## Instantiation check and the TOO THIN path (floor record §3; TC-101-06)

Every registered candidate predicts segment-final
positions; the census carries 84 instances of that
kind, so all four candidates instantiate and no
TOO THIN closure arises for a registered
candidate.

The closure path was exercised, not merely read:
the freeze computation also ran a procedure probe
(a candidate predicting reverse-face segment-final
positions, a position kind of which the census
carries no instance). The checker returned
UNINSTANTIABLE for the probe, which is the
condition under which the study would close TOO
THIN at its freeze with C101-1 NOT TESTED. The
probe is a procedure exercise, not a candidate of
the study; the closure obligation attaches to
registered candidates, none of which triggered it.
The probe and its result are in
`records/freeze-computation-output.json`.

## Verdict rule carried forward (§1.5)

C101-1 is SUPPORTED (at postdictive strength) if
and only if at least one candidate's Perna-side
count is ≥ its floor F_i above, with Q < 0.05 as
frozen. It is NOT SUPPORTED if every candidate's
count is below its floor or the candidate is
absent. The declared target of this test is
ENRICHMENT (OD-D-1); a NOT SUPPORTED outcome is
expressly not a recurrence finding.
