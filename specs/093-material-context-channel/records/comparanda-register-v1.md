# Spec 093 — Comparanda register v1 (Stage 3, T301)

**Filed 2026-11-27 under FR-093-05 / FR-093-06 (C093-4,
C093-5), seeded per D-093-7.** This register is the only
comparanda authority for computations under this spec:
a cross-cultural comparison is computed only if an entry
below naming (i) the comparanda set, (ii) the transmission
mechanism — documented trade, contact, or continuity,
stated as a checkable historical claim with its source,
(iii) a fixed time window, and (iv) the practice compared
was committed before the computation's first run. Entries
are append-only in effect: an entry's terms, once any
computation under it has run, change only by a new entry
that supersedes it, voiding the predecessor's results in
the same act (C093-5).

**Seeding (D-093-7).** v1 entries are drawn from the
corpus catalogue's 39 corpora
(`backend/glossa_lab/corpus_catalogue_seeder.py`) and the
contact-zone records
(`glossa-corpus/indus/sources/contact-zone-rebuilt-2026-10-25/`).
Every one of the 39 catalogue corpora is accounted for in
this register: two are entered (under CR-093-04), five are
the subject corpus itself (the Indus entries — a corpus is
not its own comparandum), and the remaining 32 are named
in the annex as considered and not entered, with the
reason. Entries beyond the seeded sources — Egyptian
practice, later South Asian continuity at millennial
spans — are admissible only as later amendments, each
with its mechanism argued from named sources before any
computation under it (D-093-7).

**The four-element check** over this register is
`tools/spec093/check_comparanda_register.py`: every entry
carries the four elements, and every catalogue corpus is
accounted for exactly once across the entries and the
annex. The check's output is filed in the stage record.

---

## CR-093-01 — Indus-type seals in Mesopotamian find contexts

- **Comparanda set:** the 14 Indus-type seals rebuilt in
  `seals_at_mesopotamia.json` (catalogue ids AO_22310,
  BM_122187_UR_seal_1, GADD_1, GADD_2, ASMAR_TA,
  KISH_INDUS_1, SUSA_INDUS_1, LOTHAL_PERSIAN_GULF_SEAL,
  FAILAKA_KM_1113, VA_243_BERLIN, KONAR_SANDAL_S_CYLINDER,
  JALALABAD_FARS, AL_MAQSHA_TOKEN_2, JANABIYAH_LAURSEN_10),
  each with its recorded find spot and find period.
- **Transmission mechanism:** documented contact — seals
  of Indus type were physically carried to and deposited
  at Mesopotamian, Elamite, Gulf, and Iranian-plateau
  sites; the find contexts are the mechanism's evidence.
  Source: `seals_at_mesopotamia.json` and
  `contact_zone_rebuild_provenance.md` in the same
  directory.
- **Fixed window:** 2334–1600 BCE, the span of the
  recorded `find_period` values (Akkadian through
  Sukkalmah / Old Dilmun), frozen at v1. A seal whose
  recorded period fell outside it would be excluded from
  comparisons under this entry; none does at v1.
- **Compared practice:** deposition and find context of
  Indus-type seals outside the Indus region — where they
  were deposited and in what period — against the
  Indus-side record.

## CR-093-02 — The Meluhha documentary record

- **Comparanda set:** the 1,462 CDLI textual hits rebuilt
  in `meluhha_tablets.json`, each with period and
  provenience as recorded.
- **Transmission mechanism:** documented trade —
  Mesopotamian texts naming Meluhha (the rebuild's match
  set also carries the Dilmun and Magan keywords of the
  same route) attest the contact in writing. Source:
  `meluhha_tablets.json` and
  `contact_zone_rebuild_provenance.md`.
- **Fixed window:** 2500–1600 BCE (ED IIIb through Old
  Babylonian). Hits outside the window exist in the file
  (Uruk III through Neo-Assyrian) and are excluded from
  comparisons under this entry; a fixed window excludes,
  or it is not a window.
- **Compared practice:** documentary attestation of the
  contact — which periods and proveniences attest it, and
  in what volume of surviving text.

## CR-093-03 — The Gulf / Dilmun seal population

- **Comparanda set:** the Laursen 2010 Table 1 rebuild,
  `laursen_2010_table1.json`: 121 rows (Gulf Type 92,
  Gulf INDUS 28, Gulf Linear-Elamite 1), 28 of them
  inscribed with Indus text per the rebuild's aggregate.
- **Transmission mechanism:** documented Gulf
  intermediation — the Dilmun/Gulf seal tradition stands
  between Indus and Mesopotamian sealing practice on the
  documented maritime route. Source:
  `laursen_2010_table1.json` and
  `contact_zone_rebuild_provenance.md`. (The rebuilt
  table is the artifact; the Laursen author copy never
  enters the repository, C093-10.)
- **Fixed window:** 2100–1750 BCE, the Early Dilmun
  horizon; its in-repo anchors are the seals file's Early
  Dilmun find periods (JANABIYAH_LAURSEN_10, ca.
  2100–2000 BC; FAILAKA_KM_1113, ca. 1950–1750 BC).
- **Compared practice:** seal typology and metrology
  (`gulf_type`, `dia`, `th`, `boss_dia`, `grooves`) in
  the intermediate zone, against Indus and Mesopotamian
  practice.

## CR-093-04 — The receiving culture's written corpora

- **Comparanda set:** the corpus catalogue's two
  Mesopotamian corpora — the two named in the
  annex census below as entered here —
  as catalogued in
  `backend/glossa_lab/corpus_catalogue_seeder.py`.
- **Transmission mechanism:** the documented contact of
  CR-093-02 — these are the written corpora of the
  culture whose texts carry the Meluhha attestations.
  Source: `meluhha_tablets.json` and the two catalogue
  entries.
- **Fixed window:** 2112–2004 BCE, the Ur III span as
  catalogued, and the modal attestation period under
  CR-093-02.
- **Compared practice:** documentary reference practice —
  how the receiving culture's texts register the contact
  (periods, proveniences, designations), as the frame
  the Meluhha record is read against.

---

## Annex — catalogue corpora considered and not entered

The subject corpus (not comparanda):
- Indus Script (Mahadevan 1977 synthetic)
- Indus Script (CISI corpus — Parpola 1987)
- Indus Script (Yadav et al. 2010 — TIFR corpus)
- Indus Script (Wells 2011 — Sign Catalogue)
- Indus Script (Harappa.com digital archive)

Entered under CR-093-04:
- Sumerian Ur III (CDLI statistics)
- Akkadian Cuneiform (Old Babylonian)

Not entered — no transmission mechanism of record exists
in-repo for any of these against the Indus record system,
and H2 admits no comparison without one. Each is
admissible later only by a register amendment arguing
its mechanism from named sources before any computation
under it (D-093-7):
- Linear A (DĀMOS database)
- Proto-Sinaitic (Serabit el-Khadim + Wadi el-Hol)
- Meroitic (Kushite inscriptions)
- Rongorongo (Easter Island)
- Zapotec Script (Monte Albán)
- Voynich Manuscript
- Ugaritic Baal Cycle (KTU 1.1–1.6)
- Old Hebrew (Gen-Prov, consonantal)
- Phoenician KAI Inscriptions
- Linear B / Mycenaean Greek (Pylos tablets)
- Ge'ez Genesis (Ethiopic syllabic, Dr. Fuls)
- Coptic Reference Corpus (Meroitic comparison)
- Egyptian Hieroglyphic (Middle Egyptian)
- Hittite Cuneiform (KBo corpus)
- Ancient Greek (Homer, Iliad)
- Classical Latin (Caesar, Cicero, Virgil)
- Oracle Bone Script (Shang dynasty)
- Sanskrit (Rigveda, Devanagari transliteration)
- Modern Standard Arabic (news corpus)
- English (Brown Corpus)
- Mandarin Chinese (CC-CEDICT)
- Hindi (Devanagari, news corpus)
- Japanese (Hiragana corpus)
- Korean (Hangul corpus)
- Finnish (FiWaC corpus)
- Turkish (news corpus)
- Swahili (news corpus)
- Basque (Elhuyar corpus)
- Tamil/Dravidian (classical corpus)
- Classical Syriac (Peshitta)
- Russian (Cyrillic, news corpus)
- Old Persian Cuneiform (Achaemenid inscriptions)

*This does not establish:* that the seeded comparisons
are the right ones — only that each was fixed, with its
mechanism, before anything was computed under it.
(T301's line, carried verbatim.)
