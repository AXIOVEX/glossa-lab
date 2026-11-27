# Spec 097 — Otten Corpus Custody Restoration Record (2026-11-27)

The Otten & Anastasopoulos (2025) Meroitic-Corpus,
verified absent from every custody location on
2026-11-27, has been re-acquired at its pin, verified
against the step-0 manifest, and restored to tower
custody. The custody location's own CUSTODY.md
(`glossa-custody/spec097/otten-corpus/CUSTODY.md` on
tower-compute) is the custody record of record; this
record files the restoration in the program's records
and carries the verification table. No corpus bytes
are carried in this record or anywhere in this
repository.

## Authorization

- Owner ruling, 2026-11-27 11:26 ET (Glossa-Lab chat):
  re-acquire the corpus at the pin, verify against the
  manifest, restore custody, then re-register Spec
  107's M-2 leg on its original basis.
- The staging clone's first inspection tripped the
  execution-risk flag before any verification ran.
  Owner clearance, 2026-11-27 11:33 ET, given after
  that trip, cleared work inside the staging clone;
  all verification and the copy ran under it.

## Source and pin

- Remote: github.com/Joshua-Otten/Meroitic-Corpus
  (the repository named in the paper's footnote 1, per
  the step-0 identity record).
- Pinned commit: c9158f6865325877112b6b9ceef83b3c80a93c56
- Pinned tree: 76138c53118dbc273068f1ad1e5d411b3e3362fd
- Staging clone:
  ~/.syncyard/worktrees/glossa/otten-restore-staging-20261127/Meroitic-Corpus
  — HEAD and tree read directly on 2026-11-27 and
  equal to the pin; working tree clean.

## Verification (30 of 30)

Reference table: the step-0 manifest as filed
(`records/meroitic-benchmark-step0-manifest-2026-11-20.txt`).
Staging verification ran 2026-11-27T16:37:05Z
(sha256sum exit 0); the custody copy was re-hashed
after copying at 2026-11-27T16:39:58Z with the same
result. Every file below verified OK in both passes.

| File | SHA-256 (manifest) | Result |
|---|---|---|
| Data/HamadabStelaOfAmanirenasNarrative.txt | 8c3e22902ac61361dc13bc7863b4b418ba88b06c4eaf71e4fbeba6a176dbe115 | OK |
| Data/KalabshaMeroiticInscriptionOfKharamadoyeNarrative.txt | e06dba12998118c420f4188a6607b9cab7fdfc6287922355923b27e5f136d04d | OK |
| Data/Kalabsha_Millet.txt | 42408955e513a98e35b539013ceaaff2ebc25616e2091c09f16a12d9b1ef7ac0 | OK |
| Data/LobbanVocabList.txt | 1275c34d10bf4dc397cc0e457f3a686fdb76f3fbc192b3b42efb6afba753d622 | OK |
| Data/mero-corpus.txt | b7f3350c2f2118a8223854462a8e881c424cba6b26c01ebfb676efa92ea253ce | OK |
| Data/MilletExamples.txt | 9e0dc67ca945fa915479f015cdb6083b5788f86c3cc096f171994b0e4e670e6f | OK |
| Data/RillyExamples.txt | beae69e1b417cdd6bcdf88b2d6987af22b6cc99044dbd40d3276b8b13815f1f7 | OK |
| Data/TanyidamaniNarrative.txt | 92144779aec84f735a3f0851c8898ad26a40a733d4466aebe93ecfd307e4dba1 | OK |
| Embeddings/egyptian_dim_100.txt | 20fc91ebd357736a8e96311dd4dc2086e72ebb66255e311cae41679f0f3adfe9 | OK |
| Embeddings/egyptian_dim_120.txt | 568f5727ba3434ef2767374cc83e38c5559102e610927098437136833a80deab | OK |
| Embeddings/egyptian_dim_20.txt | b4119313aaca89f50b791d0b8fc4219f0606859e1077d22d62edcffbb7ddab03 | OK |
| Embeddings/egyptian_dim_50.txt | bce8e4f2910aecf14b7e67648b2f70d0f1f1ff18f418e0a4949ffaf4f518fc70 | OK |
| Embeddings/meroitic_dim_100.txt | 9da08536433995ef577d392e17a0440cc0a2e722ca740315e34af8d303e98c94 | OK |
| Embeddings/meroitic_dim_120.txt | 59c0d7c8a9add3dae38832ebd41cfbec5f297c57b52f0d4319a026f82318851e | OK |
| Embeddings/meroitic_dim_20.txt | dc4c2e5ab35a32d67f6d5ab2e3fb343056c5280654231cc9685382e55f24a2d6 | OK |
| Embeddings/meroitic_dim_50.txt | 0ae1f4105d57b1eb5f77b65e6379c5f0d8ca62ec423c881de733db3757945397 | OK |
| bilingual_dicts/adj_mr-eg.txt | f34a996d42ee954e326712d1497de52efc4f6f2dc26e76735aeb6f7de5d84b79 | OK |
| bilingual_dicts/fra-eng.0-5000.txt | bd6b571a68e32c7914e729a6dc5cffe28aeb2204ef868f7fb1a4dc5e545266ba | OK |
| bilingual_dicts/names_mr-eg.txt | bed3f2240bb86db6cf7af9b81803f59ed93039230c7e3a9209d51d3e7a486bc2 | OK |
| bilingual_dicts/nouns_mr-eg.txt | 3271932b757df71e9e5f2bb4120932387838f8dbb607aa811401f831a2968af4 | OK |
| bilingual_dicts/nouns+names+nums.txt | 614775d3c9a291c31a3236a9ef65676c223d0ca9211b41962181a1bdde74b207 | OK |
| bilingual_dicts/num_mr-eg.dict | c1353dae92d30a06510d4484545bb94db8a2a8306f347005e212bb19fdfcf105 | OK |
| bilingual_dicts/prep_mr-eg.txt | 129564fe25f978ade144c8ffe73e00ac1599d6bdd2fd1320cbcdc02ded2e27c4 | OK |
| bilingual_dicts/titularies_mr-eg.dict | df2e5f643af4eeec3bd4ab4cd464e11396888bc2137f03223f7dd9a1182c2d8a | OK |
| bilingual_dicts/verb_mr-eg.txt | d7c7f9539744d35d565ffadd5da1c37817c2dd5faa34c94fc7e612422d32e858 | OK |
| Code/find_nearest_neighbors.py | d11a8c4c676f67418fdc9bf0a29ac2dc9651742cd75d5fd007e1371f0fe800ad | OK |
| Code/getW2V_embeddings.py | 3dc5ddc589fab1508e12ba5ffe18ae19de804d4d31cd47c30ac00dcfacaf6a22 | OK |
| Code/intrinsic_eval.py | a242d1245a121280a65f3fe1fea8fa8aa544b67b639c1b720cbdc8ab4905cfd7 | OK |
| Code/RamsesScraperComplete.py | 02682781e77f561aff7f377bf8cbd420fd9a832f64c97c54ae6865e60522197a | OK |
| README.md | 9979a88afbe238bd837f7075c778d4ea9fe9a1c13f4283a25e7a4c1f0ebf8ee4 | OK |

Tree accounting: the pinned tree carries 33 blobs and
1 gitlink. The 33 blobs are the 30 manifest files plus
3 .DS_Store files (root, Data/, Embeddings/) not in
the manifest, carried as pinned. Code/vecmap is a
gitlink (commit b82246f6c249633039f67fa6156e51d852bd73a3)
with no .gitmodules at the pin; not retrievable, not
in the manifest, present in custody only as an empty
directory.

## Restored custody

- Location (tower-compute):
  ~/.syncyard/worktrees/glossa/glossa-custody/spec097/otten-corpus/
- Copied 2026-11-27T16:39:14Z from the verified
  staging working tree (excluding .git); post-copy
  re-hash 30 of 30 OK, no exceptions.
- Permissions: files 0440, directories 0550
  (read-only, Holdat pattern), set after the re-hash.
- CUSTODY.md in the location carries the source, pin,
  rulings, verification result, terms, and the
  home-discrepancy resolution.

## Custody terms of record

No licence exists for this corpus. The custody basis
is an owner risk acceptance (Tristen Pierson,
2026-11-20 delegated-decisions package, Item 2), not a
licensing finding. A permission request was sent to
both authors on 2026-11-20 (Gmail 1a1fb44214cf7994);
no reply is on file, and silence is recorded as
silence, never as permission. Terms: never committed
to any git repository, never redistributed or shared,
computation in held custody only, aggregate statistics
only in published work, custody ends if the rights
holders object.

## Home-discrepancy resolution

The step-0 identity record placed the original scratch
custody on the mini-server (~/glossa-work/meroitic-corpus-src);
the custody record said tower-compute. The 2026-11-27
custody search inventoried every named location on
tower-compute, the mini-server, and the Muse VM
workspace; both recorded homes, and every other
custody location, held no corpus bytes. The restored
home of record is the tower custody location above.

**AI disclosure:** executed by an AI agent (Muse, via
Muse) at the direction of Tristen Pierson, per
constitution sec. VI.
