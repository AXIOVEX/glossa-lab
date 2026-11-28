# Spec 109 — G1 Enriched-Objective Close Record (T104)

**Date:** 2026-11-27. **Scope closed:** the
enriched-objective amendment commissioned after the
scale study — G1's objective enriched with the
positional-consistency term built from G2's licensed
positional induction, and its temperature schedule
calibrated per corpus to the objective's own measured
swap-delta scale, preflighted at the same floors on
five fresh 1× corpora, with the identical preflight at
2× filed as a secondary diagnostic
(`records/g1-enriched-registration-2026-11-27.md`
carries the registration, the development, and the
verdict rule; `records/g1-enriched-preflight-2026-11-27.md`
carries the results; this record the test cases, the
kill evaluation, and the part state).

**Outcome: FAILED, clause (i)** — median recovery
0.719 against the 0.80 floor, as filed in the
preflight record §1. Clause (ii) passed (5/5
replications clear; median penalized margin
1,050.69 nats) and the shuffle control passed
(0.070 against the 0.360 bound). G1-E is not
licensed; G1 produces no scoreable output; Stage 3
remains blocked; the amendment commissions no second
revision; no floor moved.

## 1. TC-109-02 — Preflight conformance, re-run for this generator (PASS)

Executed as an independent verification script
(`records/g1-enriched-tc109-02-verification.py`,
SHA-256 `99075ba9…`) over the custody corpora and
both raw outputs: **PASS, 69/69 checks on the 1×
verdict run and 70/70 on the 2× diagnostic run**
(the additional check is the diagnostic-only flag),
payload exit 0 in both executions (logs in custody,
`glossa-custody/spec109/g1-enriched/run/` and
`…/run-2x/`). What it establishes, in the test
case's own terms:

- The Stage 1, G1-R, and enriched harness pins in
  each raw output match the filed files, and the
  frozen constants in each raw output match the
  registration (λ = 1.0; C_HI / C_MID / C_LO against
  δ̂_ref = 63.904459128199335; the search constants
  40 × 160,000, reheat 80,000, p_cycle 0.3,
  CALIB_K 2,000, α = 0.5, floor 0.80).
- Each corpus rebuilt from its seed of record by the
  harness's own admission path is byte-identical to
  the custody corpus the run filed; the 1× admission
  profile is exact (1,670 / 7,002 / 1,650 distinct),
  and at 2× the scale amendment's accounting
  recomputes (3,340 artifacts, distinct and fallback
  counts as filed, effective scale 1.995).
- Each filed candidate equals its run's best polished
  state; its enriched objective, base objective, and
  positional term rescore from the filed assignment,
  and the planted truth's objectives and both gaps
  recompute.
- δ̂ recomputes exactly under the registered
  calibration rule (the search's own preamble, same
  seeds), draws included, for every right and shuffle
  search.
- Each candidate's recovery (denominator 57 at every
  replication) and miss anatomy recompute to the
  filed figures; each penalized margin and null 99th
  percentile recomputes through the Stage 1 scorers
  with the filed seeds (the null's 999 margins
  included).
- The shuffle control is verified by deterministic
  re-execution of the identical enriched search on
  the rebuilt shuffled derivations — recovery and δ̂
  equal the filed figures in all ten executions (the
  shuffle candidate itself was not filed in the raw
  outputs; the verification is by re-execution, and
  the script and the preflight record say so).
- The summary medians and the verdict block
  recompute from the per-replication figures;
  clause (ii) is checked under both the harness's
  filed at-least-3-of-5 rule and the registration's
  median-replication form, which coincide on this
  run's figures.
- No undeciphered-system output exists in either raw
  output: this preflight produced none (see §2).

## 2. TC-109-09 — Program invariants (trace executed at landing)

Executed over this landing's diff: the changes are
confined to Spec 109's own records (the amendment
registration, the enriched harness, the verification
script, the preflight record, this close record, the
two raw-output copies), `tasks.md`, the history
ledger, and PROGRAM-STATE. No file of Specs 093,
097, 098, 102, 105, 107, or any other study is
touched; no gate is altered; the claims ledger does
not move (the amendment's claim determination,
registration §7: no new claim — the amendment
registers a generator design under C109-7's
revised-generator discipline as filed, and asserts
no new proposition); no standing, verdict, or tally
in any program changed. Nothing was deposited or
published. The trace passes on the landing's
read-back.

## 3. TC-109-10 — Kill criteria evaluated (spec.md §9, under the amendment §8 posture)

1. **Null yield at the frozen bar** — not engaged;
   it binds at Part 1's own stage over its
   candidates, which do not exist while the
   generator is unlicensed.
2. **Preflight failure** — **fires for G1-E.** The
   generator produces no scoreable output and Stage
   3 remains blocked. The amendment commissions no
   further revision; a further design is a new
   commission under a new registration.
3. **Control failure** — not fired. The shuffle
   control passed at 1× (0.070 against the 0.360
   bound) and in the 2× diagnostic (0.140 against
   0.386); the pipeline did not measure itself.
4. **Gate dependence** — not engaged.
5. **Integrity tripwire** — no breach of the study's
   substance; one filing defect, disclosed on the
   record in the preflight record §5: the amendment
   registration's first transfer to the worktree
   silently produced an empty file (a
   transfer-channel defect, the same defect that
   emptied the verification script's first transfer),
   discovered at verification time and repaired by
   re-filing the registration byte-identical to the
   authored text, hash-verified. The design freeze
   itself precedes the verdict run on the timestamped
   custody artifacts and the hash-pinned harness, as
   §5 of the preflight record sets out.

**Part 1 state after this preflight:** OPEN, BLOCKED
at its generator, unchanged in posture and now
sharper in diagnosis. Three generators have been
preflighted at the same floors on fresh corpora —
the filed search (0.772), G1-R (0.737), G1-E (0.719)
— and the scale study's conditional result stands
beside them (0.807 at 2× in basin-found terms, not
held at 4×). The two search-side repairs each held
the basin everywhere they were run, including at 2×
under calibration in this landing's diagnostic; the
binding constraint is the objective's edge-value
evidence at this corpus profile, and the strongest
verified structural channel the program has — the
positional induction, consumed in full distributional
form — is now measured to be insufficient as an
objective term against it. What a future Part 1
commission would need is a different evidence channel
or a different corpus profile, not a fourth search;
whether such a commission is raised is a program
decision above this record. Parts 2–5 are untouched:
Part 2's Stage 2 positional result stands (this
failure is the objective term's, not the
induction's), Part 3's channel result stands, and
Parts 4–5 keep their own registrations and gates.

**AI disclosure:** executed by an AI agent (Muse, via Muse)
at the direction of Tristen Pierson, per constitution sec. VI.
