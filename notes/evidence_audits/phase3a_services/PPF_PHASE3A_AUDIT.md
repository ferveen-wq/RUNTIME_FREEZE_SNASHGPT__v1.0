# PPF — PHASE 3A EVIDENCE AUDIT

Status: VERIFIED
Phase: 3A
Service: PPF

## CURRENT LIVE RUNTIME

### Qualification signals
- request_type
- service_intent
- active_service_context
- missing_fields
- phase3a_required
- phase3a_complete
- phase3a_qualifier_id

### Signal ownership
- QUALIFICATION_ENGINE.md is the effective final writer of:
  - phase3a_required
  - phase3a_complete
  - phase3a_qualifier_id
- Qualification layer also controls:
  - request_type
  - service_intent
  - active_service_context
  - missing_fields

### Entry trigger
- Phase 3A runs after Phase 0–2 is complete
- Requires:
  - service_intent
  - vehicle_model
  - vehicle_year
- No pricing allowed in Phase 3A

### PPF qualifier sequence
- Q1 → PHASE3A_Q_PPF_COVERAGE_INTENT
- Q2 → PHASE3A_Q_PPF_DRIVING_PATTERN
- Q3 → PHASE3A_Q_PPF_COMPARISON_FOCUS (conditional only)

### One-question rule
- Architecture states one question per assistant turn
- If phase3a_required == true, assembly must output exactly one Phase 3A qualifier question and stop

### Fallback behavior
- If user ignores current qualifier and pushes price / changes topic:
  - nudge once
  - repeat same qualifier
- If still unresolved, matrix allows safe progression through known/unknown handling

### Dependencies
- GLOBAL_VEHICLE_CLASSIFICATION_REPOSITORY.md
- GLOBAL_CORE_CONTEXT_PARAMETERS.md
- CONVERSATION_DYNAMIC_PARAMETERS.md
- PHASE3A_QUALIFICATION_DECISION_MATRIX.md

### Downstream handoff
- Phase 3B readiness for PPF when:
  - PPF_COVERAGE_INTENT is known (or UNSURE)
  - PPF_DRIVING_PATTERN is known (or UNKNOWN)
- Phase 3B must not execute until phase3a_complete == true

## EFFECTIVE CONTROL CHAIN

- Qualification writer → QUALIFICATION_ENGINE.md
- Qualifier order / gating → PHASE3A_QUALIFICATION_DECISION_MATRIX.md
- Architecture enforcement → 01_SYSTEM_OPERATING_MODEL.md + 02_OWNERSHIP_MODEL.md
- Downstream render gating → assembly only after Phase 3A completion

## HISTORICAL CONTEXT

- Not required yet for current PPF Phase 3A audit
- Current live runtime is sufficiently explicit in engine + matrix + architecture

## GAP CANDIDATE

- None confirmed yet from this first PPF Phase 3A pass

## CONCLUSION

PPF Phase 3A currently behaves as:
- qualification/state-owned, not phrase-owned
- QUALIFICATION_ENGINE is the final writer of Phase 3A state
- qualifier order is explicitly locked in the decision matrix
- one-question and no-pricing rules are architecture-backed
- handoff to Phase 3B is blocked until Phase 3A completion
