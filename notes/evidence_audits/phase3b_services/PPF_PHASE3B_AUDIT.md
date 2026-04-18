# PPF — PHASE 3B EVIDENCE AUDIT

Status: VERIFIED
Phase: 3B
Service: PPF

## CURRENT LIVE RUNTIME

### Readiness gate
- Phase 3B readiness for PPF is defined in PHASE3A_QUALIFICATION_DECISION_MATRIX.md:
  - PPF_COVERAGE_INTENT is known (or UNSURE)
  - PPF_DRIVING_PATTERN is known (or UNKNOWN)

### Qualification completion dependency
- RUNTIME_EXECUTION_FLOW.md requires:
  - run Phase 3A before Phase 3B pricing/SKU logic
- If phase3a_required == true:
  - assembly must output exactly one Phase 3A qualifier question and STOP
- If phase3a_complete == true:
  - proceed to Phase 3B pricing/SKU selection and subsequent Phase 4 responses

### Price-entry condition
- PRICE_LADDER_ENGINE.md executes only if:
  - QUALIFICATION_STATUS == READY_FOR_NEGOTIATION
  - OR QUALIFICATION_STATUS == READY
- Runtime architecture/orchestration currently treats READY_FOR_NEGOTIATION as the primary progression gate
- PHASE4_8_MESSAGE_ASSEMBLY_MAP.md Route E requires:
  - request_type == PRICE_REQUEST
  - QUALIFICATION_STATUS == READY_FOR_NEGOTIATION
  - ((phase3a_required == false) OR (phase3a_complete == true))
  - all qualification fields complete

### Negotiation influence
- NEGOTIATION_LOGIC_MODULE.md executes only when:
  - QUALIFICATION_STATUS == READY_FOR_NEGOTIATION
- It materially affects Phase 3B as upstream signal/framing authority
- It emits pricing-relevant pressure signals including:
  - PRICE_PRESSURE_LEVEL = LOW | MEDIUM | HIGH

### Price ladder ownership
- PRICE_LADDER_ENGINE.md is the sole writer of:
  - price_ladder_state
- It must always set price_ladder_state before exiting
- Terminal states are defined inside PRICE_LADDER_ENGINE.md
- Assembly/template are forbidden to write price_ladder_state

### Dependency usage
- Numeric pricing authority:
  - PRICE_TABLE_VAT_INCL.md
- SKU ordering / selection dependency:
  - SKU_SELECTION_MATRIX.md
- Additional bounded support dependencies in pricing surface:
  - GLOBAL_CORE_CONTEXT_PARAMETERS.md
  - CONVERSATION_DYNAMIC_PARAMETERS.md
  - GLOBAL_PRODUCT_NAMING_REGISTRY_v1.0.md
  - PRODUCT_SERVICE_CANON.md

### Downstream handoff
- PHASE4_8_MESSAGE_ASSEMBLY_MAP.md Route E:
  - selects appropriate PHASE3B_* acknowledgement block
  - uses PRICE_LADDER_ENGINE.md output
- For PPF price-ready path:
  - PHASE3B_PPF_RANGE is the mapped phrase block
- runner/context_reset_prompt.txt hardens the PPF price-ready path:
  - selected_phrase_id MUST equal PHASE3B_PPF_RANGE
  - override must not apply unless QUALIFICATION_STATUS == READY_FOR_NEGOTIATION
- runner/run_uat.py flags contradiction if:
  - PHASE3B_PPF_RANGE appears while q_status != READY_FOR_NEGOTIATION

## EFFECTIVE CONTROL CHAIN

- Phase 3A qualifier completion → PHASE3A_QUALIFICATION_DECISION_MATRIX.md
- Qualification state writer → QUALIFICATION_ENGINE.md
- Runtime progression gate → RUNTIME_EXECUTION_FLOW.md / RUNTIME_STATE_MACHINE.md
- Negotiation signal/framing layer → NEGOTIATION_LOGIC_MODULE.md
- Pricing-state owner → PRICE_LADDER_ENGINE.md
- Price render routing → PHASE4_8_MESSAGE_ASSEMBLY_MAP.md
- Tested-lane hardening / contradiction checks → runner/context_reset_prompt.txt + runner/run_uat.py

## HISTORICAL CONTEXT

- No additional git recovery required for this first PPF Phase 3B pass
- Current runtime + architecture + tested-lane evidence are sufficient
- A known reconciliation point remains:
  - PRICE_LADDER_ENGINE.md tolerates QUALIFICATION_STATUS == READY
  - runtime architecture and tested lane treat READY_FOR_NEGOTIATION as the primary gate

## GAP CANDIDATE

- No new PPF-specific gap confirmed in this pass
- Existing READY vs READY_FOR_NEGOTIATION reconciliation remains the relevant cross-layer issue

## CONCLUSION

PPF Phase 3B currently behaves as:
- gated by Phase 3A completion
- gated operationally by READY_FOR_NEGOTIATION in runtime orchestration and tested lane
- influenced upstream by NEGOTIATION_LOGIC_MODULE pricing-pressure signals
- executed for pricing only through PRICE_LADDER_ENGINE.md
- rendered through PHASE4_8_MESSAGE_ASSEMBLY_MAP.md using PHASE3B_PPF_RANGE for the PPF price-ready path
- protected by runner contradiction checks that forbid PHASE3B_PPF_RANGE when status is not READY_FOR_NEGOTIATION
