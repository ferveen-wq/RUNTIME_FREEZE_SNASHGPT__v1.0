import json
from pathlib import Path

from price_resolver_offline import (
    resolve_ceramic,
    resolve_polishing,
    resolve_ppf,
    resolve_ppf_front,
    resolve_ppf_matte,
    resolve_tint,
)

CASES = {
    "ceramic_vcb1_civic": resolve_ceramic(2020, "VCB_1"),
    "ceramic_vcb1_civic_old": resolve_ceramic(2016, "VCB_1"),
    "ppf_full_body_range": resolve_ppf("VCB_2", "HIGHWAY", "DEFAULT"),
    "ppf_xpel_intent": resolve_ppf("VCB_2", "HIGHWAY", "XPEL"),
    "ppf_front_camry_vcb2": resolve_ppf_front("VCB_2"),
    "ppf_matte_camry_vcb2": resolve_ppf_matte("VCB_2"),
    "ppf_matte_xpel_camry_vcb2": resolve_ppf_matte("VCB_2", "XPEL"),
    "tint_price": resolve_tint("VCB_2"),
    "polishing_price": resolve_polishing("VCB_2"),
}

def main():
    p = Path("tests/active_rollout_uat/phase3b_multi_service_price.json")
    data = json.loads(p.read_text(encoding="utf-8"))

    failures = []

    for case in data:
        case_id = case.get("case_id")
        if case_id not in CASES:
            continue

        truth = CASES[case_id]
        expected_contains = set(str(x) for x in case.get("expect_contains", []))
        expected_debug = case.get("expect_debug", {})

        for price in truth["prices"]:
            if str(price) not in expected_contains:
                failures.append(f"{case_id}: missing expected price {price}")

        selected_skus = "[" + ", ".join(truth["selected_skus"]) + "]"
        if "selected_skus" in expected_debug and expected_debug["selected_skus"] != selected_skus:
            failures.append(
                f"{case_id}: selected_skus expected {expected_debug['selected_skus']} but resolver gives {selected_skus}"
            )

        if "VCB" in expected_debug and expected_debug["VCB"] != truth["VCB"]:
            failures.append(
                f"{case_id}: VCB expected {expected_debug['VCB']} but resolver gives {truth['VCB']}"
            )

    if failures:
        print("[FAIL] price preflight failed")
        for f in failures:
            print("-", f)
        raise SystemExit(1)

    print("[OK] price preflight passed")

if __name__ == "__main__":
    main()
