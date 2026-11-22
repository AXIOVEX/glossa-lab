# Re-verification remainder package — Spec 091 (OD-4)

**Date:** 2026-11-22
**Commission:** Owner decision OD-4 on the Co-scientist refresh adjudication of
2026-11-22 (`coscientist-refresh-adjudication-2026-11-22.md`), commissioning the
remainder itemised in the first re-verification pass
(`external-support-reverification-2026-11-21.md`, PR #633) and in adjudication
unit I-20.
**Scope of this package:** (a) the targeted inspection for M330, whose
external-support claim closed NOT VERIFIABLE in the first pass; (b) the
outside-proposal legs of M124 and M329, both PARTIALLY VERIFIED on their DEDR
legs only; (c) the unresolved Elamite forms and the incomplete Mahadevan
citation, mapped to named signs and basis items and finished or formally
retired.
**Rules observed:** verification only against lawfully held or lawfully
reachable material — the program's held Parpola 2010 recovered text, the
Parpola 1994 OCR scan in restricted custody, the restored DEDR tree, and
published sources reachable through the paper-search route. No external sends,
no purchases, no contact with any scholar. A verification outcome is
provenance only, as the first pass established. Class consequences are applied
only where the program's existing rules mechanically dictate one (the M202
addendum rule); anything else is flagged for the owner in §9.

## 1. The mapping the first pass lacked

The first pass could not resolve the program-internal comparative codes
(MC-07, MC-18, MC-21; SL-03, SL-04, SL-14) to named publications, and two of
the six class-E basis lines as rendered in
`specs/099-inference-log/records/basis-rows-2026-11-21.json` are truncated
mid-word. The mapping below is read from the filed bases themselves and from
the upstream filed record that produced them (§2).

| Code | Filed form | Sign(s) whose basis carries it | What the code is |
|---|---|---|---|
| MC-07 | Elamite 'an' | M202, M330 | Program-internal pointer (Phase-276 corroboration package); no publication is named anywhere in the record |
| MC-18 | Elamite 'kun' | M044, M124 | Same |
| MC-21 | Elamite 'bur/pur' | M329 | Same |
| SL-03 | Sanskrit 'annam/anna' | M202, M330 | Same |
| SL-04 | Sanskrit 'kona' | M044, M124 | Same |
| SL-14 | Sanskrit 'pura' | M329 | Same |

The Sanskrit map: SL-03 'annam/anna' (M202, M330), SL-04 'kona' (M044, M124),
SL-14 'pura' (M329). The Elamite map: MC-07 'an' (M202, M330), MC-18 'kun'
(M044, M124), MC-21 'bur/pur' (M329). No other sign's basis carries these
codes. (Two further Phase-163 entries in the upstream trails file — a 'co'
reading sourced to Wells 2015 and a 'cul' reading sourced to Parpola 1994 —
belong to signs outside the six class-E filings and are out of scope here.)

## 2. The truncated corroboration lines — FINISHED by production

The first pass recorded that the Phase-276 segments of the M202 and M330
bases are truncated in the basis rows and "uncheckable until the underlying
record is produced in full." The underlying record is on file in the
repository: `reports/phase108_anchor_trails.json`, the upstream source from
which the basis rows were extracted. Read first-hand in this pass, both bases
stand there in full:

- M202, `entry_fields.basis`, final segment: "Phase-276: dual external
  corroboration — Elamite 'an' (MC-07) + Sanskrit 'annam/anna' (SL-03)".
- M330, `entry_fields.basis`, final segment: identical wording — "Phase-276:
  dual external corroboration — Elamite 'an' (MC-07) + Sanskrit 'annam/anna'
  (SL-03)".

The item is finished: the filed bases are produced, not completed by
inference (Spec 099 §3.4 is observed — nothing was reconstructed; the text
was read from a filed record). The two legs the production adds to the map
are checked in §5 (SL-03) and §6 (MC-07). A consequence for the inference log
is flagged in §9: the log's notes on M202 and M330 record the truncated
segments and enter no items for them; entering the two comparative items for
each reading, now that the lines stand produced, is a Spec 099 act and is not
executed in this package.

## 3. DEDR entry 1638 as numbered (M044) — FINISHED

The first pass named the closing instrument for this item: the dictionary's
own digital edition, queried by entry number. That instrument has since been
run twice on the record. The register reconciliation
(`dedr-register-reconciliation-2026-11-21.md`) read entry 1638 in the
restored tree as Ta. kucukucu "to whisper," with no ku form, and the F-4
digital-edition pass (`dedr-digital-edition-pass-2026-11-22.md`) confirmed
against the DSAL digital edition of the printed dictionary that print entry
1638 = tree entry 1638 = Ta. kucukucu "to whisper" (p. 150), with no
tree-versus-print divergence anywhere in the pass. This pass re-read the two
entries in a fresh clone of the pinned tree (github.com/moli-mandala/data at
`d5050e5a9671012df416e9c474c75aba41c07f8c`): the clone's `dedr_new.csv`
hashes to SHA-256 `fbcc2b2d47c9be24338d846319de2b2c5a2ad4f45451274e3223bc63bc60cae0`,
byte-identical to the restore pin, and in that file entry 1638's rows are the
kucukucu family — Ta. kucukucu "to whisper," kucukucuppu "whispering," Mal.
kuśukuśukka "to whisper," and their kin — with no ku form among them. As a
control on the same instrument, entry 4570 reads Ta. poṉ "gold, metal, iron,
wealth, ornament, beauty" (M329's dictionary entry, §8) and entry 1651 reads
Ta. kuṭam "waterpot" (M124's, §8).

The M044 act's symmetry clause is therefore settled as the F-4 pass recorded:
not triggered. The DEDR leg of M044's basis stands struck; M044 stands in
class U. No further action on this item.

## 4. The Mahadevan leg of M047's basis — RETIRED

The filed basis for M047 ends "(sourced from Parpola 1994a + Mahadevan" and
names no Mahadevan publication. The first pass could retrieve no Mahadevan
text proposing the value. This pass closes the item by retirement, on four
grounds, each read first-hand or from a named reachable source:

1. **The citation resolves to a catalogue, not a proposal.** The crosswalk
   from which the basis line derives carries its own citation block, read in
   the F-9 pass: Mahadevan 1977 (the concordance), Parpola 1994a/b (sign
   list, fig. 5.1), Wells 2015. These are the sources for sign correspondence
   and glyph identity. The concordance catalogues signs; it proposes no
   phonetic values.
2. **The one Mahadevan text the program has engaged in full contains no such
   proposal.** Mahadevan's RMRL lecture, *Vestiges of Indus Civilisation in
   Old Tamil* (read in full in this pass, 13,421 words): the word "fish"
   occurs once, in a list of pictorial motifs ("man, archer, load-bearer,
   fish, bird, etc."); no mīn, meen, or star value is proposed for any sign;
   the lecture's rebus discussion yields muruku. Parpola is cited for other
   matters only.
3. **The proposal the basis gestures at is attributed elsewhere.** The
   fish = mīn rebus is standardly attributed to Heras (1953) and developed by
   Parpola (1975; 1994: 179–184) — the attribution is consistent across the
   reachable secondary literature (Sengupta 2023, *Studia Orientalia
   Electronica* 11(1), read in this pass) and across Parpola 1994 itself
   (§10.1, verified in the F-9 pass).
4. **Mahadevan's own position on the fish sign was a different one.** The
   reachable record of his published view separates him from the mīn
   proposal: he held the fish sign had nothing to do with astronomy (his own
   interpretation ran to a sea-nymph / Mīnākshi line). A basis leg that
   implies Mahadevan proposed mīn for this sign is not merely unverifiable;
   it points at the scholar least associated with that proposal.

Retirement is the honest close: as filed, the leg names no publication; its
only expansion on the record resolves to a sign catalogue that proposes no
values; and no reachable Mahadevan text contains the proposal. The leg is
retired as a value-proposal leg. No class consequence follows — M047 stands
in class U under the F-9 act — and owner decision OD-1's broadened reopen
clause governs any future revival: a verified prior proposal, entered as a
dated, source-linked basis amendment, would be a new filing, not a repair of
this one.

## 5. SL-03, Sanskrit 'annam/anna' (M202, M330) — checked; does not support

Checked against the Monier-Williams *Sanskrit-English Dictionary* in its
Cologne digital edition (CDSL 2020 digitisation): headword **anna** (L 8478,
printed p. 45, col. 1), from √ad "to eat": neuter noun, "food or victuals,
especially boiled rice." The lexeme is real and correctly cited as a Sanskrit
word. Its sense — food, boiled rice — has no connection to the value 'can',
to any sibilant, or to the Shu-ilishu /su/ phonological slot the M202 and
M330 bases invoke. The leg therefore closes in the same form as SL-04
'kona' in the first pass: the word exists; as corroboration of the filed
reading it does not support. No class consequence: M202 stands in class U
under its own act, and a comparative leg neither carries nor strikes M330's
class E, which rests on item M330-01 (§7).

## 6. The Elamite forms — finished item by item

Two Elamite compilations were lawfully reachable as text and were read in
this pass:

- **Hallock 1969**, *Persepolis Fortification Tablets* (OIP 92), the volume's
  Glossary of Achaemenid Elamite — the named corpus glossary for the
  Achaemenid material, covering the fortification and treasury texts and the
  royal inscriptions. Read in full (headword searches across the complete
  extracted glossary, A–Z, and its sign list).
- **The Elamite basic-vocabulary list** compiled by Blažek (2015) from
  Grillot-Susini (1987) and Hinz & Koch's *Elamisches Wörterbuch* (1987),
  published as Wiktionary's "Appendix: Elamite word list" — the reachable
  digest of the Wörterbuch tradition. Read in full (351 entries).

Results, form by form:

- **MC-18 'kun' (M044, M124) — the form is verified; the corroboration is
  not.** The basic-vocabulary list attests kun (also written ku-un) at entry
  3.110, glossed **"animal."** Hallock's glossary has no common noun kun;
  its Ku-un- headwords are proper names. Nothing in either compilation
  connects the lexeme to any Indus sign, to the value ku, or to a waterpot.
  The leg is finished: the Elamite word exists, its meaning is "animal," and
  as corroboration of M044's ku or of M124's kuTam it does not support. (For
  M124 the refresh adjudication already records that the reuse of this
  package "does not derive kuTam"; M124's class E rests on its verified DEDR
  item, §8.)
- **MC-21 'bur/pur' (M329) — pur is verified as a lexeme and does not
  support; bur is not attested in either compilation.** The basic-vocabulary
  list attests pur (pu-ur) twice: entry 4.344 **"fingernail"** and entry
  12.820 **"circle."** Hallock has no common noun pur; its Pu-ra- headwords
  are proper names. Neither attested sense touches M329's gloss (gold,
  precious), and Hallock gives the Achaemenid Elamite word for gold as
  **lada / lagda** — unrelated to pur in form. No entry for bur appears in
  either compilation. The item closes: pur finished (checked; does not
  support); bur not verifiable against any reachable source, the specific
  unreachable element being the full text of Hinz & Koch's *Elamisches
  Wörterbuch*, which is not lawfully reachable as text — the two reachable
  compilations that digest it and the corpus attest neither the form nor any
  gold connection.
- **MC-07 'an' (M202, M330) — RETIRED.** Neither compilation attests a
  standalone Elamite lexeme an: the basic-vocabulary list has none (its
  an-initial entries are compounds such as an-ka "if"), and Hallock records
  only a verbal prefix an- and an entry AN of unknown meaning. The code
  itself names no publication in any filed record, so there is no named
  source left to check the pointer against. Retirement is the honest close
  for the pointer as filed; it asserts nothing about the Elamite language,
  and a future filing that names a source can be checked on its own terms.

No class consequence arises from any Elamite item: M044 and M202 stand in
class U under their own acts, and M124's and M329's class E standings rest on
their verified DEDR items, not on these comparative legs.

## 7. M330 targeted inspection — NOT VERIFIABLE, with a strengthened negative

The first pass closed M330's published-proposal item (M330-01) NOT
VERIFIABLE: its pointers name no page or section, the book's searchable text
is an OCR scan, and no passage proposing the value 'can' for any sign was
found. The adjudication commissioned a targeted inspection of the most
likely source locations, with search coverage and OCR limits recorded. The
inspection ran as follows.

**Coverage.** The whole of Parpola 1994 was extracted from the held scan and
searched in full: 392 pages, 346,212 words. Whitespace-normalised searches
for every proposal pattern ("read as … can," "value … can," "sign for …
can," "pronounced … can," "transliterated … can") return zero. The held
Parpola 2010 text (recovered clean text, 10,806 words) was searched the same
way: zero, and no sibilant material at all.

**The most likely locations, identified and read.** From the book's own
table of contents and from the claim's framing (a reading 'can' supplying
partial coverage for the Shu-ilishu /su/ phonological slot), the candidate
locations are: the Meluhha and Near East contact chapters (§§1.4–1.5), the
seal chapters (§§7.4–7.5), the language-identity chapters (ch. 8), the
areal-linguistics chapter (§9.2–9.3), and the value-proposal chapters of
Part IV (chs. 10–14) with the two indexes. The decisive ones were read at
passage level:

- **Su-ilishu occurs in exactly one place in the book**: §8.3 (printed
  pp. 131–133), with its figure caption (fig. 8.4) and a mention in the list
  of figures. Read in full, in both flowing and layout extraction: Parpola
  argues from the seal that Meluhha's language differed fundamentally from
  the Near Eastern languages, discusses a five-sign Indus inscription on a
  Mesopotamian seal whose sign juxtapositions are unattested elsewhere, and
  quotes Hunter on Near Eastern seal sequences. He assigns no Indus sign a
  value there, proposes no 'can', and raises no /su/ phonological slot. The
  2010 paper's single Su-ilishu mention makes the same language-difference
  point and nothing more.
- **"Sibilant" occurs three times in the book**: two passages and the index
  entry pointing to one of them (printed p. 151). Both passages were read in
  full; both concern South Asian areal phonology (the eastern Indo-Aryan
  sibilants in the dāsa discussion; retroflex typology in §9.2). Neither
  concerns an Indus sign.
- **The Index of Indus signs** (printed p. 349) lists signs by drawing with
  page numbers only; it carries no transliterated readings, so it cannot
  hold the proposal in text form. **The general index** has no Su-ilisu
  entry; its only sibilant entry points to the passage already read.

**OCR limits, stated plainly.** The 1994 text is a FineReader OCR scan. Its
body text reads cleanly (the passages above are fully legible, and layout
extraction of the Su-ilishu pages confirms both columns and the captions are
captured whole), but an OCR scan cannot prove a whole-book negative: a
proposal stated once, in a form the OCR garbled, would escape the searches.
That limit is exactly why the close stays NOT VERIFIABLE rather than moving
in either direction. The negative finding is nonetheless materially
stronger than the first pass's: it is now anchored at passage level in the
claim's home territory (the only Su-ilishu discussion in either book) and
across the full text of both books.

**Close.** M330-01 stands NOT VERIFIABLE. The specific element that remains
unreachable, and the only one that could convert this negative into a
verification or a contradiction, is a clean text of Parpola 1994 (a
born-digital or publisher text) — or the author. Because no contradiction
against a named source has been produced, the M202 addendum rule is not
triggered: no act is executed, and M330 stands in class E on item M330-01
exactly as before. The comparative legs newly produced for M330 (§2) are
closed at §§5–6 and carry no class weight in either direction.

## 8. The outside-proposal legs of M124 and M329 — NOT VERIFIABLE, whole-book negatives

Both readings closed PARTIALLY VERIFIED in the first pass on their DEDR legs
alone; their outside-proposal legs (via-phase pointers to Parpola) were left
open. This pass searched the full texts of Parpola 1994 and Parpola 2010 for
both.

- **M124 (filed value kuTam, gloss pot/jar).** The strings kutam, kuṭam,
  kudam and waterpot occur **zero times in the whole of Parpola 1994**, and
  zero times in Parpola 2010. Parpola nowhere proposes a kuTam or waterpot
  reading for any sign in either book. The leg closes NOT VERIFIABLE with a
  whole-book negative finding, subject to the same OCR limit stated in §7.
  M124 stands PARTIALLY VERIFIED on its dictionary item — DEDR 1651, Ta.
  kuṭam "waterpot, hub of a wheel," re-read first-hand in this pass from the
  pinned tree (§3) — and its class E is unchanged. One filing observation is
  flagged in §9: the basis row carries a LITERATURE evidence line
  (Parpola_1994_via_phase51) for which the inference log enters no item.
- **M329 (filed value poṉ, gloss gold, precious).** No passage in either book
  proposes reading a sign as poṉ or as 'gold': the targeted patterns ("read
  as … po…," "value … poṉ," any sign–gold collocation in either order)
  return zero in both books, and all 53 occurrences of "gold" in Parpola
  1994 were read in context — every one concerns artefacts, trade goods,
  mythology or ritual (gold rosettes, Meluhhan gold dust, golden fish
  images, the Pyrgi gold plates), never a sign value. The leg closes NOT
  VERIFIABLE with the same negative finding and the same OCR limit. M329
  stands PARTIALLY VERIFIED on its dictionary item — DEDR entry 4570, Ta.
  poṉ "gold, metal, iron, wealth, ornament, beauty," re-read first-hand in
  this pass (§3); the citation repair from 4524 to 4570 is carried by the
  L-2 log amendment (PR #677, in flight at the time of writing) — and its
  class E is unchanged. Its Sanskrit pura
  leg already stands failed on the record (pura means stronghold/city; the
  L-2 amendment annotates it as contributing nothing), and its Elamite leg
  is closed at §6.

## 9. Class consequences and flagged items

**No act is executed in this package.** No item in the remainder produced a
contradiction of a class E claim against its named source, so the M202
addendum rule is nowhere triggered. The standings are untouched: **3 E + 66 I
+ 4 R + 3 P + 18 U = 94**, with M124, M329 and M330 in class E on their
respective bases as recorded above.

Three consequences are flagged for the owner, none mechanically dictated,
none executed here:

1. **The produced M202/M330 basis lines have no inference-log items.** The
   log's notes on M202 and M330 record the truncated Phase-276 segments and
   enter no items for them. Now that the lines stand produced in full (§2),
   entering the two comparative items for each reading (Elamite 'an' and
   Sanskrit 'annam/anna') is a Spec 099 builder act; it would move the item
   census from 296 to 298 and belongs with the log's own amendment
   discipline, not with this package — the more so while the L-2 amendment
   (PR #677) is concurrently amending the same log files.
2. **M124's LITERATURE line has no inference-log item** (§8). Same act
   territory as item 1.
3. **A wording consequence for M329's log annotation.** The L-2 amendment
   (PR #677) states that M329's class "rests on the repaired DEDR entry and
   the Elamite leg as filed." After §6 of this package, the Elamite leg
   stands checked and does not support the reading; the class in fact rests
   on the verified DEDR item alone. No class consequence follows, but the
   annotation's wording should be corrected at the next log amendment so the
   record does not carry a leg as load-bearing that this package has shown
   carries nothing.

## 10. The I-20 characterisation

Adjudication unit I-20 also carries a characterisation, recorded here as
directed: where the program's blind coders return codings, their work is
accepted as independent extraction of what a source says, not as independent
support for a reading. No codings have returned; no action arises.

## 11. Coverage and limits

Sources read in this pass, each first-hand: Parpola 1994, *Deciphering the
Indus Script*, held OCR scan (SHA-256
`fd133822f9999c86178a32208465e847c5288b578ad14ca2cd643efe57f0e0b6`), full
text extracted and searched (392 pages, 346,212 words), with the Su-ilishu
passage (printed pp. 131–133) and both sibilant passages read at passage
level in flowing and layout extraction; Parpola 2010, "A Dravidian solution
to the Indus script problem," held recovered text (SHA-256
`c58137e54cdde3f2acdcfaf05293dfc5f5ba33def3e0b12585c451f76bd4ba84`), full
text searched (10,806 words); the restored DEDR tree at its pin
(github.com/moli-mandala/data `d5050e5a9671012df416e9c474c75aba41c07f8c`,
`dedr_new.csv` SHA-256
`fbcc2b2d47c9be24338d846319de2b2c5a2ad4f45451274e3223bc63bc60cae0`), entries
1638, 1651 and 4570 read directly; `reports/phase108_anchor_trails.json`
(the M202 and M330 bases in full); Mahadevan, *Vestiges of Indus Civilisation
in Old Tamil* (RMRL lecture, read in full, 13,421 words); the
Monier-Williams dictionary in its Cologne digital edition (headword anna,
printed p. 45); Hallock 1969 (OIP 92), Glossary of Achaemenid Elamite, read
in full by headword search; Blažek 2015's Elamite basic-vocabulary list
(compiled from Grillot-Susini 1987 and Hinz & Koch 1987), read in full;
Sengupta 2023, *Studia Orientalia Electronica* 11(1), for the Heras/Parpola
attribution of the fish = mīn rebus.

Named unreachable elements, for the record: a clean text of Parpola 1994
(§7); the full text of Hinz & Koch's *Elamisches Wörterbuch* (§6, bur). No
other remainder item is left open: every item itemised in the first pass and
in adjudication unit I-20 is closed above as verified, partially verified,
not verifiable with its unreachable element named, or retired with its
reason.
