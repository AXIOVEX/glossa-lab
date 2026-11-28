# Spec 109 — Stage 4 preflight record (Part 5: Eteocypriot candidate ranking)

Filed 2026-11-27. Stage 4 of Spec 109, executed under
registration §6 and the Stage 4 freeze
(`records/stage-4-freeze-2026-11-27.md`, SHA-256
`80ec9c9f5cdd0a3f362d1c2679277ec967f899d2fea541e3e5769d0c36d216dd`,
committed before any computation). Generator:
`records/stage-4-harness.py`, SHA-256
`c9776d3e88bf86a127b8f7b863086b9dbfd386575e6dc513ddb1508210d44a53`.
Data pins as in the freeze §7; both pins verified
fail-closed by the harness before any clause ran.

Part 5's conformance preflight (registration §2 as
particularized by freeze §5) has two clauses. §2's
clauses (ii) and (iii) are disposed of on the freeze's
face: the generator has no margin form (its scoring
is the lexicographic pair of freeze §6, whose null
separation is the verdict rule of the ranking itself,
not a preflight clause), and it has no R1 predictor
form (the known-truth control is clause N below). The
positional-recovery limitation of §2 is restated:
this generator recovers no positional classes, and no
positional clause is stated for it.

## Clause N — filed-anchor reproduction: MET

The harness, run against the pinned corpus alone,
reproduces the filed anchor facts exactly (9 of 9
checks):

- derived spellings: D(Ἀρίστωνα) =
  [a, ri, si, to, na]; D(Ἀριστώνακτος) =
  [a, ri, si, to, na, ka, to, so], under the freeze's
  derivation tables;
- LCCS(name 1, segment 6) = 4; LCCS(name 2,
  segment 6) = 4; LCCS(name 2, segment 7) = 2;
- pairings: A1 (5, 6); A2 (6, 6); J (6, 7); joint
  LCCS sum 6, Spec 104's certified optimum.

Any mismatch would have stopped the run before any
ranking. None occurred.

## Clause S — synthetic recovery: MET

Five synthetic corpora (seeds `spec109-s4-synth-1`
through `spec109-s4-synth-5`; each admitted on its
first construction attempt, no rebuilds), each built
to the freeze §5 profile: a 35-sign syllabary pool;
11 segments at the real skeleton lengths
[2, 3, 5, 4, 3, 6, 9, 7, 7, 2, 5] (53 tokens,
25 distinct marks in stream, 15 singletons, as
constructed and filed per corpus in custody); a
planted instance mirroring the real alignment shape
(LCCS 4 / 4 / 2, pairings (6, 7) under J); every
planted anchored sign carrying at least 5 tokens;
8 planted held-out forms (3 / 2 / 2 / 1 across the
planted finals).

Per replication, the generator's top-ranked
candidate is J in all five; recovery of the planted
anchored signs by the top candidate's map:

| rep | top | recovery | shuffle top | shuffle recovery |
|-----|-----|----------|-------------|------------------|
| 1 | J | 1.000 | A1 | 0.167 |
| 2 | J | 1.000 | A1 | 0.000 |
| 3 | J | 1.000 | A1 | 0.167 |
| 4 | J | 1.000 | A1 | 0.167 |
| 5 | J | 1.000 | A2 | 0.167 |

Median recovery **1.000**, at or above the frozen
floor of 0.80. Shuffle control (planted derived
spellings deranged per corpus): median recovery
**0.167**, below 0.5 × 1.000 = 0.500 as required.
The generator recovers the planted instance's
anchored map in full on every replication, and the
deranged-label control does not.

## Disclosure — the first execution's stop

A first execution of the harness (2026-11-28T00:33:06Z)
met clauses N and S exactly as filed above, then
stopped at the harness's own fail-closed inventory
assertion before any ranking ran: payload exit 1.
The harness had recomputed the development inventory
for the permutation null with editorial brackets
stripped, yielding 34 marks, against the freeze's
35. The filed inventory governs: Spec 105's L1
derivation files the 35-mark list over these same
two pinned files with the restored sign '[sa]' and
'sa' as separate marks (69 tokens), and the freeze's
§6 fixes the permutation domain as that filed
inventory. The harness was corrected to build the
inventory from the tokens as recorded; the run was
then re-executed whole, and every figure in this
stage's records comes from the second execution
(2026-11-28T00:33:56Z, payload exit 0). '[sa]' occurs
in no anchored map and no implied ending; it enters
the null only as a member of the permutation domain,
as filed. No floor, seed, or rule was changed.

## Result

Both preflight clauses are met at the frozen floors.
The ranking proceeded under registration §6 and the
freeze, on the registration's own terms. The
preflight produced no output on any undeciphered
material beyond the anchor facts clause N
reproduces, which are the filed facts of Specs 096
and 104.
