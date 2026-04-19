# HARNESS RESTORE CHECK — 2026-04-19

Status: RESTORE_CONFIRMED

## Patch
- runner/run_uat.py
- build_case_constraints() changed to no-op trusted mode
- expect_* fields no longer injected into generation prompt

## Sentinel rerun
Pack:
- notes/deferred_invalid_uat/_sentinel_should_fail_phase4_ppf_price_resistance_v1.json.invalid

Result:
- FAILED as expected

Observed debug:
- selected_phrase_id = PHASE4_PPF_PRICE_SENSITIVITY_L1

Conclusion:
- Sentinel falsification now behaves correctly
- expectation leakage path is no longer active in this runner mode
- post-generation validation is now meaningful again
