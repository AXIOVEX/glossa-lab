# Spec 107 — Cycle 2 Outcome Record (T206)

**Date:** 2026-11-27. **Program:** Spec 107 — Active
Decipherment Loop, cycle 2. Registration:
`records/cycle-2-registration-2026-11-27.md` (PR #794,
merged 3b8503f0). This record closes the cycle: every
leg's outcome against its registered falsifier (§1), the
posterior trace (§2), and the kill-criteria evaluation
(§3, TC-107-12). TC-107-11's diff audit is at §4.

## 1. Outcomes against the registered falsifiers

**I-2 (Indus) — INDETERMINATE.** Executed exactly as
registered, preflight first (`records/i2-outcome-record-2026-11-27.md`;
raw output `records/i2-raw-output.json`). The OD-O-1
preflight PASSED in full: target shape exact (1,670 /
7,002 / 390 / d = 20/1670); achieved duplication exactly
0.011976 in 120/120 replications; R2 ground-truth sets
in exact two-implementation agreement. R1 is positive
for both donors at 1× (Meroitic RIGHT 0.6822 vs SHUFFLE
0.2263; Latin 0.4338 vs 0.1019). R2 is measurable for
neither donor at either registered level — the donors'
ground-truth restricted sets at ρ ∈ {0.95, 0.90} over
non-sole occurrences contain one mark (Meroitic *a*,
initial) and zero marks (Latin), against a measurability
floor of 5 — so the registered rule returns
INDETERMINATE. C107-7's falsifier is not met: the
verdict is the mechanical consequence of the registered
rule over the filed per-replication values, and the two
implementations agree on every ground-truth set and
count (TC-107-07 executed).

**C-E-15 / E-2 (Eteocypriot) — decision STOP; E-2 not
executed.** The feasibility decision
(`records/ce15-decision-record-2026-11-27.md`) applied
the registered four-condition rule to the inventoried
correspondences: the ICS 196 pair is consumed (and is
one trial under the independence rule); the Androkles B
correspondences and the residue names of A fail
independent identifiability; the one remaining item,
Ἀνδροκλῆς ↔ *a-to-ro-ke-le-we-se* in ANDROKLES-A, is a
single trial and fails the arithmetic-sufficiency
condition against the named baselines at the registered
battery's thresholds. C107-8's falsifier is not met: no
set satisfying all four conditions exists in the filed
record, and the decision is STOP (TC-107-08 executed).
E-2's non-execution is filed at
`records/e2-non-execution-record-2026-11-27.md`;
C107-9's outcome is that recorded non-execution, as
registered (TC-107-09 executed, non-execution arm).

**M-2 (Meroitic) — STOPPED AT THE CALIBRATION GATE,
basis finding.** The registered reconstruction from the
pinned Kovetsky build only yields 4,886 words / 5,883
CVC pairs / same-place rate 0.3002 against the filed
12,863 / 13,406 / 0.3152, while the NES reference
reproduces exactly (0.3038), isolating the failure to
the Meroitic basis: the filed figures were computed
over the development partition plus the 932 example
phrases of the Otten & Anastasopoulos (2025) corpus,
which the registration excludes from M-2 inputs and
which are in any case no longer in tower custody
(`records/m2-outcome-record-2026-11-27.md`; calibration
script and output filed alongside it). The battery was
not run; no battery statistic exists. C107-10's
falsifier is met in its stop arm — the calibration
figures were not reproduced and the battery did not
score anyway; it stopped, as registered (TC-107-10
executed, gate arm).

## 2. Posterior trace

Priors are the registration §1 record; movements cite
their licensing outcome records.

- **Indus positional clause.** Prior P(I-2 POSITIVE)
  0.55. Outcome INDETERMINATE, with the configuration
  changed underneath it: the R1 separation is now
  calibrated on a conforming generator (I-1's
  qualification is discharged), and the clause's
  untestability is measured rather than suspected — at
  realistic restriction levels the known-structure
  donors hold essentially no restricted marks (1 and 0).
  The binding constraint on this question is no longer
  the machinery or the simulation; it is the scarcity of
  the phenomenon in any donor available to the program.
  A future positional test at these levels has a lower
  prior of measurability than cycle 2 assumed; a test at
  materially lower restriction levels would be a
  different claim about a different phenomenon and would
  need its own registration. (Licensed by the I-2
  outcome record.)
- **Eteocypriot alignment line.** Prior P(STOP) 0.80;
  STOP realized. The line's validation path is closed on
  the present material: its ground truth is consumed and
  what remains is one trial. No posterior remains to
  carry — the question is answered, not deferred.
  (Licensed by the C-E-15 decision record.)
- **Meroitic phonotactic affiliation.** Prior
  P(POSITIVE for a family) 0.25. The battery question is
  untouched — no evidence about either family was
  produced, and the 0.25 carries forward unmoved as a
  prior for any future administration. What the cycle
  did move is a basis belief: "the Spec 097 phonotactic
  basis is re-derivable from the Kovetsky build alone"
  is refuted by measurement (4,886 of 12,863 words), and
  the design queue inherits a re-registration task — a
  Kovetsky-only basis with freshly computed calibration
  figures, or a lawful basis including the example
  phrases with custody restored — priced with the
  knowledge that the Otten custody tree is absent from
  tower-compute and its recovery is an owner-side
  question. (Licensed by the M-2 outcome record.)
- **The loop itself.** Cycle 2 is the first cycle whose
  Indus leg ran on a generator proven conformant before
  scoring; both of its other legs closed by gates
  working as designed (a decision rule and a calibration
  gate). The trace records no standing, verdict, or
  tally change in any program (C107-11; §4).

## 3. Kill-criteria evaluation (spec.md §4; TC-107-12)

1. **Information exhaustion** (cycles 1 and 2 jointly):
   cycle 1 returned a supported-adjudicated negative
   (E-1), a positive (M-1), and an indeterminate (I-1);
   cycle 2 returned a verdict, a decision with a
   consequence, and a basis finding with a consequence.
   Neither cycle is a no-yield cycle, and queued tests
   with expected information gain remain (the M-2
   re-registration; the Spec 102 affiliation test armed
   on its own gates). **Not met.**
2. **Total blockage:** the remaining discriminating
   tests are not all blocked on named external inputs.
   M-2's blockage is a registration defect plus a
   custody loss, both internal; I-2's is a property of
   the fixed donor corpora. **Not met.**
3. **Ranking collapse:** cycle 2's outcomes are not
   knife-edge under any recorded perturbation — the
   preflight margins are exact, the C-E-15 arithmetic
   fails by an order of magnitude (one item against a
   multi-item battery), and the calibration gate fails
   by 7,977 words. **Not met.**
4. **Null yield** (against registration §2's minimum —
   at least one leg returning a non-indeterminate
   verdict or a decision/finding with a consequence):
   the C-E-15 STOP is a decision with a consequence (the
   alignment validation path closes), and the M-2 basis
   finding has a consequence (a registration defect
   identified and a re-registration task queued). The
   minimum is met; cycle 2 is not a null cycle. **Not
   met.**
5. **Integrity tripwire:** no breach of a custody term,
   gate condition, or the registration discipline
   occurred in cycle 2's execution — every gate was
   administered as registered and its outcome recorded;
   no unregistered analysis entered the trace; no
   restricted bytes were used (the Otten material was
   never touched, and is absent). Two standing items are
   recorded under this criterion's care: OD-O-1 was
   ruled by the owner on 2026-11-27 and is discharged by
   the I-2 preflight as registered; OD-O-2 (the Round O
   Eteocypriot conformance qualifications) remains
   unruled by the owner and stands as an open referral —
   no cycle-2 record asserts Eteocypriot licensing
   language. The M-2 basis defect is a registration
   defect discovered by a gate before any scoring, not
   an execution breach; it is recorded in the M-2
   outcome record and carried into the design queue.
   **Not fired.**

**Conclusion: the loop stays open.** No criterion is
met; the cycle's three legs each produced the outcome
their registrations specified for what the evidence
turned out to be.

## 4. TC-107-11 diff audit (executed at pull-request time)

The cycle-2 execution landing's diff against its base
(merge 3b8503f0) contains only: the three legs' outcome
records, execution scripts, raw outputs, and the I-2
script diff; the E-2 non-execution record; this outcome
record; two history-ledger entries; the tasks.md ticks
for T202–T206; and one disposition annotation on the
recommendations ledger's C-E-15 row recording the
decision (an annotation of the row's own item, licensed
by the C-E-15 decision record — not a standing change).
No claim standing, verdict, or tally in any program is
changed by the landing; every effect in §2 cites its
licensing outcome record; the I-2, C-E-15/E-2, and M-2
effects match registration §3, §5, and §6's registered
effects exactly.

**AI disclosure:** executed by an AI agent (Muse, via
Muse) at the direction of Tristen Pierson, per
constitution sec. VI.
