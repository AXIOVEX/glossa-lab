# Spec 105 — Test Cases

Each test case names the claim it exercises, its
procedure, and its pass condition. TC-105-01 is
Stage 0's acceptance test and is recorded in
`records/registration-2026-11-25.md`; TC-105-02..
TC-105-07 execute with Stage 1.

**TC-105-01 — Package form (C105-1..C105-5; Stage 0).**
Parse `aee-claims.json`; compare its claim ids and
order against claims.md; check every claim carries a
falsifier and a does-not-establish line.
*Pass:* the JSON parses; the same five claim ids in
the same order in both files; every falsifier and
does-not-establish line present.

**TC-105-02 — Strip fidelity, Indus (C105-2;
Stage 1, before any derivation).** Verify the
operational copy's SHA-256 against the Spec 100 pin
(`62d14d2bebf7c2c80d98a2958e75ec52bff3f240ff3f5e85d1f7f40cbe28218e`);
rebuild the expected streams from the pinned file by
the strip rule of spec.md §3.1 through an
independently written checker (group rows by `form`,
order artifacts by `seal_id`, tokens by `position`,
read the `letters` column only) and compare against
the built derivation and reserve datasets jointly.
*Pass:* the pin verifies; the recorded census
reproduces (1,670 artifacts, 7,002 tokens, 390
distinct recorded marks, positions contiguous from
0); the two datasets' artifacts are exactly the
source's artifacts in recorded order, split by the
registered rule (index mod 5 = 4 to the reserve),
token for token.

**TC-105-03 — Strip fidelity, Eteocypriot and
Meroitic (C105-2; Stage 1, before any derivation).**
Verify the two Spec 096 files' SHA-256 against
spec.md §3.2 and the Kovetsky build's commit pin and
`inscriptions.jsonl` SHA-256 against §3.3; rebuild
the expected streams from the sources by the strip
rules through an independently written checker and
compare against the built datasets.
*Pass:* the pins verify; the Eteocypriot dataset is
exactly ICS 196's and Androkles Dedication A's
recorded lines, groups, and marks (2 artifacts, 3
lines, 14 groups, 69 tokens) and contains nothing
from any other record of the corpus files; the
Meroitic dataset is exactly the `text` streams of
the 376 stream-carrying rows in file order (29,843
character tokens, 5,195 groups), character for
character, case and lacuna marks as recorded.

**TC-105-04 — Stripping verification (C105-1,
C105-2; Stage 1).** Audit each built dataset for
surviving annotation: (a) a schema check — every
artifact object carries exactly the field `lines`,
every line is a list of groups, every group a list
of mark strings, and the dataset object carries no
field beyond its sandbox name and its artifact list;
(b) a blocklist scan of the datasets' full text for
annotation vocabulary drawn from the sources'
field names and value spaces (among them: `greek`,
`translation`, `gloss`, `site`, `iconography`,
`upos`, `xpos`, `morpheme`, `semantic`, `rem`,
`griffith`, `reading`, `edition`, `stratum`,
`split`, `status`, `correspondence`, `date`), and
for any source identifier (seal ids, CISI numbers,
ICS numbers, REM numbers) appearing as a dataset
value.
*Pass:* the schema is exact for every artifact of
every dataset; the blocklist scan returns zero hits;
no source identifier appears. (Mark strings
themselves are the recordings' own and are not
blocklist material; the scan targets fields,
annotation values, and identifiers.)

**TC-105-05 — Derivation purity and agreement
(C105-3; Stage 1).** Run the L0–L1 derivation under
the filed implementation and under a second,
independently written implementation of spec.md §5's
rungs, each reading only its sandbox's derivation
dataset; audit the filed implementation's inputs
(its opened paths are the dataset and its own
outputs only).
*Pass:* for every sandbox, the two implementations'
inventories are identical as sets, with identical
recurrence marks per class; the filed inventory
equals the set of distinct marks in the derivation
dataset, computed independently; no input beyond the
dataset was read.

**TC-105-06 — Reserve seal and partition discipline
(C105-4; Stage 1).** Hash the built Indus reserve
dataset and compare against the hash filed at build;
check the derivation and reserve artifact index sets
are disjoint and jointly the full recorded order;
confirm no Stage 1 script opens the reserve dataset
except the build and this audit.
*Pass:* the hashes match; the index sets are
disjoint and exhaustive under the registered rule;
the derivation's inputs contain no reserve artifact.

**TC-105-07 — Standing discipline (C105-5;
Stage 1).** Read the outcome record and the
execution landing's full diff.
*Pass:* no record states a changed standing,
verdict, or tally in any program; the derived
inventories appear only in this spec's records,
labelled sandbox-internal; no working sign list,
anchors register, or corpus file in the repo is
modified by the landing; the recommendations ledger
is untouched by this study (D-105-3).
