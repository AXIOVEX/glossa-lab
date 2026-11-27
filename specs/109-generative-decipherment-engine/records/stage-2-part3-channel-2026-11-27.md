# Spec 109 — Stage 2 Part 3 Channel Record (T202)

**Date:** 2026-11-27. **Leg:** Part 3, the context
channel, executed under registration
`records/registration-2026-11-27.md` §4 and the Stage
2 freeze (`records/stage-2-freeze-2026-11-27.md`).
**Licensing:** G3 PASSED its Stage 1 preflight
(`records/stage-1-close-2026-11-27.md` §4) and is
licensed for Stage 2 under its registered cap and
label. **Execution:** the same harness run as T201
(`records/stage-2-harness.py`, payload exit 0); terms
at `records/stage-2-context-terms.json`; the join (b)
table at `records/stage-2-joinb-table.json`; term
candidate records in the custody register (516
records across both legs). **Every context score
filed in this record carries no iconography
component** — the iconography sub-channel is GATED
on Spec 100 (spec.md §6), inactive, and no
iconography input was used. **No standing, verdict,
or tally moved; the channel's term is additive
evidence for other parts' scoring, not a margin.**

## 1. Join validations (both registered STOPs armed)

**Join (a), population site join — VALIDATED.** The
inner join of phase100 and phase114 on `cisi_id`
joins all 1,670 seals with **zero disagreements**
(site and sign list agree on every seal), and the
joined site census reproduces the filed site census
of Spec 091's record **exactly**: Mohenjo-daro 606,
Harappa 492, Lothal 124, Kalibangan 110, Dholavira
106, Chanhu-daro 78, Surkotada 61, Banawali 60,
Rakhigarhi 33.

**Join (b), Spec 093 census join — VALIDATED.** The
pinned join output (SHA-256 `7107f738…`) carries
exactly 179 pairs; the material census reproduces
exactly (Steatite 176, Clay 1, Faience 1, 1 pair
carrying the `-` sentinel); every pair's site is
Mohenjo-daro; every pair's `text_id` resolves in the
pinned canonical store. The census's filed limit
rides on every use below: all 179 pairs are
Mohenjo-daro, single stratum (C093-1, INDEPENDENT IN
PART), so the material and find-context families are
single-site channels and are not presented as more.

## 2. The terms, their nulls, and their caps

Per-sign context terms (registration §4's statistic)
were computed for three context families, each with
its own label-permutation null (within length
strata, B = 999) and its cap (the null's pooled 99th
percentile), and its frozen weight (join effective-N
share: site 1670/1849 = 0.9032; material and
find-context 179/1849 = 0.0968 each):

| Family | Universe | Scored signs (≥ 5 tokens) | Cap (null p99) | Null mean term | Largest filed terms |
|---|---|---|---|---|---|
| Site | M-scheme, 1,670 seals | 151 | 0.0769 | 0.0065 | M048 0.0823 (above cap); M125 0.0604; M065 0.0588 |
| Material | P-scheme, 179 pairs | 50 | 0.1422 | 0.0067 | P276 0.4506, P221 0.2231 (both above cap) |
| Find context (`area_section`) | P-scheme, 179 pairs | 50 | 0.6730 | 0.2194 | P144 0.6616; P202 0.5551 (none above cap) |

Terms above their family's cap are filed at their
measured values; the cap binds at scoring time, as
registered (a contribution is capped before
weighting). The material family's two large terms
are the expected small-cell effect of Spec 093's
filed counts (Clay 1, Faience 1, sentinel 1: a sign
attested on a rare-material seal draws a large log
ratio), and the find-context family's high null mean
(0.2194) is the noise level of 18 area sections over
179 seals. The two joins live in disjoint sign
universes (M-scheme and P-scheme; no tracked
crosswalk exists, Spec 091's record §6), so no
combined per-sign term across universes is defined
or filed; the terms stand per family with their
weights and caps.

## 3. Out-of-site validation — the registered prediction

Filed classes: Part 2's full-corpus positional
classes at ρ = 0.90 (131 restricted marks). Both
directions ran duplicate-aware at their floors
(53 measurable signs per direction, 33 of them
restricted, against floors of 20 and 5; validation
seals kept: 488 of 492 Harappa-side, 602 of 606
Mohenjo-daro-side):

| Direction | Δ (median term, unrestricted − restricted) |
|---|---|
| Mohenjo-daro → Harappa | 0.00955 |
| Harappa → Mohenjo-daro | 0.00821 |
| **Pooled** | **0.00888** |

The pooled Δ is positive, as predicted, but the
label-permutation null (site labels permuted within
length strata, B = 999, full pipeline recomputed per
draw) has mean 0.01592 and 99th percentile
**0.03371**: arbitrary partitions of the same seals
produce apparent class-travel at or above the real
site split's level. The observed pooled Δ sits
inside the null's central mass. **The term does not
discriminate the filed positional classes out-of-site
beyond its null.**

## 4. Channel verdict

**CHANNEL NULL** (registration §4's rule: joins
validated; validation discrimination not beyond the
null). The verdict is filed, and **the context term
is withdrawn from this study's scoring**: Parts 1
and 5 run without the term, as registration §4
provides for this outcome. The filed terms, caps,
and weights above remain on the record as channel
measurements (each labelled: no iconography
component), available to any future registration
that re-opens the channel under a new design; they
carry no scoring force in this study from this
record onward. This is a finding about context at
this corpus — site, material, and find context, at
these populations, do not carry positional-behaviour
signal beyond provenance that survives its own
null — and it is the channel's registered negative
outcome, not a machinery failure: both joins
validated exactly, the validation ran at its floors
in both directions, and its null was computed under
the registered permutation.

**AI disclosure:** executed by an AI agent (Muse, via Muse)
at the direction of Tristen Pierson, per constitution sec. VI.
