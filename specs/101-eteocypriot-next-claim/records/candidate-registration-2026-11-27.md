# Spec 101 — Candidate registration (T201) — 2026-11-27

Registered under Spec 107 cycle 1 (the owner's
commission of 2026-11-26), before any scoring load of
the Perna-side state. This commit strictly precedes
the first scoring run (TC-101-02).

## Derivation

The candidate set was derived mechanically from the
ICS 196 development set alone, by the rule of
spec.md §3.1 P-2 (a sign sequence recurring at
segment-final position in at least two development
segments), by `records/candidate-derivation.py` over
the Spec 096 corpus file (SHA-256 `2954283d…`,
version 1.1.1). The script opens no Perna-side file.
Full output: `records/candidate-derivation-output.json`.

- Development segments D = 11 (ICS 196, 2 lines,
  segments numbered 1–11 in flattened order).
- Recurring segment-final suffixes (f ≥ 2): exactly
  4, all of length 1. No suffix of length ≥ 2
  recurs. The candidate set is therefore exactly
  the set derived in the floor record's §2, and
  K = 4 respects the registered cap K ≤ 4.

## The registered candidate set

| Candidate | Signs | f_i | Development occurrences (segments) |
|---|---|---|---|
| -se | [se] | 3 | 6, 7, 8 |
| -na | [na] | 2 | 1, 5 |
| -i | [i] | 2 | 3, 4 |
| -ti | [ti] | 2 | 9, 11 |

## Predicted positions

Each candidate predicts occurrences at the
segment-final positions of the Perna-side census
(the position kind registered in the floor record
§1.2). The census of record is the state intaken at
T101 (`records/intake-identity-record-2026-11-27.md`):
M = 84 segment-final positions.

## What this registration does not do

It sets no floor. Floors are computed at the freeze
(T202) by the floor record's §1.3 formula from the
inputs registered here (f_i, D = 11, K = 4) and the
census's M. It scores nothing: no count of any
candidate in the Perna-side state has been taken at
the time of this commit, by this actor or, to the
record's knowledge, any other.
