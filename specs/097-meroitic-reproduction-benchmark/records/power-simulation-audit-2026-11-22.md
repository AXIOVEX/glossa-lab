# Meroitic Decipherment Campaign — Power and Simulation Audit of the Stage 4.2 Affiliation Test (Spec 097, OD-15)

**Date: 2026-11-22. Commission: OD-15 of the Co-scientist
refresh adjudication (Spec 091 record), commissioned by the
owner 2026-11-22 13:18 ET. Venue: tower-compute. This audit
measures the operating characteristics of the affiliation
test as frozen in freeze v2 and executed in Stage 4.2
(claim C097-9). It changes no verdict, no standing, and no
Stage 4 number. Companion: `power-simulation-audit-2026-11-22.json`
(every number below, machine-readable).**

## 1. Validation before simulation

No simulation result in this record was produced until the
frozen machinery reproduced the executed outputs.

- The frozen pipeline (`pipeline-v2.py`, the program's own
  campaign code, held in the campaign scratch on
  tower-compute) was re-run in its `stage42` mode on
  2026-11-22. Its output is **byte-identical** to the landed
  `records/stage-4-2-results.json` (verified by `cmp`):
  R1 vocabulary test S = 4 of 12, p = 0.0326; R2 vocabulary
  test S = 1 of 12, p = 0.824; phonotactic rate 0.3152 over
  13,406 pairs, shuffle p = 0.474; formative leg 5, pass.
- The ASJP input files in custody match freeze v2 §4's
  registered SHA-256 pins exactly (forms.csv `4ee30b77…`,
  languages.csv `647174df…`, parameters.csv `2ed306c2…`).
- All audit computation imported the frozen pipeline
  unchanged (its scoring rule, vocabulary builder, and
  comparator sets); no component was reimplemented. The
  permutation counts above the frozen 10,000 and the
  injection simulations of §4 are extensions, labelled as
  such wherever they appear.
- Freeze v3 check: the v2 and v3 vocabulary companions
  carry **identical form counts for every one of the 12
  scored concepts** (the 182 → 179 cleanup removed only
  concept-less forms), so this audit of the executed v2
  design describes the v3 design's scored test unchanged.

## 2. The null behaviour of S

Under the frozen permutation design (comparator forms
shuffled across concepts, per-concept counts preserved),
extended from the frozen 10,000 permutations to 100,000 for
tail precision (the frozen 10,000-permutation run reproduces
the executed p-values exactly: 0.0326 and 0.824):

| | R1 (Nubian + Nara) | R2 (Afroasiatic) |
|---|---|---|
| mean S under the null | 1.506 | 1.397 |
| per-concept chance match rate | 0.1255 | 0.1164 |
| P(S ≥ 4) | 0.0334 | 0.0229 |
| P(S ≥ 5) (the bar) | 0.0046 | 0.0028 |
| P(S ≥ 6) | 0.0003 | 0.0002 |

Three consequences:

1. **The joint bar is the S bar.** In both comparator sets
   the smallest S whose permutation p falls below 0.01 is
   S = 5. The registered pass rule (p < 0.01 AND S ≥ 5) is
   therefore exactly S ≥ 5 in operation; the two conditions
   never bind separately at n = 12.
2. **The freeze's α is confirmed.** Freeze v2's power
   statement put α ≈ 0.0043 for the S ≥ 5 bar under an
   assumed chance rate of 0.10 per concept. The measured
   chance rates are a little higher (0.1255 R1, 0.1164 R2),
   and the actual permutation α is 0.0046 (R1) and 0.0028
   (R2). The freeze's arithmetic also reproduces exactly
   under its own assumptions (binomial: α = 0.0043; power
   0.806 at rate 0.50 against the stated 0.81; 0.417 at
   0.35 against the stated 0.42).
3. **R1's observed S = 4 sits at the 96.7th percentile of
   its null** (p = 0.0326): above chance expectation by a
   factor of 2.7 in count, one concept short of the bar,
   and a factor of about 3.3 short on the p condition.

## 3. What the design could detect — the prospective frame

Parameterisation (the audit's frame, stated on its face):
let θ be the share of the 12 concepts carrying a true
Meroitic–comparator correspondence, and d the probability
that a true correspondence survives as a match under the
frozen skeleton rule (sound change or transcription can
hide a real correspondence, so d < 1 is the realistic
case). A concept then matches with probability
q = q0 + (1 − q0)·θ·d, with q0 the measured chance rate,
and S is binomial(12, q) to the accuracy the permutation
null confirms. Power is P(S ≥ 5):

| θ | d = 1.0 | d = 0.75 | d = 0.5 |
|---|---|---|---|
| 0.20 | 0.28 | 0.17 | 0.09 |
| 0.35 | 0.65 | 0.43 | 0.22 |
| 0.50 | 0.90 | 0.70 | 0.40 |
| 0.60 | 0.97 | 0.84 | 0.53 |
| 0.80 | 1.00 | 0.97 | 0.75 |

(R1's q0; R2's table is within 0.01–0.02 throughout.)

**Minimum detectable effect at 80% power: θ ≈ 0.43**
(d = 1.0), **θ ≈ 0.57** (d = 0.75), **θ ≈ 0.85**
(d = 0.5), for both comparator sets. In plain terms: at
this design, an affiliation carried by fewer than about
5 of the 12 concepts, or one whose correspondences the
skeleton rule detects only half the time, was more likely
to be missed than caught. The freeze's own summary —
"the tests can therefore detect only a strong
correspondence signal" — is confirmed and now quantified.

## 4. The conditional frame — how far the executed run sat from the bar

A second simulation conditions on the executed comparator
lists: synthetic correspondences are injected into the real
lists (one added comparator form per designated concept,
built from a Meroitic skeleton of that concept so the
frozen rule scores it), and the frozen test is re-run.
This frame answers a narrower question — how much
additional true signal, on top of the lists as they stand,
would have carried the executed run over its bar — and it
flatters R1, whose observed arrangement already sits at
S = 4. It is reported for that narrower purpose only and
is **not** the design's power.

- R1 needed exactly **one** further matching concept.
  With exactly k of the 12 concepts truly corresponding
  and detectable, the executed test passes with
  probability 0.65 (k = 1), 0.91 (k = 2), 0.98 (k = 3),
  and 1.00 (k ≥ 4). Under the θ-parameterisation the
  conditional 80% point is θ ≈ 0.18 (d = 1.0), 0.25
  (d = 0.75), 0.37 (d = 0.5).
- R2, observed at S = 1, needed **four** further matching
  concepts: pass probability 0.00 for k ≤ 3, 0.67 at
  k = 4, and 1.00 at k ≥ 5. Conditional 80% point
  θ ≈ 0.45 (d = 1.0), 0.59 (d = 0.75).

## 5. What the Stage 4.2 verdict rules out, and what it does not

In the prospective frame of §3, the probability of a
result at or below the observed one, by true affiliation
strength (5% level used as the consistency boundary):

**R1 (observed S = 4).** P(S ≤ 4) falls below 0.05 only at
θ ≈ 0.55 (d = 1.0) and θ ≈ 0.73 (d = 0.75); at d = 0.5 no
θ up to 1.0 is excluded. The Clopper–Pearson 95% interval
for the per-concept match probability on 4 of 12 is
[0.099, 0.651], which contains the chance rate 0.1255 and
every moderate-signal value. **The R1 failure therefore
rules out only a strong, cleanly detectable Nubian/Nara
signal (roughly θ above 0.55 at perfect detection). It is
fully consistent with a moderate affiliation (θ up to
about 0.5), with a stronger affiliation whose
correspondences the skeleton rule detects poorly, and
with no affiliation at all.** The R1 result is the
uninformative half of the verdict, exactly as freeze v2
§5 anticipated when it registered the UNDECIDABLE
adjudication for a double failure at this power.

**R2 (observed S = 1).** P(S ≤ 1) falls below 0.05 at
θ ≈ 0.25 (d = 1.0), θ ≈ 0.33 (d = 0.75), θ ≈ 0.50
(d = 0.5). The Clopper–Pearson 95% interval on 1 of 12 is
[0.002, 0.385]. **The R2 vocabulary failure is the
informative half: an Afroasiatic affiliation carried by
more than about a quarter of the concepts, with
correspondences the rule can see, would very probably
have scored higher than 1.** Weaker or poorly detected
affiliation remains consistent with the result.

**The verdict as a whole.** UNDECIDABLE AT THIS POWER
stands, and this audit narrows its meaning in one
direction only: the double failure is not symmetric
evidence. It carries real weight against a strong
Afroasiatic vocabulary signal and very little weight
against a Nubian/Nara affiliation of moderate strength.
Nothing here supports R3 (isolate) either: at the
strengths the design cannot see, R1 and R3 are
indistinguishable to this test, which is the content of
the verdict as registered. Any future affiliation claim
on this corpus basis needs either more concepts, a
correspondence rule with a higher detection rate on known
controls, or both; at n = 12 the bar and the noise floor
are what this record measures them to be.

## 6. The phonotactic leg (analytic note, not simulation)

The R2 phonotactic leg is a rate test on 13,406 pairs, so
its arithmetic differs: the binomial standard error of the
observed rate 0.3152 is ≈ 0.0040, and a one-sided α = 0.01
shuffle test at that count detects a deficit of roughly
0.013 or more at 80% power. The leg was therefore well
powered for its stated effect — and it failed on
direction, not power: the observed Meroitic rate (0.3152)
sits **above** the NES reference rate (0.3038) the leg
required it to fall below, with shuffle p = 0.474. On this
corpus basis Rowan's restriction shows no measurable
deficit; that half of the R2 failure does not plead power.

## 7. Custody and scope notes

All computation ran on the CC BY / CC BY-SA vocabulary and
the CC BY 4.0 ASJP lists, as in Stage 4.2 itself; no
Otten-derived text was touched or published, and the
outputs are aggregate statistics only, per the F-6 custody
posture. The audit's simulations inject synthetic forms
into comparator lists in memory; no corpus file was
modified. Simulation seeds: audit master 20261122;
permutation extension seed 777001; injection seed 424242;
fixed-k seed 5150; consistency seed 987654. Replicates:
100,000 permutations per extended null; 4,000 injection
replicates per (θ, d) cell; 6,000 per consistency cell.

**Flagged for adjudication: nothing.** No Stage 4 verdict,
tally, or standing is touched by this record. One
observation is offered to the record without a
recommendation attached: the two vocabulary failures are
of unequal evidential weight (§5), which future citations
of the Stage 4.2 outcome should preserve rather than
summarise as a symmetric double failure.
