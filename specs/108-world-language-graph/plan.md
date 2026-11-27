# Spec 108 — Plan

## Shape

The package mirrors Specs 104, 106, and 107: spec.md
states the study; claims.md and aee-claims.json carry
the seven claims in the program's claim form; the
design is filed in full at records/design-2026-11-26.md;
the history ledger opens live at registration. The
graph package itself lives inside this spec package:
canonical streams at `graph/`, implementation at
`tools/`, batch reports and audit results at `records/`.

## Stage 0 — Registration

- **T001.** Write the package: the build and population
  as the design specifies them (spec.md §§2–4), the
  seven claims with falsifiers, the test cases
  implementing WLG-01..09, and this plan.
- **T002.** Record the owner's commission act of
  2026-11-27 03:08 ET (all eight design decisions
  adopted as written) in the history ledger.
- **T003.** Intake the claims through the sanctioned
  importer; place the study in the taxonomy; run the
  settling chain in standing order (verify-canonicals
  before the pin moves; the T405 pair re-executed with
  byte-equal result blocks; assignment sets
  re-materialized; the canonical pin refreshed as a new
  re_derivations entry); regenerate the generated
  layers; update the census pins from the regenerated
  actuals; file the registration record with the
  executed figures; run TC-108-01 over the empty
  package streams as the build's first audit.

## Stage 1 — Build

- **T101.** Implement the schema and store
  (`tools/wlg_schema.py`, `tools/wlg_store.py`): record
  kinds, subtype and predicate vocabularies, endpoint
  rules, the no-unqualified-family-field rule, the
  provenance wrapper.
- **T102.** Implement the population builder
  (`tools/build.py`): batch assembly B0–B6 from the
  filed batch data, with timestamped progress
  indicators (items verified of items attempted, batch
  named).
- **T103.** Implement the gap-register generator
  (`tools/gapgen.py`) from the design's §4.2 rule and
  §4.3 schema.
- **T104.** Implement the projection and view generator
  (`tools/view.py`): typed geometry, view state,
  off-sphere index, time-slice query, reproduction from
  view state.
- **T105.** Implement the audit suite (`tools/audit.py`)
  for WLG-01..09 and run it over a test release.

## Stage 2 — Population

- **T201.** B0: source registry founded; Glottolog
  version in force pinned as actually opened and
  recorded; crosswalks opened.
- **T202.** B1 + B2: global skeleton and decipherment
  histories from the research report, behind the
  seven-step verification gate; batch report filed.
- **T203.** B3 + B4: historical edges, population
  movements confined to population entities, covariate
  blocks or their explicit empty state; batch report
  filed.
- **T204.** B5: gap census completion against the
  generated register; batch report filed.
- **T205.** B6: the three priority programs reconciled
  to the filed program record at DOSSIER depth; the
  filed record governs over the research report;
  batch report filed.

## Stage 3 — Release

- **T301.** Run WLG-01..09 over the populated graph;
  file the audit results verbatim.
- **T302.** Generate the gap register; file it in
  machine and readable form.
- **T303.** File release 1: the graph snapshot hash,
  the source manifest hash, and the three baseline pins
  read back untouched.
- **T304.** Land the build and population by pull
  request under the program's discipline; update
  PROGRAM-STATE.
