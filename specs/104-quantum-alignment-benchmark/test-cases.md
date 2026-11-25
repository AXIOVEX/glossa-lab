# Spec 104 — Test Cases

Each test case names the claim it exercises, its
procedure, and its pass condition. TC-104-01 is
Stage 0's acceptance test and is recorded in
`records/registration-2026-11-25.md`; TC-104-02..
TC-104-07 execute with Stage 1.

**TC-104-01 — Package form (C104-1..C104-4; Stage 0).**
Parse `aee-claims.json`; compare its claim ids and
order against claims.md; check every claim carries a
falsifier and a does-not-establish line.
*Pass:* the JSON parses; the same four claim ids in
the same order in both files; every falsifier and
does-not-establish line present.

**TC-104-02 — Instance fidelity (C104-1; Stage 1,
before any solving).** Verify the corpus file SHA-256
against the Spec 096 freeze pin
(`5077285e8eac4b21785ca29cb151d47407f780998d85fa1eea27ef9d7e04f2dd`);
recompute the score matrix from the pinned corpus with
the E1 driver's own derivation and LCCS functions
(`specs/096-eteocypriot-program/records/eteocypriot-e1-driver.py`),
loading development records only.
*Pass:* the pin verifies; the recomputed matrix equals
the filed E1 run record's `lccs_by_segment` for both
names, cell for cell; the derived spellings equal the
run record's. Any inequality stops the execution and
is filed as a finding (plan.md, Stage 1 stop rule).

**TC-104-03 — Formulation soundness, real instance
(C104-1; Stage 1).** Enumerate the QUBO exhaustively
over all 2^22 points; solve the hard-constraint
assignment ILP to zero MIP gap.
*Pass:* the exhaustive maximum equals the ILP optimum
in value; every exhaustive maximizer is feasible (each
name exactly one segment, each segment at most one
name); every infeasible point has objective value
below 0 (the §3 lemma, checked on the whole space).

**TC-104-04 — Penalty rule at every size (C104-1;
Stage 1).** For the real instance and each synthetic
instance, recompute P from the instance's scores and
evaluate the QUBO objective at the ILP optimum point.
*Pass:* P = 1 + Σ_ij s_ij at every size; the ILP
optimum point is feasible and its QUBO value equals
its assignment score.

**TC-104-05 — SA determinism (C104-2; Stage 1).** Run
the SA arm twice on the real instance under the
registered parameters and seeds (spec.md §4).
*Pass:* the two runs' per-restart best F values, best
feasible scores, and optimum-reaching proposal indices
are identical (wall times excepted).

**TC-104-06 — Quantum route evidence (C104-3;
Stage 1).** File the execution-time route probe
response (and, if the route authenticates, the job
records) in this spec's `records/`.
*Pass:* every quantum number in the outcome record
traces to a completed job record on the connector
route, with simulator runs labelled SIMULATOR; or the
arm's outcome is recorded NOT EXECUTED — ROUTE DEAD
with the probe's refusal response filed and no quantum
number reported for any size.

**TC-104-07 — Standing discipline (C104-4; Stage 1).**
Read the outcome record and the execution landing's
full diff.
*Pass:* no record states a changed standing, verdict,
or tally in any program; the outcome record's verdicts
are exactly V-104-A and V-104-B in spec.md §6's
vocabulary; the recommendations ledger is untouched by
this study (D-104-4).
