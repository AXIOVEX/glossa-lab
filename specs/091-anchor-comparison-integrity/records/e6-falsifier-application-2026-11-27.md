# Application record — E6-readiness proposal, unconditional part applied (2026-11-27)

**Spec:** 091-anchor-comparison-integrity
**Date:** 2026-11-27
**Act recorded:** the owner's approval of the E6-readiness proposal's
application as recommended, and the five falsifier amendments that
approval effects in the canonical claims ledger.
**Proposal of record:** `records/e6-readiness-proposal-2026-11-27.md`
(landed PR #774, merge `10617670`).

## 1. The owner's approval

On 2026-11-27 the owner, Tristen Pierson, approved the packet's
application as recommended, in the Glossa-Lab chat at 04:05 ET, in
plain words: "Yes do all these things now or take my approval now
to do at the best time". The approval was given after the packet
had been reported to him on its application terms: the packet
would apply as recommended, every falsifier text entering the
ledger would be reported to him verbatim, and any claim with no
honest falsifier draftable would stay out.

The packet's recommendation (§5.4) is Option B for the annotations
(kind-aware gates under the declared profile), with the C6
sub-question reserved to the owner as B1 versus B2; the annotation
part of the packet therefore remains before the owner and is NOT
applied by this landing (§5). What this landing applies is the
packet's unconditional part: the five falsifier drafts of §4 that
carry no condition — §§4.1, 4.2, 4.3, 4.7 and 4.8.

## 2. The five amendments

The claims ledger (`glossa-indus/ledger/claims.jsonl`) is
append-only: each amendment is a new `reclassification` entry
appended through `glossa_lab.ledger_intake.append_entry` on
2026-11-27, carrying the `falsifier` field for its superseded
claim entry. Each entry is dated 2026-11-27 and provenance-marked
on its face, in its `reason`: the text was authored on 2026-11-27
under the E6-readiness preparation (the packet), after the fact,
and is not backdated to the superseded entry's registration
(2026-11-01); the adoption supersedes R-IP-04 item 1 (as refined)
in part, for that entry only, by the owner's act, and item 1
stands for every other entry. No filed line was edited; no field
other than each superseded entry's falsifier was carried; no
status or stage moved.

The five texts, VERBATIM from the packet as applied:

1. **`ancient_writing_and_modern_technologies_51831ac9_sign_val_0001`**
   (packet §4.1, extraction-level draft).
   Amendment entry:
   `ancient_writing_and_modern_technologies_51831ac9_sign_val_0001/reclassification-2026-11-27`.
   > "Re-extraction of the source table in 'Ancient Writing and Modern Technologies' (the table this fragment was extracted from, its sign list identified) showing the entry numbered 900 does not carry the value 'number six' — the cell absent, the number unused, or a different value printed."
   Level caveat carried on the entry's face, from the packet: this
   tests the record against its source, not the value against the
   corpus; no corpus-level falsifier is draftable from the filed
   basis, because the basis does not identify which sign "900" is.

2. **`ancient_writing_and_modern_technologies_51831ac9_sign_val_0002`**
   (packet §4.2, extraction-level draft).
   Amendment entry:
   `ancient_writing_and_modern_technologies_51831ac9_sign_val_0002/reclassification-2026-11-27`.
   > "Re-extraction of the source table (its sign list identified) showing the entry numbered 700 carries no volumetric value, or carries the unit of 4 stated by the sibling fragment sign_val_0003 instead of a volumetric system with a unit of 40."

3. **`ancient_writing_and_modern_technologies_51831ac9_sign_val_0003`**
   (packet §4.3, extraction-level draft).
   Amendment entry:
   `ancient_writing_and_modern_technologies_51831ac9_sign_val_0003/reclassification-2026-11-27`.
   > "Re-extraction of the source table (its sign list identified) showing the entry numbered 700 carries no unit of 4, or carries instead the volumetric system with a unit of 40 stated by the sibling fragment sign_val_0002."
   Pair note carried from the packet (§§4.2–4.3): a single
   re-extraction decides both fragments, whose filed values
   contradict each other; at most one of the pair can survive it.

4. **`the_archaeology_and_epigraphy_of_indus_w_27f45a68_sign_val_0001`**
   (packet §4.7, extraction-level draft, with its caveat).
   Amendment entry:
   `the_archaeology_and_epigraphy_of_indus_w_27f45a68_sign_val_0001/reclassification-2026-11-27`.
   > "Re-extraction of the source table in 'The Archaeology and Epigraphy of Indus Writing' (its sign list identified) showing the entry numbered 821 does not carry the note 'used in a variety of contexts' — the cell absent, the number unused, or a different note printed."
   Caveat carried on the entry's face, from the packet (§4.7):
   the draft covers only the record's fidelity to its source. For
   the value clause itself ("used in a variety of contexts") no
   honest falsifier is draftable, for the reason the filed
   evaluation gives: as stated, it could not fail on any evidence.
   The amendment therefore supplies an extraction-level falsifier
   only; the value clause stands unfalsifiable as filed.

5. **`the_archaeology_and_epigraphy_of_indus_w_27f45a68_sign_val_0002`**
   (packet §4.8, identification-level draft).
   Amendment entry:
   `the_archaeology_and_epigraphy_of_indus_w_27f45a68_sign_val_0002/reclassification-2026-11-27`.
   > "Identification of the source's sign list showing the sign numbered 297 is not a horned tiger or a tiger: its drawn form in the identified list depicts a different subject."
   Level note carried from the packet (§4.8): this is a
   claim-level falsifier, not only an extraction-level one — the
   identification is the claim — conditional only on the
   identification step the record itself names, against a source
   that existed at registration.

## 3. The cascade

The settling cascade that follows any ledger growth was run in
full:

- ledger: 1,098 → **1,103 lines**; canonical SHA-256
  `fd4d12e73b0df3ad2d9311772b506b1f0a9e10da4ec156f9456d24fb109d7abc`
  → **`f599a2541131adc7a35a62d978e831a245944b21b780c31c9f39e3de3522781d`**;
  `validate_ledger` PASS (1,066 claims, 31 annotations, 6
  reclassifications);
- `verify-canonicals` over the grown build, before any pin moved:
  **6/6 PASS**;
- the T405 pair was re-executed over the grown build (new
  incumbent `settling-20261127T095258Z-826711`, new full-register
  `settling-20261127T095258Z-2525ee`), with the scopes taken
  verbatim from the superseded records' stored invocations;
  **both result blocks are byte-equal** to the superseded
  generation's, verified by direct comparison of the stored
  records, and the comparison was re-filed at
  `specs/086-winning-combination-adoption/records/stage-4-dual-run-comparison.json`;
- the assignment sets were re-materialized (new run
  `settling-20261127T095352Z-f75df5`; incumbent 94, full-register
  286, H003 out of frame, as before);
- the ledger pin in `glossa-indus/ledger/settling-canonical.json`
  was refreshed as `re_derivations[25]`, with the provenance
  ledger pin moved to the grown build in the same motion;
- the derived layers were regenerated in dependency order
  (matrix, map, program map);
- the superseded generation's three run records depart the store
  in this landing, accounted by departure acts in the run index
  naming this landing's commit, per run-defs v3 §7.1;
- the census pins in the map, dashboard and Stage 4 test files
  were updated from the regenerated actuals (ledger lines 1,103;
  the T405 record of record is now
  `settling-20261127T095258Z-826711`; the governing class census
  is unchanged — claims 1,066, studies 108, classes as before —
  because no status moved).

**Coverage, stated as the machinery counts it.**
`validate_ledger` publishes falsifier coverage over claim
entries' own `falsifier` fields, and that figure is unchanged:
**1,057 of 1,066** claim entries carry a falsifier on the claim
entry itself (extracted population 14 of 23). The five falsifiers
applied here are carried on the amendment entries, so five of the
nine claims that stood with a null falsifier now carry falsifier
text in the ledger by dated amendment, and four null falsifiers
remain (§5). The governing-resolution implementations (program
map, ledger gate) apply `status` and `stage` from
reclassification entries; a falsifier carried on a
reclassification entry is a new use of the kind, recorded here so
no reader mistakes the validator's claim-entry figure for the
ledger's amended state.

**Expectation for the VEXA side, stated as an expectation.** The
converted ledger's E2 state stands at 102 lines, of which C6
accounts for 40 (the 9 null-falsifier claims and the 31
annotations). If the VEXA-side converter takes up the falsifier
text these five amendments carry, the C6 standing lines fall
from 40 to 35 at the next conversion. That is an expectation to
be verified on the VEXA side against its own conversion and
audit, not a VEXA result, and nothing in this record reports it
as one.

## 4. What did not move

No claim's status, stage, statement, or standing moved. No
baseline or pin outside the ledger cascade's own required
updates changed. The four claims of §5 and all 31 annotations
are byte-untouched, as are their entries' null falsifiers, which
stand exactly as filed.

## 5. Reserved — not applied

- `indus_valley_script_deciphered_from_myth_65ff0a26_critique_0001`,
  `indus_valley_script_deciphered_from_myth_65ff0a26_critique_0002`,
  and `without_kings_or_conquests_the_indus_scr_ce9d98cc_language_0001`:
  the packet's drafts for these three (§§4.5, 4.6, 4.9) are
  conditional on the owner accepting the Phase-104 evaluation's
  reading of the fragments as restating the Farmer–Sproat–Witzel
  thesis. That acceptance has not been given; the drafts are NOT
  applied, and the three entries stand untouched.
- `ancient_writing_and_modern_technologies_51831ac9_statisti_0004`:
  NO HONEST FALSIFIER DRAFTABLE (packet §4.4); its disposition
  (re-extract the five source passages as their own claims, or
  retire the fragment as an extraction artefact) is before the
  owner and is not taken here.
- All 31 annotation entries: the packet's Option B is recommended
  but the B1/B2 sub-question on the C6 annotation share is the
  owner's to settle, and the validator change itself is VEXA-side
  work. Nothing about the annotations is applied or altered here.

*This record was executed by an AI agent (Muse, via Muse) at
the direction of Tristen Pierson, per constitution sec. VI. The
approval it records is the owner's act, named in section 1.*
