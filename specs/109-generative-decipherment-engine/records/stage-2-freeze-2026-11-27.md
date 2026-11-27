# Spec 109 — Stage 2 Freeze (T201 and T202)

**Frozen 2026-11-27, before any computation under it.**
This freeze fixes every constant registration
`records/registration-2026-11-27.md` §§3–4 marks
FREEZE for the two licensed Stage 2 legs, states
their effective Ns from a counting-only census, and
states the exact statistic forms the runs will use.
No check statistic of either leg was computed before
this freeze was written; the census below counted
presences and population sizes only, in the pattern
of Spec 093's T402 counting pass.

**Licensing basis.** Stage 1's preflight
(`records/stage-1-preflight-2026-11-27.md` §6,
`records/stage-1-close-2026-11-27.md` §4) licenses
Stage 2 for Part 2's positional-class and
numerical/metrological output kinds and for Part 3's
context channel. Part 2's segmentation and
recurrent-partial families FAILED the preflight and
are **not executed in this stage**; no segmentation
or partial statistic is computed on the corpus under
this freeze. Part 3's iconography sub-channel is
GATED (spec.md §6) and no iconography input is used.
Part 2's verdict in this stage is therefore a verdict
over the two licensed families, and the outcome
record states that scope on its face.

## 1. Data pins (verified at freeze time)

| Input | Pin (SHA-256) |
|---|---|
| Spec 105 custody `indus-derivation.json` (1,336 artifacts, 5,611 tokens, 372 marks) | `84476daa3a1d9ded33ee7c3eeaffb29fac0290ecf3507873206d4d60ac8b948b` |
| Spec 105 custody `indus-reserve.json` (334 artifacts, 1,391 tokens) | `bfbe79cb2d2d7c131fb0e2c7cc8004995d36af6c3e4cc5b1cdb5bb5ed29930ff` |
| `outputs/phase100_full_corpus.json` (1,670 translations) | `c2b14e94971f438cfd25f24123db975de6c02980e0e425cffb91fbc4de4d578c` |
| `outputs/phase114_full_seal_translations.json` (1,670 translations) | `07b84a9c82f0fb5328d6ab344d038a3a0a984079f99804f2014580a28aa40196` |
| `glossa-corpus/indus/canonical/objects.jsonl` (canonical store; matches Spec 093's T103 pin) | `e24f42a95ee4cc1fdb16c789c3edfb937993ed7c82223d6daa96d66895174ae5` |
| Spec 093 join output `specs/093-material-context-channel/records/t103-join-pairs-v1.jsonl` (179 pairs) | `7107f738832a4e3b04cff91d81073212bc0f3a77afed6f0ccc3cee4fce621703` |
| Spec 105 Stage 3 output (the filed L3 table) `specs/105-elsewhere-sandbox/records/stage-3-output-2026-11-25.json` | `b80b7d997327d9130274e1527ecf73d44f7eafcb22fa4bba596b4541b4bbb3c8` |
| Spec 091 motif-numerical evidence record (JSON companion; counted-sign set and site census of record) | `23e2f0f43cfe79da77b7cde3860c27580a09e4b9019a6d6ff0a585baecc505e8` |

The full corpus of registration §3 is the union of
the two custody datasets: 1,670 artifacts, 7,002
tokens, 390 marks (derivation 1,336 / 5,611 / 372;
reserve 334 / 1,391; the reserve's seal is spent,
spec.md §5, and it enters here as corpus material
for induction statistics, which score nothing
against it). Every custody artifact carries exactly
one recorded group (derivation 1,336 groups over
1,336 artifacts, reserve 334 over 334, per Spec
105's filed totals and the freeze census), so an
occurrence's position is its position within its
artifact's single group, under Spec 105's D-105-14
rule: length-1 group → sole; first → initial; last →
final; otherwise medial. The population files record
one sign list per seal; positions there are
positions within that list, the same rule.

## 2. Part 2 freeze (registration §3)

**Positional family.**
- Measurable mark: ≥ 5 tokens in the population the
  statistic is computed over. Full-corpus measurable
  marks: **151** of 390 (census). Derivation-set
  measurable marks: 126 of 372.
- Restriction: a mark is class-restricted at level ρ
  if its positional distribution (initial / medial /
  final / sole) has a **unique** dominant position
  whose share is ≥ ρ. ρ ∈ {0.95, 0.90} as registered.
  A tied argmax has no dominant position and cannot
  be restricted.
- Structures: each (mark, ρ, dominant position)
  restriction call over the full corpus for a
  measurable mark.
- L3 reconciliation: the derivation-set positional
  counts are recomputed and compared cell by cell
  against the filed L3 table (372 marks × sole /
  initial / final / medial). The comparison of
  record is exact equality; any inequality is filed
  as a divergence finding, not silently resolved.
  Call-level comparison (full-corpus calls vs the
  L3 derivation-set calls, both ρ levels) is filed
  with divergences itemized.
- Split halves: the derivation set split
  duplicate-aware — distinct sequences by
  first-appearance ordinal in the derivation file,
  ordinal % 2 == 0 to half A, odd to half B, every
  copy of a sequence in the same half. Census: half
  A 669 artifacts, half B 667; 1,324 distinct
  sequences; **75 marks** carry ≥ 5 tokens in both
  halves (the upper bound on stability-measurable
  structures).
- Stability tolerance (registered here): a structure
  (mark, ρ, dominant position) is **STABLE** iff the
  mark carries ≥ 5 tokens in each half, is
  restricted at ρ with the same dominant position in
  each half, and its full-corpus call is that same
  call. It is **UNSTABLE** iff it is measurable in
  both halves and either half's call differs. It is
  **INDETERMINATE** (per structure) iff the mark
  carries < 5 tokens in either half.
- Per-site validation: for each full-corpus
  structure, at each site where the mark carries
  ≥ 5 tokens in the population files (Part 3's site
  join), the site's dominant position is computed
  and filed (agreement = equal to the structure's
  dominant position). Per-site figures are filed as
  the out-of-stratum validation of registration §3;
  the STABLE call itself rides on the split halves,
  as §3's stability rule states.
- Null: within-artifact shuffle of signs (preserves
  each artifact's length and sign multiset, hence
  the corpus frequencies), B = 999 draws, seed
  string `spec109-s2-posnull-v1` (seed integer =
  first 8 bytes of the string's SHA-256, big-endian;
  the same derivation for every seed in this
  freeze). Filed per ρ: the observed restricted-call
  count and its percentile in the null distribution
  of restricted-call counts over measurable marks.

**Numerical / metrological family.**
- Counted-sign set, as filed in Spec 091's
  motif-numerical evidence record §5: **{M012, M059,
  M391}** (tokens over the full corpus, census:
  M012 143, M059 222, M391 193 — equal to the filed
  record's counts).
- Context populations (census): **F** — seals tagged
  NUMERAL_FORMULA in phase100: 14 seals, of which 4
  bear a counted sign (1 token each) and 10 bear
  none. **T** — artifacts bearing ≥ 1 counted sign:
  486 over the full corpus (derivation halves 199 /
  187); an artifact's count is its counted-sign
  token total. **R** — stroke-series runs (maximal
  runs of one counted sign of length ≥ 2): 4 over
  the full corpus (halves 1 / 2) — below any floor;
  filed as a census fact with run lengths, not as a
  check population. **C** — combination contexts
  (artifacts bearing ≥ 2 counted tokens): 68 over
  the full corpus (halves 31 / 26).
- Check 1, bounded range (population T): statistics
  are the count distribution's maximum, its
  variance, and its share of contexts with
  count ≥ 3. Null: the unconstrained-tally shuffle,
  identified here with the §3 family null form —
  within-artifact shuffle of signs, which leaves
  tallies unconstrained by position — B = 999, seed
  string `spec109-s2-numnull-v1` (one null stream
  shared by checks 1 and 3). **SUPPORTED** iff
  maximum ≤ 5 AND observed variance is below the
  null's 5th percentile AND observed share
  (count ≥ 3) is at or below the null's 5th
  percentile. Otherwise NOT SUPPORTED, figures
  filed. (The design queue's falsifier for this
  family is that the counts distribute as
  unconstrained tally noise under the null; this
  rule is that falsifier mechanized.)
- Check 2, positional restriction (counted set):
  the three counted signs' full-corpus restriction
  calls at both ρ levels, from the positional
  machinery. **SUPPORTED** iff at least one counted
  sign is restricted at ρ = 0.90 over the full
  corpus. Otherwise NOT SUPPORTED, figures filed.
- Check 3, combination consistency (population C):
  the registered place/count model form is fixed
  here as the **additive tally with a contiguous
  tally block**: in a combination context, the
  counted tokens form one contiguous block of the
  artifact's sequence. Statistic: the share of
  combination contexts whose counted tokens are
  contiguous. Null: the check-1 stream.
  **SUPPORTED** iff the observed share exceeds the
  null's 99th percentile. Otherwise NOT SUPPORTED,
  figures filed.
- Stability: each check is recomputed on both
  derivation halves (check populations per half
  from the census: T 199 / 187, C 31 / 26 — both
  above the floor of 10 per half fixed here; check
  2's half form is the counted signs' half calls).
  A check is **STABLE** iff both halves return the
  full corpus's supported / not-supported direction;
  **UNSTABLE** iff a half disagrees; a check whose
  half population fell below the floor of 10 would
  file INDETERMINATE (none does, per the census).
  A check SUPPORTED and STABLE files one structure
  hypothesis to the gates; SUPPORTED and UNSTABLE
  files as an unstable structure with figures; NOT
  SUPPORTED files no structure.

**Part 2 verdict (registration §3, over the licensed
families).** POSITIVE iff at least one STABLE
structure is filed to the gates; NEGATIVE iff no
structure is stable in either licensed family;
INDETERMINATE per family iff that family's stability
is not measurable at these floors (filed per family,
not averaged away).

**Gate filings.** Each STABLE structure is filed in
the outcome record with a gate filing reference:
positional-class structures to Spec 091's anchor
comparison; numerical structures to Spec 098's
identifiability gate. A filing is a candidate for
that gate under its own registration; no gate is run
in this stage and no standing moves.

## 3. Part 3 freeze (registration §4)

**Join (a) — population site join.** Inner join of
phase100 and phase114 on `cisi_id` (1,670 ids on
each side). A seal whose site or sign list disagrees
between the two files is excluded from the join and
counted, with the disagreements itemized.
Validation: the joined seals' site census must
reproduce the filed site census of Spec 091's
record (motif-numerical evidence §5) **exactly**:
Mohenjo-daro 606, Harappa 492, Lothal 124,
Kalibangan 110, Dholavira 106, Chanhu-daro 78,
Surkotada 61, Banawali 60, Rakhigarhi 33 (total
1,670). A mismatch is a **STOP**, filed, and the
channel does not run.

**Join (b) — Spec 093 census join.** The pinned
join output at §1. Validation: exactly 179 pairs;
the material census exactly Steatite 176, Clay 1,
Faience 1, and 1 pair carrying the empty sentinel
(the recorded value `-`); every pair's site
Mohenjo-daro; every pair's `text_id` resolving to a
canonical object in the pinned objects file, whose
`_source_extra.raw_signs` is the pair's sign
sequence (Parpola P-scheme). A mismatch on any count
is a **STOP**, filed. The census's filed limit rides
on every use: all 179 pairs are Mohenjo-daro, single
stratum (C093-1, INDEPENDENT IN PART); the material
and find-context channels are single-site channels
and no record of this part may present them as more.

**Contexts.** Site (join (a)): the 9 site values.
Material (join (b)): `material_raw` as recorded
(Steatite, Clay, Faience, and the `-` sentinel,
which is filed as its own context value of N = 1 and
carries no usable signal, as Spec 093's T402
recorded). Find context (join (b)): `area_section`
as recorded — Spec 093's T202 field definition — 18
distinct values over the 179 pairs, every pair
carrying a value.

**Channel statistic (per sign, per context
family).** For sign s and context family with values
v: T(s) = Σ_v (n_{s,v} / n_s) · Σ_c P̂(c | s, v) ·
log [ P̂(c | s, v) / P̂(c | s) ], over the four
position classes c, with rates estimated on the
family's joined population and no smoothing (cells
with P̂(c | s, v) = 0 contribute 0). A sign's term is
**scored** iff n_s ≥ 5 in the family's population;
terms for all signs are computed, below-floor terms
flagged unscored. Site family population: the 1,670
joined seals (M-scheme signs; 390 distinct, 151 at
≥ 5 tokens). Material and
find-context family population: the 179 pairs
(P-scheme signs, 182 distinct, 50 at ≥ 5 tokens,
1,003 tokens — census).

**Null and cap.** Per family: context labels
permuted within length strata (stratum = the seal's
sign count), B = 999, seed string
`spec109-s2-ctxnull-v1`. The family's **cap** is the
99th percentile of the pooled null distribution of
per-sign terms (scored signs); a filed term's
contribution to any later candidate margin is
capped at its family's cap, as registered.

**Weights (the formula FREEZE of registration
§4).** Each context family is weighted by its join's
effective N as a share of the two joins' total:
w_site = 1670 / 1849 = 0.9032; w_material =
w_find-context = 179 / 1849 = 0.0968. The combined
term for a candidate is the sum over families of
w · T(s), summed over the candidate's scored signs,
each family's contribution capped at its cap before
weighting. The two joins live in disjoint sign
universes (M-scheme and P-scheme; no tracked
crosswalk exists — Spec 091's record §6), so no
combined per-sign term across universes is defined
or filed in this stage; the terms are filed per
family with their weights and caps, and the
universe boundary is stated on the channel record's
face.

**Out-of-site validation (the registered
prediction).** Filed classes: Part 2's full-corpus
positional classes at ρ = 0.90 as filed by T201 in
this stage (restricted signs with their dominant
positions; all other measurable signs unrestricted).
Directions: Mohenjo-daro → Harappa and Harappa →
Mohenjo-daro, over join (a)'s seals at those sites.
Duplicate-aware: a validation seal whose sign
sequence occurs at the fit site is excluded from the
validation profiles and counted (census: validation
seals kept 488 of 492 Harappa-side, 602 of 606
Mohenjo-daro-side). For measurable sign s (≥ 5
tokens on the fit site and ≥ 5 on the kept
validation seals; census: 53 signs each direction):
the cross-site term T_{F→V}(s) = Σ_c q̂_V(c | s) ·
log [ q̂_V(c | s) / q̂_F(c | s) ], the KL form of the
registered statistic with the fit site's rates as
the reference distribution, profiles smoothed with
α = 0.5 added to each of the four position cells
before normalization. Statistic per direction:
Δ_dir = median T over measurable unrestricted signs
− median T over measurable restricted signs; the
registered prediction is Δ > 0 (classed signs'
positional profiles travel out-of-site; unclassed
signs' drift more). Pooled statistic: the mean of
the two directions. Null: site labels permuted
within length strata over the pooled Mohenjo-daro +
Harappa seals, B = 999, seed string
`spec109-s2-valnull-v1`, the full pipeline (profiles,
terms, Δ) recomputed per draw with the filed classes
held fixed. Floors: a direction is measurable iff
it carries ≥ 20 measurable signs and ≥ 5 measurable
restricted signs; a direction below its floors files
INDETERMINATE at its floors.

**Channel verdict (registration §4).** CHANNEL
POSITIVE iff both joins validate and the pooled Δ
exceeds its null's 99th percentile. CHANNEL NULL iff
both joins validate and the pooled Δ is at or below
the 99th percentile (filed; the term is withdrawn
from this study's scoring). INDETERMINATE iff a join
validation STOPs or a validation direction is below
its floors.

**Labels.** Every context score filed in this stage
carries the label **no iconography component** (the
iconography sub-channel is gated and inactive), and
every use of join (b) carries its single-site limit.
The context term is additive evidence for other
parts' scoring; it is not a margin and cannot
substitute for one.

## 4. Provenance, replay, and records

The harness is filed in this spec's records with its
SHA-256 in the outcome records; every figure is
produced by two independent implementations in exact
agreement (a disagreement is a STOP, filed).
Candidate records (induced structures and context
terms, each with generator pin, seed, data pins, and
this freeze as its constraint-set version) are held
in the generated-hypotheses register in custody
under `glossa-custody/spec109/`, never committed;
the outcome records carry the register's pin.
TC-109-03's replay at this stage: the harness re-run
from the filed pins reproduces the register exactly.
TC-109-04 recomputes the positional family from the
filed intermediate tables; TC-109-05 recomputes the
channel's validations and one filed term from the
filed join tables.

**AI disclosure:** executed by an AI agent (Muse, via Muse)
at the direction of Tristen Pierson, per constitution sec. VI.
