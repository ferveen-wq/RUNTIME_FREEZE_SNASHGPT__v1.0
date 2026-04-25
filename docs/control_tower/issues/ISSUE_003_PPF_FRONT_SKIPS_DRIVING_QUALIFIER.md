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

## Final Classification Lock — 2026-04-24

After:
- authority scan
- cross-service comparison
- active rollout trace validation
- debug attempt (invalid method ruled out)

Conclusion:

- No deterministic failure reproduced in active trace
- Runtime logic behaves correctly under controlled conditions
- Prior inconsistent outcomes are attributed to:
  → execution / prompt obedience instability
  → NOT written-rule conflict

Decision:

- DO NOT patch:
  - CUSTOMER_CHAT_INTAKE_RULES.md
  - QUALIFICATION_ENGINE.md
  - PHASE3A_QUALIFICATION_DECISION_MATRIX.md

- ISSUE_003 is now:
  STATUS: MONITORED (NOT PATCHABLE)

Next action:
- Continue rollout stabilization
- Revisit only if:
  - deterministic reproduction appears
  - or failure rate crosses threshold in real logs



## Status Update — 2026-04-25
Status remains MONITORED / NOT PATCHABLE.
No deterministic runtime defect is confirmed. Reopen only if repeatable active raw evidence appears.

## Reopened Evidence — 2026-04-25

Status changed from MONITORED to REOPENED.

Reason:
- Active Phase 0–3 closeout raw UAT reproduced the same behavior again.

Evidence:
- Case: phase0_3_ppf_camry_2022_front_entry
- Input: ppf camry 2022 front
- Actual selected_phrase_id: PHASE3B_PPF_RANGE
- Actual QUALIFICATION_STATUS: READY_FOR_NEGOTIATION
- Expected selected_phrase_id: PHASE3A_Q_PPF_DRIVING_PATTERN
- Expected QUALIFICATION_STATUS: NOT_READY

Current classification:
- Runtime authority propagation / execution obedience issue.
- Do not patch again until deterministic owner is confirmed.

Next action:
- Run single-case targeted reproduction only.
- Avoid full-suite raw UAT until this issue is isolated.

## Deterministic Active Evidence Update — 2026-04-25

After enforcing active-only UAT and active-only owner-map defaults, the issue still reproduces.

Confirmed active evidence:
- UAT file: tests/active_rollout_uat/phase0_3_intake_matrix_probe_v1.json
- Case: phase0_3_ppf_camry_2022_front_entry
- Input: ppf camry 2022 front
- Actual:
  - QUALIFICATION_STATUS = READY_FOR_NEGOTIATION
  - selected_phrase_id = PHASE3B_PPF_RANGE
  - price_ladder_state = INITIAL
- Expected:
  - QUALIFICATION_STATUS = NOT_READY
  - selected_phrase_id = PHASE3A_Q_PPF_DRIVING_PATTERN
  - price_ladder_state = NONE

Classification update:
- Not old test-folder drift.
- Not locked-vs-active drift.
- Not ISSUE_006 assembly-only pattern, because readiness itself is wrong.
- Primary owner candidate is QUALIFICATION_ENGINE.md readiness/status gating.
- Secondary concern remains ISSUE_004 cross-service qualifier ownership normalization.

Patch direction:
- Strengthen Qualification Engine so any active Phase 3A qualifier requirement hard-forces:
  - phase3a_required = true
  - phase3a_complete = false
  - qualification_state = NOT_READY
  - QUALIFICATION_STATUS = NOT_READY
  - price_ladder_state = NONE
  - no Phase 3B readiness
