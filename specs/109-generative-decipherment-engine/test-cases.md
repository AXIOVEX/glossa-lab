# Spec 109 — Test Cases

Each test case names the claim it exercises, its
procedure, and its pass condition. Stage 0's acceptance
test is TC-109-01; the remaining test cases execute
with their stages and their results are filed in the
stage outcome records. TC-109-01 is re-run over the
amended package at every later registration landing of
this study.

**TC-109-01 — Package form (C109-1; Stage 0).**
Parse the package's bundle file (aee-claims.json);
compare its claim ids and order against claims.md;
check every claim for a falsifier and a
does-not-establish line; check that spec.md §3 states
the five parts, §2 the preflight, §4 the judging rule,
§6 the iconography statement (what exists, what does
not, what acquisition requires), and §9 the five kill
criteria; check that records/registration-2026-11-27.md
carries a registration for each part with its verdict
rule and its information row.
*Pass:* the ids and order are equal (C109-1..C109-9);
every claim carries both lines; the five parts, the
preflight, the judging rule, the iconography statement,
and the kill criteria are stated in full; each part's
registration is present with a three-outcome verdict
rule.

**TC-109-02 — Preflight conformance (C109-7;
Stage 1, and re-run for each later generator).** From
the filed preflight record: verify the synthetic
corpora's profile parameters against the filed
censuses; verify the control pins; recompute each
recovery figure from the filed per-corpus results;
check the two implementations' agreement statement
covers every ground-truth set and figure; check the
record carries the Latin/Meroitic positional
limitation on its face and claims no positional figure
from those controls; check that no undeciphered-system
scoring output of the generator exists anywhere in the
landing predating the preflight record.
*Pass:* every recomputation equals the filed value;
the verdict (PASSED / FAILED / NOT MEASURABLE IN PART)
is the mechanical consequence of registration §2's
floors over the recomputed figures; the limitation is
carried as stated.

**TC-109-03 — Replay conformance (C109-8; every stage
that files candidates).** Select the stage's filed
candidate records from custody by their pins in the
outcome record; replay the generation from the records
(generator pin, state, seed, data pins, constraint-set
version); compare the replayed candidate set and
margins against the filed ones.
*Pass:* the replayed set is identical — same
candidates, same order, same margins — and every
candidate record carries every provenance field.

**TC-109-04 — Part 2 induction conformance (C109-3;
Stage 2).** From the filed Part 2 freeze and outcome
record: verify the corpus pins; recompute one family's
filed structures from the filed intermediate tables
(the positional family: per-mark positional shares and
restriction calls at both ρ levels); verify the
induction's overlap with the filed L3 table is
reconciled as the registration requires (reproduction
or a filed divergence finding); verify every filed
structure carries its stability results and its
provenance, and that no STABLE structure lacks a
gate filing reference.
*Pass:* recomputations equal the filed values; the
part's verdict is the mechanical consequence of
registration §3's rule over the filed stability
results.

**TC-109-05 — Part 3 channel conformance (C109-4;
Stage 2).** From the filed channel record: verify both
join validations reproduce the filed censuses exactly
(the population site census; the Spec 093 census: 179
pairs, Steatite 176, Clay 1, Faience 1, 1 empty
sentinel) or that a STOP is filed instead; recompute
the context term for one filed candidate from the
filed join tables; verify the term's filed contribution
never exceeds its null's 99th percentile; verify no
iconography input appears in any join, and every filed
context score carries the no-iconography label.
*Pass:* all checks hold, and the channel verdict is
the mechanical consequence of registration §4's rule
over the filed validation figures.

**TC-109-06 — Part 1 search conformance (C109-2;
Stage 3).** From the filed freeze record, run index,
and outcome record: verify the freeze sequence's order
and timestamps (constraint set and inventory closed
before the reserve's hash commitment; the commitment
before any search run; every search run after the
commitment); verify the reserve was opened exactly
once, at scoring; recompute each filed candidate's
penalized margin from the filed per-sign held-out
counts under the frozen decide() rule, with the
free-choice count charged at 2 nats per searched
assignment; verify each candidate's provenance is
complete; apply the registered bar to the recomputed
margins.
*Pass:* every recomputation equals the filed value,
and the filed outcome is the bar's mechanical
consequence over the recomputed margins.

**TC-109-07 — Part 5 ranking conformance (C109-6;
Stage 4).** From the filed freeze and outcome record:
verify the comparanda set equals the registered closed
set (with the derivation-tables reduction stated if it
applies); recompute the ranking for one text from the
filed candidate records under the registered
lexicographic rule (components (1) and (2) only);
verify the permutation-null recomputation is filed and
the part's verdict follows from it; scan the part's
records for licensing language, any "all checks
passed" statement, and any resolution or presumption
of OD-O-2.
*Pass:* the ranking recomputes exactly; the verdict is
registration §6's mechanical consequence; the scan
returns zero hits.

**TC-109-08 — Part 4 conformance / gated
non-execution (C109-5; Stage 5).** If Spec 102's
freeze exists: read the Part 4 outcome record; verify
the vocabulary consumed is Spec 102's frozen
vocabulary exactly (hash against the freeze record);
verify the ASJP/family sets are the freeze's; recompute
the verdict from the filed per-form values under
registration §7's rules, including the wrong-family
control's figures; verify no Spec 102 gate figure is
restated in amended form anywhere in the part's
records. If Spec 102 closed NOT ADMINISTERED: check
that no Part 4 execution record or scoring output
exists anywhere in the landing and that the stage-close
record carries NOT ADMINISTERED — INPUT GATE UNMET as
the part's outcome.
*Pass:* in the executed case, the verdict recomputes
as stated and the gates stand untouched; in the gated
case, the non-execution is complete as stated.

**TC-109-09 — Trace and standing discipline (C109-9;
every stage, executed at pull-request time).** Over
every landing diff of the stage: check that no record
of any program's standings, verdicts, or tallies is
altered in content outside this study's outcome
records and the licensing records of existing gates,
and that every standings effect named in the
stage-close record cites its licensing outcome record.
*Pass:* the diffs are confined as stated, and the
stage-close citations are complete.

**TC-109-10 — Kill-criteria evaluation (C109-1;
every stage close).** Read the stage-close record's
kill-criteria section: each of the five criteria of
spec.md §9 is tested against the stage's filed
outcomes in words, with the per-part instances of
registration §§3–7 named where they apply, and the
state of each part (open, closed with the criterion
named, or gated) is stated.
*Pass:* all five evaluations are present, each is
traceable to the filed outcomes, and every part's
state follows from them.
