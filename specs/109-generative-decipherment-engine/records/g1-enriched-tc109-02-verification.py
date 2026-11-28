#!/usr/bin/env python3
"""TC-109-02 verification for the Spec 109 G1-E preflight.

Independent recomputation, from the custody corpora and
the filed candidate assignments, of every verdict-bearing
figure in records/g1-enriched-preflight-2026-11-27.md.
The enriched harness is imported at its SHA-256 pin and
its frozen constants are checked against the amendment
registration's values; the Stage 1 and G1-R harnesses are
asserted at their pins through it. Checks, per
replication:

 1. the corpus rebuilt from its seed of record by the
    harness's own admission path is byte-identical to
    the custody corpus the run filed, and the admission
    profile is exact (at 2x: the scale amendment's
    fallback accounting recomputes);
 2. the filed candidate's enriched objective E and base
    objective L, recomputed by full rescoring, equal the
    run's delta-based accounting; the candidate equals
    the best polished state; the positional term and the
    truth objectives and gaps recompute;
 3. delta-hat recomputed by the registered calibration
    rule (the search's own preamble, same seeds) equals
    the filed value exactly, draws included;
 4. recovery and the stem/edge anatomy recomputed from
    the filed candidate equal the filed figures;
 5. the margin block recomputed with the filed seeds
    (derangement, shuffled assignment, permutation null
    B = 999) equals the filed figures;
 6. the shuffle control by deterministic re-execution:
    the shuffled derivation is rebuilt with its filed
    seed and the identical enriched search re-run; its
    recovery and delta-hat must equal the filed figures
    (the shuffle candidate itself was not filed in the
    raw output; this check is by re-execution, and
    says so);
 7. the summary medians and the verdict block recomputed
    from the per-replication figures under the
    registration's clause rules equal the filed block
    (clause (ii) is checked under both readings: the
    harness's filed rule, at least 3 of 5 replications
    clearing, and the registration's median-replication
    form; on this run's figures they coincide);
 8. no key anywhere in the raw output references
    undeciphered material.

Run once per raw output (the 1x verdict run and the 2x
diagnostic). Usage:
  g1-enriched-tc109-02-verification.py RAW_JSON CUSTODY_DIR
Exit code 0 iff every check passes.
"""
import hashlib
import importlib.util
import json
import random
import sys
from collections import Counter
from pathlib import Path
from statistics import median

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location(
    "g1e", HERE / "g1-enriched-harness.py")
G = importlib.util.module_from_spec(spec)
spec.loader.exec_module(G)
H = G.H
NV = G.NV

FROZEN_LAMBDA = 1.0
FROZEN_C = (0.46945080842976417, 0.15648360280992138,
            0.000782418014049607)
failures = []


def check(name, cond, detail=""):
    print(f"  [{'PASS' if cond else 'FAIL'}] {name} {detail}",
          flush=True)
    if not cond:
        failures.append(name)


def admissible_map(Hmod, family, det_init, det_final):
    init_vals, fin_vals = Hmod.family_positional(family)
    admissible = {}
    for s in range(NV):
        adm = set(range(NV))
        if s in det_init:
            adm &= init_vals
        if s in det_final:
            adm &= fin_vals
        admissible[s] = adm if adm else set(range(NV))
    return admissible


def main():
    raw_path, custody = Path(sys.argv[1]), Path(sys.argv[2])
    raw = json.loads(raw_path.read_text())
    k = raw["scale"]
    Hmod = H if k == 1 else G.load_scaled_stage1(k)
    print(f"TC-109-02 verification of {raw_path.name} "
          f"(scale {k}x, namespace {raw['seed_namespace']})",
          flush=True)
    check("harness pin (self)", raw["g1e_harness_sha256"]
          == hashlib.sha256((HERE / "g1-enriched-harness.py")
                            .read_bytes()).hexdigest())
    check("imported harness pins",
          raw["stage1_harness_sha256"] == G.STAGE1_SHA
          and raw["g1r_harness_sha256"] == G.G1R_SHA)
    lam = raw["constants"]["lambda"]
    check("frozen lambda", G.LAMBDA == FROZEN_LAMBDA
          and lam == FROZEN_LAMBDA)
    check("frozen calibration constants",
          (G.C_HI, G.C_MID, G.C_LO) == FROZEN_C
          and (raw["constants"]["c_hi"],
               raw["constants"]["c_mid"],
               raw["constants"]["c_lo"]) == FROZEN_C)
    check("frozen search constants",
          (G.RESTARTS, G.STEPS, G.REHEAT_AT, G.P_CYCLE,
           G.CALIB_K, G.ALPHA, G.RECOVERY_FLOOR)
          == (40, 160000, 80000, 0.3, 2000, 0.5, 0.80))
    lengths = H.indus_lengths() * k
    recs, shuf_recs, margin_pass = [], [], []
    for rep in raw["replications"]:
        seed = rep["seed"]
        got_seed, corp, extra = G.admit_corpus(
            Hmod, raw["seed_namespace"], rep["rep"], lengths, k)
        check(f"rep {rep['rep']} seed of record",
              got_seed == seed, f"({seed})")
        filed = json.loads(
            (custody / f"synth-rep{rep['rep']}.json").read_text())
        check(f"rep {rep['rep']} corpus identical to custody",
              filed["seed"] == seed
              and filed["signseqs"] == corp["signseqs"]
              and filed["family"] == corp["family"])
        if k == 1:
            check(f"rep {rep['rep']} admission profile",
                  len(corp["signseqs"]) == 1670
                  and sum(len(g) for g in corp["signseqs"]) == 7002
                  and extra["distinct"] == 1650
                  and rep["distinct"] == 1650)
        else:
            check(f"rep {rep['rep']} admission profile (2x)",
                  len(corp["signseqs"]) == 3340
                  and extra["distinct"] == rep["distinct"]
                  and extra["fallbacks"] == rep["fallbacks"]
                  and abs(rep["effective_scale"]
                          - rep["distinct"] / 1650.0) < 1e-12)
        deriv, reserve, _n = Hmod.split_corpus(corp["signseqs"])
        truth = corp["truth"]
        perm = truth["perm_value_to_sign"]
        anchors_sv = {perm[v]: v for v in truth["anchors"]}
        token_counts = Counter(m for g in corp["signseqs"]
                               for m in g)
        inv = [0] * NV
        for v, s in enumerate(perm):
            inv[s] = v
        cand = rep["g1_candidate_phi"]
        check(f"rep {rep['rep']} candidate is best polished",
              cand == rep["g1_best_polished_phi"])
        E, _dt, _lq = G.build_E(Hmod, deriv, corp["family"], lam)
        e_cand = E.total(cand)
        l_cand = E.base(cand)
        check(f"rep {rep['rep']} candidate E/L rescore",
              abs(e_cand - rep["g1_info"]["objective_enriched"])
              < 1e-6 and abs(
                  l_cand - rep["g1_info"]["objective_base"]) < 1e-6,
              f"(E {e_cand:.4f}, L {l_cand:.4f})")
        check(f"rep {rep['rep']} positional term recompute",
              abs(G.pos_term(E.M, cand)
                  - rep["g1_info"]["pos_term"]) < 1e-6
              and abs(e_cand - (l_cand + lam
                                * rep["g1_info"]["pos_term"]))
              < 1e-6)
        check(f"rep {rep['rep']} truth gaps recompute",
              abs(E.total(inv)
                  - rep["truth_objective_enriched"]) < 1e-6
              and abs(E.base(inv)
                      - rep["truth_objective_base"]) < 1e-6
              and abs((e_cand - rep["truth_objective_enriched"])
                      - rep["objective_gap_enriched"]) < 1e-6
              and abs((l_cand - rep["truth_objective_base"])
                      - rep["objective_gap_base"]) < 1e-6)
        # calibration recomputation: the search's own preamble
        pos = H.positional_counts(deriv)
        det = H.detect_restricted(pos, 0.95)
        det_i = {s for s, c in det.items() if c == "initial"}
        det_f = {s for s, c in det.items() if c == "final"}
        adm = admissible_map(Hmod, corp["family"], det_i, det_f)
        adm_copy = {s: set(a) for s, a in adm.items()}
        rng0 = random.Random(f"{seed}-g1e-init0")
        phi_freq = Hmod._initial_assignment(
            rng0, dict(anchors_sv), adm_copy, deriv,
            corp["family"], freq_init=True)
        dhat, draws = G.measure_delta_scale(
            E, phi_freq, adm_copy, dict(anchors_sv),
            f"{seed}-g1e-calib")
        check(f"rep {rep['rep']} delta-hat recompute",
              dhat == rep["g1_info"]["delta_hat"]
              and draws == rep["g1_info"]["calib_draws"],
              f"({dhat:.4f} over {draws} draws)")
        rec = H.recovery_g1(cand, perm, set(anchors_sv),
                            token_counts)
        check(f"rep {rep['rep']} recovery recompute",
              rec["recovery"] == rep["g1_recovery"]["recovery"]
              and rec["hits"] == rep["g1_recovery"]["hits"]
              and rec["denominator"]
              == rep["g1_recovery"]["denominator"])
        anat = G.anatomy(cand, perm, truth, set(anchors_sv),
                         token_counts)
        check(f"rep {rep['rep']} anatomy recompute",
              anat == rep["anatomy"])
        # margins recomputation with the filed seeds
        rng_der = random.Random(seed + "-derange")
        der = list(range(NV))
        while True:
            rng_der.shuffle(der)
            if all(der[v] != v for v in range(NV)):
                break
        phi_wrong = [der[inv[s]] for s in range(NV)]
        rng_sa = random.Random(seed + "-shufassign")
        free_signs = [s for s in range(NV) if s not in anchors_sv]
        sa_vals = [cand[s] for s in free_signs]
        rng_sa.shuffle(sa_vals)
        phi_shuffle = list(cand)
        for s, v in zip(free_signs, sa_vals):
            phi_shuffle[s] = v
        mg = H.g1_margins(corp["family"], reserve, cand,
                          phi_wrong, phi_shuffle)
        n_free = NV - len(anchors_sv)
        best_rival_total = min(mg["rivals"].values())
        penalized = mg["margin_raw"] - 2 * n_free
        p99, _dist = H.g1_null(corp["family"], reserve, cand,
                               anchors_sv, best_rival_total,
                               n_free, seed + "-null")
        fm = rep["g1_margin"]
        check(f"rep {rep['rep']} margin recompute",
              mg["margin_raw"] == fm["margin_raw"]
              and penalized == fm["penalized_margin"]
              and p99 == fm["null_p99"]
              and fm["free_choices"] == n_free
              and fm["pass"] == bool(penalized >= 10
                                     and penalized > p99),
              f"(penalized {penalized:.2f}, p99 {p99:.2f})")
        # shuffle control by deterministic re-execution
        rng_s2 = random.Random(seed + "-g1shuffle")
        shuf_deriv = []
        for g in deriv:
            gg = list(g)
            rng_s2.shuffle(gg)
            shuf_deriv.append(gg)
        pos_sh = H.positional_counts(shuf_deriv)
        det_sh = H.detect_restricted(pos_sh, 0.95)
        phi_s, info_s = G.g1e_search(
            Hmod, shuf_deriv, corp["family"], anchors_sv,
            {s for s, c in det_sh.items() if c == "initial"},
            {s for s, c in det_sh.items() if c == "final"},
            seed + "-g1eshuf")
        rec_s = H.recovery_g1(phi_s, perm, set(anchors_sv),
                              token_counts)
        check(f"rep {rep['rep']} shuffle re-execution",
              info_s["delta_hat"] == rep["g1_shuffle_delta_hat"]
              and rec_s["recovery"]
              == rep["g1_shuffle_recovery"]["recovery"],
              f"(recovery {rec_s['recovery']:.3f})")
        recs.append(rep["g1_recovery"]["recovery"])
        shuf_recs.append(rep["g1_shuffle_recovery"]["recovery"])
        margin_pass.append(rep["g1_margin"]["pass"])
    med = median(recs)
    med_shuf = median(shuf_recs)
    order = sorted(range(len(recs)), key=lambda i: recs[i])
    clause_ii_median_rep = bool(margin_pass[order[len(recs) // 2]])
    expect = {
        "clause_i_recovery": bool(med >= 0.80),
        "clause_ii_margin": bool(sum(margin_pass) >= 3),
        "shuffle_control": bool(med_shuf < 0.5 * med),
    }
    expect["verdict"] = ("PASSED" if all(expect.values())
                         else "FAILED")
    check("summary medians recompute",
          raw["summary"]["g1_recovery_median"] == med
          and raw["summary"]["g1_shuffle_recovery_median"]
          == med_shuf
          and raw["summary"]["g1_margin_pass_reps"]
          == sum(margin_pass))
    check("verdict block recompute (filed rule)",
          raw["summary"]["verdicts"] == expect, f"({expect})")
    check("clause (ii) under the median-replication reading",
          clause_ii_median_rep
          == raw["summary"]["verdicts"]["clause_ii_margin"],
          f"(median replication clears: {clause_ii_median_rep})")
    if k > 1:
        check("diagnostic-only flag", raw["summary"].get(
            "diagnostic_only") is True)

    def walk(o):
        if isinstance(o, dict):
            for kk, vv in o.items():
                yield kk
                yield from walk(vv)
        elif isinstance(o, list):
            for vv in o:
                yield from walk(vv)
    bad = [kk for kk in walk(raw) if "indus" in kk.lower()]
    check("raw output carries no undeciphered-material keys",
          not bad, f"({bad})")
    print("TC-109-02:", "PASS" if not failures else
          f"FAIL ({len(failures)} checks)", flush=True)
    return 0 if not failures else 1


if __name__ == "__main__":
    sys.exit(main())
