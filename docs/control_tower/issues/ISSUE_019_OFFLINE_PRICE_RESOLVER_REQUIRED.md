# ISSUE_019 — Offline price resolver required before further Phase 3B price UAT

## Finding — 2026-04-27

Repeated live UAT against `ceramic_vcb1_civic` showed shifting wrong outputs:
- non-table ranges
- wrong ceramic SKU pair
- correct VCB but wrong age-band SKU selection

Offline deterministic resolver confirmed the expected trace:
- vehicle_year = 2020
- CURRENT_YEAR = 2026
- vehicle_age = 6
- ceramic_pricing_age_band = AGE_3_6
- selected_skus = [CERAMIC_1Y, CERAMIC_3Y]
- VCB_1 prices = [90, 120]
- final range = 90 to 120 BD VAT included

## Decision

Stop using live LLM UAT to discover deterministic price logic bugs.

Pricing UAT must follow this order:
1. Offline resolver calculates expected trace.
2. UAT case expectations are generated/checked against offline trace.
3. Live UAT is run once as confirmation.
4. If live output differs from offline trace, classify as runtime obedience/output contract failure.

## Status

OPEN — resolver currently covers ceramic only.
Next required work:
- Expand `runner/price_resolver_offline.py` to PPF, tint, polishing.
- Add runner precheck to compare pricing UAT cases against offline resolver before API calls.

## Validation Evidence — Offline Resolver Baseline — 2026-04-27

Offline resolver successfully produced expected deterministic traces:

- ceramic_vcb1_civic:
  - VCB_1
  - selected_skus = [CERAMIC_1Y, CERAMIC_3Y]
  - price range = 90 to 120

- ppf_camry_vcb2:
  - VCB_2
  - selected_skus = [GLOBAL_SIGNATURE_10Y, GLOBAL_ELITE_8Y]
  - price range = 790 to 880

- ppf_xpel_camry:
  - VCB_2
  - selected_skus = [XPEL_EXO_7Y, GLOBAL_SIGNATURE_10Y]
  - price range = 880 to 1040

- tint_camry_vcb2:
  - selected_skus = [TINT_NANO_CERAMIC, TINT_XPEL_XR_PLUS]
  - price range = 110 to 220

- polishing_camry_vcb2:
  - selected_skus = [POLISH_SILVER]
  - price = 50

Decision:
- Add resolver preflight before further live pricing UAT.
