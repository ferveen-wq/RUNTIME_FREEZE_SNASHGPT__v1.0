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

## Cross-Service Authority Evidence — 2026-04-24

Owner-map comparison across Phase 3A parameters:

PPF:
- `PPF_COVERAGE_INTENT` has writers in:
  - `CUSTOMER_CHAT_INTAKE_RULES.md`
  - `QUALIFICATION_ENGINE.md`
- `PPF_DRIVING_PATTERN` has writers in:
  - `CUSTOMER_CHAT_INTAKE_RULES.md`
  - `QUALIFICATION_ENGINE.md`

Ceramic:
- `CERAMIC_GOAL` and `CERAMIC_WASH_PATTERN` are governed by `QUALIFICATION_ENGINE.md` selection logic.
- No Intake writer surfaced in owner-map output.

Tint:
- `TINT_GOAL` is governed by `QUALIFICATION_ENGINE.md` selection logic.
- No Intake writer surfaced in owner-map output.

Conclusion:
PPF has a unique competing-authority risk not mirrored in Ceramic/Tint.
Likely architecture correction:
- `CUSTOMER_CHAT_INTAKE_RULES.md` may extract same-message hints.
- `QUALIFICATION_ENGINE.md` must remain the final qualification-state owner for Phase 3A readiness and qualifier sequencing.

Patch decision:
Do not patch until the exact boundary wording is defined and validation is set.

## Debug Method Lesson — 2026-04-24

Attempted temporary `print(...)` debug inside `QUALIFICATION_ENGINE.md` active runtime copy.

Result:
- No debug output appeared.
- Runtime `.md` files are instruction surfaces, not executable Python.
- This method is invalid and must not be repeated.

Updated investigation rule:
- Do not insert executable-style debug into runtime markdown files.
- Use runner-level tracing, report inspection, owner-map, and deterministic test repetition instead.

Latest active trace:
- `phase3b_ppf_price_trace.json` reran as active case and passed 1/1.
- This supports current classification as intermittent execution/obedience instability, not a deterministic written-rule defect.
