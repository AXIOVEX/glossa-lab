# Spec 100 — Adoption and Registration (2026-11-22)

**Adoption act.** Adjudication unit I-21 of the
Co-scientist refresh adjudication (PR #673, landed
2026-11-22) proposed the deposit of the per-seal
iconography labels and the rerun of the 13 animal-motif
claims. The owner's OD-5 act (2026-11-22 11:36 ET,
Glossa-Lab chat) disposed it: **the rerun is authorised;
the per-seal iconography deposit is held** until William
Miller Sr's reply on the program's 2026-11-20 Holdat
permission letter (Gmail 1a1fb36478ee78e4), which the
hourly indus-reply-watch monitors under flag F-1. This
package is the registration that act ordered. The study
is registered and its pipeline is built and proven in
custody; it has not executed, and no claim in it carries
a result.

- **Number decision (D-100-1).** At the check of
  2026-11-22 the highest landed spec package on
  origin/main was 099 (`specs/099-inference-log/`), no
  100 directory existed, and no branch or open pull
  request carried 100. This package takes 100. (The
  branch was cut from 8c272479 and merged forward to the
  landing tip before push; the five intervening landings
  touched none of this package's files.)
- **Ledger intake and full registration: performed in
  this landing** (D-100-2), in the Spec 096/097/098/099
  pattern. Claims C100-1..C100-7 were appended to the
  canonical ledger through tools/ledger/import_bundle.py
  (route 2), dated 2026-11-22: 7 appended, 0 already
  canonical; the ledger grows from 1,056 lines / 1,025
  claims to 1,063 lines / 1,032 claims (canonical
  SHA-256 `94174d7cac64875caf3ac23d671304fbfa8261ecb8b89b710d63a1effb49aab6`,
  from `4c956265ea64e6a7e3df458e88e4370d23feb81697b0cc27afc60499f399cbe7`).
  The program-map taxonomy gains one study entry,
  100-motif-claims-rerun, domain Anchors & readings,
  subdomain Validation batteries for the SA-lineage
  anchors, Phases 111–119 (studies 100 → 101). The
  settling chain was refreshed in the standing order:
  verify-canonicals 6/6 PASS over the grown build before
  any pin moved; both T405 scenarios re-executed (runs
  settling-20261122T165435Z-5611f9 and
  settling-20261122T165435Z-c7bc9d, same candidates, same
  286-sign full-frame scope, same registered scenario
  ids) with result blocks byte-equal to the superseded
  generation's; the Stage 4 dual-run comparison re-filed
  from the new pair (the diff against the previous
  filing is the ledger pin only); assignment sets
  re-materialized unchanged (run
  settling-20261122T165448Z-548d35; incumbent 94,
  full-register 286, H003 out of frame); the canonical
  pin refreshed with the re-derivation recorded as
  re_derivations[16]; the superseded generation
  (settling-20261122T033634Z-974b13,
  settling-20261122T033700Z-bdc7da,
  settling-20261122T033749Z-467348) departed the store in
  this landing, its departure accounted in the run index
  by departure acts (run-defs v2 §7.1) appended through
  `run_records.append_act`, carrying the superseding
  commit `6dca5ef61a60086899953c9653185584eed379eb`, each
  record's final git blob and its SHA-256, after the
  run-index completion pass (`build_legacy_index.py`)
  entered the `re_derivations[16]` event and named the
  departed records post-spec skips (folded census 67
  entries). The generated layers were regenerated in
  dependency order (matrix: 1,032 claims, 1,555 cells —
  supports 1,548, opposes 7; program map: 101 studies;
  map-data: 1,676 elements, 1,555 edges, settling runs
  carried 2, SHA-256
  `d686b5e6529f8342f150c2aac81f51f5a159cb41579a8a3272849444b8ddd3eb`),
  and every census pin the intake moves was updated in
  the same pull request from the regenerated artifacts'
  actuals: claims 1025 → 1032, bundle population
  1002 → 1009, open class 1016 → 1023, draft status
  1001 → 1008, studies 100 → 101, Anchors & readings
  domain 15 → 16, falsifier-present 1016 → 1023, ledger
  lines 1056 → 1063, matrix cells and map edges
  1548 → 1555, map element kinds 1669 → 1676, claims
  untouched by any run 1024 → 1031, the T405 run of
  record in the Spec 095 T403 dashboard tests re-pinned
  to settling-20261122T165435Z-5611f9 (its quantities are
  the superseded generation's, byte-equal), and the
  dashboard and system-graph e2e censuses 1,025 → 1,032.
  The five affected backend suites were run on the final
  tree: **114 tests, all passed**. The ledger gate on
  the final tree, both modes, run standalone: **default
  29 PASS / 0 FAIL / 1 NOT-RUN (RESULT: PASS)** and
  **--regen 32 PASS / 0 FAIL / 0 NOT-RUN (RESULT:
  PASS)**. (The single NOT-RUN in default mode is the
  V7 lossless-regeneration check, which runs under
  --regen.)
- **Pipeline proof (D-100-3).** The six test cases and
  the end-to-end proof run executed in custody at
  registration; payload verdicts in
  `records/tc-execution-2026-11-22.md` (test suite exit
  0, 6 passed; proof run exit 0 over synthetic labels;
  record mode without a deposit exit 3, GATE CLOSED).
  The pipeline of record refuses record-mode execution
  while the gate is closed; the proof computed nothing
  from any real label.
- **The pinned corpus is not held on the venue.** The
  Holdat corpus build of record (SHA-256 `62d14d2b…`,
  the T303 build) is not present on tower-compute at
  registration — the same state the F-4 study package
  recorded on 2026-11-22. A CSV answering to the
  source's filename exists in an archived pytest scratch
  tree on the host; its SHA-256 is `253f7569…`, not the
  pin, so it is not the build of record and was not
  used, read for labels, or copied. The deposit act
  (Stage 1, when the gate opens) therefore begins by
  producing the pinned bytes in custody and verifying
  the pin; the extractor refuses any other bytes
  (TC-100-06). No Holdat-derived per-seal label is
  written anywhere in this package.
- **The gate, as registered (spec.md section 4).**
  Execution is gated on the per-seal iconography
  deposit. The deposit is HELD on the owner's order
  (OD-5 act, 2026-11-22 11:36 ET) until William Miller
  Sr's reply to the program's 2026-11-20 Holdat
  permission letter (flag F-1) is reported by the
  indus-reply-watch. On a reply granting the basis, the
  deposit is made as a tracked record and the rerun
  then executes under this registration. On a refusal,
  this study closes as GATE REFUSED and no execution on
  Holdat-derived labels occurs under it. While the gate
  is closed, the pipeline of record refuses record-mode
  execution (exit 3, GATE CLOSED) and no rerun result is
  computed for the record.
- No anchor, standing, or register entry is changed by
  this package; the ledger, taxonomy, census, and
  generated-layer changes above are the registration,
  and nothing else. Stages 1–2 have not run; Stage 3
  (consequences) is not part of this spec.

**Venue.** All work for this package, including the test
execution, the custody proof run, the intake, the
settling re-executions, the generators, and both gate
modes, ran on tower-compute in the fresh clone
`~/glossa-work/s100-motif-rerun-2026-11-22`. Nothing ran
in the coordination VM or on the mini-server.
