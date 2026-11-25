# Spec 104 — Stage 1 outcome record

Date: 2026-11-25. Study: the quantum alignment benchmark
(registration: PR #734, merged 2026-11-25, main `1f76e839`).
Execution ran on tower-compute only, in the study venv
`~/.syncyard/worktrees/glossa/venvs/spec104-study`
(numpy 2.5.5, scipy 1.18.1), by the filed execution script
`records/stage-1-execution-script.py`; raw solver output is
filed at `records/stage-1-raw-output-2026-11-25.json`.

## Verdicts (exactly as registered in spec.md section 8)

- **V-104-A (real instance, quantum solution quality):
  NOT EXECUTED — ROUTE DEAD.** The quantum arm never ran:
  the registered IBM Quantum route refused authentication
  at registration time and again at execution time
  (evidence below). No quantum number exists for the real
  instance, so no MATCHES / DOES NOT MATCH verdict can be
  returned. The certified classical optimum the quantum
  arm would have been judged against is **6** (below).
- **V-104-B (scaling comparison): NOT EXECUTED.** The
  quantum arm is absent at every size. The classical
  scaling table below stands as the study's scaling
  record, and no comparison is drawn.

A null quantum outcome is a complete outcome under the
registration. Nothing in this record is a decipherment
claim, and no anchor standing, verdict, or tally moves
(claim C104-4; the landing diff was audited, TC-104-07).

## The instance as built

From Spec 096's corpus (`specs/096-eteocypriot-program/
corpus/corpus.json`), development split only, inscription
ICS 196 (the Amathus bilingual): the pilot's two scored
correspondences (Ἀρίστωνα, Ἀριστώνακτος) against the 11
Eteocypriot segments, scored by the E1 driver's own LCCS
functions. The recomputed matrix equals the filed E1 run
record exactly: rows [1,1,0,0,1,4,1,0,1,1,0] (Σ=10) and
[1,1,0,0,1,4,2,0,1,1,1] (Σ=12). Variables n = 22, penalty
P = 1 + Σs = 23, per the registered formulation.

## Classical arm — real instance

- **Certified optimum: 6**, certified two independent
  ways that agree (TC-104-03): exhaustive enumeration of
  all 2^22 QUBO points (maximum F = 6, attained at exactly
  one point, which is feasible; the best infeasible point
  scores F = −15, consistent with the registered lemma's
  bound of −1) and ILP on the hard-constraint assignment
  formulation solved to zero MIP gap (HiGHS; value 6;
  0.018 s). The unique maximizer assigns word 1 to
  segment 6 and word 2 to segment 7.
- **Simulated annealing** (registered parameters):
  all 10 restarts reached the certified optimum; median
  time-to-optimum 0.0013 s (first reach between proposal
  338 and proposal 9,285 across restarts). A second,
  identical SA pass reproduced every value (TC-104-05).

## Scaling arm — classical results as measured

Synthetic instances from the registered generator
(spec.md section 5); quantum outcome at every size:
not attempted — route dead.

| size (w×s) | n | P | certified optimum (ILP) | ILP time | SA best | SA median | SA restarts reaching optimum |
|---|---|---|---|---|---|---|---|
| real (2×11) | 22 | 23 | 6 | 0.018 s | 6 | 6 | 10/10 |
| 3×14 | 42 | 42 | 10 | 0.007 s | 10 | 9 | 2/10 |
| 4×18 | 72 | 79 | 14 | 0.006 s | 13 | 10 | 0/10 |
| 6×24 | 144 | 163 | 24 | 0.005 s | 18 | 13 | 0/10 |
| 8×32 | 256 | 263 | 32 | 0.011 s | 22 | 15.5 | 0/10 |
| 10×40 | 400 | 375 | 40 | 0.013 s | 18 | 15.5 | 0/10 |
| 12×48 | 576 | 569 | 48 | 0.006 s | 22 | 18.5 | 0/10 |

Reportable shape, stated plainly: the exact ILP arm
certifies every registered size in at most 0.018 s — on
this problem family the classical exact solver is
effectively instant at every size the study registered —
while the fixed-budget SA heuristic's solution quality
falls steadily behind the certified optima as size
grows. Per-restart detail is in the raw output file.

## Quantum arm — the dead route, with evidence

Probe filed at `records/quantum-route-probe-2026-11-25.txt`
(execution-day re-probe, TC-104-06; the registration-day
probe returned identically). Through the registered
connector route: GET /api/v1/backends → HTTP 401, error
code 1219 "Error authenticating user"; GET
/api/v1/accounts/014f444c351f4ecbb720d173b3778b85 → HTTP
401 code 1219; GET /api/v1/instances → 404. Root cause,
per the connector's own verified record: the registered
connection cannot perform IBM's IAM token exchange (its
hosts list carries quantum.cloud.ibm.com only and the
placement is fixed as a bearer header; the exchange
needs the API key form-encoded at iam.cloud.ibm.com), so
the key presented directly as a bearer token is refused.
No backend list, job submission, or simulator session is
reachable through the route. Per the registration, no
unregistered route was substituted, and no local
simulator result was produced or labelled as one. The
routes that could open the arm (an owner-side
trusted-environment Qiskit setup, or an owner-vaulted
short-lived IAM token) are owner decisions; neither has
been taken.

## Finding F-104-1 — the Spec 096 freeze pin is stale

TC-104-02's pin conjunct failed at execution: the corpus
file hashes to 2954283d… against the registered freeze
pin 5077285e…. The evidence chain, all read from the
repo: the pin names the corpus blob as frozen at Spec
096 Stage 1 (commit 173882a2, 2026-11-20, blob hash
5077285e… — the pin was correct when frozen); the E1 run
of record ran the same day against those bytes; Red Team
correction rounds then changed the corpus (rounds 1–3,
last at commit d0047041, 2026-11-21) without refreshing
the pin or the E1 driver's identical built-in constant.
A semantic diff of the frozen and current blobs touches
only translation glosses, status and sealing metadata,
and the corpus version field (1.0.0 → 1.1.1) — never the
Eteocypriot lines or the ground-truth correspondences
this study consumes — and the recomputed matrix from the
current file equals the filed run record exactly.

Disposition: the deviation is recorded here and in the
raw output (`pin_match: false, deviation: F-104-1`);
execution proceeded on the registered content gate,
which passed exactly, and would have stopped the
execution had the matrix differed in any cell. The pin
itself belongs to Spec 096's records and is not edited
from this study; refreshing it (and the driver's
constant) is a Spec 096 housekeeping act for the program
to schedule. TC-104-02 is therefore recorded as
**PASS WITH DEVIATION F-104-1**, not as a clean pass.

## Test cases

| test case | result |
|---|---|
| TC-104-01 registration precedes execution | PASS (PR #734 merged before any execution) |
| TC-104-02 instance fidelity | PASS WITH DEVIATION F-104-1 (pin stale; recomputed matrix equals the filed run record exactly) |
| TC-104-03 certification agreement | PASS (exhaustive max F = 6 = ILP value; unique feasible argmax; best infeasible F = −15) |
| TC-104-04 QUBO/ILP consistency | PASS (ILP point feasible with F = its score at all 7 instances) |
| TC-104-05 SA determinism | PASS (second pass identical in every value) |
| TC-104-06 quantum route probe | PASS (probe filed; refusal documented; arm closed on evidence) |
| TC-104-07 standing audit | PASS (landing diff adds only this study's records under specs/104-quantum-alignment-benchmark/records/; no standing, verdict, tally, or recommendations-ledger file touched) |

## Outcome against the registered claims

- C104-1 (instance fidelity): the consumed material is
  proven identical to the pilot's; the pin instrument
  itself is stale (F-104-1).
- C104-2 (classical certification): supported as
  registered — two exact methods agree on 6; SA reaches
  it 10/10 on the real instance.
- C104-3 (quantum comparison): not executed — route
  dead; the claim's comparison was never run and no
  quantum result is asserted in either direction.
- C104-4 (no standing moves): held.
