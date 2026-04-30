## ISSUE_015 — Phase 3B Price Exposure Validation

Goal:
Validate that Phase 3B does not only select the PHASE3B_* transition phrase, but also exposes actual approved price/range through PRICE_LADDER_ENGINE.

## Status
FUNCTIONALLY RESOLVED / MONITORED — updated 2026-04-30

## Current evidence

### PPF front Phase3B price
Report:
- tests/reports/raw_uat_20260430_115941.json

Confirmed:
- selected_phrase_id = PHASE3B_PPF_RANGE
- service_intent / active_service_context = ppf
- PPF_COVERAGE_INTENT = FULL_FRONT
- PPF_DRIVING_PATTERN = HIGHWAY
- selected_skus = [PPF_FRONT_GLOBAL]
- price_source_rows = PPF_FRONT_GLOBAL / VCB_2 / PRICE 295
- price_ladder_state = FINAL_PRICE_REACHED
- customer-facing price rendered as 295 Bahraini Dinars VAT included
- no full-body leakage observed

Note:
- Test was strengthened to forbid 790 / 880 / GLOBAL_SIGNATURE_10Y / GLOBAL_ELITE_8Y.
- Exact “BD VAT included” wording is not required when “Bahraini Dinars VAT included” is rendered.

### Ceramic Phase3B price
Report:
- tests/reports/raw_uat_20260430_112719.json

Confirmed:
- selected_phrase_id = PHASE3B_CERAMIC_RANGE
- selected_skus = [CERAMIC_1Y, CERAMIC_3Y]
- price_source_rows = CERAMIC_1Y / CERAMIC_3Y using VCB_2 prices 100 / 130
- QUALIFICATION_STATUS = READY_FOR_NEGOTIATION
- price_ladder_state = FINAL_PRICE_REACHED

### Tint Phase3B price
Report:
- tests/reports/raw_uat_20260430_113304.json

Confirmed:
- selected_phrase_id = PHASE3B_TINT_RANGE
- selected_skus = [TINT_NANO_CERAMIC, TINT_XPEL_XR_PLUS]
- price_source_rows = TINT_NANO_CERAMIC 130 / TINT_XPEL_XR_PLUS 220
- QUALIFICATION_STATUS = READY_FOR_NEGOTIATION
- price_ladder_state = FINAL_PRICE_REACHED

### Polishing Phase3B price
Report:
- tests/reports/raw_uat_20260430_110143.json

Confirmed:
- PASS after final Route E polishing execution lock + runner contradiction guards
- selected_phrase_id = PHASE3B_POLISHING_RANGE
- selected_skus exact/non-empty enforced by runner
- FINAL_PRICE_REACHED with selected_skus=[] now fails
- POLISH_GOLD forbidden for standard exterior polishing price

## Classification
- Phase3B price exposure is functionally validated across PPF, Ceramic, Tint, and Polishing.
- Determinism remains monitored because not every service has fresh 3x post-final-patch proof.

## Control decision
- Do not block M5 on ISSUE_015.
- Do not mark full deterministic stability unless 3x is intentionally run for the target service.
