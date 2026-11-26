# Spec 091 — Stage 5, T501 (W1 leg): the recomputation fed by Kobayashi's T401 coding

Record filed 2026-11-24. Run `study-20261124T094545Z-1e08ae`
(run record: `records/study-20261124T094545Z-1e08ae.json`; full
per-entry results: `records/t501-w1-recomputation-results-2026-11-24.json`).
Claims: C091-2 (the coding this recomputation consumes), C091-3
(the recomputation itself). This record executes the W1 half of
T501 over the records that exist. The W2 half is not executed:
T402 has not started (no D-091-1 act for W2 readers), so there
are no filed lines to recompute from, and tasks.md's T501
checkbox is unchanged by this record.

## 1. The act and its inputs

The eligible set was recomputed mechanically under
eligibility-defs v1 §5 from the three records that document
names, by `backend/scripts/spec091_stage5_recomputation.py`:

- **Staged record (frozen):**
  `backend/glossa_lab/data/mahadevan_parpola_crosswalk_v2_provenance.json`,
  SHA-256 `b7543523f8ae87e637244db07c9a07e1266b78db582cf07591fc094d0b2043e4`
  (WP4 classes, anchor readings as recorded, and the frozen
  construction-input set in its `inputs` block).
- **Locator record (frozen):** the T202 artifact
  (`mahadevan_parpola_crosswalk_v2_locators.json`, SHA-256
  `0074f2cc36a13943c758969430d0fdc8e3a7d0f2c5250e1594c02601534f3ef0`)
  read together with the supplementary pass
  (`mahadevan_parpola_crosswalk_v2_locators_supplement.json`,
  SHA-256 `610eeff1f9d8c64449cf040c6012e22b17c3506152076a4270bd836ff009c50c`);
  per entry per field the supplement's outcome wins
  (`records/stage-2-supplement-delta.json`). Phonetic census of
  the merged record: 9 located / 175 not-found; semantic: 0
  located / 184 not-found, so no semantic classification arises
  (eligibility-defs §5).
- **Coding record (new):**
  `backend/glossa_lab/data/mahadevan_parpola_crosswalk_v2_coding_kobayashi.json`,
  SHA-256 `d542bcae5a035e229549f22982c716a6fa3222725acd54025ddd8b6d549be242`
  — §2 below.

The recomputation is a pure function of these inputs. Its
anti-redefinition check passed: all 175 entries with no coding
reproduce their staged WP4 classifications exactly (175/175,
no mismatches), so every class change below is one the coded
record itself produces, in the direction WP4's rules dictate.

## 2. The coding record (T401, Kobayashi)

Professor Masato Kobayashi (University of Tokyo), engaged
2026-11-20 under D-091-1 (`records/t401-coder-engagement-record-2026-11-20.md`),
filed his completed blind coding on 2026-11-23 at 19:56 ET
(Gmail `1a20b0e76b2d2ddd`, engagement thread
`1a1fb478074a3ca3`): the packet
`kobayashi-blind-coding-packet.md` (10,078 bytes, SHA-256
`ed0e0af3ab4e578772ad4174060891fdb258ccd6f7c280973ac1001c9117242b`)
with all 9 assigned entries coded, none filed as not attested,
response sheet dated 24/Nov/2026. The assignment was the 9
located phonetic entries, source passages and the sign list
only, under blinding protocol v1 (filed 2026-11-17, before any
coding). Coded values, carried byte-for-byte per
eligibility-defs §3.4:

| Sign | Coded value | Alternatives as filed |
|---|---|---|
| M047 | mīn | — |
| M087 | veḷ | vēḷ, vēḷi |
| M088 | mu- | mu-m- |
| M091 | aṟu | caṟu |
| M092 | eḻu | — |
| M175 | katir | — |
| M261 | muruku | — |
| M281 | piḷḷay | — |
| M311 | vaṭa | — |

Eligibility-defs §3's preconditions were checked per entry in
the run and all hold for all 9: a §2 locator is on record and
the coding record cites that locator (§3.1); the coder is
named with his lineage exclusion on record (§3.2); the coding
was produced under the filed protocol and no deviation is
recorded against it (§3.3); the values are carried as supplied
(§3.4). No deviation has been reported or recorded, so no
coding is void (§4) and no entry falls back.

## 3. Per-entry outcomes

WP4's rule order as restated in eligibility-defs §5 step 1
(1 ineligible, 2 project-derived, 3 used during candidate
construction, 4 independently sourced, 5 unverified):

| Sign | Staged class | Recomputed class | Rule | Basis |
|---|---|---|---|---|
| M047 | project_derived | **independently_sourced** | 4 | Located; coded from the primary source by a lineage-excluded coder; not a construction input. The comparison is re-based on the source's own attestation (§5 worked consequence (a)). |
| M087 | project_derived | used_during_candidate_construction | 3 | Located and coded, but the anchor's value is a frozen construction input (Phase-51 crosswalk import). The staged class rested on rule 2 (the staged value was a Phase-96 anchor-table copy); with the comparison re-based on the coded value rule 2 no longer fires, and rule 3 states the standing ground. Eligibility is unchanged: not eligible. |
| M088 | ineligible | ineligible | 1 | Located and coded, but the anchor table carries no reading for this sign (a numeral component, not an anchor): there is no anchor comparison for the coding to re-base. |
| M091 | ineligible | ineligible | 1 | As M088. |
| M092 | ineligible | ineligible | 1 | As M088. |
| M175 | used_during_candidate_construction | used_during_candidate_construction | 3 | Construction input: rule 3 precedes rule 4 (§5 worked consequence (b)); independent coding of a construction input's source does not launder it (§3). |
| M261 | used_during_candidate_construction | used_during_candidate_construction | 3 | As M175. |
| M281 | used_during_candidate_construction | used_during_candidate_construction | 3 | As M175. (For the coded value's form, see §5 and §6.3.) |
| M311 | used_during_candidate_construction | used_during_candidate_construction | 3 | As M175. |

## 4. The aggregate, as produced

**Eligible set: {M047} — 1 entry, from 0.** C091-3's carried
register falsifier (every entry traceable to the project's own
derivation, the eligible count stays 0, the gap re-registers
as structural) does not arise: at least one entry now carries
an independently sourced comparison.

Census over all 184 entries, staged → recomputed:
independently sourced 0 → 1; used during candidate
construction 6 → 7; project-derived 116 → 114; unverified
7 → 7; ineligible 55 → 55. Two entries changed class (M047,
M087, §3); the remaining 182 are as staged, the 175 uncoded
among them by the anti-redefinition check of §1 and the 7
remaining coded entries by the rules of §3.

Examined census (C091-1's totality, preserved per
eligibility-defs §4): 184 entries examined; the phonetic field
carries a locator for 9, of which 9 are now coded; 175 fields
are not-found and keep their WP4 classes exactly.

## 5. Identity reporting (reporting only)

Classification never depends on whether values agree
(eligibility-defs D11). What follows is identity reporting
under the audit rule the provenance overlay carries (spec 006
Step 3c: lowercase, NFD-strip diacritics, first segment before
'/', strip parenthetical glosses, letters only), computed in
the run from the filed records:

| Sign | Coded | Locator record's cited value | Raw = | Normalized = | Anchor reading as recorded | Raw = | Normalized = |
|---|---|---|---|---|---|---|---|
| M047 | mīn | mīn | yes | yes | min/mīn | no | yes |
| M087 | veḷ | veḷ | yes | yes | veL | no | yes |
| M088 | mu- | mu(m) | no | yes | — (none) | — | — |
| M091 | aṟu | aru | no | yes | — (none) | — | — |
| M092 | eḻu | elu | no | yes | — (none) | — | — |
| M175 | katir | katir | yes | yes | katir | yes | yes |
| M261 | muruku | muruku | yes | yes | muruku | yes | yes |
| M281 | piḷḷay | piḷḷai | no | no | piLLai | no | no |
| M311 | vaṭa | vaṭa | yes | yes | vaTamiin | no | no |

Two cells carry their explanation on their face. M311's
anchor reading as recorded is the compound string `vaTamiin`
(the anchor table records vaṭa-mīn as one string); the staged
record already carried identity false/false for the staged
comparator against that string, and the coded value stands to
it exactly as the staged comparator did, while matching the
entry's located value byte-for-byte. M281 is §6.3 below.

## 6. Gaps in the registration, recorded, with no improvised rule

1. **No agreement vocabulary exists for W1.** Neither the
   blinding protocol, eligibility-defs v1, nor WP4 defines
   match categories (agree / partial / disagree or any other)
   for a coded value against a program value, and D11 bars
   classification from depending on agreement in any case.
   This record therefore reports classes (§3) and identity
   facts (§5) and applies no agreement verdict. The outcome
   vocabulary of `w2-reproduction-protocol-v1.md` governs W2
   (T402) only and was not imported into this leg.
2. **Alternatives have no registered recomputation role.**
   Protocol §4 requires alternative printed forms to be
   recorded, not resolved; eligibility-defs §3.4 consumes
   "the coded value" (singular), byte-for-byte. The
   alternatives as filed are carried in the coding record and
   reported in §2; no rule gives them a part in the
   recomputation and none was improvised. Noted instances:
   M091's alternative caṟu corresponds to the fig. 15.2 form
   (*c)aṟu quoted in the locator record's evidence; M088's
   alternative mu-m- is the form the §10.4 sequence text
   prints; M087's alternatives vēḷ / vēḷi are the source's
   other printed forms for that sign.
3. **M281: the source presents two printed forms.** Parpola
   1994's text gives piḷḷai (§13.1); its fig. 15.2 no. 13
   gives piḷḷay. The locator record's cited value carries
   piḷḷai; the coder filed piḷḷay as the value and recorded
   no alternative. No registered rule chooses between a
   source's printed forms for a coding record, so the coded
   value is consumed as filed (§3.4) and the divergence is
   reported, not resolved. It has no class consequence:
   M281's class is set by rule 3, which no coding moves.
4. **Source revision.** The coder's response-sheet edition
   line is blank. The coding record states the source
   revision as the works named in the packet (Parpola 1994,
   Cambridge University Press; Parpola 2010, World Classical
   Tamil Conference lecture). This is not a deviation under
   protocol §6's enumeration; it is recorded here as a
   completeness note on the coding record.
5. **The locator record's cited values for M091 and M092 are
   diacritic-free as frozen** (`aru`, `elu`), where the
   sources print aṟu / eḻu and the coder coded the printed
   forms; identity for those entries holds at the
   audit-normalized level and not at the raw level (§5). The
   locator record is a frozen Stage 2 artifact and is not
   edited by this act; the observation is filed here for
   Stage 6.

## 7. What this does and does not establish

- **C091-2.** The T401 record's open condition — C091-2
  remains open "until a coder's blind coding is filed and
  compared at T501" — is now met for Kobayashi's coding: the
  protocol was filed before coding started, the coder's
  identity and lineage exclusion are on record, no deviation
  is recorded, and the filed coding has been compared in
  this run. The claim's formal per-claim disposition remains
  Stage 6's act (T602). Kolichala's coding remains
  outstanding; the T401 bench was built so either filed
  coding can feed T501, and his, when filed, feeds a further
  recomputation.
- **C091-3.** Executed for the W1 leg over the records that
  exist; the eligible set is reported as produced (§4).
- **No standing, verdict, or tally moves (C091-15).** The
  94 anchors' standings (3 E + 66 I + 4 R + 3 P + 18 U = 94)
  are untouched. M047 the anchor remains class U (F-9 act,
  2026-11-22): the eligibility of its crosswalk comparison
  and the anchor's support class are different quantities.
  Audit v2 (T502) is where disposition consequences would be
  filed, and citation consequences are T503's; neither is
  performed by this record.
- **Owner decision (2026-11-26).** T502 and T503 were
  considered by the owner and left UNCOMMISSIONED; the
  deferral is recorded at both tasks in `tasks.md` (Stage
  5), which stay unchecked. No audit or citation work is
  performed under this note.
- *This does not establish:* that any reading is correct —
  eligibility certifies that the M047 comparison can now
  testify independently, not what it testifies (C091-3's own
  line) — and nothing about the other 8 coded entries'
  readings, whose comparisons stand exactly as classed in §3.
- **The outcome letter.** The owner's thank-you of 2026-11-24
  promised Professor Kobayashi a further letter with the
  comparison outcome. That letter is now owed; a draft is
  filed with the program's records outside this repo and is
  not sent by this act (external sends need the owner's
  approval of the actual text).
