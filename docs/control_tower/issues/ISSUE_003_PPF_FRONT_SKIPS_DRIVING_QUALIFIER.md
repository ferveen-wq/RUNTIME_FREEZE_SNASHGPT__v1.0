# ISSUE_003 — PPF front coverage skips Phase 3A driving-pattern qualifier

## Type
Runtime Behavior Bug

## Affected Surface
Pending owner confirmation.

## Observed Clean Trace
Input turn 1:
`ppf camry 2022 front`

Actual:
- phase: 3B
- request_type: PRICE_REQUEST
- selected_phrase_id: PHASE3B_PPF_RANGE
- QUALIFICATION_STATUS: READY_FOR_NEGOTIATION

Expected:
- phase: 3A
- selected_phrase_id: PHASE3A_Q_PPF_DRIVING_PATTERN
- QUALIFICATION_STATUS: NOT_READY

## Why This Matters
PPF front coverage alone is not price-ready.
Driving pattern must still be captured before pricing.

## Scope Constraint
Do not patch until owner file is proven.

## Candidate Owners To Inspect
- QUALIFICATION_ENGINE.md
- PHASE3A_QUALIFICATION_DECISION_MATRIX.md
- RUNTIME_EXECUTION_FLOW.md
- PHASE4_8_MESSAGE_ASSEMBLY_MAP.md

## Status
OPEN

## Authority Finding — 2026-04-24

Owner-map evidence found two files writing/setting `PPF_DRIVING_PATTERN`:
- `CUSTOMER_CHAT_INTAKE_RULES.md`
- `QUALIFICATION_ENGINE.md`

Authority index does not explicitly list `PPF_DRIVING_PATTERN`, but it does state:
- `request_type`, `QUALIFICATION_STATUS`, `missing_fields`, `service_intent`, and `active_service_context` are owned by `QUALIFICATION_ENGINE.md`
- `CUSTOMER_CHAT_INTAKE_RULES.md` is forbidden from writing `request_type`

Current classification:
- Possible competing authority between Intake extraction and Qualification selection.
- Do not patch until authority boundary is clarified.
