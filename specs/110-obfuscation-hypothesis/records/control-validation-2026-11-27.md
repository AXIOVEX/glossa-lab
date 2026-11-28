# Spec 110 control validation — the gate ran, and the battery failed it — 2026-11-27

The battery was run exactly as registered, gate first, on tower in
worktree `spec110-wt-20261127`. Harness:
`records/obfuscation-harness.py` (imports the Spec 109 Stage 1 harness,
SHA-256 `f4e84285…`, for the synthetic corpus builder). Raw gate
output in custody at `glossa-custody/spec110/gate-output.json`,
SHA-256 `070f184d4293d9200796e401f44d7df2fb70e0b4fb497a6dd7d4ee62944
cb8cb`. The harness's payload completed (exit 0); the gate result is
the data below. **No real corpus was scored: the harness stopped at
the gate, and no `raw-output.json` exists.**

## The gate, leg by leg

- **G-A (family A detection): FAIL.** The flattening pattern fired on
  T-HOM in **5 of 5** replications. The structure pattern fired on
  T-POLY in **0 of 5**. Replication 1 recomputed independently
  (TC-110-02): the T-POLY corpus's A3 is 0.7196 against a band max of
  0.7861 and its A4 is 1.6165 against a band min of 0.8578 — the
  three-alphabet mixture's corpus-level bigram statistics stay inside
  the natural band. The band pools letter-profile samples (Latin, A4
  up to 1.8670) with sign-profile samples, and at that width the
  structure clause cannot see this transformation.
- **G-D (family D detection): FAIL — 0 of 5.** Splitting the ten most
  frequent signs into variant pairs does not move the hapax-type share
  (the variants of frequent signs are not hapax), and the registered
  rule requires the inventory size and the hapax-type share to exceed
  the size-matched band together. Family D as registered cannot see
  this T-HOM.
- **G-C (family C detection): FAIL.** C1 fired on T-POLY in **0 of 5**
  (the same structure-pattern insensitivity as G-A). C2 detected
  T-SUB-D in **0 of 5**: the recovered mapping inverted the planted
  permutation on 0.092 / 0.200 / 0.154 / 0.108 / 0.123 of shared signs
  against the registered 0.80 — above chance, far below the bar. The
  profile-matching machinery does not recover a substitution at this
  profile.
- **G-B (family B detection): PASS — 5 of 5.** Observed omnibus JSD
  0.2014–0.2788 against null 99th percentiles of 0.0103–0.0113 and a
  genre-baseline max of 0.0245. The differential-substitution test
  works as registered.
- **G-INV (invariance): PASS — 5 of 5.** No family fired on the
  uniform substitution T-SUB-U in any replication; the registration's
  §2 invariance limit is confirmed empirically.
- **G-FP (false positives): FAIL.** Family C1 fired on **2 of 12**
  natural-control samples (two Latin quarter samples) against the
  registered at-most-1 rule. Family B false-fired on exactly 1 of 5
  synthetic site splits (within its rule: replication 3, observed
  0.0245 against a leave-one-out baseline of 0.0194); families A and D
  false-fired on none. The pooled band is not calibrated across the
  letter/sign heterogeneity of the control set at the registered
  tolerance for C1.

**Gate verdict: FAIL.** Under registration §4 and kill criterion 1,
the battery has failed: the real-corpus runs are **not scoreable** and
the study stops here. No threshold was adjusted after the gate ran,
and no second gate run was made.

## Independent verification (TC-110-02): PASS

`records/tc110-02-control-verification.py`, an independent
implementation importing only the Stage 1 corpus builder: all four
family A band edges reproduce exactly from the control samples; the
replication-1 T-HOM flattening fire and T-POLY non-fire reproduce from
recomputed statistics; the replication-1 G-B detection reproduces
(observed 0.2788 against p99 0.0104 and baseline 0.0245, matching the
filed run to 4 dp); and the filed gate counts mechanically imply the
filed FAIL under the registered thresholds. 8 of 8 checks PASS,
payload exit 0. (One verification-side defect was found and fixed
during the check: the first verification build flattened the Meroitic
corpus at the word level instead of the grapheme level; the corrected
build reproduces the filed bands exactly. The harness's grapheme-level
flattening follows the corpus's structure: lines of words, words of
graphemes.)

## What this outcome is, and is not

The gate establishes three things: family B's differential test and
the battery's invariance property work as registered; families A's
structure clause, C, and D at their registered thresholds do not
detect their registered transformations at this profile; and C1
false-fires above its registered rate on natural controls. It
establishes nothing about the hypothesis on the real corpora, which
were never scored: **H is untested by this battery, not falsified by
it.** A battery that can see these signatures would be a new design
under a new registration; redesigning inside this study is exactly
what the gate exists to prevent.
