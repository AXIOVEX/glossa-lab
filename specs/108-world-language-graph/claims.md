# Spec 108 — Claims

Seven claims, C108-1..C108-7, each with its falsifier
and its does-not-establish line, in the program's claim
form. The claims are intaken at registration through
the sanctioned importer (plan.md, Stage 0); intake sets
no standing, and no claim in this package carries a
result beyond what its test cases check.

**C108-1 — The graph's node schema keeps languages and
scripts distinct, and no node carries a placement as a
fact.** Language and script nodes are different record
kinds joined only by time-scoped WRITES relations;
every node carries exactly one subtype from the
design's lists; family placement exists only as
placement assertions and PROPOSED_RELATION edges; the
node schema has no unqualified family field.

*Falsifier:* any node record in a released stream that
carries a family value outside a placement assertion;
any language/script kind conflation; any script status
value appearing as a language status or the reverse
(WLG-03).

*Does not establish:* that any placement assertion in
the graph is correct — only that placements are
represented in the one permitted form.

**C108-2 — The edge layer keeps the seven historical
predicates mechanically distinct and preserves
competition.** Every historical edge carries its
predicate, evidence class, proponent, basis, scope, and
a concrete falsifier or narrowing condition; competing
edges coexist as separate records; no merge, majority,
or consensus record exists that its sources do not
themselves state; transitive closure is computed only
within admitted GENETIC_DESCENT and never crosses
PROPOSED_RELATION, contact, areal, population, script,
or WRITES relations; no language relationship is
derived from a script relationship, a population
movement, or a rendering product.

*Falsifier:* a released edge missing any required
field; a CONTACT_BORROWING edge with an empty feature
scope; a POPULATION_MOVEMENT edge terminating on a
language node; a consensus or merged record not stated
by a source (WLG-03, WLG-09).

*Does not establish:* that any edge's asserted
relationship is true — only that the layer represents
each assertion in its own name.

**C108-3 — Geometry is typed before coordinates, and
the projection never implies what the assertions do
not say.** Every rendered coordinate resolves to a
typed geometry assertion; attested and inferred
geometries are stored, rendered, and exported in
separate layers; NO_GEOMETRY nodes appear in the
off-sphere index and never at a default coordinate;
time is an interval query with no interpolation
between slices; the eight never-imply rules of the
design's §3.8 hold for every view this build files.

*Falsifier:* a coordinate in a filed view that resolves
to no geometry assertion; an inferred geometry rendered
in an attested form; a node placed at a fallback
coordinate; an exported view whose state does not
reproduce it (WLG-07, WLG-08).

*Does not establish:* any geographic, homeland, or
contact claim — views are renderings over a release,
not evidence.

**C108-4 — The gap register is complete by
construction.** Every script node assessed S0, S1, or
S2, every language node assessed L0, L1, or L2, every
L3 language with PLACEMENT_UNRESOLVED, every
inferred-unknown node, and every script whose linguistic
status is disputed carries exactly one gap entry, with
known and missing lists populated, blockers typed,
candidates banded A–D by evidence (within-band order a
work order, not a likelihood), movement conditions
named, and a structured priority.

*Falsifier:* a node meeting a generation threshold with
no gap entry, or with two; a gap entry whose candidate
reference does not resolve to a live placement
assertion or hypothesis edge; a candidate ranked by a
probability the register does not carry (WLG-04).

*Does not establish:* that any gap will close, or that
any candidate placement is likely — the register
describes an epistemic state and a work queue.

**C108-5 — The graph is evidence infrastructure, not a
fourth baseline, and this build moves nothing.** No
Spec 106 baseline, template, or pin is amended; no
program standing, verdict, or tally is edited; the
release's three hashes (graph snapshot, source
manifest, baseline pins) are distinct and separately
recomputable; graph content reaches a baseline only
through the reviewed amendment pipeline of the design's
§5.3, which this build does not execute.

*Falsifier:* any diff in this study's landings touching
a baseline template, a pin, or a program record of a
standing, verdict, or tally; a baseline-links record
asserting an adoption no amendment record names
(WLG-06).

*Does not establish:* that any graph assertion is fit
for baseline adoption — adoption is a separate,
reviewed act.

**C108-6 — Every populated item is sourced, labelled,
and reviewable.** Every field assertion and edge
carries exactly one evidence class (F/K/H), a source
grade (P1–P4), and a review state; every item names a
source actually opened, with a locator, or carries the
UNSOURCED flag, which appears only on (H) items; no
(F) item is unsourced; every (H) item carries a removal
condition; consensus / contested / fringe labels from
the ingestion source are preserved in the confidence
labels and never upgraded in transit.

*Falsifier:* a released item with no evidence class, a
missing or unopenable locator, an UNSOURCED item not
classed (H), or a confidence label stronger than its
source's own label (WLG-02).

*Does not establish:* that a sourced item is true —
only that its provenance is inspectable at the scope
its source claims.

**C108-7 — The release's census and pins recompute
exactly.** The release's stated counts (by node kind,
subtype, status, evidence class, gap kind, and
predicate) recompute exactly from the canonical
streams, and the graph snapshot hash and source
manifest hash recompute exactly under the schema
version the release names.

*Falsifier:* any count or hash in the release record
that does not recompute from the streams as filed
(WLG-01, WLG-05).

*Does not establish:* the correctness of any individual
assertion — only the internal integrity of the release
as a countable, citable object.
