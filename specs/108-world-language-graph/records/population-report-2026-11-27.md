# Spec 108 — Population Report (Batches B0–B6, Release WLG-R1)

Filed 2026-11-27. Every batch passed the design's
seven-step verification gate (§6.7) in the form this
build can execute it: extraction with locators (every
assertion and edge carries its source and section
locator); a source check against the ingestion source
as filed; the type-discipline check (the audit suite's
WLG-03); a competition sweep (competing positions in
the source were entered as separate records — see the
Meroitic, Indus, and macro-family cases); duplicate
extraction for high-impact items in the form of the
cross-batch reconciliation below; the mechanical
audits WLG-01..09 (all PASS, filed separately); and
this report. Attempted / landed / quarantined are
stated per batch. Progress indicators were emitted
per batch by the builder (items verified of items
attempted, batch named); the build log's progress
lines are the record of that.

**Release census (recomputed by WLG-05):** 148 nodes
(82 LANGUAGE, 52 SCRIPT, 14 CONTEXT), 129 edges, 365
assertions, 53 gap entries, 7 sources. Coverage:
143 SKELETON, 5 DOSSIER (the three priority programs'
script and language nodes), 0 STANDARD — no node is
claimed at STANDARD in this release, because the
batches populated identity, status, principal edges,
and placement assertions at skeleton depth outside the
priority dossiers, and depth is a property of our
work, labelled as such. Raising census nodes to
STANDARD is future population work, not a claim made
here.

## B0 — Authorities and crosswalks

Landed: 7 source records, 3 crosswalk assertions.
The classification authority in force is pinned as
**Glottolog 4.8 as reported in the research report**
(SRC-GLOTTOLOG-4.8): the report's Part B.1 states the
4.8 census (421 spoken-language families + isolates)
from secondary summaries, and the primary Glottolog
data tables were **not opened directly in this
build**. That limit is recorded on the source record
itself and here: no assertion in this release rests
on Glottolog alone beyond what the report states, and
no catalogue code is asserted for any node. A direct
Glottolog table extraction is a future refresh batch
under design §6.6. Custody sources (Holdat, Otten,
Rilly & de Voogt Appendix) are registered with their
terms; none was opened for content, and no restricted
byte is stored anywhere in this package.

## B1 + B2 — Skeleton and decipherment histories

Landed: 82 nodes (52 LANGUAGE incl. 27 family/clade
nodes, 30 SCRIPT), 135 assertions, 75 edges. Sources:
research report Parts A and B.1–B.2. Decipherment
histories are carried as mechanism-and-verification
assertions for every deciphered or partly deciphered
script the report covers, including the failed-attempt
record (e.g. Carian's century of Greek letter values;
the 1857 Royal Asiatic Society sealed-translation
test as cuneiform's verification standard). Statuses:
S3 ×23 and S4 ×3 among all batches' scripts; family
nodes carry no status (the filed NOT_APPLICABLE
assertion pattern, 27 records).

## B3 — Family, contact, and script-history edges

Landed within B1/B2 and the census batch's edge work:
GENETIC_DESCENT ×27 (only where the source states a
consensus grouping), SCRIPT_DESCENT ×5,
SCRIPT_BORROWING ×4, CONTACT_BORROWING ×3 (each with
its mandatory feature scope), PROPOSED_RELATION ×42
across all batches (the macro-family proposals of
Part B.3 — Nostratic, Altaic/Transeurasian, Austric,
Indo-Pacific, Amerind, Dene-Yeniseian, Elamo-Dravidian,
Alarodian — entered as hypothesis edges with their
proponents and critics named in the basis, never as
descent). **No AREAL_CONVERGENCE edge is populated in
release 1:** no item in the ingestion source was
extracted as a named areal-convergence assertion with
the feature set the predicate requires; the predicate
exists in the schema and the layer is empty rather
than padded. Three family nodes no other batch
created (Kartvelian, Mixe-Zoquean, Northwest
Caucasian) were landed in this batch so every
cross-batch reference resolves.

## B4 — Movement and covariates

Landed: 14 CONTEXT population entities, 7
POPULATION_MOVEMENT edges, 4 restriction assertions.
Every movement edge terminates on population entities
only, carries its ancient-DNA or historical basis, and
states on its face that it asserts nothing about any
language. The genes-are-not-language restriction is
filed as assertions on the standing warning cases
(Vanuatu language continuity, Hungarian elite
dominance, the IVC core-DNA absence). Covariate
blocks: outside the priority dossiers, nodes carry the
explicit NO_ASSERTION_POPULATED state, as the design
requires — silence is not presented as a negative
finding. Covariate population beyond that state is
future batch work and is not claimed here.

## B5 — Gap census

Landed: 58 nodes (36 LANGUAGE, 22 SCRIPT), 199
assertions, 47 edges, from research report Parts C
and D (entries 1–32, with D.32's sub-items broken out
individually). Every census entry carries a
corpus_description (ranges kept as ranges), a
known_summary, and an explicit not_known. The gap
register generated from the release carries 53
entries: 28 LANGUAGE_NOT_UNDERSTOOD, 24
SCRIPT_UNDECIPHERED, 1 LINGUISTIC_STATUS_DISPUTED
(the Indus script). Dongba and Quipu are represented
with their system-function assertions (mnemonic /
semasiographic systems, not undeciphered
glottography), as the report directs.

## B6 — Priority reconciliation

Landed: 20 assertions and 3 baseline-links identity
records, all sourced to the filed program record
(SRC-PROGRAM-RECORD, P1), which governs over the
research report wherever they differ. The differences
that matter, stated plainly: the Indus corpus of
record is 1,670 artifacts (not the report's general
4,000–5,000 inscribed objects, a different counting
convention); the Meroitic corpus of record is the
Kovetsky build's 396 inscriptions / 368 distinct texts
(not the report's REM-based general figures); the
Eteocypriot position includes the Spec 101 outcome as
executed in Spec 107 cycle 1 (C101-1 NOT SUPPORTED),
which postdates the report. Cross-batch status
adjudications at reconciliation: Hurrian L3 (the
report's "largely understood" read against the §1.7
scale), Urartian L4 ("well understood"), Sumerian L4
retained conservatively (L5 was considered and not
taken), Numidian's label in the shorter filed form.
The three baseline pins are recorded in the release
record exactly as filed in Spec 106; none was
recomputed, amended, or adopted from.

## Quarantine and non-population

- **Quarantined: none.** The builder's duplicate-ID
  quarantine fired zero times after the reconciliation
  adjudications above were applied to the batch data
  before assembly; the build report
  (`records/build-report.json`) records zero
  quarantined records and zero dangling references.
- **Not populated, by design or by evidence:**
  geometry coordinates (every node is NO_GEOMETRY in
  release 1 — no geometry assertion with coordinates
  has been extracted and verified, so the off-sphere
  index carries all 148 nodes; placing nodes on
  report-level geography without typed, sourced
  geometry assertions would violate design §3.2);
  AREAL_CONVERGENCE edges (above); STANDARD coverage
  depth (above); direct Glottolog table data (B0);
  any content from the three custody sources (B0).
