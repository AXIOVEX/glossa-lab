# Spec 109 — Tasks

## Stage 0 — Registration

- [x] T001 Package written (spec.md, claims.md,
  aee-claims.json, plan.md, test-cases.md, this file,
  records/registration-2026-11-27.md,
  records/history-ledger.md opened live).
- [x] T002 Owner's directive of 2026-11-27 ~13:54 ET
  and the standing blanket approval of 2026-11-27
  04:05 ET recorded in the history ledger.
- [x] T003 Claims intaken; taxonomy placed; settling
  chain run in standing order; generated layers
  regenerated; census pins updated from actuals;
  registration cascade record filed with executed
  figures; TC-109-01 run.

## Stage 1 — Preflight

- [x] T101 Preflight harness built on tower-compute;
  preflight run for the Indus generators (Parts 1–3);
  preflight record filed with per-clause results, the
  positional limitation on its face, and the
  two-implementation agreement statement; TC-109-02
  run. No undeciphered-system output scored.
  Executed 2026-11-27: G3 PASSED; G2 passed for its
  positional and numerical families and failed for
  segmentation and (on the control) partials; G1
  failed clause (i). Records:
  records/stage-1-preflight-2026-11-27.md and
  records/stage-1-close-2026-11-27.md.

- [x] T102 G1 revision: the Stage 1 failure diagnosed
  from the filed raw output and the custody corpora
  (two mechanisms: the objective's near-optimal plateau
  in the edge values, and one basin failure); the
  revised generator G1-R registered as an amendment
  (records/g1-revision-registration-2026-11-27.md; no
  new claim — the determination is filed at its §6);
  the re-preflight executed on five fresh corpora
  (seeds spec109-s1r-synth-{1..5}) at the same floors;
  TC-109-02 re-run. Executed 2026-11-27: **FAILED,
  clause (i)** — median recovery 0.737 against the 0.80
  floor (per-replication 0.632-0.807); clause (ii)
  passed 5/5 (median penalized margin 990.1 nats) and
  the shuffle control passed (0.175). The basin defect
  is repaired (candidate objective above the planted
  truth's on all five fresh corpora); the plateau is
  the binding constraint. G1 remains unlicensed; Stage
  3 remains blocked; no second revision is commissioned
  by the amendment. Records:
  records/g1-revision-preflight-2026-11-27.md and
  records/g1-revision-close-2026-11-27.md.

- [x] T103 G1 identifiability-scale study: the G1-R
  preflight re-run at 2x and 4x corpus scale under a
  registered amendment
  (records/g1-scale-registration-2026-11-27.md; no
  new claim — the determination is filed at its
  section 6), five fresh corpora per scale (seeds
  spec109-scl2-synth-{1..5},
  spec109-scl4-synth-{1..5}), the generator,
  objective, scoring, and floors identical, the
  scale definition's two combinatorial
  accommodations on the record (the length-2 stem
  pool saturates at the 529-pair inventory maximum;
  distinctness falls back at length-2 slots only,
  with F and the effective scale filed per corpus);
  TC-109-02 re-run in verification form (PASS
  119/119). Executed 2026-11-27: **MIXED** — median
  recovery 0.807 at 2x (the floor crossed) and 0.772
  at 4x (not held); clause (ii) passed 5/5 at both
  scales and the shuffle control passed at both.
  Basin failures returned at scale (negative
  objective gaps in 1 of 5 replications at 2x and 2
  of 5 at 4x, carrying all of the study's stem
  misses), while in basin-found replications the 1x
  plateau anatomy persists (stems 0; edge-only
  misses of 8-15 at gaps of +30 to +97 nats).
  Neither (A) information nor (B) objective design
  is supported in its clean form. G1 remains
  unlicensed; Stage 3 remains blocked; no floor
  moved. Records:
  records/g1-scale-study-2026-11-27.md and
  records/g1-scale-close-2026-11-27.md.

- [x] T104 G1 enriched objective: the plateau attacked
  with the program's strongest verified structure —
  the objective enriched with a positional-consistency
  term built from G2's licensed positional induction
  (full distributional form, on both sides of the
  assignment; the planted assignment never read), the
  weight chosen on development corpora by a registered
  grid and selection rule (λ* = 1.0), and the search's
  temperature schedule calibrated per corpus to the
  objective's own measured swap-delta scale (δ̂;
  constants frozen against δ̂_ref = 63.9045);
  registered as an amendment
  (records/g1-enriched-registration-2026-11-27.md; no
  new claim — the determination is filed at its §7);
  the preflight executed on five fresh corpora (seeds
  spec109-s1e-synth-{1..5}) at the same floors, with
  the identical preflight at 2x filed as a secondary
  diagnostic (seeds spec109-s1e2-synth-{1..5});
  TC-109-02 re-run for this generator (PASS 69/69 at
  1x, 70/70 at 2x). Executed 2026-11-27: **FAILED,
  clause (i)** — median recovery 0.719 against the
  0.80 floor (per-replication 0.684-0.772); clause
  (ii) passed 5/5 (median penalized margin
  1,050.69 nats) and the shuffle control passed
  (0.070). The calibrated search held the basin on
  all five verdict corpora and on all five diagnostic
  corpora at 2x (no basin failures; the scale study's
  2x basin failure does not recur in this draw); the
  enriched objective's near-optimal region still
  contains non-truth assignments, the misses
  edge-only (stems 0 in all ten replications). G1
  remains unlicensed; Stage 3 remains blocked; the
  amendment commissions no second revision. Records:
  records/g1-enriched-preflight-2026-11-27.md and
  records/g1-enriched-close-2026-11-27.md.

## Stage 2 — Structure induction and context channel

- [x] T201 Part 2 executed under registration §3 for
  the families the Stage 1 preflight licensed
  (positional classes and numerical/metrological;
  segmentation and recurrent partials not licensed
  and not run): freeze filed; induction run; stability
  computed; generated-hypotheses register opened;
  108 STABLE structures filed to Spec 091's anchor
  comparison; outcome record filed; TC-109-04 run.
  Verdict POSITIVE (positional family; the numerical
  family's three checks not supported, stably).
  Records: records/stage-2-freeze-2026-11-27.md,
  records/stage-2-part2-outcome-2026-11-27.md,
  records/stage-2-close-2026-11-27.md.
- [x] T202 Part 3 executed under registration §4:
  both joins built and validated exactly (no STOP);
  context terms, nulls, and caps computed for the
  site, material, and find-context families;
  out-of-site validation run in both directions;
  channel record filed with its verdict and the
  no-iconography label; TC-109-05 run. Verdict
  CHANNEL NULL (pooled Δ 0.00888 against null p99
  0.03371); the context term is withdrawn from this
  study's scoring. Records:
  records/stage-2-part3-channel-2026-11-27.md,
  records/stage-2-close-2026-11-27.md.

## Stage 3 — Assignment search

- [ ] T301 Part 1 executed under registration §5:
  freeze sequence run in order (constraint set
  versioned; value inventory closed; 109 reserve cut
  and hash-committed; schedule registered); search run
  with timestamped progress; top-K selected; reserve
  opened once; adjudication under the frozen decide()
  rule; ranked candidate set and outcome record filed;
  TC-109-06 and TC-109-03 run.

## Stage 4 — Eteocypriot reading candidates

- [ ] T401 Part 5 executed under registration §6:
  generator preflight clauses run; freeze filed with
  the comparanda closed and the component drop
  restated; candidates generated and ranked per text;
  permutation-null recomputation filed; ranked sets
  and outcome record filed with no licensing language;
  TC-109-07 and TC-109-03 run.

## Stage 5 — Meroitic gloss induction (gated)

- [ ] T501 Part 4, on its registered gate: if
  Spec 102's digitisation and freeze exist, executed
  under registration §7 (freeze from Spec 102's frozen
  vocabulary; profiles and candidates generated;
  held-out scoring against null and wrong-family
  control; ranked gloss candidates and outcome record
  filed; TC-109-08 and TC-109-03 run). If Spec 102
  closes NOT ADMINISTERED, the gated outcome is filed
  and the stage closes unexecuted.
