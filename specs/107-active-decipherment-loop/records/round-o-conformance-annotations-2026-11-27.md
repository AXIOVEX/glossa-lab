# Spec 107 — Round O conformance annotations (2026-11-27)

Dated annotations arising from Co-scientist Round O (adjudication
of record:
`specs/091-anchor-comparison-integrity/records/coscientist-sweep-adjudication-2026-11-27-round-o.md`).
The cycle-1 registration, execution scripts, raw outputs, outcome
records, and trace are preserved unedited; these annotations
qualify them going forward. No standing, verdict, or tally moves.

## 1. I-1 duplication conformance (unit O-I-1)

The cycle-1 registration (§2) specifies the generator's
duplication step so that "the achieved duplication rate matches
d within ±0.01 (the achieved rate is filed)", with target
d = 20/1670 = 0.011976048. The filed raw output
(`records/i1-raw-output.json`) gives, for every replication, the
generated artifact count A′ and the distinct-artifact count U;
the achieved rate is (A′ − U)/A′. At 1× (A′ = 1,670):

| Donor | Filed U range | Achieved d range | Median d |
|---|---|---|---|
| Meroitic | 970–1,057 | 0.367066–0.419162 | 0.393713 |
| Latin | 1,258–1,310 | 0.215569–0.246707 | 0.232934 |

The allowed 1× distinct-count interval under the tolerance is
1,634–1,666. No filed replication at any scale meets the
registered tolerance (120 of 120 outside it, computed from the
filed rows with each cell's own A′). The generator injects
roughly d × A′ copies into a sample drawn from naturally
repeated donor spans; adding copies does not bring the sample's
total duplication to d. Two-implementation scorer agreement does
not test this requirement, because both scorers receive the same
generated sample.

Consequences, exactly as far as they reach:

- I-1's mechanical verdict stands: the filed medians satisfy the
  registered rule's explicit neither-donor-measurable branch, so
  the outcome is INDETERMINATE on the filed figures. The
  nonconformance is a sample-generation defect, not a registered
  statistical NEGATIVE, and no standing changes (unit O-I-4,
  DO NOT APPLY, concurred at adjudication).
- The license wording is qualified: the predictor leg was
  calibrated on samples whose duplication profile is the donors'
  natural profile plus the injected copies, **not** at the
  registered Indus duplication profile. Forward citations of I-1
  carry this qualification, as they carry the Round N
  normalization qualification for IND-1.
- The trace's kill-criteria item 5 ("Integrity tripwire: none
  fired") is qualified by §4 of this record: a registered
  constraint failed in every replication, and criterion 5's
  treatment is referred to the owner (OD-O-1 in the Round O
  adjudication record). The trace's historical text stands.
- Any corrected simulation is registered prospectively; this run
  is not repaired invisibly and is not treated as a fresh Indus
  holdout.

## 2. Calibration license (unit O-I-2)

The cycle-1 registration (§1) describes I-1's outcomes as
discriminating "among all five Indus hypotheses at once,
including the non-linguistic one". The registered computation
takes the target's shape parameters only; it takes no proposed
Indus family, sign reading, or linguistic/non-linguistic target
model as input, and its statistic is a function of the observed
shape, the fixed donor streams, and the seed, identically in
every target-language world. I-1 is therefore **indirect method
calibration**: it can challenge an assumption about the method's
performance on the donors under the generated sampling regime
and inform which future tests are worth doing. It supplies, by
itself, no target-family or linguistic/non-linguistic update,
and the registration's ranking language is qualified accordingly
going forward. The donor-control measurements stand at that
narrower license; nothing is discarded.

## 3. M-1 description-level clarification (units O-I-3 and O-M-1)

The M-1 outcome record's description-level pooling flag states
that the pooled never-successor digit class {0, 5, 6, 8, 9} is
"absent as a class in funerary, where every digit has a successor
somewhere". The filed raw tables
(`records/m1-raw-output.json`, population S strata) show the five
marks occur only in the document stratum — 0: 7, 5: 12, 6: 10,
8: 5, 9: 7 occurrences, 41 in total, none with a successor — and
do not occur in funerary or any other stratum at all. The only
digit attested in funerary is 4, once, group-initial. An empty
never-successor list for a stratum therefore records absence of
the marks, not successor observations against them.

The explanation of record is corrected to: **the five pooled
never-successor digits are attested only in the document stratum,
where all retain that property; their behavior is unassessed in
the other strata because they are absent there. This is a
document-supported positional observation, not a witnessed
funerary failure and not a pooling artifact** (a zero pooled
outgoing count cannot conceal a positive stratum count under the
same partition). The outcome record's broader stratum-basis
citation guidance stands under this corrected explanation. No
count, conformance figure, or the M-1 POSITIVE verdict is
touched; Spec 105's filed pooled counts stand as filed.

## 4. Trace qualification

The cycle-1 trace's kill-criteria evaluation is qualified as
follows. Items 1–4 stand as evaluated (the null-yield minimum is
an advance disjunction and is met by the two decided verdicts,
M-1 POSITIVE and E-1 NOT SUPPORTED, alone). Item 5 is no longer
carried as an unqualified "none fired": the I-1 duplication
nonconformance (§1) and the E-1 conformance gaps (Round O units
O-E-1 and O-E-2, recorded in the Spec 101 package) are
registration-conformance matters of the kind criterion 5
reserves for recording and owner ruling. They are referred to
the owner as OD-O-1 and OD-O-2 in the Round O adjudication
record. This annotation records and qualifies; it does not rule,
and it does not rewrite the trace.

## 5. Completion crosswalk (unit O-M-2)

Spec 107's `spec.md` §6 and claim C107-5 (in `claims.md` and
`aee-claims.json`) name the cycle-1 completion records by their
prospective dates, `records/cycle-1-outcome-2026-11-26.md` and
`records/cycle-1-trace-2026-11-26.md`. No files of those names
exist. The completed records are:

- `records/cycle-1-outcome-2026-11-27.md`
- `records/cycle-1-trace-2026-11-27.md`

Pointers to the November 26 names resolve through this
crosswalk. The registration-era texts are preserved unedited;
the AEE assessment snapshot of 2026-11-26 is not rewritten.
