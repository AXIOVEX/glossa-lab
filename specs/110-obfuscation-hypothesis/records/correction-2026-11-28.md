# Spec 110 — Correction record (2026-11-28): the entropy quantities actually computed

Filed under Round Q of the Co-scientist loop, ledger row
Q-I-1 (APPLY; adjudication
`specs/091-anchor-comparison-integrity/records/coscientist-sweep-adjudication-2026-11-28-round-q.md`
§1). This is a dated correction of interpretation. All frozen
outputs, historical mechanical labels, and filed scores are
preserved exactly as executed; nothing is rescored and no
verdict is substituted.

## The quantities

Let `H_all` denote entropy over all tokens. Let `H_X`, `H_Y`,
and `H_XY` be the entropies of the first marginal, second
marginal, and joint distribution of the same normalized
within-sequence bigram table. Then:

- Proper conditional entropy: `H(Y|X) = H_XY - H_X`.
- Proper bigram mutual information:
  `I(X;Y) = H_Y - H(Y|X)`.
- Spec 110's frozen A4 is `H_all - H(Y|X)`. It is **not**
  bigram mutual information in general: it equals mutual
  information only if `H_all = H_Y`, which need not hold in
  short, bounded sequences.
- Spec 110's frozen A3 and A4 are algebraically linked:
  `A4 = H_all(1 - A3)`. A3 and A4 are therefore **not
  independent findings**, and the structure family's two
  excursions are not two independent replications.
- Spec 111's filed conditional entropy (see the
  cross-reference note at
  `specs/111-deep-antiquity-evaluation/records/correction-2026-11-28.md`)
  computes `H_XY - H_all` instead of subtracting `H_X`; it
  is not the conditional entropy it is labelled as.

## Recomputed Indus values (from the filed aggregate tables, bits)

| Quantity | Value |
|---|---|
| H_all | 6.265061399 |
| H_X | 6.499966322 |
| H_Y | 5.491198311 |
| H_XY | 10.240560673 |
| Proper I(X;Y) | 1.750603959 |
| Spec 110's frozen A4 | 2.524467047 |
| Spec 111's filed value | 3.975499274 |

## Definition-level counterexample

For the two sequences `[a,b]`, `[a,c]`: X is constant and Y
is equiprobable over b/c, so the true mutual information is
0 and the true conditional entropy is 1 bit. The filed
functions return A4 = 0.5 and filed conditional entropy =
-0.5 respectively. A negative conditional entropy is
impossible for a genuine conditional entropy; the witness is
mathematical, not a proposed control study.

## Interpretation limits, of record

- The frozen A3/A4 comparisons remain mechanically
  reproducible statistics; their meanings are narrower than
  their labels.
- A4 is not to be described as mutual information in any
  adjudication, and A3/A4 are not to be counted as two
  independent findings.
- The obfuscation filing's structure result stands as an
  excursion from the specified synthetic model on the frozen
  statistics, under the adjudication framing recorded at
  Round Q (generator/observation-unit mismatch leading,
  genre and editorial sequence construction following,
  "length effects" only with the matched-multiset caveat).
  Neither implementation agreement nor correct downstream
  arithmetic cures the semantic mismatch corrected here.
- No standing, verdict, or tally moves on this record.
