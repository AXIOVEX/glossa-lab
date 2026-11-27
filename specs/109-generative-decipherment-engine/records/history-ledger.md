# Spec 109 — History Ledger

Opened live at registration, 2026-11-27. Entries are
appended in order; none is edited after the fact.

**2026-11-27 — Registration.** The owner's directive
in the Glossa-Lab chat (~13:54 ET) rejected a
verification-only posture for the program and ordered
the program made capable of attempting decipherment —
to solve, not only to find mistakes — under his
standing blanket approval for Glossa work of the same
day (04:05 ET: "Yes do all these things now or take my
approval now to do at the best time") and his
keep-working directive. This package registers the
discovery side as Spec 109: the shared conformance
preflight (OD-O-1 pattern), five generative parts
(assignment search; sign-class and structure
induction; the context channel; Meroitic gloss
induction, gated on Spec 102; Eteocypriot reading
candidates), the frozen judging rule of Spec 098 used
as filed, and the study's kill criteria. Generation
and adjudication are registered as separate: the
engine proposes ranked candidate sets with margins,
the existing frozen gates dispose, and registration
moves no standing, verdict, or tally in any program.
The study's provenance is the owner's direct
directive; per D-109-3 no recommendations-ledger row
is added. Decisions D-109-1..D-109-5 are recorded in
spec.md §11, including the number check (highest
landed package on origin/main: 108; the one open pull
request at the check, #799, carries Spec 107 material
only) and the taxonomy placement with Specs 104, 106,
and 107.

**AI disclosure:** entries in this ledger are written
by an AI agent (Muse, via Muse) at the direction of
Tristen Pierson, per constitution sec. VI.

## 2026-11-27 — Spec 109 registered and landed

The registration package and the claims intake cascade landed as one
PR (branch `spec-109-registration`): registration commit `ab783146`
and its completion commit. The cascade record
(`records/registration-cascade-2026-11-27.md`) carries the executed
figures and the serialization disclosure: the cascade first executed
over the 1,123-line build and was superseded unmerged when PR #799
and PR #800 landed first, then re-executed in full over the merged
build — ledger 1,124 → 1,133 lines (canonical `542c7fa2…`), 1,088
claims, pin re_derivations[30], the T405 pair re-executed byte-equal,
the superseded generation departed under §7.1, the ledger gate at
32 PASS / 0 FAIL / 1 NOT-RUN over the final tree. No standing moved.
Stage 0 closes with this entry; the next stage is Stage 1
(preflight), uncommissioned.

**2026-11-27 — Stage 1 executed (T101): the
conformance preflight.** Executed the same day under
the owner's blanket approval and keep-working
directive, in a fresh worktree on tower-compute
(`spec-109-stage-1-preflight`); the full record is
`records/stage-1-preflight-2026-11-27.md` and the
close is `records/stage-1-close-2026-11-27.md`. The
harness ran five synthetic replications at the exact
Indus profile with planted positional classes,
segmentation, partials, context structure, and
sign-value structure; clause (iii) re-ran Spec 107's
filed I-2 execution unchanged, reproducing cycle 2's
medians to four decimals for both donors (RIGHT above
WRONG and SHUFFLE; verdict INDETERMINATE, the
registered configuration), and reproducing the
positional limitation on the re-run's own ground
truth (Meroitic 1 mark, Latin 0, against the floor of
5 — positional recovery on those controls NOT
MEASURABLE, the clause run on the synthetic controls
as registered). Verdicts: **G3 (context channel)
PASSED** in full and is licensed for Stage 2. **G2
(structure induction) PASSED for its positional and
numerical families** (recovery 1.000, controls
0.000) and **FAILED for segmentation** (F1 median
0.569 at the 0.80 floor; shuffle control 0.443, 78%
of its true rate) **and for recurrent partials on
the control at the boundary** (recovery 1.000;
control 0.500 against the required < 0.500). **G1
(assignment search) FAILED clause (i)**: median
recovery 0.772 at the 0.80 floor (per-replication
0.614–0.825), while its margin clause passed 5/5 at
a median penalized margin of 933.2 nats — the
objective discriminates the planted truth
decisively; the search does not reliably find it.
Kill criteria 2 and 3 fired for the failed
generators and families, which produce no scoreable
output until revised generators pass under new
registrations; no floor was moved. TC-109-02
recomputed every filed figure from custody: PASS,
38/38. No undeciphered-system output was produced or
scored; no standing, verdict, or tally moved.
Stage 2 is licensed in part (Part 2 positional and
numerical families, Part 3 channel); Stage 3 is
blocked at its generator.

## 2026-11-27 — G1 revision executed (T102): re-preflight FAILED, clause (i)

The Stage 1 close left Part 1 blocked at its generator,
with the margin anatomy as the revision's starting
evidence. The revision was executed the same day under
the owner's blanket approval and keep-working directive,
in a fresh worktree on tower-compute
(`spec-109-g1-revision`). The diagnosis, run over a
restart-by-restart reproduction of the filed Stage 1 run
(the filed hits reproduce exactly: 47/44/40/45/35 of 57),
separated two mechanisms: the objective's near-optimal
plateau in the edge values (the filed best states beat
the planted truth's objective by +26 to +50 nats on four
corpora while missing 10–17 signs, all edge values in
short cycles; the constraints exclude no planted value
anywhere) and one basin failure (the fifth corpus's best
found state 497.7 nats below truth at a swap-local
optimum). Two refinement forms (fixed-temperature
sampling marginals; modal aggregation over the optima)
were built, measured, and set aside on the record — the
first dilutes the optima, the second collapses to the
argmax state on every corpus probed. The revised
generator G1-R (40 restarts × 160,000 steps; swaps and
3-cycle rotations; one reheat; per-restart polish; the
objective, constraints, scoring, and floors identical)
was registered as an amendment
(`records/g1-revision-registration-2026-11-27.md`; the
claim determination at its §6: no new claim, C109-7 as
filed carrying the revised-generator pattern) and
re-preflighted on five fresh corpora
(`spec109-s1r-synth-{1..5}`). **Verdict: FAILED, clause
(i)** — median recovery **0.737** at the 0.80 floor
(0.632 / 0.684 / 0.807 / 0.737 / 0.772); clause (ii)
passed 5/5 at a median penalized margin of 990.1 nats;
the shuffle control passed (0.175). The basin defect is
repaired on fresh material (candidate objective above
the planted truth's on all five corpora, by +20 to +57
nats); the plateau is the binding constraint — at this
profile the objective does not identify a fifth to a
third of the edge values, and no search over it recovers
what it does not carry. TC-109-02 re-run for this
generator: PASS, 45/45, every figure recomputed
independently and the verdict mechanical. Kill
criterion 2 fired for G1-R; the floor was not moved; the
amendment commissions no second revision. G1 produces
no scoreable output; Stage 3 remains blocked; no
standing, verdict, or tally moved.
