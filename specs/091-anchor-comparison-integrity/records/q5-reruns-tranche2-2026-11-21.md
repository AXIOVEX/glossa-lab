# Spec 091 — Q5 item 3 dependency-aware reruns, Tranche 2: downstream targets after anchor deletion

**Date:** 2026-11-21 · **Spec:** 091-anchor-comparison-integrity · **Workstream:** Co-scientist audit Q5 item 3, Round 2 tranche 2 · **Venue:** tower-compute (fresh clone `~/glossa-work/r2-reruns-bbdd9d30`) · **Runner:** `backend/scripts/spec091_q5_reruns.py` · **Machine record:** `records/q5-reruns-2026-11-21.json`

## Method

For each target: (1) verify the raw co-occurrence count behind the filed argument from a second in-repo corpus record where one exists (the Phase-142 collocate network, `backend/reports/phase142_collocate_network.json`, corpus statistics 1,670 seals / 7,002 tokens / 390 signs, the same Holdat corpus population as the corrected battery); (2) delete the interpreted-anchor contribution (the anchor's authority, not the raw count: a verified raw adjacency count remains a fact about sign sequences, but it corroborates a reading only through the deleted anchor's interpretation); (3) record precisely what evidence remains and whether what remains discriminates the reading at all. Adjudicated vocabulary: **E** external-support claims on file, unverified, NOT IDENTIFIABLE; **I** internally motivated candidate, identifiability untested; **R** requires revalidation; **P** expert-pending provisionally; **U** insufficient evidence. This record changes no standing.

## Per-sign outcomes

### M005 (kōṉ, I) — cites 'HIGH' M342, count of 4
- Raw count: **verified**. Phase-142 lists M342 as a right neighbour of M005 with count 4 (M005 frequency 15). The count reproduces; its corroborative use does not survive deletion of M342 (U).
- **Residue:** initial position + DEDR 2199 lexical motivation. The residue does not discriminate kōṉ from other initial-position candidates on file.

### M030 (kō, I) — cites M342 collocations, count of 4
- Raw count: **verified**. Phase-142 lists M342 as a right neighbour of M030 with count 4 (M030 frequency 18).
- **Residue:** the corrected positional/bigram structural pass (T302 battery v2: score 2, positional pass, bigram pass neighbour_match=3/4=75.0%, DEDR leg not_run). That pass is structural only; it is not a test of the reading kō, and the DEDR leg was not run in the corrected battery.

### M068 (maṟi, I) — cites M342 collocations, count of 4
- Raw count: **not independently verified**. Phase-142 holds no initial-sign entry for M068; the count of 4 stands on the anchor record alone (single-source on file). Recorded as such, not substituted.
- **Residue:** rhinoceros motif association with a generic 'young animal/calf' gloss (DEDR 4706 per the anchor record's Phase-272 injection). The gloss is generic and is not specifically predicted by the rhinoceros motif; the residue does not discriminate maṟi.

### M089 (tu/tū, I) — upgrade invokes M342 and M176 (both U) plus M267 (I)
- Raw counts: **not stated consistently on file**. The anchor record's upgrade text lists M342 collocations twice with different counts (n=15 and n=13), M176 twice (n=6 and n=12), and M267 twice (n=6 and n=10). No single verified count can be extracted; all three anchors are deleted in any case.
- **Residue:** terminal distribution and bigram structure (T302 battery v2: positional pass, bigram pass neighbour_match=4/5=80.0%, DEDR not_run). These do not select tu/tū over other terminal-distributed candidates.

### M347 (ka, I) — Dravidian slot model + interpreted neighbours
- Raw contexts: the anchor record files 7 contexts and exemplifies 3 distinct patterns: `M342-[M347]-M293`, `M028-[M347]-M367`, `M211-[M347]-M099`. Recomputed as raw contexts with the slot interpretation removed, they are sequences involving M342 (U), M367 (U) and M099 (I); context signs M293, M028 and M211 are outside the 94 and are assigned no standing here.
- **Residue:** essentially all stated grammatical motivation is lost. What remains is the bare fact of 7 medial contexts; nothing in the residue selects ka.

### M375 (taṇ, I) — the taṇ-ay-an pattern depends on M342 and M176 (both U)
- Raw counts: **verified from the Phase-103 name-lexicon record** (`outputs/phase103_name_lexicon.json`): corpus frequency 7; NAME_AY_AN pattern count 2; sample patterns on file include the raw trigram `[M375]-M342-M176`. (The anchor record's text says name_slots=4 where the Phase-103 record says name_slot_count=7; the discrepancy is recorded, not resolved here.) The raw trigram exists; the translated pattern 'taṇ-ay-an = cool/noble man' is deleted as corroboration, because both suffix readings are U.
- **Residue:** iconographic alternatives taṇ / taṇṭu (DEDR 3009 folded-arm motivation, unresolved between the two) and a later literary naming parallel (taṇ- as a personal-name prefix in Sangam Akam poetry). Neither discriminates taṇ as this sign's reading.

### M398 (kuṟi, P) — the 'of-kuṟi-belonging' pattern relies on M267 (I) and M342 (U)
- Raw counts: **verified from Phase-103**: corpus frequency 3; GENITIVE_NAME_SUFFIX pattern count 1 (the raw sequence `M267-[M398]-M342` is on file); NAME_AY_AN count 1 (raw sequence `[M398]-M342-M176`). The translated pattern is deleted as corroboration.
- **Residue:** iconography (hook+ring) + DEDR 1769 dictionary candidate; kuṟi / kuṟu remains unresolved on the residue.

### M037 (kēḷ, I) — collocation with M267, count of 4; M267's genitive value is internally inferred
- Raw count: **verified**. Phase-142 lists M267 as a right neighbour of M037 with count 4 (M037 frequency 16).
- **Residue:** initial position + DEDR 2017. The residue does not discriminate kēḷ.

### M075 (māṟ, I) — collocation with 'HIGH' M267, count of 4
- Raw count: **not independently verified** (no Phase-142 initial-sign entry for M075; single-source on the anchor record, as for M068).
- **Residue:** DEDR 4796 only, which is also cited for M015 (mā); the distinction between the two readings is not supplied on file, so the residue does not discriminate māṟ from mā.

### M267 (iN/in, genitive, I) — its own numerical claim: NOT EXECUTABLE AS SPECIFIED
- Filed claim (Phase-74 grammar test, `outputs/phase74_m267_grammar_test.json`): 26 observed AGENT–M267–TITLE configurations against a null mean of 6, filed as a 4.3x enrichment, z = 8.038, p = 0.0 (verdict on file: GENITIVE_MARGINAL, not promoted).
- What reproduces: the arithmetic. 26 / 6 = 4.333, matching the filed 4.3x. The pattern counts on file (agent-before-and-title-after 26; agent-before-only 67; title-after-only 79; neither 228; total 400) are internally consistent, and M267's raw distribution facts reproduce across records (frequency 400; medial rate 0.785 in the Phase-64 record; motif distribution across all motif types in the anchor record).
- What does not reproduce as a test: the filed z implies a null standard deviation of (26 − 6) / 8.038 = 2.488, which matches no stated null on file (a Poisson null at mean 6 would give z = 8.165). More fundamentally, the rerun's own condition fails: the AGENT slot markers on file are M059, M176, M305, M328, M336 and the TITLE markers are M030, M041, M073, M099, M211. The AGENT set includes M176 (U) and M328 (U); the TITLE set includes M099 (I) and M073 (I). The slot labels are assigned from the same candidate reading/grammar system the test is meant to support, and no slot labelling independent of that system, and no selection correction over the candidate search, is stated on file.
- **Recorded outcome: rerun NOT EXECUTABLE AS SPECIFIED**, for that reason. The 4.3x figure is an enrichment over slots defined by the system under test and carries no independent weight.

### M374 (kul, I) — interpretation uses M328=man (U) and M073=king (I)
- The interpreted context ('between authority signs') is removed. No numeric claim is on file for this sign.
- **Residue:** the Munda kul comparison (Witzel 1999) and the Dravidian kulam comparison (DEDR 1709). That is a lexical comparison, not an Indus sign mapping; it does not establish that this sign reads kul.

## Payload verdicts (runner exit code 0 overall)

- `M005: filed_n=4 phase142_n=4 verified=True` · `M030: filed_n=4 phase142_n=4 verified=True` · `M037: filed_n=4 phase142_n=4 verified=True`
- `M068: filed_n=4 phase142=absent verified=None (single-source)` · `M075: filed_n=4 phase142=absent verified=None (single-source)`
- `M089: filed upgrade counts internally inconsistent (duplicated, differing); anchors deleted regardless`
- `M347: n_contexts=7 patterns_on_file=3 slot interpretation removed`
- `M375: freq=7 ay_an=2 genitive=0` · `M398: freq=3 ay_an=1 genitive=1`
- `M267: enrichment=4.3333 (filed 4.3x) z_filed=8.038 rerun_as_specified=NOT_EXECUTABLE`
- `M374: no numeric claim on file; interpreted context removed`

## What this record does not do

It changes no standing, no ledger entry, and no register value. It reports evidence residues after deletion only.
