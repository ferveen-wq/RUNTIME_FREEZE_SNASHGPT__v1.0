# PHASE 0–3B FILE SURFACE SWEEP

Status: IN_PROGRESS

## Goal
Identify all files materially associated with:
- Phase 0–2
- Phase 3A
- Phase 3B

and classify them as:
- RUNTIME_AUTHORITY
- ENGINE_AUTHORITY
- ROUTING_RENDER_AUTHORITY
- DEPENDENCY_SUPPORT
- TESTED_LANE_ENFORCEMENT
- REFERENCE_ONLY

## Open questions
- Does NEGOTIATION_LOGIC_MODULE.md materially affect Phase 3B readiness or only upstream framing?
- Are any Phase 3 lock/addendum/state files still not reflected in architecture docs?
- Are any dependency files being consumed without being clearly classified in architecture docs?

## Classified surface (current evidence)

### RUNTIME_AUTHORITY
- 00__LOCKED__UPLOAD_SET/00__Runtime/GLOBAL_RUNTIME_FLOW_MAP.md
- 00__LOCKED__UPLOAD_SET/00__Runtime/RUNTIME_EXECUTION_FLOW.md
- 00__LOCKED__UPLOAD_SET/00__Runtime/RUNTIME_STATE_MACHINE.md
- 00__LOCKED__UPLOAD_SET/00__Runtime/AUTHORITY_INDEX.md
- 00__LOCKED__UPLOAD_SET/00__Runtime/PHASE3_LOCK_INDEX.md
- 00__LOCKED__UPLOAD_SET/00__Runtime/PHASE3_ORCHESTRATION_WIRING_ADDENDUM.md
- 00__LOCKED__UPLOAD_SET/00__Runtime/RUNTIME_LOAD_MANIFEST.md

### ENGINE_AUTHORITY
- 00__LOCKED__UPLOAD_SET/01__Engines/QUALIFICATION_ENGINE.md
- 00__LOCKED__UPLOAD_SET/01__Engines/NEGOTIATION_LOGIC_MODULE.md
- 00__LOCKED__UPLOAD_SET/01__Engines/PRICE_LADDER_ENGINE.md
- 00__LOCKED__UPLOAD_SET/01__Engines/OBJECTION_RESOLUTION_ENGINE.md

### ROUTING_RENDER_AUTHORITY
- 00__LOCKED__UPLOAD_SET/00__Runtime/PHASE4_8_MESSAGE_ASSEMBLY_MAP.md
- 00__LOCKED__UPLOAD_SET/00__Runtime/OUTPUT_RESPONSE_TEMPLATE.md
- 00__LOCKED__UPLOAD_SET/00__Runtime/PHASE4_6_HUMAN_PHRASE_LIBRARY.md

### DEPENDENCY_SUPPORT
- 00__LOCKED__UPLOAD_SET/03__Parameters/SKU_SELECTION_MATRIX.md
- 00__LOCKED__UPLOAD_SET/03__Parameters/PRICE_TABLE_VAT_INCL.md
- 00__LOCKED__UPLOAD_SET/03__Parameters/GLOBAL_CORE_CONTEXT_PARAMETERS.md
- 00__LOCKED__UPLOAD_SET/03__Parameters/CONVERSATION_DYNAMIC_PARAMETERS.md
- 00__LOCKED__UPLOAD_SET/02__Repositories/PRODUCT_SERVICE_CANON.md
- 00__LOCKED__UPLOAD_SET/02__Repositories/GLOBAL_PRODUCT_NAMING_REGISTRY_v1.0.md
- 00__LOCKED__UPLOAD_SET/02__Repositories/GLOBAL_VEHICLE_CLASSIFICATION_REPOSITORY.md

### TESTED_LANE_ENFORCEMENT
- runner/context_reset_prompt.txt
- runner/run_uat.py
- runner/phrase_library_validator.py
- runner/runtime_diff_sentinel.py

## Key findings

- NEGOTIATION_LOGIC_MODULE.md is materially part of the Phase 3B surface as upstream signal/framing authority.
- PRICE_LADDER_ENGINE.md remains the sole pricing-state owner for price_ladder_state.
- PHASE3_LOCK_INDEX.md and PHASE3_ORCHESTRATION_WIRING_ADDENDUM.md are materially relevant and should not be omitted from Phase 3B due diligence.
- Runtime, architecture, and tested-lane enforcement still show a READY vs READY_FOR_NEGOTIATION reconciliation point.
