# Spec 107 cycle 1 — M-1 run and outcome record — 2026-11-27

Test M-1 (Meroitic): stratum-conditioned
recomputation, executed as registered in
`records/cycle-1-registration-2026-11-26.md` §3 by
`records/m1-execution.py` on tower-compute,
against the Kovetsky build only (SHA-256
`1e91e3a0…`). The Otten corpus is not an input;
no Otten byte was consumed. Raw output:
`records/m1-raw-output.json`, including the full
per-mark positional table per stratum.

## Validation gates (both STOP-gates passed)

- Population S pooled figures reproduce the filed
  sandbox figures exactly: 24,648 adjacencies; 448
  distinct pairs; top pair (t, e) at 1,352; a: 737
  occurrences, 725 initial-or-sole; i: 2,880
  occurrences, 2,857 neither-initial-nor-sole;
  digits 0, 5, 6, 8, 9 never have a successor;
  digit 8 has no neighbour.
- Population P partition reproduces the campaign's
  filed counts exactly: development 335 (funerary
  223, royal_temple 41, document 42, graffito 22,
  other 7); held out 33 (funerary 16, royal_temple
  10, document 5, graffito 2, other 0).

## The two verdict-bearing facts, per stratum (Population S)

Rate = conformance; a fact holds where the rate
≥ 0.95 in a stratum with ≥ 30 occurrences of the
mark. Strata below the floor are description only.

**a-conformance** (initial-or-sole / total):
pooled 725/737 = 0.9837. Funerary 602/612 =
0.9837; royal_temple 58/59 = 0.9831; document
41/42 = 0.9762 — holds in every adequate-floor
stratum. Graffito 21/21 and other 3/3 are below
the occurrence floor (description: both 1.0000).

**i-conformance** (neither-initial-nor-sole /
total): pooled 2857/2880 = 0.9920. Funerary
2494/2504 = 0.9960; royal_temple 190/197 =
0.9645; document 76/80 = 0.9500; graffito 89/90 =
0.9889 — holds in every adequate-floor stratum.
Other 8/9 is below the floor (description).

Neither fact is a genre artifact under the
registered definition (no fact holds pooled but
fails in funerary; none holds in funerary but
fails in every other adequate-floor stratum).

## Out-of-stratum prediction (Population P, development arm)

Funerary rates predict royal_temple rates closely:
a-conformance 0.9855 (funerary) vs 0.9778
(royal_temple), difference 0.0077; i-conformance
0.9957 vs 0.9528, difference 0.0429. Description;
no verdict weight.

## Description-level pooling flag

The pooled never-successor digit class {0, 5, 6,
8, 9} appears complete in no large stratum: it is
complete in document (402 groups) and absent as a
class in funerary, where every digit has a
successor somewhere. The pooled statement "digits
never have a successor" is therefore a property
of the pooled corpus driven by the non-funerary
strata, and later records should cite it with its
stratum basis. This flag is description-level; it
does not touch the two verdict-bearing facts,
whose strata all hold.

## Verdict (registered rule)

**M-1: POSITIVE — both conformance facts are
stratum-stable.**

## What this does to the Meroitic line (design's per-outcome table)

The corpus-wide positional statistics behind
MER-2 and MER-3 are converted from pooled claims
into controlled ones: the a-sign and i-sign
restrictions hold within the funerary stratum
itself and in every other stratum with enough
occurrences to judge, so they are not funerary-
genre artifacts and not pooling artifacts. The
practical scope of MER-2/MER-3 is unchanged and
now stratum-backed. M-2 (stratum-first re-derivation
of the L4 classes) proceeds in cycle 2 on a
validated basis. No standing, verdict, or tally
of any earlier study is moved by this record.
