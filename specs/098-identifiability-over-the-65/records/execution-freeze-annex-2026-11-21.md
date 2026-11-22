# Spec 098 — Stage 1, T103: execution freeze annex (power grid + estimator details)

**Date:** 2026-11-21 · **Task:** T103 (acceptance: record) · **Claim:** C098-5 · **Venue:** tower-compute · **Status:** committed before the seal, as freeze §5 requires; the seal (T104) is struck in a later commit that cites this annex. This annex fixes only what freeze v1 §5 leaves open (the context model's order, smoothing constant, and exact estimator) and states the power grid. It changes no bar, parameter, or outcome rule of freeze v1 §§3–5; a change to anything below is a new freeze version, recorded as such.

## 1. Population, as amended before any scoring

The population is the frozen annex population as amended by the WS2 relabel execution of 2026-11-21 (Spec 091 standings act): M202's external claim was contradicted on re-verification and struck, and M202 moved from class E to class U, so it leaves this study's population. **Population: 70 signs — Arm I, the 65; Arm E, five (M044, M047, M124, M329, M330).** The multiplicity family for all reporting is these 70 signs. No scoring of any kind had occurred when the amendment landed; the design freeze is otherwise untouched.

## 2. Power grid (development-side counts only)

Basis, fixed here so the result cannot be re-narrated afterwards: token counts are canonical-grapheme-field tokens over the deduplicated development clusters (cluster rule of freeze §2; representative record per cluster), computed by `tools/stage1_run.py` in the same payload-verified run as the T101/T102 records (exit 0). The expected held-out count per sign is its development count divided by 4 (the frozen split's 4:1 expectation); no actual held-out count is stated anywhere in Stage 1. The minimum detectable margin per sign is the per-token mean margin that would reach the frozen 10-nat bar at its expected held-out count (10 / expected held-out, in nats per token), before the permutation-null condition, which can only raise the effective bar. The full per-sign grid is `records/stage1-grid-2026-11-21.json`.

Headline of the grid, stated before unsealing:

- **21 of 70 signs** have an expected held-out count at or above the frozen 5-token minimum; **49 fall below it in expectation** and stand to be UNDECIDABLE AT THIS POWER at scoring unless their actual held-out counts beat the expectation.
- Arm E: only M124 meets the floor in expectation (expected 10.75). M047 (2.75), M329 (1.0), and M330 (1.5) fall below; M044 has 0 canonical-field tokens (its single resolved diplomatic attestation is recorded in the T102 record).
- M374 has 0 tokens and already stands at the frozen UNDECIDABLE default (T102 record).
- UNDECIDABLE AT THIS POWER is therefore the expected majority outcome of this study, exactly as freeze §7 gap 3 anticipated. That expectation is part of this record, not a post-hoc narration.

## 3. Estimator details, fixed

- **Context.** For each occurrence of the target sign in an inscription sequence, the context is the ordered pair (left neighbour, right neighbour) of canonical grapheme ids within the same inscription, with BOS/EOS sentinels at the sequence ends. Sequences are the deduplicated clusters' representative records under freeze §2. Context order is therefore 1 (immediate neighbours only).
- **Model.** A value-conditioned context model: for a value v (the candidate, or a rival under the WP8 fairness conditions of spec §3.4), the context distribution P_v is estimated on development data only, from the development occurrences the Stage 2 prediction sheets assign to v. Candidate and rivals share this estimator, the context order, and the smoothing, exactly.
- **Estimator.** Add-α smoothing with **α = 0.1** over the sign's development context vocabulary V (the contexts observed with the sign in development data) plus one unseen-context bucket: P_v(c) = (count_v(c) + α) / (N_v + α·(|V| + 1)). A held-out occurrence with value v scores log P_v(context), natural log; the log-likelihoods handed to the frozen decision rule (`tools/seal_and_score.py`, `decide`) are the totals over the sign's held-out occurrences, in nats.
- **Penalties, null, bootstrap.** As freeze v1 §5, unchanged: 2 nats per free choice charged to candidates and rivals alike; permutation null B = 999, seed 9801, margin must exceed the null's 99th percentile; cluster bootstrap B = 999, seed 9802 for reported intervals. The null permutes value assignments over the sign's held-out occurrences.
- **Decision.** The frozen outcome vocabulary and precedence of spec §4, with the T101 record's ceiling: no genuine-holdout arm exists, so IDENTIFIABLE ON HELD-OUT is unavailable; the in-corpus arm's best outcome is DISCRIMINATED ON PSEUDO-HELD-OUT.

## Payload verdict

```
PAYLOAD VERDICT T103: grid_written=stage1-grid-2026-11-21.json population=70
(runner exit 0; 21 of 70 signs meet the 5-token floor in expectation)
```
