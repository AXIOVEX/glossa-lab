# The inference log for the 94 strict-core readings

Spec 099 Stage 1, filed 2026-11-21. Generated from `inference-log.json` by `tools/build_inference_log.py`; the JSON is the record of record and this rendering is never edited separately.

Entries: 94. Items: 296 (210 primary (a), 61 other-reading / candidate-system (b), 25 ambiguous).

Item types: **a** = primary evidence; **b** = another reading or a candidate-system construct used as evidence; **ambiguous** = the filed basis does not state the item's inputs. Status notes carry the landed annotations (withdrawn, FAILED, struck, not reproducible) with their sources.

## M044 — ku (class U, Q4 M)

> Basis as recorded: ; Phase-276: dual external corroboration — Elamite 'kun' (MC-18) + Sanskrit 'kona' (SL-04) + DEDR 1638; Source as recorded: Phase-83 gap sprint; Dictionary reference as recorded: 1638; Evidence lines the audit counted as independent: 3 (CROSSWALK_CORPUS, DEDR, EXTERNAL_CORROBORATION); Tests filed: phonetic_value, meaning

| Item | Kind | Type | Statement | Targets | Notes |
|---|---|---|---|---|---|
| M044-01 | dictionary_entry | a | DEDR 1638 — one observation cited twice in the basis: as an external corroboration leg ('DEDR 1638') and as this reading's dictionary reference; entered as one item (spec section 3.2) | — | Status: DEDR 1638 FAILS in the restored tree (entry 1638 = kucukucu; register reconciliation 2026-11-21, PR #645 DEDR pass). Adjudicated under the addendum rule on 2026-11-21 (records/m044-addendum-adjudication-2026-11-21.md, Red Team Round 2 finding RT2-02): the DEDR leg is struck, no leg stands verified as filed, no basis remains, and the reading takes class U; this log's executed class follows the amended standings |
| M044-02 | comparative_lexical | a | external corroboration leg: Elamite 'kun' (MC-18) | — | — |
| M044-03 | comparative_lexical | a | external corroboration leg: Sanskrit 'kona' (SL-04) | — | — |

- Note: the basis-as-recorded segment is empty as filed ('Basis as recorded: ;'); the Phase-276 segment carries the filed legs
- Note: the audit's evidence lines count a CROSSWALK_CORPUS line for this reading, but no crosswalk step is stated in the basis text as filed

## M047 — min/mīn (class U, Q4 A)

> Basis as recorded: FACT-CHECK CORRECTION 2026-05-11: Distributional assignment 'par' (LOW, Round 2) overridden by crosswalk evidence. M047 = P47 = 'fish (plain)' per mahadevan_parpola_crosswalk.json (sourced from Parpola 1994a + Mahadevan ; Evidence lines the audit counted as independent: 2 (CROSSWALK_CORPUS, EXTERNAL_CORROBORATION); Tests filed: drawing, phonetic_value, meaning

| Item | Kind | Type | Statement | Targets | Notes |
|---|---|---|---|---|---|
| M047-01 | positional_statistic | a | distributional assignment 'par' (LOW, Round 2), overridden within the filed basis by the crosswalk evidence | — | Status: superseded within the filed basis by the 2026-05-11 fact-check correction |
| M047-02 | crosswalk_identity | a | crosswalk identity: M047 = P47 = 'fish (plain)' per mahadevan_parpola_crosswalk.json (sourced from Parpola 1994a + Mahadevan) | — | Status: an identity at most, never a value: the identity rests on catalogue correspondence between the two sign lists, not on this reading (spec section 3.3); the basis as filed truncates mid-clause at this item. Re-verification outcome: VERIFIED AS FILED, provenance only (relabel execution record). F-9 act (2026-11-22): the owner adopted the itemization test; the directed re-examination entered no published_proposal item for this entry (the filed basis states no published proposal of the value; records/f9-itemization-adjudication-2026-11-22.md), no internal motivation for the reading remains on the filed basis, and the reading takes class U; this log's executed class follows the amended standings |

## M124 — kuTam (class E, Q4 M)

> Basis as recorded: ; Phase-276: dual external corroboration — Elamite 'kun' (MC-18) + Sanskrit 'kona' (SL-04) + DEDR 1651; Source as recorded: Parpola_1994_via_phase51; Dictionary reference as recorded: 1651; Gloss as recorded: pot / jar; Evidence lines the audit counted as independent: 4 (CROSSWALK_CORPUS, DEDR, EXTERNAL_CORROBORATION, LITERATURE); Tests filed: phonetic_value, meaning

| Item | Kind | Type | Statement | Targets | Notes |
|---|---|---|---|---|---|
| M124-01 | dictionary_entry | a | DEDR 1651 — one observation cited twice in the basis: as an external corroboration leg ('DEDR 1651') and as this reading's dictionary reference; entered as one item (spec section 3.2) | — | Status: re-verification: PARTIALLY VERIFIED (the DEDR legs check out as filed) |
| M124-02 | comparative_lexical | a | external corroboration leg: Elamite 'kun' (MC-18) | — | Status: leg inherited from M044's Phase-276 package; the adjudication records that the reuse does not derive kuTam. Re-verification: PARTIALLY VERIFIED (DEDR legs only) |
| M124-03 | comparative_lexical | a | external corroboration leg: Sanskrit 'kona' (SL-04) | — | Status: leg inherited from M044's Phase-276 package; the adjudication records that the reuse does not derive kuTam. Re-verification: PARTIALLY VERIFIED (DEDR legs only) |

## M202 — can (class U, Q4 S)

> Basis as recorded: Phase-163 sibilant discovery: reading 'can' found in literature (4 mentions across sources: Mahadevan_2009_vestiges). Provides partial coverage for Shu-ilishu /su/ phonological slot.; Phase-276: dual external corroborati; Source as recorded: Phase-111; Evidence lines the audit counted as independent: 3 (CROSSWALK_CORPUS, EXTERNAL_CORROBORATION, LITERATURE); Tests filed: phonetic_value, meaning

| Item | Kind | Type | Statement | Targets | Notes |
|---|---|---|---|---|---|
| M202-01 | published_proposal | a | the reading is filed as found in the literature (4 mentions across sources: Mahadevan_2009_vestiges) | — | Status: CONTRADICTED on re-verification: Mahadevan 2009 (Vestiges) contains no 'can' reading; the claim was struck under the addendum rule and the reading reclassed U (relabel execution record, section 4) |
| M202-02 | slot_label | b | the reading is filed as providing partial coverage for the Shu-ilishu /su/ phonological slot | — | Reason: the /su/ slot is a construct of the candidate system's phonological coverage argument; the coverage claim is evidence only inside that system Target note: the basis names the slot but no reading as its premise |

- Note: the Phase-276 segment is truncated in the basis as filed ('dual external corroborati'); its legs are not stated and no items are entered for it

## M329 — poṉ (class E, Q4 M)

> Basis as recorded: Round 5: MEDIAL position (freq=5), distributional assignment; Phase-276: dual external corroboration — Elamite 'bur/pur' (MC-21) + Sanskrit 'pura' (SL-14) + DEDR 4524; Dictionary reference as recorded: 4524; Gloss as recorded: gold, precious; personal name; Evidence lines the audit counted as independent: 4 (CROSSWALK_CORPUS, DEDR, EXTERNAL_CORROBORATION, GRAMMAR); Tests filed: distribution, functional_role, phonetic_value, meaning

| Item | Kind | Type | Statement | Targets | Notes |
|---|---|---|---|---|---|
| M329-01 | positional_statistic | a | positional distribution: MEDIAL position, frequency 5, distributional assignment | — | — |
| M329-02 | dictionary_entry | a | DEDR 4524 — one observation cited twice in the basis: as an external corroboration leg ('DEDR 4524') and as this reading's dictionary reference; entered as one item (spec section 3.2) | — | Status: the DEDR leg is verified at the print entry cited; the restored tree's entry 4524 is a different entry and the numbering divergence is unresolved (register reconciliation section (c); relabel execution record, Round 2 amendment) |
| M329-03 | comparative_lexical | a | external corroboration leg: Elamite 'bur/pur' (MC-21) | — | — |
| M329-04 | comparative_lexical | a | external corroboration leg: Sanskrit 'pura' (SL-14) | — | Status: FAILS on its checkable part: Sanskrit pura means stronghold/city, not gold (re-verification record). The claim stands in E under the addendum: PARTIALLY VERIFIED, the dictionary leg checks out as filed and the remaining legs are not contradicted in their named sources |

## M330 — can (class E, Q4 S)

> Basis as recorded: Phase-163 sibilant discovery: reading 'can' found in literature (4 mentions across sources: Parpola_1994). Provides partial coverage for Shu-ilishu /su/ phonological slot.; Phase-276: dual external corroboration — Elamit; Source as recorded: Phase-111; Evidence lines the audit counted as independent: 3 (CROSSWALK_CORPUS, EXTERNAL_CORROBORATION, LITERATURE); Tests filed: phonetic_value, meaning

| Item | Kind | Type | Statement | Targets | Notes |
|---|---|---|---|---|---|
| M330-01 | published_proposal | a | the reading is filed as found in the literature (4 mentions across sources: Parpola_1994) | — | Status: NOT VERIFIABLE from lawfully reachable material: the held Parpola 1994 text is an OCR scan, and a negative result from it is weaker than a contradiction from a clean text (relabel execution record) |
| M330-02 | slot_label | b | the reading is filed as providing partial coverage for the Shu-ilishu /su/ phonological slot | — | Reason: the /su/ slot is a construct of the candidate system's phonological coverage argument; the coverage claim is evidence only inside that system Target note: the basis names the slot but no reading as its premise |

- Note: the Phase-276 segment is truncated in the basis as filed ('dual external corroboration — Elamit'); its legs are not stated and no items are entered for it

## M002 — kuṉ (class I, Q4 S)

> Basis as recorded: Round 2: INITIAL position (freq=16), distributional assignment; UPGRADED-V18: consistent INITIAL (n=16); has specific PDR reading; Phase-272: DEDR 1694 injected + existing evidence → HIGH; Dictionary reference as recorded: 1694; Evidence lines the audit counted as independent: 2 (DEDR, GRAMMAR); Tests filed: distribution, phonetic_value, meaning

| Item | Kind | Type | Statement | Targets | Notes |
|---|---|---|---|---|---|
| M002-01 | positional_statistic | a | positional distribution: INITIAL position, frequency 16, distributional assignment; restated as consistent in the V18 upgrade | — | — |
| M002-02 | self_assertion | b | the basis asserts the sign 'has specific PDR reading' | — | Reason: the adjudication's words: an input, not corroboration — the candidate system's own assertion about its reading, filed as part of the basis Target note: the assertion names no other reading; it is the system's own claim about this reading |
| M002-03 | dictionary_entry | a | DEDR 1694 cited for this reading (Phase-272 injection) | — | — |

- Note: the Phase-272 segment's roll-up ('existing evidence → HIGH') is a derivation step of the candidate system, recorded here, not an item (spec section 3.3)

## M004 — kēḷ (class I, Q4 S)

> Basis as recorded: Round 1: INITIAL position (freq=17), distributional assignment; UPGRADED-V18: consistent INITIAL (n=17); has specific PDR reading; Source as recorded: +Phase48_validated; Evidence lines the audit counted as independent: 2 (GRAMMAR); Tests filed: distribution, functional_role Later corrected validation battery: score 2 against a promotion threshold of 2 (positional pass, dedr not_run, bigram pass); moved from requires revalidation to this class.

| Item | Kind | Type | Statement | Targets | Notes |
|---|---|---|---|---|---|
| M004-01 | positional_statistic | a | positional distribution: INITIAL position, frequency 17, distributional assignment; restated as consistent in the V18 upgrade | — | — |
| M004-02 | self_assertion | b | the basis asserts the sign 'has specific PDR reading' | — | Reason: the adjudication's words: an input, not corroboration — the candidate system's own assertion about its reading, filed as part of the basis Target note: the assertion names no other reading; it is the system's own claim about this reading |
| M004-03 | corrected_validation | a | corrected validation battery: score 2 against a promotion threshold of 2 (positional pass, dedr not_run, bigram pass); the sign was moved from requires revalidation to its filed class on this result | — | — |

## M005 — kōṉ (class I, Q4 S)

> Basis as recorded: Round 2: INITIAL position (freq=15), distributional assignment; UPGRADED-V18: consistent INITIAL (n=15); HIGH-anchor collocate M342 (n=4); has specific PDR reading; Phase-272: DEDR 2199 injected + existing evidence → HIG; Dictionary reference as recorded: 2199; Evidence lines the audit counted as independent: 2 (DEDR, GRAMMAR); Tests filed: distribution, phonetic_value, meaning

| Item | Kind | Type | Statement | Targets | Notes |
|---|---|---|---|---|---|
| M005-01 | positional_statistic | a | positional distribution: INITIAL position, frequency 15, distributional assignment; restated as consistent in the V18 upgrade | — | — |
| M005-02 | self_assertion | b | the basis asserts the sign 'has specific PDR reading' | — | Reason: the adjudication's words: an input, not corroboration — the candidate system's own assertion about its reading, filed as part of the basis Target note: the assertion names no other reading; it is the system's own claim about this reading |
| M005-03 | corpus_count | a | raw co-occurrence count with M342: n=4 | — | — |
| M005-04 | interpreted_anchor | b | collocation premise: this sign collocates with M342 as a HIGH anchor | M342 | Reason: the premise is M342 under its interpreted reading and HIGH standing; the raw count is carried separately as an (a) item |
| M005-05 | dictionary_entry | a | DEDR 2199 cited for this reading (Phase-272 injection) | — | — |

- Note: the Phase-272 segment's roll-up ('existing evidence → HIGH') is a derivation step of the candidate system, recorded here, not an item (spec section 3.3)

## M006 — puli (class I, Q4 S)

> Basis as recorded: Exclusive to tiger seals (lift > 5.0); PDR puli = tiger; Evidence lines the audit counted as independent: 2 (DEDR, ICONOGRAPHIC); Tests filed: drawing, distribution, phonetic_value, meaning

| Item | Kind | Type | Statement | Targets | Notes |
|---|---|---|---|---|---|
| M006-01 | motif_association | a | the sign is exclusive to tiger seals (filed lift > 5.0) | — | Status: motif evidence not reproducible from held records (standings supplement 2026-11-21, section 3) |
| M006-02 | comparative_lexical | a | PDr puli = tiger (the motif's lexical counterpart) | — | — |

## M007 — aaL (class I, Q4 S)

> Basis as recorded: ; Phase-255: commodity phoneme corroboration — matches PDr 'akatti'=agate (DEDR 7), appears on 4 trade/zebu seals; Source as recorded: Phase-89 systematic DEDR (ICON, HIGH); Dictionary reference as recorded: DEDR 0340; Gloss as recorded: person; Evidence lines the audit counted as independent: 2 (CROSSWALK_CORPUS, DEDR); Tests filed: distribution, phonetic_value, meaning

| Item | Kind | Type | Statement | Targets | Notes |
|---|---|---|---|---|---|
| M007-01 | dictionary_entry | a | commodity phoneme corroboration: PDr 'akatti' = agate (DEDR 7) | — | — |
| M007-02 | motif_association | a | the sign appears on 4 trade/zebu seals | — | — |
| M007-03 | dictionary_entry | a | DEDR 340 recorded as this reading's dictionary reference | — | — |

- Note: the basis carries two dictionary references that do not agree: the Phase-255 corroboration cites DEDR 7 (PDr 'akatti' = agate, a commodity claim that does not state this reading's own gloss) and the dictionary-reference segment records DEDR 0340 (gloss as recorded: person). Both are entered as filed; the disagreement is recorded, not resolved

## M009 — āṇ (class I, Q4 S)

> Basis as recorded: Round 2: INITIAL position (freq=16), distributional assignment; UPGRADED-V18: consistent INITIAL (n=16); has specific PDR reading; Phase-272: DEDR 367 injected + existing evidence → HIGH; Dictionary reference as recorded: 367; Evidence lines the audit counted as independent: 2 (DEDR, GRAMMAR); Tests filed: distribution, phonetic_value, meaning

| Item | Kind | Type | Statement | Targets | Notes |
|---|---|---|---|---|---|
| M009-01 | positional_statistic | a | positional distribution: INITIAL position, frequency 16, distributional assignment; restated as consistent in the V18 upgrade | — | — |
| M009-02 | self_assertion | b | the basis asserts the sign 'has specific PDR reading' | — | Reason: the adjudication's words: an input, not corroboration — the candidate system's own assertion about its reading, filed as part of the basis Target note: the assertion names no other reading; it is the system's own claim about this reading |
| M009-03 | dictionary_entry | a | DEDR 367 cited for this reading (Phase-272 injection) | — | — |

- Note: the Phase-272 segment's roll-up ('existing evidence → HIGH') is a derivation step of the candidate system, recorded here, not an item (spec section 3.3)

## M010 — paṭ (class I, Q4 S)

> Basis as recorded: Round 1: INITIAL position (freq=17), distributional assignment; UPGRADED-V18: consistent INITIAL (n=17); has specific PDR reading; Phase-255: commodity phoneme corroboration — matches PDr 'akatti'=agate (DEDR 7), appears; Evidence lines the audit counted as independent: 2 (CROSSWALK_CORPUS, GRAMMAR); Tests filed: distribution, meaning

| Item | Kind | Type | Statement | Targets | Notes |
|---|---|---|---|---|---|
| M010-01 | positional_statistic | a | positional distribution: INITIAL position, frequency 17, distributional assignment; restated as consistent in the V18 upgrade | — | — |
| M010-02 | self_assertion | b | the basis asserts the sign 'has specific PDR reading' | — | Reason: the adjudication's words: an input, not corroboration — the candidate system's own assertion about its reading, filed as part of the basis Target note: the assertion names no other reading; it is the system's own claim about this reading |
| M010-03 | dictionary_entry | a | commodity phoneme corroboration: PDr 'akatti' = agate (DEDR 7) | — | — |

- Note: the Phase-255 segment truncates in the basis as filed at 'appears'; the seal-count clause is not completed and no motif item is entered for it

## M013 — nakaram (class I, Q4 S)

> Basis as recorded: Exclusive to gharial seals (lift > 5.0); PDR nakaram = crocodile/makara; Source as recorded: +Phase48_validated; Evidence lines the audit counted as independent: 2 (DEDR, ICONOGRAPHIC); Tests filed: drawing, distribution, phonetic_value, meaning Later corrected validation battery: score 2 against a promotion threshold of 2 (positional pass, dedr not_run, bigram pass); moved from requires revalidation to this class.

| Item | Kind | Type | Statement | Targets | Notes |
|---|---|---|---|---|---|
| M013-01 | motif_association | a | the sign is exclusive to gharial seals (filed lift > 5.0) | — | Status: motif evidence not reproducible from held records (standings supplement 2026-11-21, section 3) |
| M013-02 | comparative_lexical | a | PDr nakaram = crocodile/makara (the motif's lexical counterpart) | — | — |
| M013-03 | corrected_validation | a | corrected validation battery: score 2 against a promotion threshold of 2 (positional pass, dedr not_run, bigram pass); the sign was moved from requires revalidation to its filed class on this result | — | — |

## M014 — tiru (class I, Q4 S)

> Basis as recorded: Round 1: INITIAL position (freq=17), distributional assignment; UPGRADED-V18: consistent INITIAL (n=17); has specific PDR reading; Source as recorded: +Phase48_validated; Evidence lines the audit counted as independent: 2 (GRAMMAR); Tests filed: distribution, functional_role Later corrected validation battery: score 2 against a promotion threshold of 2 (positional pass, dedr not_run, bigram pass); moved from requires revalidation to this class.

| Item | Kind | Type | Statement | Targets | Notes |
|---|---|---|---|---|---|
| M014-01 | positional_statistic | a | positional distribution: INITIAL position, frequency 17, distributional assignment; restated as consistent in the V18 upgrade | — | — |
| M014-02 | self_assertion | b | the basis asserts the sign 'has specific PDR reading' | — | Reason: the adjudication's words: an input, not corroboration — the candidate system's own assertion about its reading, filed as part of the basis Target note: the assertion names no other reading; it is the system's own claim about this reading |
| M014-03 | corrected_validation | a | corrected validation battery: score 2 against a promotion threshold of 2 (positional pass, dedr not_run, bigram pass); the sign was moved from requires revalidation to its filed class on this result | — | — |

## M015 — mā (class I, Q4 S)

> Basis as recorded: Round 2: INITIAL position (freq=15), distributional assignment; UPGRADED-V18: consistent INITIAL (n=15); has specific PDR reading; Phase-272: DEDR 4796 injected + existing evidence → HIGH; Dictionary reference as recorded: 4796; Evidence lines the audit counted as independent: 2 (DEDR, GRAMMAR); Tests filed: distribution, phonetic_value, meaning

| Item | Kind | Type | Statement | Targets | Notes |
|---|---|---|---|---|---|
| M015-01 | positional_statistic | a | positional distribution: INITIAL position, frequency 15, distributional assignment; restated as consistent in the V18 upgrade | — | — |
| M015-02 | self_assertion | b | the basis asserts the sign 'has specific PDR reading' | — | Reason: the adjudication's words: an input, not corroboration — the candidate system's own assertion about its reading, filed as part of the basis Target note: the assertion names no other reading; it is the system's own claim about this reading |
| M015-03 | dictionary_entry | a | DEDR 4796 cited for this reading (Phase-272 injection) | — | — |

- Note: the Phase-272 segment's roll-up ('existing evidence → HIGH') is a derivation step of the candidate system, recorded here, not an item (spec section 3.3)

## M016 — kaḷiṟu (class I, Q4 S)

> Basis as recorded: Exclusive to elephant seals (lift > 5.0); PDR kaḷiṟu = male elephant; Evidence lines the audit counted as independent: 2 (DEDR, ICONOGRAPHIC); Tests filed: drawing, distribution, phonetic_value, meaning

| Item | Kind | Type | Statement | Targets | Notes |
|---|---|---|---|---|---|
| M016-01 | motif_association | a | the sign is exclusive to elephant seals (filed lift > 5.0) | — | Status: motif evidence not reproducible from held records (standings supplement 2026-11-21, section 3) |
| M016-02 | comparative_lexical | a | PDr kaḷiṟu = male elephant (the motif's lexical counterpart) | — | — |

## M017 — kai (class I, Q4 S)

> Basis as recorded: Round 1: INITIAL position (freq=18), distributional assignment; UPGRADED-V18: consistent INITIAL (n=18); has specific PDR reading; Source as recorded: +Phase48_validated; Evidence lines the audit counted as independent: 2 (GRAMMAR); Tests filed: distribution, functional_role Later corrected validation battery: score 2 against a promotion threshold of 2 (positional pass, dedr not_run, bigram pass); moved from requires revalidation to this class.

| Item | Kind | Type | Statement | Targets | Notes |
|---|---|---|---|---|---|
| M017-01 | positional_statistic | a | positional distribution: INITIAL position, frequency 18, distributional assignment; restated as consistent in the V18 upgrade | — | — |
| M017-02 | self_assertion | b | the basis asserts the sign 'has specific PDR reading' | — | Reason: the adjudication's words: an input, not corroboration — the candidate system's own assertion about its reading, filed as part of the basis Target note: the assertion names no other reading; it is the system's own claim about this reading |
| M017-03 | corrected_validation | a | corrected validation battery: score 2 against a promotion threshold of 2 (positional pass, dedr not_run, bigram pass); the sign was moved from requires revalidation to its filed class on this result | — | — |

## M018 — nēr (class I, Q4 S)

> Basis as recorded: Round 1: INITIAL position (freq=18), distributional assignment; UPGRADED-V18: consistent INITIAL (n=18); has specific PDR reading; Source as recorded: +Phase48_validated; Evidence lines the audit counted as independent: 2 (GRAMMAR); Tests filed: distribution, functional_role Later corrected validation battery: score 2 against a promotion threshold of 2 (positional pass, dedr not_run, bigram pass); moved from requires revalidation to this class.

| Item | Kind | Type | Statement | Targets | Notes |
|---|---|---|---|---|---|
| M018-01 | positional_statistic | a | positional distribution: INITIAL position, frequency 18, distributional assignment; restated as consistent in the V18 upgrade | — | — |
| M018-02 | self_assertion | b | the basis asserts the sign 'has specific PDR reading' | — | Reason: the adjudication's words: an input, not corroboration — the candidate system's own assertion about its reading, filed as part of the basis Target note: the assertion names no other reading; it is the system's own claim about this reading |
| M018-03 | corrected_validation | a | corrected validation battery: score 2 against a promotion threshold of 2 (positional pass, dedr not_run, bigram pass); the sign was moved from requires revalidation to its filed class on this result | — | — |

## M020 — kuṉ (class I, Q4 S)

> Basis as recorded: Round 1: INITIAL position (freq=18), distributional assignment; UPGRADED-V18: consistent INITIAL (n=18); has specific PDR reading; Source as recorded: +Phase48_validated; Evidence lines the audit counted as independent: 2 (GRAMMAR); Tests filed: distribution, functional_role Later corrected validation battery: score 2 against a promotion threshold of 2 (positional pass, dedr not_run, bigram pass); moved from requires revalidation to this class.

| Item | Kind | Type | Statement | Targets | Notes |
|---|---|---|---|---|---|
| M020-01 | positional_statistic | a | positional distribution: INITIAL position, frequency 18, distributional assignment; restated as consistent in the V18 upgrade | — | — |
| M020-02 | self_assertion | b | the basis asserts the sign 'has specific PDR reading' | — | Reason: the adjudication's words: an input, not corroboration — the candidate system's own assertion about its reading, filed as part of the basis Target note: the assertion names no other reading; it is the system's own claim about this reading |
| M020-03 | corrected_validation | a | corrected validation battery: score 2 against a promotion threshold of 2 (positional pass, dedr not_run, bigram pass); the sign was moved from requires revalidation to its filed class on this result | — | — |

## M023 — vaḷ (class I, Q4 S)

> Basis as recorded: Round 1: INITIAL position (freq=16), distributional assignment; UPGRADED-V18: consistent INITIAL (n=16); has specific PDR reading; Phase-255: commodity phoneme corroboration — matches PDr 'akatti'=agate (DEDR 7), appears; Evidence lines the audit counted as independent: 2 (CROSSWALK_CORPUS, GRAMMAR); Tests filed: distribution, meaning

| Item | Kind | Type | Statement | Targets | Notes |
|---|---|---|---|---|---|
| M023-01 | positional_statistic | a | positional distribution: INITIAL position, frequency 16, distributional assignment; restated as consistent in the V18 upgrade | — | — |
| M023-02 | self_assertion | b | the basis asserts the sign 'has specific PDR reading' | — | Reason: the adjudication's words: an input, not corroboration — the candidate system's own assertion about its reading, filed as part of the basis Target note: the assertion names no other reading; it is the system's own claim about this reading |
| M023-03 | dictionary_entry | a | commodity phoneme corroboration: PDr 'akatti' = agate (DEDR 7) | — | — |

- Note: the Phase-255 segment truncates in the basis as filed at 'appears'; the seal-count clause is not completed and no motif item is entered for it

## M025 — cem (class I, Q4 S)

> Basis as recorded: Round 1: INITIAL position (freq=17), distributional assignment; UPGRADED-V18: consistent INITIAL (n=17); has specific PDR reading; Phase-255: commodity phoneme corroboration — matches PDr 'cempu'=copper (DEDR 2781), appe; Evidence lines the audit counted as independent: 2 (CROSSWALK_CORPUS, GRAMMAR); Tests filed: distribution, meaning

| Item | Kind | Type | Statement | Targets | Notes |
|---|---|---|---|---|---|
| M025-01 | positional_statistic | a | positional distribution: INITIAL position, frequency 17, distributional assignment; restated as consistent in the V18 upgrade | — | — |
| M025-02 | self_assertion | b | the basis asserts the sign 'has specific PDR reading' | — | Reason: the adjudication's words: an input, not corroboration — the candidate system's own assertion about its reading, filed as part of the basis Target note: the assertion names no other reading; it is the system's own claim about this reading |
| M025-03 | dictionary_entry | a | commodity phoneme corroboration: PDr 'cempu' = copper (DEDR 2781) | — | — |

- Note: the Phase-255 segment truncates in the basis as filed at 'appe'; the seal-count clause is not completed and no motif item is entered for it

## M026 — mā (class I, Q4 S)

> Basis as recorded: Round 1: INITIAL position (freq=17), distributional assignment; UPGRADED-V18: consistent INITIAL (n=17); has specific PDR reading; Source as recorded: +Phase48_validated; Evidence lines the audit counted as independent: 2 (GRAMMAR); Tests filed: distribution, functional_role Later corrected validation battery: score 2 against a promotion threshold of 2 (positional pass, dedr not_run, bigram pass); moved from requires revalidation to this class.

| Item | Kind | Type | Statement | Targets | Notes |
|---|---|---|---|---|---|
| M026-01 | positional_statistic | a | positional distribution: INITIAL position, frequency 17, distributional assignment; restated as consistent in the V18 upgrade | — | — |
| M026-02 | self_assertion | b | the basis asserts the sign 'has specific PDR reading' | — | Reason: the adjudication's words: an input, not corroboration — the candidate system's own assertion about its reading, filed as part of the basis Target note: the assertion names no other reading; it is the system's own claim about this reading |
| M026-03 | corrected_validation | a | corrected validation battery: score 2 against a promotion threshold of 2 (positional pass, dedr not_run, bigram pass); the sign was moved from requires revalidation to its filed class on this result | — | — |

## M027 — māṟ (class I, Q4 S)

> Basis as recorded: Round 1: INITIAL position (freq=17), distributional assignment; UPGRADED-V18: consistent INITIAL (n=17); has specific PDR reading; Source as recorded: +Phase48_validated; Evidence lines the audit counted as independent: 2 (GRAMMAR); Tests filed: distribution, functional_role Later corrected validation battery: score 2 against a promotion threshold of 2 (positional pass, dedr not_run, bigram pass); moved from requires revalidation to this class.

| Item | Kind | Type | Statement | Targets | Notes |
|---|---|---|---|---|---|
| M027-01 | positional_statistic | a | positional distribution: INITIAL position, frequency 17, distributional assignment; restated as consistent in the V18 upgrade | — | — |
| M027-02 | self_assertion | b | the basis asserts the sign 'has specific PDR reading' | — | Reason: the adjudication's words: an input, not corroboration — the candidate system's own assertion about its reading, filed as part of the basis Target note: the assertion names no other reading; it is the system's own claim about this reading |
| M027-03 | corrected_validation | a | corrected validation battery: score 2 against a promotion threshold of 2 (positional pass, dedr not_run, bigram pass); the sign was moved from requires revalidation to its filed class on this result | — | — |

## M029 — yānai (class I, Q4 S)

> Basis as recorded: Round 3: INITIAL position (freq=11), distributional assignment [Phase-216: SA-cons=0.17 DEDR✓ source=Parpola 1994+]; Source as recorded: Parpola 1994+; Evidence lines the audit counted as independent: 2 (GRAMMAR, LITERATURE); Tests filed: distribution, phonetic_value, meaning

| Item | Kind | Type | Statement | Targets | Notes |
|---|---|---|---|---|---|
| M029-01 | positional_statistic | a | positional distribution: INITIAL position, frequency 11, distributional assignment | — | — |
| M029-02 | consistency_score | ambiguous | candidate-system consistency score: SA-cons=0.17 | — | Reason: the filed basis states the score but no definition of its inputs; whether it is computed over primary data or over interpreted material is not stated, so it is recorded ambiguous under spec section 3.4 |

## M030 — kō (class I, Q4 S)

> Basis as recorded: Round 1: INITIAL position (freq=18), distributional assignment; UPGRADED-V18: consistent INITIAL (n=18); HIGH-anchor collocate M342 (n=4); has specific PDR reading; Source as recorded: +Phase48_validated; Evidence lines the audit counted as independent: 2 (GRAMMAR); Tests filed: distribution, functional_role Later corrected validation battery: score 2 against a promotion threshold of 2 (positional pass, dedr not_run, bigram pass); moved from requires revalidation to this class.

| Item | Kind | Type | Statement | Targets | Notes |
|---|---|---|---|---|---|
| M030-01 | positional_statistic | a | positional distribution: INITIAL position, frequency 18, distributional assignment; restated as consistent in the V18 upgrade | — | — |
| M030-02 | self_assertion | b | the basis asserts the sign 'has specific PDR reading' | — | Reason: the adjudication's words: an input, not corroboration — the candidate system's own assertion about its reading, filed as part of the basis Target note: the assertion names no other reading; it is the system's own claim about this reading |
| M030-03 | corpus_count | a | raw co-occurrence count with M342: n=4 | — | — |
| M030-04 | interpreted_anchor | b | collocation premise: this sign collocates with M342 as a HIGH anchor | M342 | Reason: the premise is M342 under its interpreted reading and HIGH standing; the raw count is carried separately as an (a) item |
| M030-05 | corrected_validation | a | corrected validation battery: score 2 against a promotion threshold of 2 (positional pass, dedr not_run, bigram pass); the sign was moved from requires revalidation to its filed class on this result | — | — |

## M032 — koL (class I, Q4 S)

> Basis as recorded: [Phase-116 recal: SA-cons=0.12✓ DEDR✓]; Source as recorded: Phase-89 systematic DEDR (ICON, MEDIUM); Dictionary reference as recorded: DEDR 2173; Gloss as recorded: take/hold; Evidence lines the audit counted as independent: 1 (DEDR); Tests filed: phonetic_value, meaning

| Item | Kind | Type | Statement | Targets | Notes |
|---|---|---|---|---|---|
| M032-01 | consistency_score | ambiguous | candidate-system consistency score: SA-cons=0.12 | — | Reason: the filed basis states the score but no definition of its inputs; whether it is computed over primary data or over interpreted material is not stated, so it is recorded ambiguous under spec section 3.4 |
| M032-02 | dictionary_entry | a | DEDR 2173 recorded as this reading's dictionary reference | — | — |

## M034 — tōḷ (class I, Q4 S)

> Basis as recorded: Round 1: INITIAL position (freq=17), distributional assignment; UPGRADED-V18: consistent INITIAL (n=17); has specific PDR reading; Source as recorded: +Phase48_validated; Evidence lines the audit counted as independent: 2 (GRAMMAR); Tests filed: distribution, functional_role Later corrected validation battery: score 2 against a promotion threshold of 2 (positional pass, dedr not_run, bigram pass); moved from requires revalidation to this class.

| Item | Kind | Type | Statement | Targets | Notes |
|---|---|---|---|---|---|
| M034-01 | positional_statistic | a | positional distribution: INITIAL position, frequency 17, distributional assignment; restated as consistent in the V18 upgrade | — | — |
| M034-02 | self_assertion | b | the basis asserts the sign 'has specific PDR reading' | — | Reason: the adjudication's words: an input, not corroboration — the candidate system's own assertion about its reading, filed as part of the basis Target note: the assertion names no other reading; it is the system's own claim about this reading |
| M034-03 | corrected_validation | a | corrected validation battery: score 2 against a promotion threshold of 2 (positional pass, dedr not_run, bigram pass); the sign was moved from requires revalidation to its filed class on this result | — | — |

## M037 — kēḷ (class I, Q4 S)

> Basis as recorded: Round 2: INITIAL position (freq=16), distributional assignment; UPGRADED-V18: consistent INITIAL (n=16); HIGH-anchor collocate M267 (n=4); has specific PDR reading; Phase-272: DEDR 2017 injected + existing evidence → HIG; Dictionary reference as recorded: 2017; Evidence lines the audit counted as independent: 2 (DEDR, GRAMMAR); Tests filed: distribution, phonetic_value, meaning

| Item | Kind | Type | Statement | Targets | Notes |
|---|---|---|---|---|---|
| M037-01 | positional_statistic | a | positional distribution: INITIAL position, frequency 16, distributional assignment; restated as consistent in the V18 upgrade | — | — |
| M037-02 | self_assertion | b | the basis asserts the sign 'has specific PDR reading' | — | Reason: the adjudication's words: an input, not corroboration — the candidate system's own assertion about its reading, filed as part of the basis Target note: the assertion names no other reading; it is the system's own claim about this reading |
| M037-03 | corpus_count | a | raw co-occurrence count with M267: n=4 | — | — |
| M037-04 | interpreted_anchor | b | collocation premise: this sign collocates with M267 as a HIGH anchor | M267 | Reason: the premise is M267 under its interpreted reading and HIGH standing; the raw count is carried separately as an (a) item |
| M037-05 | dictionary_entry | a | DEDR 2017 cited for this reading (Phase-272 injection) | — | — |

- Note: the Phase-272 segment's roll-up ('existing evidence → HIGH') is a derivation step of the candidate system, recorded here, not an item (spec section 3.3)

## M038 — pōr (class I, Q4 S)

> Basis as recorded: Round 1: INITIAL position (freq=17), distributional assignment; UPGRADED-V18: consistent INITIAL (n=17); has specific PDR reading; Phase-272: DEDR 4605 injected + existing evidence → HIGH; Dictionary reference as recorded: 4605; Evidence lines the audit counted as independent: 2 (DEDR, GRAMMAR); Tests filed: distribution, phonetic_value, meaning

| Item | Kind | Type | Statement | Targets | Notes |
|---|---|---|---|---|---|
| M038-01 | positional_statistic | a | positional distribution: INITIAL position, frequency 17, distributional assignment; restated as consistent in the V18 upgrade | — | — |
| M038-02 | self_assertion | b | the basis asserts the sign 'has specific PDR reading' | — | Reason: the adjudication's words: an input, not corroboration — the candidate system's own assertion about its reading, filed as part of the basis Target note: the assertion names no other reading; it is the system's own claim about this reading |
| M038-03 | dictionary_entry | a | DEDR 4605 cited for this reading (Phase-272 injection) | — | — |

- Note: the Phase-272 segment's roll-up ('existing evidence → HIGH') is a derivation step of the candidate system, recorded here, not an item (spec section 3.3)

## M041 — pēr (class I, Q4 S)

> Basis as recorded: Round 1: INITIAL position (freq=17), distributional assignment; UPGRADED-V18: consistent INITIAL (n=17); has specific PDR reading; Source as recorded: +Phase48_validated; Evidence lines the audit counted as independent: 2 (GRAMMAR); Tests filed: distribution, functional_role Later corrected validation battery: score 2 against a promotion threshold of 2 (positional pass, dedr not_run, bigram pass); moved from requires revalidation to this class.

| Item | Kind | Type | Statement | Targets | Notes |
|---|---|---|---|---|---|
| M041-01 | positional_statistic | a | positional distribution: INITIAL position, frequency 17, distributional assignment; restated as consistent in the V18 upgrade | — | — |
| M041-02 | self_assertion | b | the basis asserts the sign 'has specific PDR reading' | — | Reason: the adjudication's words: an input, not corroboration — the candidate system's own assertion about its reading, filed as part of the basis Target note: the assertion names no other reading; it is the system's own claim about this reading |
| M041-03 | corrected_validation | a | corrected validation battery: score 2 against a promotion threshold of 2 (positional pass, dedr not_run, bigram pass); the sign was moved from requires revalidation to its filed class on this result | — | — |

## M045 — yānai (class I, Q4 S)

> Basis as recorded: Exclusive to elephant seals (lift > 5.0); PDR yānai = elephant; Evidence lines the audit counted as independent: 2 (DEDR, ICONOGRAPHIC); Tests filed: drawing, distribution, phonetic_value, meaning

| Item | Kind | Type | Statement | Targets | Notes |
|---|---|---|---|---|---|
| M045-01 | motif_association | a | the sign is exclusive to elephant seals (filed lift > 5.0) | — | Status: motif evidence not reproducible from held records (standings supplement 2026-11-21, section 3) |
| M045-02 | comparative_lexical | a | PDr yānai = elephant (the motif's lexical counterpart) | — | — |

## M049 — pu (class I, Q4 S)

> Basis as recorded: [Phase-116 recal: SA-cons=0.12✓ DEDR✓]; Source as recorded: Phase-80 DEDR rebus (puL = DEDR 4349); Dictionary reference as recorded: DEDR 4349; Gloss as recorded: fish+mark -> puL (bird/mark on fish); Evidence lines the audit counted as independent: 1 (DEDR); Tests filed: phonetic_value, meaning

| Item | Kind | Type | Statement | Targets | Notes |
|---|---|---|---|---|---|
| M049-01 | consistency_score | ambiguous | candidate-system consistency score: SA-cons=0.12 | — | Reason: the filed basis states the score but no definition of its inputs; whether it is computed over primary data or over interpreted material is not stated, so it is recorded ambiguous under spec section 3.4 |
| M049-02 | dictionary_entry | a | DEDR 4349 recorded as this reading's dictionary reference | — | — |
| M049-03 | iconographic_interpretation | a | rebus derivation as filed: fish+mark -> puL (bird/mark on fish) | — | — |

## M050 — pār (class I, Q4 S)

> Basis as recorded: Round 1: INITIAL position (freq=17), distributional assignment; UPGRADED-V18: consistent INITIAL (n=17); has specific PDR reading; Phase-272: DEDR 4084 injected + existing evidence → HIGH; Dictionary reference as recorded: 4084; Evidence lines the audit counted as independent: 2 (DEDR, GRAMMAR); Tests filed: distribution, phonetic_value, meaning

| Item | Kind | Type | Statement | Targets | Notes |
|---|---|---|---|---|---|
| M050-01 | positional_statistic | a | positional distribution: INITIAL position, frequency 17, distributional assignment; restated as consistent in the V18 upgrade | — | — |
| M050-02 | self_assertion | b | the basis asserts the sign 'has specific PDR reading' | — | Reason: the adjudication's words: an input, not corroboration — the candidate system's own assertion about its reading, filed as part of the basis Target note: the assertion names no other reading; it is the system's own claim about this reading |
| M050-03 | dictionary_entry | a | DEDR 4084 cited for this reading (Phase-272 injection) | — | — |

- Note: the Phase-272 segment's roll-up ('existing evidence → HIGH') is a derivation step of the candidate system, recorded here, not an item (spec section 3.3)

## M051 — pū/puḷ (class I, Q4 N)

> Basis as recorded: Comb/flower sign; Source as recorded: +Phase48_validated; Evidence lines the audit counted as independent: 1 (ICONOGRAPHIC); Tests filed: drawing, meaning Later corrected validation battery: score 2 against a promotion threshold of 2 (positional pass, dedr not_run, bigram pass); moved from requires revalidation to this class.

| Item | Kind | Type | Statement | Targets | Notes |
|---|---|---|---|---|---|
| M051-01 | iconographic_interpretation | a | comb/flower sign, read pu/pul | — | — |
| M051-02 | corrected_validation | a | corrected validation battery: score 2 against a promotion threshold of 2 (positional pass, dedr not_run, bigram pass); the sign was moved from requires revalidation to its filed class on this result | — | — |

## M052 — ta (class I, Q4 S)

> Basis as recorded: [Phase-116 recal: SA-cons=0.12✓ DEDR✓]; Source as recorded: Phase-80 DEDR rebus (taNal = DEDR 3036); Dictionary reference as recorded: DEDR 3036; Gloss as recorded: fish+stroke -> taNal (mark on fish); Evidence lines the audit counted as independent: 1 (DEDR); Tests filed: phonetic_value, meaning

| Item | Kind | Type | Statement | Targets | Notes |
|---|---|---|---|---|---|
| M052-01 | consistency_score | ambiguous | candidate-system consistency score: SA-cons=0.12 | — | Reason: the filed basis states the score but no definition of its inputs; whether it is computed over primary data or over interpreted material is not stated, so it is recorded ambiguous under spec section 3.4 |
| M052-02 | dictionary_entry | a | DEDR 3036 recorded as this reading's dictionary reference | — | — |
| M052-03 | iconographic_interpretation | a | rebus derivation as filed: fish+stroke -> taNal (mark on fish) | — | — |

## M053 — mi (class I, Q4 S)

> Basis as recorded: [Phase-216: SA-cons=0.17 DEDR✓ source=Phase-80 DEDR rebus (miiN = DEDR 4839)]; Source as recorded: Phase-80 DEDR rebus (miiN = DEDR 4839); Dictionary reference as recorded: DEDR 4839; Gloss as recorded: fish variant -> miiN (fish variant); Evidence lines the audit counted as independent: 1 (DEDR); Tests filed: phonetic_value, meaning

| Item | Kind | Type | Statement | Targets | Notes |
|---|---|---|---|---|---|
| M053-01 | consistency_score | ambiguous | candidate-system consistency score: SA-cons=0.17 | — | Reason: the filed basis states the score but no definition of its inputs; whether it is computed over primary data or over interpreted material is not stated, so it is recorded ambiguous under spec section 3.4 |
| M053-02 | dictionary_entry | a | DEDR 4839 recorded as this reading's dictionary reference | — | — |
| M053-03 | iconographic_interpretation | a | rebus derivation as filed: fish variant -> miiN (fish variant) | — | — |

## M054 — mi (class I, Q4 S)

> Basis as recorded: [Phase-216: SA-cons=0.17 DEDR✓ source=Phase-80 DEDR rebus (miiNDu = DEDR 4855)]; Source as recorded: Phase-80 DEDR rebus (miiNDu = DEDR 4855); Dictionary reference as recorded: DEDR 4855; Gloss as recorded: fish+two -> miiNDu (fish again); Evidence lines the audit counted as independent: 1 (DEDR); Tests filed: phonetic_value, meaning

| Item | Kind | Type | Statement | Targets | Notes |
|---|---|---|---|---|---|
| M054-01 | consistency_score | ambiguous | candidate-system consistency score: SA-cons=0.17 | — | Reason: the filed basis states the score but no definition of its inputs; whether it is computed over primary data or over interpreted material is not stated, so it is recorded ambiguous under spec section 3.4 |
| M054-02 | dictionary_entry | a | DEDR 4855 recorded as this reading's dictionary reference | — | — |
| M054-03 | iconographic_interpretation | a | rebus derivation as filed: fish+two -> miiNDu (fish again) | — | — |

## M055 — miN3 (class I, Q4 S)

> Basis as recorded: [Phase-216: SA-cons=0.17 DEDR✓ source=Phase-89 systematic DEDR (ICON, MEDIUM)]; Source as recorded: Phase-89 systematic DEDR (ICON, MEDIUM); Dictionary reference as recorded: DEDR 4826; Gloss as recorded: fish+3; Evidence lines the audit counted as independent: 1 (DEDR); Tests filed: phonetic_value, meaning

| Item | Kind | Type | Statement | Targets | Notes |
|---|---|---|---|---|---|
| M055-01 | consistency_score | ambiguous | candidate-system consistency score: SA-cons=0.17 | — | Reason: the filed basis states the score but no definition of its inputs; whether it is computed over primary data or over interpreted material is not stated, so it is recorded ambiguous under spec section 3.4 |
| M055-02 | dictionary_entry | a | DEDR 4826 recorded as this reading's dictionary reference | — | — |
| M055-03 | iconographic_interpretation | a | rebus derivation as filed: fish+3 | — | — |

## M057 — māṭu (class I, Q4 S)

> Basis as recorded: Exclusive to zebu bull seals (lift > 5.0); PDR māṭu = cattle; Source as recorded: +Phase48_validated; Evidence lines the audit counted as independent: 2 (DEDR, ICONOGRAPHIC); Tests filed: drawing, distribution, phonetic_value, meaning Later corrected validation battery: score 2 against a promotion threshold of 2 (positional pass, dedr not_run, bigram pass); moved from requires revalidation to this class.

| Item | Kind | Type | Statement | Targets | Notes |
|---|---|---|---|---|---|
| M057-01 | motif_association | a | the sign is exclusive to zebu bull seals (filed lift > 5.0) | — | Status: motif evidence not reproducible from held records (standings supplement 2026-11-21, section 3) |
| M057-02 | comparative_lexical | a | PDr māṭu = cattle (the motif's lexical counterpart) | — | — |
| M057-03 | corrected_validation | a | corrected validation battery: score 2 against a promotion threshold of 2 (positional pass, dedr not_run, bigram pass); the sign was moved from requires revalidation to its filed class on this result | — | — |

## M060 — kāṇṭāmirukam (class I, Q4 S)

> Basis as recorded: Exclusive to rhinoceros seals (lift > 5.0); PDR kāṇṭāmirukam = rhinoceros (horn-beast); Source as recorded: +Phase48_validated; Evidence lines the audit counted as independent: 2 (DEDR, ICONOGRAPHIC); Tests filed: drawing, distribution, phonetic_value, meaning Later corrected validation battery: score 2 against a promotion threshold of 2 (positional pass, dedr not_run, bigram pass); moved from requires revalidation to this class.

| Item | Kind | Type | Statement | Targets | Notes |
|---|---|---|---|---|---|
| M060-01 | motif_association | a | the sign is exclusive to rhinoceros seals (filed lift > 5.0) | — | Status: motif evidence not reproducible from held records (standings supplement 2026-11-21, section 3) |
| M060-02 | comparative_lexical | a | PDr kāṇṭāmirukam = rhinoceros (horn-beast) (the motif's lexical counterpart) | — | — |
| M060-03 | corrected_validation | a | corrected validation battery: score 2 against a promotion threshold of 2 (positional pass, dedr not_run, bigram pass); the sign was moved from requires revalidation to its filed class on this result | — | — |

## M061 — ka (class I, Q4 S)

> Basis as recorded: [Phase-116 recal: SA-cons=0.25✓ DEDR✓]; Source as recorded: Phase-80 DEDR rebus (kaNan = DEDR 1166); Dictionary reference as recorded: DEDR 1166; Gloss as recorded: bull+sign -> kaNan (bull+marker); Evidence lines the audit counted as independent: 1 (DEDR); Tests filed: phonetic_value, meaning

| Item | Kind | Type | Statement | Targets | Notes |
|---|---|---|---|---|---|
| M061-01 | consistency_score | ambiguous | candidate-system consistency score: SA-cons=0.25 | — | Reason: the filed basis states the score but no definition of its inputs; whether it is computed over primary data or over interpreted material is not stated, so it is recorded ambiguous under spec section 3.4 |
| M061-02 | dictionary_entry | a | DEDR 1166 recorded as this reading's dictionary reference | — | — |
| M061-03 | iconographic_interpretation | a | rebus derivation as filed: bull+sign -> kaNan (bull+marker) | — | — |

## M062 — erutu (class I, Q4 S)

> Basis as recorded: Exclusive to zebu bull seals (lift > 5.0); PDR erutu = bull, ox; Evidence lines the audit counted as independent: 2 (DEDR, ICONOGRAPHIC); Tests filed: drawing, distribution, phonetic_value, meaning

| Item | Kind | Type | Statement | Targets | Notes |
|---|---|---|---|---|---|
| M062-01 | motif_association | a | the sign is exclusive to zebu bull seals (filed lift > 5.0) | — | Status: motif evidence not reproducible from held records (standings supplement 2026-11-21, section 3) |
| M062-02 | comparative_lexical | a | PDr erutu = bull, ox (the motif's lexical counterpart) | — | — |

## M063 — mutalai (class I, Q4 S)

> Basis as recorded: FACT-CHECK CORRECTION 2026-05-11: Original V7 assignment was HIGH based on claimed 'lift > 5.0 on gharial seals'. Actual measured gharial lift = 4.35 (below threshold). M063 appears on 3/18 seals with gharial motif (vs. ; Source as recorded: +Phase48_validated; Evidence lines the audit counted as independent: 2 (DEDR, ICONOGRAPHIC); Tests filed: drawing, distribution, phonetic_value, meaning Later corrected validation battery: score 2 against a promotion threshold of 2 (positional pass, dedr not_run, bigram pass); moved from requires revalidation to this class.

| Item | Kind | Type | Statement | Targets | Notes |
|---|---|---|---|---|---|
| M063-01 | motif_association | a | M063 appears on 3/18 seals with gharial motif; the measured gharial lift is 4.35 | — | Status: the original filed claim (lift > 5.0 on gharial seals, HIGH) FAILED as specified: measured lift 4.35 < 5.0 (standings supplement section 4; the 2026-05-11 fact-check correction in the basis) |
| M063-02 | corrected_validation | a | corrected validation battery: score 2 against a promotion threshold of 2 (positional pass, dedr not_run, bigram pass); the sign was moved from requires revalidation to its filed class on this result | — | — |

- Note: the basis truncates at '(vs. ;' — the comparison clause is not completed in the basis as filed

## M065 — kuTam (class I, Q4 S)

> Basis as recorded: ; Phase-255: commodity phoneme corroboration — matches PDr 'akatti'=agate (DEDR 7), appears on 49 trade/zebu seals; Source as recorded: Phase-50+Parpola; Gloss as recorded: jar/pot [kuTam]; Evidence lines the audit counted as independent: 2 (CROSSWALK_CORPUS, LITERATURE); Tests filed: distribution, phonetic_value, meaning

| Item | Kind | Type | Statement | Targets | Notes |
|---|---|---|---|---|---|
| M065-01 | dictionary_entry | a | commodity phoneme corroboration: PDr 'akatti' = agate (DEDR 7) | — | — |
| M065-02 | motif_association | a | the sign appears on 49 trade/zebu seals | — | — |

- Note: the Phase-255 corroboration names PDr 'akatti' = agate (DEDR 7), which is not this reading's gloss as recorded (jar/pot); the corroboration is entered as filed and the mismatch recorded, not resolved

## M066 — cōḻ (class I, Q4 S)

> Basis as recorded: Round 1: INITIAL position (freq=16), distributional assignment; UPGRADED-V18: consistent INITIAL (n=16); has specific PDR reading; Phase-272: DEDR 2905 injected + existing evidence → HIGH; Dictionary reference as recorded: 2905; Evidence lines the audit counted as independent: 2 (DEDR, GRAMMAR); Tests filed: distribution, phonetic_value, meaning

| Item | Kind | Type | Statement | Targets | Notes |
|---|---|---|---|---|---|
| M066-01 | positional_statistic | a | positional distribution: INITIAL position, frequency 16, distributional assignment; restated as consistent in the V18 upgrade | — | — |
| M066-02 | self_assertion | b | the basis asserts the sign 'has specific PDR reading' | — | Reason: the adjudication's words: an input, not corroboration — the candidate system's own assertion about its reading, filed as part of the basis Target note: the assertion names no other reading; it is the system's own claim about this reading |
| M066-03 | dictionary_entry | a | DEDR 2905 cited for this reading (Phase-272 injection) | — | — |

- Note: the Phase-272 segment's roll-up ('existing evidence → HIGH') is a derivation step of the candidate system, recorded here, not an item (spec section 3.3)

## M067 — kōṭṭāṉ (class I, Q4 S)

> Basis as recorded: Exclusive to rhinoceros seals (lift > 5.0); PDR kōṭṭāṉ = horned one; Phase-272: DEDR 2071 injected + existing evidence → HIGH; Dictionary reference as recorded: 2071; Evidence lines the audit counted as independent: 2 (DEDR, ICONOGRAPHIC); Tests filed: drawing, distribution, phonetic_value, meaning

| Item | Kind | Type | Statement | Targets | Notes |
|---|---|---|---|---|---|
| M067-01 | dictionary_entry | a | DEDR 2071 cited for this reading (Phase-272 injection) | — | — |
| M067-02 | motif_association | a | the sign is exclusive to rhinoceros seals (filed lift > 5.0) | — | Status: motif evidence not reproducible from held records (standings supplement 2026-11-21, section 3) |
| M067-03 | comparative_lexical | a | PDr kōṭṭāṉ = horned one (the motif's lexical counterpart) | — | — |

- Note: the Phase-272 segment's roll-up ('existing evidence → HIGH') is a derivation step of the candidate system, recorded here, not an item (spec section 3.3)

## M068 — maṟi (class I, Q4 S)

> Basis as recorded: Exclusive to rhinoceros seals (lift > 5.0); PDR maṟi = young animal/calf (generic); UPGRADED-V18: HIGH-anchor collocate M342 (n=4); has specific PDR reading; Phase-272: DEDR 4706 injected + existing evidence → HIGH; Dictionary reference as recorded: 4706; Evidence lines the audit counted as independent: 2 (DEDR, ICONOGRAPHIC); Tests filed: drawing, distribution, phonetic_value, meaning

| Item | Kind | Type | Statement | Targets | Notes |
|---|---|---|---|---|---|
| M068-01 | self_assertion | b | the basis asserts the sign 'has specific PDR reading' | — | Reason: the adjudication's words: an input, not corroboration — the candidate system's own assertion about its reading, filed as part of the basis Target note: the assertion names no other reading; it is the system's own claim about this reading |
| M068-02 | corpus_count | a | raw co-occurrence count with M342: n=4 | — | — |
| M068-03 | interpreted_anchor | b | collocation premise: this sign collocates with M342 as a HIGH anchor | M342 | Reason: the premise is M342 under its interpreted reading and HIGH standing; the raw count is carried separately as an (a) item |
| M068-04 | dictionary_entry | a | DEDR 4706 cited for this reading (Phase-272 injection) | — | — |
| M068-05 | motif_association | a | the sign is exclusive to rhinoceros seals (filed lift > 5.0) | — | Status: motif evidence not reproducible from held records (standings supplement 2026-11-21, section 3) |
| M068-06 | comparative_lexical | a | PDr maṟi = young animal/calf (generic) (the motif's lexical counterpart) | — | — |

- Note: the Phase-272 segment's roll-up ('existing evidence → HIGH') is a derivation step of the candidate system, recorded here, not an item (spec section 3.3)

## M069 — nēr (class I, Q4 S)

> Basis as recorded: Round 2: INITIAL position (freq=16), distributional assignment; UPGRADED-V18: consistent INITIAL (n=16); has specific PDR reading; Phase-272: DEDR 3774 injected + existing evidence → HIGH; Dictionary reference as recorded: 3774; Evidence lines the audit counted as independent: 2 (DEDR, GRAMMAR); Tests filed: distribution, phonetic_value, meaning

| Item | Kind | Type | Statement | Targets | Notes |
|---|---|---|---|---|---|
| M069-01 | positional_statistic | a | positional distribution: INITIAL position, frequency 16, distributional assignment; restated as consistent in the V18 upgrade | — | — |
| M069-02 | self_assertion | b | the basis asserts the sign 'has specific PDR reading' | — | Reason: the adjudication's words: an input, not corroboration — the candidate system's own assertion about its reading, filed as part of the basis Target note: the assertion names no other reading; it is the system's own claim about this reading |
| M069-03 | dictionary_entry | a | DEDR 3774 cited for this reading (Phase-272 injection) | — | — |

- Note: the Phase-272 segment's roll-up ('existing evidence → HIGH') is a derivation step of the candidate system, recorded here, not an item (spec section 3.3)

## M070 — vēl (class I, Q4 S)

> Basis as recorded: Round 1: INITIAL position (freq=17), distributional assignment; UPGRADED-V18: consistent INITIAL (n=17); has specific PDR reading; Phase-272: DEDR 5540 injected + existing evidence → HIGH; Dictionary reference as recorded: 5540; Evidence lines the audit counted as independent: 2 (DEDR, GRAMMAR); Tests filed: distribution, phonetic_value, meaning

| Item | Kind | Type | Statement | Targets | Notes |
|---|---|---|---|---|---|
| M070-01 | positional_statistic | a | positional distribution: INITIAL position, frequency 17, distributional assignment; restated as consistent in the V18 upgrade | — | — |
| M070-02 | self_assertion | b | the basis asserts the sign 'has specific PDR reading' | — | Reason: the adjudication's words: an input, not corroboration — the candidate system's own assertion about its reading, filed as part of the basis Target note: the assertion names no other reading; it is the system's own claim about this reading |
| M070-03 | dictionary_entry | a | DEDR 5540 cited for this reading (Phase-272 injection) | — | — |

- Note: the Phase-272 segment's roll-up ('existing evidence → HIGH') is a derivation step of the candidate system, recorded here, not an item (spec section 3.3)

## M073 — kōṉ (class I, Q4 S)

> Basis as recorded: Exclusive to zebu bull seals (lift > 5.0); PDR kōṉ = king (bull metaphor); Source as recorded: +Phase48_validated; Evidence lines the audit counted as independent: 2 (DEDR, ICONOGRAPHIC); Tests filed: drawing, distribution, phonetic_value, meaning Later corrected validation battery: score 2 against a promotion threshold of 2 (positional pass, dedr not_run, bigram pass); moved from requires revalidation to this class.

| Item | Kind | Type | Statement | Targets | Notes |
|---|---|---|---|---|---|
| M073-01 | motif_association | a | the sign is exclusive to zebu bull seals (filed lift > 5.0) | — | — |
| M073-02 | comparative_lexical | a | PDr kōṉ = king (bull metaphor) (the motif's lexical counterpart) | — | — |
| M073-03 | corrected_validation | a | corrected validation battery: score 2 against a promotion threshold of 2 (positional pass, dedr not_run, bigram pass); the sign was moved from requires revalidation to its filed class on this result | — | — |

## M074 — ker (class I, Q4 S)

> Basis as recorded: ; Phase-255: commodity phoneme corroboration — matches PDr 'eḷḷu'=sesame (DEDR 839), appears on 4 trade/zebu seals; Source as recorded: Phase-87 DEDR_REBUS_EXTENDED; Evidence lines the audit counted as independent: 2 (CROSSWALK_CORPUS, DEDR); Tests filed: distribution, phonetic_value, meaning

| Item | Kind | Type | Statement | Targets | Notes |
|---|---|---|---|---|---|
| M074-01 | dictionary_entry | a | commodity phoneme corroboration: PDr 'eḷḷu' = sesame (DEDR 839) | — | — |
| M074-02 | motif_association | a | the sign appears on 4 trade/zebu seals | — | — |

## M075 — māṟ (class I, Q4 S)

> Basis as recorded: Round 2: INITIAL position (freq=14), distributional assignment; UPGRADED-V18: HIGH-anchor collocate M267 (n=4); has specific PDR reading; Phase-272: DEDR 4796 injected + existing evidence → HIGH; Dictionary reference as recorded: 4796; Evidence lines the audit counted as independent: 2 (DEDR, GRAMMAR); Tests filed: distribution, phonetic_value, meaning

| Item | Kind | Type | Statement | Targets | Notes |
|---|---|---|---|---|---|
| M075-01 | positional_statistic | a | positional distribution: INITIAL position, frequency 14, distributional assignment | — | — |
| M075-02 | self_assertion | b | the basis asserts the sign 'has specific PDR reading' | — | Reason: the adjudication's words: an input, not corroboration — the candidate system's own assertion about its reading, filed as part of the basis Target note: the assertion names no other reading; it is the system's own claim about this reading |
| M075-03 | corpus_count | a | raw co-occurrence count with M267: n=4 | — | — |
| M075-04 | interpreted_anchor | b | collocation premise: this sign collocates with M267 as a HIGH anchor | M267 | Reason: the premise is M267 under its interpreted reading and HIGH standing; the raw count is carried separately as an (a) item |
| M075-05 | dictionary_entry | a | DEDR 4796 cited for this reading (Phase-272 injection) | — | — |

- Note: the Phase-272 segment's roll-up ('existing evidence → HIGH') is a derivation step of the candidate system, recorded here, not an item (spec section 3.3)

## M076 — naN (class I, Q4 S)

> Basis as recorded: [Phase-116 recal: SA-cons=0.12✓ DEDR✓]; Source as recorded: Phase-91 threshold-1.0 (score=1.00); Dictionary reference as recorded: DEDR 3537; Gloss as recorded: comb+3 strokes; Evidence lines the audit counted as independent: 1 (DEDR); Tests filed: phonetic_value, meaning

| Item | Kind | Type | Statement | Targets | Notes |
|---|---|---|---|---|---|
| M076-01 | consistency_score | ambiguous | candidate-system consistency score: SA-cons=0.12 | — | Reason: the filed basis states the score but no definition of its inputs; whether it is computed over primary data or over interpreted material is not stated, so it is recorded ambiguous under spec section 3.4 |
| M076-02 | dictionary_entry | a | DEDR 3537 recorded as this reading's dictionary reference | — | — |
| M076-03 | iconographic_interpretation | a | rebus derivation as filed: comb+3 strokes | — | — |

## M078 — cēr (class I, Q4 S)

> Basis as recorded: Round 1: INITIAL position (freq=17), distributional assignment; UPGRADED-V18: consistent INITIAL (n=17); has specific PDR reading; Phase-272: DEDR 2814 injected + existing evidence → HIGH; Dictionary reference as recorded: 2814; Evidence lines the audit counted as independent: 2 (DEDR, GRAMMAR); Tests filed: distribution, phonetic_value, meaning

| Item | Kind | Type | Statement | Targets | Notes |
|---|---|---|---|---|---|
| M078-01 | positional_statistic | a | positional distribution: INITIAL position, frequency 17, distributional assignment; restated as consistent in the V18 upgrade | — | — |
| M078-02 | self_assertion | b | the basis asserts the sign 'has specific PDR reading' | — | Reason: the adjudication's words: an input, not corroboration — the candidate system's own assertion about its reading, filed as part of the basis Target note: the assertion names no other reading; it is the system's own claim about this reading |
| M078-03 | dictionary_entry | a | DEDR 2814 cited for this reading (Phase-272 injection) | — | — |

- Note: the Phase-272 segment's roll-up ('existing evidence → HIGH') is a derivation step of the candidate system, recorded here, not an item (spec section 3.3)

## M080 — vēṅkai (class I, Q4 S)

> Basis as recorded: Exclusive to tiger seals (lift > 5.0); PDR vēṅkai = tiger (poetic); Source as recorded: +Phase48_validated; Evidence lines the audit counted as independent: 2 (DEDR, ICONOGRAPHIC); Tests filed: drawing, distribution, phonetic_value, meaning Later corrected validation battery: score 2 against a promotion threshold of 2 (positional pass, dedr not_run, bigram pass); moved from requires revalidation to this class.

| Item | Kind | Type | Statement | Targets | Notes |
|---|---|---|---|---|---|
| M080-01 | motif_association | a | the sign is exclusive to tiger seals (filed lift > 5.0) | — | Status: motif evidence not reproducible from held records (standings supplement 2026-11-21, section 3) |
| M080-02 | comparative_lexical | a | PDr vēṅkai = tiger (poetic) (the motif's lexical counterpart) | — | — |
| M080-03 | corrected_validation | a | corrected validation battery: score 2 against a promotion threshold of 2 (positional pass, dedr not_run, bigram pass); the sign was moved from requires revalidation to its filed class on this result | — | — |

## M082 — pa (class I, Q4 S)

> Basis as recorded: ; Phase-255: commodity phoneme corroboration — matches PDr 'akatti'=agate (DEDR 7), appears on 3 trade/zebu seals; Source as recorded: Phase-80 DEDR rebus (pal = DEDR 3966); Dictionary reference as recorded: DEDR 3966; Gloss as recorded: plant+stroke -> pal (plant with mark); Evidence lines the audit counted as independent: 2 (CROSSWALK_CORPUS, DEDR); Tests filed: distribution, phonetic_value, meaning

| Item | Kind | Type | Statement | Targets | Notes |
|---|---|---|---|---|---|
| M082-01 | dictionary_entry | a | commodity phoneme corroboration: PDr 'akatti' = agate (DEDR 7) | — | — |
| M082-02 | motif_association | a | the sign appears on 3 trade/zebu seals | — | — |
| M082-03 | dictionary_entry | a | DEDR 3966 recorded as this reading's dictionary reference | — | — |
| M082-04 | iconographic_interpretation | a | rebus derivation as filed: plant+stroke -> pal (plant with mark) | — | — |

## M089 — tu/tū (class I, Q4 N)

> Basis as recorded: Positional analysis; UPGRADED: high frequency (171); consistent TERMINAL position (n=171); collocates with HIGH anchor M342 (n=15); collocates with HIGH anchor M267 (n=6); collocates with HIGH anchor M176 (n=6); collocat; Source as recorded: +Phase48_validated; Evidence lines the audit counted as independent: 2 (GRAMMAR); Tests filed: distribution, functional_role Later corrected validation battery: score 2 against a promotion threshold of 2 (positional pass, dedr not_run, bigram pass); moved from requires revalidation to this class.

| Item | Kind | Type | Statement | Targets | Notes |
|---|---|---|---|---|---|
| M089-01 | positional_statistic | a | positional distribution as upgraded: UPGRADED: high frequency (171); consistent TERMINAL position (n=171) | — | — |
| M089-02 | corpus_count | a | raw co-occurrence count with M342: n=15 | — | Status: counts unreliable: the Tranche 2 rerun record filed contradictory pairs for each collocate (falsifiers annex, Round 2 row annotations, 2026-11-21); the counts are entered as filed |
| M089-03 | interpreted_anchor | b | collocation premise: this sign collocates with M342 as a HIGH anchor | M342 | Reason: the premise is M342 under its interpreted reading and HIGH standing; the raw count is carried separately as an (a) item Status: counts unreliable: the Tranche 2 rerun record filed contradictory pairs for each collocate (falsifiers annex, Round 2 row annotations, 2026-11-21); the counts are entered as filed |
| M089-04 | corpus_count | a | raw co-occurrence count with M267: n=6 | — | Status: counts unreliable: the Tranche 2 rerun record filed contradictory pairs for each collocate (falsifiers annex, Round 2 row annotations, 2026-11-21); the counts are entered as filed |
| M089-05 | interpreted_anchor | b | collocation premise: this sign collocates with M267 as a HIGH anchor | M267 | Reason: the premise is M267 under its interpreted reading and HIGH standing; the raw count is carried separately as an (a) item Status: counts unreliable: the Tranche 2 rerun record filed contradictory pairs for each collocate (falsifiers annex, Round 2 row annotations, 2026-11-21); the counts are entered as filed |
| M089-06 | corpus_count | a | raw co-occurrence count with M176: n=6 | — | Status: counts unreliable: the Tranche 2 rerun record filed contradictory pairs for each collocate (falsifiers annex, Round 2 row annotations, 2026-11-21); the counts are entered as filed |
| M089-07 | interpreted_anchor | b | collocation premise: this sign collocates with M176 as a HIGH anchor | M176 | Reason: the premise is M176 under its interpreted reading and HIGH standing; the raw count is carried separately as an (a) item Status: counts unreliable: the Tranche 2 rerun record filed contradictory pairs for each collocate (falsifiers annex, Round 2 row annotations, 2026-11-21); the counts are entered as filed |
| M089-08 | corrected_validation | a | corrected validation battery: score 2 against a promotion threshold of 2 (positional pass, dedr not_run, bigram pass); the sign was moved from requires revalidation to its filed class on this result | — | — |

- Note: the basis opens with the unelaborated label 'Positional analysis' and truncates at 'collocat;' after the third collocate; no further premise is stated and none is entered
- Note: the adjudication records this reading's upgrade counts as internally inconsistent (Q5 tranche record); the counts are entered as filed
- Note: Round 2 amendment (standings supplement): this reading's class rests on its filed corrected-battery result (score 2), not on the collocation counts

## M099 — kol/koḷ (class I, Q4 N)

> Basis as recorded: Jar/vessel sign; Evidence lines the audit counted as independent: 2 (GRAMMAR, ICONOGRAPHIC); Tests filed: drawing, distribution, functional_role, meaning

| Item | Kind | Type | Statement | Targets | Notes |
|---|---|---|---|---|---|
| M099-01 | iconographic_interpretation | a | jar/vessel sign, read kol/kol | — | — |

- Note: the audit's evidence lines count a GRAMMAR line for this reading, but the basis as filed states no grammatical evidence beyond the iconographic identification; the falsifiers annex records this reading's basis as too thin to falsify

## M128 — kaṇ (class I, Q4 S)

> Basis as recorded: Round 3: MEDIAL position (freq=7), distributional assignment [Phase-116 recal: SA-cons=0.12✓ DEDR✓]; Source as recorded: Parpola 1994+; Evidence lines the audit counted as independent: 2 (GRAMMAR, LITERATURE); Tests filed: distribution, phonetic_value, meaning

| Item | Kind | Type | Statement | Targets | Notes |
|---|---|---|---|---|---|
| M128-01 | positional_statistic | a | positional distribution: MEDIAL position, frequency 7, distributional assignment | — | — |
| M128-02 | consistency_score | ambiguous | candidate-system consistency score: SA-cons=0.12 | — | Reason: the filed basis states the score but no definition of its inputs; whether it is computed over primary data or over interpreted material is not stated, so it is recorded ambiguous under spec section 3.4 |

## M130 — mui (class I, Q4 S)

> Basis as recorded: [Phase-116 recal: SA-cons=0.12✓ DEDR✓]; Source as recorded: Phase-89 systematic DEDR (ICON, MEDIUM); Dictionary reference as recorded: DEDR 4951; Gloss as recorded: sprout/shoot; Evidence lines the audit counted as independent: 1 (DEDR); Tests filed: phonetic_value, meaning

| Item | Kind | Type | Statement | Targets | Notes |
|---|---|---|---|---|---|
| M130-01 | consistency_score | ambiguous | candidate-system consistency score: SA-cons=0.12 | — | Reason: the filed basis states the score but no definition of its inputs; whether it is computed over primary data or over interpreted material is not stated, so it is recorded ambiguous under spec section 3.4 |
| M130-02 | dictionary_entry | a | DEDR 4951 recorded as this reading's dictionary reference | — | — |

## M145 — miṭ (class I, Q4 S)

> Basis as recorded: [Phase-216: SA-cons=0.17 DEDR✓ source=Phase-95 retroflex expansion (score=1.90]; Source as recorded: Phase-95 retroflex expansion (score=1.90); Dictionary reference as recorded: DEDR 4836; Gloss as recorded: fish+mark2; Evidence lines the audit counted as independent: 1 (DEDR); Tests filed: phonetic_value, meaning

| Item | Kind | Type | Statement | Targets | Notes |
|---|---|---|---|---|---|
| M145-01 | consistency_score | ambiguous | candidate-system consistency score: SA-cons=0.17 | — | Reason: the filed basis states the score but no definition of its inputs; whether it is computed over primary data or over interpreted material is not stated, so it is recorded ambiguous under spec section 3.4 |
| M145-02 | dictionary_entry | a | DEDR 4836 recorded as this reading's dictionary reference | — | — |
| M145-03 | consistency_score | ambiguous | Phase-95 retroflex expansion score=1.90 | — | Reason: an internal expansion score whose inputs the filed basis does not state; recorded ambiguous under spec section 3.4 |

## M151 — viḷ (class I, Q4 S)

> Basis as recorded: Round 4: MEDIAL position (freq=5), distributional assignment; Dictionary reference as recorded: 5471; Gloss as recorded: to fall, bow/arrow, jungle; Evidence lines the audit counted as independent: 3 (DEDR, GRAMMAR); Tests filed: distribution, functional_role, phonetic_value, meaning

| Item | Kind | Type | Statement | Targets | Notes |
|---|---|---|---|---|---|
| M151-01 | positional_statistic | a | positional distribution: MEDIAL position, frequency 5, distributional assignment | — | — |
| M151-02 | dictionary_entry | a | DEDR 5471 recorded as this reading's dictionary reference | — | — |

## M194 — kaṭ (class I, Q4 S)

> Basis as recorded: [Phase-116 recal: SA-cons=0.12✓ DEDR✓]; Source as recorded: Phase-95 retroflex expansion (score=1.90); Dictionary reference as recorded: DEDR 1161; Gloss as recorded: pass/cross; Evidence lines the audit counted as independent: 1 (DEDR); Tests filed: phonetic_value, meaning

| Item | Kind | Type | Statement | Targets | Notes |
|---|---|---|---|---|---|
| M194-01 | consistency_score | ambiguous | candidate-system consistency score: SA-cons=0.12 | — | Reason: the filed basis states the score but no definition of its inputs; whether it is computed over primary data or over interpreted material is not stated, so it is recorded ambiguous under spec section 3.4 |
| M194-02 | dictionary_entry | a | DEDR 1161 recorded as this reading's dictionary reference | — | — |
| M194-03 | consistency_score | ambiguous | Phase-95 retroflex expansion score=1.90 | — | Reason: an internal expansion score whose inputs the filed basis does not state; recorded ambiguous under spec section 3.4 |

## M220 — al (class I, Q4 S)

> Basis as recorded: ; Phase-255: commodity phoneme corroboration — matches PDr 'akatti'=agate (DEDR 7), appears on 9 trade/zebu seals; Source as recorded: Phase-89 systematic DEDR (PHON, MEDIUM); Dictionary reference as recorded: DEDR 0180; Gloss as recorded: not/without; Evidence lines the audit counted as independent: 2 (CROSSWALK_CORPUS, DEDR); Tests filed: distribution, phonetic_value, meaning

| Item | Kind | Type | Statement | Targets | Notes |
|---|---|---|---|---|---|
| M220-01 | dictionary_entry | a | commodity phoneme corroboration: PDr 'akatti' = agate (DEDR 7) | — | — |
| M220-02 | motif_association | a | the sign appears on 9 trade/zebu seals | — | — |
| M220-03 | dictionary_entry | a | DEDR 180 recorded as this reading's dictionary reference | — | — |

## M267 — iN/in (genitive of) (class I, Q4 S)

> Basis as recorded: FACT-CHECK CORRECTION 2026-05-11: Original V6 assignment 'min/mīn' (HIGH) was wrong. M267 has freq=400 in the Holdat corpus and appears across ALL motif types (unicorn 127, zebu bull 72, elephant 37, rhinoceros 25, etc.); Source as recorded: Phase-74 grammar z=8.04 p<0.0001 + Phase-64 score=7.0; Dictionary reference as recorded: 494; Gloss as recorded: genitive particle [AGENT]-M267-[TITLE] 4.3x above null; Evidence lines the audit counted as independent: 4 (DEDR, GRAMMAR, LITERATURE); Tests filed: drawing, distribution, functional_role, phonetic_value, meaning

| Item | Kind | Type | Statement | Targets | Notes |
|---|---|---|---|---|---|
| M267-01 | dictionary_entry | a | DEDR 494 recorded as this reading's dictionary reference | — | — |
| M267-02 | corpus_count | a | M267 has freq=400 in the Holdat corpus and appears across all motif types (unicorn 127, zebu bull 72, elephant 37, rhinoceros 25, etc.) | — | Status: the Holdat corpus is unheld in every working clone and no written Miller permission is on file (custody statement 2026-11-21); the counts are as filed |
| M267-03 | positional_statistic | a | Phase-74 grammar statistic for the genitive pattern: z=8.04, p<0.0001 | — | Status: figures withdrawn as evidence (standings supplement section 2, RT1-14): the 4.3x lift and z = 8.038 are withdrawn; the raw counts stand (26 observed vs null mean 6) |
| M267-04 | consistency_score | ambiguous | Phase-64 score=7.0 for this reading | — | Reason: an internal candidate-system score whose inputs the filed basis does not state; recorded ambiguous under spec section 3.4 |
| M267-05 | slot_label | b | the filed pattern [AGENT]-M267-[TITLE]: M267 read as the genitive between an AGENT slot and a TITLE slot (4.3x above null as filed) | M176, M328, M099, M073 | Reason: the AGENT and TITLE slots are constructs of the candidate system, and the pattern's markers are themselves readings: the AGENT markers of record include M176 and M328, the TITLE markers M099 and M073 (standings supplement section 2). The adjudication's words: conditional circularity — not independent confirmation unless the labels are independently justified Target source: standings-supplement-2026-11-21.md Status: figures withdrawn as evidence (standings supplement section 2, RT1-14) |

- Note: the 2026-05-11 fact-check correction records that the original V6 assignment 'min/min' (HIGH) for this sign was wrong; the correction is part of the filed basis
- Note: the dictionary-reference segment (494) is carried as a dictionary item by the template pass

## M347 — ka (class I, Q4 S)

> Basis as recorded: Phase-117 grammar inference: slot=MEDIAL_BETWEEN_CONF, n_contexts=7, patterns=['M342-[M347]-M293', 'M028-[M347]-M367', 'M211-[M347]-M099']. Inferred from Dravidian grammar slot model (Phases 74-112). [Phase-120: grammar ; Source as recorded: Phase-117; Evidence lines the audit counted as independent: 1 (GRAMMAR); Tests filed: distribution, functional_role

| Item | Kind | Type | Statement | Targets | Notes |
|---|---|---|---|---|---|
| M347-01 | slot_label | b | grammar inference: this sign occupies the slot MEDIAL_BETWEEN_CONF in 7 contexts, under the Dravidian grammar slot model (Phases 74-112) | — | Reason: the slot and the slot model are constructs of the candidate system; the inference is filed as 'inferred from Dravidian grammar slot model (Phases 74-112)' Target note: the slot is a model construct; the basis names no single reading as its premise |
| M347-02 | positional_statistic | a | the filed sequence patterns place this sign between named signs in 7 contexts | — | — |
| M347-03 | interpreted_anchor | b | the filed patterns read this sign between M342, M293, M028, M367, M211 and M099 in their interpreted roles | M342, M293, M028, M367, M211, M099 | Reason: the patterns are stated over the other signs in their interpreted roles in the slot model; three of the targets (M293, M028, M211) stand outside the strict core and carry no standings |

- Note: the adjudication's Q3 item 6 struck interpreted-anchor premises M342, M328, M367, M099 from this reading's basis ('essentially all stated grammatical motivation lost'); the M328 premise is not named in the appendix basis as filed and is recorded here, not itemized, so the log does not state what the basis does not
- Note: the basis truncates at '[Phase-120: grammar ;' — the Phase-120 segment is not stated and no item is entered for it

## M351 — vī (class I, Q4 M)

> Basis as recorded: Phase-123 substrate match: Munda 'bi' (seed/sprout). DEDR 5388 vī = seed — attested Tamil/Telugu agricultural vocabulary. Phonological: Munda 'bi' → Dravidian 'vī' (voiced bilabial shift p/b→v). Positional: MEDIAL after ; Source as recorded: Phase-128 substrate upgrade; Dictionary reference as recorded: DEDR 5388 (vī = seed, Tamil/Telugu); Evidence lines the audit counted as independent: 2 (CROSSWALK_CORPUS, DEDR); Tests filed: distribution, functional_role, phonetic_value, meaning

| Item | Kind | Type | Statement | Targets | Notes |
|---|---|---|---|---|---|
| M351-01 | dictionary_entry | a | DEDR 5388 recorded as this reading's dictionary reference | — | — |
| M351-02 | comparative_lexical | a | substrate match: Munda 'bi' (seed/sprout), Witzel tradition as filed | — | — |
| M351-03 | comparative_lexical | a | stated sound correspondence: Munda 'bi' -> Dravidian 'vi' (voiced bilabial shift p/b->v) | — | — |
| M351-04 | positional_statistic | a | positional statement: MEDIAL (the basis truncates after 'after') | — | Status: the basis as filed truncates mid-clause at this item |

## M374 — kul (class I, Q4 M)

> Basis as recorded: Phase-123 substrate match: Munda 'kul' (tiger/king-tiger, Witzel 1999). DEDR 1709 kulam = clan/lineage — attested Tamil noun. Positional: MEDIAL between authority signs (M328=āl/man, M073=kōṉ/king) and vessel/cargo signs; Source as recorded: Phase-128 substrate upgrade; Dictionary reference as recorded: DEDR 1709 (kulam = clan/lineage, Tamil); Evidence lines the audit counted as independent: 2 (CROSSWALK_CORPUS, DEDR); Tests filed: distribution, functional_role, phonetic_value, meaning

| Item | Kind | Type | Statement | Targets | Notes |
|---|---|---|---|---|---|
| M374-01 | dictionary_entry | a | DEDR 1709 recorded as this reading's dictionary reference | — | — |
| M374-02 | comparative_lexical | a | substrate match: Munda 'kul' (tiger/king-tiger, Witzel 1999) | — | — |
| M374-03 | interpreted_anchor | b | positional context: MEDIAL between authority signs (M328=al/man, M073=kon/king) and vessel/cargo signs | M328, M073 | Reason: the context is stated through the other signs under their readings (M328 as al/man, M073 as kon/king): an interpreted context, struck as such by the adjudication's Q3 item 7 |

## M375 — taṇ (class I, Q4 S)

> Basis as recorded: Folded-arm sign ~ taṇ 'cool/refreshing' (DEDR 3009) or taṇṭu 'staff/rod'. Phase-103 NAME_AY_AN pattern: [M375]-M342-M176 (taṇ-ay-an = 'cool/noble man'). Sangam Akam poetry: taṇ- is a common personal name prefix. Freq=7; ; Source as recorded: Phase-105; Evidence lines the audit counted as independent: 3 (DEDR, GRAMMAR, ICONOGRAPHIC); Tests filed: drawing, distribution, functional_role, phonetic_value, meaning

| Item | Kind | Type | Statement | Targets | Notes |
|---|---|---|---|---|---|
| M375-01 | iconographic_interpretation | a | folded-arm sign, read tan 'cool/refreshing' (DEDR 3009) or tantu 'staff/rod' | — | — |
| M375-02 | dictionary_entry | a | DEDR 3009 cited for tan | — | — |
| M375-03 | positional_statistic | a | the filed sequence pattern [M375]-M342-M176 occurs as a sign sequence | — | — |
| M375-04 | interpreted_anchor | b | the NAME_AY_AN pattern read as tan-ay-an = 'cool/noble man' | M342, M176 | Reason: the pattern's reading rests on M342's and M176's readings (ay, an); the adjudication's Q3 item 8 removed this translated pattern as a major argument |
| M375-05 | literary_parallel | a | Sangam Akam poetry: tan- is a common personal name prefix | — | — |
| M375-06 | corpus_count | a | frequency 7 as filed | — | — |

## M391 — ka/kaṇ (class I, Q4 N)

> Basis as recorded: Numeral/stroke sign; Source as recorded: +Phase48_validated; Evidence lines the audit counted as independent: 2 (GRAMMAR); Tests filed: distribution, functional_role Later corrected validation battery: score 2 against a promotion threshold of 2 (positional pass, dedr not_run, bigram pass); moved from requires revalidation to this class.

| Item | Kind | Type | Statement | Targets | Notes |
|---|---|---|---|---|---|
| M391-01 | iconographic_interpretation | a | numeral/stroke sign, read ka/kan | — | Status: numerical claim WEAKENED (standings supplement section 6: stroke-count pattern 2/187 for this sign, against SUFFIX_ONLY 74/187) |
| M391-02 | corrected_validation | a | corrected validation battery: score 2 against a promotion threshold of 2 (positional pass, dedr not_run, bigram pass); the sign was moved from requires revalidation to its filed class on this result | — | — |

## M087 — veL (class R, Q4 S)

> Basis as recorded: [Phase-116 recal: SA-cons=0.12✓ DEDR✓]; Source as recorded: Parpola_1994_via_phase51; Gloss as recorded: white / two strokes; Evidence lines the audit counted as independent: 1 (LITERATURE); Tests filed: phonetic_value, meaning

| Item | Kind | Type | Statement | Targets | Notes |
|---|---|---|---|---|---|
| M087-01 | consistency_score | ambiguous | candidate-system consistency score: SA-cons=0.12 | — | Reason: the filed basis states the score but no definition of its inputs; whether it is computed over primary data or over interpreted material is not stated, so it is recorded ambiguous under spec section 3.4 |
| M087-02 | iconographic_interpretation | a | gloss as recorded: white / two strokes | — | — |

- Note: the filed source attributes the reading to Parpola 1994 (via Phase-51); no DEDR entry number is filed for this sign

## M165 — cul (class R, Q4 S)

> Basis as recorded: Phase-163 sibilant discovery: reading 'cul' found in literature (4 mentions across sources: Parpola_1994). Provides partial coverage for Shu-ilishu /su/ phonological slot. [Phase-216: SA-cons=0.17 DEDR✓ source=Phase-111]; Source as recorded: Phase-111; Evidence lines the audit counted as independent: 1 (LITERATURE); Tests filed: phonetic_value, meaning

| Item | Kind | Type | Statement | Targets | Notes |
|---|---|---|---|---|---|
| M165-01 | consistency_score | ambiguous | candidate-system consistency score: SA-cons=0.17 | — | Reason: the filed basis states the score but no definition of its inputs; whether it is computed over primary data or over interpreted material is not stated, so it is recorded ambiguous under spec section 3.4 |
| M165-02 | published_proposal | a | the reading is filed as found in the literature (4 mentions across sources: Parpola_1994) | — | — |
| M165-03 | slot_label | b | the reading is filed as providing partial coverage for the Shu-ilishu /su/ phonological slot | — | Reason: the /su/ slot is a construct of the candidate system's phonological coverage argument; the coverage claim is evidence only inside that system Target note: the basis names the slot but no reading as its premise |

## M264 — peN (class R, Q4 S)

> Basis as recorded: [Phase-116 recal: SA-cons=0.12✓ DEDR✓]; Source as recorded: Parpola_1994_via_phase51; Gloss as recorded: female / woman; Evidence lines the audit counted as independent: 1 (LITERATURE); Tests filed: phonetic_value, meaning

| Item | Kind | Type | Statement | Targets | Notes |
|---|---|---|---|---|---|
| M264-01 | consistency_score | ambiguous | candidate-system consistency score: SA-cons=0.12 | — | Reason: the filed basis states the score but no definition of its inputs; whether it is computed over primary data or over interpreted material is not stated, so it is recorded ambiguous under spec section 3.4 |
| M264-02 | iconographic_interpretation | a | gloss as recorded: female / woman | — | — |

- Note: the filed source attributes the reading to Parpola 1994 (via Phase-51); no DEDR entry number is filed for this sign

## M311 — vaTamiin (class R, Q4 S)

> Basis as recorded: [Phase-116 recal: SA-cons=0.12✓ DEDR✓]; Source as recorded: Parpola_1994_via_phase51; Gloss as recorded: north star; Evidence lines the audit counted as independent: 1 (LITERATURE); Tests filed: phonetic_value, meaning

| Item | Kind | Type | Statement | Targets | Notes |
|---|---|---|---|---|---|
| M311-01 | consistency_score | ambiguous | candidate-system consistency score: SA-cons=0.12 | — | Reason: the filed basis states the score but no definition of its inputs; whether it is computed over primary data or over interpreted material is not stated, so it is recorded ambiguous under spec section 3.4 |
| M311-02 | iconographic_interpretation | a | gloss as recorded: north star | — | — |

- Note: the filed source attributes the reading to Parpola 1994 (via Phase-51); no DEDR entry number is filed for this sign

## M222 — min (class P, Q4 S)

> Basis as recorded: Promoted from anchor staging archive (2026-06-07T18:20:18Z); evidence_type=compound_slot_coherence; score=1.00; status=verified; DEDR: shine / lightning (verb); Source as recorded: anchor_staging_archive:compound_semantic_coherence; Evidence lines the audit counted as independent: 1 (GRAMMAR); Tests filed: distribution SOURCE CONFLICT: the paper's public anchor table lists this sign's reading as 'kur', while the canonical anchor register and the audit record it as 'min'; the register's own annotation records 'kur' as a superseded earlier reading for this sign. The row follows the register/audit value.

| Item | Kind | Type | Statement | Targets | Notes |
|---|---|---|---|---|---|
| M222-01 | slot_label | b | the reading was promoted on evidence_type=compound_slot_coherence (anchor staging archive) | — | Reason: slot coherence is a construct of the candidate system; the adjudication's Q3 item 10 removed interpreted-context credit for this reading pending provenance Target note: the basis names no individual reading as the coherence premise |
| M222-02 | consistency_score | ambiguous | staging score=1.00, status=verified as filed | — | Reason: an internal staging score whose inputs the filed basis does not state; recorded ambiguous under spec section 3.4 |
| M222-03 | dictionary_entry | a | DEDR gloss as filed: shine / lightning (verb); no DEDR number is filed | — | — |

- Note: SOURCE CONFLICT as filed: the paper's public anchor table lists this sign's reading as 'kur'; the canonical anchor register and the audit record 'min' (MEDIUM), with 'kur' a superseded earlier reading. The log follows the register/audit value, as the appendix row does
- Note: class P as executed is 'pending — no documented expert or referral' (standings supplement section 5)

## M362 — aṇi (class P, Q4 S)

> Basis as recorded: Starburst / asterisk iconography ~ aṇi 'ornament/adorn' (DEDR 0145). Phase-103: appears in name-slot patterns between animal classifiers and titles. Sangam literature: aṇi- prefix in personal names (Aṇi-van, Aṇi-tan). Po; Source as recorded: Phase-105; Evidence lines the audit counted as independent: 3 (DEDR, GRAMMAR, ICONOGRAPHIC); Tests filed: drawing, distribution, functional_role, phonetic_value, meaning

| Item | Kind | Type | Statement | Targets | Notes |
|---|---|---|---|---|---|
| M362-01 | iconographic_interpretation | a | starburst / asterisk iconography, read ani 'ornament/adorn' (DEDR 0145) | — | — |
| M362-02 | dictionary_entry | a | DEDR 145 cited for ani | — | — |
| M362-03 | slot_label | b | the sign appears in name-slot patterns between animal classifiers and titles (Phase-103) | — | Reason: the name-slot pattern and its classifier/title roles are constructs of the candidate system; the adjudication's Q3 item 11 removed interpreted-context credit for this reading pending provenance Target note: the basis names the slot pattern but no individual reading as its premise |
| M362-04 | literary_parallel | a | Sangam literature: ani- prefix in personal names (Ani-van, Ani-tan) | — | — |

- Note: the basis truncates at 'Po;' — the following segment is not stated and no item is entered for it

## M398 — kuṟi (class P, Q4 S)

> Basis as recorded: Hook+ring iconography ~ kuṟi 'mark/sign' (DEDR 1769) or kuṟu 'small/short'. Phase-103: NAME_AY_AN + GENITIVE_NAME_SUFFIX patterns. Pattern [M267]-[M398]-[M342]: 'of-kuṟi-belonging' = genitive personal name. Score 1.2 (hi; Source as recorded: Phase-105; Evidence lines the audit counted as independent: 3 (DEDR, GRAMMAR, ICONOGRAPHIC); Tests filed: drawing, distribution, functional_role, phonetic_value, meaning

| Item | Kind | Type | Statement | Targets | Notes |
|---|---|---|---|---|---|
| M398-01 | iconographic_interpretation | a | hook+ring iconography, read kuri 'mark/sign' (DEDR 1769) or kuru 'small/short' | — | — |
| M398-02 | dictionary_entry | a | DEDR 1769 cited for kuri | — | — |
| M398-03 | slot_label | b | the sign is filed under the NAME_AY_AN + GENITIVE_NAME_SUFFIX patterns (Phase-103) | — | Reason: the named patterns are constructs of the candidate system's name grammar Target note: the pattern names are constructs; the concrete pattern instance is carried as its own item |
| M398-04 | positional_statistic | a | the filed sequence pattern [M267]-[M398]-[M342] occurs as a sign sequence | — | — |
| M398-05 | interpreted_anchor | b | the pattern read as 'of-kuri-belonging' = genitive personal name | M267, M342 | Reason: the reading of the pattern rests on M267's genitive reading and M342's suffix reading; struck as a premise by the adjudication's Q3 item 9 |
| M398-06 | consistency_score | ambiguous | a score of 1.2 is filed for this reading (the basis truncates at '(hi') | — | Reason: an internal score whose definition and inputs the filed basis does not state, and whose statement is itself truncated; recorded ambiguous under spec section 3.4 Status: the basis as filed truncates mid-clause at this item |

## M012 — oṉṟu/1 (class U, Q4 N)

> Basis as recorded: single stroke = numeral 1; Source as recorded: +Phase48_validated; Evidence lines the audit counted as independent: 1 (GRAMMAR); Tests filed: distribution, functional_role Later corrected validation battery: score 1 against a promotion threshold of 2 (positional pass, dedr not_run, bigram fail); moved from requires revalidation to this class.

| Item | Kind | Type | Statement | Targets | Notes |
|---|---|---|---|---|---|
| M012-01 | iconographic_interpretation | a | single stroke, read as the numeral 1 | — | Status: numerical claim WEAKENED (standings supplement section 6: stroke-count pattern 1/141 for this sign) |
| M012-02 | corrected_validation | a | corrected validation battery: score 1 against a promotion threshold of 2 (positional pass, dedr not_run, bigram fail); the sign was moved from requires revalidation to its filed class on this result | — | — |

## M039 — āṉai (class U, Q4 S)

> Basis as recorded: Exclusive to elephant seals (lift > 5.0); PDR āṉai = elephant (variant); Source as recorded: +Phase48_validated; Evidence lines the audit counted as independent: 2 (DEDR, ICONOGRAPHIC); Tests filed: drawing, distribution, phonetic_value, meaning Later corrected validation battery: score 1 against a promotion threshold of 2 (positional pass, dedr not_run, bigram not_run); moved from requires revalidation to this class.

| Item | Kind | Type | Statement | Targets | Notes |
|---|---|---|---|---|---|
| M039-01 | motif_association | a | the sign is exclusive to elephant seals (filed lift > 5.0) | — | — |
| M039-02 | comparative_lexical | a | PDr āṉai = elephant (variant) (the motif's lexical counterpart) | — | — |
| M039-03 | corrected_validation | a | corrected validation battery: score 1 against a promotion threshold of 2 (positional pass, dedr not_run, bigram not_run); the sign was moved from requires revalidation to its filed class on this result | — | — |

## M042 — vaN (class U, Q4 S)

> Basis as recorded: [Phase-116 recal: SA-cons=0.62✓ DEDR✓]; Source as recorded: Phase-89 systematic DEDR (ICON, MEDIUM); Dictionary reference as recorded: DEDR 5231; Gloss as recorded: arch/bow; Evidence lines the audit counted as independent: 1 (GRAMMAR); Tests filed: distribution Later corrected site-statistics check: outcome insufficient data; moved from requires revalidation to this class.

| Item | Kind | Type | Statement | Targets | Notes |
|---|---|---|---|---|---|
| M042-01 | consistency_score | ambiguous | candidate-system consistency score: SA-cons=0.62 | — | Reason: the filed basis states the score but no definition of its inputs; whether it is computed over primary data or over interpreted material is not stated, so it is recorded ambiguous under spec section 3.4 |
| M042-02 | dictionary_entry | a | DEDR 5231 recorded as this reading's dictionary reference | — | — |
| M042-03 | corrected_validation | a | corrected site-statistics check: outcome insufficient data; the sign was moved from requires revalidation to its filed class on this result | — | — |

## M046 — kaL (class U, Q4 S)

> Basis as recorded: [Phase-116 recal: SA-cons=0.12✓ DEDR✓]; Source as recorded: Phase-89 systematic DEDR (ICON, MEDIUM); Dictionary reference as recorded: DEDR 1286; Gloss as recorded: leg/stem; Evidence lines the audit counted as independent: 1 (GRAMMAR); Tests filed: distribution Later corrected site-statistics check: outcome insufficient data; moved from requires revalidation to this class.

| Item | Kind | Type | Statement | Targets | Notes |
|---|---|---|---|---|---|
| M046-01 | consistency_score | ambiguous | candidate-system consistency score: SA-cons=0.12 | — | Reason: the filed basis states the score but no definition of its inputs; whether it is computed over primary data or over interpreted material is not stated, so it is recorded ambiguous under spec section 3.4 |
| M046-02 | dictionary_entry | a | DEDR 1286 recorded as this reading's dictionary reference | — | — |
| M046-03 | corrected_validation | a | corrected site-statistics check: outcome insufficient data; the sign was moved from requires revalidation to its filed class on this result | — | — |

## M048 — mu/muṉ (class U, Q4 N)

> Basis as recorded: Positional analysis; UPGRADED: high frequency (157); consistent TERMINAL position (n=157); collocates with HIGH anchor M342 (n=13); collocates with HIGH anchor M267 (n=7); collocates with HIGH anchor M176 (n=5); collocat; Source as recorded: +Phase48_validated; Evidence lines the audit counted as independent: 1 (GRAMMAR); Tests filed: distribution, functional_role

| Item | Kind | Type | Statement | Targets | Notes |
|---|---|---|---|---|---|
| M048-01 | positional_statistic | a | positional distribution as upgraded: UPGRADED: high frequency (157); consistent TERMINAL position (n=157) | — | — |
| M048-02 | corpus_count | a | raw co-occurrence count with M342: n=13 | — | — |
| M048-03 | interpreted_anchor | b | collocation premise: this sign collocates with M342 as a HIGH anchor | M342 | Reason: the premise is M342 under its interpreted reading and HIGH standing; the raw count is carried separately as an (a) item |
| M048-04 | corpus_count | a | raw co-occurrence count with M267: n=7 | — | — |
| M048-05 | interpreted_anchor | b | collocation premise: this sign collocates with M267 as a HIGH anchor | M267 | Reason: the premise is M267 under its interpreted reading and HIGH standing; the raw count is carried separately as an (a) item |
| M048-06 | corpus_count | a | raw co-occurrence count with M176: n=5 | — | — |
| M048-07 | interpreted_anchor | b | collocation premise: this sign collocates with M176 as a HIGH anchor | M176 | Reason: the premise is M176 under its interpreted reading and HIGH standing; the raw count is carried separately as an (a) item |

- Note: the basis truncates at 'collocat;' after the third collocate; no further premise is stated and none is entered
- Note: Round 2 amendment (standings supplement): no corrected battery result is filed for this sign; its class rests on the absence of a qualifying filed result

## M059 — ēḷ/eḷ (class U, Q4 N)

> Basis as recorded: Numeral 7; Source as recorded: +Phase48_validated; Evidence lines the audit counted as independent: 1 (GRAMMAR); Tests filed: distribution, functional_role Later corrected validation battery: score 1 against a promotion threshold of 2 (positional pass, dedr not_run, bigram not_run); moved from requires revalidation to this class.

| Item | Kind | Type | Statement | Targets | Notes |
|---|---|---|---|---|---|
| M059-01 | iconographic_interpretation | a | the sign read as the numeral 7 | — | Status: numerical claim WEAKENED (standings supplement section 6: stroke-count pattern 1/210 for this sign) |
| M059-02 | corrected_validation | a | corrected validation battery: score 1 against a promotion threshold of 2 (positional pass, dedr not_run, bigram not_run); the sign was moved from requires revalidation to its filed class on this result | — | — |

## M077 — nal (class U, Q4 S)

> Basis as recorded: Round 1: INITIAL position (freq=18), distributional assignment; UPGRADED-V18: consistent INITIAL (n=18); has specific PDR reading; Source as recorded: +Phase48_validated; Evidence lines the audit counted as independent: 2 (GRAMMAR); Tests filed: distribution, functional_role Later corrected validation battery: score 1 against a promotion threshold of 2 (positional pass, dedr not_run, bigram fail); moved from requires revalidation to this class.

| Item | Kind | Type | Statement | Targets | Notes |
|---|---|---|---|---|---|
| M077-01 | positional_statistic | a | positional distribution: INITIAL position, frequency 18, distributional assignment; restated as consistent in the V18 upgrade | — | — |
| M077-02 | self_assertion | b | the basis asserts the sign 'has specific PDR reading' | — | Reason: the adjudication's words: an input, not corroboration — the candidate system's own assertion about its reading, filed as part of the basis Target note: the assertion names no other reading; it is the system's own claim about this reading |
| M077-03 | corrected_validation | a | corrected validation battery: score 1 against a promotion threshold of 2 (positional pass, dedr not_run, bigram fail); the sign was moved from requires revalidation to its filed class on this result | — | — |

## M108 — kaL (class U, Q4 S)

> Basis as recorded: [Phase-116 recal: SA-cons=0.12✓ DEDR✓]; Source as recorded: Phase-89 systematic DEDR (ICON, MEDIUM); Dictionary reference as recorded: DEDR 1286; Gloss as recorded: wheel/circle; Evidence lines the audit counted as independent: 1 (GRAMMAR); Tests filed: distribution Later corrected site-statistics check: outcome insufficient data; moved from requires revalidation to this class.

| Item | Kind | Type | Statement | Targets | Notes |
|---|---|---|---|---|---|
| M108-01 | consistency_score | ambiguous | candidate-system consistency score: SA-cons=0.12 | — | Reason: the filed basis states the score but no definition of its inputs; whether it is computed over primary data or over interpreted material is not stated, so it is recorded ambiguous under spec section 3.4 |
| M108-02 | dictionary_entry | a | DEDR 1286 recorded as this reading's dictionary reference | — | — |
| M108-03 | corrected_validation | a | corrected site-statistics check: outcome insufficient data; the sign was moved from requires revalidation to its filed class on this result | — | — |

## M162 — il/iḷ (class U, Q4 N)

> Basis as recorded: House/dwelling sign; Source as recorded: +Phase48_validated; Evidence lines the audit counted as independent: 2 (GRAMMAR, ICONOGRAPHIC); Tests filed: drawing, distribution, functional_role, meaning Later corrected validation battery: score 1 against a promotion threshold of 2 (positional pass, dedr not_run, bigram fail); moved from requires revalidation to this class.

| Item | Kind | Type | Statement | Targets | Notes |
|---|---|---|---|---|---|
| M162-01 | iconographic_interpretation | a | house/dwelling sign, read il/il | — | — |
| M162-02 | corrected_validation | a | corrected validation battery: score 1 against a promotion threshold of 2 (positional pass, dedr not_run, bigram fail); the sign was moved from requires revalidation to its filed class on this result | — | — |

## M176 — an/aṇ (class U, Q4 N)

> Basis as recorded: Masculine suffix; Evidence lines the audit counted as independent: 1 (GRAMMAR); Tests filed: distribution, functional_role Later corrected site-statistics check: outcome difference not detected; moved from requires revalidation to this class. The standings companion records a corrected terminal-position rate for this sign of 19.1% (68 of 356 occurrences), replacing an earlier published rate.

| Item | Kind | Type | Statement | Targets | Notes |
|---|---|---|---|---|---|
| M176-01 | internal_label | b | the filed basis is the candidate system's own functional label for the sign: masculine suffix | — | Reason: no corpus count, dictionary entry, or published proposal is filed for this sign; the basis is the system's suffix-inventory label restated Target note: the label names no other reading; it is the system's own assignment |
| M176-02 | corrected_validation | a | corrected site-statistics check: outcome difference not detected; the sign was moved from requires revalidation to its filed class on this result | — | — |

- Note: the standings companion records a corrected terminal-position rate for this sign of 19.1% (68 of 356 occurrences), replacing an earlier published rate (appendix row)

## M233 — ūr (class U, Q4 N)

> Basis as recorded: Settlement/place marker; Source as recorded: +Phase48_validated; Evidence lines the audit counted as independent: 1 (GRAMMAR); Tests filed: distribution, functional_role Later corrected validation battery: score 1 against a promotion threshold of 2 (positional pass, dedr not_run, bigram not_run); moved from requires revalidation to this class.

| Item | Kind | Type | Statement | Targets | Notes |
|---|---|---|---|---|---|
| M233-01 | iconographic_interpretation | a | settlement/place marker, read ur (town/settlement) | — | — |
| M233-02 | corrected_validation | a | corrected validation battery: score 1 against a promotion threshold of 2 (positional pass, dedr not_run, bigram not_run); the sign was moved from requires revalidation to its filed class on this result | — | — |

## M305 — ōṭu/comitative (class U, Q4 S)

> Basis as recorded: terminal pinch mark; UPGRADED: moderate frequency (83); consistent TERMINAL position (n=83); collocates with HIGH anchor M342 (n=10); collocates with HIGH anchor M176 (n=7); has specific PDR reading; Source as recorded: +Phase48_validated; Evidence lines the audit counted as independent: 1 (GRAMMAR); Tests filed: distribution, functional_role Later corrected validation battery: score 1 against a promotion threshold of 2 (positional pass, dedr not_run, bigram not_run); moved from requires revalidation to this class.

| Item | Kind | Type | Statement | Targets | Notes |
|---|---|---|---|---|---|
| M305-01 | positional_statistic | a | positional distribution as upgraded: UPGRADED: moderate frequency (83); consistent TERMINAL position (n=83) | — | — |
| M305-02 | self_assertion | b | the basis asserts the sign 'has specific PDR reading' | — | Reason: the adjudication's words: an input, not corroboration — the candidate system's own assertion about its reading, filed as part of the basis Target note: the assertion names no other reading; it is the system's own claim about this reading |
| M305-03 | corpus_count | a | raw co-occurrence count with M342: n=10 | — | — |
| M305-04 | interpreted_anchor | b | collocation premise: this sign collocates with M342 as a HIGH anchor | M342 | Reason: the premise is M342 under its interpreted reading and HIGH standing; the raw count is carried separately as an (a) item |
| M305-05 | corpus_count | a | raw co-occurrence count with M176: n=7 | — | — |
| M305-06 | interpreted_anchor | b | collocation premise: this sign collocates with M176 as a HIGH anchor | M176 | Reason: the premise is M176 under its interpreted reading and HIGH standing; the raw count is carried separately as an (a) item |
| M305-07 | corrected_validation | a | corrected validation battery: score 1 against a promotion threshold of 2 (positional pass, dedr not_run, bigram not_run); the sign was moved from requires revalidation to its filed class on this result | — | — |

## M328 — ā/āl (class U, Q4 N)

> Basis as recorded: Man/person sign; Source as recorded: +Phase48_validated; Evidence lines the audit counted as independent: 1 (GRAMMAR); Tests filed: distribution, functional_role Later corrected validation battery: score 1 against a promotion threshold of 2 (positional pass, dedr not_run, bigram not_run); moved from requires revalidation to this class.

| Item | Kind | Type | Statement | Targets | Notes |
|---|---|---|---|---|---|
| M328-01 | iconographic_interpretation | a | man/person sign, read a/al | — | — |
| M328-02 | corrected_validation | a | corrected validation battery: score 1 against a promotion threshold of 2 (positional pass, dedr not_run, bigram not_run); the sign was moved from requires revalidation to its filed class on this result | — | — |

## M336 — iṉ/locative (class U, Q4 N)

> Basis as recorded: chevron terminal = locative case marker; UPGRADED: high frequency (161); consistent TERMINAL position (n=161); collocates with HIGH anchor M342 (n=14); collocates with HIGH anchor M099 (n=6); collocates with HIGH anchor ; Source as recorded: +Phase48_validated; Evidence lines the audit counted as independent: 1 (GRAMMAR); Tests filed: distribution, functional_role Later corrected validation battery: score 1 against a promotion threshold of 2 (positional pass, dedr not_run, bigram fail); moved from requires revalidation to this class.

| Item | Kind | Type | Statement | Targets | Notes |
|---|---|---|---|---|---|
| M336-01 | positional_statistic | a | positional distribution as upgraded: UPGRADED: high frequency (161); consistent TERMINAL position (n=161) | — | — |
| M336-02 | corpus_count | a | raw co-occurrence count with M342: n=14 | — | — |
| M336-03 | interpreted_anchor | b | collocation premise: this sign collocates with M342 as a HIGH anchor | M342 | Reason: the premise is M342 under its interpreted reading and HIGH standing; the raw count is carried separately as an (a) item |
| M336-04 | corpus_count | a | raw co-occurrence count with M099: n=6 | — | — |
| M336-05 | interpreted_anchor | b | collocation premise: this sign collocates with M099 as a HIGH anchor | M099 | Reason: the premise is M099 under its interpreted reading and HIGH standing; the raw count is carried separately as an (a) item |
| M336-06 | interpreted_anchor | b | a third collocation premise is filed but its target is cut off in the basis as filed | — | Reason: the basis truncates mid-clause at this premise; the premise is (b)-type but its target cannot be recovered from the filed text Target note: the basis as filed names no target; the clause is truncated |
| M336-07 | corrected_validation | a | corrected validation battery: score 1 against a promotion threshold of 2 (positional pass, dedr not_run, bigram fail); the sign was moved from requires revalidation to its filed class on this result | — | — |

## M342 — ay/ā (class U, Q4 S)

> Basis as recorded: Terminal marker, Dravidian case suffix; Evidence lines the audit counted as independent: 1 (GRAMMAR); Tests filed: distribution, functional_role Later corrected site-statistics check: outcome difference not detected; moved from requires revalidation to this class. The standings companion records a corrected terminal-position rate for this sign of 12.0% (70 of 584 occurrences), replacing an earlier published rate.

| Item | Kind | Type | Statement | Targets | Notes |
|---|---|---|---|---|---|
| M342-01 | internal_label | b | the filed basis is the candidate system's own functional label for the sign: terminal marker, Dravidian case suffix | — | Reason: no corpus count, dictionary entry, or published proposal is filed for this sign; the basis is the system's suffix-inventory label restated Target note: the label names no other reading; it is the system's own assignment |
| M342-02 | corrected_validation | a | corrected site-statistics check: outcome difference not detected; the sign was moved from requires revalidation to its filed class on this result | — | — |

- Note: the standings companion records a corrected terminal-position rate for this sign of 12.0% (70 of 584 occurrences), replacing an earlier published rate (appendix row)
- Note: this sign is the most-depended-on premise in the 94: the dependency record names it as a premise for M005, M030, M068, M089, M347, M375, M398 and the already-U checks; those edges are carried on the depending readings' entries, not here

## M367 — am/neuter (class U, Q4 N)

> Basis as recorded: terminal diamond = neuter suffix; UPGRADED: high frequency (190); consistent TERMINAL position (n=190); collocates with HIGH anchor M176 (n=8); collocates with HIGH anchor M099 (n=6); collocates with HIGH anchor M267 (n=; Source as recorded: +Phase48_validated; Evidence lines the audit counted as independent: 1 (GRAMMAR); Tests filed: distribution, functional_role

| Item | Kind | Type | Statement | Targets | Notes |
|---|---|---|---|---|---|
| M367-01 | positional_statistic | a | positional distribution as upgraded: UPGRADED: high frequency (190); consistent TERMINAL position (n=190) | — | — |
| M367-02 | corpus_count | a | raw co-occurrence count with M176: n=8 | — | — |
| M367-03 | interpreted_anchor | b | collocation premise: this sign collocates with M176 as a HIGH anchor | M176 | Reason: the premise is M176 under its interpreted reading and HIGH standing; the raw count is carried separately as an (a) item |
| M367-04 | corpus_count | a | raw co-occurrence count with M099: n=6 | — | — |
| M367-05 | interpreted_anchor | b | collocation premise: this sign collocates with M099 as a HIGH anchor | M099 | Reason: the premise is M099 under its interpreted reading and HIGH standing; the raw count is carried separately as an (a) item |
| M367-06 | interpreted_anchor | b | collocation premise: this sign collocates with M267 as a HIGH anchor; the count is cut off in the basis as filed | M267 | Reason: the premise is M267 under its interpreted reading and HIGH standing Status: the filed count is truncated in the basis as filed |
