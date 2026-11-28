# Spec 110 — Plan

Execution follows the registration
(`records/registration-2026-11-27.md`) §7 order:

1. **Registration.** Package written; AEE assessment
   run over the bundle; TC-110-01 executed; claims
   intaken through the standard cascade (intake,
   canonical verification, the T405 pair re-executed
   over the grown build, pin refreshed as a new
   re-derivation, generated layers regenerated,
   superseded generation departed, census pins updated
   from the regenerated actuals); cascade record
   filed.
2. **Harness.** The battery harness built on
   tower-compute over the pinned corpora and the
   Spec 109 synthetic machinery; corpus censuses
   filed (counts, inventories, strata) before any
   statistic is computed.
3. **Control gate.** Transformations applied to the
   synthetic controls; the gate legs of registration
   §4 evaluated; control-validation record filed. On
   any leg's failure the study stops here (kill
   criterion 1) and the real-corpus runs are not
   scoreable.
4. **Execution.** The battery run on the Indus,
   Eteocypriot, and Meroitic corpora; per-corpus
   per-family verdicts under registration §5;
   execution record filed with every figure, its
   null, and — for any PRESENT — its alternative
   explanations.
5. **Verification and close.** TC-110-02 and
   TC-110-03 recomputations by the independent
   verification script; TC-110-04 trace over the
   landing diff; TC-110-05 kill evaluation; close
   record; PROGRAM-STATE updated.

All computation runs on tower-compute in the study's
worktree; intermediates live in custody under
`glossa-custody/spec110/` (D-110-4). Every run emits
timestamped, countable progress lines, and every
reported verdict is the run's own payload verdict.
