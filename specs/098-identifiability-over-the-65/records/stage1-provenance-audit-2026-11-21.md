# Spec 098 — Stage 1, T101: provenance audit and the genuine-holdout subset

**Date:** 2026-11-21 · **Task:** T101 (acceptance: record) · **Claim:** C098-6 · **Venue:** tower-compute, fresh clone · **Runner:** `tools/stage1_run.py` (census mode), payload exit 0 · **Corpus of record:** `glossa-corpus/indus/exports/indus_research.jsonl`, SHA-256 verified against the freeze pin (`08fc96c8…`), 15,508 records.

## The audit

Every sequence-bearing source in the corpus of record was enumerated and checked against the candidate-generation inputs of record, under the criterion frozen in spec §3.3: a source forms the genuine-holdout subset only if it is documented as acquired after the latest candidate-assignment date in the population annex, or is otherwise demonstrably absent from every candidate-generation input.

Census (runner output, payload-verified):

| Source system | Records | Sequence-bearing |
|---|---|---|
| indusscript-m77 | 2,906 | 2,906 |
| mayig-cisi | 179 | 127 |
| PennMuseum | 7,515 | 0 |
| MetOpenAccess | 4,904 | 0 |
| ClevelandArtOpenAccess | 4 | 0 |
| **Total** | **15,508** | **3,033** |

The sequence-bearing total (3,033) reproduces the freeze record's sampling frame exactly.

## The check against candidate-generation inputs

Exactly two sources carry sequences, and both are the program's candidate-generation inputs of record, not later arrivals:

- **indusscript-m77** is the Mahadevan 1977 concordance corpus (M77) over which the anchor program's candidates were generated: the 287-reading anchor register, the phase batteries, the corrected Spec 091 batteries, and the Phase-142 collocate population all ran over this corpus population (the "Holdat corpus population" of the program's records; corpus snapshot SHA `08fc96c8…`, the same file this freeze pins).
- **mayig-cisi** is the CISI digitisation (mayig/indus-valley-script-corpus, per the corpus README's source layout) that supplies the Parpola-coded sequences used by the same derivation and crosswalk work.

Neither source is documented as acquired after any candidate-assignment date; both predate the program's candidate assignments (which run through the Phase-276 injections) because they are the inputs those assignments were computed from. The corpus README's acquisition pipeline (`backend/scripts/corpus_indus_acquire_free.py` and its successors) documents both as founding corpus sources. The three museum open-access sources carry object metadata and no sign sequences at all, so they cannot form a sequence-bearing holdout under any reading of the criterion.

## Finding

**The genuine-holdout subset is empty. Its absence is recorded, as the task provides.** No sequence-bearing source in the corpus of record was demonstrably absent from candidate generation, and none was acquired after the latest candidate-assignment date.

Frozen consequences, stated so they cannot be re-narrated later: no sign in the population is scored on a genuine-holdout primary arm; the outcome IDENTIFIABLE ON HELD-OUT is unavailable to this study as constituted; every sign's ceiling on the in-corpus arm is DISCRIMINATED ON PSEUDO-HELD-OUT (spec §3.3, freeze §7 gap 1 — gap now resolved on the record, in the direction the freeze anticipated).

## Payload verdict

```
PAYLOAD VERDICT STAGE1-CENSUS: PASS   (runner exit 0; corpus pin verified;
T101 census: 15,508 records, 3,033 sequence-bearing, 2 sequence-bearing sources)
```
