# Spec 107 cycle 1 — I-1 run and outcome record — 2026-11-27

Test I-1 (Indus): scramble-simulation identifiability
calibration, executed as registered in
`records/cycle-1-registration-2026-11-26.md` §2 by
`records/i1-execution.py` on tower-compute. Raw
output: `records/i1-raw-output.json`. Two
independent implementations of the predictor
scoring agreed on every replication's advantage to
6 decimal places (TC-107-02); the run did not stop.

## Run facts

- Target shape (from the Spec 105 custody
  datasets, combined in Stage 1 order): 1,670
  artifacts, 7,002 tokens, inventory 390 marks,
  duplication rate d = 0.0120.
- Donor A (Meroitic): Kovetsky build
  `inscriptions.jsonl`, SHA-256 `1e91e3a0…`,
  inventory 32.
- Donor B (Latin): Caesar, *De Bello Gallico*
  Books I–IV, Project Gutenberg eBook #218.
  Pinned before any scoring: SHA-256
  `84ac8411841a4d8f…`, 169,899 bytes, held in
  custody at `glossa-custody/spec107/`. The
  canonical gutenberg.org route returned HTTP 503
  from the execution host; the file was acquired
  from the PGLAF Gutenberg mirror on the cycle's
  first acquisition attempt and identity-checked
  (an earlier wrong-file fetch from a stale mirror
  path was caught by the identity check and the
  bytes destroyed, before any scoring). Inventory
  after preparation: 22 letters, 20,547 groups.
- Grid: 2 donors × 3 scales (0.5×, 1×, 2×) × 20
  replications = 120 replications, each scored
  under RIGHT, WRONG, and SHUFFLE.

## Results (medians over replications)

Predictor advantage R1 (baseline − derived mean
per-token log-loss, G-IND construction):

| Donor | Scale | RIGHT | WRONG | SHUFFLE | R3 |
|---|---|---|---|---|---|
| Meroitic | 0.5× | 0.7888 | −0.0385 | 0.2511 | 1.0 |
| Meroitic | 1× | 0.7588 | −0.0427 | 0.2440 | 1.0 |
| Meroitic | 2× | 0.7750 | −0.0936 | 0.2505 | 1.0 |
| Latin | 0.5× | 0.4278 | −0.4311 | 0.0918 | 1.0 |
| Latin | 1× | 0.4308 | −0.5959 | 0.1038 | 1.0 |
| Latin | 2× | 0.4324 | −0.6788 | 0.1061 | 1.0 |

R3 (adjacency recovery) is 1.0 at every cell: at
these stream sizes the samples' attested pair sets
cover the donors' full-stream top-100 pairs. Filed
as description; it carries no verdict weight.

R2 (positional-restriction recovery): **not
measurable for either donor.** At the registered
ground-truth definition (≥20 full-stream
occurrences and ≥99% of occurrences in one
restriction class), the Meroitic full stream
contains 0 restricted marks (its strongest case,
the a-sign, stands at 725/737 = 98.4%
initial-or-sole — below the 99% bar) and the
Latin stream contains 0.

## Verdict (registered rule)

**I-1: INDETERMINATE.**

The predictor clause is positive for both donors
at 1× (median RIGHT 0.7588 and 0.4308, each ≥ 0.05
and ≥ 2 × max(WRONG, SHUFFLE) medians), so neither
donor is NEGATIVE; but the registered rule returns
INDETERMINATE when R2 is measurable for neither
donor while R1 is positive for both, and that is
the case here. The positional-restriction leg of
the calibration could not be run, because neither
donor's genuine structure contains a mark
restricted at the registered 99% level for the
recovery to find.

## What this does to the Indus line (design's per-outcome table)

An indeterminate I-1 leaves the Indus structural
statistics where they stood: usable, uncalibrated
on the positional leg. The predictor leg's
behaviour at this shape is now measured fact, not
assumption: at Indus size, a genuine bigram-plus-
initial structure produces a large advantage over
the unigram baseline (0.43–0.76 nats), a wrong
donor produces none, and a within-group shuffle
retains a smaller advantage (0.10–0.24) carried by
positional and unigram structure. IND-1's GOOD is
not re-scored by this test (and remains under the
Round N qualification, N-I-1). Cycle 2's lead for
the Indus line is I-2 as re-specified by this
outcome: a positional-recovery calibration whose
ground truth is defined at the restriction levels
real corpora actually show (the donors' own
98%-class restrictions), registered fresh before
it runs.
