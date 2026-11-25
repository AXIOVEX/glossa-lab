# Spec 104 — Claims

Four claims, C104-1..C104-4, each with its falsifier
and its does-not-establish line, in the program's
claim form. The claims are intaken at registration
through the sanctioned importer (spec.md, D-104-5);
intake sets no standing, and no claim in this package
carries a result: the benchmark has not executed.

**C104-1 — The instance and the formulation are
faithful to the Spec 096 pilot's scoring.** The score
matrix recomputed from the freeze-pinned corpus
(SHA-256
`5077285e8eac4b21785ca29cb151d47407f780998d85fa1eea27ef9d7e04f2dd`)
by the E1 driver's own derivation equals the filed E1
run record's matrix exactly, and the QUBO of spec.md
§3 (penalty P = 1 + the sum of all scores) attains its
maximum exactly at the best feasible one-to-one
assignment of that scoring, certified independently by
exhaustive enumeration and by an exact ILP solve to
zero MIP gap.

*Falsifier:* any of — the recomputed matrix differing
from the filed run record in any cell; the exhaustive
QUBO optimum differing from the ILP optimum in value;
a QUBO maximizer that is infeasible (a name without
exactly one segment, or a segment carrying two names);
an infeasible point of the real instance with
objective value at or above 0.

*Does not establish:* that the pilot's correspondences,
or any reading of any Eteocypriot text, are correct —
the corpus ground truth is never an input to the
instance, the formulation, or any solver.

**C104-2 — The classical arms' filed results are the
registered procedures' actual outputs.** The exact
arm's certified optima and times, and the
simulated-annealing arm's per-restart best values,
optimum-reaching counts, and times, are produced on
tower-compute under the parameters and seeds
registered in spec.md §4, on the real instance and on
the synthetic instances the registered generator of
spec.md §5 produces.

*Falsifier:* a rerun of the filed execution script,
under the registered parameters and seeds on the same
instance data, producing a different certified optimum
at any size, or different simulated-annealing best
values (timings excepted, which are reported as
measured and expected to vary).

*Does not establish:* any solver's performance on any
other instance, formulation, parameter set, or machine.

**C104-3 — The quantum arm's reported outcome is
exactly what the program's IBM Quantum connector route
returns.** If the route authenticates and jobs
complete, the best-found values filed are those of the
completed job records, with simulator runs labelled
SIMULATOR; if the route refuses authentication at
execution as it did at the registration probe of
2026-11-25 (HTTP 401, error code 1219), the arm's
outcome is NOT EXECUTED — ROUTE DEAD and no quantum
number is reported for any size.

*Falsifier:* any quantum result in this study's
records not traceable to a completed job record on the
connector route; any simulator result labelled or
readable as hardware; any quantum number reported for
a size while the arm's outcome stands NOT EXECUTED.

*Does not establish:* anything about quantum hardware
or QAOA capability in general — only about this
program's access route and, if jobs ever run under
this registration, about these instances.

**C104-4 — The benchmark moves no standing by
itself.** No anchor standing, claim verdict, or tally
in the Indus, Eteocypriot, or Meroitic programs
changes by anything this study files; its verdicts
concern solvers only.

*Falsifier:* any record of this study stating a
changed standing, verdict, or tally; any citing record
treating this benchmark's outcomes as evidence for or
against any decipherment claim, including the ICS 196
correspondences.

*Does not establish:* that the alignment formulation
is the right model of the Amathus bilingual — it is
the Spec 096 pilot's own scoring reused as an
optimization instance, nothing more.
