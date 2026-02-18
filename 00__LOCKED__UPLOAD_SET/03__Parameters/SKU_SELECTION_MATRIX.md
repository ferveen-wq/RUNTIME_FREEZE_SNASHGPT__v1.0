# PHASE 3 — SERVICE SELECTION MATRIX (LOCKED)

Applies to:
- PPF
- Ceramic Coating
- Graphene Coating
- Polishing (prep-only)

This file defines DEFAULT / SECOND / UPLADDER / DOWNLADDER logic.
No invention allowed. Use SKUs from GLOBAL_PRODUCT_NAMING_REGISTRY only.

────────────────────────────────────────────
1) PPF — PAINT PROTECTION FILM
────────────────────────────────────────────

Rules (Global):
- Coverage default = FULL BODY
- Front PPF is NEVER named unless customer is cost-conscious or asks
- Brand is surfaced ONLY if explicitly requested
- Driving pattern affects ordering (CITY vs HIGHWAY)

──────────────
VCB_1 — DAILY / MID SEGMENT
──────────────

VCB_1 | DEFAULT | CITY
- Default (A): GLOBAL_LUXE_5Y
- Second (B): GLOBAL_ELITE_8Y
- Upladder: GLOBAL_SIGNATURE_10Y
- Downladder: PPF_FRONT_GLOBAL

VCB_1 | DEFAULT | HIGHWAY
- Default (A): GLOBAL_ELITE_8Y
- Second (B): GLOBAL_SIGNATURE_10Y
- Upladder: XPEL_EXO_7Y
- Downladder: GLOBAL_LUXE_5Y

VCB_1 | XPEL | CITY
- Default (A): XPEL_EXO_7Y
- Second (B): GLOBAL_ELITE_8Y
- Upladder: XPEL_UP_10Y
- Downladder: GLOBAL_LUXE_5Y

VCB_1 | XPEL | HIGHWAY
- Default (A): XPEL_EXO_7Y
- Second (B): GLOBAL_SIGNATURE_10Y
- Upladder: XPEL_UP_10Y
- Downladder: GLOBAL_ELITE_8Y

──────────────
VCB_2 — PREMIUM SEGMENT
──────────────

VCB_2 | DEFAULT | CITY
- Default (A): GLOBAL_ELITE_8Y
- Second (B): GLOBAL_LUXE_5Y
- Upladder: GLOBAL_SIGNATURE_10Y
- Downladder: PPF_FRONT_GLOBAL

VCB_2 | DEFAULT | HIGHWAY
- Default (A): GLOBAL_SIGNATURE_10Y
- Second (B): GLOBAL_ELITE_8Y
- Upladder: XPEL_EXO_7Y
- Downladder: GLOBAL_LUXE_5Y

VCB_2 | XPEL | CITY
- Default (A): XPEL_EXO_7Y
- Second (B): GLOBAL_ELITE_8Y
- Upladder: XPEL_UP_10Y
- Downladder: GLOBAL_LUXE_5Y

VCB_2 | XPEL | HIGHWAY
- Default (A): XPEL_EXO_7Y
- Second (B): GLOBAL_SIGNATURE_10Y
- Upladder: XPEL_UP_10Y
- Downladder: GLOBAL_ELITE_8Y

──────────────
VCB_3 — LUXURY SEGMENT
──────────────

VCB_3 | DEFAULT | CITY
- Default (A): GLOBAL_ELITE_8Y
- Second (B): GLOBAL_SIGNATURE_10Y
- Upladder: XPEL_EXO_7Y
- Downladder: GLOBAL_LUXE_5Y

VCB_3 | DEFAULT | HIGHWAY
- Default (A): GLOBAL_SIGNATURE_10Y
- Second (B): GLOBAL_ELITE_8Y
- Upladder: XPEL_UP_10Y
- Downladder: GLOBAL_LUXE_5Y

VCB_3 | XPEL | CITY
- Default (A): XPEL_EXO_7Y
- Second (B): GLOBAL_SIGNATURE_10Y
- Upladder: XPEL_UP_10Y
- Downladder: GLOBAL_ELITE_8Y

VCB_3 | XPEL | HIGHWAY
- Default (A): XPEL_UP_10Y
- Second (B): XPEL_EXO_7Y
- Upladder: XPEL_FUSION_10Y
- Downladder: GLOBAL_SIGNATURE_10Y

──────────────
MATTE PPF (ALL SEGMENTS)
──────────────
- Default: GLOBAL_MATTE_10Y
- If brand explicitly requested: XPEL_STEALTH_10Y

────────────────────────────────────────────
2) CERAMIC & GRAPHENE — FULL BODY ONLY
────────────────────────────────────────────

Rules:
- No partial variants
- No polishing bundles
- Selection influenced by VEHICLE AGE
- Vehicle segment affects ORDER, not SKUs

──────────────
Vehicle Age 0–3 Years
──────────────
- Default (A): CERAMIC_3Y
- Second (B): CERAMIC_5Y
- Upladder: GRAPHENE_3Y
- Downladder: CERAMIC_1Y

──────────────
Vehicle Age 3–6 Years
──────────────
- Default (A): CERAMIC_1Y
- Second (B): CERAMIC_3Y
- Upladder: CERAMIC_5Y
- Downladder: GRAPHENE_1Y

──────────────
Vehicle Age 7+ Years
──────────────
- Default (A): CERAMIC_1Y
- Second (B): GRAPHENE_1Y
- Upladder: CERAMIC_3Y
- Downladder: NONE (paint correction gate upstream)

────────────────────────────────────────────
3) POLISHING — PREP ONLY (NOT A SKU LADDER)
────────────────────────────────────────────

Rules:
- Polishing is NEVER a standalone upsell
- Polishing is NEVER priced inside ladder
- Polishing is introduced as paint preparation only

──────────────
Vehicle Age 0–3
──────────────
- No polishing by default
- Mention only if swirls / defects are raised

──────────────
Vehicle Age 3–6
──────────────
- Light polishing may be required
- Framed as bonding & finish prep

──────────────
Vehicle Age 7+
──────────────
- Polishing required for ceramic / graphene
- If refused → conditional ladder or inspection path

────────────────────────────────────────────
4) WRAP — VEHICLE WRAP (FULL VEHICLE ONLY)
────────────────────────────────────────────

RULES (LOCKED):
- Wrap pricing is supported ONLY for FULL VEHICLE wrap.
- Partial/roof wrap SKUs must NOT be selected here.
- Roof-black styling is fulfilled ONLY via ROOF_PPF_BLACK_GLOSS (handled in PPF flow / roof rule), not via WRAP.

OUTPUT CONTRACT (used by PRICE_LADDER_ENGINE):
- WRAP_DEFAULT_A
- WRAP_SECOND_B

WRAP FINISH MAPPING (FULL VEHICLE):
- If WRAP_FINISH == GLOSS:
	WRAP_DEFAULT_A = WRAP_GLOSS
	WRAP_SECOND_B  = WRAP_MATTE
- If WRAP_FINISH == MATTE:
	WRAP_DEFAULT_A = WRAP_MATTE
	WRAP_SECOND_B  = WRAP_SATIN
- If WRAP_FINISH == SATIN:
	WRAP_DEFAULT_A = WRAP_SATIN
	WRAP_SECOND_B  = WRAP_MATTE
- If WRAP_FINISH == UNKNOWN:
	WRAP_DEFAULT_A = WRAP_GLOSS
	WRAP_SECOND_B  = WRAP_MATTE

────────────────────────────────────────────
END OF FILE — LOCKED
────────────────────────────────────────────
