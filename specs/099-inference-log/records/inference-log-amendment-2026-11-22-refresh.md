# Spec 099 — Inference log amendment: M329 citation repair, pura-leg annotation, M047 provenance field

Filed 2026-11-22 under the Co-scientist refresh
adjudication of 2026-11-22
(`specs/091-anchor-comparison-integrity/records/coscientist-refresh-adjudication-2026-11-22.md`),
§5, landing L-2, units I-3, I-4 and I-9 (log part). The
governing findings are the F-4 DEDR digital-edition pass
(`specs/091-anchor-comparison-integrity/records/dedr-digital-edition-pass-2026-11-22.md`)
and the F-9 itemization adjudication
(`specs/091-anchor-comparison-integrity/records/f9-itemization-adjudication-2026-11-22.md`).

## The changes

No item is added, removed, or re-typed beyond the
citation repair below; the census is unchanged (296
items = 210 primary / 61 candidate-system / 25
ambiguous); no class changes; the historical filings
(the basis as filed, and every earlier record) are
unrepaired.

1. **M329 — DEDR citation repaired, 4524 → 4570 (I-4).**
   A wrong entry number with a recoverable intended
   entry is a repairable citation error, a different
   operation from striking a failed gloss. The F-4 pass
   found poṉ is DEDR entry **4570** in print (p. 404)
   and in the restored tree alike; the filed citation
   4524 was simply wrong. The builder's M329 curation
   now states the dictionary-entry item at 4570, with
   the amendment trail in the item's status note (filed
   as 4524; repaired 2026-11-22; the earlier
   unresolved-numbering-divergence framing superseded).
   The basis as filed still reads 4524 and is not
   rewritten. The same repair lands on the register
   surfaces at L-1.
2. **M329 — pura-leg annotation (I-3).** The Sanskrit
   pura item's status note now states expressly: the
   pura leg failed and contributes nothing to the
   basis; the class rests on the DEDR entry as repaired
   and the Elamite leg as filed. No strike, no class
   change — M329 satisfies the itemization test and its
   failure stands under the addendum's
   partial-verification arm.
3. **M047 — verified-provenance field beside the class
   (I-9, log part).** M047's entry gains a provenance
   note carried beside its class U: Parpola 1994
   §10.1's proposal for the fish-sign family stands
   verified as filed as a prior proposal, and the
   re-verification outcome is VERIFIED AS FILED
   (provenance only). The class moved on the
   filed-basis rule under the itemization test; the
   downgrade is documentary, not evidential, and this
   field preserves both facts. The historical log is
   not silently repaired: the entry's filed basis and
   its F-9 status note stand as landed.

## Verification payloads (this clone, before commit)

- Baseline reproduction, before any change: the builder
  over the unamended inputs reproduced the committed
  log byte-for-byte (JSON and rendering).
- Builder after the change: `built 94 entries; census
  a=210 b=61 ambiguous=25` — census unchanged.
- Log diff against the pre-amendment log: exactly the
  M329 entry (dictionary-entry item statement and
  status note; pura item status note) and the M047
  entry (the added provenance entry note), plus this
  amendment's provenance naming in the log header where
  the builder carries it.
- Fixture suite `tests/test_inference_log.py`:
  **15 passed** in this clone.

**AI disclosure:** executed by an AI agent (Muse, via
Muse) at the direction of Tristen Pierson, per
constitution sec. VI.
