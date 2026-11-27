# Spec 102 — Execution Machinery: Build and Fixture Verification (2026-11-27)

## 1. What was built

`tools/execution_machinery.py` — the scoring and gate
machinery the execution registration of 2026-11-27
schedules, implemented from the registered text of
Spec 102 (spec.md §3.2, §3.6 as amended, §3.7, §4 as
amended RT6-M11) and Spec 097 freeze v2 (§4, §7):

- per-concept graded score (2 / 1 / 0 under the frozen
  correspondence rule) and the primary statistic T;
  the frozen binary S for the comparability subset;
- the joint permutation null (comparator forms shuffled
  across concepts, per-concept counts preserved) and
  the permutation p-value (1 + #{perm ≥ obs}) /
  (1 + nperm);
- Holm adjustment across the two-test family;
- G-1's arithmetic (≥ 40 scored concepts per test,
  ≥ 20 outside the Stage 4.2 twelve, per-test concept
  sets);
- G-2's operative simulation as RT6-M11 pins it:
  the registered injection construction, 4,000
  replicates per (θ, d) cell, the bar at the
  permutation null's 99th percentile in the
  design-stage form (sorted[int(0.99 · n)]), and
  deterministic stream derivation from the single
  freeze-registered integer seed;
- the prospective binomial bound of spec §4
  (q0 = 0.1255, per-test α ≤ 0.005);
- the §3.6 split construction as amended (RT6-H6).

The machinery operates at skeleton level. The skeleton
computation itself is not fixed by Spec 102's
registered text (the ASJPcode mapping and diacritic
fold are Spec 097 pipeline code, freeze v2 §7) and is
a freeze-time input, as the execution registration
records; the module's `fixture_skeleton` exists only
for its own fixtures and is marked as never a study
input.

## 2. How it was verified: synthetic fixtures only

`tools/test_execution_machinery.py` — 13 fixture
tests. Every expected value was computed independently
of the machinery:

- **the split construction** against TC-102-07's
  filed table (all five texts: digest, residue, and
  side exact);
- **the pair rule, T, and S** against cases computed
  by hand from spec §3.2's text;
- **the permutation null** against exact enumeration
  of a two-concept fixture by `itertools.permutations`
  (the null takes exactly the enumerated values
  {0, 4}, in roughly equal shares over 400 draws);
- **the p-value form and the 99th-percentile bar**
  against hand arithmetic;
- **the Holm adjustment** against hand-computed cases;
- **G-1's arithmetic** against two synthetic
  vocabularies whose counts are fixed by construction;
- **the injection construction** at its deterministic
  extremes (θ = d = 1 forces T to its maximum in every
  replicate; θ = 0 injects nothing and a replicate
  never strictly exceeds a bar equal to its T), and
  **seed determinism** (identical seed and stream
  reproduce an identical power result);
- **the binomial bound** against the prospective table
  printed in spec §4 itself (N = 30 → bar S ≥ 10,
  power 0.52; N = 40 → bar 12, 0.68; N = 50 → bar 14,
  0.78; α ≤ 0.005 in each case) — the only power
  figures in this verification, and they are the
  design's own registered expectations, recomputed.

Result: **13 of 13 fixture tests PASS** (plain runner;
each test prints its own progress line as it passes).
File hashes at filing: `execution_machinery.py`
SHA-256
`480e99cb11b1a39c188ec285e874966d5a88fb0155e2a21013d626cd13abdcc4`;
`test_execution_machinery.py` SHA-256
`6e7417e56f1b96af35daa001b16dc906d6b835bac268dd9f915ba1b9812d68d9`.

## 3. Venue disclosure, stated plainly

The machinery was to be built and tested on
tower-compute. The tower-compute SSH route was
attempted on 2026-11-27 and its approval timed out
unanswered; it was not retried. The build and the
fixture verification therefore ran in the Muse VM,
on synthetic fixtures only — no custody material, no
corpus, and no study computation of any kind was
touched there, and the machinery is pure Python whose
fixture results do not depend on the venue. This is
recorded as a deviation from the commissioning
brief's venue instruction, not papered over: the
execution registration (§6) makes re-running the
fixture suite on tower-compute, with the result filed
with the freeze, a precondition of the freeze. No
freeze, scoring, or gate computation may rest on the
VM verification alone.

## 4. Hard limits observed

No real concept list was frozen. No real power figure
was computed. No Meroitic form was scored. Nothing was
compared against any family hypothesis. The study's
state after this record is the armed state the
execution registration files.

**AI disclosure:** executed by an AI agent (Muse, via Muse)
at the direction of Tristen Pierson, per constitution sec. VI.
