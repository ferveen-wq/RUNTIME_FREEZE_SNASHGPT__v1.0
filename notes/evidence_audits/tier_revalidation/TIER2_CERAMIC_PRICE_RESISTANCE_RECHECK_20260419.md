# TIER 2 — CERAMIC PRICE RESISTANCE RECHECK

Status: TRUSTED_FAILURE
Date: 2026-04-19

## Pack
- tests/uat/phase4_ceramic_price_resistance_strict_v2.json

## Result after runner trust fix
- FAILED

## Observed debug
- phase: 4
- request_type: OTHER
- objection_signal: PRICE_SENSITIVITY
- objection_repeat_count: 0
- selected_phrase_id: PHASE4_CERAMIC_PRICE_SENSITIVITY_L1
- QUALIFICATION_STATUS: READY_FOR_NEGOTIATION
- price_ladder_state: INITIAL

## Pack expectation
- selected_phrase_id: PHASE4_CERAMIC_PRICE_PRESSURE_L1

## Conclusion
After trusted-mode rerun, the ceramic price-resistance lane does not match the strict pack expectation.
The runtime selects PHASE4_CERAMIC_PRICE_SENSITIVITY_L1 instead of PHASE4_CERAMIC_PRICE_PRESSURE_L1.

## Classification
- Trusted failure
- Contract mismatch
- Parallel mismatch to the PPF price-resistance lane
