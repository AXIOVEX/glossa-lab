# Adjudication record — C101-1 adjudicated NOT SUPPORTED (2026-11-27)

**Spec:** 101-eteocypriot-next-claim
**Claim:** `101-eteocypriot-next-claim/C101-1`
**Date:** 2026-11-27
**Act recorded:** the owner's adjudication of C101-1 as NOT SUPPORTED, and
the standing change it effects in the canonical claims ledger.

## 1. The owner's act

On 2026-11-27 the owner, Tristen Pierson, adjudicated claim C101-1 as
**NOT SUPPORTED**. The act was given in the Glossa-Lab chat at 03:09 ET,
by a one-tap decision widget and in plain words: "Adjudicate C101-1 as
NOT SUPPORTED". The option had been presented to him with the cycle-1
outcome on 2026-11-26 (23:54 ET); the adjudication is his act, on the
registered outcome, under this spec's registered discipline (the floor
record, section 1.5: the SUPPORTED and NOT SUPPORTED readings are
registered in advance of the outcome, and task T401 prepared the outcome
for the owner's approval act).

## 2. The outcome the adjudication rests on

Spec 101 was executed exactly as registered, as test E-1 of the active
decipherment loop's cycle 1 (Spec 107; execution landed in PR #770,
merge `effb87e9`). The execution records are
`records/intake-identity-record-2026-11-27.md`,
`records/candidate-registration-2026-11-27.md`,
`records/freeze-addendum-2026-11-27.md` and
`records/scoring-outcome.json` in this package, and the cycle-1 outcome
is `specs/107-active-decipherment-loop/records/cycle-1-outcome-2026-11-27.md`.

The outcome, as filed: candidate ending counts **-se 0, -na 9, -i 1,
-ti 14** against the registered floors **33 / 25 / 25 / 25** (Q =
0.031153 < 0.05). Every registered candidate fell below its floor, so
under the floor record's section 1.5 the outcome reads NOT SUPPORTED:
the claim is not supported as registered. Per OD-D-1 the registered
target is ENRICHMENT; this is expressly **not a recurrence finding** —
nothing in the outcome or in this adjudication says the endings do not
recur, and no such statement is made anywhere in the record.

C101-2's exposure statement stands verbatim, unchanged by this act:
"that Perna 2019's chapter including its printed reading of ICS 194/195
was read in full on 2026-11-22 (OD-9) before any candidate was
registered".

## 3. The standing change

The claims ledger (`glossa-indus/ledger/claims.jsonl`) is append-only:
a standing change is a new line, never an edit. The change was made
through the ledger's own standing-change discipline — a
`reclassification` entry appended through
`glossa_lab.ledger_intake.append_entry` on 2026-11-27:

- entry id `101-eteocypriot-next-claim/C101-1/reclassification-2026-11-27`,
  kind `reclassification`, superseding
  `101-eteocypriot-next-claim/C101-1`;
- the field it moves is `status`: **draft → unsupported**.
  `unsupported` is the registered vocabulary value for a NOT SUPPORTED
  adjudication (program-map-defs v1, section 4.2; class **negative**),
  and the program map's governing resolution now carries C101-1 at
  status `unsupported`, class negative.

No other field of the claim moved, no other claim's standing moved, and
no baseline or pin outside the ledger cascade's own required updates
changed.

## 4. The cascade

The settling cascade that follows any ledger growth was run in full:

- ledger: 1,097 → **1,098 lines**; canonical SHA-256 `51f4fbbd…` →
  **`fd4d12e73b0df3ad2d9311772b506b1f0a9e10da4ec156f9456d24fb109d7abc`**;
  `validate_ledger` PASS (1,066 claims, 31 annotations, 1
  reclassification; falsifier coverage unchanged at 1,057 of 1,066);
- `verify-canonicals` over the grown build, before any pin moved:
  **6/6 PASS**;
- the T405 pair was re-executed over the grown build (new incumbent
  `settling-20261127T081822Z-c833b0`, new full-register
  `settling-20261127T081822Z-b6a378`); **both result blocks are
  byte-equal** to the superseded generation's, verified by direct
  comparison of the stored records, and the comparison was re-filed at
  `specs/086-winning-combination-adoption/records/stage-4-dual-run-comparison.json`;
- the ledger pin in `glossa-indus/ledger/settling-canonical.json` was
  refreshed as `re_derivations[24]`, with the provenance ledger pin
  moved to the grown build in the same motion;
- the derived layers were regenerated in dependency order (matrix,
  map, program map) and the assignment sets re-materialized (new run
  `settling-20261127T081842Z-cbc5d7`; incumbent 94, full-register 286,
  H003 out of frame, as before);
- the superseded T405 generation's three run records depart the store
  in this landing, accounted by departure acts in the run index naming
  this landing's commit, per run-defs v3 section 7.1;
- the census pins in the conformance, map, dashboard and Stage 4 test
  files were updated from the regenerated actuals (ledger lines 1,098;
  governing class census: open 1,057 → 1,056, negative 6 → 7; claims
  1,066 and studies 108 unchanged).

One disclosure: the first T405 re-execution attempt in this landing was
invoked with a malformed scope string; the settling layer refused and
wrote an absence record (`settling-20261127T081744Z-6af31b`). The
absence record and its single run-index entry act were removed before
landing, and the pair was re-executed with the scope taken verbatim
from the superseded records' stored invocations — the same treatment
the Spec 105 landing gave an erroneous first-attempt run record. No
result of record derives from the refused attempt.

## 5. Scope

This record and its landing move exactly one standing: C101-1, from
draft to NOT SUPPORTED (unsupported). Cycle 2 of the loop is not
commissioned by this act. Eteocypriot's live positive-claim inventory
of this kind is now empty, as the cycle-1 outcome record already
stated; that is a statement about the inventory, not about the
language.

*This record was executed by an AI agent (Muse, via Muse) at the
direction of Tristen Pierson, per constitution sec. VI. The
adjudication it records is the owner's act, named in section 1.*
