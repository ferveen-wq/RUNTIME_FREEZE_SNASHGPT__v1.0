CURRENT_YEAR = 2026

PRICE_TABLE = {
    "GLOBAL_LUXE_5Y": {"VCB_1": 550, "VCB_2": 630, "VCB_3": 730},
    "GLOBAL_ELITE_8Y": {"VCB_1": 750, "VCB_2": 790, "VCB_3": 890},
    "GLOBAL_SIGNATURE_10Y": {"VCB_1": 800, "VCB_2": 880, "VCB_3": 990},
    "XPEL_EXO_7Y": {"VCB_1": 920, "VCB_2": 1040, "VCB_3": 1100},
    "XPEL_UP_10Y": {"VCB_1": 1320, "VCB_2": 1340, "VCB_3": 1400},
    "GLOBAL_MATTE_10Y": {"VCB_1": 840, "VCB_2": 920, "VCB_3": 990},
    "XPEL_STEALTH_10Y": {"VCB_1": 1360, "VCB_2": 1460, "VCB_3": 1520},
    "PPF_FRONT_GLOBAL": {"VCB_1": 300, "VCB_2": 295, "VCB_3": 295},
    "GLOBAL_MATTE_FRONT_10Y": {"VCB_1": 350, "VCB_2": 450, "VCB_3": 525},

    "CERAMIC_1Y": {"VCB_1": 90, "VCB_2": 100, "VCB_3": 120},
    "CERAMIC_3Y": {"VCB_1": 120, "VCB_2": 130, "VCB_3": 150},
    "CERAMIC_5Y": {"VCB_1": 160, "VCB_2": 170, "VCB_3": 190},
    "GRAPHENE_1Y": {"VCB_1": 110, "VCB_2": 120, "VCB_3": 140},

    "TINT_NANO_CERAMIC": {"VCB_1": 80, "VCB_2": 110, "VCB_3": 110},
    "TINT_XPEL_XR_PLUS": {"VCB_1": 180, "VCB_2": 220, "VCB_3": 220},

    "POLISH_SILVER": {"VCB_1": 45, "VCB_2": 50, "VCB_3": 55},
}

PPF_MATRIX = {
    ("VCB_1", "DEFAULT", "HIGHWAY"): ["GLOBAL_ELITE_8Y", "GLOBAL_SIGNATURE_10Y"],
    ("VCB_2", "DEFAULT", "HIGHWAY"): ["GLOBAL_SIGNATURE_10Y", "GLOBAL_ELITE_8Y"],
    ("VCB_2", "XPEL", "HIGHWAY"): ["XPEL_EXO_7Y", "GLOBAL_SIGNATURE_10Y"],
    ("VCB_3", "DEFAULT", "HIGHWAY"): ["GLOBAL_SIGNATURE_10Y", "GLOBAL_ELITE_8Y"],
}

def price_result(service, vcb, selected_skus, **extra):
    prices = [PRICE_TABLE[sku][vcb] for sku in selected_skus]
    return {
        "service": service,
        "VCB": vcb,
        "selected_skus": selected_skus,
        "prices": prices,
        "range": (min(prices), max(prices)),
        "price_source_rows": [
            {"sku": sku, vcb: PRICE_TABLE[sku][vcb]} for sku in selected_skus
        ],
        **extra,
    }

def resolve_ceramic(vehicle_year, vcb):
    vehicle_age = CURRENT_YEAR - vehicle_year

    if vehicle_age <= 3:
        selected_skus = ["CERAMIC_3Y", "CERAMIC_5Y"]
        age_band = "AGE_0_3"
    elif 4 <= vehicle_age <= 6:
        selected_skus = ["CERAMIC_1Y", "CERAMIC_3Y"]
        age_band = "AGE_3_6"
    else:
        selected_skus = ["CERAMIC_1Y", "GRAPHENE_1Y"]
        age_band = "AGE_7_PLUS"

    return price_result(
        "ceramic",
        vcb,
        selected_skus,
        vehicle_year=vehicle_year,
        CURRENT_YEAR=CURRENT_YEAR,
        vehicle_age=vehicle_age,
        ceramic_pricing_age_band=age_band,
    )

def resolve_ppf(vcb, driving_pattern="HIGHWAY", brand_intent="DEFAULT"):
    selected_skus = PPF_MATRIX[(vcb, brand_intent, driving_pattern)]
    return price_result("ppf", vcb, selected_skus, driving_pattern=driving_pattern, brand_intent=brand_intent)

def resolve_ppf_front(vcb, finish_intent="GLOSS"):
    if finish_intent == "MATTE":
        return price_result("ppf_front", vcb, ["GLOBAL_MATTE_FRONT_10Y"], finish_intent=finish_intent)
    return price_result("ppf_front", vcb, ["PPF_FRONT_GLOBAL"], finish_intent=finish_intent)

def resolve_ppf_matte(vcb, brand_intent="DEFAULT"):
    if brand_intent == "XPEL":
        return price_result("ppf_matte", vcb, ["XPEL_STEALTH_10Y"], brand_intent=brand_intent, finish_intent="MATTE")
    return price_result("ppf_matte", vcb, ["GLOBAL_MATTE_10Y"], brand_intent=brand_intent, finish_intent="MATTE")

def resolve_tint(vcb):
    return price_result("tint", vcb, ["TINT_NANO_CERAMIC", "TINT_XPEL_XR_PLUS"])

def resolve_polishing(vcb):
    return price_result("polishing", vcb, ["POLISH_SILVER"])

if __name__ == "__main__":
    checks = {
        "ceramic_vcb1_civic": resolve_ceramic(2020, "VCB_1"),
        "ppf_camry_vcb2": resolve_ppf("VCB_2", "HIGHWAY", "DEFAULT"),
        "ppf_xpel_camry": resolve_ppf("VCB_2", "HIGHWAY", "XPEL"),
        "tint_camry_vcb2": resolve_tint("VCB_2"),
        "polishing_camry_vcb2": resolve_polishing("VCB_2"),
    }
    for name, result in checks.items():
        print(name, result)
