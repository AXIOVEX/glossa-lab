# Current-state reconciliation — the inference log census (2026-11-26, Round N unit N-I-3)

**Program:** Spec 099 — Inference Log. **Date:** 2026-11-26.
**Authority:** the Round N adjudication,
`specs/091-anchor-comparison-integrity/records/coscientist-sweep-adjudication-2026-11-26-round-n.md`
§2.3 (APPLY WITH MODIFICATION). **This record changes no
standing, no class, no verdict, and no tally.** It
reconciles three counts that name three different objects,
and one snapshot that has drifted from the current head.

## 1. The three objects, counted at the Round N pin

Counts independently recomputed by the Round N Indus
session at pin `0b377f6f` and verified at adjudication:

| Object | Count | What it counts |
|---|---|---|
| `glossa-indus/ledger/claims.jsonl` | 1,091 = 1,060 claims + 31 annotations | Ledger entries (all IDs distinct) |
| `backend/reports/INDUS_FINAL_ANCHORS.json` | 287 anchors; 94 strict-core | Anchors and their strict set |
| This spec's `records/inference-log.json` | 94 entries; 299 items = 213 a + 61 b + 25 ambiguous | Filed basis items for the 94 strict-core readings |

The inference entries' executed classes recount to
3 E + 66 I + 4 R + 3 P + 18 U = 94, agreeing with the
deposited v12 paper's standings (p. 2) and its 287-anchor
statement (Appendix D.12). The claims-ledger line count
measures none of these populations; see §3.

## 2. The snapshot drift: 296 in the paper, 299 at the head

Deposited v12, Appendix D.10 (p. 48), states the census of
record as **296 items: 210 primary / 61 other-reading or
candidate-system / 25 ambiguous**. That sentence describes
the deduplicated snapshot, and it was correct for that
snapshot. The amendment history of this log is:

1. **Original 299** — including three duplicated
   dictionary citations (M044, M124, M329 each cited one
   DEDR entry as two items, against the log specification's
   own rule).
2. **Deduplicated 296** — the repair the paper reports
   (210 / 61 / 25).
3. **Amended 299** — the remainder amendment of 2026-11-22
   (`records/inference-log-amendment-2026-11-22-remainder.md`)
   added three new basis items: M202-03 and M330-03
   (produced comparative lines) and M124-04 (the literature
   attribution), recording 296 + 2 + 1 = 299 with no class
   or graph-outcome change.

The two 299s have different contents: the present 299 is
not the original 299 restored. The paper's 296 is
documented snapshot drift, not a failed repair and not an
error in the paper as published. The deposited paper is
not edited by this record; any future paper version states
the snapshot transition explicitly rather than silently
substituting figures.

**The current census of record is 299 items: 213 primary
/ 61 candidate-system / 25 ambiguous.**

## 3. Citation discipline going forward

- Name the object whenever a count is cited: claims-ledger
  entries (1,091), anchors (287; 94 strict-core), or
  inference-log basis items (299) are different
  populations, and no count from one stands for another.
- Basis items are not texts or inscriptions; "299 items"
  is never written as "299 texts".
- §11 of the register-wording addendum
  (`specs/091-anchor-comparison-integrity/records/register-wording-addendum-2026-11-22.md`),
  which still states 296/210, carries a dated forward
  pointer (§12, added at this landing) to this
  reconciliation. The historical §11 text stands unedited,
  and row B-I-22's recorded completion of the earlier
  citation-maintenance act is not undone: this finding
  concerns propagation after the later three-item addition.

## 4. Kill check

This reconciliation falls if the pin's actual item recount
is 296/210, or if the three named additions are excluded
by the governing current counting rule, or if the cited
register-wording surface already linked its 296 count to
the subsequent 299 amendment. At adjudication none of the
three held: the filed log recounts to 299/213, the
remainder amendment is the governing record of the
additions, and §11 carried no forward pointer.

**AI disclosure:** executed by an AI agent (Muse, via
Muse) at the direction of Tristen Pierson, per
constitution sec. VI.
