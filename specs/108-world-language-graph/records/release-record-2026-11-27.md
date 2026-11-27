# Spec 108 — Release Record, WLG-R1 (2026-11-27)

Release 1 of the World Language Graph, admitted by the
audit suite (all nine audits PASS; see
`records/audit-results-release-1-2026-11-27.md`). The
machine release record is `records/release-1.json` and
the release stream entry in `graph/releases.jsonl`.

**The three hashes, kept distinct (design §5.4):**

- Graph snapshot hash (SHA-256 over the canonical
  nodes, edges, assertions, and gaps streams, in ID
  order, schema wlg-1.0):
  `d2c8fddc060800646846d8bf27471241cd59af225c7c8515a5a7762b428439cd`
- Source manifest hash (SHA-256 over the sources
  stream):
  `5f3cbb38f7d7203c4a8e12af74e2550140793732c751bf8a185d41e0a5a17d08`
- Baseline pins, recorded untouched (the Spec 106
  templates' own pins; this release does not recompute
  or replace them): Indus
  `eb0e1d6218fadf8eed06c78eeb92979163ebb37b1206eb3d151c9c0d23b501e6`;
  Eteocypriot
  `fca1cc8a238631b0c6df8b2901daa5e84dc4cb2387dcdad560285c6e95beec4f`;
  Meroitic (version 2)
  `ecabd227f7e767a3a740ece3b355d8620db476b89ac482d7a8386b483a97f4f2`.

**Census:** 148 nodes (82 LANGUAGE, 52 SCRIPT,
14 CONTEXT), 129 edges, 365 assertions, 53 gap
entries, 7 sources. Edges by predicate:
GENETIC_DESCENT 27, WRITES 41, SCRIPT_DESCENT 5,
SCRIPT_BORROWING 4, CONTACT_BORROWING 3,
PROPOSED_RELATION 42, POPULATION_MOVEMENT 7,
AREAL_CONVERGENCE 0 (the layer is empty in this
release; see the population report). Coverage depths:
143 SKELETON, 5 DOSSIER, 0 STANDARD.

**Gap register headline state for the three priority
programs** (full register:
`records/gap-register-release-1-2026-11-27.md`):

- **Indus.** Script node S0 (SIGN_LIST_UNIT; its
  linguistic status disputed — the register's one
  LINGUISTIC_STATUS_DISPUTED entry), inferred language
  L0. Dominant blocker INFORMATION (with a PERMISSION
  component on the Spec 100 route). Candidates all in
  band C; the Dravidian line is first in the
  within-band work order on testability, with the
  register's caveat that investigation volume is not
  support and independent sourcing stands at 1 of 94.
- **Eteocypriot.** Language L1; its script carries no
  gap (the Cypriot syllabary is deciphered, S3).
  Dominant blocker INFORMATION (corpus size), with
  ACCESS and EXPERTISE components on the named
  outstanding inputs. Candidates all in band C.
- **Meroitic.** Script S3 (no script gap; the two
  scales kept unmerged), language L2. Dominant blocker
  POWER, with an ACCESS component now largely
  discharged. Candidates: Northern East Sudanic in
  band B, Afroasiatic in band C; the isolate-for-testing
  position is the null, not a candidate. Spec 102's
  gates G-1 and G-2 are carried unchanged.

**No standing moved.** This release amends no Spec 106
baseline, template, or pin; edits no program standing,
verdict, or tally; and adopts nothing into any
baseline. The baseline-links stream carries three
identity records only.
