# RUNTIME FILE INVENTORY
Status: DRAFT
Purpose: Classify active runtime files by authority role before final architecture consolidation.

## Classification Buckets
- A = Runtime authority
- B = Engine authority
- C = Dependency / contract
- D = Phrase / content authority
- E = Governance / change-control
- F = Human playbook / support
- G = Draft / future / excluded
- H = Ignore

## Initial Inventory

### A — Runtime authority
- 00__Runtime/AUTHORITY_INDEX.md
- 00__Runtime/CUSTOMER_CHAT_INTAKE_RULES.md
- 00__Runtime/GLOBAL_RUNTIME_FLOW_MAP.md
- 00__Runtime/KNOWLEDGE__RUNTIME_CORE_BUNDLE.md
- 00__Runtime/PHASE3A_QUALIFICATION_DECISION_MATRIX.md
- 00__Runtime/PHASE3_ORCHESTRATION_WIRING_ADDENDUM.md
- 00__Runtime/PHASE4_8_MESSAGE_ASSEMBLY_MAP.md
- 00__Runtime/RUNTIME_EXECUTION_FLOW.md
- 00__Runtime/RUNTIME_LOAD_MANIFEST.md
- 00__Runtime/RUNTIME_STATE_MACHINE.md

### B — Engine authority
- 01__Engines/CLOSING_HANDOVER_ENGINE.md
- 01__Engines/NEGOTIATION_LOGIC_MODULE.md
- 01__Engines/OBJECTION_RESOLUTION_ENGINE.md
- 01__Engines/PRICE_LADDER_ENGINE.md
- 01__Engines/QUALIFICATION_ENGINE.md
- 01__Engines/SILENCE_HANDLING_ENGINE.md
- 01__Engines/PHASE_4_7_HOOK_QUESTION_ENGINE.md
- 01__Engines/phase_4_5_tone_engine.md

### C — Dependency / contract
- 02__Repositories/GLOBAL_PRODUCT_NAMING_REGISTRY_v1.0.md
- 02__Repositories/GLOBAL_VEHICLE_CLASSIFICATION_REPOSITORY.md
- 02__Repositories/PRODUCT_SERVICE_CANON.md
- 03__Parameters/CONVERSATION_DYNAMIC_PARAMETERS.md
- 03__Parameters/GLOBAL_CORE_CONTEXT_PARAMETERS.md
- 03__Parameters/PRICE_TABLE_VAT_INCL.md
- 03__Parameters/SKU_SELECTION_MATRIX.md

Dependency classification note:
- Manifest-proven active dependencies:
  - GLOBAL_VEHICLE_CLASSIFICATION_REPOSITORY.md
  - GLOBAL_CORE_CONTEXT_PARAMETERS.md
  - CONVERSATION_DYNAMIC_PARAMETERS.md
  - SKU_SELECTION_MATRIX.md
  - PRICE_TABLE_VAT_INCL.md
- Referenced but not yet manifest-proven as first-class load items:
  - GLOBAL_PRODUCT_NAMING_REGISTRY_v1.0.md
  - PRODUCT_SERVICE_CANON.md
- Repo evidence currently shows PRODUCT_SERVICE_CANON.md is consumed as a bounded dependency and is not yet manifest-proven as a runtime-active first-class load item.
- Therefore, Phase 0–6 rollout must distinguish:
  - manifest-active runtime authorities
  - support-authority dependencies
  - reference-only repo files not yet proven runtime-consumed


Phase 0–3B file-surface normalization note:
- Proven RUNTIME_AUTHORITY files for Phase 0–3B include:
  - GLOBAL_RUNTIME_FLOW_MAP.md
  - RUNTIME_EXECUTION_FLOW.md
  - RUNTIME_STATE_MACHINE.md
  - AUTHORITY_INDEX.md
  - PHASE3_LOCK_INDEX.md
  - PHASE3_ORCHESTRATION_WIRING_ADDENDUM.md
  - RUNTIME_LOAD_MANIFEST.md
- Proven ENGINE_AUTHORITY files for Phase 0–3B include:
  - QUALIFICATION_ENGINE.md
  - NEGOTIATION_LOGIC_MODULE.md
  - PRICE_LADDER_ENGINE.md
  - OBJECTION_RESOLUTION_ENGINE.md
- Proven ROUTING_RENDER_AUTHORITY files include:
  - PHASE4_8_MESSAGE_ASSEMBLY_MAP.md
  - OUTPUT_RESPONSE_TEMPLATE.md
  - PHASE4_6_HUMAN_PHRASE_LIBRARY.md
- Proven DEPENDENCY_SUPPORT files include:
  - SKU_SELECTION_MATRIX.md
  - PRICE_TABLE_VAT_INCL.md
  - GLOBAL_CORE_CONTEXT_PARAMETERS.md
  - CONVERSATION_DYNAMIC_PARAMETERS.md
  - PRODUCT_SERVICE_CANON.md
  - GLOBAL_PRODUCT_NAMING_REGISTRY_v1.0.md
  - GLOBAL_VEHICLE_CLASSIFICATION_REPOSITORY.md
- Proven TESTED_LANE_ENFORCEMENT files include:
  - runner/context_reset_prompt.txt
  - runner/run_uat.py
  - runner/phrase_library_validator.py
  - runner/runtime_diff_sentinel.py
- NEGOTIATION_LOGIC_MODULE.md must be treated as materially part of the Phase 3B surface as upstream signal/framing authority.
- PRICE_LADDER_ENGINE.md remains the sole pricing-state owner for price_ladder_state.
- PHASE3_LOCK_INDEX.md and PHASE3_ORCHESTRATION_WIRING_ADDENDUM.md are materially relevant and must not be omitted from Phase 3B due diligence.
- Runtime, architecture, and tested-lane enforcement still contain a READY vs READY_FOR_NEGOTIATION reconciliation point.


### D — Runtime truth / content authority
- 00__Runtime/PHASE4_6_HUMAN_PHRASE_LIBRARY.md
- 00__Runtime/PHASE6__SERVICE_CANON_BUNDLE.md
- 00__Runtime/PHASE7_EDUCATION_SNIPPETS.md
- 00__Runtime/PHASE7__CORE_EDUCATION.md
- 00__Runtime/PHASE8_VIDEO_LIBRARY.md
- 00__Runtime/VISUAL_PLAYBOOK.md
- 00__Runtime/EDUCATION_TRIGGER_MATRIX.md

Runtime truth/content classification note:
- PHASE4_6_HUMAN_PHRASE_LIBRARY.md is the locked customer-facing phrase authority.
- PHASE6__SERVICE_CANON_BUNDLE.md is manifest-proven runtime-active and provides bounded service-truth content for downstream runtime consumption.
- PHASE6__SERVICE_CANON_BUNDLE.md is not mere reference/support material.
- Customer-facing use of Phase 6 content remains subject to PHASE4_8_MESSAGE_ASSEMBLY_MAP.md and output/render constraints.
- PHASE7_EDUCATION_SNIPPETS.md is present in runtime truth/content surface as an education knowledge layer referenced by runtime-governed hook / explanation architecture.
- Current tested-lane proof for Phase 7 is narrower than full architecture scope: only REENTERED_CONTINUE is runner-proven today via prompt-bridge UAT.
- PHASE7__CORE_EDUCATION.md is broader concept/support architecture, not yet proven as a direct manifest-executed runtime owner.
- Phase 8 visual support now has three distinct evidence layers:
  - assembly-layer routing exists in PHASE4_8_MESSAGE_ASSEMBLY_MAP.md
  - tool-layer implementation exists (for example attach_visuals.py and related selectors/memory helpers)
  - approved asset registry exists in control-tower video files
  However, trusted-lane execution proof is still missing, so Phase 8 visual delivery must not yet be treated as trusted runtime rollout behavior.
- Phase 9 trust/persuasion references exist in repo architecture, but are not yet promoted as trusted runtime-active execution owners.

### E — Governance / change-control
- 00__Runtime/ARCHITECTURE_ROADMAP.md
- 00__Runtime/PATCH_PROTOCOL.md
- 00__Runtime/PHASE0_2_LOCK_INDEX.md
- 00__Runtime/PHASE0_LOCK_INDEX.md
- 00__Runtime/PHASE3_LOCK_INDEX.md
- 00__Runtime/PHASE4_LOCK_INDEX.md
- 00__Runtime/PHRASE_GOVERNANCE_STANDARD.md
- 00__Runtime/PHRASE_INDEX.md
- 00__Runtime/RUNTIME_CHANGE_LEDGER.md
- 00__Runtime/SNASHGPT_MASTER_GOVERNANCE.md

### F — Human playbook / support
- 03__Playbooks/PHASE0_TO_PHASE3__HUMAN_READABLE_MENTAL_MAP.md
- 03__Playbooks/PHASE0__ONE_SCREEN_VISUAL_MENTAL_MAP.md
- 03__Playbooks/PHASE7_TO_PHASE9_CONCEPT_EXTRACTION.md
- 03__Playbooks/PHASE7__CORE_EDUCATION.md
- 03__Playbooks/SNASHGPT_PRE_ROLLOUT_CHECKLIST.md
- 03__Playbooks/SNASH_PHASE_0_TO_3_VISUAL_MENTAL_MODEL.md
- root-level rollout / source-of-truth / discussion files pending reconciliation

### G — Draft / future / excluded
- PHASE6__OVERVIEW.md
- root-level phase 0–2 contract/addendum docs until reconciled

### G1 — Governing support docs (not direct runtime executors)
- 01__Engines/PHASE_5__CLOSING_HANDOVER/PHASE5_0__OVERVIEW.md
- 01__Engines/PHASE_5__CLOSING_HANDOVER/PHASE5_1__CLOSING_STATE_MACHINE.md
- 01__Engines/PHASE_5__CLOSING_HANDOVER/PHASE5_2__HANDOVER_WORKFLOW.md
- 01__Engines/PHASE_5__CLOSING_HANDOVER/PHASE5_3__END_ESCALATE_RULES.md
- 01__Engines/PHASE_5__CLOSING_HANDOVER/PHASE5_4__YES_LATER_SILENCE_PLAYBOOK.md
- 01__Engines/PHASE_5__CLOSING_HANDOVER/PHASE5_5__WHATSAPP_NEXT_STEP_TEMPLATES__EN_AR.md
- 01__Engines/PHASE_5__CLOSING_HANDOVER/PHASE5_LOCK.md

Rule:
- These files are governing authority/support documents for `CLOSING_HANDOVER_ENGINE.md`.
- They are not to be treated as direct runtime executors in Phase 0–4 UAT unless explicitly enabled by manifest/runtime scope.

### H — Ignore
- .DS_Store
- image files
- .pages files
