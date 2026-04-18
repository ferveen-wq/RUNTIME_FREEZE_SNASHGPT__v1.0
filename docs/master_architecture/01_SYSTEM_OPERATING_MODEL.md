# SYSTEM OPERATING MODEL
Status: DRAFT
Source Policy: Active runtime files win over legacy, tests, drafts, and archive notes.
Scope: Runtime operating flow only. No customer-facing phrase invention. No pricing invention. No phase persuasion logic.

## 0. Purpose

This document records how the runtime is structured to load, validate, process an inbound customer message, and produce a final output.

Primary authority sources:
- `RUNTIME_LOAD_MANIFEST.md`
- `GLOBAL_RUNTIME_FLOW_MAP.md`
- `RUNTIME_EXECUTION_FLOW.md`
- `RUNTIME_STATE_MACHINE.md`
- `KNOWLEDGE__RUNTIME_CORE_BUNDLE.md`
- `CUSTOMER_CHAT_INTAKE_RULES.md`
- `QUALIFICATION_ENGINE.md`

---

## 1. Runtime Operating Position

[FROM: GLOBAL_RUNTIME_FLOW_MAP.md]

Status:
- governance
- human-readable map of runtime execution + authority boundaries
- not executed at runtime

[FROM: RUNTIME_EXECUTION_FLOW.md]

Role:
- defines the only allowed runtime load + execution order

[FROM: RUNTIME_STATE_MACHINE.md]

Role:
- defines runtime states, transitions, and failure handling

[FROM: KNOWLEDGE__RUNTIME_CORE_BUNDLE.md]

Role:
- runtime guardrails before execution engines are allowed to run

### Runtime Truth vs Memory / Test Context

Rule:
- Active runtime files are the only source of truth for system behavior.
- Chat discussions, temporary notes, and reconstruction summaries must not be treated as authoritative behavior definitions.

Implications:
- Historical chat-page reconstruction may recover context, but it must not override runtime files.
- If chat-derived understanding conflicts with runtime files, runtime files win.

### Runtime vs Test / Harness Distinction

### Validation Boundary Rule (LOCKED)

Definition:
- “Validated” means:
  - validated against manifest-active runtime path only

- “Not automatically validated” includes:
  - support-authority dependencies (registry, SKU, pricing, canon)
  - repository completeness
  - metadata completeness

Rules:
- UAT or testing success confirms:
  - runtime execution path correctness
  - phase sequencing correctness
  - engine interaction correctness

- UAT or testing success does NOT confirm:
  - registry completeness
  - product metadata completeness
  - SKU surface completeness
  - price table semantic correctness beyond numeric mapping

Implication:
- Phase 0–6 may be marked “validated” for runtime behavior
- while support-authority layer remains incomplete or deferred

Control:
- All dependency gaps must be tracked via ARCHITECTURE_GAP_REGISTER.md
- No assumption of full-system correctness without dependency-layer validation

Rule:
- Runtime behavior must always be distinguished from test or harness behavior.

Definitions:
- Runtime = production behavior defined by active runtime files and execution flow
- Harness / UAT = validation layer used to test or simulate behavior

Constraints:
- Green UAT results do not by themselves prove runtime truth.
- Test or harness behavior must not be promoted into runtime doctrine unless it is confirmed against runtime authority files.
- If runtime and harness interpretations differ, architecture must treat runtime files as authoritative until reconciliation is complete.

### Phase Structure (Execution Reality)

The runtime operates in the following enforced order:

- Phase 0 — Intake & Control
  - handles raw customer input ingestion
  - applies `CUSTOMER_CHAT_INTAKE_RULES.md`
  - extracts structured signals only
  - does not decide final answers

- Phase 0B — Runtime Guardrails Authority
  - applies `KNOWLEDGE__RUNTIME_CORE_BUNDLE.md`
  - has absolute authority to halt, gate, or delay execution
  - no downstream engine may override this layer

- Phase 1–2 — Qualification Not-Ready / Intake Qualification
  - applies `QUALIFICATION_ENGINE.md`
  - resolves missing fields, readiness, and routing safety
  - enforces qualification-before-negotiation progression

Rule:
- Phase 0 → Phase 0B → Phase 1–2 must always execute in this order
- no phase skipping is allowed

---

## 2. Runtime Load / Boot Sequence

[FROM: RUNTIME_EXECUTION_FLOW.md]

Step 1:
- Load `RUNTIME_VERSION_CONTRACT.md`
- Validate required runtime files exist
- Validate required versions match exactly
- If validation fails:
  - stop execution
  - return version mismatch report
- No fallback
- No partial execution

Step 2:
- Load `RUNTIME_LOAD_MANIFEST.md`
- Confirm runtime load order
- Confirm runtime file count and categories
- If mismatch with Version Contract:
  - stop execution

Step 3:
- Load `RUNTIME_STATE_MACHINE.md`
- Set initial runtime state
- Prepare allowed state transitions

Step 4:
- Load `KNOWLEDGE__RUNTIME_CORE_BUNDLE.md`
- Lock runtime knowledge snapshot for this execution

Step 4.5:
- Load `bundles/customer_knowledge/KNOWLEDGE__CUSTOMER_KNOWLEDGE_BUNDLE.md`
- Merge into active runtime knowledge snapshot (read-only)

---

## 3. Runtime Manifest Operating Role

---

## 3A. Runtime Wiring and Dependency Model (LOCKED)

Purpose:
Define how runtime execution interacts with dependency layers without creating hidden or duplicate authority.

### 1. Manifest-Active Runtime Path

Definition:
- Only files loaded via `RUNTIME_LOAD_MANIFEST.md` are considered runtime-active.
- Only runtime-active files can:
  - control flow
  - influence decisions
  - produce outputs

Rule:
- If a file is not part of manifest load → it is NOT runtime-active.

---

### 2. Support-Authority Dependency Layer

Includes:
- Product Naming Registry
- SKU Selection Matrix
- Price Table
- Service Canon
- Parameter files

Role:
- Provide data only
- Must NOT:
  - control flow
  - introduce logic
  - override runtime decisions

---

### 3. Manifest vs Dependency Rule

- Runtime files = behavior authority
- Dependency files = data authority

Conflict rule:
- Runtime logic ALWAYS wins over dependency interpretation
- Dependencies must align to runtime, not vice versa

---

### 4. Deferred Support-Authority Cleanup Rule

Observation:
- Some dependency entries may be:
  - partially defined
  - missing metadata
  - structurally inconsistent

Rule:
- These MUST NOT be patched during runtime stabilization
- They MUST be:
  - logged in ARCHITECTURE_GAP_REGISTER
  - resolved in a dedicated cleanup phase

Reason:
- Prevents:
  - fragmented fixes
  - duplicate authority
  - regression risk

---

### 5. Phase 0–6 Completion Priority Rule

Rule:
- Full system stability MUST be achieved for:
  - Phase 0 → Phase 6

Before:
- Any Phase 7–9 expansion
- Any non-critical support-authority cleanup

Implication:
- Missing metadata (non-breaking) does NOT block Phase 0–6 completion
- Runtime correctness is prioritized over data completeness

---



[FROM: RUNTIME_LOAD_MANIFEST.md]

Purpose:
- governs runtime boot order and Phase 0 intake control
- enforces identity integrity
- enforces context continuity
- enforces cross-platform searchability
- applies before qualification, pricing, or negotiation logic may execute

Allowed to do:
- define runtime phases
- define file load order
- define conflict-resolution priority
- define Phase 0 intake constraints
- allow internal-only flags for assistants

Must not contain:
- pricing scripts
- negotiation ladders
- objection playbooks
- silence recovery playbooks
- tone writing rules
- visual playbook rules
- auto-learning or auto-patching behavior

---

## 4. Runtime Phase Order

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

## 5. Single-Turn Runtime Pipeline

[FROM: GLOBAL_RUNTIME_FLOW_MAP.md]

Turn execution (high level):
1. `CUSTOMER_CHAT_INTAKE_RULES.md`
2. `QUALIFICATION_ENGINE.md`
3. `NEGOTIATION_LOGIC_MODULE.md`
4. `PRICE_LADDER_ENGINE.md` (only when requested by negotiation routing)
5. `OBJECTION_RESOLUTION_ENGINE.md`
6. `PHASE4_8_MESSAGE_ASSEMBLY_MAP.md`
7. `OUTPUT_RESPONSE_TEMPLATE.md`

Pipeline law:
- Intake extracts
- Qualification classifies
- downstream engines compute
- Assembly selects
- Output Template formats

---

## 6. Inbound Customer Message Processing

[FROM: RUNTIME_EXECUTION_FLOW.md]
[FROM: CUSTOMER_CHAT_INTAKE_RULES.md]

Step 5 — Intake Processing:
- Apply `CUSTOMER_CHAT_INTAKE_RULES.md`
- Accept inbound customer input in these forms:
  - plain text chat
  - screenshot of chat
  - pasted chat history
  - short messages
  - emojis combined with text
  - voice note transcripts once converted to text upstream
- Extract structured inputs from raw customer message

Intake handling includes:
- language detection
- screenshot and pasted-chat handling
- short-message handling
- pre-qualification extraction
- objection-related emitted signals
- normalized handoff into qualification

Intake must:
- mark missing information as missing
- preserve customer meaning
- stop where qualification begins

Intake must not:
- decide pricing
- decide final answers
- format customer reply
- override qualification or runtime sequencing

Output of Step 5:
- normalized input signals only
- no routing ownership transfer beyond handoff inputs

---

## 7. Qualification and Routing Gate

[FROM: RUNTIME_EXECUTION_FLOW.md]
[FROM: QUALIFICATION_ENGINE.md]
[FROM: AUTHORITY_INDEX.md]

Step 6 — Qualification & Routing:
- Apply `QUALIFICATION_ENGINE.md`
- Qualification must produce an explicit status signal
- Runtime must not proceed to Negotiation unless `QUALIFICATION_STATUS = READY_FOR_NEGOTIATION`

Qualification is the canonical writer for:
- `request_type`
- `QUALIFICATION_STATUS`
- `missing_fields`
- `service_intent`
- `active_service_context`
- `detected_service_intent_in_message`

Qualification output must also include:
- `qualification_state`
- `context_completeness`
- `missing_info_ask_count`

Qualification must:
- resolve missing fields deterministically
- preserve already-known context through carry-forward
- enforce ambiguity guards
- avoid assumption-based progression

Qualification must not:
- generate customer-facing text
- perform pricing calculations
- perform silence handling
- select tone
- format output

If qualification is not ready:
- route to clarification or graceful exit
- do not allow forward progression into negotiation or pricing

---

## 8. Service Context Continuity Gate

[FROM: RUNTIME_EXECUTION_FLOW.md]

Mandatory order:
1. Compute `detected_service_intent_in_message` from current message
2. Preserve `active_service_context` from conversation state
3. Run Phase 4.8 Service Context Continuity Gate before any update to `active_service_context`

If the continuity gate triggers:
- stop the pipeline for this turn
- output must be only:
  - `PHASE4_6_HUMAN_PHRASE_LIBRARY.md → L.3 SERVICE CONTEXT CLARIFIER (ONE QUESTION)`
- do not include service explanations, pricing, or technical answers in the same turn
- do not mutate `active_service_context` on this turn

Resume:
- only on next customer reply

Update rule:
- only after customer explicitly confirms switching services may `active_service_context` be updated

---

## 9. Phase 3A Qualifier-First Gate
Note:
- Runtime progression into Negotiation remains gated by `READY_FOR_NEGOTIATION`.
- `PRICE_LADDER_ENGINE.md` still contains tolerant entry wording for `READY` as well.
- Until reconciled, architecture and tests should treat `READY_FOR_NEGOTIATION` as the primary progression state.

[FROM: RUNTIME_EXECUTION_FLOW.md]
[FROM: PHASE3A_QUALIFICATION_DECISION_MATRIX.md]
[FROM: QUALIFICATION_ENGINE.md]
[FROM: PHASE4_8_MESSAGE_ASSEMBLY_MAP.md]

Rule:
- after Phase 0–2 has produced ready state
- and Phase 3 begins
- run Phase 3A before Phase 3B pricing and SKU logic
- runtime phase label remains `PHASE_3`

If `phase3a_required == true`:
- Assembly must output exactly one Phase 3A qualifier question and stop
- output must use the mapped verbatim phrase block only
- Phase 3B must not execute until the customer replies and `phase3a_complete == true`

If `phase3a_complete == true`:
- proceed to Phase 3B pricing, SKU selection, and later Phase 4 responses

---

## 10. Global Silence Gate

[FROM: RUNTIME_EXECUTION_FLOW.md]
[FROM: RUNTIME_STATE_MACHINE.md]
[FROM: SILENCE_HANDLING_ENGINE.md]
[FROM: PHASE3_ORCHESTRATION_WIRING_ADDENDUM.md]

Purpose:
- silence handling applies in all phases
- silence is time-based only
- silence is not tied only to post-pricing

Required runtime state:
- `LAST_COUNTED_OUTBOUND_TIMESTAMP`
- `LAST_CUSTOMER_SIGNAL_TIMESTAMP`
- `FOLLOW_UP_COUNT`
- `SILENCE_SUPPRESSED`
- `SILENCE_SUPPRESSION_REASON`
- `INPUT_MODE`
- `CONVERSATION_STATUS`
- `AGENT_TAKEOVER_FLAG`

Customer signal gate:
- update `LAST_CUSTOMER_SIGNAL_TIMESTAMP` only on explicit new customer communication

Counted outbound rule:
- update `LAST_COUNTED_OUTBOUND_TIMESTAMP` only when system sends an outbound message that expects customer reply

Blockers:
- `CONVERSATION_STATUS != OPEN`
- `AGENT_TAKEOVER_FLAG == TRUE`
- `SILENCE_SUPPRESSED == TRUE`
- `INPUT_MODE == BACKFILL_BATCH`

Execution:
- invoke `SILENCE_HANDLING_ENGINE.md`

Outcomes:
- if `EXIT_FLAG == TRUE`:
  - stop outbound actions
  - mark silence terminated
  - exit
- if `ALLOW_ACTION == TRUE`:
  - allow one follow-up action
- if `SILENCE_STAGE == NONE`:
  - proceed with normal phase engine selection

---

## 11. Negotiation, Pricing, Objection, and Closing

[FROM: RUNTIME_EXECUTION_FLOW.md]

Step 6.1 — Negotiation Logic:
- execute `NEGOTIATION_LOGIC_MODULE.md`
- logic only
- no customer phrasing

Step 6.2 — Price Ladder Execution:
- if negotiation routing indicates pricing response is required:
  - execute `PRICE_LADDER_ENGINE.md`

Step 6.3 — Objection Resolution:
- execute `OBJECTION_RESOLUTION_ENGINE.md`
- logic only
- no customer phrasing
- runs after price exposure when applicable

Step 6.4 — Closing and Handover:
- execute `CLOSING_HANDOVER_ENGINE.md`
- control only
- no customer phrasing
- if `AUTOMATION_TERMINATED_FLAG == TRUE`:
  - stop all automation immediately

---

## 12. Message Construction and Output

[FROM: GLOBAL_RUNTIME_FLOW_MAP.md]
[FROM: PHASE4_8_MESSAGE_ASSEMBLY_MAP.md]
[FROM: OUTPUT_RESPONSE_TEMPLATE.md]

Assembly:
- `PHASE4_8_MESSAGE_ASSEMBLY_MAP.md`
- selects `selected_phrase_id`
- must not invent text
- must only pick approved phrase blocks
- must not rewrite classification

Output formatting:
- `OUTPUT_RESPONSE_TEMPLATE.md`
- final formatting only
- language order
- timestamp
- hygiene

Hard rules:
- Assembly selects only
- Phrase Library writes only
- Output Template formats only

---

## 13. Runtime State Governance

[FROM: RUNTIME_STATE_MACHINE.md]

States:
- S0 — BOOT
- S1 — LOAD_MANIFEST
- S2 — LOAD_COMPONENTS
- S3 — VALIDATE_RUNTIME
- S4 — ACTIVE
- S5 — DEGRADED
- S6 — HALT

Inside ACTIVE:
- apply Intake
- then call Qualification
- do not call Negotiation unless qualification is ready
- do not execute any engine if `CONVERSATION_STATUS != OPEN`
- do not execute any engine if `AUTOMATION_TERMINATED_FLAG == TRUE`
- if `HANDOVER_REQUIRED_FLAG == TRUE`:
  - set `AGENT_TAKEOVER_FLAG = TRUE`
  - stop automation immediately

Hard stop conditions include:
- manifest missing or unreadable
- required file missing
- lock conflict
- checklist failure
- validation gate failure

HALT behavior:
- stop runtime
- emit internal error only
- no customer-facing text

---

## 14. Session Rule After Termination

[FROM: RUNTIME_STATE_MACHINE.md]

If customer sends a new message after:
- `AUTOMATION_TERMINATED_FLAG == TRUE`
or
- `CONVERSATION_STATUS != OPEN`

Then:
- prior session remains terminal and immutable
- orchestration must open a new session context
- new session may import a context snapshot for continuity
- prior outcomes must not be reversed

---

## 15. Runtime Guardrail Rules

[FROM: KNOWLEDGE__RUNTIME_CORE_BUNDLE.md]

Phase 0 guardrail rules include:
- Phase 0 has absolute authority to halt, gate, or delay execution
- no downstream engine may override Phase 0 decisions
- mixed, conflicting, or ambiguous identities halt progression
- unknown, unsafe, or contradictory inputs halt execution
- pricing guardrails apply before execution
- output hygiene constraints are authoritative
- engines may emit only contract signals
- if emitted signal has no routing coverage in test mode, response is suppressed
- in production mode, fallback routing must be used




────────────────────────────────────────────
PHASE 0–6 RENDERING + ROUTING CONTRACT (LOCKED)
────────────────────────────────────────────

Purpose:
- Eliminate ambiguity between internal truth (Phase 6) and customer-facing output (Phase 4.6)
- Prevent future drift in service explanation behavior

### CONTROL CHAIN (MANDATORY)

PHASE4_8_MESSAGE_ASSEMBLY_MAP.md
    → Routing authority (decides WHAT to use)

PHASE4_6_HUMAN_PHRASE_LIBRARY.md
    → Customer-facing output (decides HOW it is said)

PHASE6__SERVICE_CANON_BUNDLE.md
    → Internal truth + constraints only (defines WHAT is true)

---

### HARD RENDERING RULES

1) Phase 6 canon MUST NOT be emitted directly to customers

2) The ONLY exception:
   - PHASE_0_2_MIN blocks (explicitly allowed for intake)

3) All customer-facing service responses MUST come from:
   - PHASE4_6_HUMAN_PHRASE_LIBRARY.md

4) No engine may paraphrase Phase 6 into customer output

---

### ROUTE B (PHASE 0–2) — HARD CONTRACT

IF request_type == SERVICE_CONFIRMED:

- MUST use ONLY PHASE4_6 customer-facing blocks
- MUST NOT emit PHASE6 canon directly
- MUST render selected phrase VERBATIM
- MUST NOT append Phase 6 explanation

---

### ARCHITECTURAL INTERPRETATION

- Phase 6 = constraint layer (internal truth)
- Phase 4.6 = rendering layer (customer output)
- Phase 4.8 = decision layer (routing logic)

This separation is mandatory and must not be collapsed.

---

### ANTI-DRIFT RULE

Every service behavior MUST be documented in 3 layers:

1) CURRENT LIVE RUNTIME
2) HISTORICAL RECOVERED INTENT
3) OPEN DECISION (if unresolved)

Do NOT merge these layers into one narrative.



# GAP-008 NORMALIZATION — PHASE 4–6 RENDER CONTRACT

## CURRENT LIVE RUNTIME (PROVEN)

- Phase 6 is manifest-active
- Phase 6 contains service truth + constraints
- Phase 6 MUST NOT be rendered directly to customers

- Phase 4.6 is the ONLY customer-facing phrase authority
- Phase 4_8 controls routing and selection of Phase 4.6 blocks

- Route B (SERVICE_CONFIRMED):
  - uses ONLY PHASE4_6_HUMAN_PHRASE_LIBRARY.md
  - MUST NOT render Phase 6 content directly

## HISTORICAL CONTEXT

- Previous Route B used Phase 6 bundle sections directly
- This behavior was replaced in commit 94a7d8a

## SYSTEM RULE (CANONICAL)

1. Phase 6 = TRUTH LAYER (NON-RENDERABLE)
2. Phase 4.6 = RENDER LAYER (CUSTOMER-FACING ONLY)
3. Phase 4_8 = ENFORCEMENT LAYER (ROUTING + SELECTION)

## HARD CONSTRAINT

No engine may:
- render Phase 6 content directly
- paraphrase Phase 6 into customer output
- bypass Phase 4.6 for customer communication

## FAILURE MODE

If violated:
- Phase 6 leaks into output
- routing inconsistency occurs
- documentation diverges from runtime
