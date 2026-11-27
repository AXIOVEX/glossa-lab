# Spec 107 — The Active Decipherment Loop, and Cycle 1
(I-1, M-1, E-1)

**Status: REGISTERED 2026-11-26 — the loop adopted and
cycle 1 commissioned by the owner's act of 2026-11-26
22:48 ET in the Glossa-Lab chat ("Adopt the loop and
commission cycle 1 as proposed"). This landing registers
the loop and the three cycle-1 tests. Execution follows
in this study's Stage 1, in the order and under the
registrations filed here and in Spec 101.**

**Provenance.** The design document *Active Decipherment
Design — Glossa-Lab (2026-11-26)*, filed in the goal
workspace (`files/active-decipherment-design-2026-11-26.md`),
built from the deep research report of 2026-11-26
(`~/workspace/research_notes/decipherment-methods-fixed-corpus-20261127-0337/report.md`)
and the multivariate signal inventory of 2026-11-26
(`files/multivariate-signal-inventory-2026-11-26.md`,
compiled from this repo at main head `8465d9eb`). The
owner adopted the design, commissioned I-1 and M-1,
commissioned Spec 101's execution (E-1), confirmed the
standing gates unchanged, and noted the Eteocypriot
ranking judgment, by the single act above, which took
all five decisions in the design's closing list as
proposed.

## 1. What this spec is

The three corpora are fixed; no new texts are coming on
any schedule the program controls. This spec registers
the operating discipline the design specifies — a
five-step loop that orders checkable sub-tests by
expected information gain per unit cost, with each
direction closed on the record when its information runs
out — and executes its first cycle: one test per program,
chosen by the design's Part 3 ranking.

**Honesty note, carried from the design.** No published
application of expected-information-gain ranking,
Bayesian optimisation, or active learning to
decipherment or epigraphy exists; the research report
searched and found none. The loop is a designed transfer
from adjacent fields (Bayesian experimental design;
active learning for phonotactics, SCiL 2024), its
components validated separately in their home fields. It
is an operating discipline, not a method with a
decipherment track record, and it is labelled that way
in every record this study files.

## 2. The loop (design Part 1, registered)

One cycle takes the top-ranked test from each program's
queue, executes it under its registration, updates the
program's hypothesis standings, re-ranks the queues, and
files the trace. Five steps, in order, every cycle.

**Step 1 — Explicit hypothesis sets, stated before any
test is ranked.** Each program carries a written
hypothesis set including the outcomes nobody is hoping
for; a test is rankable only if its outcomes discriminate
among members of the set.

- **Indus:** the script encodes a Dravidian language; an
  Indo-Aryan language; a Munda or Para-Munda language; a
  language of a lost or isolate family; or the system is
  not linguistic writing at all (the Farmer, Sproat &
  Witzel position, a live rival on this program's
  record). Absorbing verdict: **indeterminate at current
  evidence**.
- **Eteocypriot:** a pre-Greek isolate of Cyprus; related
  to one of the conjectured families on record (Hurrian,
  Etruscan/Lemnian, Semitic lines have all been
  proposed); or the surviving corpus is too thin for any
  affiliation question to be posed. Absorbing verdict:
  **too thin to test**.
- **Meroitic:** affiliation with Northern East Sudanic
  (Rilly's position, the program's R1 set); with
  Afroasiatic (the R2 side, Rowan's phonotactic argument
  among its supports); or an isolate for testing
  purposes (the R3 null of the Stage 4.2 design).
  Absorbing verdict: **undecidable at this power** (the
  standing Stage 4.2 verdict, until a test with adequate
  power displaces it).

The hypothesis sets live in the ELSEWHERE baseline
templates (Spec 106: Indus 88 axioms, Eteocypriot 71,
Meroitic 76, as corrected by the 2026-11-26 errata). A
cycle's seed record names at least one hypothesis under
which the registered prediction fails (the Round N
lesson: an ensemble whose contact point exercises axioms
present in every instance returns a conditional logical
result, not an evidentiary test). A test that cannot
fail under any carried hypothesis is not registered.

**Step 2 — Candidate analyses registered in advance,
each with its falsifier.** Registration follows the
research report's falsifiability checklist, applied to
every test type: (1) the item set is fixed in advance,
its size stated as the power denominator, with effective
N reported in the units that actually bind; (2) the
prediction is stated before scoring — what pattern, in
which direction, at what minimum size; (3) the null is
stated — a structure-preserving permutation or shuffle
distribution and, where a family or language model is
involved, a wrong-family or wrong-language control run
through the identical pipeline; (4) borrowing and
contamination strata are identified and handled before
scoring, and every split is duplicate-aware (no sequence
on both sides); (5) the verdict rule is stated in
advance, with three outcomes always available —
positive, negative, and indeterminate at the stated N. A
registration whose verdict rule has no indeterminate
outcome is refused.

**Step 3 — Ranking by expected information gain per
unit cost, with the sensitivity printed next to the
ranking.** Likelihoods are elicited judgments, recorded
in the cycle's ranking record with author and date. The
ranking is never published naked: the likelihood
assignments are perturbed across the range the program
regards as plausible, and the record states whether the
top-ranked test survives. Where the ranking flips under
plausible perturbation, the record says so; a ranking
that only holds under one fragile assignment is treated
as no ranking, and the tie is broken by cost (cheapest
first) and gate-readiness. Cycle 1's ranking record,
with its sensitivity statements, is
`records/cycle-1-registration-2026-11-26.md` §1.

**Step 4 — Blinded or held-out scoring wherever the
test allows**, in this order of preference: (1) held-out
scoring on a sealed or procedurally excluded split whose
seal is intact (the Indus sandbox reserve's seal is
spent; no entry pretends otherwise); (2) split-half
prediction; (3) out-of-stratum prediction; (4) arithmetic
or structural self-checks; (5) scramble controls — the
identical pipeline on a scrambled or wrong-language
corpus of the same shape must fail. Where none of the
five is available, the test is not registered.

**Step 5 — The posterior trace, with stopping rules.**
Each cycle closes by filing, per program: the ranking
record (with sensitivity), the executed tests' outcome
records, and an updated hypothesis-standing note stating
what moved, what did not, and the current standing of
every hypothesis in the set, including the absorbing
verdicts. The existing registered gates consume the
trace unchanged: G-IND, G-ETE, and G-MER have executed at
their registered licenses, and Specs 100, 101, and 102
keep their own gate conditions, which this loop does not
amend, waive, or route around. (Spec 101 is executed in
cycle 1 under its own registration, on the owner's
commission; that is its gate opening as registered, not
a waiver.)

Stopping rules, per direction (a hypothesis paired with
the tests that discriminate it): a direction closes
**supported** or **refuted** only at its registered
verdict rule; closes **indeterminate** when the power
calculation at the available N shows the minimum
detectable effect is larger than any effect the
hypothesis plausibly predicts; closes **exhausted** when
every remaining queued test that discriminates it is
blocked on a named external input, reopening only when
that input arrives.

**Progress.** Every cycle runner emits timestamped
progress indicators (tests completed of tests in the
cycle, with the current test named), per the program's
standing constraint of 2026-11-26.

## 3. Cycle 1 — the three tests

The full registrations are filed at
`records/cycle-1-registration-2026-11-26.md`. In brief:

- **I-1 (Indus) — scramble-simulation identifiability
  calibration.** What could any method of the kind this
  program runs extract from a corpus shaped like the
  Indus corpus (1,670 short artifacts, 7,002 tokens, the
  empirical length distribution and duplication rate)?
  Two donor corpora of known structure (Meroitic, from
  the pinned Kovetsky build; Latin, from a pinned
  public-domain text) are reshaped to the Indus profile,
  ciphered, and attacked with the program's own
  statistics — the G-IND-form predictor comparison
  (right-model, wrong-model, and shuffle conditions) and
  the L3 positional statistics — at 0.5×, 1×, and 2×
  scale, 20 replications per cell. Verdict rule,
  falsifier, and standings effects as registered there
  §2. Cost: tower compute.
- **M-1 (Meroitic) — stratum-conditioned structural
  recomputation.** Are the corpus-wide structural facts
  (adjacency structure, positional classes, the a-sign
  conformance 725/737 = 98.4% and the i-sign conformance
  2,857/2,880 = 99.2%) properties of the language, or
  artifacts of pooling a formula-dominated funerary
  majority with everything else? Recomputed within genre
  strata over the pinned build, on two populations (the
  sandbox row population, whose pooled figures must
  reproduce the filed tables exactly, validating the
  join; and the campaign's frozen partition population,
  whose strata counts must reproduce the filed counts),
  with out-of-stratum prediction. Verdict rule,
  falsifier, and standings effects as registered there
  §3. Cost: tower compute. The Otten corpus is not an
  input; nothing in this test consumes it.
- **E-1 (Eteocypriot) — Spec 101 executed as
  registered.** The postdictive occurrence test of
  ICS 196 ending candidates in ICS 194/195 under
  Perna 2019, under Spec 101's registration and its
  binding floor record, unamended: preconditions
  P-1..P-3 in stage order, floors computed by the floor
  record's §1.3 formula, SUPPORTED only on both
  conjuncts of §1.5, the target standing as declared
  under OD-D-1 — **enrichment**, expressly not a
  recurrence finding — and the exposure statement
  carried verbatim in the outcome record. Its stages,
  records, and test cases are Spec 101's own
  (TC-101-01..TC-101-06); this spec's C107-4 and
  TC-107-04 stand on their results. Cost: desk.

**What cycle 1 deliberately does not do** (design
Part 3): it does not run Spec 102 (blocked on a delivery
and a commission, gates untouched), does not touch
Spec 100's gate (no reply from Miller), does not reopen
Spec 103, T502/T503, or the quantum arm of Spec 104
(owner-closed), and does not refresh the Spec 096 freeze
pin (instruction withdrawn on the record).

## 4. Limits and kill criteria (design Part 4, registered)

The loop generates no new information; it optimizes the
order in which the existing evidence is interrogated.
The Indus anchor problem (1 of 94 strict-core anchors
independently sourced) and the Eteocypriot corpus floor
(69 development tokens) remain exactly as they stand.
The ranking numbers are argued orderings, not
measurements. LLMs and general AI tools are excluded as
scorers, adjudicators, and validators under this loop;
they may generate candidate hypotheses and draft
analysis code, each then tested under §2's rules.

**Kill criteria** — any one closes the loop on the
record:

1. **Information exhaustion:** two consecutive cycles in
   which no queued test in any program has an expected
   information gain above the registration threshold the
   cycle record sets.
2. **Total blockage:** every remaining discriminating
   test in all three programs is blocked on a named
   external input.
3. **Ranking collapse:** the cycle ranking flips under
   every plausible likelihood perturbation the program is
   willing to record.
4. **Null yield:** a full cycle executes and no outcome
   moves any hypothesis standing by the minimum the
   cycle's registration set in advance (one null cycle is
   data; the criterion is stated in advance so that a
   second is a decision).
5. **Integrity tripwire:** any breach of a custody term,
   a gate condition, or the registration discipline (an
   unregistered analysis entering the trace, a seal
   mishandled, restricted bytes used beyond their terms)
   halts the loop immediately, on the program's standing
   rule, until the breach is recorded and the owner
   rules.

If the loop is killed, the programs return to their
pre-loop posture — records maintained, external inputs
watched, owner-gated items awaiting his word — with the
loop's trace standing as the account of what the fixed
corpora were asked and what they answered.

## 5. Decisions

- **D-107-1 (number).** At the check of 2026-11-26 the
  highest landed spec package on origin/main was 106
  (`specs/106-elsewhere-world-model-templates/`); no 107
  directory, branch, or open pull request carried 107.
  This package takes 107.
- **D-107-2 (taxonomy).** Spec 107 sits under Program
  infrastructure / Governance, lifecycle & generated
  layers, with Specs 104 and 106: it is program method,
  not a language study. Its cycle-1 tests are executed
  for the three language programs but registered as this
  study's claims, in the pattern of Spec 106 (D-106-2).
- **D-107-3 (no recommendations-ledger row).** The
  study's provenance is the owner's direct adoption act,
  not a Co-scientist recommendation; as with Specs 104
  and 106, no row is added.
- **D-107-4 (E-1's home).** E-1's execution records land
  in Spec 101's own package (its corpus state, candidate
  registration, freeze addendum, outcome record), because
  Spec 101's registration fixes their places; this spec
  carries the cycle trace and the posterior standings,
  and cites Spec 101's records for the test itself.
- **D-107-5 (custody).** I-1's donor B text and all
  simulation intermediates are held in custody on
  tower-compute under `glossa-custody/spec107/` and never
  committed, in the pattern of D-105-8; the filed records
  carry the donor pins (source, SHA-256) so any reader
  can re-acquire the identical bytes. The Kovetsky build
  is read at its pin and never modified. No Otten-corpus
  byte is an input to any cycle-1 test.

## 6. Stages

- **Stage 0 — Registration (this landing).** The loop,
  the cycle-1 ranking record with sensitivity, the three
  test registrations, the claims intake, and the
  mechanical audits of TC-107-01.
- **Stage 1 — Cycle 1 execution.** I-1, M-1, and E-1
  executed under their registrations; outcome records
  filed; the posterior trace and the kill-criteria
  evaluation filed at cycle close (records/
  cycle-1-outcome-2026-11-26.md and
  records/cycle-1-trace-2026-11-26.md).
- **Stage 2 — Cycle 2 (COMMISSIONED 2026-11-27 by the
  owner's keep-working directive in the Glossa-Lab
  chat).** Registered at
  records/cycle-2-registration-2026-11-27.md: I-2
  (positional recovery at realistic restriction
  levels), the C-E-15 feasibility decision with E-2
  gated behind it, and M-2 (the phonotactic battery).
  Tasks T201–T206.

## 7. Standing

Registration moves no standing, verdict, or tally in any
program. Cycle 1's standings effects, if any, are
exactly those the three registrations license, and are
stated in the cycle-1 trace against the outcome records
that license them.

**AI disclosure:** executed by an AI agent (Muse, via Muse)
at the direction of Tristen Pierson, per constitution sec. VI.
