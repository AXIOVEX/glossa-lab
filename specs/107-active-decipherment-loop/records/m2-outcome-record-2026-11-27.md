# Spec 107 — Cycle 2: M-2 Outcome Record (T205)

**Date:** 2026-11-27. **Program:** Spec 107 — Active
Decipherment Loop, cycle 2. **Test:** M-2, the Meroitic
phonotactic battery registered at
`records/cycle-2-registration-2026-11-27.md` §6.

**Outcome: STOPPED AT THE CALIBRATION GATE — basis
finding. No battery statistic was computed.** The
registered gate requires the battery's basis to be
reconstructed from the pinned Kovetsky build only, under
pipeline-v2 conventions, reproducing Spec 097 freeze
v2's filed development figures (12,863 words; 13,406 CVC
pairs; same-place rate 0.3152; NES reference 0.3038, each
to 4 decimal places) before any scoring. The
reconstruction does not reproduce them, and the reason
is a defect in the basis as registered, documented at
§2 with its evidence. Under the registration's own rule
the stop is the outcome; nothing was improvised around
it.

## 1. The gate, administered

Reconstruction script: `records/m2-calibration.py`
(pipeline-v2's `tokens_of` and `same_place_rate`
conventions verbatim, the PLACE table verbatim, the
development partition by freeze v2 §1's rule over the
pinned build, inscriptions source SHA-256
`1e91e3a0c52626482bc4015b597df862e7818602dab48a7e870240ab2e567bc4`).
Raw output: `records/m2-calibration-output.json`.

| Figure | Filed (freeze v2 / stage42-results) | Kovetsky-only reconstruction | Gate |
|---|---|---|---|
| Words | 12,863 | 4,886 | **fail** |
| CVC pairs | 13,406 | 5,883 | **fail** |
| Same-place rate | 0.3152 | 0.3002 | **fail** |
| NES reference rate | 0.3038 | 0.3038 (374 ASJP forms, 293 pairs, 0.303754…) | pass, exact |

The NES reference reproducing exactly — from the ASJP
custody lists (lexibank/asjp at
`cf4bf0d13c95256b1b48f440d07c5c098500a770`) under the
pipeline's own conventions — isolates the failure to the
Meroitic side of the basis: the conventions and the
comparator custody are right; the Meroitic basis as
registered cannot produce the filed figures.

## 2. The basis finding

The filed figures were computed by pipeline-v2 over the
development partition **plus the 932 distinct example
phrases** of the per-scholar files (freeze v2 §1: the
335 development texts, and "the 932 distinct example
phrases of the per-scholar files (Millet, Rilly,
Kalabsha) are development material"; pipeline-v2's
`stage42` adds `examples()` to the word basis before
computing, and its filed output records
`words_basis: 12863`). The shortfall of the
Kovetsky-only reconstruction — 7,977 words — is the
example phrases' contribution.

Those example files are not Kovetsky-build material.
They are Data files of the **Otten & Anastasopoulos
(2025) corpus** (Spec 097 step-0 identity record: the
target corpus held at `~/glossa-work/meroitic-corpus-src`,
with `Data/MilletExamples.txt` SHA-256 `9e0dc67c…`,
`Data/RillyExamples.txt` SHA-256 `beae69e1…` in its pin
manifest; the inspectable-packet manifest states the
same custody in terms). The cycle-2 registration
requires the basis to be reconstructed from the pinned
Kovetsky build **only** and that **no Otten byte enter
any M-2 input**. The two requirements together make the
gate unsatisfiable as registered: the figures to be
reproduced were computed over a basis 62% of whose words
are Otten-corpus example phrases the registration
excludes. The registration's basis sentence carries the
defect — it names "335 texts / 932 phrases" as the
development partition of the Kovetsky build, when the
932 phrases are Otten-corpus files.

Independently, the gate could not be administered the
other way either: the Otten custody tree
(`~/glossa-work/`) no longer exists on tower-compute
(searched 2026-11-27: the worktrees, the campaign
custody, and the home tree; the example files are
nowhere in custody), so the filed basis cannot be
reconstructed from custody today under any reading.

## 3. Consequences

- M-2's battery (items SP-CVC, LV-CO, ONSET-CC, CODA-C,
  LV-TRANS; Nulls W and X; control C; the family-range
  verdict rule) was **not run**. No score, null, or
  control figure exists for it, and none is reported.
  The ASJP segment→place-class mapping table, registered
  to be filed before any battery statistic, is moot and
  was not produced.
- TC-107-10 is executed in its gate arm: the calibration
  gate was administered before scoring and stopped the
  test, which is the outcome the test case registers for
  a basis that does not reproduce.
- The defect is in the cycle-2 registration's basis
  sentence, adopted in PR #794. Correcting it is a
  re-registration decision for a future cycle (a
  Kovetsky-only basis with its own freshly computed
  calibration figures, or a basis that lawfully includes
  the example phrases with their custody restored) — it
  is not corrected inside this execution, and this
  record recommends the discrepancy be carried into the
  cycle-2 outcome record's posterior trace so the design
  queue prices it.
- No claim's standing moves. C107-10's falsifier is met
  in its stop arm: the battery's registered basis did
  not reproduce under the registered reconstruction rule.

**AI disclosure:** executed by an AI agent (Muse, via
Muse) at the direction of Tristen Pierson, per
constitution sec. VI.
