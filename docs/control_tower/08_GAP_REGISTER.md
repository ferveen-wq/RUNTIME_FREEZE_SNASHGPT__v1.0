# GAP REGISTER



## GAP — Deferred-family prompt routing residual drift (2026-04-21)

### Type
Prompt-routing / ownership-to-phrase mismatch

### Evidence
- tests/reports/uat_report_20260421_143821.json

### Observed behavior
- Deferred-family inputs (thinking / later / approval / travel / car unavailable) are recognized
- But not consistently routed to safe exit / open-door handling
- Some cases still fall into:
  - generic service deepen
  - wrong service-family phrases
  - Phase 4 silence fallback (AR salary case)

### Residual drift cases
- car_unavailable_en -> PHASE5_POLISH_EXPECTATION_DEEPEN_L1
- salary_ar -> PHASE4_PPF_SILENCE_PRIMARY
- partner_ar -> PHASE5_CERAMIC_PRICE_GAP_DEEPEN_L1
- travel_ar -> PHASE5_TINT_COMPARE_DEEPEN_L1

### Correct behavior (target)
- All deferred-family cases should:
  - avoid generic deepen branches
  - avoid service-family price-gap logic
  - prefer exit / open-door / pause-safe handling

### Interpretation
- Ownership mapping is now correct (Phase 3 + Phase 5)
- First prompt-routing patch improved behavior
- Remaining issue is localized fallthrough inside service routers

### Status
OPEN — narrowed (post first routing patch)

## GAP-022 — Deferred-family routing partially corrected, residual cross-service + Arabic drift remains
Status: RESOLVED (probe-pack scope)
Last Updated: 2026-04-22
Owner: Runtime / Prompt Bridge / Late-Stage Routing

Evidence:
- tests/reports/uat_report_20260421_143821.json
- tests/reports/uat_report_20260422_035318.json

What improved:
- THINKING_EN -> PHASE5_PPF_EXIT_FORK_L3
- PARTNER_EN -> PHASE5_PPF_EXIT_FORK_L3
- NOT_RECEIVED_AR -> PHASE5_PPF_EXIT_FORK_L3

Residual failures:
- CAR_UNAVAILABLE_EN -> PHASE5_POLISH_EXPECTATION_DEEPEN_L1
- SALARY_AR -> PHASE4_PPF_SILENCE_PRIMARY
- PARTNER_AR -> C.2 CERAMIC EXPLANATION + QUALIFIER (PHASE 0–2)
- TRAVEL_AR -> PHASE5_TINT_COMPARE_DEEPEN_L1
- TRAVEL_EN -> PPF exit instead of ceramic-family exit

Reading:
- This is no longer a broad deferred-family ambiguity.
- It is now a narrower routing defect affecting:
  - service-family isolation
  - Arabic late-stage handling
  - Phase 4 silence leakage for timing/salary cases

Rule:
- Do not reopen broad phrase hunting.
- Next patch lane should isolate:
  1) polishing car-unavailable handling
  2) tint travel handling
  3) Arabic partner-approval late-stage preservation
  4) salary/timing leakage into Phase 4 silence

Update:
- tests/reports/uat_report_20260422_035906.json

Resolution reading:
- The previously isolated residual drift no longer reproduces in the active deferred-family classification probe pack.
- Fixed cases include:
  - CAR_UNAVAILABLE_EN
  - SALARY_AR
  - PARTNER_AR
  - TRAVEL_AR
  - TRAVEL_EN

Closure rule:
- Treat GAP-022 as resolved for the current probe-pack scope.
- Keep caution that broader regression coverage is still required before calling this universally rollout-complete.

