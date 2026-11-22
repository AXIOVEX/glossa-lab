# Spec 102 — Design-Stage Counts and Power Simulation (2026-11-22)

**Commission:** OD-21 (owner, 2026-11-22 13:51 ET).
**Venue:** tower-compute. **Status:** design stage only.
Nothing in this record is a study result: no expanded
vocabulary exists, no gate has been computed against a
freeze, and nothing has been scored. The counts below
measure what the held material can and cannot support,
and the simulations measure the registered design's
operating characteristics, so the spec's gates
(G-1, G-2) rest on numbers rather than hopes.
**Method:** the program's own frozen pipeline
(`pipeline-v2.py` of the Spec 097 campaign, held in
the campaign scratch on tower-compute) imported
unchanged; the counting and simulation driver is
filed at `tools/design_power_sim.py` in this spec's
directory. No Otten-derived text was touched or
published; every input below is CC BY 4.0, CC BY-SA
4.0, or an aggregate over them.

## 1. The held-material ceiling

- The frozen vocabulary (gold lexicon CC BY 4.0 +
  Meroitic Wiktionary CC BY-SA 4.0, built by the
  pipeline's own `build_vocab`) carries **182 forms**,
  of which **26 carry an ASJP concept**, over exactly
  **12 concepts**: 12, 15, 16, 17, 21, 46, 55, 62, 70,
  72, 75, 97 — the Stage 4.2 twelve. Per-concept
  Meroitic form counts: 12: 2, 15: 3, 16: 2, 17: 2,
  21: 1, 46: 1, 55: 4, 62: 2, 70: 2, 72: 4, 75: 2,
  97: 1 (identical to OD-17 §3.1's executed table).
- The gold lexicon carries 82 entries (47 certain,
  34 probable, 1 debated). Its entries beyond the
  scored twelve are titles, theonyms, toponyms, and
  kin terms; no ASJP concept attaches to them under
  any faithful mapping. **Concept expansion from held
  material is impossible** — the finding spec §2
  registers and D-102-4 acts on.

## 2. Comparator and reconstruction coverage

- ASJP (pins as freeze v2 §4): the R1 set (Old
  Nubian, Nobiin, Dongolawi, Kunuz, Meidob, Nara)
  covers **100 of 100** concepts; the R2 set
  (Coptic, Late Egyptian, Middle Egyptian, Akkadian,
  Biblical Hebrew, Amharic, Hausa) covers **100 of
  100**. Per-concept comparator counts over the
  scored twelve: NES 2–8 forms per concept, AA 2–8
  (full table in OD-17 §3.1).
- PROTO_NILE_NUBIAN covers **16 concepts** (11, 22,
  39, 41, 43, 44, 47, 51, 54, 57, 61, 66, 72, 75,
  82, 100); only 72 and 75 intersect the scored
  twelve. Arm R (spec §3.4) is therefore only
  meaningful over an expanded vocabulary, as
  registered.

## 3. The primary statistic on the executed lists (validation)

The graded statistic T of spec §3.2, computed on the
Stage 4.2 lists as filed (20,000 permutations, seed
777001):

| | T observed | Null mean | Permutation p | Null 99th pct |
|---|---|---|---|---|
| R1 | 9 | 4.50 | 0.0421 | 10 |
| R2 | 4 | 5.08 | 0.7623 | 10 |

The asymmetry OD-15 measured in the binary statistic
(R1 near its bar, R2 nowhere near) reproduces in T:
the design-stage statistic is validated against the
executed record before it is used for power.

## 4. Injection power for T at N = 12 (conditional frame)

By OD-15 §4's method (synthetic correspondences
injected into the real lists; 4,000 replicates per
cell; bar at the null's 99th percentile):

| θ | d = 1.0 | d = 0.75 | d = 0.50 |
|---|---|---|---|
| 0.20 | 0.776 | 0.667 | 0.511 |
| 0.35 | 0.952 | 0.879 | 0.717 |
| 0.50 | 0.992 | 0.960 | 0.860 |
| 0.65 | 1.000 | 0.987 | 0.929 |

Minimum detectable effect at 80% power, interpolated:
**θ ≈ 0.22 (d = 1.0), 0.29 (d = 0.75), 0.42
(d = 0.50)** — against the executed binary design's
0.43 / 0.57 / 0.85 (OD-15 §3). This frame conditions
on the executed lists and flatters the design, as
OD-15 states of its own §4; it is the method gate
G-2 re-runs on the frozen expanded lists, not a
promise about them.

## 5. The binary statistic at expanded N (prospective bound)

Binomial frame of OD-15 §3 with the measured chance
rate q0 = 0.1255, per-test α ≤ 0.005, q = q0 +
(1 − q0)·θ·d:

| N | Bar (S ≥) | α | Power at (θ = 0.30, d = 0.75) |
|---|---|---|---|
| 12 | 6 | 0.0018 | 0.16 |
| 20 | 8 | 0.0019 | 0.30 |
| 30 | 10 | 0.0027 | 0.52 |
| 40 | 12 | 0.0028 | 0.68 |
| 50 | 14 | 0.0027 | 0.78 |

The independence assumption makes this the
conservative bound (the measured permutation tail is
thinner: OD-15 §2). It is carried on the design's
face (spec §4) so the comparability subset's limits
are registered alongside the primary statistic's.

## 6. What these numbers fix in the design

- G-1's floor (40 concepts, 20 of them new) sits
  where the expanded test's power becomes decisive
  for the primary statistic and meaningful even for
  the binary bound; below it, the study would risk
  repeating Stage 4.2's uninterpretable outcome on
  fresh material, which M-18 forbids in spirit.
- G-2's threshold (80% power at θ = 0.30, d = 0.75
  by the §4 method on the frozen lists) is met at
  N = 12 by the statistic alone (0.879 at θ = 0.35;
  MDE ≈ 0.29) — the gates bind jointly, so neither
  a large-but-weak vocabulary nor a strong statistic
  on consumed material can administer the test.
- Seeds: permutation extension 777001; injection
  424242. Replicates: 20,000 permutations; 4,000
  injection replicates per cell.

**AI disclosure:** executed by an AI agent (Muse, via Muse)
at the direction of Tristen Pierson, per constitution sec. VI.
