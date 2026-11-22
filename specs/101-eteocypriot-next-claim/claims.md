# Spec 101 — Claims

Four claims, C101-1..C101-4, each with its falsifier and
its does-not-establish line, in the program's claim
form. The claims are intaken at registration through the
sanctioned importer (spec.md, D-101-2); intake sets no
standing, and no claim in this package carries a result:
the study has not executed.

**C101-1 — At least one development-set ending candidate
recurs in ICS 194/195 under Perna 2019.** At least one
recurring-ending candidate, registered from the ICS 196
development set alone before scoring (spec §3.1, P-2),
occurs in the ICS 194/195 text under Perna 2019's
re-edition at its registered positions at or above its
registered occurrence floor, in the postdictive form
registered in spec §3.3.

*Falsifier:* every registered candidate is below its
registered floor or absent at scoring.

*Does not establish:* that any candidate's proposed
meaning is correct, or that the candidate predicted an
unseen text — occurrence at postdictive strength is a
distributional result over two texts, and meaning would
require an identifiability stage and adjudication this
spec does not register.

**C101-2 — The study reports its exposure honestly.**
Every outcome record of this study states, on its face,
that Perna 2019's chapter including its printed reading
of ICS 194/195 was read in full on 2026-11-22 (OD-9)
before any candidate was registered, and no outcome of
this study is described anywhere in the program's
records as a blind or held-out prediction.

*Falsifier:* an outcome record of this study omitting
the exposure statement, or any program record describing
a result of this study as a blind prediction.

*Does not establish:* that a postdictive result is
worthless; the claim governs the study's reporting of
its own strength, not the result's existence.

**C101-3 — No scoring uses an unstated table.** Every
derivation, stem table, or sign table used by any
scoring run of this study is written in full in the
study's freeze addendum before the run; where the E1
machinery is reused, the addendum reproduces the E1
driver's tables verbatim.

*Falsifier:* a scoring run whose derivation or tables
differ from the freeze addendum's, or a freeze addendum
omitting any table a run used.

*Does not establish:* that the tables are correct — only
that they are completely stated, so a re-runner needs
nothing the record does not contain (the defect OD-8's
F-4 found in freeze §5, closed here by construction).

**C101-4 — The Perna-side state has its own identity,
and Spec 096's corpus is untouched.** The corpus state
used for scoring is a new corpus state with a C095-3
identity record (per-inscription SHA-256 pins,
provenance naming Perna 2019 as edition of record and
the OpenEdition route, custody
`held_from_secondary_reproductions`), and the Spec 096
corpus file hashes to its version-1.1.1 value
(`2954283d…`) before and after this study's intake.

*Falsifier:* the Spec 096 corpus file differing from
its version-1.1.1 hash after this study's intake; a
scoring run over a Perna-side state lacking the
identity record.

*Does not establish:* that Perna's readings are correct
— the identity record pins what was read, not what the
stone says.

## Amendment pointers — 2026-11-22 (Red Team Round 6) — BINDING

The claim texts above are preserved unchanged. The
binding amendment record is
`records/floor-derivation-and-outcome-registration-2026-11-22.md`.

- **At C101-1 (RT6-H4, RT6-M5, RT6-M6).** The
  "registered occurrence floor" C101-1 names is the
  floor computed by the floor record's §1.3 rule
  (smallest k ≥ 2 with Binomial(M, f_i / 11) upper
  tail below 0.05 / K; never below 2), over a
  candidate set capped at K ≤ 4 (floor record §2).
  SUPPORTED requires a candidate at or above its
  computed floor **and** the registered family-wise
  chance probability Q below 0.05 (floor record
  §1.4–§1.5). If the study closes TOO THIN at its
  freeze, C101-1 stands NOT TESTED, neither SUPPORTED
  nor NOT SUPPORTED (floor record §3). Floors move
  only by that formula; any other change is a new
  candidate registration (floor record §4).
- **At C101-2 (RT6-L6).** The exposure statement
  C101-2 requires is the canonical string quoted
  character-for-character in the floor record's §5
  (and in spec.md's appended §3.3 amendment): "that Perna 2019's chapter including its printed reading of ICS 194/195 was read in full on 2026-11-22 (OD-9) before any candidate was registered"
  TC-101-04 is pointed at that quoted string.
