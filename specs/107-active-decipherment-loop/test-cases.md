# Spec 107 — Test Cases

Each test case names the claim it exercises, its
procedure, and its pass condition. Stage 0's acceptance
test is TC-107-01; the Stage 1 test cases execute with
cycle 1 and their results are filed in the cycle-1
outcome record.

**TC-107-01 — Package form (C107-1; Stage 0).**
Parse aee-claims.json; compare its claim ids and order
against claims.md; check every claim for a falsifier and
a does-not-establish line; check that spec.md §2 states
the five loop steps and §4 the five kill criteria.
*Pass:* the ids and order are equal (C107-1..C107-6);
every claim carries both lines; the loop and the
criteria are stated in full.

**TC-107-02 — I-1 execution conformance (C107-2;
Stage 1).** From the filed I-1 run record and raw output:
recompute the target shape parameters from the custody
datasets' filed censuses; verify the donor pins; verify
the replication table carries every registered cell
(2 donors × 3 scales × 20 replications × 3 conditions);
recompute each cell's median advantage and the 1×
positional-recovery figures from the filed
per-replication table; apply the registered verdict
rule to the recomputed figures.
*Pass:* every recomputation equals the filed value; the
filed verdict is the mechanical consequence of the
registered rule over the recomputed figures; the
independent second implementation of the predictor
scoring agrees with the first on every replication's
advantage to six decimal places.

**TC-107-03 — M-1 execution conformance (C107-3;
Stage 1).** From the filed M-1 run record and raw output:
verify the build pin; verify the Population S pooled
recomputation reproduces the filed Spec 105 figures
exactly (24,648 adjacencies; 448 distinct ordered pairs;
top pair (t, e) at 1,352; a-sign 737 occurrences, 725
group-initial-or-sole; i-sign 2,880 occurrences, 2,857
neither-initial-nor-sole); verify the Population P
partition reproduces the filed strata counts (development
335 — funerary 223, royal/temple 41, document 42,
graffito 22, other 7; held out 33 — funerary 16,
royal/temple 10, document 5, graffito 2, other 0);
recompute the per-stratum conformance rates from the
filed per-stratum positional table and apply the
registered verdict rule.
*Pass:* every validation figure reproduces exactly; the
verdict is the mechanical consequence of the registered
rule over the recomputed rates. A validation failure is
a STOP under the registration, filed as such, and is not
a PASS of this test case.

**TC-107-04 — E-1 execution conformance (C107-4;
Stage 1).** Read Spec 101's execution records as landed
in its package: TC-101-01 (intake identity), TC-101-02
as extended (registration precedence and floor values),
TC-101-03 (scoring reproduction), TC-101-04 as amended
(the verbatim exposure string), TC-101-05 as conformed
(floor arithmetic and complete tables), TC-101-06
(TOO THIN closure path, exercised in procedure).
*Pass:* every one of TC-101-01..TC-101-06 is executed
with its result filed in Spec 101's records, and no
deviation from the registered design is recorded in any
of them; a deviation recorded in Spec 101's records is
reported here as this test case's result, not smoothed
over.

**TC-107-05 — Trace and standing discipline (C107-5;
Stage 1, executed at pull-request time).** Over every
landing diff of this study: check that no record of any
program's standings, verdicts, or tallies is altered in
content outside the outcome records and the cycle-1
trace this spec files, and that every standings effect
named in the trace cites its licensing outcome record.
*Pass:* the diffs are confined as stated, and the
trace's citations are complete.

**TC-107-06 — Kill-criteria evaluation (C107-6;
Stage 1).** Read the cycle-1 trace's kill-criteria
section: each of the five criteria of spec.md §4 is
tested against the filed trace in words, including the
null-yield criterion against the minimum set in the
cycle-1 registration §1 (any one of: a test verdict that
is not INDETERMINATE / NOT TESTED; a standings effect
licensed by an outcome record; a queue re-ranking that
changes any program's cycle-2 lead).
*Pass:* all five evaluations are present, each is
traceable to the filed trace, and the loop's state after
cycle 1 (open or closed, with the criterion named if
closed) is stated.
