# Preparation record — 2026-11-27 — Eteocypriot paper, version 5 candidate

Study: Spec 096 — Eteocypriot Program

## Status

**CANDIDATE — NOT DEPOSITED, NOT SENT, NOT PUBLISHED.** Prepared
2026-11-27 for the owner's approval of the actual text. Under the
owner's rule of 2026-11-27, the paper iterates through Co-scientist
review after text approval and before any deposit finalizes; that
round has not run and is not part of this preparation. Version 4
stands as deposited (Zenodo record 24545017, DOI
10.5281/zenodo.24545017, PDF SHA-256
`f3f6a343d2f9646ea0a5c6bbf9ff8e93434eb1e77159251c49c6522044fcaa71`)
and is untouched by this record.

## The candidate

- **File:** `eteocypriot-alignment-v5-candidate-2026-11-27.pdf`,
  filed in the goal workspace
  (`files/eteocypriot-alignment-v5-candidate-2026-11-27.pdf`).
- **Pages:** 10. **Bytes:** 197,571. **SHA-256:**
  `34f57ac940479098d47f3edccf5c4529ca2e308729f25a3a4a4b1b419c4062f7`.
- **Source:** `pierson_2026_eteocypriot_program_preprint_v5.tex`,
  built on tower-compute (TeX Live 2026, pdflatex, three passes,
  zero errors) in `~/.syncyard/worktrees/glossa/eteocypriot-paper-v5/`
  from the deposited v4 source.

## Change 1 — the stem-count correction (the reason for v5)

Authority: the paper erratum of 2026-11-26
(`records/paper-erratum-2026-11-26-stems-count.md`, Round N unit
N-E-3).

Section 5.2 previously read: "The derivation the driver implements
contains a consonant-stem table (**sixteen** entries, plus a
special case in its letter handling)". It now reads "**fifteen**
entries". The special-case clause stands exactly as written.

Verified first-hand at preparation: the pinned E1 driver
(`records/eteocypriot-e1-driver.py`) hashes to the erratum's pin
(SHA-256
`9ec475fd419150e7d07a6a36f3e306eadc62b0427cdb2a4924825870116c9c95`)
and its STEMS dictionary contains exactly 15 entries. No numerical
result, verdict, or standing rests on the sentence, and none
changes.

## Change 2 — internal-language scrub (owner directive 2026-11-27)

The v4 text predates the owner's 2026-11-27 directive that papers
carry no internal language. A full-text scan for spec numbers,
requirement and test-case IDs, claim IDs, floor and finding IDs,
and ledger or claim-status vocabulary found the following, each
replaced with a plain description of the same thing. No number,
result, verdict, or claim changes under any of these.

1. **Spec number removed (2 places).** Section 2: "adopted as the
   Eteocypriot Program (Spec 096) on 2026-11-20" now reads
   "adopted as the Eteocypriot Program on 2026-11-20".
   Bibliography: the program-record entry's title "Spec 096 —
   Eteocypriot Program: specification, claims, …" now reads
   "Eteocypriot Program: specification, claims, …". Reason: a
   spec number is an internal label; the citation still names the
   record set and the repository.
2. **Claim IDs replaced (13 places).** "C096-1" through "C096-4"
   now read "Claim 1" through "Claim 4" throughout (the Section 2
   claim list, Sections 5.1 and 5.3, and the Section 6 verdict
   list, including the quoted mandated citation form "Claim 4
   SUPPORTED — process claim, self-assessed"). Reason: C096-n is
   a claim ID; "Claim n" names the same four claims in plain
   words, in the order the paper introduces them.
3. **Ledger vocabulary removed (2 places).** Section 2: "Four
   claims were intaken into the program's claims ledger in claim
   form" now reads "Four claims were registered in advance".
   Section 6: "The claims stand in the program's ledger at their
   intake state (draft / created): ledger standings unchanged"
   now reads "The claims stand in the program's record exactly as
   registered: their standings are unchanged". Reason: the claims
   ledger, its intake states, and its status values are internal
   system vocabulary; the statements' content (registered in
   advance; standings unchanged) is preserved.
4. **Floor IDs replaced (3 places).** Section 3.1: "F-E1a (the
   ICS 196 leg of E1)" now reads "The ICS 196 leg's floor";
   "F-E1b (the Androkles leg)" now reads "The Androkles leg's
   floor"; "F-E2 (the E2 census floor: …)" now reads "The E2
   census floor (…)". Section 4.3: "(floor F-E2)" now reads "(the
   E2 census floor)". Reason: F-E1a/F-E1b/F-E2 are internal floor
   identifiers; the paper already names each floor descriptively.
5. **Finding ID removed (1 place).** Section 5.4: "finding F-2
   stands closed as adjudicated" now reads "that finding stands
   closed as adjudicated". Reason: F-2 is an internal finding
   identifier; the finding is identified by the paragraph itself.
6. **Intake vocabulary replaced (7 places).** The corpus-process
   noun "intake" is replaced throughout: "The Androkles intake
   was then executed as a new corpus state" → "The Androkles
   material was then taken in as a new corpus state"; "no
   sign-level intake" → "no sign-level material"; "the intake
   changes what the program holds" → "the taking-in changes what
   the program holds"; "intake-enlarged pool" → "enlarged pool";
   "the Androkles intake has been executed as a new corpus state"
   → "the Androkles material has been taken in as a new corpus
   state"; "on a Perna-side intake held as a new corpus state" →
   "on Perna-side material held as a new corpus state"; "The
   acquisition and intake recorded in §3.3" → "The acquisition
   and taking-in recorded in §3.3"; and in the bibliography,
   "Androkles intake records" → "Androkles taking-in records".
   Reason: "intake" is the program's internal label for the
   corpus process; the plain words describe the same acts.
7. **Internal package and round labels replaced (1 place).**
   Acknowledgements: "(the delegated-decisions package of
   2026-11-20 and Red Team Rounds 1–4 of 2026-11-21)" now reads
   "(the review package of 2026-11-20 and the red-team rounds of
   2026-11-21)". Reason: the package name and round numbering are
   internal record labels; the dates and the descriptions stand.

The paper's own defined terms stand: the two alignment
assumptions (A1, A2), the experiments (E1, E2, E3), the tests
(P1, P2, P3), the null models (NC-1, NC-2), and the verdict words
(NOT SUPPORTED, TOO THIN, NOT ENGAGED, SUPPORTED) are each defined
or introduced in the paper's own text and are its public
vocabulary, not internal labels.

## Version furniture

"Preprint v4" now reads "Preprint v5" in the version line and the
closing line. The DOI line still names the v4 record DOI
(10.5281/zenodo.24545017) deliberately: no DOI is invented for an
undeposited candidate; the new version's DOI is assigned at
deposit, on the owner's later order.

## Slop check

- The one corrected number was verified first-hand against the
  pinned driver (hash and 15-entry count above).
- A full-text diff against the deposited v4 source shows no other
  number differs: every figure in the candidate (the frozen census
  of 54 signs in 11 segments, the ICS 217 control's 66 signs, the
  held-out form counts, the LCCS scores, the null percentages, the
  audit output hash, all dates) is byte-identical to v4, whose
  text passed the program's slop check before deposit (release
  record of 2026-11-22 and its addenda).
- The rendered candidate was text-extracted and checked: "fifteen"
  is present, and no occurrence of "sixteen", any claim ID, the
  spec number, or the words "ledger" or "intake" appears in the
  rendered text.

## What does not happen on this record

No deposit, no venue action, no send. On the owner's approval of
the text, the paper goes to Co-scientist review; only after that
round is adjudicated does any deposit question return to the
owner.

**AI disclosure:** executed by an AI agent (Muse, via Muse)
at the direction of Tristen Pierson, per constitution sec. VI.
