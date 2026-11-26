# ELSEWHERE Baseline Template — Meroitic Program

## Spec 106 — ELSEWHERE world-model templates (Glossa-Lab methodology study)

**Frame:** The Kingdom of Kush in its Napatan-to-Meroitic span, as the Meroitic texts require; the corpus is overwhelmingly Meroitic-period, c. 3rd century BCE – 4th century CE.

**What this file is.** The spawn-ready baseline axiom set for this program's ELSEWHERE instances, under the method of `../methodology.md` (Spec 106). Spawning an instance means: copy this baseline, vary the (H) axioms as the test requires (and, for sensitivity tests, drop or vary named (K) axioms), declare the resulting set in full, and run the lifecycle. The baseline itself is never an instance.

**Kind labels.** (F) floor fact, known without a doubt; (K) period knowledge, well supported by the record but revisable, source named; (H) hypothesis, declared openly. A line flagged UNSOURCED may appear only as an (H): it names a variable an instance must declare, not a premise it may use.

**Editorial flag (Spec 106 assembly, 2026-11-25).** Two lines below carry (F) on reference-grade sourcing (MER-GEO-01, MER-GEO-02). They are filed as the census returned them; demoting them to (K) is the first amendment any instance that leans on them should declare.

---

## Seed record (framework §4; provenance standard §9)

- **Study identity.** Glossa-Lab, ELSEWHERE world-model baseline for the Meroitic program; registered as Spec 106 (`specs/106-elsewhere-world-model-templates/`); framework adopted: ELSEWHERE Framework Specification, Version 1 (2026-11-25).
- **Baseline template.** This file, `templates/meroitic-baseline.md`, version 1 (2026-11-25). Axiom census as seeded: 76 axioms in domains 2–8 (GEO 0, POL 0, MOV 0, DNA 0, ECO 0, ENV 0, CON 0), plus Domain 1 (language-internal) carried by reference to Spec 105. By kind: (F) 4, (K) 62, (H) 10. Lines carrying the UNSOURCED flag: 2. SHA-256 over the axiom lines as filed (one per line, in file order): `eeadf46e336fa80d09bcffa2538d3cf4c32c8756fdb6150c817ff0b19cdb4cf4`.
- **The full axiom set as seeded.** The census in this file, domains 2–8, together with Domain 1 by its Spec 105 reference. This file is the seeded set; the hash above pins it.
- **The claim queue as opened.** Empty. Claims enter only by an authorizing act at the reasoning level, recorded in the study's seed-and-iteration log; instances never originate claims.
- **The evidence set.** The Spec 097 corpus (the campaign build pinned by that study) and the fixed epigraphic and archaeological record of the Kingdom of Kush. **Registered contact points:** Spec 105's G-MER validation gate (derived structure checked against Griffith's deciphered sound values, GOOD / NOT-GOOD) for language-internal derivations; the program's registered-study discipline for all results.
- **Date and authorizing order.** Seeded 2026-11-25 under the owner's orders in the Glossa-Lab chat of 2026-11-25 12:39 ET (ELSEWHERE world-model expansion) and 12:44 ET (ELSEWHERE made a formal framework).
- **Log home.** The adopting study's log lives at `records/elsewhere-seed-and-iteration-log.md` in its spec package (framework §9); this seed record is the log's first entry wherever this template is seeded into a study.

---

## Template amendment — version 2 (2026-11-25, Round G unit G-M-1)

The seed record above stands as filed for version 1; this section
versions the template under the framework's iteration protocol
(template versions may change; the seed may not). Version 2 amends
exactly one axiom line:

- **MER-ENV-01 (K)** read in version 1: "The Meroitic language was
  written only during the Kingdom of Meroe, c. 300 BCE – 350 CE,
  though the language itself is attested earlier in Egyptian
  transcriptions of personal names from as early as the second
  millennium BCE." The exclusive "only during" clause is
  incompatible with the template's own MER-ENV-03 (the script
  outlived the fall of Meroe; the latest known text, REM 0094 at
  Kalabsha, is re-dated to 410/450 CE) and MER-MOV-08 ("the last
  Meroitic text is in fact a Blemmye king's inscription"). No
  binding scope rule in the template or the framework confines
  MER-ENV-01 to a kingdom-period subset; the Round G session's
  kill check was run against the template and study records at
  adjudication and was not met. In version 2 the line reads:
  "Meroitic writing is attested during the Kingdom of Meroe,
  c. 300 BCE – 350 CE, and continued after its fall (MER-ENV-03);
  the language itself is attested earlier in Egyptian
  transcriptions of personal names from as early as the second
  millennium BCE." Source unchanged (Rilly 2016).
- **Census unchanged:** 76 axioms; (F) 4, (K) 62, (H) 10;
  UNSOURCED-flag lines 2. **Axiom-line SHA-256, version 2:**
  `ecabd227f7e767a3a740ece3b355d8620db476b89ac482d7a8386b483a97f4f2`,
  recomputed by the method of `records/census-audit.py`
  (TC-106-05), which passes on the amended file. The version 1
  pin (`eeadf46e336fa80d09bcffa2538d3cf4c32c8756fdb6150c817ff0b19cdb4cf4`)
  is retained in the seed record above and in this study's git
  history; no instance has been spawned from either version, so
  no derivation, result, or status is affected. The correction
  is filed before first instantiation, as the unit directed.
- **Authority:** Co-scientist Round G unit G-M-1, sustained
  APPLY at adjudication; `specs/091-anchor-comparison-integrity/records/coscientist-sweep-adjudication-2026-11-25-round-g.md`
  §3.1. Iteration entry: `records/elsewhere-seed-and-iteration-log.md`,
  Iteration 1.

---

## Domain 1 — Language-internal

By reference to Spec 105 (`specs/105-elsewhere-sandbox/`): the corpus floor (distinction, sequence, co-presence, recurrence, boundary, over the recorded token streams as the one declared input assumption) and the derivation ladder L0–L6 with its boundary gates. This template does not duplicate that content; a full instance carries a Spec 105 language derivation inside this world model.

## Domain 2 — Geography (GEO)

- MER-GEO-01 (F) — Kush was centred along the Nile Valley in what is now northern Sudan and southern Egypt, in the Middle Nile corridor. Source: Wikipedia, "Kingdom of Kush" (reference).
- MER-GEO-02 (F) — The Nile in Sudan runs over six groups of cataracts, from the Sixth at Sabaloka just north of Khartoum northward to Abu Hamed, and the First Cataract at Aswan was the traditional border zone between Egypt and Nubia. Source: Sirak et al. 2021, Nature Communications (scholarly, for the First-to-Khulubnarti cataract framing); Wikipedia, "Kingdom of Kush" (reference, for the six-cataract sequence).
- MER-GEO-03 (K) — Meroe stood on the east bank of the Nile, about 200 km north-east of Khartoum, between the Fifth and Sixth Cataracts. Source: Wikipedia, "Meroë" (reference).
- MER-GEO-04 (K) — The "Island of Meroe" of ancient writers is the modern Butana, a region bounded by the Nile (from the Atbara River to Khartoum), the Atbara and the Blue Nile; Meroe stood on its edge, with Musawwarat es-Sufra and Naqa as other major Meroitic centres in the Butana. Source: Wikipedia, "Meroë" (reference).
- MER-GEO-05 (K) — Napata lay far north of Meroe at the foot of Gebel Barkal, near modern Karima, below the Fourth Cataract, and remained the great Amun centre after the royal seat moved south. Source: Wikipedia, "Kingdom of Kush" (reference); Wikipedia, "Meroë" (reference, Napata retained for the Amun Temple).
- MER-GEO-06 (K) — At its peak the rulers of Meroe controlled the Nile Valley north to south over a straight-line distance of more than 1,000 km. Source: Wikipedia, "Meroë" (reference).
- MER-GEO-07 (K) — Meroe's position was chosen in part because it sat on the fringe of the summer rainfall belt, unlike the purely riverine north, allowing rainland as well as floodplain subsistence. Source: Wikipedia, "Meroë" (reference, citing Martin Meredith).
- MER-GEO-08 (K) — The Nile's Great Bend, where the river turns south-west through the Bayuda Desert between Abu Hamed and Al Dabbah, made desert shortcut routes across the Bayuda an alternative to following the river's long loop. Source: Wikipedia, "Kingdom of Kush" via search-result reading (reference); the Great Bend course is also shown in Sirak et al. 2021, Nature Communications (scholarly).
- MER-GEO-09 (K) — The Wadi Howar, the remnant of the ancient Yellow Nile, ran west-east for over 1,100 km across the southern Libyan Desert to join the Nile north of the Great Bend opposite Old Dongola, and in prehistory served as a communication route between inner Africa and the Nile Valley. Source: Wikipedia, "Wadi Howar" via search-result reading (reference).
- MER-GEO-10 (K) — The lower Wadi Howar held a Napatan-period Kushite fortress, Gala Abu Ahmed, about 110 km west of the Nile, showing Kushite state presence on the desert route west in the Napatan phase (c. 750–350 BCE). Source: Wikipedia, "Wadi Howar" via search-result reading (reference).
- MER-GEO-11 (K) — Meroe's location also afforded access to trade routes toward the Red Sea, east across the desert from the Nile–Atbara region. Source: Wikipedia, "Meroë" (reference).
- MER-GEO-12 (H) — Precise political borders of the Meroitic kingdom, especially to the south and into the Butana interior, are not fixed by the record; the Antiquity isotope study states the kingdom's actual boundaries remain a matter of speculation while its focus was the Nile and its tributaries. Source: Kozieradzka-Ogunmakin & Sołtysiak 2023, Antiquity (scholarly).

## Domain 3 — Politics and administration (POL)

- MER-POL-01 (K) — Kush re-emerged as an independent kingdom centred at Napata after Egypt's New Kingdom disintegrated around 1070 BCE, and Kushite kings later ruled Egypt as the Twenty-fifth Dynasty in the 8th–7th centuries BCE. Source: Wikipedia, "Kingdom of Kush" (reference).
- MER-POL-02 (K) — King Aspelta moved the capital to Meroe, considerably farther south than Napata, possibly c. 591 BCE, just after the sack of Napata by the Egyptian pharaoh Psamtik II; royal burials transferred to Meroe around 300 BCE under Arakamani. Source: Wikipedia, "Meroë" (reference).
- MER-POL-03 (K) — Napata did not disappear when the seat moved: it retained religious importance, above all the Amun temple at Gebel Barkal, which was venerated as the residence of Amun and an essential symbol of Kushite kingship. Source: Wikipedia, "Kingdom of Kush" (reference); Wikipedia, "Meroë" (reference).
- MER-POL-04 (K) — Kushite kingship was Amun-centred and Egyptianising in form — pharaonic titles, Amun worship, monumental building and royal burial forms adapted from Egypt — while remaining a distinct Nubian political culture. Source: Wikipedia, "Kingdom of Kush" (reference).
- MER-POL-05 (K) — The king of Meroe was an autocratic ruler who shared authority with the Queen Mother, or Kandake; the administration is described as including treasurers, seal bearers, heads of archives and chief scribes. Source: Wikipedia, "Meroë" (reference).
- MER-POL-06 (K) — The kandake was not merely a consort title: Amanirenas bore both qore (ruler) and kandake, and Shanakdakhete (c. 170–150 BCE) is shown as a ruling queen of Meroe in her own right. Source: Wikipedia, "Amanirenas" via search-result reading (reference); Wikipedia, "Meroë" (reference, for Shanakdakhete).
- MER-POL-07 (K) — In 25/24 BCE Kushite forces under Amanirenas struck Roman Egypt at Syene, Philae and Elephantine and carried off statues of Augustus, one bronze head of which was later buried under temple steps at Meroe. Source: Wikipedia, "Meroë" (reference); Wikipedia, "Amanirenas" via search-result reading (reference).
- MER-POL-08 (K) — The Roman prefect Gaius Petronius counter-invaded, defeated Kushite forces, took Primis (Qasr Ibrim) and sacked Napata (dated 23/22 BCE in the sources used), but did not hold the far south. Source: Wikipedia, "Meroë" (reference); Wikipedia, "Amanirenas" via search-result reading (reference).
- MER-POL-09 (K) — The war ended in a peace treaty negotiated with Augustus at Samos in 21/20 BCE, strikingly favourable to Meroe: the Romans evacuated the southern part of the Thirty-Mile Strip including Primis and the Meroites were exempted from tribute, while Rome kept the Dodekaschoinos as a border zone with the frontier near Hiere Sycaminos (Maharraqa). Source: Wikipedia, "Amanirenas" via search-result reading (reference, citing Hintze 1978).
- MER-POL-10 (K) — That frontier arrangement held, with generally peaceful Rome–Meroe relations, until the end of the 3rd century CE. Source: Wikipedia, "Amanirenas" via search-result reading (reference).
- MER-POL-11 (K) — Lower Nubia was administered provincially: Karanog was probably a provincial capital under its own peshto (princely governor) in the 2nd and 3rd centuries CE, with excavated peshto palace complexes. Source: Penn Museum Expedition, "Karanog, Wealthy Capital of a Lower Nubian Province" via search-result reading (museum / scholarly-popular); Wikipedia, "Karanog" via search-result reading (reference).
- MER-POL-12 (H) — How uniformly and bureaucratically the Meroitic centre actually controlled Lower Nubia and the provinces, as opposed to ruling through local title-holding elites whose loyalty was newly emphasised in the last century BCE, is debated; the Egyptian-style uniform-bureaucracy model has been specifically questioned. Source: Edwards-tradition discussion in "The Confluence of History and Archaeology in Lower Nubia" via search-result reading (scholarly).

## Domain 4 — People movement (MOV)

- MER-MOV-01 (K) — Nubia was a long-standing corridor where people from sub-Saharan Africa, Egypt and West Eurasia interacted, and Nubia and Egypt had a dynamic relationship for more than 6,000 years before the Christian period. Source: Sirak et al. 2021, Nature Communications (scholarly).
- MER-MOV-02 (K) — Under the New Kingdom (c. 1550–1070 BCE) much of Nubia came under Egyptian rule, governed by a Viceroy of Kush, with Egyptian temples, garrisons and settlement implanted in the Middle Nile. Source: Wikipedia, "Kingdom of Kush" (reference).
- MER-MOV-03 (K) — The royal families of Kush and Egypt occasionally intermarried, even though Kushite culture, language and ethnicity remained distinct and Egyptian art distinguished Kushites by dress and appearance. Source: Wikipedia, "Kingdom of Kush" (reference).
- MER-MOV-04 (K) — Kashta's daughter Amenirdis was appointed Divine Adoratrice of Amun in Thebes, and Piye's daughter Shepenupet II held the same office, placing Kushite royal women inside Egypt's chief Amun institution during the Twenty-fifth Dynasty. Source: Wikipedia, "Kingdom of Kush" (reference).
- MER-MOV-05 (K) — In the 3rd century BCE to 3rd century CE the northernmost part of Nubia (the Dodekaschoinos) was occupied first by Ptolemaic and then by Roman Egypt, and was only taken back by the Kushite king Yesebokheamani at the end of that period. Source: Wikipedia, "Kingdom of Kush" (reference).
- MER-MOV-06 (K) — Rilly's linguistic model has Northern East Sudanic speech communities spreading with the desiccation of the Wadi Howar / Yellow Nile system, with Nubian speech communities later moving from western Sudan into the Nile Valley. Source: Rilly, "The Wadi Howar Diaspora" (Brill, Frontiers of the Roman World / Sudan studies) via search-result reading (scholarly); Dimmendaal 2023, UCLA Encyclopedia of Egyptology via search-result reading (scholarly).
- MER-MOV-07 (K) — At the kingdom's end the Noba people moved into the Nile Valley, introduced the Nubian languages, and gave their name to Nubia; Meroitic was superseded by Nubian, the language of a new elite originating from western Sudan. Source: Wikipedia, "Kingdom of Kush" (reference); Rilly 2016, UCLA Encyclopedia of Egyptology (scholarly).
- MER-MOV-08 (K) — The Blemmyes, from the Eastern Desert, were at war with the Kushites in the kingdom's final phase and held Lower Nubian centres such as Kalabsha in the post-Meroitic period; the last Meroitic text is in fact a Blemmye king's inscription (see MER-ENV-03). Source: Wikipedia, "Kingdom of Kush" (reference); Rilly 2016, UCLA Encyclopedia of Egyptology (scholarly).
- MER-MOV-09 (K) — Diocletian is reported to have entrusted the Nobatae in 296 CE with defence of the southern Egyptian frontier, placing a Nubian-speaking group on Rome's border before Meroe fell. Source: Poznań Museum, "Post-Meroitic Period and X-Group" via search-result reading (museum).
- MER-MOV-10 (H) — Whether Aksum destroyed Meroe or only campaigned through an already collapsing kingdom is unresolved: Ezana's inscriptions record a campaign along the Atbara to the Nile against the Noba and the Kasu (Kush), Meroe itself is not mentioned in Ezana's text, and some authorities read other inscriptions as proof of destruction while archaeological evidence points to decline around 300 CE. Source: Wikipedia, "Kingdom of Kush" (reference); Wikipedia, "Meroë" (reference).

## Domain 5 — DNA and population (DNA)

**This domain is essentially empty for Meroitic Kush, and the census says so plainly: as of the sources opened, there is no published genome-wide ancient DNA from a Meroitic-period (c. 300 BCE – 350 CE) Kushite individual. Every axiom below is either about that gap or about a neighbouring period, labeled at the resolution the papers support. No Meroitic-period genetic claim should be spawned from this domain.**

- MER-DNA-01 (K) — Before the Kulubnarti study, only three ancient genome-wide samples existed for the entire Nile Valley, all from Egypt. Source: Sirak et al. 2021, Nature Communications (scholarly); Emory News report of the same study via search-result reading (university press).
- MER-DNA-02 (K) — The first genome-wide ancient DNA from Sudan is from Kulubnarti, between the Second and Third Cataracts, and dates to the Christian period, c. 650–1000 CE — roughly 300 to 650 years after Meroe fell — not to the Meroitic period. Source: Sirak et al. 2021, Nature Communications (scholarly).
- MER-DNA-03 (K) — The Kulubnarti sample is 66 individuals from two cemeteries, raising the Nile Valley ancient genome-wide total from 3 to 69. Source: Sirak et al. 2021, Nature Communications (scholarly).
- MER-DNA-04 (K) — Kulubnarti individuals carried on average about 43% Nilotic-related ancestry (individual range about 36–54%), with the remaining ancestry consistent with introduction through Egypt and ultimately resembling a Bronze and Iron Age Levant-related pool. Source: Sirak et al. 2021, Nature Communications (scholarly).
- MER-DNA-05 (K) — The Kulubnarti gene pool was shaped over at least a millennium of admixture and carries disproportionately female-associated West Eurasian-related ancestry, suggesting female mobility was important in shaping it. Source: Sirak et al. 2021, Nature Communications (scholarly).
- MER-DNA-06 (K) — The two socially differentiated Kulubnarti cemeteries were not genetically distinct, and seven pairs of inter-cemetery relatives as close as second-degree show fluidity across the social divide. Source: Sirak et al. 2021, Nature Communications (scholarly).
- MER-DNA-07 (K) — Present-day Nubians are not directly descended from the Kulubnarti Nubians without additional admixture, so even the Christian-period genomes cannot be read straight back onto Meroitic-period Kushites. Source: Sirak et al. 2021, Nature Communications (scholarly).
- MER-DNA-08 (H) UNSOURCED — Any statement about the genetic ancestry, relatedness or population structure of Meroitic-period Kushites themselves is currently a hypothesis with no published genome-wide ancient-DNA source behind it, and is flagged UNSOURCED by construction in this census.

## Domain 6 — Material economy (ECO)

- MER-ECO-01 (K) — Iron production was practised in the Meroe region for more than 1,000 years, potentially starting as early as the Twenty-fifth Dynasty period, on the evidence of 97 radiocarbon dates from slag-mound investigations at Meroe and Hamadab. Source: Humphris & Scheibner 2017, African Archaeological Review (scholarly, open access via Springer).
- MER-ECO-02 (K) — Large slag heaps at Meroe led Sayce in 1912 to call Meroe "the Birmingham of ancient Africa," a characterisation that entered the literature on very little excavated evidence. Source: Humphris & Scheibner 2017, African Archaeological Review (scholarly).
- MER-ECO-03 (H) — The scale and centrality of Meroitic iron production — gigantic and export-supplying, versus substantial but local and episodic — is debated: the famous early dates (including a late-6th-century BCE date) were cautioned by their own publishers, few in-situ furnaces have been found relative to the slag heaps, and the new chronology was built precisely because scale over time was unsettled. Source: Humphris & Scheibner 2017, African Archaeological Review (scholarly); Charlton & Humphris 2017 experimental study via search-result reading (scholarly).
- MER-ECO-04 (K) — Meroe traded ivory, slaves, rare skins, ostrich feathers, copper and ebony, exported textiles and jewellery, and Nubia was very rich in gold, worked and traded through Kushite channels from the eastern desert borderlands. Source: Wikipedia, "Meroë" (reference); UNESCO General History of Africa chapter via search-result reading (scholarly-popular, for gold between the Nile and Red Sea, mainly north of the 18th parallel).
- MER-ECO-05 (K) — Kushite cotton textiles reached their highest achievement in Nubia around 400 BCE in the chronology the Meroe article reports, and cotton was a Meroitic export and temple / royal fabric. Source: Wikipedia, "Meroë" (reference).
- MER-ECO-06 (K) — Animal husbandry dominated over crop agriculture in the Napatan–Meroitic economy as described in the UNESCO history, cotton was cultivated earlier in Kush than in Egypt, and agricultural produce was largely for local consumption rather than export. Source: UNESCO General History of Africa chapter via search-result reading (scholarly-popular).
- MER-ECO-07 (K) — Butana settlement was savannah-oriented, mixing permanent and less permanent agricultural settlements exploiting rainlands, with large-scale livestock farming enabled by hafir water storage away from the Nile. Source: Wikipedia, "Meroë" (reference); Kozieradzka-Ogunmakin & Sołtysiak 2023, Antiquity (scholarly, for hafirs, saqia and livestock expansion).
- MER-ECO-08 (K) — After Petronius's expedition the Meroe sites show abundant Roman-period trade finds, and Meroe is mentioned in the 1st-century CE Periplus of the Erythraean Sea, placing it on the edge of the Red Sea trading world. Source: Wikipedia, "Meroë" (reference).
- MER-ECO-09 (K) — About 70 Meroitic ostraca, predominantly short texts with numbers, are the evident traces of administrative and commercial activity — accounting exists in the record, but only at this thin resolution. Source: Rilly 2016, UCLA Encyclopedia of Egyptology (scholarly).
- MER-ECO-10 (H) — No Meroitic system of weights, measures, prices or coinage can be censused at usable resolution from the sources opened; Kush is not shown striking its own coinage, and any axiom giving Meroitic units, tariffs or price levels would be UNSOURCED. Source: absence noted against Rilly 2016, UCLA Encyclopedia of Egyptology (scholarly) and the program records read — flagged as a gap, not a positive claim.

## Domain 7 — Environment and chronology (ENV)

- MER-ENV-01 (K) — Meroitic writing is attested during the Kingdom of Meroe, c. 300 BCE – 350 CE, and continued after its fall (MER-ENV-03); the language itself is attested earlier in Egyptian transcriptions of personal names from as early as the second millennium BCE. Source: Rilly 2016, UCLA Encyclopedia of Egyptology (scholarly).
- MER-ENV-02 (K) — Meroitic texts are not attested in great numbers before the end of the 2nd century BCE; the bulk of the corpus extends from the last decades BCE to the 4th century CE, and the earliest cursive specimens are pilgrims' graffiti from Kawa and Dukki Gel dated to the beginning of the 2nd century BCE. Source: Rilly 2016, UCLA Encyclopedia of Egyptology (scholarly).
- MER-ENV-03 (K) — The script outlived the fall of Meroe (c. 350 CE): the latest known text is the inscription of the Blemmye king Kharamadoye at Kalabsha (REM 0094), re-dated to 410/450 CE. Source: Rilly 2016, UCLA Encyclopedia of Egyptology (scholarly); Wikipedia, "Meroitic script" (reference).
- MER-ENV-04 (K) — The REM (Répertoire d'épigraphie méroïtique) corpus as published includes some 1,300 texts, with approximately 900 further unpublished examples, mainly from Qasr Ibrim and Musawwarat es-Sufra — over 2,000 inscriptions in total known from northern Sudan and Egyptian Nubia. Source: Rilly 2016, UCLA Encyclopedia of Egyptology (scholarly).
- MER-ENV-05 (K) — Half of the published REM corpus consists of funerary texts on stelae or offering tables; the longest documents are royal inscriptions (no more than about two dozen recovered), alongside temple captions, some 250 graffiti, amuletic texts, and the ostraca of MER-ECO-09. Source: Rilly 2016, UCLA Encyclopedia of Egyptology (scholarly).
- MER-ENV-06 (K) — In the program's own held corpus the formulaic skew is sharper still: the campaign build held 396 inscriptions / 368 distinct texts, and in its held-out partition funerary texts dominated (16 funerary against 5 documents and 2 graffiti). Source: Glossa-Lab gap analysis 2026-11-25 and SCOPE-meroitic.md, Spec 097 record (program records).
- MER-ENV-07 (K) — Life in the corridor depended on the Nile flood regime and, away from the river, on stored rainwater: hafirs (large reservoirs, the Great Hafir at Musawwarat es-Sufra being 250 m across) caught the short wet season's rain for dry-season water, fields and cattle. Source: Wikipedia, "Kingdom of Kush" (reference); Weschenfelder on Meroitic water management via search-result reading (scholarly).
- MER-ENV-08 (K) — The Butana in antiquity was semi-arid savannah between the Nile, Blue Nile and Atbara; its modern semi-arid desert character may reflect soil degradation processes rather than a simple large drop in rainfall. Source: Weschenfelder on Meroitic water management via search-result reading (scholarly, citing Berking & Schütt; Näser & Scheibner).
- MER-ENV-09 (K) — Isotope evidence (carbon and oxygen in dental enamel from 13 cemeteries) shows a shift toward more arid conditions toward the end of the Meroitic kingdom and into the post-Meroitic period, with associated changes in agricultural practice and land use. Source: Kozieradzka-Ogunmakin & Sołtysiak 2023, Antiquity (scholarly).
- MER-ENV-10 (H) — Whether that aridification, rather than political and economic instability, materially caused the kingdom's dissolution is debated; the isotope authors present it as a possible contribution, and the older literature treats geo-political and economic instability and social unrest as prime contributors. Source: Kozieradzka-Ogunmakin & Sołtysiak 2023, Antiquity (scholarly).
- MER-ENV-11 (H) — The older claim that charcoal-burning for iron smelting stripped the Butana of forest and thereby degraded Meroe's environment is repeated in general accounts but is not established at the resolution of the archaeometallurgical literature opened here, which treats the early iron narrative as evidence-poor. Source: Wikipedia, "Kingdom of Kush" via search-result reading (reference, for the claim); Humphris & Scheibner 2017, African Archaeological Review (scholarly, for the evidential caution).

## Domain 8 — Language contact (CON)

- MER-CON-01 (F) — Meroitic was written in two scripts, cursive and hieroglyphic, both derived from Egyptian scripts, sharing one alphasyllabic system of 23 signs plus a word-divider of two or three dots. Source: Rilly 2016, UCLA Encyclopedia of Egyptology (scholarly).
- MER-CON-02 (F) — The scripts' sound values were deciphered in 1907–1911 by Francis Llewellyn Griffith, largely through royal and Egyptian names written in both Meroitic and Egyptian; the language itself remains only partly understood, with no more than about a hundred words translated with some certainty in Rilly's 2016 summary. Source: Rilly 2016, UCLA Encyclopedia of Egyptology (scholarly).
- MER-CON-03 (K) — The cursive script is an offshoot of a local form of early Demotic Egyptian, the hieroglyphic signs derive from Egyptian hieroglyphs (partly recycling signs already used to transcribe 25th-Dynasty and Napatan names), cursive came first, and the hieroglyphic form was a later deliberate monumental invention, first attempted around 100 BCE. Source: Rilly 2016, UCLA Encyclopedia of Egyptology (scholarly).
- MER-CON-04 (K) — Cursive makes up about 90% of the corpus and was used for almost everything including royal chronicles; hieroglyphic was nearly exclusive to the royal sphere in connection with the cult of the gods. Source: Rilly 2016, UCLA Encyclopedia of Egyptology (scholarly); Wikipedia, "Meroitic script" (reference).
- MER-CON-05 (K) — Before Meroitic writing, Egyptian was the written language of Kush: Egyptian hieroglyphs wrote Kushite names and lexical items through the Napatan period, and many Meroitic titles eventually understood are Egyptian borrowings. Source: Wikipedia, "Meroitic script" (reference); Rilly 2016, UCLA Encyclopedia of Egyptology (scholarly, for borrowed titles and Egyptian loanwords as decipherment anchors).
- MER-CON-06 (K) — There are no real bilingual texts for Meroitic; progress since Griffith has rested on Egyptian loanwords, divine and royal names, and iconographic context — the name-equation route, not a Rosetta-style parallel text. Source: Rilly 2016, UCLA Encyclopedia of Egyptology (scholarly).
- MER-CON-07 (K) — At the northern frontier Meroitic speakers lived alongside Greek- and Latin-using Ptolemaic and Roman Egypt for six centuries; Greek and Roman authors (Strabo, Pliny, the Periplus) are external witnesses to Kush, and Ezana's later inscriptions in the region are in Greek and Ge'ez. Source: Wikipedia, "Kingdom of Kush" (reference); Wikipedia, "Meroë" (reference).
- MER-CON-08 (K) — Meroitic left no descendant language and disappeared, presumably in the early Middle Ages, superseded by Nubian. Source: Rilly 2016, UCLA Encyclopedia of Egyptology (scholarly).
- MER-CON-09 (K) — Old Nubian, the written language of the successor Christian kingdoms, is attested from the 8th century CE, was written in a Coptic-derived alphabet that retained three Meroitic cursive letters, and belongs to the Nubian branch of Nilo-Saharan (Eastern Sudanic) — outside evidence about the region's later language, not evidence about Meroitic itself. Source: Wikipedia, "Meroitic script" (reference, for the three retained letters); EBSCO / Dimmendaal 2023 via search-result reading (scholarly / reference, for Old Nubian's date and classification).
- MER-CON-10 (K) — Rilly's affiliation case (Rilly 2010, Le méroïtique et sa famille linguistique; Rilly & de Voogt 2012) places Meroitic in Northern East Sudanic, a branch of East Sudanic within Nilo-Saharan, alongside Nubian, Nara, Taman and Nyima, on lexical and morphological correspondences (e.g. Meroitic kdite "sister" beside Proto-Nubian *kedidi and Proto-Nara *kadete). Source: Rilly 2016, UCLA Encyclopedia of Egyptology (scholarly).
- MER-CON-11 (H) — That affiliation, although presented by Rilly as established and recognised by prominent Nilo-Saharanists, is contested in print: Lipiński (2011) argued most of Rilly's c. 50 secure words look Afroasiatic, and Rowan (2006, 2011) argued Meroitic phonotactics pattern with Afroasiatic and against Nilo-Saharan; general classifications still list Meroitic as unclassified / possibly Nilo-Saharan or Afroasiatic. Source: Lipiński 2011 review article via search-result reading (scholarly); Wikipedia, "Meroitic language" via search-result reading (reference).
- MER-CON-12 (H) — Earlier alternatives remain on the record as hypotheses, not settlements: Trigger (1964) first proposed the East Sudanic link on partly erroneous data and Hintze rejected a positive conclusion in his lifetime and treated Meroitic as effectively isolate-like; Bender (1981, "The Meroitic problem") framed the classification as an open problem, and Behrens / Bechhaus-Gerst argued the earlier Nile Valley populations (C-Group, Kerma) spoke Afroasiatic languages, which would change the substrate picture under Meroitic. Source: Rilly, "The Wadi Howar Diaspora" via search-result reading (scholarly, for Trigger / Hintze); Wikipedia, "Meroitic language" via search-result reading (reference, for Bender); Wikiwand "Nubians" summary of Behrens / Bechhaus-Gerst via search-result reading (reference).
- MER-CON-13 (K) — The Glossa-Lab program's own registered affiliation test of the Nubian/Nara (Northern East Sudanic) hypothesis returned UNDECIDABLE AT THIS POWER (4 of 12 concepts, p = 0.0326 against a bar of p < 0.01 with a margin condition), so for program purposes the affiliation is an open hypothesis regardless of the field's centre of gravity. Source: Glossa-Lab gap analysis 2026-11-25 (program record).

---

---

## The most consequential (H) axioms

1. **MER-ECO-03 — the scale and centrality of iron production at Meroe.** If iron was gigantic and export-oriented, Meroe was an industrial centre whose charcoal demand, labour organisation and trade reach structure the whole world model; if it was substantial but local and episodic, the economy re-centres on cattle, gold and transit trade. The slag heaps are real either way; the spawning instance must not silently pick the "Birmingham of Africa" version.
2. **Spoken-language unity vs regional diversity under one written standard (H, UNSOURCED as a positive claim).** The census holds no axiom asserting that one spoken Meroitic was uniform from the First Cataract to the Butana. The written standard is uniform and formulaic, but the kingdom ruled Lower Nubian peshto provinces, Butana pastoralists and Eastern Desert neighbours (Blemmyan is listed among the kingdom's languages in general references), so a single spoken language across the kingdom is an assumption an ELSEWHERE instance would be smuggling in. Flagged here as consequential precisely because it is unaxiomised: spawn it as an open variable, not a default. Source for the caution: Wikipedia, "Kingdom of Kush" (reference, listing Meroitic, Egyptian, Blemmyan and Old Nubian as the kingdom's languages); Rilly 2016 (scholarly, corpus is a written standard).
3. **MER-ENV-10 / MER-GEO-12 combined — the Butana's period habitability and the kingdom's real extent.** Whether the Butana heartland was a well-watered savannah sustained by royal hafir management that later degraded (by climate shift, by soil degradation, or by over-exploitation), or a marginal zone always held thinly from the river, decides how much of Kush lived off the Nile at all — and the isotope aridification signal (MER-ENV-09) is new enough that its causal weight is still a hypothesis.

Note, per the task frame: the Meroitic affiliation question itself (MER-CON-10 / MER-CON-11) is a language-program claim and is therefore deliberately *not* counted among these world-model H's, even though it is the program's largest open question.

## Domains too thin to census honestly

- **DNA (Domain 4) is too thin to census for the Meroitic period at all.** There is no published Meroitic-period genome-wide ancient DNA in the sources opened. The domain above censuses only the gap and one Christian-period Nubian study (Kulubnarti, c. 650–1000 CE) at its own period's resolution. Any ELSEWHERE instance needing Meroitic-period population genetics has no axioms to spawn from and must treat the variable as unknown.
- **Weights, measures, prices and accounting (within ECO) are too thin for axioms.** The record opened supports only MER-ECO-09 (c. 70 mostly numeric ostraca as traces of administration / commerce) and the negative flag MER-ECO-10. No unit, tariff, wage or price axiom is offered.
- **Provincial administration below the peshto level (within POL) is thin.** One office (peshto) and a generic list (treasurers, seal bearers, heads of archives, chief scribes, from a general reference) are all the opened record supports; office-by-office axioms for other Meroitic titles were dropped rather than padded, because the c. 100 securely translated words include several titles (Rilly 2016) but the pages opened did not enumerate them with functions.

---

*Drafted 2026-11-25 for Spec 106. Sources opened in this pass: Rilly 2016 (UEE, scholarly, full text); Sirak et al. 2021, Nature Communications (scholarly, full text); Humphris & Scheibner 2017, African Archaeological Review via Springer (scholarly, full text); Kozieradzka-Ogunmakin & Sołtysiak 2023, Antiquity (scholarly, full text); Wikipedia "Kingdom of Kush", "Meroë", "Meroitic script" (reference, full text); Glossa-Lab gap analysis 2026-11-25 and SCOPE-meroitic.md (program records, full text). Further scholarly items (Rilly's Wadi Howar paper, Lipiński 2011, Weschenfelder on water management, Penn Museum on Karanog, Dimmendaal 2023) were read at search-result depth and are labeled as such at each citation. Rilly & de Voogt 2012 and Rilly 2010 could not be opened in full in this pass (paywalled / purchase-gated — the same access gap the program record names); their contents are cited only as summarised in Rilly 2016 and the program records.*

---

## Erratum (2026-11-26) — seed-record domain counts (Round N unit N-E-2)

The seed record above (the **Baseline template** line) states
the domain census as "GEO 0, POL 0, MOV 0, DNA 0, ECO 0,
ENV 0, CON 0". Those zeroes are false metadata: they are not
the counts of this file's axiom lines. Recomputed from the
axiom lines as filed (domains 2–8), the census as seeded is:

**GEO 12, POL 12, MOV 10, DNA 8, ECO 10, ENV 11, CON 13 — 76 axioms in total.**

Erratum census (machine-readable, for
records/census-audit-v2.py): GEO 12, POL 12, MOV 10, DNA 8, ECO 10, ENV 11, CON 13.

No axiom line is added, removed, or altered by this erratum;
the SHA-256 over the axiom lines as filed recomputes
unchanged: `ecabd227f7e767a3a740ece3b355d8620db476b89ac482d7a8386b483a97f4f2` (the version 2 axiom-line hash; version 1's was `eeadf46e336fa80d09bcffa2538d3cf4c32c8756fdb6150c817ff0b19cdb4cf4`). The historical seed record is preserved
unedited above; this erratum supersedes its domain-count
figures only. The same zero-count defect stood in all three
baseline templates' seed records; parallel errata of the
same date correct the other two. The registered audit's
failure to catch the defect (TC-106-05's per-domain
comparison was never implemented in version 1) is recorded
in the Round N adjudication,
`specs/091-anchor-comparison-integrity/records/coscientist-sweep-adjudication-2026-11-26-round-n.md`
§3.2, and the corrected audit is
`records/census-audit-v2.py`.

