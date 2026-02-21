# GLOBAL_RUNTIME_FLOW_MAP.md
Status: GOVERNANCE (non-runtime)
Purpose: Human-readable map of runtime execution + authority boundaries.
Scope: Documentation + enforcement reference only. Not executed at runtime.

--------------------------------------------------------------------------
1) Runtime Pipeline (Single Turn)
--------------------------------------------------------------------------
Source of sequencing truth:
- RUNTIME_LOAD_MANIFEST.md (file inventory + ordering)
- RUNTIME_EXECUTION_FLOW.md (execution order)
- RUNTIME_STATE_MACHINE.md (state transitions + hard stops)

Turn execution (high-level):
S4 ACTIVE →
  1) CUSTOMER_CHAT_INTAKE_RULES.md
     - Extract signals (objection_signal, objection_repeat_count, etc.)
     - MUST NOT finalize request_type if Qualification owns it (see AUTHORITY_INDEX).

  2) QUALIFICATION_ENGINE.md
     - Classifies request_type
     - Emits QUALIFICATION_STATUS + missing_fields
     - Emits service_intent + active_service_context + detected_service_intent_in_message

  3) NEGOTIATION_LOGIC_MODULE.md
     - Logic only; no customer text

  4) PRICE_LADDER_ENGINE.md (only when requested by negotiation routing)
     - price_ladder_state + pricing range selection
     - MUST NOT write request_type

  5) OBJECTION_RESOLUTION_ENGINE.md
     - Logic only; no customer text

  6) PHASE4_8_MESSAGE_ASSEMBLY_MAP.md
     - Selects selected_phrase_id (and only selects)
     - Must NOT invent text; must only pick blocks from PHASE4_6
     - Must NOT write request_type (see AUTHORITY_INDEX)

  7) OUTPUT_RESPONSE_TEMPLATE.md
     - Final formatting only (language order, timestamp, hygiene)
     - Must NOT change routing decisions or signals

--------------------------------------------------------------------------
2) Canonical “Writers” vs “Readers”
--------------------------------------------------------------------------
Definitions:
- WRITER: the only place allowed to assign/overwrite a signal.
- READER: may consume a signal to choose behavior, but cannot overwrite.

The exact list is in AUTHORITY_INDEX.md.

--------------------------------------------------------------------------
3) Hard Rules (Operational)
--------------------------------------------------------------------------
Rule A: One signal → one writer.
Rule B: Assembly selects phrasing; it does not change classification.
Rule C: Phrase Library contains text only; it does not encode routing logic.
Rule D: Output Template formats only; it does not decide.

--------------------------------------------------------------------------
4) Build Gate
--------------------------------------------------------------------------
Before any UAT run:
  python runner/lint_authority.py

If lint fails → STOP. Do not patch “elsewhere” to make tests green.
