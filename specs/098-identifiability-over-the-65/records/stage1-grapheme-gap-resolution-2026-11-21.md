# Spec 098 — Stage 1, T102: the M044/M374 grapheme gap, resolved on the record

**Date:** 2026-11-21 · **Task:** T102 (acceptance: record + test) · **Claim:** C098-2 · **Venue:** tower-compute, fresh clone · **Runner:** `tools/stage1_run.py` (census mode), payload exit 0 · **Crosswalk of record:** `backend/glossa_lab/data/mahadevan_parpola_crosswalk_v2.json` at the pinned commit (184 entries).

## Method

Exhaustive search for both signs over the whole corpus of record (15,508 records): the canonical grapheme field, and both diplomatic fields (`text_code_diplomatic` and `text_code_diplomatic_normalized`), with variant decorations stripped, in every source system and sign scheme. Any Parpola-coded attestation was then resolved token by token under the frozen crosswalk, and the resolution verified against the crosswalk's own entries (the task's test leg).

## M044 (ku, Arm E) — resolved, one attestation

M044 is attested exactly once in the corpus of record: record `GLI-IND-0000321` (source mayig-cisi, Parpola scheme), diplomatic sequence `324-009-288-325-349-044`, the token `044` appearing in both diplomatic fields of that one record. The frozen crosswalk carries the entry M044 ↔ P044 (parpola_num 44; confidence MEDIUM; source Parpola 1994 Appendix B), so the attesting token resolves to M044 under the crosswalk of record, and the resolution verifies.

The full resolved sequence is `[unmapped 324, M009, unmapped 288, unmapped 325, unmapped 349, M044]`: the crosswalk of record covers only 184 signs, and the other four tokens of this inscription have no entry; no mapping was invented for them. Two consequences are recorded plainly: (1) M044 has exactly one attested token in the corpus of record, and it sits outside the canonical grapheme field (that record's canonical ids are null), so the power grid's canonical-field count for M044 is 0 and its count under any arm is at most 1 — below the frozen 5-token minimum either way; (2) its one context sequence is only partially resolvable under the frozen crosswalk. M044 therefore stands to be UNDECIDABLE AT THIS POWER at scoring; the gap itself is resolved, in that the sign's attestation and its crosswalk status are now on the record rather than assumed.

## M374 (kul, Arm I) — not attested; the frozen default applies

M374 has no attestation anywhere in the corpus of record: zero occurrences in the canonical field and zero in either diplomatic field in any source or scheme, and crosswalk v2 carries no M374 entry. There is nothing to resolve. As the freeze provides (§7 gap 2), **M374 defaults to UNDECIDABLE AT THIS POWER, unscored**, and that default is now recorded as the Stage 1 outcome for this sign.

## Payload verdict

```
PAYLOAD VERDICT T102: M044_resolved=True M374_unattested=True   (runner exit 0;
resolved sequences verify against the crosswalk of record for every token
the crosswalk covers; M374's absence is an exhaustive-search result, not
an assumption)
```
