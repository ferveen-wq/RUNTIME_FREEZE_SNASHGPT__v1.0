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
