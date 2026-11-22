# Spec 098 — Stage 1, T104: the seal

**Date:** 2026-11-21 · **Task:** T104 (acceptance: test) · **Claim:** C098-1 · **Venue:** tower-compute, fresh clone · **Runner:** `tools/stage1_run.py` (seal mode), payload exit 0.

## The seal

Struck under the frozen rule of freeze v1 §3 (`int(SHA-256("098-split-v1:" + cluster_id)) mod 5 == 0` over the deduplicated clusters of freeze §2), after the T101 provenance record, the T102 grapheme-gap record, and the T103 execution freeze annex were all committed — the commit order is the evidence, and this record predates every scoring artifact. No scoring-path code has run.

- Clusters over the sequence-bearing corpus of record: **2,413**
- Held-out clusters: **517**
- Seal SHA-256 (over the sorted held-out cluster ids, one per line, UTF-8): **`1974d83a5f667b71dbd53ecdb2e42a8221c6d4b91bdd32202b2a80579bf96cf9`**

The held-out list itself is held in custody outside the repository, at `~/glossa-custody/spec098/heldout-clusters-v1.txt` on tower-compute (the Spec 097 custody pattern). It is released to the scoring path exactly once, at Stage 3 scoring, and that release is recorded in the run index. A seal whose hash does not recompute at scoring time voids the run (SEAL FAILURE, no per-sign outcomes).

## Verification (the task's test leg)

The seal hash was recomputed from the custody list with the reference implementation (`tools/seal_and_score.py`, `verify_seal`) at striking time, including a re-read of the custody file from disk: **verify = True**.

## Payload verdict

```
PAYLOAD VERDICT T104: clusters=2413 held_out=517
seal_sha256=1974d83a5f667b71dbd53ecdb2e42a8221c6d4b91bdd32202b2a80579bf96cf9
verify=True   (runner exit 0)
```

Stage 1 is complete: T101 (genuine-holdout subset empty, absence recorded), T102 (M044 resolved under the crosswalk; M374 defaulted UNDECIDABLE), T103 (power grid + estimator annex), T104 (this seal). Stage 2 (rivals and prediction sheets, development data only) is the next stage and is not part of this record.
