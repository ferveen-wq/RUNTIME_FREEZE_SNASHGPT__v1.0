# PHASE ARCHITECTURE
Status: DRAFT
Source Policy: Active runtime files win over legacy, tests, drafts, and archive notes.
Scope: Phase ordering, phase gates, phase inputs/outputs, and phase transition conditions only. No customer-facing phrase invention. No pricing invention beyond referenced runtime authority.

## 0. Purpose

This document records how the runtime phases are structured, what each phase is allowed to do, what each phase must not do, and what conditions move a conversation from one phase to the next.

Primary authority sources:
- `RUNTIME_LOAD_MANIFEST.md`
- `RUNTIME_EXECUTION_FLOW.md`
- `QUALIFICATION_ENGINE.md`
- `PHASE3A_QUALIFICATION_DECISION_MATRIX.md`
- `NEGOTIATION_LOGIC_MODULE.md`
- `PRICE_LADDER_ENGINE.md`
- `OBJECTION_RESOLUTION_ENGINE.md`
- `SILENCE_HANDLING_ENGINE.md`
- `CLOSING_HANDOVER_ENGINE.md`

---

## 1. Canonical Runtime Phase Order

[FROM: RUNTIME_LOAD_MANIFEST.md]

Runtime phase order:
- Phase 0 — Intake & Control
- Phase 0B — Runtime Guardrails Authority
- Phase 1–2 — Qualification Not-Ready / Intake Qualification
- Phase 3A — Qualifier-First Gate
- Phase 3B — Price Exposure
- Phase 4 — Confidence / Objection / Price Pressure

Rule:
- no phase may execute out of order

---

## 2. Phase 0 — Intake & Control

[FROM: RUNTIME_LOAD_MANIFEST.md]
[FROM: CUSTOMER_CHAT_INTAKE_RULES.md]
[FROM: KNOWLEDGE__RUNTIME_CORE_BUNDLE.md]

Purpose:
- govern runtime boot order and Phase 0 intake control
- enforce identity integrity
- enforce context continuity
- enforce cross-platform searchability
- define valid customer input handling
- classify unsafe or contradictory conditions before engines run

Inputs:
- plain text chat
- screenshot of chat
- pasted chat history
- short messages
- emojis combined with text

Outputs:
- structured extracted inputs
- input normalization
- objection intake tags
- price/comparison detection cues
- roof-black routing cues
- phase-0 guardrail outcome

Allowed:
- detect primary language
- convert screenshot/pasted chat into usable text intent
- extract customer intent, car details, service requested, questions asked, emotional tone
- halt or gate execution on unsafe or contradictory conditions

Must not:
- decide pricing
- decide final answers
- format customer reply
- override qualification or runtime sequencing

Transition onward:
- proceeds only after Phase 0 prerequisites are satisfied
- intake passes normalized inputs into qualification
- intake stops where qualification begins
- downstream phases may not run early

---

## 3. Phase 0B — Runtime Guardrails Authority

[FROM: KNOWLEDGE__RUNTIME_CORE_BUNDLE.md]

Purpose:
- apply non-negotiable runtime guardrails before execution engines run

Inputs:
- runtime context
- contract signals
- safety and contradiction conditions

Outputs:
- halt / gate / delay authority
- signal coverage enforcement
- output hygiene dominance
- pricing guardrails before execution

Allowed:
- halt execution
- gate execution
- delay execution
- suppress unsupported routed signals in test mode

Must not:
- execute qualification logic
- perform pricing calculations
- recover silence
- negotiate objections
- mutate behavior automatically

Transition onward:
- no downstream engine may override Phase 0 decisions

---

## 4. Phase 1–2 — Qualification Not-Ready / Intake Qualification

[FROM: QUALIFICATION_ENGINE.md]
[FROM: RUNTIME_EXECUTION_FLOW.md]

Purpose:
- evaluate incoming context and signals
- determine readiness, constraints, and routing requirements before response, tone, or service framing is applied

Inputs:
- structured and unstructured context from upstream layers
- user messages
- session metadata
- language detection output
- routing pre-signals

Outputs:
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

Allowed:
- readiness assessment
- missing-context detection
- coarse request classification for routing safety
- service-context continuity handling
- qualifier sequencing preparation

Locked early-phase behavior:
- one question max
- minimum vehicle context first when `missing_fields` is non-empty
- L1 clarification dominance when vehicle context is incomplete
- no pricing, ladders, discounts, persuasion, or Phase 3/4 leakage
- preserve already-known fields through carry-forward

Must not:
- generate customer-facing text
- recommend services in customer-facing form
- influence tone
- interact with pricing, discounts, offers, or promotional logic
- perform silence handling

Transition onward:
- do not call Negotiation unless `QUALIFICATION_STATUS = READY_FOR_NEGOTIATION`
- if missing / incomplete / not-ready:
  - route to clarification or graceful exit
  - no forward progression

---

## 5. Phase 3A — Qualifier-First Gate

[FROM: RUNTIME_EXECUTION_FLOW.md]
[FROM: PHASE3A_QUALIFICATION_DECISION_MATRIX.md]
[FROM: QUALIFICATION_ENGINE.md]
[FROM: PHASE4_8_MESSAGE_ASSEMBLY_MAP.md]

Purpose:
- collect just enough additional service-specific inputs to make Phase 3B pricing logical
- enforce one-question qualifier sequencing before pricing

Entry conditions:
- Phase 0–2 complete
- `service_intent` known
- `QUALIFICATION_STATUS == READY_FOR_NEGOTIATION` is the primary runtime progression gate
- `PRICE_LADDER_ENGINE.md` currently tolerates `READY` as well, but this remains a tracked reconciliation item and must not be treated as the main orchestration rule
- `vehicle_model` known
- `vehicle_year` known

Outputs:
- `phase3a_required`
- `phase3a_complete`
- `phase3a_qualifier_id`
- qualifier answer normalization into service-specific parameters

Allowed:
- ask one qualifier per assistant turn
- nudge once if qualifier is ignored
- repeat same qualifier once
- set UNKNOWN or UNSURE and proceed safely when allowed by matrix
- capture qualifier answers from the previous assistant-turn qualifier prompt
- apply same-message fallback detection where explicitly allowed by engine logic

Locked behavior:
- runtime phase label remains `PHASE_3`
- Phase 3A vs Phase 3B is represented by:
  - `phase3a_required`
  - `phase3a_complete`
  - `phase3a_qualifier_id`
  - `price_ladder_state`
- `QUALIFICATION_ENGINE.md` is the effective final writer for:
  - `phase3a_required`
  - `phase3a_complete`
  - `phase3a_qualifier_id`
- `PHASE4_8_MESSAGE_ASSEMBLY_MAP.md` maps `phase3a_qualifier_id` to one verbatim phrase block only
- roof-black PPF override may complete Phase 3A without running the normal PPF qualifier chain

Must not:
- output pricing
- ask multiple questions
- skip qualifier order
- emit separate runtime phase labels `PHASE_3A` or `PHASE_3B`

Transition onward:
- if `phase3a_required == true`:
  - assembly outputs exactly one Phase 3A qualifier question and stops
- if `phase3a_complete == true`:
  - proceed to Phase 3B pricing/SKU selection

---

## 6. Phase 3B — Price Exposure

[FROM: RUNTIME_LOAD_MANIFEST.md]
[FROM: RUNTIME_EXECUTION_FLOW.md]
[FROM: PRICE_LADDER_ENGINE.md]
[FROM: SKU_SELECTION_MATRIX.md]
[FROM: PRICE_TABLE_VAT_INCL.md]
[FROM: PHASE4_8_MESSAGE_ASSEMBLY_MAP.md]

Purpose:
- control how pricing is expressed and escalated once pricing discussion is allowed

Entry conditions:
- `QUALIFICATION_STATUS == READY_FOR_NEGOTIATION` or `QUALIFICATION_STATUS == READY`
- Phase 3A complete when required

Hard gate before pricing:
- car model
- model year
- service category

Soft gate:
- usage context only when materially relevant to pricing posture

Outputs:
- `price_ladder_state`

Allowed:
- control price anchors and ranges
- manage escalation boundaries
- render approved price outputs from locked pricing authority
- read SKU ordering from `SKU_SELECTION_MATRIX.md`
- read numeric prices from `PRICE_TABLE_VAT_INCL.md`

Must not:
- decide service fit
- educate or re-steer service choices
- invent prices
- invent coverage variants
- redefine SKU defaults inside pricing engine
- substitute services automatically
- expose raw SKU IDs in customer-facing text
- must not treat roof-black styling as wrap pricing path

Locked behavior:
- `PRICE_LADDER_ENGINE.md` is the only writer of `price_ladder_state`
- `SKU_SELECTION_MATRIX.md` is the SKU-order authority
- `PRICE_TABLE_VAT_INCL.md` is the numeric pricing authority
- wrap automation pricing is full-vehicle only
- roof-black styling belongs to the PPF path, not the wrap path

Transition onward:
- if price has been exposed, objection resolution may run
- if exact pricing cannot safely proceed, escalate or terminate pricing path per ladder rules

---

## 7. Phase 4 — Confidence / Objection / Price Pressure

[FROM: RUNTIME_LOAD_MANIFEST.md]
[FROM: OBJECTION_RESOLUTION_ENGINE.md]
[FROM: CLOSING_HANDOVER_ENGINE.md]
[FROM: PHASE4_8_MESSAGE_ASSEMBLY_MAP.md]

Purpose:
- handle post-price objection decisioning
- resolve final control outcomes
- stop automation or hand over to human when required

Phase 4 includes:
- objection resolution after pricing exposure
- closing / terminal governance
- handover control

Clarification:
- Runtime control Phase 4 includes objection decisioning plus terminal closing/handover control.
- Separately, `PHASE4_8_MESSAGE_ASSEMBLY_MAP.md` uses the label “Phase 5” for the post-price objection-deepening phrase layer.
- That assembly-map “Phase 5” is a routing/render layer for controlled clarification after price.
- It is NOT the same thing as the `PHASE_5__CLOSING_HANDOVER` document pack, which governs closing/handover behavior for `CLOSING_HANDOVER_ENGINE.md`.

### 7.1 Objection Resolution

Purpose:
- deterministically handle objections after pricing has been exposed

Inputs:
- `QUALIFICATION_STATUS`
- `negotiation_state`
- `price_ladder_state`
- `objection_signal`
- `objection_repeat_count`
- `customer_response_latency`

Outputs:
- decision object
- `quote_required`
- `automation_allowed`

Allowed:
- decide continue / pause / escalate / exit

Must not:
- generate customer-facing language
- modify price ladder outputs
- create prices, discounts, bundles, or offers
- introduce service steering

### 7.2 Closing & Handover

Purpose:
- define final conversation states and system behavior after pricing, objection handling, silence handling, and PIM have completed

Inputs:
- `QUALIFICATION_STATUS`
- `NEGOTIATION_STATE`
- `PRICE_LADDER_STATE`
- `OBJECTION_SIGNAL`
- `QUOTE_REQUIRED_FLAG`
- `AUTOMATION_ALLOWED_FLAG`
- `OBJECTION_REPEAT_COUNT`
- `CUSTOMER_RESPONSE_LATENCY`
- `COMMITMENT_ARTIFACT_STATUS`

Outputs:
- `FINAL_CONVERSATION_STATE`
- `HANDOVER_REQUIRED_FLAG`
- `HANDOVER_REASON`
- `AUTOMATION_TERMINATED_FLAG`
- `SESSION_CLOSE_REASON`

Allowed:
- declare terminal conversation states
- govern when automation must stop
- govern when human handover occurs

Must not:
- generate customer-facing text
- decide tone or persuasion
- reopen objections or silence recovery
- modify Phase 3 engine behavior

Transition onward:
- if `AUTOMATION_TERMINATED_FLAG == TRUE`:
  - stop all automation immediately

---

## 8. Global Silence Gate (Phase-Agnostic)

[FROM: RUNTIME_EXECUTION_FLOW.md]
[FROM: SILENCE_HANDLING_ENGINE.md]

Purpose:
- apply silence handling across Qualification, Negotiation, Pricing, and Objection phases
- keep silence time-based only

Inputs:
- `LAST_COUNTED_OUTBOUND_TIMESTAMP`
- `LAST_CUSTOMER_SIGNAL_TIMESTAMP`
- `FOLLOW_UP_COUNT`
- `SILENCE_SUPPRESSED`
- `INPUT_MODE`
- `CONVERSATION_STATUS`
- `AGENT_TAKEOVER_FLAG`

Outputs:
- `SILENCE_STAGE`
- `SILENCE_ACTIVE`
- `ALLOW_ACTION`
- `EXIT_FLAG`

Allowed:
- compute silence stage
- allow one follow-up action when permitted
- terminate silence path when required

Must not:
- generate customer-facing language
- decide tone
- reopen Price Ladder
- resolve objections
- change services or scope

Transition onward:
- if `EXIT_FLAG == TRUE`:
  - stop outbound actions and exit
- if `ALLOW_ACTION == TRUE`:
  - allow one follow-up action
- if `SILENCE_STAGE == NONE`:
  - proceed with normal phase engine selection

---

## 9. Phase Boundary Rules

[FROM: RUNTIME_EXECUTION_FLOW.md]
[FROM: RUNTIME_LOAD_MANIFEST.md]

Rules:
- no phase may execute out of order
- Phase 0 must hand off to qualification without taking routing ownership
- Phase 0B guardrails may halt, gate, or delay any downstream progression
- Phase 1–2 must remain qualification-first and one-question-safe
- Phase 3A must run before Phase 3B when required
- pricing must not run before `QUALIFICATION_STATUS = READY_FOR_NEGOTIATION`
- objection resolution must not run before price exposure
- closing/handover must consume canonical outputs only
- Phase 5 files must not be loaded during Phase 0–4 UAT unless explicitly enabled

---

## 10. Phase 7 Historical Runtime Label / Support Route

[FROM: PHASE4_8_MESSAGE_ASSEMBLY_MAP.md]

Purpose:
- document the historical assembly-map Phase 7 label that existed before authority reconciliation
- do not treat Phase 7 as the owner of late-stage follow-up, silence, deferred, or closing behavior

Inputs:
- `READY_TO_PROCEED`
- `THINKING`
- `SILENT`
- `DEFERRED`
- `REENTERED`
- `active_service_context`

Outputs:
- constrained support phrasing only when separately allowed by higher runtime ownership

Allowed:
- continue context safely
- preserve service continuity
- suppress hooks, pricing, and Phase 6 explanation during this support route

Must not:
- act as a late-stage behavioral owner
- introduce pricing
- introduce service education by default
- replace Phase 5 objection / silence / deferred / handover ownership

---

## 11. Phase 7 Education Support Layer

[FROM: PHASE7_EDUCATION_SNIPPETS.md]
[FROM: PHRASE_GOVERNANCE_STANDARD.md]
[FROM: PHASE_4_7_HOOK_QUESTION_ENGINE.md]

Purpose:
- provide reusable explanation snippets when explanation is allowed by routing/governance

Status:
- support layer referenced by runtime-governed explanation architecture
- not a standalone late-stage control owner
- `REENTERED_CONTINUE` remains the only runner-proven Phase 7 support lane; broader THINKING / SILENT / DEFERRED / READY_TO_PROCEED must not be treated as Phase 7-owned behavior

---

## 12. Phase 8 Visual Attachment Layer

[FROM: PHASE4_8_MESSAGE_ASSEMBLY_MAP.md]
[FROM: PHASE8_VISUAL_INTELLIGENCE_MAP.md]
[FROM: PHASE8_VIDEO_LIBRARY.md]

Purpose:
- attach optional visual proof/support after an allowed explanation context

Status:
- promoted in runtime notes and routed in assembly-map logic
- still needs separate execution-path trust classification distinct from phrase routing

---

## 13. Phase 9 Trust / Persuasion Reference Layer

Purpose:
- hold future trust/persuasion reference architecture only

Status:
- not yet trusted as runtime-active execution ownership
- remain deferred until manifest + execution-path evidence is explicit

