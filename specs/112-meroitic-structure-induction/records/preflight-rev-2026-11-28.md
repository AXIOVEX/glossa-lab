# Spec 112 — Revision Preflight Verdict (2026-11-28)

**Verdict: FAILED. The revision closes as filed.**

The revision preflight ran once, under the freeze at commit
`3a2b5807`, against the floors, ground-truth sets, and scoring
rules carried unchanged from the first execution. All three legs
failed. The corpus induction therefore does not run, and no
further design is run under this registration (revision kill
criterion, claims C112-10). Figures below are from
`records/preflight-rev-output.json` as recomputed independently
under TC-112-11 (`records/verify-rev-output.json`: 20 of 20 checks
agree; verifier payload exit code 0).

## Precondition: fixture proofs (TC-112-10) — met in full

`records/fixture-proofs-rev.json`, all three proofs passed:
(a) zero one-segment candidates in any top-5 list over both
fixtures (5,000 forms); (b) on the easy fixture the planted
segmentation outscored the all-single-character fallback on 2,193
of 2,193 planted forms (bar: at least 95%); (c) median boundary F1
was 1.0 on the easy fixture (2,193 ground-truth forms) and 1.0 on
the hard fixture (2,485 ground-truth forms). The whole-form
degeneracy of the first execution is removed mechanically, and
that removal is proven on fixtures before the preflight, as
registered. The failure below is therefore not the filed
degeneracy recurring: the revised segmenter does segment, on the
corpus as on the fixtures.

## P-1 segmentation — FAILED

Median boundary F1 over the 1,719 ground-truth forms: **0**
(floor 0.80). Distribution of per-form F1: 1,342 forms at 0; 308
forms at 1 (exact); 60 at 2/3; 7 at 1/2; 2 at 2/5. The segmenter
returned a segmentation for every form (predicted boundary counts:
one boundary on 1,393 forms, two on 289, three on 31, four on 5,
six on 1), but on most forms its chosen boundaries do not include
the pinned gold boundary, and most ground-truth forms carry
exactly one boundary, so a miss scores 0. Removing the degeneracy
was necessary and is proven; it was not sufficient. The corrected
positional-class unigram objective, at the registered inventory
floor and boundary penalty, does not recover the gold suffix
onsets on the real corpus, although it recovers them on both
fixtures. No figure here is a claim about Meroitic morphology;
it is a measurement of this objective on this corpus.

## P-2 slots — FAILED on the match leg; the name-slot sub-leg held

Sequence match: **73 of 95 labeled texts (0.768)** against the
floor of 90%. The name-slot sub-leg held again: the presentation
slot's filler entropy, 9.237 bits, is strictly the greatest of the
six slots (filiation2 6.839, filiation1 6.705, closing 6.684,
invocation 3.362, offering 3.293). This is a large improvement
over the first execution's 1 of 95 under the positional-band
model, and it is still below the floor.

The induced grammar, for the record: invocation frame (woSi,
Soreyi), pair coverage 0.481 of the 210 funerary texts; offering
anchor ato with the 9-type family {ato, atoS, atoXe, atoXme, atom,
atomX, atomXe, atomelx, atotek}; filiation markers tedx and teri,
with tedx first in 73 of the 96 texts carrying both paradigms
(majority 0.760); the induced slot order equals the template
order. Slot yield 6 of 6 on the real texts, 2 of 6 under the token
shuffle.

Mismatch anatomy (from the filed per-text records): 22 mismatches
— 14 with an extra induced slot only, 7 with a missing slot only,
1 with both. Every extra-only case is an extra filiation1: the
paradigm rule assigns filiation1 to any token containing the tedx
marker anywhere in the text, while the label construction (carried
unchanged) only counts filiation material after the invocation
span. The dominant residual is that asymmetry, together with 3
missing filiation1, 3 missing filiation2, 1 missing presentation,
and 1 missing closing.

## P-3 partials — FAILED on precision and on both shuffle legs

Segmenter-based proposals at the frozen threshold: tau_st = 10
distinct residuals (the maximum support attained by any final
segment under the segmenter over the character-shuffled null
corpus). Proposals: 14 — eb, eqowi, ke, lX, leb, li, lowi, owi,
qowi, te, to, wi, ye, yeqowi. Gold hits: 5 (leb, li, lowi, te,
wi). **Precision 5/14 = 0.357** (floor 0.80); recall against the
16 length-at-least-2 gold strings 5/16, filed for transparency.
Precision improved over the first execution (4 of 36) and the
proposal set shrank by design, but stacked complexes (eqowi,
yeqowi, qowi, owi) still pass the recurrence threshold.

Shuffle legs: the character-shuffle proposal ratio is 3/14 =
0.214, above the 0.20 cap; the carried slot-yield ratio is 2/6 =
1/3, also above the cap. P-3 therefore fails on all three of its
conditions under the conjunction construction stated on the
freeze record's face.

## Verification (TC-112-11) and a disclosed verifier correction

The independent verifier agreed with the filed output on 20 of 20
checks (rational figures exact; entropies to 1e-9 with the same
argmax). Its first run agreed on 19 of 20: its recomputation of
the P-3 gold union applied an attestation filter the registered
construction does not contain, yielding 20 strings against the
construction of record's 24 (the first execution's construction,
carried unchanged: the gold morphology's filed corpus_form plus
corpus_variants, with the E-to-o fold). Precision agreed at 5/14
under both unions, so the preflight output was never affected.
The verifier was corrected (the filter removed, the correction
noted in its docstring; corrected SHA-256
`d5b252878d842c4d5bfe22af51aedf2e6a839ba99a87bc4b9c652a3abb7339f1`,
against `cdb9b45e6ec0354a2b66375e55b424554530130dda6bf2e0a7f25d1d29e2b661`
at freeze) and re-run to 20 of 20. The frozen harness was not
touched.

## Disposition

The revision closes as filed. The corpus induction does not run;
the harness's induce subcommand refuses without a filed full-pass
verdict, and this record is that refusal's basis. No candidate
segmentations, partials, or slot assignments from this study are
licensed as findings. The filed outputs (fixture proofs,
preflight output, verification output) stand as the study's
record: two successive search designs have now failed the same
frozen floors on this corpus, which is a finding about the search
designs and the information in the corpus as pinned, and is filed
as such.
