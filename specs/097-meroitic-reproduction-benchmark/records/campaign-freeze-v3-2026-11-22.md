# Meroitic campaign freeze v3 — vocabulary-source cleanup — 2026-11-22

**Spec:** 097 (Meroitic reproduction benchmark). **Finding of
record:** RT1-47 (Red Team Round 1), whose F-4 arm this record
executes. **Commission:** the F-4 study package, commissioned
by the owner in chat 2026-11-22. **Execution venue:**
tower-compute.

## Status of this freeze

Freeze v3 is a new freeze **for future work only**. It adopts
freeze v2 (2026-11-20) sections 1–3 and 5–8 unchanged — the
custody terms, the corpus of record, the anchors and the
attested-only comparator rule, the split (335 development /
33 held out over the 368 distinct texts of the acquired
corpus), the metrics, and the prohibitions all stand as
frozen in v2 — and it replaces only the section 4 vocabulary
companion: `freeze-v3-vocabulary-2026-11-22.json` (filed
beside this record; SHA-256
`ee7056a461907f213a92a7aeb268c0e11ffb0c88d736c9799df647101e68bdd1`)
in place of `freeze-v2-vocabulary-2026-11-20.json` (SHA-256
`ab1de889b6e8674512fa64c9bb9e7bf5f2efe15f609f681558ba7781f23178fc`).

**Freeze v2 and every landed Stage 4 result stand
untouched.** No Stage 4 number was recomputed, and none
needs to be: section 3 below shows the cleanup cannot move
any of them.

## 1. The defect cleaned

Freeze v2 section 3 removed Wikipedia and "standard
summaries" as freeze-grade sources for anchors, yet the
section 4 vocabulary still carried them: 33 of its 182
entries listed a "Wikipedia contributors (2026)" citation
among their sources — including forms for scored concepts 16
woman (kdi, kadi) and 75 water (ato, ate), concept 75 being
one of R1's four matching concepts. The cleanup applies
section 3's own standard to section 4's apparatus.

## 2. The cleanup rule and the diff against v2

The rule, applied entry by entry by script (transformation
and diff both machine-verified):

- An entry carrying scholarly sources besides the Wikipedia
  citation **keeps its form, gloss, confidence and concept**;
  only the Wikipedia citation object is removed.
- An entry whose **only** source is the Wikipedia citation is
  **excluded** from the v3 vocabulary and named in this
  record. These are exactly anchor A1's forms, which freeze
  v2 section 3 already marks PROVISIONAL and excludes from
  scoring controls on this same ground; v3 treats the
  vocabulary entry consistently with the anchor.

The diff, in counts and sources:

| | freeze v2 | freeze v3 |
|---|---|---|
| vocabulary forms | 182 | **179** |
| Wikipedia citations anywhere in the apparatus | 33 | **0** |
| entries changed (citation removed, form retained) | — | 30 |
| entries excluded (Wikipedia-only apparatus) | — | 3 |
| forms added | — | 0 |

The 30 retained-and-cleaned forms: kdi, kadi (concept 16);
at "bread" (no concept); ato, ate (concept 75); lẖ, lh, lx,
laẖ; tedḫe, tdḫe, edḫe, dḫe, yedḫe, tedhe; terike, erike,
yerike; yetmde; ms, mash, mš, mos (concept 72); qore, qor,
qr; ktke, kdke; perite, prite. Each now stands on its
retained scholarly apparatus (Rilly 2004 / 2010 / 2016,
Rilly & de Voogt 2012, Griffith 1911, as filed per entry).

The 3 excluded forms: **qes, qos, qesw**, all glossed "Kush",
confidence "probable", concept none, whose entire v2
apparatus was the single citation "Wikipedia contributors
(2026), Meroitic language (Vocabulary section)". They are
excluded, not silently dropped: a future freeze may restore
them only on a scholarly source with pages, and until then
they carry the PROVISIONAL status freeze v2 section 3 already
assigns their anchor.

## 3. Why no landed result moves

Concept coverage is identical before and after (forms per
scored concept, v2 = v3): 12 night 2, 15 dog 3, 16 woman 2,
17 fire 2, 21 head 1, 46 bone 1, 55 louse 4, 62 belly 2,
70 heart 2, 72 sun 4, 75 water 2, 97 egg 1. The excluded
forms carry no concept; the cleaned forms keep their forms
and concepts. Stage 4.2's formative count S and its four
matching concepts (2, 15, 16, 75) are computed over forms and
concepts the cleanup does not alter, so S = 4 and every other
Stage 4 verdict would be computed identically under the v3
vocabulary. That is a statement about the diff, verified
above — not a re-run, and no Stage 4 record is amended.

## 4. Framework dependence, stated at the point of citation

The vocabulary and the formative legs of any test run under
this freeze rest substantially on one scholarly tradition —
Claude Rilly's — and R1's hypothesis is that same tradition's
hypothesis. The freeze's registered mitigation is the
attested-only comparator rule (freeze v2 section 3, carried
forward unchanged): Rilly-tradition forms count only where
independently attested. The mitigation does not cure the
dependence. Any future citation of a result computed under
freeze v3 carries this paragraph with it. (RT1-47's other
arm, the citation-discipline record of 2026-11-21, already
executes this discipline for the landed records; this freeze
carries the statement natively.)

## 5. What this freeze does not do

It does not re-split the corpus, does not re-run or amend any
Stage 4 stage, does not change any anchor's status (A1's
forms were already PROVISIONAL under v2), and does not
authorize any new test. A test under freeze v3 is a separate
commission, frozen against this record and the v3 vocabulary
companion's hash.

**Payload verdict: freeze v3 produced and diff-verified —
182 → 179 forms, 33 Wikipedia citations → 0 (30 removed with
forms retained, 3 Wikipedia-only forms excluded and named),
concept coverage identical across all 12 scored concepts;
freeze v2 and all Stage 4 results untouched.**

## Amendment 2026-11-22 — F-A correction to section 3 (labels only, counts unchanged)

**Authority:** flagged for adjudication as F-A by the OD-17
freeze-split dependency audit (PR #692, record
`od17-freeze-split-dependency-audit-2026-11-22.md` §5);
correction authorised by the owner 2026-11-22 13:50 ET.
This amendment corrects gloss labels and one sentence in
section 3 above. The original text is preserved verbatim
in this amendment; nothing above is rewritten.

**The defect.** Section 3's per-concept table attaches
glosses from a numbering other than the ASJP parameter
numbering of record to 9 of its 12 concept IDs, and its
matching-concepts sentence names concepts that do not
correspond to the executed Stage 4.2 record.

**Original text, as filed (preserved):** "Concept coverage
is identical before and after (forms per scored concept,
v2 = v3): 12 night 2, 15 dog 3, 16 woman 2, 17 fire 2,
21 head 1, 46 bone 1, 55 louse 4, 62 belly 2, 70 heart 2,
72 sun 4, 75 water 2, 97 egg 1." And: "Stage 4.2's
formative count S and its four matching concepts
(2, 15, 16, 75) are computed over forms and concepts the
cleanup does not alter, so S = 4 and every other Stage 4
verdict would be computed identically under the v3
vocabulary."

**Corrected labels** (ASJP numbering of record, per the
registered concept map in the pipeline code that freeze v2
section 4 designates, corroborated by the executed
Stage 4.2 outcome record, which names "21 dog, 46 foot,
72 sun, 75 water", and by the OD-17 audit §3.3): 12 **two**
(not "night"), 15 **small** (not "dog"), 16 woman
(unchanged), 17 **man** (not "fire"), 21 **dog** (not
"head"), 46 **foot** (not "bone"), 55 **eat** (not
"louse"), 62 **kill** (not "belly"), 70 **give** (not
"heart"), 72 sun (unchanged), 75 water (unchanged),
97 **good** (not "egg"). The corrected table reads:
12 two 2, 15 small 3, 16 woman 2, 17 man 2, 21 dog 1,
46 foot 1, 55 eat 4, 62 kill 2, 70 give 2, 72 sun 4,
75 water 2, 97 good 1.

**Corrected matching-concepts sentence:** Stage 4.2's
four matching concepts are **(21, 46, 72, 75)**, as
executed and as recorded in `stage-4-2-results.json`
(per-concept pattern) and the Stage 4.2 outcome record.
Concept 2 was never scored.

**Counts do not change.** Every count in the amended
table was verified against the executed record before
this amendment landed: the per-concept counts
(12: 2, 15: 3, 16: 2, 17: 2, 21: 1, 46: 1, 55: 4, 62: 2,
70: 2, 72: 4, 75: 2, 97: 1; 26 concept-bearing forms)
recount identically from `freeze-v2-vocabulary-2026-11-20.json`
and `freeze-v3-vocabulary-2026-11-22.json`, and agree with
the OD-16 comparison's scoring projection and the OD-17
audit §3.3. No Stage 4 number, verdict, or standing is
touched: Stage 4.2 ran under freeze v2, and freeze v3 is
for future work only — which is why the correction
matters: a future test frozen against v3 now inherits a
correctly labelled table.
