# Paper review adjudication — Eteocypriot paper, version 5 candidate (2026-11-27)

**Kind:** CO-SCIENTIST PAPER REVIEW ROUND + ADJUDICATION. **Actor:** the
Glossa-Lab chat's paper-round worker, under the owner's orders of
2026-11-27: every paper iterates through Co-scientist review before any
deposit finalizes (03:31 ET), and the deposits of both candidates are
approved (04:05 ET) but execute only after the rounds. Claim-changing
items are referred to the owner, not applied. Nothing in this round was
deposited anywhere.

## 1. Material and route

Candidate under review: the version 5 candidate of "Too Thin to Test:
A Preregistered Pilot Study of Eteocypriot Bilingual Alignment, Its
Registered Verdicts, and the Corrections They Required" (10 pages;
preparation record
`records/preparation-record-2026-11-27-v5-candidate.md`, PR #775).
Its changes from the deposited v4 (Zenodo record 24545017) are the
§5.2 stem-count correction ("sixteen entries" → "fifteen entries",
Round N erratum N-E-3) and a full scrub of internal program language
under the owner's 2026-11-27 no-internal-language rule for papers.

Route: the tower-compute automation Brave (Academia Co-scientist),
the Eteocypriot session `1828e4db-cc7b-434a-891a-12aca9ad1b8a` only,
under the standing composer discipline (probe, upload,
placeholder-matched verify by length and FNV-1a, guarded send
re-checking session URL, length, and hash). Briefs and captures at
the goal's `hidden_files/coscientist-paper-round-2026-11-27/eteocypriot-v5/eteocypriot/`:

| Iteration | Brief | Chars | FNV-1a | Capture | Bytes | SHA-256 |
|---|---|---|---|---|---|---|
| 1 | `BRIEF-eteocypriot-v5.md` | 2,875 | `e65fdb58` | `OUTPUT-eteocypriot-v5.md` | 14,325 | `9bfbb611c7efb88a0974154159651b655d1cbbde71632897560e6362b4d9fd50` |
| 2 | `BRIEF2-eteocypriot-v5.md` | 2,180 | `5790d1e6` | `OUTPUT2-eteocypriot-v5.md` | 1,204 | `6d2c0e704762bc7e251157670e691b77104bdcdfbe38a081ffe28ff92a994b64` |

**Two disclosures.** (1) *Brief checksum transcription error.* The
iteration-1 brief printed the candidate's SHA-256 truncated to 62
hexadecimal characters (two characters dropped mid-string in
transcription from a summary). The session caught it, reviewed the
attached bytes, and flagged the discrepancy as a file-identity note,
not a paper finding. The preparation record of record carries the
full digest, `34f57ac940479098d47f3edccf5c4529ca2e308729f25a3a4a4b1b419c4062f7`,
and the file's identity was independently verified by fresh hashes
when the attachment was staged; the iteration-2 brief supplied the
full digest and the session verified both checksums against it
("both checksums match the corrected values supplied... The
iteration-1 file-identity discrepancy is resolved"). (2) *Composer
incident, nothing sent.* Browser tab indices shifted between sends
as duplicate tabs closed; one send sequence, aimed by a stale index
at a different program's session tab, placed the unsent brief and
the v5 attachment in that session's composer. The guarded send
refused on the session-URL check, so nothing was sent; the draft
text and the attachment were removed from that composer and verified
gone (composer length 0, chip absent) before work continued, and a
throw-on-wrong-session pre-guard was added to every later send in
the round.

## 2. The intended revisions — session's verdicts

**Stem-count correction: correct.** The session parsed the pinned
driver itself (SHA-256 `9ec475fd…`, matching the audit and the dated
erratum) and counted 15 STEMS keys, with the ξ → k+s expansion a
separate branch in `letters_of`, not a sixteenth entry: "fifteen
entries, plus a special case in its letter handling" is right in
itself and in §5.2's context, and §5.4's bound (the charged mappings
do not affect the verdict-bearing derivations) is unaffected. Row
N-E-3's correction is confirmed carried.

**Scrub: no meaning-changing error.** All 13 occurrences of the
numbered claim labels resolve consistently against §6's verdict list
(Claim 1 NOT SUPPORTED with its qualifications; Claim 2 TOO THIN,
closed/unengaged at freeze; Claim 3 NOT ENGAGED; Claim 4 SUPPORTED,
narrowed). The two standings sentences are supported at the strength
the paper discloses ("Four claims were registered in advance"; "The
claims stand in the program's record exactly as registered: their
standings are unchanged" — checked against the canonical record's
four entries). The descriptive floor names identify the correct
units, the taking-in replacements preserve the acquisition
distinctions, and the version line with the v4 DOI deliberately
retained is acceptable for an undeposited candidate. The session
does not certify a byte-level diff against v4; the preparation
record carries that.

The session's own checks also confirmed: Table 1's 54 signs
(51 legible + 1 restored + 2 damaged); the 48-legible-sign held-out
total; A1 0/2 and A2 1/2 with the derived spellings and segment 6
selection; the two null frequencies (114/999, 191/999 as rounded).

## 3. Units and adjudications

**PV5-E1 — Date-bound the next-study status statements. OWNER
DECISION, referred as OD-P-4.** The abstract ("A next-claim study
is registered, not executed") and §7 state the Spec 101 study's
status in an unqualified present tense; that study has since
executed and was adjudicated NOT SUPPORTED on 2026-11-27, and the
paper gives only "November 2026", no reporting cutoff. The session's
preferred fix is the minimal historical-scope one (date-bound both
statements to the paper's 23 November 2026 reporting cutoff, without
importing the later outcome); the alternative is a brief dated
update. Choosing the paper's temporal scope is the owner's
decision. Not applied. No pilot verdict is affected either way.

**PV5-E2 — §4.2 tie sentence. APPLY.** As written, "the
patronymic's failure is a tie at the shared maximum" confuses
cross-name score equality with a maximisation tie: the filed score
vectors ([1,1,0,0,1,4,1,0,1,1,0] and [1,1,0,0,1,4,2,0,1,1,1]) each
have a unique maximum of 4 at segment 6, and the filed audit states
no maximum tie occurred. The sentence now reads, in the session's
proposed words: "Each replicate repeats the maximisation over
candidate segments, with ties assigned to the earliest segment. In
the real run, both derived spellings have a unique maximum of 4 at
segment 6; the patronymic fails because its correspondent is
segment 7, not because a tie-break selects the wrong segment."
Confirmed as rendered at iteration 2. Ledger row P-E-1.

**PV5-E3 — LCCS expansion. APPLY.** §4.2 named the metric "longest
common correct sequence"; the registered definition (§2 and the
freeze) is the longest common contiguous syllabogram subsequence —
an overlap measure, not a correctness measure, as the patronymic's
score of 4 at the wrong segment itself shows. The sentence now
reads "with a longest common contiguous syllabogram subsequence
(LCCS) of 4". Confirmed at iteration 2. Ledger row P-E-2.

**PV5-E4 — Androkles apparatus locator. APPLY.** §3.3 and
reference [3] located the sign-level apparatus at pp. 236–238. The
filed intake record
(`records/androkles-intake-record-2026-11-22.md`, read directly at
adjudication) distinguishes the plates (fig. 88–90) at pp. 236–237
from the syllabic apparatus at pp. 238–239, and the transcription
pages pp. 238–239 ground both reading passes and the 15-sign
summary; the old locator omits p. 239. §3.3 now reads "with the
sign-by-sign syllabic apparatus at pp. 238–239" and reference [3]
carries the same locator; the article's overall pp. 235–244 range
is unchanged, and no historical program record was rewritten.
Confirmed at iteration 2. Ledger row P-E-3.

## 4. Iteration 2 and the revised candidate

Iteration 2 submitted the revised candidate carrying PV5-E2, E3, E4
to the same session. Its confirmation: all three applied changes
are correct as rendered, "neither more nor less"; the fifteen-entry
correction and the scrub approval stand; "Apart from the expressly
referred date-bounding item, the revised text is correct and
complete from my side within this paper-text review."

**Revised candidate:** `eteocypriot-alignment-v5-candidate-revised-2026-11-27.pdf`
(goal files), 10 pages, 197,694 bytes, SHA-256
`d6c9ff10d8e76354caaf91b091e8f4724ffa639b1b0a587b440a9eb65a39a193`.
Built on tower-compute from the v5 candidate source (three pdflatex
passes, zero errors, page count unchanged); every changed sentence
verified in the rendered PDF and every replaced sentence verified
absent.

**Round verdict for this paper: clean apart from one owner decision
(OD-P-4), which is referred to the owner with the session's
preferred wording and is not applied.** The deposit step waits on
that decision; nothing was deposited, sent, or published in this
round, and no verdict or standing moved (the four pilot verdicts
are untouched by every unit above).

**AI disclosure:** this record was compiled by an AI agent (Muse,
via Muse) at the direction of Tristen Pierson, per constitution
sec. VI. It compiles the round's dispositions of record; it
adjudicates nothing beyond the paper-text items named above and
changes no standing, class, verdict, or tally.
