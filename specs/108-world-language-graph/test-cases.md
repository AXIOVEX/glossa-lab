# Spec 108 — Test Cases

Each test case implements one of the design's nine
mechanical audits (WLG-01..09, design §5.5) over the
populated graph release, and names the claim it
exercises. The audit suite is `tools/audit.py` in this
package; its output over release 1 is filed at
`records/audit-results-release-1-2026-11-27.md` and in
machine form in the release record. A release that
fails any test case does not ship; the failure is a
ledger entry, not a warning.

**TC-108-01 — Package and schema form (WLG-01;
C108-7).** Parse every canonical stream; check every
record carries its kind's required fields; resolve
every ID reference; check for duplicate IDs.
*Pass:* all streams parse; no missing required field;
no dangling reference; no duplicate ID.

**TC-108-02 — Label and source audit (WLG-02;
C108-6).** For every field assertion and edge: exactly
one evidence class; either a named, opened source with
a locator or the UNSOURCED flag; every UNSOURCED item
classed (H); no (F) item unsourced; every (H) item
carrying a removal condition; every item carrying a
source grade and a review state.
*Pass:* all conditions hold for all items.

**TC-108-03 — Shared schema conformance (WLG-03;
C108-1, C108-2).** Language and script kinds never
conflated; permitted endpoint kinds hold for every
predicate (including POPULATION_MOVEMENT terminating
only on population entities, and CONTACT_BORROWING
carrying a non-empty feature scope); status values
come only from the S0–S4 and L0–L5 scales, each on its
own kind (FAMILY_OR_CLADE nodes exempt from the status
requirement by their filed NOT_APPLICABLE assertion);
structural and historical layers disjoint in storage;
no node record carries an unqualified family field.
*Pass:* all conditions hold.

**TC-108-04 — Completeness and gap coverage (WLG-04;
C108-4).** Generate the gap set from the design's §4.2
thresholds over the release's status assessments and
compare it to `gaps.jsonl`: exactly one entry per
qualifying node; every entry's known and missing lists
populated; every candidate reference resolving to a
live placement assertion or hypothesis edge.
*Pass:* the generated set and the filed register are
identical, and all field conditions hold.

**TC-108-05 — Census and pin verification (WLG-05;
C108-7).** Recompute the release's counts by node kind,
subtype, status, evidence class, gap kind, and
predicate from the streams; recompute the graph
snapshot hash and the source manifest hash.
*Pass:* every recomputed value equals the release
record's stated value.

**TC-108-06 — No-standing-moves audit (WLG-06;
C108-5).** Over this study's landing diffs and the
release contents: no edit to any program record of a
standing, verdict, or tally; no baseline template or
pin altered (the three baseline pins read back equal
to their filed values); no hypothesis edge traversed
in any generated closure; no node field populated from
a neighbouring node, a population edge, or a rendering
product.
*Pass:* all conditions hold.

**TC-108-07 — Geometry audit (WLG-07; C108-3).** Every
coordinate in every filed view resolves to a typed
geometry assertion; attested and inferred geometries
are in separate layers; no node sits at a default or
fallback coordinate; every NO_GEOMETRY node appears in
the off-sphere index; every exported view state
reproduces its view byte-for-byte under the build's
view generator.
*Pass:* all conditions hold.

**TC-108-08 — Temporal audit (WLG-08; C108-3).** Every
interval in the release is well-formed in the
normalised year model (no year-zero error; start not
after end); no edge is rendered in a time slice its
temporal scope does not overlap; period labels resolve
to their named schemes.
*Pass:* all conditions hold.

**TC-108-09 — Competition preservation (WLG-09;
C108-2).** Where the release's sources contain
competing placements or relations for the same target,
all competing assertions are present as separate
records; no merge, majority, or consensus record exists
that its sources do not themselves state. The filed
control case is Meroitic: the Northern East Sudanic
and Afroasiatic proposals and the isolate-for-testing
null are all present, in their own forms, and none is
stored as the language node's family.
*Pass:* all conditions hold, including the control
case.
