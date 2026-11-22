# Spec 099 — Adoption and Registration Record (2026-11-21)

**Adoption act.** The owner's commission of 2026-11-21
22:14 ET in the Glossa-Lab chat: build the inference log for
the Indus program — flag F-4's first item from the Red Team
Round 1 adjudication. The log gates the Q3 circularity unit
of the Co-scientist audit adjudication
(adjudicated-but-blocked since 2026-11-21 because no
inference log existed; the Round 1 execution's dependency
record, PR #645, states the same) and the M267 retest, whose
slot labels derive from the same candidate system.

**Number.** D-099-1: at the check of 2026-11-21, the highest
landed spec package on origin/main was 098
(`specs/098-identifiability-over-the-65`), no 099 directory
existed, and no branch or open pull request carried 099.
This package takes 099.

**What is registered where.**

- The spec package itself (this directory) is the study's
  registration of record: specification, eight AEE claims
  with falsifiers (claims.md; bundle form in aee-claims.json),
  plan, tasks, three implemented test cases, and the
  reference implementation (`tools/inference_log.py`).
- **Ledger intake and full registration: performed in this
  landing** (D-099-2), in the Spec 096/097/098 pattern. Claims
  C099-1..C099-8 were appended to the canonical ledger through
  tools/ledger/import_bundle.py (route 2), dated 2026-11-21:
  8 appended, 0 already canonical; the ledger grows from
  1,048 lines / 1,017 claims to 1,056 lines / 1,025 claims
  (canonical SHA-256 `4c956265ea64e6a7e3df458e88e4370d23feb81697b0cc27afc60499f399cbe7`,
  from `8a521d407a5e0895c024cf3eca92050b3967d65e63d0bd8836f56d8421c47875`).
  The program-map taxonomy gains one study entry,
  099-inference-log, domain Anchors & readings, subdomain
  Validation batteries for the SA-lineage anchors, Phases
  111–119 (studies 99 → 100). The settling chain was
  refreshed in the standing order: verify-canonicals 6/6 PASS
  over the grown build before any pin moved; both T405
  scenarios re-executed (runs settling-20261122T033634Z-974b13
  and settling-20261122T033700Z-bdc7da, same candidates, same
  286-sign full-frame scope, same registered scenario ids)
  with result blocks byte-equal to the superseded
  generations'; the Stage 4 dual-run comparison re-filed from
  the new pair (the diff against the previous filing is the
  ledger pin only); assignment sets re-materialized unchanged
  (run settling-20261122T033749Z-467348; incumbent 94,
  full-register 286, H003 out of frame); the canonical pin
  refreshed with the re-derivation recorded as
  re_derivations[15]; the superseded generation
  (settling-20261121T110155Z-e5597c,
  settling-20261121T110155Z-f28db5,
  settling-20261121T110209Z-bb2f40) departed the store in this
  landing, its departure accounted in the run index by
  departure acts (run-defs v2 §7.1) appended through
  `run_records.append_act`, carrying the superseding commit
  `ec0f50e1fda84757367925833a844087cc5e6fa9`, each record's
  final git blob and its SHA-256, after the run-index
  completion pass (`build_legacy_index.py`) entered the
  `re_derivations[15]` event and named the departed records
  post-spec skips (folded census 63 entries). The generated
  layers were regenerated in dependency order (matrix:
  1,025 claims, 1,548 cells — supports 1,541, opposes 7;
  program map: 100 studies; map-data: 1,669 elements, 1,548
  edges, settling runs carried 2, SHA-256
  `2ba1350569c67cb2c1347541655dcbb742afb15ba96f7b5049ce3c7b1180dd61`),
  and every census pin the intake moves was updated in the
  same pull request from the regenerated artifacts' actuals:
  claims 1017 → 1025, bundle population 994 → 1002, open
  class 1008 → 1016, draft status 993 → 1001, studies 99 →
  100, Anchors & readings domain 14 → 15, falsifier-present
  1008 → 1016, ledger lines 1048 → 1056, matrix cells and map
  edges 1540 → 1548, map element kinds 1661 → 1669, claims
  untouched by any run 1016 → 1024, the T405 run of record in
  the Spec 095 T403 dashboard tests re-pinned to
  settling-20261122T033634Z-974b13 (its quantities are the
  superseded generation's, byte-equal), and the dashboard and
  system-graph e2e censuses 1,017 → 1,025. The five affected
  backend suites were run on the final tree: **114 tests, all
  passed**. The ledger gate on the final tree, both modes,
  run standalone: **default 29 PASS / 0 FAIL / 1 NOT-RUN
  (RESULT: PASS)** and **--regen 32 PASS / 0 FAIL / 0 NOT-RUN
  (RESULT: PASS)**. (The single NOT-RUN in default mode is
  the V7 lossless-regeneration check, which runs under
  --regen.)
- No anchor, standing, or register entry is changed by this
  package; the ledger, taxonomy, census, and generated-layer
  changes above are the registration, and nothing else. The
  log itself is Stage 1; the audit is Stage 2; neither has
  run at adoption (D-099-3: the audit, when it runs, reports
  and does not move).

**Venue.** All work for this package, including the fixture
test execution, the intake, the settling re-executions, the
generators, and both gate modes, ran on tower-compute in the
fresh clone `~/glossa-work/s099-inference-log`. Nothing ran
in the coordination VM or on the mini-server.
