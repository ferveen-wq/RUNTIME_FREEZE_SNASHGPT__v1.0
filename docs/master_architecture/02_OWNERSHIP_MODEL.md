# OWNERSHIP MODEL
Status: DRAFT
Source Policy: Active runtime files win over legacy, tests, drafts, and archive notes.
Scope: Runtime authority ownership only. No customer-facing phrase writing. No pricing invention. No phase prose beyond ownership boundaries.

## 0. Purpose

This document defines which runtime component owns each signal, decision, control action, and customer-facing construction step.

Primary authority sources:
- `AUTHORITY_INDEX.md`
- `RUNTIME_EXECUTION_FLOW.md`
- `RUNTIME_STATE_MACHINE.md`
- `RUNTIME_LOAD_MANIFEST.md`
- `KNOWLEDGE__RUNTIME_CORE_BUNDLE.md`

---

## 1. Ownership Law

[FROM: GLOBAL_RUNTIME_FLOW_MAP.md]

Rule A:
- one signal → one writer

Rule B:
- assembly selects phrasing
- it does not change classification

Rule C:
- phrase library contains text only
- it does not encode routing logic

Rule D:
- output template formats only
- it does not decide

[FROM: AUTHORITY_INDEX.md]

Definitions:
- WRITER = the only place allowed to assign/overwrite a signal
- READER = may consume a signal to choose behavior, but cannot overwrite

---

## 2. Runtime Component Ownership

## 2.1 Runtime Load Manifest

[FROM: RUNTIME_LOAD_MANIFEST.md]

Owns:
- runtime boot order
- Phase 0 intake control
- conflict-resolution priority
- identity integrity
- context continuity
- duplicate handling
- title discipline
- internal-only assistant flags
- UAT phase-loading boundaries

Must not contain:
- pricing scripts
- negotiation ladders
- objection playbooks
- silence recovery playbooks
- tone writing rules
- auto-learning / auto-patching behavior

---

## 2.2 Runtime Core Bundle

[FROM: KNOWLEDGE__RUNTIME_CORE_BUNDLE.md]

Owns:
- non-negotiable runtime guardrails
- Phase 0 halt / gate / delay authority
- safety dominance
- pricing guardrails before execution
- anti-repetition learning protection
- signal coverage governance
- output hygiene constraint

Does not:
- execute qualification logic
- perform pricing calculations
- apply discounts
- recover silence
- negotiate objections
- learn or mutate behavior automatically

---

## 2.3 Customer Chat Intake Rules

[FROM: CUSTOMER_CHAT_INTAKE_RULES.md]
[FROM: AUTHORITY_INDEX.md]

Owns:
- valid customer input handling
- Arabic / English / mixed handling
- screenshot and pasted chat handling
- emoji and short-message handling
- pre-qualification extraction

Writes:
- `objection_signal`
- `objection_repeat_count`
- `customer_response_latency`

Boundary note:
- Intake may extract hints, cues, and normalized handoff fields for downstream use.
- Intake must not assign or overwrite qualification-owned routing signals such as `request_type`, `service_intent`, `active_service_context`, or `detected_service_intent_in_message`.

Forbidden writers for:
- `request_type`
  - `CUSTOMER_CHAT_INTAKE_RULES.md`
  - `PHASE4_8_MESSAGE_ASSEMBLY_MAP.md`
  - `OUTPUT_RESPONSE_TEMPLATE.md`
  - `PHASE4_6_HUMAN_PHRASE_LIBRARY.md`

---

## 2.4 Qualification Engine

Authority file:
- `QUALIFICATION_ENGINE.md`

Dependency authority:
- `PHASE3A_QUALIFICATION_DECISION_MATRIX.md`
- `GLOBAL_PRODUCT_NAMING_REGISTRY_v1.0.md`
- `GLOBAL_CORE_CONTEXT_PARAMETERS.md`
- `CONVERSATION_DYNAMIC_PARAMETERS.md`

[FROM: QUALIFICATION_ENGINE.md]

Writes:
- `request_type`
- `QUALIFICATION_STATUS`
- `qualification_state`
- `context_completeness`
- `missing_fields`
- `missing_info_ask_count`
- `service_intent`
- `active_service_context`
- `detected_service_intent_in_message`
- `phase3a_required`
- `phase3a_complete`
- `phase3a_qualifier_id`

[FROM: QUALIFICATION_ENGINE.md]

Must NOT:
- generate customer-facing text
- recommend services in customer-facing form
- perform pricing calculations
- perform silence handling
- perform tone selection
- format output responses

[FROM: PHASE3A_QUALIFICATION_DECISION_MATRIX.md]
[FROM: QUALIFICATION_ENGINE.md]
[FROM: PHASE4_8_MESSAGE_ASSEMBLY_MAP.md]

Phase 3A rules:
- Phase 3A runs AFTER Phase 0–2 is complete
- requires `service_intent + vehicle_model + vehicle_year`
- one question per assistant turn
- no pricing in Phase 3A
- runtime phase label remains `PHASE_3`
- qualifier state is represented by:
  - `phase3a_required`
  - `phase3a_complete`
  - `phase3a_qualifier_id`
- qualifier answers may be normalized from the reply to the previous assistant qualifier turn
- if user ignores qualifier:
  - nudge once
  - repeat same qualifier
  - if still unanswered → set UNKNOWN or UNSURE and proceed safely
- `QUALIFICATION_ENGINE.md` is the effective final writer of:
  - `phase3a_required`
  - `phase3a_complete`
  - `phase3a_qualifier_id`

[FROM: GLOBAL_PRODUCT_NAMING_REGISTRY_v1.0.md]

Naming rules:
- use only canonical product/service names
- no aliases in output
- aliases allowed only for input detection

---

## 2.4A Global Product Naming Registry

[FROM: GLOBAL_PRODUCT_NAMING_REGISTRY_v1.0.md]

Status note:
- currently marked DRAFT
- treat as critical naming dependency unless replaced by a locked successor

Owns:
- valid internal product and SKU names
- alias handling for detection only
- rejection of invented or modified names

Must not override:
- locked runtime sequencing
- locked state ownership
- locked pricing tables
- locked service canon

---

## 2.5 Negotiation Logic Module

[FROM: NEGOTIATION_LOGIC_MODULE.md]

Writes:
- `negotiation_state`
- `NEGOTIATION_STATE`

Phase role:
- solution framing and negotiation before pricing

Not allowed to:
- provide exact prices
- negotiate numbers or discounts
- execute pricing logic
- re-run or reset qualification
- defend pricing or attack competitors

---

## 2.6 Price Ladder Engine

[FROM: PRICE_LADDER_ENGINE.md]
[FROM: AUTHORITY_INDEX.md]
[FROM: PRICE_TABLE_VAT_INCL.md]
[FROM: SKU_SELECTION_MATRIX.md]
[FROM: PRODUCT_SERVICE_CANON.md]

Writes:
- `price_ladder_state`

Forbidden writers for:
- `price_ladder_state`
  - `PHASE4_8_MESSAGE_ASSEMBLY_MAP.md`
  - `OUTPUT_RESPONSE_TEMPLATE.md`

Rules:
- uses locked pricing authority
- uses locked SKU selection dependency
- must not invent prices
- must not fabricate synthetic ranges
- must not decide service fit
- must not introduce new service steering logic
- must not redefine SKU defaults inside the pricing engine
- must not expose raw SKU IDs in customer-facing output
- wrap automation pricing is full-vehicle only
- roof-black styling belongs to PPF-path handling, not wrap pricing

---

## 2.7 Objection Resolution Engine

[FROM: OBJECTION_RESOLUTION_ENGINE.md]

Owns:
- objections that occur after pricing has been exposed

Outputs:
- decision object
- `quote_required`
- `automation_allowed`

Must not:
- generate customer-facing language
- negotiate, persuade, pressure, or emotionally frame
- modify, override, or reinterpret Price Ladder outputs
- create new prices, discounts, bundles, or offers
- introduce service steering
- parse raw customer messages

---

## 2.8 Silence Handling Engine

[FROM: SILENCE_HANDLING_ENGINE.md]

Writes:
- `SILENCE_STAGE`
- `SILENCE_ACTIVE`
- `ALLOW_ACTION`
- `EXIT_FLAG`

Must not:
- generate customer-facing language
- decide tone, persuasion, visuals, hooks, or negotiation actions
- interpret customer intent
- modify pricing, services, or scope
- reopen Price Ladder
- resolve objections

---

## 2.9 Closing & Handover Engine

[FROM: CLOSING_HANDOVER_ENGINE.md]

Writes:
- `FINAL_CONVERSATION_STATE`
- `HANDOVER_REQUIRED_FLAG`
- `HANDOVER_REASON`
- `AUTOMATION_TERMINATED_FLAG`
- `SESSION_CLOSE_REASON`

Must not:
- inspect raw customer messages
- generate phrases or tone
- restart pricing, objections, silence, or PIM

---

## 2.10 Message Assembly

[FROM: PHASE4_8_MESSAGE_ASSEMBLY_MAP.md]
[FROM: AUTHORITY_INDEX.md]

Writes:
- `selected_phrase_id`

Owns:
- block selection
- ordering
- caps
- hook slot wiring
- suppression precedence

Must not:
- invent customer-facing phrases
- write `request_type`
- write `price_ladder_state`

Assembly output contract:
- customer sees one coherent message only

---

## 2.11 Human Phrase Library

[FROM: AUTHORITY_INDEX.md]
[FROM: PHASE4_6_HUMAN_PHRASE_LIBRARY.md]

Customer-facing message content:
- WRITER = `PHASE4_6_HUMAN_PHRASE_LIBRARY.md`

Rules:
- phrase library writes text only
- every phrase block must include EN and AR
- placeholder parity must match
- phrase library must not encode routing logic

---

## 2.12 Tone Engine

[FROM: phase_4_5_tone_engine.md]

Owns:
- how messages should feel
- tone selection
- emotional and behavioral boundaries
- hook permission constraints

Does NOT:
- generate phrases or sentences
- change phrase wording
- reorder message structure
- override safety rules

---

## 2.13 Hook Question Engine

[FROM: PHASE_4_7_HOOK_QUESTION_ENGINE.md]

Owns:
- whether optional engagement question may appear

Does NOT:
- create new phrases
- introduce new tones
- alter message order
- force engagement
- escalate conversation

Rules:
- hooks are optional
- hooks are fully suppressible
- hooks must respect tone permissions
- hooks must respect assembly limits

---

## 2.14 Output Response Template

[FROM: OUTPUT_RESPONSE_TEMPLATE.md]
[FROM: AUTHORITY_INDEX.md]

FORMATTER:
- `OUTPUT_RESPONSE_TEMPLATE.md`

Owns:
- only allowed customer-facing response structure
- formatting
- language order
- timestamp and hygiene rules

Must NEVER:
- make decisions
- reopen qualification logic
- introduce pricing logic
- override execution flow

---

## 2.15 Runtime State Machine

[FROM: RUNTIME_STATE_MACHINE.md]

Owns:
- runtime states
- allowed transitions
- failure handling
- recovery rules
- session rule after terminal state

Does not:
- define file inventory
- define response formatting
- implement engine logic

---

## 2.16 Runtime Execution Flow

[FROM: RUNTIME_EXECUTION_FLOW.md]

Owns:
- the only allowed runtime load + execution order

Must NEVER:
- implement business logic
- implement pricing logic
- implement qualification criteria
- add customer-facing wording

---

## 2.17 Orchestrator

[FROM: RUNTIME_STATE_MACHINE.md]
[FROM: RUNTIME_EXECUTION_FLOW.md]
[FROM: PHASE3_ORCHESTRATION_WIRING_ADDENDUM.md]

Owns / writes where runtime explicitly assigns:
- `LAST_COUNTED_OUTBOUND_TIMESTAMP`
- `LAST_CUSTOMER_SIGNAL_TIMESTAMP` (with Intake)
- `FOLLOW_UP_COUNT`
- `INPUT_MODE`
- `SILENCE_SUPPRESSED`
- `SILENCE_SUPPRESSION_REASON`
- `SILENCE_TERMINATED`
- `AGENT_TAKEOVER_FLAG`
- `CONVERSATION_STATUS`

Also owns:
- canonical normalization of cross-engine Phase 3 keys
- enforcement of sequence and terminal-state blocking

---

## 3. Canonical Signal Ownership

[FROM: AUTHORITY_INDEX.md]
[FROM: PHASE3_ORCHESTRATION_WIRING_ADDENDUM.md]

Classification / routing:
- `request_type` → Qualification only
- `QUALIFICATION_STATUS` → Qualification only
- `missing_fields` → Qualification only
- `service_intent` → Qualification only
- `active_service_context` → Qualification only
- `detected_service_intent_in_message` → Qualification only

Objection / timing:
- `objection_signal` → Intake only
- `objection_repeat_count` → Intake only
- `customer_response_latency` → Intake only

Pricing / objection control:
- `negotiation_state` / `NEGOTIATION_STATE` → Negotiation Logic only
- `price_ladder_state` → Price Ladder only
- decision object / `quote_required` / `automation_allowed` → Objection Resolution only

Silence:
- `SILENCE_STAGE` / `SILENCE_ACTIVE` / `ALLOW_ACTION` / `EXIT_FLAG` → Silence Handling only
- `SILENCE_SUPPRESSION_REASON` → Orchestrator only

Closing:
- `FINAL_CONVERSATION_STATE` → Closing & Handover only
- `HANDOVER_REQUIRED_FLAG` → Closing & Handover only
- `HANDOVER_REASON` → Closing & Handover only
- `AUTOMATION_TERMINATED_FLAG` → Closing & Handover only
- `SESSION_CLOSE_REASON` → Closing & Handover only

Customer-facing construction:
- `selected_phrase_id` → Assembly only
- customer-facing phrase text → Human Phrase Library only
- final formatted layout → Output Template only

---

## 4. UAT / Loading Boundary

[FROM: RUNTIME_LOAD_MANIFEST.md]

For Phase 0–4 UAT:
- Phase 5 closing/handover files must not be loaded unless Phase 5 UAT is explicitly enabled

Ownership clarification:
- UAT and harness layers may validate, constrain, or expose runtime behavior, but they do not become ownership authorities for runtime signals or routing decisions.
- If a UAT or harness result conflicts with active runtime files, ownership remains with the runtime authority file until reconciliation is completed.

Rule:
- Test scaffolding may check behavior.
- It must not silently redefine writers, readers, selectors, or formatters.

Implication:
- Green UAT status does not transfer ownership.
- Harness-side enforcement must not be documented as runtime ownership unless confirmed by runtime authority files.

