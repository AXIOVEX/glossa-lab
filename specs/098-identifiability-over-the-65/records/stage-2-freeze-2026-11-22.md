# Spec 098 — Stage 2 Freeze (2026-11-22)

**Commission:** the owner's act in the Glossa-Lab chat,
2026-11-22 02:31 ET ("Commission Spec 098 Stage 2").
**Stage frozen:** Stage 2 of `tasks.md` — T201 (rival
construction) and T202 (prediction sheets), development data
only. **Venue:** tower-compute, fresh clone under
`~/glossa-work/` (freeze v1 §6). This freeze answers, on its
face, the three demands the Stage 2 design note
(`records/stage-2-design-note-2026-11-21.md`, as corrected by
`records/stage-2-design-note-correction-2026-11-21.md`)
makes of any Stage 2 freeze, and fixes the construction
rules Stage 2 executes under. It changes no parameter of
freeze v1 §§3–5 and no bar, penalty, seed, or outcome rule;
a change to anything it fixes is a new freeze version,
recorded as such.

## 0. Population, as executed

Confirmed at execution from the current standings record
(Spec 091 standings supplement, as amended by the M044 act):
the partition of record is **4 E + 65 I + 4 R + 3 P + 18 U =
94**. This study's population is the annex population as
amended by the execution freeze annex (70) and its Round 2
amendment (69): **69 signs — Arm I, the 65; Arm E, four
(M047, M124, M329, M330)**. M202 and M044 have left the
population by the two addendum-rule strikes; M374 remains in
Arm I at its frozen UNDECIDABLE default (T102). The
multiplicity family for Stage 2 reporting is these 69 signs.

The F-9 act (the M047 class-E definition question, adopted
by the owner 2026-11-22) had **not landed** on origin/main
at the execution commit (`6bcd95eb`); no F-9 pull request
was open. M047 is therefore a member of this population as
class E, on its entry exactly as filed (candidate value
min/mīn, DEDR 4897). An F-9 amendment to M047's entry basis
would not change its membership, its class for this study's
purposes, its candidate value, or this population; if it
lands before Stage 3, Stage 3's record states it.

## 1. The bar arithmetic, answered (design note demand 1)

**The bar stands as frozen.** It is not re-registered.
Freeze v1 §5, as the RT2-03 correction record restates it: a
sign is DISCRIMINATED (at best DISCRIMINATED ON
PSEUDO-HELD-OUT, §3 below) only if **both** hold at scoring:

- its **penalized margin is at least 10 nats** over the best
  rival, the flexibility penalty being **2 nats per free
  choice** (unresolved variant alternation, homophony
  allowance, gloss alternation), charged to candidates and
  rivals alike; and
- the margin **exceeds the permutation null's 99th
  percentile** (B = 999, seed 9801).

The per-sign arithmetic, stated in advance as the design
note requires: against a rival carrying no free choices, a
candidate carrying *k* free choices faces an effective
threshold of **10 + 2k nats** over its held-out tokens. At
the frozen 5-token floor that is an average advantage of
**2.0 nats per token** (k = 0), **≈2.4** (k = 1), **≈2.8**
(k = 2), sustained across every held-out token the sign
has — before the null conjunct, which can only raise the
effective bar. The bar does not scale down for signs with
fewer tokens. The per-sign figures (free choices itemized
under §4, threshold, per-token burden at the sign's
expected held-out count) are computed by
`tools/stage2_run.py` and filed in the Stage 2 outcome
record's data (`records/stage-2-outcome-2026-11-22.json`).
The expected consequence is stated here so it cannot be
re-narrated later: at this bar, UNDECIDABLE AT THIS POWER
and NOT IDENTIFIABLE are the expected outcomes for most of
the population, exactly as freeze §7 gap 3 and the Stage 1
grid anticipated.

## 2. Per-sign eligibility by count (design note demand 2)

The correction record (§3) requires this freeze to state
**how** per-sign counts are established under the
pseudo-held-out ceiling, Stage 1 having produced expected
counts only. The method, fixed here:

- **Stage 2 eligibility is stated from the Stage 1 power
  grid** (`records/stage1-grid-2026-11-21.json`), whose
  counts are development-side: each sign's development token
  count over the deduplicated development clusters, and its
  **expected held-out count** (development count ÷ 4, the
  frozen split's 4:1 expectation). Stage 2 reproduces those
  counts from the corpus of record and verifies them
  against the grid before any construction (the runner's
  grid-reproduction check; a mismatch halts the run).
- **No actual held-out count is stated anywhere in
  Stage 2.** The actual per-sign held-out counts are
  established exactly once, at Stage 3 scoring, from the
  custody list released to the scoring path on that single
  recorded occasion, verified against the seal (seal record:
  517 held-out clusters, SHA-256
  `1974d83a5f667b71dbd53ecdb2e42a8221c6d4b91bdd32202b2a80579bf96cf9`).
  Decision rule 1's count arm binds at Stage 3 on those
  actual counts.
- Eligibility classes in this freeze, per sign (the full
  69-row table is filed with the outcome record's data):
  - **ELIGIBLE IN EXPECTATION** — expected held-out count
    ≥ 5: **21 signs** (M015, M017, M025, M050, M051, M053,
    M060, M062, M065, M067, M070, M089, M099, M124, M130,
    M145, M194, M267, M347, M375, M391).
  - **BELOW FLOOR IN EXPECTATION** — expected held-out
    count < 5: **47 signs**. These stand to be UNDECIDABLE
    AT THIS POWER at scoring unless their actual held-out
    counts beat the expectation (execution freeze annex,
    §2); Stage 2 records their outcome in exactly those
    terms.
  - **FROZEN DEFAULT** — M374: UNDECIDABLE AT THIS POWER,
    unscored, by the T102 record. **1 sign.**
- The seal is **not** opened, read, or released in
  Stage 2. The custody file at
  `~/glossa-custody/spec098/heldout-clusters-v1.txt` is not
  read by any Stage 2 process. Stage 2's development export
  is built by recomputing the frozen split rule over the
  corpus of record (the computation Stage 1 itself ran);
  the recomputed held-out set's seal hash is verified
  against the committed seal — a verification that the
  recomputation equals the sealed partition, producing no
  held-out content — and the TC-098-01 guard
  (`tools/seal_and_score.py`, `development_export`) is run
  over the actual development export, as T201's acceptance
  requires. No held-out sequence, token, or per-sign
  held-out count is examined or stated.

## 3. The ceiling, carried verbatim (design note demand 3)

**Every result is DISCRIMINATED ON PSEUDO-HELD-OUT at
best, because no genuine holdout exists (T101).** The
outcome IDENTIFIABLE ON HELD-OUT is unavailable to this
study as constituted (claim C098-6).

## 4. Free-choice accounting (freeze v1 §5, applied)

Charged per competitor, 2 nats each at scoring; counted
here, identically for candidates and rivals:

- **Variant alternation:** 1 per disjunction in the value
  as recorded in the population annex. In this population:
  M047 (min/mīn), M051 (pū/puḷ), M089 (tu/tū), M099
  (kol/koḷ), M267 (iN/in), M391 (ka/kaṇ) — 1 each.
- **Homophony allowance:** 1 per sign whose recorded value
  is carried by two or more signs **in the executed
  population of 69**, counted on exact recorded values:
  kuṉ (M002, M020), mā (M015, M026), māṟ (M027, M075),
  mi (M053, M054), nēr (M018, M069), kōṉ (M005, M073),
  yānai (M029, M045), kēḷ (M004, M037), ka (M061, M347),
  kuTam (M065, M124) — 1 each for each member sign. Two
  edge cases are stated, not smoothed: M391's value is the
  disjunction ka/kaṇ, not the value ka, so M391 is charged
  its variant alternation only, and M061/M347's allowance
  is counted on the exact value ka they share; M330's value
  can is carried by no other sign in the executed
  population (M202 has left it), so M330 is charged no
  homophony allowance — the allowance prices flexibility
  inside the tested population, and the M202 exit is a
  population amendment of record.
- **Gloss alternation:** 1 where the candidate's own record
  states two glosses for the one value: M047 (DEDR 4897,
  fish/star, per the T303 application record) and M329
  (gloss 'gold, precious; personal name', per the same
  record) — 1 each.
- Rivals as constructed under §5 are single values carrying
  no variant, homophony, or gloss alternation: **0 free
  choices** each, except the Arm E cross-sign rival for
  M330, which carries M202's evidence package and M202's
  accounting (0 free choices; its value is can, identical to
  the candidate's — the rivalry is of evidence packages,
  per spec §3.4).

Resulting candidate totals are computed per sign by the
runner and filed in the outcome data; the largest is
M047's: variant 1 + gloss 1 = **2** (threshold 14 nats
against a zero-choice rival).

## 5. Rival construction rules (T201; freeze v1 §4 applied)

One deterministic construction per competitor, executed by
`tools/stage2_run.py`. **Tuning budget (WP8 fairness,
Standards Part III rule 2):** every competitor — candidate
and each rival — receives exactly this one construction
pass, over the same development data and the same frozen
search space; no competitor is iteratively fitted, revised,
or re-drawn after any result; the candidate's own
construction is its filed basis, untouched. Frequency and
position matching for R-A/R-B is by construction, on WP8
control family C2's own terms: a wrong mapping for the same
sign inherits that sign's frequency profile and positional
profile exactly, so no competitor can win on frequency or
position alone; the value-side condition the freeze adds is
syllable shape.

- **Shape.** Computed on a normalized form of each value
  (normalization is for shape computation only; values of
  record are never respelled — claim C098-2): lowercase;
  diacritics folded (ā ī ū ē ō → a i u e o; ṅ ñ ṇ → n;
  ṭ → t; ḍ → d; ḷ → l; ṟ → r; ś ṣ → s); the annex's ASCII
  conventions folded the same way (capital L/T/D/N/R as the
  corresponding retroflex/nasal; the Phase notation '3' as
  the nasal); long-vowel doubling collapsed (aa ee oo →
  a e o), matching the lexica of record, which are
  length-collapsed. The shape of a normalized value is its
  syllable count together with each syllable's coda class
  (open / nasal / stop / liquid / other), syllabified by
  vowel nuclei with a maximal single-consonant onset. For a
  disjunctive candidate, the shape is that of its
  first-listed alternant. The implementing function is
  `shape()` in `tools/stage2_run.py`; this text and that
  function are the same rule, and any divergence between
  them is a defect against this freeze.
- **R-A (matched wrong Dravidian value, C2/C5).** Pool, in
  order: (1) the recorded candidate values of the other
  signs of the executed population, in annex order (Arm I
  annex order, then Arm E); (2) the keys of the
  Proto-Dravidian VOCABULARY of record
  (`backend/glossa_lab/data/dravidian.py`, 1,740 roots).
  Filter: same shape as the candidate; not equal to the
  candidate's value or any of its alternants. Draw: the
  first pool value passing the filter. If none passes, R-A
  is recorded NOT CONSTRUCTIBLE for that sign, with the
  shape and pool sizes stated — the gap is a Stage 2
  finding, not a licence to widen the space (freeze §3.6
  closes it).
- **R-B (unrelated-family value, C5).** The same rule over
  the Indo-Aryan/Sanskrit VOCABULARY of record
  (`backend/glossa_lab/data/sanskrit.py`). Freeze §4's
  second named family, Munda, is **not carried** by any
  lexicon of record in the repository (the
  `glossa-corpus/lexica/` directories carry provenance
  records only; their data files are not in the
  repository), so R-B is drawn from Sanskrit for every
  sign, and that absence is recorded here rather than
  filled from outside the frozen space.
- **R-C (logogram rival, C1/C3).** The sign carries the
  candidate value's referent as a logogram, with no
  phonetic value. The referent gloss is stated from the
  record where the record carries one (the VOCABULARY
  gloss of the normalized candidate, or the T303/record
  gloss for Arm E); where no gloss is on record, the rival
  is defined by its function alone and says so.
- **R-D (structural-only model, C6-adjacent baseline).**
  No value assignment at all: the language-neutral
  order-1 neighbour-pair model over the sign's
  development contexts, unconditioned — the annex
  estimator with the unconditioned assignment (§6).
  Beating R-D is necessary and not sufficient (spec §3.4).
- **R-E (global permutation, C1/C2, model level).** One
  model for the whole study: within each shape class of
  the executed population holding two or more signs, the
  recorded candidate values are rotated by one position in
  annex order; signs in singleton shape classes are fixed
  points. The full permutation is filed in the rivals
  record. It is scored as one model at Stage 3, not as a
  per-sign rival; per-sign records reference it.
- **Arm E additions (spec §3.4), from the T303 application
  record, for the four Arm E signs of the executed
  population:** M047 — comparandum-as-value rivals 'in'
  (Elamite, MC-01) and 'mina' (Sanskrit, SL-06); no
  cross-sign pair is named for M047 in the spec. M124 —
  the comparandum itself as value, 'kun' (Elamite, MC-18;
  the Sanskrit comparandum 'kona', SL-04, is recorded with
  it), being M044's comparanda package, the cross-sign arm
  the spec names for this sign. M329 — the comparandum
  itself as value, 'pur' (Elamite 'bur/pur', MC-21; the
  Sanskrit comparandum 'pura', SL-14, recorded with it).
  M330 — the cross-sign rival proper: M202's evidence
  package (Elamite 'an', MC-07; Sanskrit 'annam/anna',
  SL-03; value can), plus comparandum-as-value rivals 'an'
  (MC-07) and 'anna' (SL-03).

## 6. Prediction-sheet construction and review (T202)

A sheet is a pre-unsealing document (spec §3.5): it names,
for the candidate and for each rival, at least one
observable on held-out data on which their predictions
differ in a value-relevant dimension, and it carries the
occurrence assignment the execution freeze annex's
estimator requires ("the development occurrences the
Stage 2 prediction sheets assign to v"). The rules applied
in construction and review, fixed here:

- **Observable space.** The frozen estimator scores
  order-1 neighbour-pair contexts and nothing else, and
  the corpus of record carries no motif or iconography
  field on any sequence-bearing record (verified by the
  runner over the pinned export: the fields are citation,
  artifact type, grapheme sequence, crosswalk coverage,
  identifiers, rights, sign scheme, instance count, site
  name, source system, and the diplomatic codes). A
  differing observable therefore counts for this study
  only if it is a prediction about the **identity or class
  of neighbouring signs** on held-out occurrences (spec
  §3.5 categories (i) and (iii)). Category (ii), motif and
  context associations, names observables this study's
  held-out data does not carry and its estimator cannot
  score; a sheet resting on a motif association alone is
  **not accepted**, and the reason is recorded per sign —
  the category is answered in the open, not silently
  dropped. This expressly includes the spec's own example
  pair (M006 puli against M080 vēṅkai): on this corpus of
  record the distinguishing observable does not exist for
  the scoring path, and the motif claims themselves are
  not reproducible from the records (Spec 091 motif and
  numerical evidence record, PR #634). Site name and
  artifact type are provenance, not value-relevant
  observables under §3.5.
- **Acceptance.** A sheet is ACCEPTED iff the frozen record
  (the population annex row; the sign's Spec 099 inference
  log entry; the T303 application for Arm E; the Spec 091
  rerun records) states, for the candidate, a
  neighbour-identity or neighbour-class prediction — a
  filed collocation with a named sign, a filed slot pattern
  with named flanking signs, or a filed sign sequence —
  that the rivals as constructed do not state, so that the
  candidate's predictions on held-out occurrences differ
  from every per-sign rival's (each rival taking the
  unconditioned assignment under the assignment rule
  below; R-E is a model-level arm and carries no per-sign
  sheet). A sheet whose only differing observable is
  position or frequency is REJECTED (§3.5); a sign for
  which no such prediction is on record has **no
  constructible sheet** and is recorded NOT IDENTIFIABLE
  by construction (spec §3.5, claim C098-4), with the
  specific gap named per sign in the sheets record. No
  grammatical role, collocation, or gloss may be
  introduced in Stage 2 that is not already on the frozen
  record (spec §3.6: the dictionary-search space is closed
  at the freeze, and grammatical assumptions are the annex
  rows' as recorded).
- **Assignment.** On an accepted sheet, each value's
  signature is the neighbour set its record states (side
  specific where the record is side specific). The
  development occurrences assigned to a value are the
  sign's development occurrences whose neighbour pair
  meets the signature; a value with no stated signature
  takes the unconditioned assignment (all of the sign's
  development occurrences). Signatures come exclusively
  from pre-freeze filed records — nothing is fitted,
  searched, or tuned in Stage 2 — and the rule is the same
  for candidate and rivals (WP8 matched budget: one
  deterministic construction each; the asymmetry that only
  candidates carry filed derivations is the study's
  subject, and the flexibility penalty and the bars are
  its controls).
- **Precedence in Stage 2 outcomes.** Outcomes are stated
  under spec §4's precedence as far as Stage 2 can state
  them: the M374 frozen default and the below-floor-in-
  expectation UNDECIDABLE outcomes (rule 1, on the grid
  arm) precede the by-construction NOT IDENTIFIABLE
  outcomes (rule 2, sheet arm). Both are recorded with
  their basis and with their Stage 3 contingency stated:
  rule 1's binding test is the actual held-out count at
  scoring, so an in-expectation outcome can be displaced
  at Stage 3 in the direction the actual counts dictate,
  and a by-construction outcome on a below-floor sign is
  recorded as the sheet determination, not as the sign's
  outcome.

## 7. What Stage 2 does not produce

**Per-sign margins and permutation-null percentiles are
Stage 3 quantities.** Under the frozen estimator they are
functions of held-out log-likelihoods (see the reference
`decide` rule in `tools/seal_and_score.py`, whose inputs
are held-out token counts, candidate and best-rival
held-out log-likelihoods, and the null's 99th percentile),
and the held-out list is released to the scoring path
exactly once, at Stage 3 scoring (freeze v1 §3, claim
C098-1). They therefore do not exist in Stage 2 and are
recorded in the Stage 2 outcome record as **not computed —
Stage 3**, per sign. No development-side substitute margin
is computed or reported: a substitute would be a different
statistic from the frozen one, and reporting it under the
frozen outcome vocabulary would misstate the study. The
Stage 2 outcome record states every outcome Stage 2 can
determine (rule 1's default and grid arms; rule 2's sheet
arm; the signs that proceed to Stage 3 with accepted
sheets), the rival identities for every sign, and the
eligibility and threshold arithmetic for every sign; the
four signs that proceed carry no frozen-vocabulary outcome
until Stage 3 scores them.

## 8. Run discipline

Every Stage 2 run is indexed in the outcome record (Spec
089 discipline, claim C098-8), failures included, and every
reported verdict is the run's own payload verdict. Merges
only on genuine per-job CI green (10 jobs, read per job).

**AI disclosure:** executed by an AI agent (Muse, via
Muse) at the direction of Tristen Pierson, per
constitution sec. VI.
