# Spec 093 Stage 4 — T401 site pass freeze v1

**Frozen 2026-11-27, before any computation under it.**
This record states the population, the quantities, the
split, the controls, the floors, and the bar of the site
pass, and the rule that maps its outcomes to spec.md
§5's vocabulary. Nothing in §§1–8 may move after this
record is committed; a change is a superseding freeze
that voids every run under this one (C093-5's pattern,
applied to freezes by C093-8).

## 1. Pins

- Snapshot: `glossa-corpus/indus/exports/indus_research.jsonl`,
  SHA-256 `08fc96c8dbc22a37effb65e789b22b144f4baf22be1da55dc3d84db5dc44505e`.
- Populations and counts of record:
  `records/t201-counts-2026-11-19.json` and the T201
  definition (`records/t201-channel-definition-2026-11-19.md`).
- Premise: C093-1's standing as finally recorded by
  Stage 2 — **INDEPENDENT IN PART for site and find
  context** (site NOT RECOVERED under freeze v1 with
  valid controls; `records/stage2-record-2026-11-19.md`
  §4 and `records/stage2-findcontext-successor-record-v3-2026-11-20.md`
  §5). Site is a surviving field; this pass may cite it
  as channel data at exactly that strength (C093-7).
- Comparanda: this pass is a within-record-system
  conditioning, not a cross-cultural comparison; it
  cites no comparanda-register entry (C093-4 checked on
  the face of the stage record).

## 2. Population and floors

P-site: the snapshot's sequence-bearing records carrying
a non-empty `site_name` — 966 records, all
indusscript-m77 (Mohenjo-daro 839, Harappa 110,
Chanhu-Daro 7, Sutkagen-Dor 6, Lothal 3, Kalibangan 1).

**Site floor: 50 records.** Sites at or above the floor
form the adjudged set: Mohenjo-daro (839) and Harappa
(110), adjudged total 949. The four sites below the
floor (17 records) are excluded and named here, as
C093-8 requires the forcing counts on the face of the
record that stops for them: no conditioning statement
under this freeze covers Chanhu-Daro, Sutkagen-Dor,
Lothal, or Kalibangan, and no held-out arm is drawn from
them — the inventory's standing case (§5 of spec.md)
applies to them exactly as filed.

If the extraction from the pinned snapshot does not
reproduce these counts exactly, the administration
refuses (absence record) and the pass takes no outcome
from a mismatched population.

## 3. The quantities

For each adjudged record, its sequence is
`canonical_grapheme_ids` as recorded.

- **Q1 — inscription length.** The length of the
  sequence. Statistic: the two-sample
  Kolmogorov–Smirnov distance between the Mohenjo-daro
  and Harappa length distributions of the arm under
  adjudication.
- **Q2 — sign choice.** The unigram distribution over
  grapheme ids (pooled token counts per site).
  Statistic: the total variation distance between the
  two sites' distributions.

## 4. The split (held-out replication arm)

Within each adjudged site separately: the site's records
are ordered by `glossa_id` and shuffled with
`random.Random(20261127)`; the first 70% (floor) form
the discovery arm, the remainder the held-out arm.
Expected arm sizes (the tool verifies): Mohenjo-daro
587 discovery / 252 held-out; Harappa 77 discovery / 33
held-out.

## 5. The controls

- **Permutation batteries.** For each arm and each
  quantity: 2,000 permutations of the site labels over
  the arm's pooled records (discovery battery seed
  20261128; held-out battery seed 20261129), the
  statistic recomputed per permutation. Percentiles are
  read at fixed indices of the sorted battery: the 99th
  percentile is index 1979 of 2,000; the 95th is index
  1899 (the freeze v3 convention of Stage 2).
- **Pseudo-site negative control.** Within the
  Mohenjo-daro discovery records alone: 200 seeded draws
  (seed 20261130), each drawing a Harappa-sized subset
  (77 records) as a pseudo-site against the remainder,
  both statistics computed. The control behaves iff the
  95th percentile of each pseudo-site statistic falls
  below the discovery battery's 99th-percentile value
  for that quantity — the procedure must not manufacture
  site-scale differences inside one site. If the control
  misbehaves for a quantity, that quantity takes NOT YET
  with the machinery obstruction named (C093-6).

## 6. The bar

A quantity is **ACCEPTED** iff all of the following hold:

1. its discovery statistic strictly exceeds the
   discovery battery's 99th-percentile value;
2. its held-out statistic strictly exceeds the held-out
   battery's 95th-percentile value;
3. for Q1, the direction agrees across arms: the sign of
   (mean length at Mohenjo-daro − mean length at
   Harappa) is the same in both arms (Q2's statistic is
   unsigned; no direction clause applies);
4. the pseudo-site control behaves for that quantity
   (§5).

The pass is **ACCEPTED** iff both quantities are
ACCEPTED. Otherwise the pass is **NOT YET**, with the
per-quantity table on the face of its outcome record.
No re-administration under this freeze repairs a NOT
YET (C093-8); a successor attempt is a new freeze.

## 7. Runs, audit, adjudication

The administration and its batteries are Spec 089 runs
on the study surface (run-defs v2), minted by
`tools/spec093/run_stage4_site.py` into this spec's
records store, with this freeze and the §1 pins in every
run key. An independent auditor
(`tools/spec093/audit_stage4_site.py`), which does not
import the runner, recomputes both executions from the
pinned inputs and compares result blocks; the mechanical
adjudication (`tools/spec093/check_stage4_site.py`) is
gated on the audit's AGREE verdict.

## 8. Statement strength

An accepted statement under this pass is a fact about
the joint distribution of the two projections over the
named population, stated at channel strength with
C093-1's standing for site cited as premise (C093-7).
It asserts no cause, no function, and no reading, and
none may be read into it.

*This does not establish:* why any accepted regularity
holds — the pass states a joint-distribution fact at
channel strength (C093-7), and no cause, function, or
reading may be read into it. (T401's line, carried
verbatim.)
