# Spec 109 — Stage 2 Part 2 Outcome Record (T201)

**Date:** 2026-11-27. **Leg:** Part 2, structure
induction, executed under registration
`records/registration-2026-11-27.md` §3 and the
Stage 2 freeze (`records/stage-2-freeze-2026-11-27.md`,
SHA-256 `f51de777…`, committed before any computation
under it). **Licensing:** Stage 1's preflight licensed
this leg for its positional-class and
numerical/metrological output kinds only
(`records/stage-1-close-2026-11-27.md` §4). The
segmentation and recurrent-partial families were NOT
executed and no statistic of theirs was computed on
the corpus; this record's verdict is a verdict over
the two licensed families, stated here on its face.
**Execution:** `records/stage-2-harness.py` (SHA-256
`149b4f7a…`), run on tower-compute 2026-11-27, payload
exit 0; raw output at `records/stage-2-raw-output.json`
(SHA-256 `433017fa…`, byte-identical to the custody
original); intermediate tables at
`records/stage-2-positional-table.json` and
`records/stage-2-numerical-table.json`; candidate
records in the generated-hypotheses register in
custody (`glossa-custody/spec109/
stage-2-generated-hypotheses-register.jsonl`, SHA-256
`56d2a8aa…`, 516 records across both Stage 2 legs).
Every figure was produced by two independent
implementations in exact agreement inside the harness;
TC-109-04's independent recomputation is filed at the
stage-close record. **No standing, verdict, anchor, or
tally in any program moved; every structure below is a
generated hypothesis filed to a gate, not an
adjudicated fact.**

## 1. Corpus and L3 reconciliation

The corpus census reproduces the filed censuses
exactly: full corpus 1,670 artifacts / 7,002 tokens /
390 marks; derivation set 1,336 / 5,611 / 372; reserve
334 / 1,391. The derivation-set positional counts
recompute the filed L3 table **exactly, cell by cell,
over all 372 marks** (sole / initial / final / medial;
0 mismatched marks). The induction therefore
reproduces the comparison of record where they
overlap, as registration §3 requires.

Call-level comparison, full corpus against L3 (the
derivation set): 50 divergent (mark, ρ) pairs over 25
distinct marks, **all in one direction** — marks
restricted over the full corpus that are not
restricted in L3 (each at both ρ levels) — and zero
L3 calls lost, zero dominant-position conflicts. The
full-corpus induction extends L3 monotonically; the
25 marks are itemized in the positional table file
as divergence findings, as registered. (Their
restriction emerges from the reserve's 334 artifacts
joining the count; most were below the measurable
floor or below ρ on the derivation set alone.)

## 2. Positional family

Measurable marks (≥ 5 tokens, full corpus): 151 of
390. Restricted calls: **131 marks at ρ = 0.95 and
the same 131 marks at ρ = 0.90** — the two registered
levels induce identical sets on this corpus, because
no measurable mark's dominant share falls in
[0.90, 0.95). Against the registered shuffle null
(within-artifact, B = 999): observed 131 restricted
calls at each level against a null mean of 2.9, null
maximum 9, null 95th percentile 6 — observed
percentile 1.0. The corpus's positional restriction
is decisively beyond its null.

Stability (split halves of the derivation set,
duplicate-aware, 669 / 667 artifacts; tolerance as
frozen):

| ρ | STABLE | UNSTABLE | INDETERMINATE |
|---|---|---|---|
| 0.95 | 53 | 2 | 76 |
| 0.90 | 55 | 0 | 76 |

The 76 INDETERMINATE calls per level are marks
measurable over the full corpus but carrying < 5
tokens in one derivation half; they are filed with
their figures and are neither stable nor unstable.
The two UNSTABLE calls at ρ = 0.95 are M249 (final;
half A differs) and M305 (final; half B differs);
both are STABLE at ρ = 0.90 with the same dominant
position. Distinct STABLE marks: **55** (53 stable at
both levels; M249 and M305 stable at 0.90 only) —
**108 STABLE (mark, ρ) structures** in all. Their
dominant positions: initial 104, final 4 — the stable
positional structure of this corpus is overwhelmingly
initial restriction.

Per-site validation (over Part 3's site join): across
the 108 stable structures, 160 site cells were
measurable (mark ≥ 5 tokens at the site), and the
site's dominant position agrees with the structure's
in **160 of 160**. No stable structure is contradicted
at any site where it can be measured.

## 3. Numerical / metrological family

Counted-sign set as filed (Spec 091's record):
{M012, M059, M391}; full-corpus tokens 143 / 222 /
193, equal to the filed counts.

- **Check 1, bounded range (population T: 486
  artifacts bearing a counted sign): NOT SUPPORTED,
  stably.** The count distribution is {1: 418, 2: 64,
  3: 4}, maximum 3, variance 0.1427, share
  (count ≥ 3) 0.0082; both halves return the same
  direction (STABLE). Filed disclosure: the frozen
  null (within-artifact shuffle) leaves each
  artifact's counted-token total invariant, so the
  variance and share clauses compared the
  distribution to itself (null 5th percentiles equal
  the observed values exactly) and only the maximum
  clause (3 ≤ 5, met) was informative; the frozen
  rule requires variance strictly below the null's
  5th percentile, which equality does not meet, so
  the check is NOT SUPPORTED under its frozen rule.
  A corpus-level tally null (counted tokens
  redistributed across artifacts) is a different
  instrument; adopting it is a new registration's
  business, not this run's, and the bar was not
  moved to reach for it.
- **Check 2, positional restriction: NOT SUPPORTED,
  stably.** The counted signs' full-corpus dominant
  shares are M012 final 0.427, M059 medial 0.468,
  M391 medial 0.575 — none reaches ρ = 0.90, in
  either half or the full corpus.
- **Check 3, combination consistency (population C:
  68 combination contexts): NOT SUPPORTED, stably.**
  Counted tokens form one contiguous block in 0.382
  of combination contexts, against the null's 99th
  percentile of 0.618 (halves 0.258 / 0.462, same
  direction).
- **Filed census facts.** The NUMERAL_FORMULA
  population (14 seals) carries a counted sign on
  only 4 seals (1 token each); the tag does not mark
  counted-sign presence. Stroke-series runs of
  length ≥ 2 number exactly **4 in the whole corpus**
  (M059 ×3, M391 ×1, every run of length exactly 2):
  no stroke series beyond a pair exists to analyze.

The family files **no structure**: at the registered
checks, the counted contexts do not behave as a
constrained numeral system beyond tally noise — the
design queue's falsifier for this family is what the
record shows — and the negative is stable across
halves. This agrees with, and at the registered
standard sharpens, Spec 091's WEAKENED evidence on
the same signs. It establishes nothing about what
any counted sign means.

## 4. Verdict and gate filings

**Part 2 verdict (over the licensed families):
POSITIVE** — at least one STABLE structure is filed
to the gates (108 of them), under registration §3's
rule. The positional family is POSITIVE; the
numerical family returns no structure (a stable
negative, filed above). The two unlicensed families
(segmentation, recurrent partials) contribute nothing
to this verdict and remain closed as filed at
Stage 1.

Every STABLE structure is filed to Spec 091's anchor
comparison under its own registration, with a gate
filing reference (`records/stage-2-gate-filings.json`
carries the machine-readable set):

| Filing reference | Mark | ρ | Dominant | Per-site agreement |
|---|---|---|---|---|
| GF-109-091-001 | M001 | 0.95 | initial | 1/1 |
| GF-109-091-002 | M001 | 0.9 | initial | 1/1 |
| GF-109-091-003 | M002 | 0.95 | initial | 2/2 |
| GF-109-091-004 | M002 | 0.9 | initial | 2/2 |
| GF-109-091-005 | M003 | 0.95 | initial | 2/2 |
| GF-109-091-006 | M003 | 0.9 | initial | 2/2 |
| GF-109-091-007 | M004 | 0.95 | initial | 1/1 |
| GF-109-091-008 | M004 | 0.9 | initial | 1/1 |
| GF-109-091-009 | M005 | 0.95 | initial | 1/1 |
| GF-109-091-010 | M005 | 0.9 | initial | 1/1 |
| GF-109-091-011 | M008 | 0.95 | initial | 2/2 |
| GF-109-091-012 | M008 | 0.9 | initial | 2/2 |
| GF-109-091-013 | M009 | 0.95 | initial | 2/2 |
| GF-109-091-014 | M009 | 0.9 | initial | 2/2 |
| GF-109-091-015 | M010 | 0.95 | initial | 0/0 |
| GF-109-091-016 | M010 | 0.9 | initial | 0/0 |
| GF-109-091-017 | M011 | 0.95 | initial | 1/1 |
| GF-109-091-018 | M011 | 0.9 | initial | 1/1 |
| GF-109-091-019 | M013 | 0.95 | initial | 2/2 |
| GF-109-091-020 | M013 | 0.9 | initial | 2/2 |
| GF-109-091-021 | M014 | 0.95 | initial | 1/1 |
| GF-109-091-022 | M014 | 0.9 | initial | 1/1 |
| GF-109-091-023 | M015 | 0.95 | initial | 1/1 |
| GF-109-091-024 | M015 | 0.9 | initial | 1/1 |
| GF-109-091-025 | M016 | 0.95 | initial | 2/2 |
| GF-109-091-026 | M016 | 0.9 | initial | 2/2 |
| GF-109-091-027 | M017 | 0.95 | initial | 2/2 |
| GF-109-091-028 | M017 | 0.9 | initial | 2/2 |
| GF-109-091-029 | M019 | 0.95 | initial | 1/1 |
| GF-109-091-030 | M019 | 0.9 | initial | 1/1 |
| GF-109-091-031 | M020 | 0.95 | initial | 1/1 |
| GF-109-091-032 | M020 | 0.9 | initial | 1/1 |
| GF-109-091-033 | M021 | 0.95 | initial | 1/1 |
| GF-109-091-034 | M021 | 0.9 | initial | 1/1 |
| GF-109-091-035 | M022 | 0.95 | initial | 2/2 |
| GF-109-091-036 | M022 | 0.9 | initial | 2/2 |
| GF-109-091-037 | M023 | 0.95 | initial | 0/0 |
| GF-109-091-038 | M023 | 0.9 | initial | 0/0 |
| GF-109-091-039 | M024 | 0.95 | initial | 2/2 |
| GF-109-091-040 | M024 | 0.9 | initial | 2/2 |
| GF-109-091-041 | M025 | 0.95 | initial | 2/2 |
| GF-109-091-042 | M025 | 0.9 | initial | 2/2 |
| GF-109-091-043 | M026 | 0.95 | initial | 2/2 |
| GF-109-091-044 | M026 | 0.9 | initial | 2/2 |
| GF-109-091-045 | M027 | 0.95 | initial | 2/2 |
| GF-109-091-046 | M027 | 0.9 | initial | 2/2 |
| GF-109-091-047 | M030 | 0.95 | initial | 2/2 |
| GF-109-091-048 | M030 | 0.9 | initial | 2/2 |
| GF-109-091-049 | M031 | 0.95 | initial | 1/1 |
| GF-109-091-050 | M031 | 0.9 | initial | 1/1 |
| GF-109-091-051 | M033 | 0.95 | initial | 1/1 |
| GF-109-091-052 | M033 | 0.9 | initial | 1/1 |
| GF-109-091-053 | M034 | 0.95 | initial | 2/2 |
| GF-109-091-054 | M034 | 0.9 | initial | 2/2 |
| GF-109-091-055 | M035 | 0.95 | initial | 1/1 |
| GF-109-091-056 | M035 | 0.9 | initial | 1/1 |
| GF-109-091-057 | M037 | 0.95 | initial | 1/1 |
| GF-109-091-058 | M037 | 0.9 | initial | 1/1 |
| GF-109-091-059 | M038 | 0.95 | initial | 2/2 |
| GF-109-091-060 | M038 | 0.9 | initial | 2/2 |
| GF-109-091-061 | M039 | 0.95 | initial | 2/2 |
| GF-109-091-062 | M039 | 0.9 | initial | 2/2 |
| GF-109-091-063 | M041 | 0.95 | initial | 1/1 |
| GF-109-091-064 | M041 | 0.9 | initial | 1/1 |
| GF-109-091-065 | M044 | 0.95 | initial | 1/1 |
| GF-109-091-066 | M044 | 0.9 | initial | 1/1 |
| GF-109-091-067 | M045 | 0.95 | initial | 2/2 |
| GF-109-091-068 | M045 | 0.9 | initial | 2/2 |
| GF-109-091-069 | M046 | 0.95 | initial | 0/0 |
| GF-109-091-070 | M046 | 0.9 | initial | 0/0 |
| GF-109-091-071 | M052 | 0.95 | initial | 2/2 |
| GF-109-091-072 | M052 | 0.9 | initial | 2/2 |
| GF-109-091-073 | M053 | 0.95 | initial | 2/2 |
| GF-109-091-074 | M053 | 0.9 | initial | 2/2 |
| GF-109-091-075 | M056 | 0.95 | initial | 1/1 |
| GF-109-091-076 | M056 | 0.9 | initial | 1/1 |
| GF-109-091-077 | M058 | 0.95 | initial | 1/1 |
| GF-109-091-078 | M058 | 0.9 | initial | 1/1 |
| GF-109-091-079 | M060 | 0.95 | initial | 1/1 |
| GF-109-091-080 | M060 | 0.9 | initial | 1/1 |
| GF-109-091-081 | M061 | 0.95 | initial | 2/2 |
| GF-109-091-082 | M061 | 0.9 | initial | 2/2 |
| GF-109-091-083 | M062 | 0.95 | initial | 2/2 |
| GF-109-091-084 | M062 | 0.9 | initial | 2/2 |
| GF-109-091-085 | M063 | 0.95 | initial | 2/2 |
| GF-109-091-086 | M063 | 0.9 | initial | 2/2 |
| GF-109-091-087 | M066 | 0.95 | initial | 1/1 |
| GF-109-091-088 | M066 | 0.9 | initial | 1/1 |
| GF-109-091-089 | M070 | 0.95 | initial | 2/2 |
| GF-109-091-090 | M070 | 0.9 | initial | 2/2 |
| GF-109-091-091 | M071 | 0.95 | initial | 1/1 |
| GF-109-091-092 | M071 | 0.9 | initial | 1/1 |
| GF-109-091-093 | M073 | 0.95 | initial | 2/2 |
| GF-109-091-094 | M073 | 0.9 | initial | 2/2 |
| GF-109-091-095 | M075 | 0.95 | initial | 0/0 |
| GF-109-091-096 | M075 | 0.9 | initial | 0/0 |
| GF-109-091-097 | M077 | 0.95 | initial | 1/1 |
| GF-109-091-098 | M077 | 0.9 | initial | 1/1 |
| GF-109-091-099 | M078 | 0.95 | initial | 2/2 |
| GF-109-091-100 | M078 | 0.9 | initial | 2/2 |
| GF-109-091-101 | M079 | 0.95 | initial | 1/1 |
| GF-109-091-102 | M079 | 0.9 | initial | 1/1 |
| GF-109-091-103 | M080 | 0.95 | initial | 1/1 |
| GF-109-091-104 | M080 | 0.9 | initial | 1/1 |
| GF-109-091-105 | M220 | 0.95 | final | 3/3 |
| GF-109-091-106 | M220 | 0.9 | final | 3/3 |
| GF-109-091-107 | M249 | 0.9 | final | 4/4 |
| GF-109-091-108 | M305 | 0.9 | final | 4/4 |

A filing is a candidate for that gate; no gate was
run in this stage, and the structures' standing, if
any, is for the gate's own machinery on its own
registrations. The 2 UNSTABLE and 152 INDETERMINATE
(mark, ρ) calls are filed in the positional table
with their figures and carry no filing reference.

**AI disclosure:** executed by an AI agent (Muse, via Muse)
at the direction of Tristen Pierson, per constitution sec. VI.
