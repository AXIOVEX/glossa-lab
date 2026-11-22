# Spec 099 — Test-Case Execution Record (2026-11-21)

Executed on **tower-compute** in the fresh clone
`~/glossa-work/s099-inference-log`, on synthetic fixtures
only. No real reading's basis was scored and no audit was run
over the real log; this record covers the package's test
cases and bundle checks at adoption, and is not Stage 1 or
Stage 2 execution.

## TC-099-01, TC-099-02, TC-099-03 — payload verdict

Command (the glossa-ci venv interpreter; the host's system
python carries neither pytest nor the jsonschema the ledger
machinery needs):

```
~/glossa-work/venvs/glossa-ci/bin/python -m pytest \
  specs/099-inference-log/tests/test_inference_log.py -q
```

Payload verdict (the test process's own record): **15 tests
ran, all passed; process exit code 0.** TC-099-01 contributes
9 tests (the fixture validates clean; duplicate sign,
out-of-vocabulary class, kind/type mismatch, invented span,
(b) item without a reason, (b) item with neither target nor
target note, unstated target, and full-mode undercount each
rejected). TC-099-02 contributes 4 tests (the fixture checks
complete; a deleted item, an uncovered filed element, and a
dropped filed row each detected). TC-099-03 contributes 2
tests (the independent in-test implementation of spec
section 4 reproduces the reference audit exactly, components
by pairwise reachability against the reference's Tarjan; and
the planted outcomes hold: E unchanged and weakened, I on a
(b) item alone would change to U, I with an (a) item and an
unnamed slot unchanged and weakened with the slot as an open
end, ambiguous-only I divergent between the treatments, U
unchanged and unweakened, R unchanged, the two-node cycle
found, the census counted exactly).

## Bundle consistency check — payload verdict

`aee-claims.json` parses; its claim ids are C099-1..C099-8 in
order, identical to claims.md's claim ids in order; every
claim in both files carries a falsifier and a
does-not-establish line. The pinned AEE assessor
(`~/glossa-work/venvs/glossa-ci/bin/aee`) reports:

- `aee validate`: **valid: 8 claim(s)**, exit 0.
- `aee assess --no-ledger`: outcome **iterate**, exit 1 —
  the expected draft-stage reading for a bundle on asserted
  sources (the same outcome the Spec 097 and Spec 098 bundles
  received at adoption); the full assessment is filed at
  `records/adoption-aee-assessment.json`.

## What this does not establish

Fixture passage proves the schema, the completeness checker,
and the audit rules behave as written on planted cases. It
does not prove the log can be built completely over the real
filed bases, or what the audit will find over them; that is
exactly what Stages 1 and 2 exist to execute, and the claims'
falsifiers are written against those possibilities.
