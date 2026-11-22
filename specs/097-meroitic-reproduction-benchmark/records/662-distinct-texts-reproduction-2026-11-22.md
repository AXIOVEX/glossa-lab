# The 662 distinct-texts count — reproduction — 2026-11-22

**Spec:** 097 (Meroitic reproduction benchmark). **Finding of
record:** RT1-13 (Red Team Round 1), whose F-4 arm this record
executes. **Commission:** the F-4 study package, commissioned
by the owner in chat 2026-11-22. **Execution venue:**
tower-compute. The corpus file was computed over locally in
scratch and the scratch deleted after filing; nothing of the
held corpus is committed — this record carries counts only,
per freeze v2 section 1.

## 1. The claim as filed

The corpus completion record (2026-11-20) section 1 states
that the deposited `mero-corpus.txt` (18,090 lines; Otten
corpus pin `c9158f6865325877112b6b9ceef83b3c80a93c56`) is a
name-augmented training file that "collapses to 662 distinct
texts or phrases under name-masking, each repeated about 27
times on average", sourced to an unnamed "independent 2026
account". Freeze v2 section 1 conceded the program had not
reproduced the number and registered it as an external
account's figure.

The account is the public repository **MikeKovetsky/meroitic**
(cloned on tower-compute at commit
`145af0836ce1e90ef7fca6a1bd6a25d3e7e9cd9d`), whose REPORT.md
attributes the 662 to its full cleaning pipeline
(`src/pool.py`, `src/dedup.py`, `src/collapse.py`,
`src/corpus.py`, `src/clean_v2.py`) and whose filed coverage
summary (`data/discovery/coverage.md`) gives the final figures
as 662 texts and 18,075 words. The method as filed is that
pipeline, run unmodified.

## 2. Inputs

- `mero-corpus.txt` at the Otten pin `c9158f68...`: 18,090
  lines, SHA-256
  `b7f3350c2f2118a8223854462a8e881c424cba6b26c01ebfb676efa92ea253ce`
  (verified on the venue before the run).
- The account's five pipeline scripts, unmodified, at the pin
  above.

## 3. The run, stage by stage

| stage | output | account's filed figure |
|---|---|---|
| pool.py (private / royal pool construction) | private pool **178**, royal pool **11** | 178 / 11 (REPORT.md) |
| dedup.py (name-masked deduplication) | 2,168 masked skeletons | — (intermediate) |
| collapse.py (variant collapse) | 1,019 texts | — (intermediate) |
| corpus.py (normalization; 3 narrative copies dropped, 3 narratives added once) | 1,019 rows, 20,972 tokens | — (intermediate) |
| clean_v2.py (multi-word name masking + final deduplication) | **662 texts, 18,075 tokens** | **662 texts, 18,075 words** (coverage.md) |

Consistency checks inside the run: the 662 surviving texts'
copy counts sum to exactly **18,090** — every line of the
deposited file is accounted for — and 18,090 / 662 = **27.3**
copies per text, the completion record's "about 27 times on
average". Composition: 659 of the 662 are name-masked skeletons
of Otten-derived funerary texts; 3 are the narrative texts the
pipeline adds once each.

One clarification the reproduction makes visible: the
intermediate stages alone give 2,168 and 1,019. The 662 is
the full pipeline's final figure, after clean_v2's multi-word
name masking — which is how the account's own REPORT
attributes it. The completion record's phrase "under
name-masking" is accurate for the pipeline as a whole.

## 4. Outcome

**REPRODUCES EXACTLY.** Every filed figure of the account is
recovered by running its own pipeline, unmodified, over the
pinned corpus file: the pool sizes (178 / 11), the final
distinct-text count (662), the final token count (18,075), and
the completion record's derived average (about 27 copies per
text). RT1-13's open arm — a program-side reproduction that
was never run — is discharged: the 662 figure is no longer an
unreproduced external number.

What the reproduction establishes is the count and the
method, nothing more: it verifies that the deposited file
collapses as the account said, under the account's own
masking rules. It does not adjudicate whether that masking is
the right model of the corpus — the freeze's split discipline
(335 development / 33 held out over the 368 distinct texts of
the *acquired* corpus, a different and larger population than
this training file's 662 skeletons) is untouched by this
record, as are freeze v2 and every Stage 4 result.

**Payload verdict: reproduction executed end-to-end on the
venue; outcome REPRODUCES EXACTLY (662 texts, 18,075 tokens,
pools 178 / 11, copies summing to the file's 18,090 lines).**
