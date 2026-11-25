# Spec 105 — Claims

Five claims, C105-1..C105-5, each with its falsifier
and its does-not-establish line, in the program's
claim form. The claims are intaken at registration
through the sanctioned importer (spec.md, D-105-4);
intake sets no standing, and no claim in this package
carries a result: no sandbox has been built and no
derivation has run at registration.

**C105-1 — The floor is exactly the census.** The
only primitives any stage of this study uses are the
five admitted in spec.md §2 (distinction, sequence,
co-presence, recurrence, boundary) over the recorded
token streams, with the recordings themselves as the
one admitted input assumption; every other candidate
primitive is demoted in the census with its reason,
and no demoted or refused item — counting, frequency,
"word", phonetic or sign value, any scholarly sign
list, language family, lexicon, grammar, translation,
gloss, imported segmentation, iconographic or
contextual meaning, mark similarity, cross-corpus
mark identity — is used as an input anywhere in the
study.

*Falsifier:* any build, derivation, or gate record of
this study demonstrably using a non-admitted input:
a sign or phonetic value, a gloss or translation, a
segmentation or normalization not in the recording,
an outside inventory, or material from another
sandbox or from outside the three pinned sources.

*Does not establish:* that the floor is sufficient to
derive anything — sufficiency is what the ladder and
the gates test, rung by rung, and a NOT-GOOD gate is
the registered way this study fails.

**C105-2 — The sandbox datasets are faithful strips
of the pinned sources.** Each dataset's streams
reproduce exactly the recorded token streams its
strip rule selects (spec.md §3): for Indus, the
`letters` values of the pinned Holdat file grouped
by `form`, ordered by `seal_id` and `position`; for
Eteocypriot, the recorded lines, segments, and marks
of ICS 196 and Androkles Dedication A in Spec 096's
two corpus files at their current recorded bytes;
for Meroitic, the `text` fields of the stream-carrying
rows of the pinned Kovetsky build's
`inscriptions.jsonl` — in every case with all
linguistic annotation removed and nothing else
removed, and with sealed or stream-less material
absent by the registered rules.

*Falsifier:* any token in any dataset differing from
its source as recorded (mark, order, grouping, or
line structure); any recorded token selected by the
strip rule missing from its dataset; any annotation
field or value surviving in a dataset (TC-105-04);
any sealed Spec 096 held-out content or stream-less
Meroitic row present in a dataset.

*Does not establish:* that any recording is a correct
or complete representation of any artifact in the
world — the sandbox takes recordings as given
(spec.md §2) and asserts nothing about them beyond
their content.

**C105-3 — The Stage 1 inventories are derivations,
not imports.** Each sandbox's L1 inventory filed at
Stage 1 is exactly the set of equivalence classes of
marks (sameness as recorded, spec.md §2 P-1) over
that sandbox's derivation set, produced by a
derivation that reads the sandbox dataset and
nothing else, and reproduced exactly by a second,
independently written implementation of the same
registered rungs (L0–L1).

*Falsifier:* the two implementations' inventories
differing for any sandbox; any filed inventory
containing a mark absent from its derivation set, or
missing a mark present in it; the derivation reading
any input other than its sandbox's dataset (the
reserve included).

*Does not establish:* that the derived inventory is
the script's sign inventory — it is the inventory of
the recorded streams under distinction alone, filed
beside the working sign lists and never merged into
them (C105-5).

**C105-4 — The sandboxes are separate and the
reserves stay sealed.** No datum, intermediate, or
result from one sandbox is used in another; the
three derivations share the registered procedure
only. The Indus reserve (334 artifacts by the rule
of spec.md §3.1) is sealed by its filed hash at
build and is read by no derivation until the G-IND
gate stage unseals it under its own registration;
Spec 096's sealed held-out inscriptions are read by
no part of this study.

*Falsifier:* any Stage 1 record importing another
sandbox's output; any derivation input containing a
reserve artifact (checked by artifact-index
disjointness, TC-105-06); the reserve dataset's hash
at any audit differing from the hash filed at build;
any access to Spec 096's held-out content in the
study's scripts or records.

*Does not establish:* that the separation is
sufficient for the gates' independence — the gates'
own registrations must still show their checkers
worked from outside material only.

**C105-5 — The sandbox moves no standing and claims
no decipherment.** Nothing this study files changes
any anchor standing, claim verdict, or tally in the
Indus, Eteocypriot, or Meroitic programs; nothing
derived inside a sandbox is stated, labelled, or
citable as a decipherment, a reading, or evidence
for or against any reading; sandbox outputs are
labelled sandbox-internal until a boundary gate
returns GOOD, and a GOOD gate licenses only the
specific comparison it checked.

*Falsifier:* any record of this study stating a
changed standing, verdict, or tally; any derived
inventory merged into, or cited as, a working sign
list; any citing record treating a sandbox output as
a decipherment claim or as evidence in another
study's adjudication beyond a gate's registered
GOOD on its own comparison.

*Does not establish:* that the derived systems are
wrong — only that this study's outputs carry no
standing outside the sandbox until the gates say
what they say.
