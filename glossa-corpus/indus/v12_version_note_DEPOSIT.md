# Preprint v12 — Version Note (DEPOSIT text, 2026-11-22)

**Status.** This is the version note for the deposited v12 text.
The owner approved the amended v12 text for deposit on
2026-11-22, the deposit gated on the M048 re-adjudication, which
landed on the program's main branch the same day (M048 takes
class I; the partition of record, verified from the standings
record on main before the pin, is 3 E + 66 I + 4 R + 3 P + 18 U
= 94). The version DOI assigned to v12 is
**10.5281/zenodo.24441587**; the title page of the paper carries
the concept DOI (10.5281/zenodo.20379070), which resolves to the
latest version.

**Where the text lives.** The v12 revision is carried in the
public repository (https://github.com/AXIOVEX/glossa-lab) on
branch `preprint-v12-draft`, in `glossa-corpus/indus/`:

- `pierson_2026_indus_decipherment_v12_deposit.tex` — the v12
  source (identity below).
- `pierson_2026_indus_decipherment_preprint_v12.pdf` — the
  deposited build (at the pin commit).
- `CHANGELOG-v12.md` — every substantive change against v11, each
  with its record reference.
- This note.
- Freeze commit: `a89e79a46a8b80797eb3bbf230acceeba57fee43` —
  the M048 amendment commit, at which the v12 text was frozen
  for deposit.
- Pin commit: `e73ef308e59df14d441df1ee2675b34f3de2ac41` —
  substitutes the assigned version DOI for the placeholder in
  §6 and corrects the printed word count to the measured figure
  on the pinned build; the deposited PDF is carried at this
  commit. This note is completed by the records commit that
  follows it.

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

**Identity of the deposited text.**

- Source: `pierson_2026_indus_decipherment_v12_deposit.tex` at
  the pin commit, SHA-256
  `e8941022307ae3c546570fcca8d0f20e7b6af2f0e71cc4c23c4424d5eb886f11`.
  It differs from the frozen text (freeze commit; SHA-256
  `117e64e1e58f5057f68ca5de4ed0dc40146a32ddac125efc80a8ac67af9164d7`)
  in exactly two places: the version DOI (the placeholder token
  in the frozen text, filled with 10.5281/zenodo.24441587) and
  the printed word-count figure (corrected as described below).
- PDF: SHA-256
  `f9f5d8038ef9272dfbb68f563cdb8365f51fdbb4b915286109574b088a797934`.
- Build: **50 pages**; LuaLaTeX (TeX Live 2026), two passes,
  zero errors, zero undefined references or citations.
- Word count: **28,763** (method: `pdftotext | wc -w`); the
  printed figure in the paper's end matter equals the measured
  figure on the deposited build (rebuilt to the fixed point).
- The freeze build at the freeze commit: source SHA-256
  `117e64e1e58f5057f68ca5de4ed0dc40146a32ddac125efc80a8ac67af9164d7`,
  PDF SHA-256
  `21bf7c0516bbed5f056ea656e6a54232be2f8f9a6ab38e2437b834a014f8e180`,
  50 pages, word count 28,765. The deposited text differs from
  the freeze text in the version DOI and the printed word-count
  figure, and in no other sentence.
- **Placeholder rendering, disclosed.** The frozen source
  carries the version-DOI placeholder `%%VERSION_DOI%%` in §6.
  The review and freeze builds were compiled from build copies
  in which that one string is rendered as "assigned at deposit"
  (three tokens for the DOI's one, so the freeze build's count
  measures 2 higher than the deposited build's); the sources
  themselves were untouched by those builds. The deposited
  build carries the DOI itself and §6 renders in full. §6
  defers the freeze-commit string to this note, which records
  it above.

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
M048's corrected battery result, score 2, threshold met; and,
after that text was written, the M048 re-adjudication itself,
executed 2026-11-22 on the owner's commission under RT2-08 —
M048 reclassed U → I, the partition becoming 3 E + 66 I + 4 R +
3 P + 18 U = 94, carried in Appendix D.7, D.2, D.9, §5 and the
abstract before deposit). The deposit pin procedure has since
run (pin commit, above).

## How this text was reached

v12 is a post-deposit audit-cycle version of the credit-corrected
v11. It changes no reading's value and no result in §§1–4. In
summary (the full itemization, with record references, is
`CHANGELOG-v12.md`):

- §5's standings language is brought current: the October 2026
  classes are stated as that audit's, the November 2026
  relabeling (E/I/R/P/U; "supported" retired) and the current
  partition 3 E + 66 I + 4 R + 3 P + 18 U = 94 are stated (as
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
  and the M267 dependency-aware retest; the M048 corrected
  battery result and its executed re-adjudication; the
  per-reading falsifiers; Spec 098 Stages 1 and 2; Spec 099 and the
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

## Deposit record (2026-11-22)

- The owner approved the amended v12 text for deposit on
  2026-11-22. The deposit was gated on the M048
  re-adjudication; that act landed on the program's main branch
  the same day (`specs/091-anchor-comparison-integrity/records/m048-readjudication-2026-11-22.md`),
  and the partition was verified from the standings record on
  main before the pin.
- The Zenodo draft was created as a new version on the concept
  record (10.5281/zenodo.20379070): deposition 24441587,
  assigned version DOI 10.5281/zenodo.24441587. (This note's
  mentions of the placeholder token are procedural description;
  the pin lands in this note as the recorded DOI in the Status,
  the file list, and this record.)
- Freeze commit `a89e79a46a8b80797eb3bbf230acceeba57fee43`;
  pin commit `e73ef308e59df14d441df1ee2675b34f3de2ac41`;
  rebuilt; the printed word count re-verified on the rebuilt
  PDF and corrected to the measured figure (28,763).
- Deposited files: the pinned PDF
  (`pierson_2026_indus_decipherment_preprint_v12.pdf`), the
  pinned source (as `pierson_2026_indus_decipherment_v12.tex`),
  and this note. The record's description carries a Version 12
  paragraph in the record's established cumulative form.
- Next, per the standing publication order: ResearchGate, then
  Academia.edu, are brought current from this deposited
  version.

*AI disclosure: revision, build, changelog, and this note executed
by AI agents (Muse, via Muse) at the direction of Tristen
Pierson, per the standing paper rule; the external audit whose
adjudication Appendix D reports was likewise the work of an AI
reviewer (Academia Co-scientist), received through the owner.*
