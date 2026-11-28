# Spec 109 — Stage 4 outcome record (Part 5: Eteocypriot candidate ranking)

Filed 2026-11-27. Executed under registration §6
and the Stage 4 freeze
(`records/stage-4-freeze-2026-11-27.md`, SHA-256
`80ec9c9f5cdd0a3f362d1c2679277ec967f899d2fea541e3e5769d0c36d216dd`)
after the Part 5 preflight was met in full
(`records/stage-4-preflight-2026-11-27.md`). Generator:
`records/stage-4-harness.py`, SHA-256
`c9776d3e88bf86a127b8f7b863086b9dbfd386575e6dc513ddb1508210d44a53`;
run 2026-11-28T00:33:56Z, payload exit 0. Raw output:
`records/stage-4-raw-output-2026-11-27.json`,
byte-identical to the custody original at
`glossa-custody/spec109/stage-4/`.

## Verdict: RANKING NULL

Registration §6's verdict rule, applied mechanically
to the filed figures below: the top candidate's key1
(2) does not exceed the permutation null's 99th
percentile (2). The ranked set is filed; the top
rank is not distinguishable from the null at the
frozen bar. §6 states this outcome as the honest
expectation at this comparanda strength, and the
run returns it.

## The ranked candidate set (ICS 196; candidates only)

Comparanda: (a) alone — the two ICS 196 name
anchors — per the freeze's determination (the E1
derivation tables are not filed complete under
Spec 101's P-3, so comparanda (b) do not exist at
this freeze; the reduction is stated on the freeze's
face). Variant set closed: A1, A2, J. Scoring:
components (1) and (2) only; component (3) dropped
as registered; no context term (Stage 2's CHANNEL
NULL withdrew it from this study's scoring).
Ranking: lexicographic, key1 descending, then key2
descending, then variant order A1, A2, J.

| rank | variant | pairings | key1 | key2 |
|------|---------|----------|------|------|
| 1 | A1 | (5, 6) | 2 | 0.2593 (14/54) |
| 2 | J | (6, 7) | 0 | 0.3148 (17/54) |
| 3 | A2 | (6, 6) | 0 | 0.1852 (10/54) |

- **A1** (strict segment-parallel): anchored map
  {a, na, ri, si, to}; implied endings
  {[na], [no, se]}. Its lead is key1 alone: the
  ending [na] is a suffix of two of the eight
  held-out forms (e-ne-mi-na; pu-e-ne-mi-na), the
  only held-out matches any candidate scores.
- **J** (joint one-to-one): anchored map
  {a, ka, na, ri, si, to} — the widest map, and the
  highest key2 (17 of 54 development tokens covered)
  — with implied endings {[no, se], [so, ko, o, se]},
  neither a suffix of any held-out form, so key1 0.
  What separates rank 2 from rank 1 is exactly the
  registered priority of key1 over key2.
- **A2** (name-anchored free): anchored map
  {a, ri, si, to}; implied endings {[no, se]};
  key1 0, key2 lowest. It trails on both keys.

No sign carries conflicting values under any
variant; the conflicts-excluded lists are empty in
all three candidate records. Full candidate records
with generation provenance (generator, corpus,
driver, and freeze pins; null seed; constraint-set
version) are in custody at
`glossa-custody/spec109/stage-4/candidate-records.jsonl`
and are reproduced in the raw output.

## The permutation null

B = 999 permutations of the filed 35-mark
development inventory (Spec 105's L1 derivation over
the pinned corpus and intake, the restored sign
'[sa]' standing as a mark in its own right as
filed), seed 109401, applied to each candidate's
anchored map and implied endings; statistic: the
maximum key1 over the three variants.
Distribution of the null maximum:
{0: 888, 1: 3, 2: 107, 4: 1}; mean 0.221;
99th percentile **2**. Observed top key1 **2**.
2 does not exceed 2: the top rank does not
separate. One permutation in 999 reaches a maximum
of 4, above the observed top outright.

The margin structure is therefore stated plainly:
the observed lead (key1 2 against 0 and 0) sits
inside the range the null produces from the same
candidate machinery with its labels permuted —
107 of 999 permutations tie it. At comparanda (a)
alone, the ranking machinery returns an ordering,
and the ordering carries no separation from chance
at the frozen bar. That is the finding.

## Terms of this filing

The three candidates are filed as candidates: a
ranked set with margins and full generation
provenance, nothing more. No candidate is a reading
of any text, and no statement in this stage's
records presents one as such. No standing, verdict,
anchor, or tally in any program moves. Part 5's
outcome is filed under registration §6's own terms;
any future ranking under richer comparanda would
require a new freeze and a new preflight under the
registration's discipline, and is not part of this
stage.
