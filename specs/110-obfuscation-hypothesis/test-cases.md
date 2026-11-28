# Spec 110 — Test Cases

Each test case names the claim it exercises, its
procedure, and its pass condition. TC-110-01 is the
registration acceptance test; TC-110-02 and TC-110-03
execute with the battery; TC-110-04 and TC-110-05
execute at the close.

**TC-110-01 — Package form (C110-1; registration).**
Parse the package's bundle file (aee-claims.json);
compare its claim ids and order against claims.md;
check every claim for a falsifier and a
does-not-establish line in both files; check that
spec.md states the hypothesis (§1), the invariance
limit (§2), the four families (§3), the gate (§4),
the corpora (§5), the verdict discipline (§6), and
the kill criteria (§7); check that
records/registration-2026-11-27.md carries the
statistics, the bands, the gate legs, the verdict
rules with floors, and the corpus handling with pins.
*Pass:* the ids and order are equal (C110-1..C110-6);
every claim carries both lines; every registered
element is present in full.

**TC-110-02 — Control-validation recomputation
(C110-2; gate).** From the filed control-validation
record and raw output: recompute each transformation
corpus's designated family statistics from the filed
per-replication tables; check the gate legs' counts
against registration §4 (detection ≥ 4/5 per
designated pair; invariance no-fire ≥ 4/5;
false-positive ≤ 1 per family); check the band
derivation used control samples only, and that no
real-corpus figure appears anywhere in the gate's
inputs.
*Pass:* every recomputation equals the filed value;
each gate leg's outcome is the mechanical consequence
of §4 over the recomputed counts; the gate's inputs
are controls only.

**TC-110-03 — Execution recomputation (C110-3,
C110-4, C110-5, C110-6; execution).** From the filed
execution record and raw output: for each corpus,
recompute one statistic per family from the pinned
corpus under the registered handling (family A: A1;
family B: the omnibus JSD and its null percentile;
family C: the C2 gain and self-agreement for the
primary part pair; family D: V and hapax-type share);
recompute each family's verdict from the recomputed
figures under registration §5; check the Meroitic
band excludes Meroitic control samples; check every
PRESENT verdict is filed with its alternative
explanations.
*Pass:* recomputations equal the filed values; the
verdicts are §5's mechanical consequence; the
leave-target-out rule holds; the alternative
explanations are present wherever required.

**TC-110-04 — Trace and standing discipline (C110-6;
close).** Over the landing diff: check that no record
of any program's standings, verdicts, or tallies is
altered in content outside this study's own records
and the claims-ledger intake of C110-1..C110-6, and
that no record of this study presents a signature as
proof of deliberate intent.
*Pass:* the diff is confined as stated; the
proclamation scan returns zero hits.

**TC-110-05 — Kill-criteria evaluation (C110-1;
close).** Read the close record's kill-criteria
section: each of the five criteria of spec.md §7 is
tested against the study's filed outcomes in words,
with the per-family instances named where they apply,
and the state of each family (verdicts filed, closed,
or not testable) is stated.
*Pass:* all five evaluations are present and
traceable to the filed outcomes.

**TC-110-06 — Revision package form (C110-7;
revision registration).** Check the revision
bundle claims-revision.json carries exactly
C110-7..C110-11 in order, each with a falsifier and
a does-not-establish line; claims.md carries the
same five with falsifiers; the revision
registration carries its registered elements
(per-system bands, T-SHUF, the fixed-rank tail,
C2's retirement, the gate legs and seeds, the two
survey cautions, the uniform-substitution limit).
*Pass:* the filed script records/tc110-06-package-form.py
exits 0.

**TC-110-07 — Revision gate recomputation (C110-8;
revision gate).** Independently recompute the
revision gate from the registered seeds: the
per-system bands, every gate leg's counts, the
12-sample false-positive panel, family B's baseline
and legs, and the scoreability outcomes, using an
independent statistics implementation that imports
only the filed harness's corpus machinery.
*Pass:* every filed gate figure and outcome
reproduces; the filed script
records/tc110-07-08-revision-verification.py exits
0 on its gate section.

**TC-110-08 — Revision execution recomputation
(C110-9, C110-10, C110-11; revision execution).**
Independently recompute each real corpus's
statistics against the recomputed bands and
re-derive every filed verdict (and every filed
absence of a verdict) under the revision
registration's scoreability table and floors.
*Pass:* every filed verdict reproduces exactly;
the same filed script exits 0 on its execution
section.

**TC-110-04 and TC-110-05 apply at the revision
close** over the revision landing, in their filed
forms, with the revision's claims (C110-7..C110-11)
in the intake scope.
