# Spec 100 — Plan

## Stage 0 — Registration (T001–T005)

The package (spec.md, claims.md, aee-claims.json, plan.md,
tasks.md, test-cases.md, tools/, tests/, records/) lands by
pull request against the next free spec number (D-100-1),
with the design frozen in
`records/preregistration-2026-11-22.md`. The pipeline of
record (`tools/motif_rerun.py`, `tools/deposit_extract.py`)
is committed with the package and proven at registration:
the six test cases run on tower-compute against synthetic
fixtures and the tracked marginals, and an end-to-end proof
run (proof mode, synthetic labels) executes the full join
and computation path in custody; payload verdicts are
recorded in `records/tc-execution-2026-11-22.md`. The
claims bundle (`aee-claims.json`, C100-1..C100-7) is
intaken into the canonical ledger through the bundle-import
route, the taxonomy entry is added, the settling chain is
refreshed in the standing order, the generated layers are
regenerated, and every census pin the intake moves is
updated in the same pull request, as Specs 096/097/098/099
performed the same registration.

Gate: the pull request merges only on genuine per-job CI
green (all ten jobs read per job; a wrapper's success is
not the payload's).

**Stage 0 registers the study and proves its machinery. It
computes no claim's result and deposits nothing.**

## Stage 1 — The deposit (T101–T102) — GATED

Opens only on the gate event of spec section 4 (Miller's
reply granting the basis, reported by the indus-reply-watch
under flag F-1). On tower-compute, in custody: produce the
pinned Holdat corpus bytes and verify the full SHA-256
against the pin of record; run `tools/deposit_extract.py`;
land the deposit CSV with its deposit record (provenance,
permission basis, coverage, join-defect check) by pull
request under the program's CI discipline. Claims:
C100-1, C100-5, C100-6.

Gate: the deposit record states the verified pin and the
coverage on its face; a pin that does not verify stops the
stage and is recorded, not worked around.

## Stage 2 — The rerun (T201–T202) — GATED on Stage 1

On tower-compute, in a fresh clone: run the pipeline of
record in record mode against the landed deposit; land the
outcome record (full 2x2 tables for all 13 claims, lifts,
odds ratios, verdicts under the frozen vocabulary, both
paths' exact agreement stated, the labeled-population
denominator on its face, M063's filed figures carried
beside its recomputed row) by pull request. The run's own
exit code is its payload verdict. Claims: C100-2, C100-3,
C100-5.

Gate: a path disagreement or a deposit defect is the
outcome and is recorded as such; no table is repaired by
hand.

## Stage 3 — Consequences (no tasks in this spec)

Any adjudication the outcome informs (a reading's class, a
public wording) is a separate act under the program's
standing discipline, citing the Stage 2 outcome record.
Claim: C100-4.

## Closure without execution

On a refusal reply, the study closes as GATE REFUSED by a
closure record under this spec, and Stages 1–2 never run
(C100-6). On continued silence the gate simply stays
closed; the registration stands as the program's readiness
of record.
