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
