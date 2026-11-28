# Spec 111 — Evaluation Record (2026-11-27)

The full evaluation. Hypothesis H and predictions
P1–P4 as registered in spec.md §§1–2; grading scale
as spec.md §3. Every factual claim carries a checkable
citation. Scholarly-status labels are stated as labels:
where a claim about old writing is contested, the
record says who claims it, who disputes it, and what
the mainstream standing is — it does not launder a
contested claim into a fact in either direction.

## 1. The standard chronology the predictions are graded against

Writing is first securely attested in the late fourth
millennium BCE, in two places with documented local
developmental precursors: Mesopotamia (proto-cuneiform
at Uruk, c. 3400–3300 BCE, preceded by a millennia-long
token and numerical-tablet tradition) and Egypt
(inscribed labels from tomb U-j at Abydos, c. 3320
BCE, inside a developing tag-and-sign practice)
(Houston, Baines & Cooper 2003, "Last Writing:
Script Obsolescence in Egypt, Mesopotamia, and
Mesoamerica", Comparative Studies in Society and
History 45(3):430–479). No writing system anywhere is
securely dated earlier. The catastrophe horizon the
owner's directive evokes — the Younger Dryas interval
of abrupt climate change, flooding, and biomass
burning, c. 12,900–11,700 years ago — therefore
precedes the first attested writing anywhere by more
than eight thousand years; any transmission from that
horizon to the first attested scripts must cross that
gap without leaving a single securely dated written
artifact in it. That gap is not itself a grade; it is
the distance each prediction below has to travel.

## 2. P1 — Cross-system inheritance: NOT SUPPORTED

### 2.1 What the documented derivations show

Each of the three systems has a documented origin, and
the three origins are different, local, and mutually
unrelated:

- **Meroitic** was created in the Kingdom of Kush by
  adapting Egyptian scripts: its hieroglyphic form
  takes its sign forms from Egyptian hieroglyphs and
  its cursive form from Egyptian demotic, with sign
  values assigned to write the Meroitic language
  (Rilly & de Voogt 2012, The Meroitic Language and
  Writing System, Cambridge University Press — the
  program's own Spec 102 source). The script's
  decipherment by F. Ll. Griffith (1911, Karanòg: The
  Meroitic Inscriptions of Shablûl and Karanòg) rested
  on exactly this Egyptian derivation plus proper
  names known from Egyptian and classical sources.
  Before the Meroitic script existed, Kush had written
  Egyptian for centuries (the Napatan royal
  inscriptions are in Egyptian language and scripts),
  so the Meroitic script's appearance is a documented
  act of adaptation inside a literate tradition, not
  an inheritance from an unknown source.
- **The Cypriot syllabary** (the script of the
  Eteocypriot texts) descends from Cypro-Minoan, the
  Bronze Age Cypriot script attested from roughly the
  16th to the 11th century BCE, itself derived from
  the Linear A tradition of Crete (Steele 2013, A
  Linguistic History of Ancient Cyprus, CUP, ch. 1–2;
  Ferrara 2012, Cypro-Minoan Inscriptions, Vol. 1:
  Analysis, OUP). The lineage is continuous on one
  island: Cypro-Minoan sign forms develop into the
  later syllabary's forms across the Late Bronze Age /
  Iron Age transition, with the Paphian and common
  syllabaries as its regional outcomes (Masson 1983,
  Les inscriptions chypriotes syllabiques, 2nd ed. —
  the program's ICS source).
- **The Indus script** has no demonstrated external
  parent. Its antecedents are local (§3.1), and no
  sign-form or structural correspondence with either
  the Cypriot or the Meroitic line has ever been
  demonstrated in the scholarly literature. Where
  Indus signs resemble signs elsewhere, the
  resemblances are of the kind simple geometric and
  pictorial forms produce independently (crosses,
  circles, stick figures, fish), which is what P1's
  "beyond what chance and independent invention
  predict" clause excludes.

A common-descent pattern would require the three
systems to share derived features traceable to one
ancestor. What the record shows instead is three
separate derivations — from Egyptian, from the Aegean
linear tradition, and from local Indus antecedent
marks — with no shared derived feature set among
them. That is the observation P1 says should not
happen, present in full.

### 2.2 Numerical practices

The three systems' numerical practices likewise do
not align: the Indus counted signs of Spec 109 Stage
2's filed census ({M012, M059, M391}; stroke-series
runs number exactly 4 in the whole corpus, each of
length 2 — a tally-like practice); Meroitic numerals
follow the Egyptian-derived additive pattern of its
parent scripts (Rilly & de Voogt 2012); the Cypriot
syllabic tradition writes numbers with separate
numerical signs in the Aegean-derived manner. No
shared numerical convention beyond the universal
tally principle (repeated strokes for repeated units)
is attested — and the tally principle is the textbook
case of independent invention.

### 2.3 The distributional leg (measurement run in this spec)

Filed harness `records/p1-measurement-harness.py`,
raw output `records/p1-measurement-raw-output.json`
(SHA-256 6022f09a…), run 2026-11-27 on tower-compute,
payload exit 0. Structural profiles were computed
from the Spec 105 custody token streams (Indus
derivation set; Eteocypriot sandbox stream; Meroitic
sandbox stream) and the program's deciphered control
(Latin: the Spec 107 donor text, Caesar, De Bello
Gallico, Gutenberg #218, sentences as texts, letters
as signs), plus a synthetic null matched to the Indus
text lengths (seed 11101). Six declared features:
inventory size, mean text length, unigram entropy,
bigram conditional entropy, hapax fraction, and the
positional-restriction share of measurable signs
(dominant position share ≥ 0.90 among signs with ≥ 5
tokens, the Spec 109 Stage 2 construction).

Profiles (texts / tokens / inventory / mean length /
H1 bits / conditional entropy bits / hapax /
positional share):

- Indus: 1,336 / 5,611 / 372 / 4.20 / 6.27 / 3.98 /
  0.223 / 0.841
- Eteocypriot: 14 / 69 / 35 / 4.93 / 4.89 / 0.86 /
  0.514 / 1.000 (1 measurable sign — see limits)
- Meroitic: 5,195 / 29,843 / 32 / 5.74 / 4.14 / 2.82 /
  0.000 / 0.219
- Latin control: 972 / 138,622 / 27 / 142.6 / 4.05 /
  3.51 / 0.000 / 0.960
- Synthetic null: 1,336 / 5,611 / 323 / 4.20 / 6.19 /
  4.47 / 0.189 / 0.021

Standardized (z-scored) Euclidean distances: within
the trio, Indus–Eteocypriot 3.923, Indus–Meroitic
3.774, Eteocypriot–Meroitic 3.760 (mean **3.819**).
Trio-to-controls: Indus–Latin 4.258, Indus–null 2.087,
Eteocypriot–Latin 4.345, Eteocypriot–null 4.718,
Meroitic–Latin **3.130**, Meroitic–null 3.321 (mean
**3.643**). The three systems do not sit closer to
each other than they sit to the controls; the single
closest pair involving a program system is
Meroitic–Latin — two scripts of the alphabetic type,
which is the resemblance independent invention of
small-inventory phonetic scripts predicts. **The
distributional leg finds no common-descent signal.**

Limits, on the face of the measurement: five systems,
six features, one real control — descriptive and
low-power by construction; the Eteocypriot sandbox
stream is the Spec 105 derivation subset (14 texts,
69 tokens), not the full ICS corpus, so its profile
is indicative only; Latin sentence-texts are far
longer than any program text, so text-length-sensitive
features compare types, not like-for-like documents.
These limits weaken the leg's power to detect a
signal; they do not manufacture the null result,
which is driven by the inventory and entropy spread
(372 vs 35 vs 32 signs; H1 6.27 vs 4.89 vs 4.14 bits)
that any common-descent claim must explain away.

### 2.4 Grade

**P1: NOT SUPPORTED** — overall and for each script.
The documentary leg shows three separate documented
derivations; the distributional leg shows no trio
clustering; the numerical leg shows no shared
convention beyond tallying. P1's paleographic
(sign-shape) leg is separately graded UNTESTABLE ON
CURRENT EVIDENCE (§5), because the program holds no
comparable sign-shape data; that untestability does
not soften the grade, since the burden of P1 is a
positive shared-derived-feature pattern, and every
leg that can be run returns none.

## 3. P2 — Developmental discontinuity: NOT SUPPORTED

### 3.1 Indus

At Harappa, pre-firing potter's marks and post-firing
graffiti occur in the Ravi (Hakra) phase (Period 1,
c. 3300–2800 BCE); many of those marks continue
through the Kot Diji phase (Period 2, c. 2800–2600
BCE), where sign sequences on pottery are widespread,
and some are identifiable as elements of the mature
Indus writing system, which runs c. 2600–1900 BCE
(Kenoyer & Meadow, Harappa excavation record,
harappa.com "Recent Indus Discoveries and Highlights
from Excavations at Harappa 1998–2000"; Kenoyer 2006,
"The origin, context and function of the Indus
script: Recent insights from Harappa", in Osada ed.,
Proceedings of the Pre-symposium of RIHN and 7th ESCA
Harvard-Kyoto Roundtable). The mature script therefore
stands at the end of roughly seven centuries of local,
stratified sign use at a single excavated site. That
is the precursor trail P2 says a transmitted system
would not leave. **Indus: NOT SUPPORTED.**

### 3.2 Eteocypriot / Cypriot syllabic

The syllabary's precursor is Cypro-Minoan, attested on
Cyprus for roughly five centuries before the syllabary
proper, with sign-form development traceable across
the sequence (§2.1: Steele 2013; Ferrara 2012). The
Eteocypriot texts themselves (earliest substantial:
the Amathus bilingual, ICS 196, 4th century BCE on the
standard dating) stand at the end of that island
lineage, not at its start. **Eteocypriot: NOT
SUPPORTED.**

### 3.3 Meroitic

The Meroitic script appears in the 3rd–2nd century BCE
already adapted from Egyptian forms (§2.1), inside a
kingdom that had used Egyptian writing for centuries.
Its abruptness is the abruptness of a deliberate
script reform with a known donor, the opposite
signature from an unattributed fully-formed arrival.
**Meroitic: NOT SUPPORTED.**

### 3.4 Grade

**P2: NOT SUPPORTED**, all three scripts. Each system
has local developmental precursors in the stratified
or documentary record.

## 4. P3 — Chronological anomaly: NOT SUPPORTED

No script in the program, and no demonstrated direct
ancestor of one, is securely dated materially earlier
than the standard chronology allows. The earliest
Indus antecedent marks (c. 3300 BCE, §3.1) are
contemporary with proto-cuneiform — early, but inside
the standard account of writing's emergence, and they
are marks becoming a script over centuries, not a
script arriving early. Cypro-Minoan (c. 16th century
BCE) and Meroitic (3rd–2nd century BCE) sit squarely
inside their standard chronologies.

The claimed older writing sometimes cited in this
connection, each labeled with its actual standing:

- **Jiahu marks** (Henan, China; tortoise plastrons
  and bone, c. 6600–6200 BCE). The publishing team's
  own assessment: "We interpret these signs not as
  writing itself, but as features of a lengthy period
  of sign-use which led eventually to a fully-fledged
  system of writing", with no traceable direct
  connection to the later Chinese script (Li Xueqin,
  Harbottle, Zhang & Wang 2003, "The earliest writing?
  Sign use in the seventh millennium BC at Jiahu",
  Antiquity 77(295):31–44, DOI
  10.1017/S0003598X00061329). Standing: early sign use,
  not writing, by its publishers' own statement; ~11
  incised signs, occurring singly, not in sequences.
- **Vinča symbols** (Balkans; bulk c. 4500–4000 BCE,
  the Tărtăria tablets claimed c. 5300 BCE by
  association — a dating whose context and association
  are disputed). Standing: treated by most scholars as
  proto-writing or symbolic/ownership marks that do
  not record language; quantitative analysis finds
  most signs pattern as pottery marks (59%) or ornament
  (11.5%), with a residue classed as possible
  semasiographic notation (29.5%); analyses find
  little similarity to Near Eastern writing, supporting
  independent origin of the symbol use itself (Winn's
  sign corpus, 1981; status summary in the scholarly
  literature on undeciphered systems). Whatever Vinča
  is, it is not demonstrated writing, it is not an
  ancestor of any program script, and its own analysts
  separate it from the Near Eastern line.
- **Dispilio tablet** (Lake Kastoria, Greece; wooden
  tablet with rows of incised signs). A direct
  radiocarbon date on the wood calibrates to
  5324–5079 cal BC at 95.4% probability (Facorellis
  et al. 2014, Radiocarbon 56(2)). Standing: as of
  2025 there has been no proper academic publication
  demonstrating the marks as a writing system; the
  artifact is a single object, its signs unread and
  unproven to encode language, and a date for wood is
  not by itself a demonstration of when or why the
  incisions were made. It is an intriguing Neolithic
  sign-bearing object, not evidence of a literate
  civilization or of transmission to any later script.

None of the three is a script, an ancestor of a
program script, or a dated literate context; each is
a sign-use case of exactly the kind the standard
account expects Neolithic societies to produce.
**P3: NOT SUPPORTED.** What would decide it is
stated in §5.

## 5. What is untestable on current evidence, and what would decide it

- **P1, paleographic leg: UNTESTABLE on program
  data.** The program holds token streams, not
  sign-shape data: there is no comparable dataset of
  sign forms (vector or image features with provenance)
  for the three systems and their documented parents
  in program custody. Acquiring it would take:
  licensed sign-image corpora for Indus (the CISI
  material is statistics-only under its terms — scans
  are never redistributed in this program), the ICS /
  Cypro-Minoan signaries in drawn form, and the
  Meroitic signary with its Egyptian comparanda, then
  a registered shape-similarity design with a
  permutation null over form space. Until then, the
  paleographic leg rests on the published derivations
  (§2.1), which are themselves largely paleographic
  arguments — and they point to three different
  parents.
- **P3, in general form: decidable by a single class
  of find.** A written artifact — signs in sequence,
  in a system ancestral to a program script — from a
  sealed, independently dated context materially
  before 3400 BCE would move P3 to SUPPORTED for that
  line and force the chronology open. No such find
  exists in the published record as of this evaluation.
- **P4, Indus leg: UNTESTABLE** (§6.1 below) until the
  script is read or a bilingual appears; the other two
  legs are testable now and fail (§6).

## 6. P4 — Content residue: NOT SUPPORTED (Indus leg UNTESTABLE)

### 6.1 Per script

- **Indus: UNTESTABLE ON CURRENT EVIDENCE.** The
  script is undeciphered, so its texts' content cannot
  be graded for knowledge content. What can be graded
  is form: the corpus is dominated by short seal texts
  (the Spec 105 derivation set averages 4.2 signs per
  text; the longest known Indus inscriptions run to
  roughly two dozen signs), a format that cannot carry
  astronomical or mathematical treatise content of the
  kind P4 requires (Possehl 2002, The Indus
  Civilization: A Contemporary Perspective, on the
  corpus's brevity and seal-dominated character).
  P4's Indus leg is therefore untestable in content
  and unsupported in form.
- **Eteocypriot: NOT SUPPORTED.** The earliest
  substantial Eteocypriot text, the Amathus bilingual
  (ICS 196), is a civic-religious dedication — the
  city of Amathus honoring the goddess — ordinary
  content fully within the recipient culture's
  attainment, in a script centuries old by then
  (Masson 1983, ICS no. 196). No Eteocypriot text
  encodes knowledge beyond its culture's documented
  level.
- **Meroitic: NOT SUPPORTED.** The earliest Meroitic
  texts are royal and funerary inscriptions whose
  content — offering formulae, filiation, royal
  names — follows Egyptian-derived templates, and the
  language's certain vocabulary (roughly 100 words on
  the program's own position record) is funerary,
  royal, and everyday (Rilly & de Voogt 2012). Nothing
  in the earliest stratum exceeds what Kush's own
  Egyptian-trained scribal culture demonstrably had.

### 6.2 Grade

**P4: NOT SUPPORTED** overall (two of three legs fail
on readable evidence; the third is untestable in
content and unsupported in form).

## 7. The honest summary

**What H explains that the standard account does
not.** Very little, on current evidence — and the
record should say precisely what that little is. The
standard account leaves genuinely open: why writing
emerged near-simultaneously (within centuries) in
Mesopotamia and Egypt with possible stimulus contact
unresolved; why the Indus tradition's antecedent marks
are as early as they are; and why sign use recurs in
Neolithic societies (Jiahu, Vinča, Dispilio) that never
developed writing. H "explains" simultaneity and
recurrence by a common source — but at the cost of
positing the source, and the simultaneity is of
*sign use and accounting pressure in early complex
societies*, which the standard account explains by
convergent administrative need (the token-to-tablet
trajectory) without new entities. An explanation that
fits by construction earns nothing until a prediction
lands; none of H's four has.

**What H costs in unsupported assumptions.** (1) A
literate civilization before 3400 BCE that left no
securely dated written artifact, no scribal material
culture, and no certain descendant signary. (2) A
transmission event (or events) crossing more than
eight thousand years between the catastrophe horizon
and the first attested scripts, carried by a channel
— oral custody of a writing system by non-literate
custodians — that is itself unattested anywhere.
(3) Recipient traditions that then, in each case,
independently produced exactly the local precursor
trails and foreign derivations (Egyptian for Meroitic,
Aegean for Cypriot) that the standard account predicts
and H must explain away as later overlays. Each
assumption is possible; none is supported; together
they are the hypothesis's entire substance, which is
why the grades fall as they do. **A prediction failing
is not the hypothesis being impossible** — it is the
hypothesis, so far, paying full price for no
observations.

**The single new piece of evidence that would most
change the grading.** A sealed, independently dated
written artifact from before c. 3400 BCE whose sign
system is demonstrably ancestral to one of the three
program scripts (shared derived sign forms with
values, not mere resemblance). That one find would
move P3 to SUPPORTED, reopen P1's paleographic leg
with real data, and convert H from an explanation
with no landed prediction into the leading account of that line's
origin. Short of it, incremental finds move nothing:
another Neolithic sign hoard is what the standard
account already expects.

## 8. Grade summary

| Prediction | Indus | Eteocypriot | Meroitic | Overall |
|---|---|---|---|---|
| P1 inheritance | NOT SUPPORTED | NOT SUPPORTED | NOT SUPPORTED | **NOT SUPPORTED** |
| P2 discontinuity | NOT SUPPORTED | NOT SUPPORTED | NOT SUPPORTED | **NOT SUPPORTED** |
| P3 chronology | NOT SUPPORTED | NOT SUPPORTED | NOT SUPPORTED | **NOT SUPPORTED** |
| P4 content | UNTESTABLE (form: unsupported) | NOT SUPPORTED | NOT SUPPORTED | **NOT SUPPORTED** |
| P1 paleographic leg | UNTESTABLE (no program sign-shape data) | UNTESTABLE | UNTESTABLE | **UNTESTABLE ON CURRENT EVIDENCE** |

No grade in this table is a claim that the hypothesis
is impossible. Each is a claim that the prediction's
required observations are absent or contradicted on
the evidence cited, as of 2026-11-27.
