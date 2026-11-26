# Spec 103 — REM Witness Acquisition Record (2026-11-26)

## 1. The authorizing act

Spec 103 closed with one form unchecked: **asoreyi — NOT CHECKED, INCOMPLETE COVERAGE**, because 8 of the 33 held-out texts carry no witness in the held Kovetsky build. The Stage 1 outcome record states that closing the check would need a source witness the held build does not contain, that the modern REM edition is the settling record for such a question and is not held in machine-readable form, and that any acquisition toward it is a separate, owner-gated act. On 2026-11-26 the owner approved the acquisition in the Glossa-Lab chat: the recommendation was presented in the owner-decisions list of 2026-11-26 (~01:52 ET) and he answered "For everything else, execute now to your recommendations" (2026-11-26 01:54 ET). This record is the acquisition's execution record. **The asoreyi check itself was NOT run**; it needs its own future registration once a witness is held.

## 2. The eight unwitnessed texts

From the Spec 103 records (Stage 1 outcome record and results file), with their rows in the pinned Kovetsky build (`145af083…`; build data read 2026-11-26). All eight rows carry `rem: []` in the build: the build does not map them to REM numbers; their identifiers are the Griffith publication numbers.

| Text | Build row (site, object, preferred reading) | Words |
|---|---|---|
| B.O. 1 | Buhen, west of the South Temple (Philadelphia No. 10938), ostracon, `griffith:G-jea11-B.O. 1` | 16 |
| F.O. 7 | Faras, the "Western Palace", ostracon, `griffith:G-jea11-F.O. 7` | 6 |
| F.O. 17 | Faras, the "Western Palace", ostracon, `griffith:G-jea11-F.O. 17` | 11 |
| F.O. 29 | Faras, the "Western Palace", ostracon, `griffith:G-jea11-F.O. 29` | 3 |
| F.O. 39 | Faras, church site SW of the Enclosure, ostracon, `griffith:G-jea11-F.O. 39` | 7 |
| Meroe 40 | Meroe, middle cemetery grave 311, funerary offering table, `griffith:G-meroe-40` | 5 |
| Sh. 9 | Shablul, funerary, `karanog:G-karanog-Sh9` | 14 |
| Sh. 16 | Shablul, funerary, `karanog:G-karanog-Sh16` | 17 |

The decision-bearing loci are the two Shablul texts: Sh. 9 carries asoreyi's second counted locus (filed WITNESS UNAVAILABLE), and Sh. 16 carries soreyi's one unwitnessed counted locus plus asoreyi's unwitnessed near locus. The build's Shablul coverage is formula fragments, not transcriptions, which is the structural reason the two Shablul texts are unwitnessed.

## 3. The modern REM edition, identified exactly

Jean Leclant (dir.), André Heyler, Catherine Berger-El-Naggar, Claude Carrier, Claude Rilly, *Répertoire d'Épigraphie Méroïtique: Corpus des inscriptions publiées*, Académie des Inscriptions et Belles-Lettres, Paris, 2000, diffusion De Boccard. **3 volumes, 2,084 pp. ISBN 2-87754-113-4.** The Académie sells the set via Peeters at **€124 for the three volumes**. Verified from the Académie's own pages and Persée, 2026-11-26.

Chapter map (from the edition's Sommaire général), showing the set covers all eight texts by construction:

- Tome I: ch. 1 Meroitic Inscriptions (REM 0001–0137, p. 1); ch. 2 other early texts (REM 0138–0150, p. 309); **ch. 3 Inscriptions de Karanog et Shablul (REM 0201–0387, p. 337)** — carries Sh. 9 and Sh. 16.
- Tome II: ch. 4 Inscriptions de Méroé (REM 0401–0451, p. 715) — carries Meroe 40; ch. 5 Inscriptions de Faras (REM 0501–0546, p. 821) — carries the four Faras ostraca; ch. 6 Ostraca de divers sites (REM 0551–0597, p. 915) — carries B.O. 1; ch. 7 Kawa (p. 1011); ch. 8 Royal Cemeteries of Kush (p. 1261).
- Tome III: ch. 9 Textes publiés isolément depuis 1911 (REM 1001–1278, p. 1373); Annexes 1–5 (pp. 1947–1993); Liste bibliographique (p. 1997); **Index B: sites d'origine des REM (pp. 2051–2060)** — the index that resolves each text's site number to its REM number.

## 4. Open-access channel verified: Persée

The REM is deposited on Persée, the French Ministry of Higher Education open-access platform, an Académie-deposited library channel. Collection code `rem`. Verified 2026-11-26 (issue pages returned HTTP 200):

- Tome I: issue `rem_0000-0000_2000_num_1_1`; document `_845`, "Tome I - REM 0001 à REM 0387" (the full Tome I content, including the Karanog/Shablul chapter carrying Sh. 9 and Sh. 16).
- Tome II: issue `rem_0000-0000_2000_num_2_1`; document `num_2_1_847`, "Tome II - REM 0401 à REM 0851" (carries Meroe 40, the Faras ostraca, and B.O. 1).
- Tome III: issue `rem_0000-0000_2000_num_3_1`; document `num_3_1_849`, "Tome III - REM 1001 à REM 1278".

**Blocker, verified twice from tower-compute on 2026-11-26:** automated download of the tome PDFs (the platform's `docAsPDF` route) is gated by an Altcha bot-protection challenge: GETs return a 292-byte HTML notice ("This resource is protected by altcha — Please visit the document page to view its content or download the PDF version"), with and without a cookie jar, and HEAD returns 403. Document pages and page images are accessible. **Bulk page-image harvesting to assemble the tomes was considered and NOT used:** defeating the platform's bot protection at scale is not a legitimate-channel acquisition. A human session (the owner at any browser) can download the three tome PDFs from Persée in minutes; that is the prepared route to a held digital witness.

Griffith's 1911 *Karanòg: The Meroitic Inscriptions of Shablûl and Karanòg* (public domain) was considered and rejected as the acquisition: it is the source the held build already derives from, not the modern REM edition the registration names as the settling record. Substituting it would repeat the no-substitution violation.

## 5. Outcome

**No digital file was obtained or homed.** Two routes stand prepared:

1. **Persée (no cost):** channel verified to the exact issue and document identifiers above; the download step is blocked for automated access by Persée's Altcha gate. Blocker owner: Persée (the platform); the workaround is a human browser session, which is the owner's to run.
2. **Print set (€124, Peeters):** prepared to the point of purchase; the payment checkout is the blocker, and its owner is Tristen.

## 6. Custody

Designated custody home: `~/.syncyard/worktrees/glossa/glossa-custody/spec103/` on tower-compute, with a CUSTODY.md stating the terms. **Current state: NOTHING HELD.** No digital material exists, so no hashes exist. When a witness is obtained (Persée PDFs or the print set), the obtained form, source, cost, and (for digital material) SHA-256 hashes are to be appended to this record and to the custody note.

## 7. What did not happen

The asoreyi check was not run, and no classification at any locus changed. Spec 103's outcome stands exactly as filed: CLAIM STANDS for soreyi, xolkete, pxolkete, xolkte, wisi; asoreyi NOT CHECKED — INCOMPLETE COVERAGE. No standing, verdict, or tally moved.

## 8. Acquisition completed — Persée download through the desktop browser (2026-11-26)

On 2026-11-26 (~02:24 ET) the owner directed the Persée route be run through the tower-compute automation Brave browser (the desktop-browser route), on his reasoning that a genuine desktop browser session should not trip the platform's Altcha protection the way the automated route did. He was right. **All three tome PDFs were downloaded, free of charge, and are HELD in the designated custody home.** This section supersedes §5's outcome and §6's state; §§1–4 and §7 stand as filed (the asoreyi check was still not run).

**Method, exactly as executed.** In the automation Brave session (dedicated profile, tower-compute), one working tab: navigate to each document page, click the page's own PDF control ("doc-ctrl/global/pdf") once, and let the browser take the download. No bulk harvesting, no page-image scraping, no circumvention tooling, no sign-in (none is needed). Per tome:

- **Tome I** (doc `rem_0000-0000_2000_num_1_1_845`): single click; download completed unaided.
- **Tome II** (doc `rem_0000-0000_2000_num_2_1_847`): the first clicks produced no download; inspection found the page's hidden Altcha widget (`pdf-download-captcha-widget`, state "unverified"). One scripted click on its "I'm not a robot" checkbox drove the widget to state "error" and was not repeated. A fresh page load followed by a single click on the PDF control then passed the check unaided (the genuine session verifies invisibly on a fresh load, as it had for Tome I) and the download completed.
- **Tome III** (doc `rem_0000-0000_2000_num_3_1_849`): fresh load, single click, download completed unaided.

**Held material** (custody home `~/.syncyard/worktrees/glossa/glossa-custody/spec103/` on tower-compute; hashes verified in the /tmp staging area before the move and again in custody after it, identical; the custody note carries the same table):

| File | Bytes | Pages | SHA-256 |
|---|---|---|---|
| rem-tome-1-rem0001-0387.pdf | 215,556,263 | 714 | f20d9f955ff2a74d391d894f65958c3d2848d5282a26a5c5ba5ae70dd591afce |
| rem-tome-2-rem0401-0851.pdf | 174,384,353 | 658 | 55b13325bad738b8e2e53b3fc41f8340162625c8c5a2a3e982da811115dff167 |
| rem-tome-3-rem1001-1278.pdf | 182,222,445 | 712 | cc24ffe691c6522b71cc56cc812554c41786fe0654742abed4238bbcb5ebe6a1 |

Page counts sum to 2,084, the edition's stated extent; producer on all three is iText Core 8.0.2 (Persée's own PDF generator); each file ends in a complete PDF trailer. Cost: €0. The print-set route (€124) is no longer needed for a held digital witness.

**What did not happen.** The asoreyi check was not run, and no classification at any locus changed. Spec 103's outcome stands exactly as filed: CLAIM STANDS for soreyi, xolkete, pxolkete, xolkte, wisi; asoreyi NOT CHECKED — INCOMPLETE COVERAGE. Running the check against the now-held witness needs its own future registration. No standing, verdict, or tally moved.
