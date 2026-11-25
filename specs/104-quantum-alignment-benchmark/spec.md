# Spec 104 — Quantum Alignment Benchmark: a Quantum Solver against Classical Solvers on the Spec 096 Bilingual Alignment Instance

**Status: REGISTERED 2026-11-25 — registration and
execution both commissioned by the owner's order of
2026-11-25 (Glossa-Lab chat: "do the quantum alignment
benchmark after the program doc").** Registration lands
first; execution follows in a separate landing under
the same commission, exactly as registered here. No
stage of the benchmark has run at registration.

**Provenance.** The owner's decipherment gap analysis
(program document, 2026-11-25) surveyed what each
Glossa-Lab program is missing and identified exactly
one subproblem in the program that a quantum solver
can be tested on without overclaiming: the Eteocypriot
bilingual alignment, because it is a discrete
optimization with a crisp score — the Spec 096 pilot's
own LCCS scoring — whose outputs can be certified
against an exact optimum. The owner ordered the
benchmark on 2026-11-25. This spec registers it.

## 1. What this spec is

A solver benchmark. The research question is: **on the
alignment problem built from Spec 096's E1 pilot
scoring, how does a quantum solver (QAOA, through the
program's IBM Quantum access) compare with classical
solvers, in solution quality against the certified
optimum and in time-to-solution scaling?**

The verdicts are about the solvers only. No outcome of
this study is a decipherment claim, and no outcome is
evidence for or against any reading, correspondence,
or decipherment claim in any program — including the
ICS 196 correspondences themselves, whose ground truth
is never an input to the instance, the formulation, or
any solver (§7). A null or negative result for the
quantum arm is a complete outcome of this study (§6).

## 2. The instance, as counted at registration

- **Source material.** Spec 096's corpus
  (`specs/096-eteocypriot-program/corpus/corpus.json`),
  SHA-256
  `5077285e8eac4b21785ca29cb151d47407f780998d85fa1eea27ef9d7e04f2dd`
  (the Spec 096 freeze pin of 2026-11-20), inscription
  **ICS 196** — the Amathus bilingual — development
  split. This study reads the development-split ICS 196
  record only, exactly as the E1 driver does; Spec
  096's held-out material is never touched.
- **The scored correspondences.** The E1 pilot scored
  exactly two correspondences: the Greek proper names
  carrying ground-truth correspondences in the corpus
  record — **Ἀρίστωνα** (Greek word index 5) and
  **Ἀριστώνακτος** (Greek word index 6) — against the
  inscription's Eteocypriot segments
  (`records/eteocypriot-e1-driver.py`;
  `records/eteocypriot-e1-run-2026-11-20.json`, both in
  Spec 096's records).
- **Segments.** The 11 Eteocypriot segments of ICS 196,
  in corpus order (1-indexed as in the run record):
  1 `a-na`, 2 `ma-to-ri`, 3 `u-mi-e-sa-i`,
  4 `mu-ku-la-i`, 5 `la-sa-na`, 6 `a-ri-si-to-no-se`,
  7 `a-ra-to-wa-na-ka-so-ko-o-se`, 8 `ke-ra-ke-re-tu-lo-se`,
  9 `ta-ka-na-?-?-so-ti`, 10 `a-lo`, 11 `ka-i-li-po-ti`.
- **Score.** s_ij = LCCS(D(name_i), segment_j), where D
  is the E1 driver's R1–R3 derivation of a name's
  expected syllabic spelling and LCCS is the driver's
  longest common contiguous subsequence over syllable
  tokens. The matrix, from the filed run record
  (execution recomputes it from the pinned corpus by
  the driver's own functions and must match exactly,
  TC-104-02):

  | Name | Derived spelling | Scores by segment 1–11 | Σ |
  |---|---|---|---|
  | Ἀρίστωνα | a-ri-si-to-na | 1, 1, 0, 0, 1, 4, 1, 0, 1, 1, 0 | 10 |
  | Ἀριστώνακτος | a-ri-si-to-na-ka-to-so | 1, 1, 0, 0, 1, 4, 2, 0, 1, 1, 1 | 12 |

  Σ_ij s_ij = 22.
- **Why an optimization at all.** The pilot's A2 rule
  scores each name independently and takes the argmax
  per name; on this matrix it assigns **both** names to
  segment 6 (score 4 each) — an infeasible joint
  alignment, one segment carrying two names. The joint
  problem — each name exactly one segment, each segment
  at most one name, maximum total score — is the
  discrete optimization this benchmark solves. (For the
  record only: the corpus ground truth is name 1 →
  segment 6, name 2 → segment 7. The benchmark never
  uses it; §7.)

## 3. The formulation

Binary variables x_ij ∈ {0,1} over names × segments;
n = w·s variables (n = 22 on the real instance).
Maximize

    F(x) = Σ_ij s_ij·x_ij
           − P·[ Σ_i (Σ_j x_ij − 1)²
                + Σ_j Σ_{i<i'} x_ij·x_i'j ]

with **P = 1 + Σ_ij s_ij** (P = 23 on the real
instance; the same rule fixes P on every synthetic
instance, §5).

**Lemma (the formulation's soundness, registered).**
Every s_ij ≥ 0. A feasible x (each name exactly one
segment, each segment at most one name) has F(x) equal
to its score, hence ≥ 0. An infeasible x either leaves
some name's row sum ≠ 1, contributing a squared term
≥ 1 and so penalty ≥ P, or assigns some segment to two
names, contributing a pair term ≥ P; its score part is
at most Σ_ij s_ij = P − 1, so F(x) ≤ −1 < 0. Hence the
QUBO maximum equals the best feasible assignment score
and is attained only at feasible points. ∎

For minimization-based solvers (the quantum arm), the
objective is −F as an Ising Hamiltonian under the
standard substitution x = (1 − z)/2; the classical
arms optimize F as written.

## 4. The arms

- **EXACT (classical; tower-compute).** (a) Exhaustive
  enumeration of the QUBO over all 2^n points, where
  n ≤ 25 (the real instance); (b) an ILP on the
  hard-constraint assignment formulation (row sums = 1,
  column sums ≤ 1, x binary), solved to zero MIP gap
  (HiGHS, through `scipy.optimize.milp`). The ILP
  optimum is the certified optimum of the assignment
  problem; by §3's lemma it is the QUBO optimum. Where
  both run, they must agree (TC-104-03).
- **SA (classical heuristic; tower-compute).**
  Simulated annealing on F as written: single-bit-flip
  proposals from a uniform-random initial point;
  Metropolis acceptance on ΔF at temperature
  T(k) = T0·(Tend/T0)^(k/K) with **T0 = P** (the
  instance's penalty scale, so penalty-crossing moves
  stay traversable early) and **Tend = 0.01**;
  **K = max(50,000, 1,000·n)** proposals per restart;
  **R = 10** restarts per instance, restart r seeded
  104000 + r (Python `random.Random`). Recorded per
  restart: the best F seen, the best feasible score
  seen, whether the certified optimum was reached, and
  the proposal index and wall time of first reaching
  it. The temperature scale and the move set are part
  of this comparator's registered design; a different
  SA design is a different comparator and would need
  its own registration.
- **QUANTUM (IBM Quantum; the `custom.ibm-quantum`
  connector route only).** QAOA on the Ising form of
  −F: depth **p = 2**, COBYLA optimizer (at most 100
  iterations), **1,024 shots** per evaluation, initial
  parameters drawn from seed **1042025**, on the
  least-busy available real backend whose qubit count
  is ≥ n; where n exceeds every available backend, the
  size is recorded **NOT ATTEMPTED — SIZE**. Registered
  fallback: if real-hardware queue time exceeds 2
  hours, a simulator backend the route offers may be
  used, and every result from it is labelled
  **SIMULATOR** in every record and never read as
  hardware. Best-found is the best feasible F among
  sampled bitstrings; infeasible samples are scored by
  F as written and reported separately.
- **Route state, disclosed at registration (D-104-2).**
  The connector's documented authentication reality
  (`~/workspace/custom-connectors/custom.ibm-quantum/CONNECTOR.md`,
  verified 2026-10-27) is that the registered
  connection cannot complete IBM's IAM token exchange:
  its registered hosts carry only
  `quantum.cloud.ibm.com`, its placement is fixed as a
  bearer header, and the IAM exchange needs the key in
  a form-encoded body at `iam.cloud.ibm.com`, which the
  credential system does not offer. The registration-day
  probe (2026-11-25, the connector's
  `bin/ibm_quantum_probe2.py` through the registered
  surrogate path) returned **HTTP 401, error code
  1219, "Error authenticating user"** on
  GET /api/v1/backends and on
  GET /api/v1/accounts/014f444c351f4ecbb720d173b3778b85.
  The quantum arm is registered as designed above;
  **NOT EXECUTED — ROUTE DEAD is a registered outcome
  of the arm** (§6), not a deviation, and no substitute
  route — a local simulator presented as the quantum
  arm, another provider, an owner-side setup — may be
  substituted under this registration. Execution
  re-probes the route once and files the response
  (TC-104-06). The routes that could work (an
  owner-side trusted-environment Qiskit setup, or an
  owner-vaulted short-lived IAM token) are owner
  decisions, neither taken; reviving the route is
  outside this spec (§7).

## 5. The scaling arm

The real instance is small by the pilot's own verdict
(TOO THIN); the exact arm is expected to be effectively
instant on it, which is itself a reportable finding.
Scaling is measured on synthetic instances carrying the
real instance's structure:

- **Sizes** (names w × segments s): (3, 14), (4, 18),
  (6, 24), (8, 32), (10, 40), (12, 48) — n = 42, 72,
  144, 256, 400, 576. With the real instance, the span
  is n = 22 → 576, a factor of 26.
- **Generation (registered, deterministic).** For the
  m-th synthetic size (m = 1..6, in the order listed),
  seed = 20261100 + m, Python `random.Random(seed)`;
  each score drawn i.i.d. in row-major order from the
  real matrix's empirical value distribution — values
  (0, 1, 2, 4) with weights (7, 12, 1, 2), the real
  matrix's exact value census (0×7, 1×12, 2×1, 4×2
  over 22 entries). Same constraint structure, same
  penalty rule P = 1 + Σ s. No correspondence is
  planted: the instances carry the real instance's
  score distribution and structure, not a hidden
  answer.
- **Measurement.** Both classical arms run on every
  size under §4's parameters (EXACT by ILP only above
  n = 25). The quantum arm is attempted per size
  subject to §4's route and size rules. Recorded per
  size: n, Σ s, P, the certified optimum, the ILP wall
  time, the SA per-restart results and their summaries
  (best and median final feasible score, restarts
  reaching the optimum, median time-to-optimum among
  reaching restarts), and the quantum outcome in §6's
  vocabulary.

## 6. Preregistered verdicts

- **V-104-A — real instance, quantum solution
  quality.** Exactly one of: **MATCHES** (a completed
  quantum run's best feasible F equals the certified
  optimum) / **DOES NOT MATCH** (a completed quantum
  run's best feasible F is below it) / **NOT EXECUTED
  — ROUTE DEAD** (the route refuses at execution, as
  at registration) / **NOT EXECUTED — OTHER** (any
  other cause, named in the outcome record).
- **V-104-B — scaling comparison.** Exactly one of:
  **COMPLETED** (both arms measured on the real
  instance and at least 4 of the 6 synthetic sizes) /
  **NOT EXECUTED** (the quantum arm absent at every
  size; the classical table then stands as the
  classical arm's record and no comparison is drawn).
- **Classical findings** are reported as measured,
  under no separate verdict: the certified optimum of
  the real instance, whether SA reaches the certified
  optimum at each size, and the arms' times.

## 7. Hard limits

- No standing, verdict, or tally in any program moves
  (C104-4). The ICS 196 ground truth is never an input
  to any solver, score, or certification.
- All classical computation runs on tower-compute;
  none in the Muse VM. IBM Quantum job submission, if
  the route ever authenticates, goes through the
  connector's API route only.
- Spec 096's held-out set stays untouched: this study
  reads the development-split ICS 196 record only,
  exactly as the E1 driver does.
- No external contact of any kind, no purchases, no
  new credentials. If the route is dead at execution,
  the study closes on §6's registered NOT EXECUTED
  outcomes; reviving the route is an owner decision
  outside this spec.

## 8. Decisions

- **D-104-1 — number.** At the check of 2026-11-25
  the highest landed spec package on origin/main was
  103 (`specs/103-meroitic-source-witness-check/`);
  no 104 directory existed and no branch carried 104.
  This package takes 104.
- **D-104-2 — route state disclosed at registration.**
  The quantum arm is registered with its route's known
  state on the record (§4), and NOT EXECUTED — ROUTE
  DEAD is in the registered outcome vocabulary, so an
  execution that finds the route still dead closes the
  arm without a deviation or an amendment.
- **D-104-3 — taxonomy.** This study is entered in the
  program-map taxonomy under Program infrastructure /
  Governance, lifecycle & generated layers (with Specs
  092, 094, 101): its claims are about the program's
  solver machinery, not about any sign, reading, or
  corpus fact.
- **D-104-4 — no recommendations-ledger row.** The
  study's provenance is the owner's direct order of
  2026-11-25 following his gap analysis; no
  Co-scientist recommendation unit proposes it, and
  the recommendations ledger logs Co-scientist
  recommendations. No row is added.
- **D-104-5 — commission.** The owner's order of
  2026-11-25 (Glossa-Lab chat: "do the quantum
  alignment benchmark after the program doc")
  commissions registration **and** execution in one
  act, in two landings: this registration first, the
  execution second, as its own record.

## 9. Proof map (one page)

| Step | Content |
|---|---|
| Problem | The pilot's per-name argmax (A2) is jointly infeasible: both names land on segment 6. The joint one-to-one alignment under the pilot's own scoring is a discrete optimization with a crisp score. |
| Instance | 2 names × 11 segments from ICS 196 (Amathus bilingual), Spec 096 freeze-pinned corpus; LCCS matrix as filed in the E1 run record (§2). |
| Formulation | QUBO over x_ij, penalty P = 1 + Σ s; lemma (§3): the maximum is the best feasible assignment score, attained only at feasible points. |
| Certification | EXACT arm: exhaustive enumeration (real instance) and ILP to zero MIP gap (all instances) must agree. |
| Comparators | SA on the same F, registered parameters (§4). QAOA through the connector route, registered parameters, SIMULATOR labelling rule, ROUTE DEAD a registered outcome. |
| Scaling | Synthetic instances drawn i.i.d. from the real matrix's value census at 6 sizes, n to 576 (§5); per-size times and qualities reported as measured. |
| Verdicts | V-104-A (MATCHES / DOES NOT MATCH / NOT EXECUTED) and V-104-B (COMPLETED / NOT EXECUTED), returned exactly as registered (§6). |
| Bounds | Solvers only. Ground truth never an input. No standing, verdict, or tally moves (C104-4). |

The formulation is the most elementary the problem
allows: the score is the pilot's own, the constraints
are the alignment's own, and the penalty is the
smallest round rule (one more than the total score)
that makes the lemma a two-line proof. Anything
simpler — scoring names independently — is the pilot's
A2 rule, whose infeasibility is the reason the
benchmark exists.
