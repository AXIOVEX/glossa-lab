# Spec 109 — Plan

## Shape

The package mirrors Specs 104, 106, and 107: spec.md
states the study; claims.md and aee-claims.json carry
the nine claims in the program's claim form; the full
registrations for the shared preflight and the five
parts are filed at registration
(records/registration-2026-11-27.md), because the
program's discipline is that registration precedes
execution. The history ledger opens live at
registration. The method of work follows the program's
stack governance as the source of truth for how the
programs work; where this study's execution proves a
practice the stack does not yet carry, the evidence is
filed in this study's records for the stack's own
change discipline, and this study does not depart from
the stack silently in the meantime.

## Stage 0 — Registration

- **T001.** Write the package: the engine and its
  separation rule (spec.md §§1–4), the held-out
  discipline (§5), the iconography statement (§6), the
  relations to standing gates (§7), provenance (§8),
  kill criteria (§9), the nine claims with falsifiers,
  the test cases, and the registration record with the
  execution order and its sensitivity statements.
- **T002.** Record the owner's directive of 2026-11-27
  ~13:54 ET (the discovery side ordered; the
  verification-only posture rejected) and the standing
  blanket approval of 2026-11-27 04:05 ET in the
  history ledger.
- **T003.** Intake the claims through the sanctioned
  importer; place the study in the taxonomy (Program
  infrastructure / Governance, lifecycle & generated
  layers, D-109-2); run the settling chain in standing
  order (verify-canonicals 6/6 before the pin moves;
  the T405 pair re-executed with byte-equal result
  blocks; the comparison re-filed; assignment sets
  re-materialized; the canonical pin refreshed as a new
  re_derivations entry; the superseded generation's
  departure acts appended in the completion commit);
  regenerate the generated layers; update the census
  pins from the regenerated actuals; file the
  registration cascade record with the executed figures;
  run TC-109-01.

## Stage 1 — Preflight

- **T101.** Build the preflight harness on
  tower-compute over the Spec 107 simulation machinery:
  synthetic cipher corpora at the Indus profile with
  planted assignments; the Latin and Meroitic controls
  at their custody pins; two independent
  implementations of every recovery figure. Run the
  preflight for the Indus generators (Parts 1–3 share
  the harness). File the preflight record with each
  clause's result, the positional limitation carried on
  its face, and the two-implementation agreement
  statement. Run TC-109-02. No undeciphered-system
  output is scored in this stage.

## Stage 2 — Structure induction and context channel

- **T201 (Part 2).** File the part's freeze (constants
  marked FREEZE in registration §3; effective Ns).
  Run the four induction families over the full corpus;
  compute stability (split-half; per-site for
  positional classes over T202's join); open the
  generated-hypotheses register in custody; file the
  induced structures to the existing gates under those
  gates' own registrations. File the outcome record;
  run TC-109-04.
- **T202 (Part 3).** Build and validate the two joins
  (population site join; Spec 093 census join — STOP
  on either validation mismatch); compute the context
  term and its null; run the out-of-site validation;
  file the channel record with its verdict and the
  no-iconography label. Run TC-109-05.

## Stage 3 — Assignment search

- **T301 (Part 1).** Execute the registered freeze
  sequence in order (constraint set versioned; value
  inventory closed; 109 reserve cut duplicate-aware and
  hash-committed; search schedule registered). Run the
  search on tower-compute with timestamped progress
  output; select the top-K; open the reserve once and
  adjudicate under the frozen decide() rule; file the
  ranked candidate set, the per-candidate margins and
  free-choice counts, and the outcome record. Run
  TC-109-06 and TC-109-03 (replay).

## Stage 4 — Eteocypriot reading candidates

- **T401 (Part 5).** Run the Eteocypriot generator's
  preflight clauses (synthetic syllabary-profile
  corpora; the name-anchor control). File the part's
  freeze (comparanda closed; the E-2 component drop
  restated). Generate and rank per text; recompute the
  ranking under the permutation null; file the ranked
  sets and the outcome record, carrying no licensing
  language. Run TC-109-07 and TC-109-03.

## Stage 5 — Meroitic gloss induction

- **T501 (Part 4).** Gated: when Spec 102's
  digitisation has landed and its freeze exists, file
  the part's freeze from Spec 102's frozen vocabulary
  and family sets; generate distributional profiles and
  candidate glosses; score on the 33 held-out texts
  against the null and the wrong-family control; file
  the ranked gloss candidates and the outcome record.
  If Spec 102 closes NOT ADMINISTERED, file NOT
  ADMINISTERED — INPUT GATE UNMET and close the stage.
  Run TC-109-08 and TC-109-03.

## Stage close discipline (all stages)

Each stage closes with: its outcome records filed; its
test cases run with results filed; a kill-criteria
check for the legs it ran, against spec.md §9, filed in
the stage-close record (TC-109-10); a trace statement
per program — what moved, under which licensing record,
or that nothing moved (TC-109-09, executed at
pull-request time over the stage's landing diffs); and
PROGRAM-STATE updated.

## Venues and discipline

Registration lands from a fresh worker worktree on
tower-compute under `~/.syncyard/worktrees/glossa/`, on
the study branch. Execution runs on tower-compute in
the same pattern; custody bytes (candidate records,
search intermediates, synthetic corpora) live under
`glossa-custody/spec109/` and are never committed.
Every pull request merges only on genuine per-job CI
green (10/10); the known Spec 095 T404 timing flake's
reruns are disclosed where they occur; branches are
deleted in the same motion as their merges. Every job
emits timestamped, countable progress indicators.

## Risks named in advance

- The assignment search's free-choice accounting is
  severe by design: at 2 nats per searched sign, a
  candidate assigning many signs starts hundreds of
  nats down. That is the frozen rule's honest price for
  generation, and the expected first outcome is SEARCH
  NEGATIVE. The registration is written so that outcome
  is a finding, not a failure of nerve.
- The value inventory is bounded by the World Language
  Graph as filed: if the true language is outside the
  graph's dossiers, the search cannot find it, and the
  freeze record says so on its face (the Indus gap
  entry, S0/L0, blocker INFORMATION).
- Part 2's segmentation constants are judgment calls;
  they are fixed at the part's freeze so the run cannot
  tune them, and stability failure is filed, not
  repaired in flight.
- Part 4's stage may never execute: its input is a
  print book in transit with no delivery estimate, and
  its gate may close unmet. The stage is registered so
  that either outcome is a record, not a surprise.
