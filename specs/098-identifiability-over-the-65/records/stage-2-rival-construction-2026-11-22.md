# Spec 098 — Stage 2, T201: rival construction record

**Date:** 2026-11-22 · **Task:** T201 (acceptance: record +
test) · **Claim:** C098-3 · **Venue:** tower-compute, fresh
clone · **Freeze:** `records/stage-2-freeze-2026-11-22.md`
§5 · **Runner:** `tools/stage2_run.py` (rivals mode) ·
**Data:** `records/stage-2-rivals-2026-11-22.json`.

Construction followed the Stage 2 freeze exactly: one
deterministic construction per competitor, over development
data only, from the frozen search space; frequency and
position matching by construction (WP8 family C2's terms —
a wrong mapping for the same sign inherits that sign's
frequency and positional profile exactly). Munda is not
carried by any lexicon of record in the repository, so R-B
is drawn from Sanskrit for every sign (freeze §5).

The task's test leg (the TC-098-01 guard over the actual
development export) ran in the same payload: the frozen
split was recomputed over the corpus of record (2,413
clusters; 517 held out), the recomputed held-out set's seal
hash verified against the committed seal
(1974d83a5f667b71dbd53ecdb2e42a8221c6d4b91bdd32202b2a80579bf96cf9,
verify True) without reading the custody file, and
`development_export` passed all 1,896 development rows with
no SealViolation. The Stage 1 power grid was reproduced
exactly for the 69 signs (development token counts equal on
every row). No held-out sequence, token, or per-sign
held-out count was examined or stated; the seal was not
opened or released.

Payload verdict (the runner's own record): PAYLOAD VERDICT
T201: rivals_written=stage-2-rivals-2026-11-22.json
population=69 seal_verify=True guard_pass=True
grid_reproduced=True (runner exit 0).

Per-sign rivals (R-A and R-B values as drawn; full sources,
shapes, and pool data in the JSON):
| Sign | Candidate | R-A (Dravidian) | R-B (Sanskrit) | R-C referent | Extra Arm E rivals |
|---|---|---|---|---|---|
| M002 | kuṉ | kōṉ | svan | hill / mound | — |
| M004 | kēḷ | aaL | hotr | (function only) | — |
| M005 | kōṉ | kuṉ | svan | (function only) | — |
| M006 | puli | tiru | deva | tiger / leopard | — |
| M007 | aaL | kēḷ | hotr | (function only) | — |
| M009 | āṇ | kuṉ | svan | male / man | — |
| M010 | paṭ | miṭ | ap | sing / fall | — |
| M013 | nakaram | alavan | NOT CONSTRUCTIBLE | (function only) | — |
| M014 | tiru | puli | deva | (function only) | — |
| M015 | mā | kai | rta | (function only) | — |
| M016 | kaḷiṟu | erutu | varuna | (function only) | — |
| M017 | kai | mā | rta | (function only) | — |
| M018 | nēr | kēḷ | hotr | chest / heart | — |
| M020 | kuṉ | kōṉ | svan | hill / mound | — |
| M023 | vaḷ | kēḷ | hotr | strong | — |
| M025 | cem | kuṉ | svan | copper (red metal) | — |
| M026 | mā | kai | rta | (function only) | — |
| M027 | māṟ | kēḷ | hotr | tree / wood | — |
| M029 | yānai | puli | deva | (function only) | — |
| M030 | kō | mā | rta | king / chief | — |
| M032 | koL | kēḷ | hotr | take / kill | — |
| M034 | tōḷ | kēḷ | hotr | ancient / old | — |
| M037 | kēḷ | aaL | hotr | (function only) | — |
| M038 | pōr | kēḷ | hotr | (function only) | — |
| M041 | pēr | kēḷ | hotr | big | — |
| M045 | yānai | puli | deva | (function only) | — |
| M049 | pu | mā | rta | (function only) | — |
| M050 | pār | kēḷ | hotr | see / sing-out | — |
| M051 | pū/puḷ | mā | rta | (function only) | — |
| M052 | ta | mā | rta | (function only) | — |
| M053 | mi | mā | rta | (function only) | — |
| M054 | mi | mā | rta | (function only) | — |
| M055 | miN3 | kuṉ | svan | (function only) | — |
| M057 | māṭu | puli | deva | (function only) | — |
| M060 | kāṇṭāmirukam | NOT CONSTRUCTIBLE | NOT CONSTRUCTIBLE | (function only) | — |
| M061 | ka | mā | rta | (function only) | — |
| M062 | erutu | kaḷiṟu | varuna | ox / bull | — |
| M063 | mutalai | kaḷiṟu | varuna | (function only) | — |
| M065 | kuTam | aen | satam | (function only) | — |
| M066 | cōḻ | kēḷ | hotr | say / tell (full form) | — |
| M067 | kōṭṭāṉ | pakkam | paksin | (function only) | — |
| M068 | maṟi | puli | deva | (function only) | — |
| M069 | nēr | kēḷ | hotr | chest / heart | — |
| M070 | vēl | kēḷ | hotr | silver (white metal) | — |
| M073 | kōṉ | kuṉ | svan | (function only) | — |
| M074 | ker | kēḷ | hotr | (function only) | — |
| M075 | māṟ | kēḷ | hotr | tree / wood | — |
| M076 | naN | kuṉ | svan | good / virtue | — |
| M078 | cēr | kēḷ | hotr | reach / belong | — |
| M080 | vēṅkai | amma | simha | loving / dear | — |
| M082 | pa | mā | rta | (function only) | — |
| M089 | tu/tū | mā | rta | (function only) | — |
| M099 | kol/koḷ | kēḷ | hotr | take / kill | — |
| M128 | kaṇ | kuṉ | svan | see | — |
| M130 | mui | puli | deva | (function only) | — |
| M145 | miṭ | paṭ | ap | (function only) | — |
| M151 | viḷ | kēḷ | hotr | bow / curve of brow | — |
| M194 | kaṭ | paṭ | ap | protection / refuge | — |
| M220 | al | kēḷ | hotr | (function only) | — |
| M267 | iN/in (genitive) | kuṉ | svan | genitive / of | — |
| M347 | ka | mā | rta | (function only) | — |
| M351 | vī | mā | rta | (function only) | — |
| M374 | kul | kēḷ | hotr | (function only) | — |
| M375 | taṇ | kuṉ | svan | self / body | — |
| M391 | ka/kaṇ | mā | rta | (function only) | — |
| M047 | min/mīn | kuṉ | svan | fish (rebus: star, celestial) | R-X1 comparandum-as-value: in; R-X2 comparandum-as-value: mina |
| M124 | kuTam | aen | satam | pot / jar | R-X1 comparandum-as-value: kun |
| M329 | poṉ | kuṉ | svan | gold | R-X1 comparandum-as-value: pur |
| M330 | can | kuṉ | svan | (function only) | R-X1 cross-sign: can; R-X2 comparandum-as-value: an; R-X3 comparandum-as-value: anna |

R-D for every sign: the structural-only model (no value assignment; unconditioned order-1 neighbour-pair model). R-E: the global permutation filed in the data (`global_permutation_R-E` in `records/stage-2-rivals-2026-11-22.json`); signs in singleton shape classes are fixed points.
