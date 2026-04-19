# HARNESS SENTINEL FAILURE — 2026-04-19

Status: CRITICAL
Confidence impact: HIGH

## Sentinel design
A deliberately false expectation pack was created:

- input: "too expensive"
- objection_signal: PRICE_SENSITIVITY
- false expected selected_phrase_id: PHASE4_PPF_WARRANTY_SENSITIVITY_L1

This pack should have FAILED if the harness were independently validating output.

## Observed result
- UAT done. Passed=1, Failed=0, Total=1
- selected_phrase_id returned: PHASE4_PPF_WARRANTY_SENSITIVITY_L1

## Why this is critical
The sentinel expectation was intentionally wrong, yet the system returned the wrong value and passed.

This strongly suggests one or more of:
- expectation leakage into the model prompt
- self-fulfilling prompt constraints
- non-independent validation path

## Immediate decision
- Stop treating current green UAT passes as trusted rollout evidence
- Reclassify current green packs as: PROVISIONAL / TAINTED until harness audit is complete
- Shift active work from service validation to runner trust audit

## Next audit targets
- runner/run_uat.py
- build_case_constraints(...)
- inject_readonly_runtime_signals(...)
- runner/context_reset_prompt.txt
- any path where expect_debug / expect_not / case metadata may leak into generation prompt
