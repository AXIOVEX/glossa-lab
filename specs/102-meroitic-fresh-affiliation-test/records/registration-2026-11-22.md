# Spec 102 — Registration Record (2026-11-22)

**LATE-FILED — filed 2026-11-22 in the Red Team Round 6
correction round (finding RT6-C1).** This file stood at
0 bytes from the registration landing until this filing.
The registration act itself was executed on 2026-11-22
(see §3 below: registration commit and PR #698, both of
that date). The cause of the empty file is not recorded
anywhere and is stated as unknown. The figures in §4
are reconstructed from the ledger chain verified in
the tree at this filing, not copied from any earlier
draft of this record (none exists). Tasks T002 and
T004 of this spec's `tasks.md` name this file as the
adoption act of record (T002) and as the place the
intake figures stand as executed (T004); test-cases.md
names it as the record of Stage 0's acceptance test.
This filing discharges those references late, and says
so on its face.

## 1. The owner act (the adoption act of record)

Owner decision **OD-21**, commissioned by the owner,
Tristen Pierson, on **2026-11-22 at 13:51 ET**:
**design and REGISTER only** a genuinely fresh
discriminating test for Meroitic affiliation on new or
independent material (Co-scientist refresh adjudication
unit M-18), after the preceding checks named in
spec.md's provenance. The act authorises design and
registration only: **no execution, and no corpus
ingestion**. No stage of the study has run under this
registration; execution requires a fresh owner
commission, and S-1's acquisition is a separate
owner-gated act (spec.md §6).

## 2. The AEE outcome at registration

- Claims **C102-1..C102-5** were intaken at
  registration, each with its falsifier and its
  does-not-establish line (claims.md), through the
  sanctioned importer (spec.md, D-102-2). Intake sets
  no standing; no claim carries a result.
- Test cases **TC-102-01..TC-102-06** are registered
  in test-cases.md. Stage 0's acceptance test is
  T001's package-form test (aee-claims.json parses;
  claims.md and aee-claims.json carry the same five
  claim ids in the same order; every claim has a
  falsifier and a does-not-establish line).

## 3. The registration landing

- Registration commit:
  `56162cb344b55a3527d1499d3aa900f0b3f9e61d`
  ("Spec 102: the Meroitic fresh affiliation test —
  registered, design-stage counts and power filed
  (OD-21)").
- Landed by **PR #698** ("Spec 102: the Meroitic
  fresh affiliation test — registered (OD-21)"),
  merge commit
  `ac6e2ddf6700ab5a8876aa451111ef5d0f27deb0`.

## 4. The ledger chain, verified from the tree

Counts are lines / claims (entries of kind `claim`;
the balance of each line count is annotations) in
`glossa-indus/ledger/claims.jsonl`, read at the named
commits at this filing:

| Point | Commit | Lines | Claims |
|---|---|---|---|
| Before Spec 100 | parent of `6dca5ef6` | 1,056 | 1,025 |
| After Spec 100 | `6dca5ef6` | 1,063 | 1,032 |
| After Spec 101 | `a6df45eb` | 1,067 | 1,036 |
| After Spec 102 | `56162cb3` | 1,072 | 1,041 |

The Spec 102 step is exactly the five C102 claims:
1,067 / 1,036 at the registration commit's parent to
1,072 / 1,041 at the registration commit.

## 5. Ledger canonical hash, before and after the Spec 102 intake

Derived at this filing by running the repository's own
ledger canonicalisation — `canonical_sha256_bytes` in
`backend/glossa_lab/ledger_intake.py` (SHA-256 over the
canonical form: UTF-8 decoded, CRLF and lone CR
normalised to LF, re-encoded as UTF-8), the function
the ledger gate (`backend/glossa_lab/ledger_gate.py`)
itself uses over the ledger — over
`glossa-indus/ledger/claims.jsonl` as of the two
commits:

- As of the registration commit's parent (`56162cb3^`):
  `a047eb146baece9a1d007663339e29d929bc8ebd39d2fb4a2155fb0fb44a640d`
- As of the registration commit (`56162cb3`):
  `d04a481054269ff17c58f6fdb5189b6726fa6eb074d312193f55fb36e3833660`

## 6. Scope of this record

Registration/design record only. This filing changes
no standing, no verdict, and no tally, and it does not
execute Spec 102 or ingest any corpus content.

**AI disclosure:** executed by an AI agent (Muse, via Muse)
at the direction of Tristen Pierson, per constitution sec. VI.
