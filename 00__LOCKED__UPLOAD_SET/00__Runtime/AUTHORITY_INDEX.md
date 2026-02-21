# AUTHORITY_INDEX.md
Status: GOVERNANCE (enforced by lint)
Purpose: Single-writer law for signals, blocks, and routing decisions.
Scope: Applies to Phase 0–4 runtime.

--------------------------------------------------------------------------
1) Routing / Classification Signals
--------------------------------------------------------------------------

Signal: request_type
  - WRITER: 01__Engines/QUALIFICATION_ENGINE.md
  - READERS:
      - 00__Runtime/PHASE4_8_MESSAGE_ASSEMBLY_MAP.md
      - 01__Engines/PRICE_LADDER_ENGINE.md
      - 00__Runtime/PHASE3A_QUALIFICATION_DECISION_MATRIX.md
  - FORBIDDEN WRITERS:
      - CUSTOMER_CHAT_INTAKE_RULES.md
      - PHASE4_8_MESSAGE_ASSEMBLY_MAP.md
      - OUTPUT_RESPONSE_TEMPLATE.md
      - PHASE4_6_HUMAN_PHRASE_LIBRARY.md

Signal: QUALIFICATION_STATUS
  - WRITER: 01__Engines/QUALIFICATION_ENGINE.md
  - READERS: RUNTIME_STATE_MACHINE.md, RUNTIME_EXECUTION_FLOW.md, PHASE4_8_MESSAGE_ASSEMBLY_MAP.md

Signal: missing_fields
  - WRITER: 01__Engines/QUALIFICATION_ENGINE.md
  - READERS: PHASE4_8_MESSAGE_ASSEMBLY_MAP.md, PHASE3A_QUALIFICATION_DECISION_MATRIX.md

Signal: service_intent
  - WRITER: 01__Engines/QUALIFICATION_ENGINE.md
  - READERS: PHASE4_8_MESSAGE_ASSEMBLY_MAP.md, PHASE3A_QUALIFICATION_DECISION_MATRIX.md

Signal: active_service_context
  - WRITER: 01__Engines/QUALIFICATION_ENGINE.md (non-overwrite rule)
  - READERS: PHASE4_8_MESSAGE_ASSEMBLY_MAP.md (continuity gate)

Signal: detected_service_intent_in_message
  - WRITER: 01__Engines/QUALIFICATION_ENGINE.md (current message only)
  - READERS: PHASE4_8_MESSAGE_ASSEMBLY_MAP.md

Signal: objection_signal, objection_repeat_count
  - WRITER: 00__Runtime/CUSTOMER_CHAT_INTAKE_RULES.md
  - READERS: NEGOTIATION_LOGIC_MODULE.md, OBJECTION_RESOLUTION_ENGINE.md, PHASE4_8_MESSAGE_ASSEMBLY_MAP.md

Signal: price_ladder_state
  - WRITER: 01__Engines/PRICE_LADDER_ENGINE.md
  - READERS: OBJECTION_RESOLUTION_ENGINE.md, PHASE4_8_MESSAGE_ASSEMBLY_MAP.md
  - FORBIDDEN WRITERS:
      - PHASE4_8_MESSAGE_ASSEMBLY_MAP.md
      - OUTPUT_RESPONSE_TEMPLATE.md

Signal: selected_phrase_id
  - WRITER: 00__Runtime/PHASE4_8_MESSAGE_ASSEMBLY_MAP.md
  - READERS: OUTPUT_RESPONSE_TEMPLATE.md (formatting only), debug renderer

--------------------------------------------------------------------------
2) Customer-Facing Text
--------------------------------------------------------------------------

Customer-facing message content (EN/AR lines)
  - WRITER: 00__Runtime/PHASE4_6_HUMAN_PHRASE_LIBRARY.md
  - SELECTOR: 00__Runtime/PHASE4_8_MESSAGE_ASSEMBLY_MAP.md (select only; no invention)
  - FORMATTER: 00__Runtime/OUTPUT_RESPONSE_TEMPLATE.md (layout only; no rewording)

--------------------------------------------------------------------------
3) Bilingual Integrity Rules (must pass lint)
--------------------------------------------------------------------------
- Every phrase block MUST include both:
    EN: ...
    AR: ...
- Placeholder/slot parity:
    The set of {placeholders} in EN must match AR within the same block.

--------------------------------------------------------------------------
4) Temporary Hotfix Policy
--------------------------------------------------------------------------
If a temporary hotfix is unavoidable:
- It MUST be tagged:
    TEMP_HOTFIX_EXPIRES_BY: YYYY-MM-DD
    TEMP_HOTFIX_TRACK_ID: <id>
- Lint will warn (or fail) when expired.
