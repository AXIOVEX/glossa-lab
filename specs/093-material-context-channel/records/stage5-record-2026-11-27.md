# Spec 093 Stage 5 record — machinery extension (T501, T502)

**Date:** 2026-11-27. **Stage:** 5 of Spec 093 (the
material-context channel), executed under the owner's
commission of 2026-11-27 (Stages 3–6, exactly as
registered; the filed spec text is the authority — the
history ledger holds no commission record). Stage 4's
outcomes stand as its record states them (T401 NOT YET,
T402 CANNOT BE ADMINISTERED, T403 E1–E4 MET); this stage
is the machinery extension D-093-6 and D-093-7
registered, and it changes no claim's status, stage, or
score (C093-13).

## 1. The registered tasks

T501, verbatim from tasks.md: "**T501 — Matrix rows and
map layer, generated.** The generators emit the
material-context domain's matrix rows and the program
map's material-context layer from the ledger family; no
generated file is hand-edited. Acceptance: **gate**
(regeneration reproduces the surfaces byte-for-byte from
the ledger). *This does not establish:* that the layer's
claims are true — only that the surface is the ledger,
generated, citing ids."

T502, verbatim: "**T502 — Gate extension.** The ledger
gate gains the culture-layer checks (citation existence,
one-way flow, register-section counting support for
Stage 6), with a seeded-violation proof that a bad
citation fails. Acceptance: **test** (seeded violation
fails; clean tree passes in both modes at the extended
profile). *This does not establish:* that earlier layers'
checks changed — the standing profile's existing counts
are untouched, and the extension is additive."

## 2. T501 — the taxonomy amendment and regeneration

The family's fourteen claims already stood in the
generated matrix (14 rows of 1,073, emitted from the
ledger family; the matrix row format — id, population,
status, stage — carries no domain axis, so the domain
act T501 names is the program map's) and on the program
map under the study-line grouping "Claim families by
study line" / "Site, object & repertoire tests". The
matrix side of T501 is therefore a reproduction
obligation, discharged below. The map layer is the
amendment act:

- **Taxonomy amendment (PROGRAM-MAP-DEFINITIONS.md §8:
  an assignment change is a new taxonomy version,
  recorded in the stage record in the same motion,
  C088-9).** `program-map-taxonomy v1` →
  `program-map-taxonomy v2`: a sixth domain,
  **Material context**, with the single subdomain **The
  material-context channel**; the one assignment moved
  is this spec's study, `093-material-context-channel`,
  from "Claim families by study line" to the new domain.
  No other assignment changed.
- **Same-motion copies (§12 discipline):** the taxonomy
  file, the builder's `TAXONOMY_VERSION`
  (`backend/glossa_lab/program_map_generate.py`), the
  gate's `PROGRAM_MAP_TAXONOMY_VERSION`
  (`backend/glossa_lab/ledger_gate.py`), and the
  definitions document's three version literals. The
  conformance suite's pinned domain census
  (`backend/tests/test_program_map_conformance.py`) is
  data tracking the curated file and moved with it in
  the same motion ("Claim families by study line"
  41 → 40 studies; "Material context" 1). Historical
  records carrying the v1 literal are records of their
  time and were not touched.
- **Regeneration through the gated publish path**
  (`gated_publish.publish_program_map` /
  `publish_matrix`; publication only on an all-pass
  gate): the program map republished — program-map.json
  SHA-256 `732558dd…`, program-map-finds.json
  `5f19aa31…`, program-map.html `e253991c…`. The new
  domain's coverage reads 1 study, 14 claims, all class
  open (their draft standings, unchanged). The matrix
  republished **byte-identical** (matrix.json
  `913da57e…`, matrix.md `e74b13ee…`, both unchanged),
  and map-data.json is unchanged (`2ad12c4e…`) — the
  taxonomy feeds neither surface, and their regeneration
  reproducing byte-for-byte is T501's gate on those
  surfaces.
- **Disclosed mid-motion refusal:** the first
  `publish_matrix` attempt in this stage was refused by
  the gate while the published program map still carried
  the old grouping — the new V12 flow leg named the
  family's claims as missing from the layer. That is the
  machinery working as designed (a half-amended tree is
  red); after the program map published, the matrix
  publish passed with byte-identical output.
- **Gate evidence (T501's gate):** full mode over the
  landed tree — 32 PASS / 0 FAIL / 1 NOT-RUN (V7, which
  runs under `--regen`); regen mode — 35 PASS / 0 FAIL /
  0 NOT-RUN, V7 byte-identical on matrix.json, matrix.md
  and the map data, and V10's byte-compare over the
  program-map artifacts passing in both modes.
  Regeneration reproduces the surfaces byte-for-byte
  from the ledger. **T501 complete.**

## 3. T502 — the V12 culture checks

A new gate class, **V12**, in
`backend/glossa_lab/ledger_gate.py` (`_v12_checks`),
assembled in `run_gate` after V11 in the established
shape, and added to the CLI's layer map
(`tools/ledger/check_ledger_gate.py`: the `program_map`
and `map` layers gain V12; machinery paths continue to
fall back to the full gate). Posture, following V10/V11:
where the material-context layer has not landed at all
(no such domain in the taxonomy and no program-map node
carrying it), V12 enumerates a single NOT-RUN. Once any
part of the layer is present, every leg runs:

1. **Citation existence** — every claim node in the
   Material context domain cites a ledger entry that
   exists, and the channel study's node is present in
   the domain. On the landed tree: PASS — "14 claim
   nodes in the Material context domain, every one
   citing a ledger entry; the channel study node
   present".
2. **One-way flow** — the domain's claim-id set equals
   exactly the ledger's family set (ids under
   `093-material-context-channel/`); no family claim is
   grouped under another domain. On the landed tree:
   PASS — "the layer's 14 claim nodes are exactly the
   ledger's 14 claims of 093-material-context-channel;
   no family claim grouped elsewhere".
3. **Register-section counting support** — the leg
   Stage 6 lands its section under (C093-12). It reads
   the gap register's culture-side section: where the
   section is absent the leg PASSes with the zero count
   on its face ("the register carries no culture-side
   section yet; 0 GR-093 entries counted (the counting
   support Stage 6 lands the section under, C093-12)") —
   the wording decision is stated here on the record:
   absence of the section before Stage 6 is not a
   defect, and the count is never left implicit. Where
   the section is present it must carry at least one
   GR-093 entry, and every entry is checked for the
   four C093-12 elements, detected by their register
   fields (**Missing piece:** — what is not known;
   **Candidate** — the acceptance test; **Falsifier:**;
   **Type:** — the honesty type); an entry missing any
   element fails the leg, naming the entry and the
   element.

**Teeth (T502's test).** `backend/tests/
test_spec093_stage5_gate_extension.py` — ten tests over
synthetic mini-trees plus the real tree: the absent
layer enumerates NOT-RUN; the clean layer passes all
three legs; a seeded node citing no ledger entry fails
citation existence; a family claim missing from the
layer fails one-way flow; a family claim grouped under
another domain fails one-way flow; the study node
missing fails citation existence; a complete register
section is counted (1 entry); a register entry missing
its falsifier fails the counting leg, naming the entry;
an empty culture section fails; and the real tree
passes V12 at the extended profile with the 14-claim
layer. All ten pass. The neighbouring suites
(`test_spec086_ledger_gate.py`,
`test_spec088_program_map.py`,
`test_program_map_conformance.py`) pass with the single
disclosed census-pin update above. The clean tree
passes in both modes at the extended profile (full:
32 PASS / 0 FAIL / 1 NOT-RUN; regen: 35 PASS / 0 FAIL /
0 NOT-RUN). The extension is additive, as T502's own
limit requires: the change adds the V12 section and its
assembly block and touches no existing check's code or
name, so the standing profile's existing counts are
untouched — the profile gains exactly V12's checks.
**T502 complete.**

## 4. What the stage leaves standing

The layer is presentation and verification only: it
cites ledger ids and carries the standings the ledger
gives it (all fourteen claims open, as their draft
standings stand). Nothing in this stage asserts channel
evidence, and H1 is respected — no surface downstream of
the ledger states anything stronger than the ledger
does. C093-1's standing stands as Stage 2 recorded it:
INDEPENDENT IN PART for site and find context, with the
closure qualifier ("Population: 179 joined pairs, all
Mohenjo-daro; single stratum; no cross-site inference").
Stage 6 (the gap register's culture-side section and
the closeout) remains, and the counting support it
lands under is now in place.
