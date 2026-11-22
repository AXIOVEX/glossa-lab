# Spec 091 — Q5 item 3 dependency-aware reruns, Tranche 3: M063 (mutalai) — the motif claim itself

**Date:** 2026-11-21 · **Spec:** 091-anchor-comparison-integrity · **Workstream:** Co-scientist audit Q5 item 3, Round 2 tranche 3 · **Venue:** tower-compute (fresh clone `~/glossa-work/r2-reruns-bbdd9d30`) · **Runner:** `backend/scripts/spec091_q5_reruns.py` · **Machine record:** `records/q5-reruns-2026-11-21.json`

## The claim as specified

M063 (mutalai, I) was originally supported by a **motif** claim: association with the gharial motif, with an original lift threshold of **5.0**. This tranche reruns that claim itself, not a positional substitute. The later corrected battery (T302, battery v2) did **not** rerun the motif claim: its filed tests for M063 are positional (pass), DEDR (not_run, dataset not held) and bigram (pass, neighbour_match=2/4=50.0%). Those are structural results and are not evidence about the gharial association either way.

## Filed corrected figures

From the anchor record's fact-check correction of 2026-05-11 (`backend/reports/INDUS_FINAL_ANCHORS.json`, carried identically in `research/indus/anchor_table.csv`):

- measured gharial **lift = 4.35** (the originally claimed 'lift > 5.0' does not hold);
- the sign appears on **3 of 18** seals with the gharial motif (gharial carriage rate 3/18 = 16.7%);
- the sign also appears on non-gharial seals: 4 unicorn and 3 zebu bull seals are named on file, so the original 'exclusive to gharial seals' formulation fails on file as well.

## Rerun outcome

- **Verdict on the claim as specified: FAILS on the filed corrected figures.** Lift 4.35 is below the claim's own threshold of 5.0, and exclusivity fails on the filed motif counts. No deletion or reinterpretation is needed to reach this verdict; the corrected figures already on file decide it.
- **Full contingency recomputation: NOT EXECUTABLE from held records, recorded rather than substituted.** Recomputing the lift from scratch requires the full 2×2 (sign × gharial motif over the deduplicated seal population): the filed records state the gharial cell (3/18) and the resulting lift (4.35), but do not jointly file the sign's total seal count and the deduplicated seal population the lift denominator uses, and the raw Holdat corpus CSV is gitignored working data, not held in this clone. The missing cells were not reconstructed from substitute data, and no weaker test was silently substituted: the positional/bigram pass that does exist on file is a different claim and is reported above as such.

## Payload verdict

- Runner exit code: **0** (overall; see the machine record).
- `PAYLOAD VERDICT T3 M063: gharial=3/18 rate=0.1667 filed_lift=4.35 threshold=5.0 claim_fails_on_filed_figures=True full_2x2_reconstructible=False`

## Residue and non-effects

What remains for M063 after this rerun is the corrected battery's structural pass (positional + bigram, DEDR leg not run) and the DEDR 4954 lexical plausibility noted in the correction ('plausible given gharial association, but not exclusive enough'). The motif claim itself, as specified, does not stand. This record changes no standing, no ledger entry, and no register value.
