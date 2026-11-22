# Inspectable packet manifest — Meroitic reproduction and adjudication packet (OD-19)

Assembled 2026-11-22 under owner decision OD-19 (commissioned 2026-11-22 13:37 ET; adjudication item OD-19 in `specs/091-anchor-comparison-integrity/records/coscientist-refresh-adjudication-2026-11-22.md`).

## Custody statement

The packet itself is assembled and held in custody on tower-compute at `~/Development/glossa-archive/meroitic-packet-od19-2026-11-22/`, alongside the corpus. It is **not** committed to this repository and is not copied off the custody host. This record is the packet's manifest only: contents index, per-item hashes, provenance, and access terms. It contains no corpus content and no restricted material.

Access terms are the F-6 posture as restated on 2026-11-22: retention in held custody permitted, computation permitted, derived artifacts aggregate-only, **sharing paused**, publication aggregate-only with the custody caveat. The OD-14 refusal protocol (`records/custody-clarification-programme-and-refusal-protocol-2026-11-22.md`) applies to the packet: on a written refusal, the packet is annotated and its corpus-derived items are handled as the protocol directs, on the protocol's seven-day timetable.

## Packet identity

- Items indexed below: 43 (plus the packet's own `PACKET-MANIFEST.json` and inspector README, 45 files in total)
- Total size on disk at assembly: 676,693 bytes (indexed items sum to 648,587 bytes)
- Packet `PACKET-MANIFEST.json` SHA-256: `c60dcf6ace59bc39fbe6937116aff031bba7c6b1b24372bef5d952cbd98e43e6`
- Inspector README (`00-README-inspector.md`) SHA-256: `b7b203b92b70935e2fbe986484a636a115f4c00ac2ac77010c7f567cdc892a16`
- Repository state at assembly: origin/main `1173b975` (PR #690 merge, OD-15)
- Hash verification at assembly: every copied item's SHA-256 was recomputed after copying and matched its source (43 of 43 verified).

## Corpus (held in place, verified, not copied)

The Otten corpus is not duplicated into the packet. It is held in place in scratch custody at `~/glossa-work/meroitic-corpus-src` and was verified file-by-file at assembly against the step-0 pin manifest (in the packet at `01-provenance-and-custody/meroitic-benchmark-step0-manifest-2026-11-20.txt`): **30 of 30 listed files verified**, none failed.

- Corpus pin: `c9158f6865325877112b6b9ceef83b3c80a93c56`
- Tree: `76138c53118dbc273068f1ad1e5d411b3e3362fd`

## Contents index

### 01-provenance-and-custody

| File | Bytes | SHA-256 | Source |
|---|---|---|---|
| custody-clarification-programme-and-refusal-protocol-2026-11-22.md | 15557 | `016ed8ab4570744725a62072e1102669e8ddcf4f7a3f636f96fbab2883d5af77` | ~/glossa-work/od19-2026-11-22/specs/097-meroitic-reproduction-benchmark/records/custody-clarification-programme-and-refusal-protocol-2026-11-22.md |
| custody-record-2026-11-20.md | 4270 | `fd8b0eaf6294b270e04aa87dc4a1509c9b2ca748fbfb77eec1ec6c87f0481aa6` | ~/glossa-work/od19-2026-11-22/specs/097-meroitic-reproduction-benchmark/records/custody-record-2026-11-20.md |
| custody-supplement-2026-11-21.md | 6233 | `f48c61c73e92eaffeb5adeb9ebd34c1f169d1f68a555cf390b93924b768c5e4c` | ~/glossa-work/od19-2026-11-22/specs/097-meroitic-reproduction-benchmark/records/custody-supplement-2026-11-21.md |
| custody-erratum-2026-11-21.md | 1724 | `01b133bed9143cc8b0e4ca62c67bb1d944dd53282a72bf544ba471ea88af344a` | ~/glossa-work/od19-2026-11-22/specs/097-meroitic-reproduction-benchmark/records/custody-erratum-2026-11-21.md |
| corpus-completion-record-2026-11-20.md | 5914 | `248d839ff883464b726dd72f5b51841715720ceedf3027f4094198da8c0bdc9e` | ~/glossa-work/od19-2026-11-22/specs/097-meroitic-reproduction-benchmark/records/corpus-completion-record-2026-11-20.md |
| meroitic-benchmark-step0-manifest-2026-11-20.txt | 3107 | `718a4ea613aad0f693c588379b3a5ef93d461eb6a5e792364c851ac35aa136f0` | ~/glossa-work/od19-2026-11-22/specs/097-meroitic-reproduction-benchmark/records/meroitic-benchmark-step0-manifest-2026-11-20.txt |
| meroitic-benchmark-step0-identity-record-2026-11-20.md | 11291 | `4a04ed8ed95bfbfce271cb58b17e3bbae8b060b7ba6235dfde658ebbda310992` | ~/glossa-work/od19-2026-11-22/specs/097-meroitic-reproduction-benchmark/records/meroitic-benchmark-step0-identity-record-2026-11-20.md |
### 02-freeze-and-scoring-path

| File | Bytes | SHA-256 | Source |
|---|---|---|---|
| campaign-freeze-v2-2026-11-20.md | 11108 | `7941d05b45b56dcda3cdf87d926a0154f5d92e041301ad8a51952a535f7417bb` | ~/glossa-work/od19-2026-11-22/specs/097-meroitic-reproduction-benchmark/records/campaign-freeze-v2-2026-11-20.md |
| campaign-freeze-v2-amendment-2026-11-21.md | 2579 | `9bdf06cd7bb83f05314bbc1aaad638fe1677fd8afde9fe8cbd73ae7128783d1d` | ~/glossa-work/od19-2026-11-22/specs/097-meroitic-reproduction-benchmark/records/campaign-freeze-v2-amendment-2026-11-21.md |
| campaign-freeze-v3-2026-11-22.md | 5624 | `74066cbaae53cd0b0ccaa6c6f2dc50ba6efd0dbadb917c0f69e7a98de197256c` | ~/glossa-work/od19-2026-11-22/specs/097-meroitic-reproduction-benchmark/records/campaign-freeze-v3-2026-11-22.md |
| freeze-v2-vocabulary-2026-11-20.json | 133299 | `ab1de889b6e8674512fa64c9bb9e7bf5f2efe15f609f681558ba7781f23178fc` | ~/glossa-work/od19-2026-11-22/specs/097-meroitic-reproduction-benchmark/records/freeze-v2-vocabulary-2026-11-20.json |
| freeze-v3-vocabulary-2026-11-22.json | 127059 | `ee7056a461907f213a92a7aeb268c0e11ffb0c88d736c9799df647101e68bdd1` | ~/glossa-work/od19-2026-11-22/specs/097-meroitic-reproduction-benchmark/records/freeze-v3-vocabulary-2026-11-22.json |
| meroitic-benchmark-freeze-2026-11-20.md | 9932 | `67a684124394fe47fa8b8ef115d1b9ad1f571ebc21b6d8c9721030e997dbf797` | ~/glossa-work/od19-2026-11-22/specs/097-meroitic-reproduction-benchmark/records/meroitic-benchmark-freeze-2026-11-20.md |
| anchor-inventory-freeze-v1-2026-11-20.md | 6514 | `717a653432665296aa49d952038df23b54da198cf9f212119a95c6a06879ed57` | ~/glossa-work/od19-2026-11-22/specs/097-meroitic-reproduction-benchmark/records/anchor-inventory-freeze-v1-2026-11-20.md |
| pipeline-v2.py | 17432 | `74b831da221f0708b2c5a9f7e9f1a7772175fe2097783f101d33588769e1642e` | ~/glossa-work/meroitic-scratch/campaign/pipeline-v2.py |
### 03-benchmark-results

| File | Bytes | SHA-256 | Source |
|---|---|---|---|
| leg-a-results.json | 5824 | `2cc970d4c6b3e1ae52c8a1fcab8e004915e5eec15e91f777ca28427584452ad3` | ~/glossa-work/od19-2026-11-22/specs/097-meroitic-reproduction-benchmark/records/leg-a-results.json |
| leg-b-results.json | 6867 | `984edbb5a66d59cf94ce8a40632989ab14a278055c560d3fed11709878465e47` | ~/glossa-work/od19-2026-11-22/specs/097-meroitic-reproduction-benchmark/records/leg-b-results.json |
| leg-c-summary.json | 15241 | `e5e68931943834498b4b4804e5123f5448ab1c2dd0cf9cbd3d12b106c4680f0a` | ~/glossa-work/od19-2026-11-22/specs/097-meroitic-reproduction-benchmark/records/leg-c-summary.json |
| leg-c-runs.jsonl | 17417 | `a8b375b2c688c666ddebbab45fb83d1e4bf393d5e7fbdc6ab7d52c1738ba2ac4` | ~/glossa-work/od19-2026-11-22/specs/097-meroitic-reproduction-benchmark/records/leg-c-runs.jsonl |
| leg-c-runs-repair.jsonl | 26881 | `d594a6322f68f9036b8008c9993196bb00e7e3943aece5bac7e445ba206f164b` | ~/glossa-work/od19-2026-11-22/specs/097-meroitic-reproduction-benchmark/records/leg-c-runs-repair.jsonl |
| meroitic-benchmark-outcome-record-2026-11-20.md | 13417 | `b05fe0ffd63b0add18ec3923dc9ae3152aefcf583e084ba990800db8612c672b` | ~/glossa-work/od19-2026-11-22/specs/097-meroitic-reproduction-benchmark/records/meroitic-benchmark-outcome-record-2026-11-20.md |
| 662-distinct-texts-reproduction-2026-11-22.md | 4322 | `49e2ddaa7eba9ec95b9440385e60cbdfebce13a8604e335a0fda38f876ea4c0a` | ~/glossa-work/od19-2026-11-22/specs/097-meroitic-reproduction-benchmark/records/662-distinct-texts-reproduction-2026-11-22.md |
| leg_a_results.json | 5824 | `2cc970d4c6b3e1ae52c8a1fcab8e004915e5eec15e91f777ca28427584452ad3` | ~/glossa-work/meroitic-scratch/leg_a_results.json |
| leg_b_out.json | 6867 | `984edbb5a66d59cf94ce8a40632989ab14a278055c560d3fed11709878465e47` | ~/glossa-work/meroitic-scratch/leg_b_out.json |
| leg_c_summary.json | 15241 | `e5e68931943834498b4b4804e5123f5448ab1c2dd0cf9cbd3d12b106c4680f0a` | ~/glossa-work/meroitic-scratch/leg_c_summary.json |
### 04-stage4-and-audits

| File | Bytes | SHA-256 | Source |
|---|---|---|---|
| stage-4-2-outcome-record-2026-11-20.md | 4097 | `3b3a76f552396d67dfed23309119e76d01a595e27bf5805db3e96a62ab9576f7` | ~/glossa-work/od19-2026-11-22/specs/097-meroitic-reproduction-benchmark/records/stage-4-2-outcome-record-2026-11-20.md |
| stage-4-2-results.json | 3861 | `9ea5cce7d8cbeea182d49a6253c096e899e8fc94b5a4fd1e2b9a6b376233eb1f` | ~/glossa-work/od19-2026-11-22/specs/097-meroitic-reproduction-benchmark/records/stage-4-2-results.json |
| stage-4-3-outcome-record-2026-11-20.md | 3598 | `0c99177ebac5b9add478f294abc5e2530e6ace9cb84f01d56e786de26e02eb30` | ~/glossa-work/od19-2026-11-22/specs/097-meroitic-reproduction-benchmark/records/stage-4-3-outcome-record-2026-11-20.md |
| stage-4-3-candidates.json | 4571 | `4f1e7812488b7760003194153758915680d6d9a25f34c86d7e16daf8b4a86167` | ~/glossa-work/od19-2026-11-22/specs/097-meroitic-reproduction-benchmark/records/stage-4-3-candidates.json |
| stage-4-4-outcome-record-2026-11-20.md | 4193 | `e78f238f45d36928c13bf9ab5248e996374f76000b64f0e336b0be1e095616b5` | ~/glossa-work/od19-2026-11-22/specs/097-meroitic-reproduction-benchmark/records/stage-4-4-outcome-record-2026-11-20.md |
| stage-4-4-results.json | 4390 | `11369924c0ad5568ea32f7ad7b55c11052eaa18ec88cc2dea3e3e2459d490e8f` | ~/glossa-work/od19-2026-11-22/specs/097-meroitic-reproduction-benchmark/records/stage-4-4-results.json |
| stage-4-5-anchor-tranche-send-record-2026-11-20.md | 3746 | `ef8d42ffb44dd82c87f80749a5563f1a3c05e8f3f54f6f8e6994bc08a5582004` | ~/glossa-work/od19-2026-11-22/specs/097-meroitic-reproduction-benchmark/records/stage-4-5-anchor-tranche-send-record-2026-11-20.md |
| stage-4-5-supplement-2026-11-21.md | 7663 | `840f28217eb63bb42bff9e2cc95e39395400d7273b3bc23c2da98c52a0abb267` | ~/glossa-work/od19-2026-11-22/specs/097-meroitic-reproduction-benchmark/records/stage-4-5-supplement-2026-11-21.md |
| stage-4-5-supplement-correction-2026-11-21.md | 6335 | `37814d5347d7e692bb26c9ba17967e8f991413157b0aaad704c2229419a719b3` | ~/glossa-work/od19-2026-11-22/specs/097-meroitic-reproduction-benchmark/records/stage-4-5-supplement-correction-2026-11-21.md |
| power-simulation-audit-2026-11-22.md | 10126 | `ca8952b26d8c835d2ba9a8a90c88bfd65b5c610974e9a8a659e0174510af4c9a` | ~/glossa-work/od19-2026-11-22/specs/097-meroitic-reproduction-benchmark/records/power-simulation-audit-2026-11-22.md |
| power-simulation-audit-2026-11-22.json | 14155 | `65286b91baa8e8caa5169eb2b6e02d7a66dc5fedf5b7d55f44b72ec5ff800704` | ~/glossa-work/od19-2026-11-22/specs/097-meroitic-reproduction-benchmark/records/power-simulation-audit-2026-11-22.json |
### 05-adjudication-trail

| File | Bytes | SHA-256 | Source |
|---|---|---|---|
| verdict-restatement-2026-11-20.md | 5291 | `0ec136076ed6c68c89e5285a93d095559abd2a5cfb915c4b0c284178c6b21673` | ~/glossa-work/od19-2026-11-22/specs/097-meroitic-reproduction-benchmark/records/verdict-restatement-2026-11-20.md |
| verdict-tally-correction-2026-11-21.md | 3857 | `cd78ff3618ef714443765210ea0377a3f0dbee2bbeae236dd2ee2d3916fd5657` | ~/glossa-work/od19-2026-11-22/specs/097-meroitic-reproduction-benchmark/records/verdict-tally-correction-2026-11-21.md |
| citation-gloss-addendum-2026-11-22.md | 13637 | `1125e218e1652b3838ada2fa2157616d4875f10cf973056895acc44e8b6e56d2` | ~/glossa-work/od19-2026-11-22/specs/097-meroitic-reproduction-benchmark/records/citation-gloss-addendum-2026-11-22.md |
| citation-discipline-record-2026-11-21.md | 9446 | `0ebd3e735df9c7e7e72cf89950e207d8d4f3797eb191a576ed031b7ea5759cff` | ~/glossa-work/od19-2026-11-22/specs/097-meroitic-reproduction-benchmark/records/citation-discipline-record-2026-11-21.md |
| citation-discipline-erratum-2026-11-21.md | 2120 | `82b8a6735cf8544c1afca6fc0570497f2a38062daf738d990965f24170214809` | ~/glossa-work/od19-2026-11-22/specs/097-meroitic-reproduction-benchmark/records/citation-discipline-erratum-2026-11-21.md |
| adoption-and-registration-2026-11-20.md | 7635 | `1e01f2081959427804a9b340c0be78d987f9c3e6030155a7b5e86532198f76f5` | ~/glossa-work/od19-2026-11-22/specs/097-meroitic-reproduction-benchmark/records/adoption-and-registration-2026-11-20.md |
| coscientist-refresh-adjudication-2026-11-22.md | 60322 | `82b614032930b670105e500ce5f00ded7cbf7a3e09c9b11c8e41e081c355662b` | ~/glossa-work/od19-2026-11-22/specs/091-anchor-comparison-integrity/records/coscientist-refresh-adjudication-2026-11-22.md |

Every hash above is the full SHA-256, identical to the value carried in the packet's own `PACKET-MANIFEST.json`.

## Provenance

Repository items were copied from a fresh clone of AXIOVEX/glossa-lab at origin/main `1173b975`. The frozen scoring path (`pipeline-v2.py`) and the executed Leg A/B/C outputs were copied from tower-compute scratch custody (`~/glossa-work/meroitic-scratch/`), where the campaign ran; each is identified by its full hash in the packet manifest. The adjudication record was copied from `specs/091-anchor-comparison-integrity/records/` at the same commit.

## Pending at assembly (indexed, not included)

- **OD-16 executable freeze v2/v3 comparison** — commissioned 2026-11-22 13:23 ET; PR #691 open at assembly; indexed as pending, not included.
- **OD-17 freeze-split dependency audit** — commissioned 2026-11-22 13:27 ET; PR #692 open at assembly; indexed as pending, not included.
- **OD-18 expert-verification preparation** — authorised 2026-11-22 13:33 ET; PR #693 open at assembly; indexed as pending, not included.

No unfinished work is included in the packet. A packet supplement is the route for adding these items once landed.

## Not included, and why

- The Otten corpus bytes: held in place under the F-6 posture and verified against the pin manifest (above); duplicating them into the packet would multiply custody copies without adding inspectability.
- OD-16, OD-17, and OD-18 outputs: in flight at assembly (above).
- The internal-use Meroitic paper: a publication artifact, not part of the reproduction and adjudication record this packet inspects.
