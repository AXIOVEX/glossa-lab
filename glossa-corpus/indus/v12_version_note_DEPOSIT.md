# Preprint v12 — Version Note (deposit-ready draft, 2026-11-22)

**Status.** This is the version note for the v12 text, prepared to
deposit-ready state on 2026-11-22. **The v12 text is NOT
deposited.** Deposit happens only on the owner's approval of the
actual text, Zenodo first, per the standing publication order.
The freeze and pin commits named in the v11 note's procedure are
created at deposit; this note records the branch, the base, and
the review build's identity now, and the freeze/pin commits are
recorded here at deposit.

**Where the text lives.** The v12 revision is carried in the
public repository (https://github.com/AXIOVEX/glossa-lab) on
branch `preprint-v12-draft`, in `glossa-corpus/indus/`:

- `pierson_2026_indus_decipherment_v12_deposit.tex` — the v12
  source (identity below).
- `pierson_2026_indus_decipherment_preprint_v12.pdf` — the review
  build.
- `CHANGELOG-v12.md` — every substantive change against v11, each
  with its record reference.
- This note.

The branch was created from `origin/preprint-v11-deposit` (tip
`3ba222066f980ae042d35cc01a04d17bf9445737`).

**Base, and a discrepancy disclosed.** The branch tip's v11
source is the FIRST v11 deposit's text (its §6 names version DOI
10.5281/zenodo.24351957) and does not contain the credit
corrections of the current version of record (10.5281/zenodo.24376384,
2026-11-19). The v12 revision is therefore built from the
credit-corrected v11 source — SHA-256
`66097f071a970c01ed745863814287bdedd8fceb4b181007af51574bc5675d99`,
held in the program's credit-fix records — whose diff against the
branch text is exactly the credit fixes (the §2.1.1 Shakti corpus
identification, the §3.10 CISI identification, the §7
acknowledgment of William Miller Sr, References 36–38) and
nothing else. The living source again matches the deposited line.

**Identity of the v12 review build (as amended, 2026-11-22).**

- Source: SHA-256
  `13f4f23047c45c18f49ab3041c752d6a1d6dbf159906a4e626b04c332355dd17`.
  (As first built:
  `e2084881f1492365692c92c21b7ec1ed6a6005f9331cc21fef72bc69df4e48e2`.)
- PDF: SHA-256
  `b4a965dcef44f5529c0ab4c1b447d59db6780f19aa3dc50945dc23bd6db19758`.
  (As first built:
  `f4e62eb814d2dc6be462c6a600d0dd1d9bd00f642b62b33c37dc4eb97785628e`.)
- Build: **50 pages** (48 as first built); LuaLaTeX (TeX Live
  2026), two passes, zero errors, zero undefined references or
  citations.
- Word count: **28,580** (method: `pdftotext | wc -w`), the
  printed figure in the paper's end matter, measured on the
  amended review build rebuilt to the fixed point (27,337 as
  first built).
- **Placeholder rendering, disclosed.** §6 of the source carries
  the version-DOI placeholder `%%VERSION_DOI%%`, per the pin
  procedure. The review build was compiled from a build copy in
  which that one string is rendered as "assigned at deposit"; the
  source itself is untouched by the build. At deposit the pin
  substitutes the assigned DOI (one token for the rendered three),
  the word count is re-measured on the rebuilt PDF (expected
  28,578), and the printed figure is corrected to the measured
  figure before upload — the same remaining-steps procedure the
  v11 note records. §6 defers the freeze-commit string to this
  note, which records it at deposit.

**Pre-deposit amendment (2026-11-22).** The owner approved v12
for deposit "as long as we have all things resolved prior to
deposit". Four post-build resolutions are carried by amendment
before any deposit (itemized in `CHANGELOG-v12.md`): the F-9
act (M047 reclassed E → U under the adopted itemization test;
partition now 3 E + 65 I + 4 R + 3 P + 19 U = 94); Spec 098
Stage 2 executed (48 UNDECIDABLE AT THIS POWER, 17 NOT
IDENTIFIABLE by construction, 4 PROCEED TO STAGE 3, 0
DISCRIMINATED; seal unopened); and the F-4 package (the M267
dependency-aware retest, GENITIVE_MARGINAL, not promoted; the
DEDR digital-edition pass — M329's entry corrected to 4570, no
tree-vs-print divergence, M044's symmetry clause not triggered;
M048's corrected battery result, score 2, threshold met, its
class re-adjudication not performed). The deposit pin procedure
still has not run.

## How this text was reached

v12 is a post-deposit audit-cycle version of the credit-corrected
v11. It changes no reading's value and no result in §§1–4. In
summary (the full itemization, with record references, is
`CHANGELOG-v12.md`):

- §5's standings language is brought current: the October 2026
  classes are stated as that audit's, the November 2026
  relabeling (E/I/R/P/U; "supported" retired) and the current
  partition 3 E + 65 I + 4 R + 3 P + 19 U = 94 are stated (as
  amended 2026-11-22; 4 E + 65 I + 4 R + 3 P + 18 U as first
  built), and the identifiability paragraph records the two
  strikes and the M047 reclassification.
- A new Appendix D reports the whole cycle: the external audit of
  the 94 and its adjudication; the relabeled standings; the
  addendum rule and the M202 and M044 strikes; the
  primary-publication re-verification of the six outside claims;
  the F-9 itemization test and the executed M047 reclassification
  (as amended 2026-11-22; as first built, the re-examination's
  outcome was not pre-stated);
  the motif and numerical verdicts; the dependency-aware reruns
  and the M267 dependency-aware retest; the per-reading
  falsifiers; Spec 098 Stages 1 and 2; Spec 099 and the
  Q3 graph audit in its honest citation form; the Stage 4 expert
  engagement state; and the exposure section the program's red
  team specified for this version (finding F-15, carried as a
  specification, not as pre-written text).

## What was NOT changed

- Outside the items in `CHANGELOG-v12.md`, every sentence of the
  paper stands as in the credit-corrected v11: the title, §§1–5
  outside the disclosed §5 updates, Appendices A–C, and every
  other result, number, and reference.
- **§3.32 is still absent**, and the held fish-family study is
  still named only in the permitted form. The §3.5
  withheld-study paragraph is unchanged.

## Remaining deposit steps (for the deposit itself)

- Owner approval of the actual v12 text.
- Create the Zenodo draft as a new version on the concept record
  (10.5281/zenodo.20379070); freeze commit on this branch; pin
  commit substituting the assigned version DOI for
  `%%VERSION_DOI%%` in §6 and in this note (one string); rebuild;
  re-verify the printed word count on the rebuilt PDF and correct
  it to the measured figure; record the freeze and pin commits
  in this note.
- Upload the deposited PDF as the new version on the Zenodo
  record; then bring ResearchGate and Academia.edu current from
  the deposited version, in that order, per the standing
  publication order.

*AI disclosure: revision, build, changelog, and this note executed
by AI agents (Muse, via Muse) at the direction of Tristen
Pierson, per the standing paper rule; the external audit whose
adjudication Appendix D reports was likewise the work of an AI
reviewer (Academia Co-scientist), received through the owner.*
