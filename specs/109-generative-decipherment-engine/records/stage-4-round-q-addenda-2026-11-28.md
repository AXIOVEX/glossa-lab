# Spec 109 Stage 4 — Round Q addenda (2026-11-28)

Filed under Round Q of the Co-scientist loop, ledger rows
Q-E-1 and Q-E-3 (adjudication
`specs/091-anchor-comparison-integrity/records/coscientist-sweep-adjudication-2026-11-28-round-q.md`
§2). The original Stage 4 code, freeze, preflight, outcome,
and close records are preserved unedited. No standing,
verdict, or tally changes on this record, and no corrected
control experiment is commissioned by it.

## (a) Q-E-1 conformance addendum — the derangement construction defect

The Stage 4 freeze (§6) specifies a fixed derangement per
corpus, and the preflight describes the derived spellings as
deranged. The executed construction does not deliver that
property. In `stage-4-harness.py` (clause S), the label list
is shuffled and then rotated once if any fixed point exists;
that operation does not guarantee removal of fixed points,
and no final check is performed. The verifier
(`stage-4-verify.py`) repeats the same construction in its
clause-S reconstruction, so verifier agreement verifies
reproducibility of the reported figures, not the missing
property — a shared verifier gap.

Reconstruction of the actual seeded mappings gives:

| Replication | Fixed points after the fallback | In the planted anchored set? |
|---|---|---|
| 1 | lo, so | so is in the planted derived spellings / anchored set |
| 2 | none | — |
| 3 | none | — |
| 4 | o, ma, mi | none |
| 5 | re | none |

Three of the five shuffle controls (replications 1, 4, and
5) are therefore not the registered derangements, and
replication 1 leaves an active planted anchored label
unchanged.

**Qualification, of record.** Reliance on "preflight met in
full" is replaced by: **numerical floors met on the executed
controls; the registered derangement construction not met.**
This is a control-conformance defect, not proof that a
correctly deranged control would fail the recovery
threshold. The observed recoveries, the shuffle median, and
the RANKING NULL arithmetic are expressly preserved: the
session's independent reproduction of the full permutation
null distribution (0: 888, 1: 3, 2: 107, 4: 1 over 999
permutations; 99th percentile 2; observed top score 2)
confirms RANKING NULL as arithmetically correct on the
filed figures.

**Referred, not decided.** The disposition of the clause-S /
full-conformance labels and any license consequence is
referred to the owner and recorded here as referred. No
automatic continuation-license or standing change follows
from this addendum.

## (b) Q-E-3 skeleton correction — "real skeleton" lengths and fixture scope

The freeze (§6) and preflight call
[2,3,5,4,3,6,9,7,7,2,5] the "real skeleton lengths". Against
the pinned ICS 196 ranking input that is wrong, and is
corrected of record:

| | Segment lengths | Total |
|---|---|---|
| Filed "real skeleton" | [2,3,5,4,3,6,9,7,7,2,5] | 53 |
| Actual ranking input | [2,3,5,4,3,6,10,7,7,2,5] | 54 |

Segment 7 has ten signs, not nine.

Two scope corrections ride with it. First, pool versus
realized types: the synthetic construction's 35-label
sampling pool is not 35 realized types (each synthetic
stream realizes 25 types, 15 of them singletons, as the
preflight itself reports); the broader 35-label development
inventory is a different object from the real ICS 196 core
census and must not be substituted for it. Second, fixture
isomorphism: the five fixtures are structurally isomorphic
under consistent label renaming across segments, derived
spellings, and test forms — five label realizations of one
construction, not five distinct structural difficulties —
and each deliberately makes its planted anchored signs
measurable at the ≥5-token floor, which no sign in the
54-token real core reaches.

**Description, of record.** The five 1.000 synthetic
recoveries stand as filed, described as a **planted
implementation control**: they demonstrate recovery of the
planted alignment and ending structure on the constructed
fixtures, not detection power at real-corpus sparsity and
not recovery of an unknown language. No revised fixtures,
power estimate, or additional study is commissioned by this
correction.
