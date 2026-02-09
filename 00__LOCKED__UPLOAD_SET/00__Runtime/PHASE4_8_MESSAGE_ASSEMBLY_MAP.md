# PHASE 4.8 — MESSAGE ASSEMBLY MAP

Status: ACTIVE / LOCKED BEHAVIOR 
Phase: 4.8  
Scope: Message assembly structure, ordering, caps, and slot wiring  
Dependencies:
- Phase 4.6 — Human Phrase Library (LOCKED; core A–L)
- Phase 4.7 — Hook Question Engine (LOCKED)
- Phase 4.5 — Tone Engine (ACTIVE; enforceable constraints)

---

## PURPOSE

Define how a single customer-facing message is assembled from internal blocks.

This document controls:
- Block selection (what can be included)
- Ordering (what must come before/after)
- Caps (max blocks, max questions)
- Hook slot wiring (if/where hooks may appear)


- Suppression precedence (tone, silence, objection, closing)

This document does NOT:
- Create or rewrite customer-facing phrases
- Introduce new tone logic
- Modify Phase 4.6 wording or intent
- Modify Phase 4.7 hook logic

Assembly has final authority over inclusion/exclusion.

---

## ASSEMBLY OUTPUT CONTRACT (LOCKED)

Customer sees ONE coherent message only.

Display format must be (HARD):

BILINGUAL RENDERING RULE (DO NOT INTERLEAVE):
1) Render the FULL customer message in ENGLISH first (all included blocks concatenated in the selected order).
2) Then render the FULL customer message in ARABIC (same content, same order, Arabic versions).
3) Do NOT alternate languages per block.
4) Separate the two language sections with exactly ONE blank line.
5) Timestamp is ALWAYS the final line (after both languages).

Final output layout:

<ENGLISH full message>
(blank line)
<ARABIC full message>
<span style="color:#6b7280">Timestamp: YYYY-MM-DD HH:MM</span>

---

## ASSEMBLY INPUTS (READ-ONLY)

Assembly evaluates these inputs only (no mutation):

1) Phrase blocks (Phase 4.6)
- Categories: A–L (opening → neutral transition)

2) Tone constraints (Phase 4.5)
- Allowed block categories
- Hook permission flags (allow/suppress)
- Escalation rules (non-escalatory)

3) Hook output (Phase 4.7)
- Hook candidates (questions or prompts)
- Hook “allowed contexts” definition is locked in 4.7

4) Suppression signals (runtime/state)
- Silence detected
- Objection detected
- Price tension detected
- Closing lock active
- Repetition risk (pattern already used recently)

5) Service context signals (runtime/state)
- active_service_context
- detected_service_intent_in_message

---

## MESSAGE BLOCK MODEL (STRUCTURE)

A response is assembled from 0–3 blocks, chosen contextually:

Block Types (internal):
- B0: Presence / Opening (4.6.A)
- B1: Context Acknowledgement (4.6.B)
- B2: Core Value / Explanation (4.6.C–K as applicable)
- B3: Neutral Transition / Soft Next Step (4.6.L)
- H1: Hook Slot (4.7 output) — conditional

Notes:
- Blocks are OPTIONAL unless required for clarity.
- “Core Value” means: the minimum helpful content the customer needs now.
- Hooks are never required.

---

## ORDERING RULES (HARD)

If multiple blocks are included, ordering must follow:

1) B0 (if used)
2) B1 (if used)
3) B2 (if used; core content)
4) B3 (if used)
5) H1 (if allowed)

Hard rules:
- Hooks (H1) may only appear AFTER core content (B2) when B2 exists.
- Hooks may never appear before the message has delivered value.
- Hooks may never replace core content.

---

## CAPS (HARD)

- Max blocks per response: 3 (excluding bilingual rendering)
- Max questions per response: 1 (total, across whole message)
- If H1 is a question, the rest of the message must contain 0 questions.

────────────────────────────────────────────────────────────
GREETING ROUTES (HARD OVERRIDE — NO DRIFT)
────────────────────────────────────────────────────────────

## GREETING_ONLY (NEW / NO CONTEXT) — ONBOARDING GREETING
IF request_type == GREETING_ONLY:
  - suppress_hooks = TRUE
  - Output MUST use ONLY:
    - PHASE4_6_HUMAN_PHRASE_LIBRARY.md → A4_GREETING_SERVICE_CONTEXT
  - selected_phrase_id MUST equal A4_GREETING_SERVICE_CONTEXT
  - STOP (do not append any other blocks).

## REENTERED_CONTINUE (CONTEXT EXISTS) — CONTINUE WITHOUT RESET
IF request_type == REENTERED_CONTINUE:
  - suppress_hooks = TRUE
  - Output MUST use ONLY:
    - PHASE4_6_HUMAN_PHRASE_LIBRARY.md → A6_REENTERED_CONTINUE
  - selected_phrase_id MUST equal A6_REENTERED_CONTINUE
  - STOP (do not append any other blocks).

### 3A) Phase 3A Qualifier-First Gate (HARD)
# LOCK_METADATA
# LOCK_STATUS: LOCKED
# LOCK_SCOPE: PHASE 3A — qualifier_id → phrase routing + suppression rules
# LOCK_DATE: 2026-02-09
# LOCK_REASON: Phase 3A UAT passed; prevent legacy blocks overriding qualifier flow
# CHANGE_CONTROL: Architecture approval required

IF phase == PHASE_3
AND phase3a_required == true
AND phase3a_qualifier_id is present:

  - suppress_hooks = TRUE
  - Output MUST be:
    - exactly 1 question
    - use ONLY the matching block in PHASE4_6_HUMAN_PHRASE_LIBRARY.md

  - Mapping (phase3a_qualifier_id → Phrase block):
    - PHASE3A_Q_PAINT_CONDITION_REPAINT_SCRATCH → PHASE3A_Q_PAINT_CONDITION_REPAINT_SCRATCH
    - PHASE3A_Q_PPF_COVERAGE_INTENT             → PHASE3A_Q_PPF_COVERAGE_INTENT
    - PHASE3A_Q_PPF_DRIVING_PATTERN             → PHASE3A_Q_PPF_DRIVING_PATTERN
    - PHASE3A_Q_PPF_COMPARISON_FOCUS            → PHASE3A_Q_PPF_COMPARISON_FOCUS
    - PHASE3A_Q_CERAMIC_GOAL                    → PHASE3A_Q_CERAMIC_GOAL
    - PHASE3A_Q_CERAMIC_WASH_PATTERN            → PHASE3A_Q_CERAMIC_WASH_PATTERN
    - PHASE3A_Q_TINT_GOAL                       → PHASE3A_Q_TINT_GOAL
    - PHASE3A_Q_TINT_COVERAGE                   → PHASE3A_Q_TINT_COVERAGE
    - PHASE3A_Q_WRAP_FINISH                     → PHASE3A_Q_WRAP_FINISH
    - PHASE3A_Q_POLISHING_SCOPE                 → PHASE3A_Q_POLISHING_SCOPE

  - selected_phrase_id MUST equal the phrase block name above.
  - STOP (do not append any other blocks).

## PHASE 1–2 — PROFESSIONAL PRESENCE MODE (MANDATORY)

Purpose:
- Establish calm, confident human presence
- Guide without educating
- Keep communication light and non-technical

Hard Rules:
- Output MUST be short (1–2 sentences max per language)
- Output MUST ask exactly 1 soft guiding question
- NO education blocks allowed
- NO lists, bullets, or multi-option breakdowns
- NO brand, spec, warranty, pricing, or comparison language
- NO emojis
- NO sales pressure
- NO internal labels or explanations

Enforcement (Hard):
Trigger condition (ALL must be true):
- request_type in {BROWSING_GENERIC, SERVICE_INQUIRY}
- service_intent == unknown
- missing_fields is empty

Required output behavior:
- Use ONLY:
  1) PHASE4_6 → L.0 (Browsing Safe Primer — ONE QUESTION)
- Do NOT append any additional question.
- Suppress education, comparison, and advisory checklists
- Suppress hooks (H1)

## PHASE 1–2 — LOW-INTENT BROWSING (OVERRIDE)
---
## PHASE 1–2 GATING RULE (HARD PRE-ROUTE OVERRIDE)

Purpose:
- Ensure early-stage browsing queries remain light and non-forcing before service intent is clarified.
- Prevent premature vehicle qualification or service listing during low-intent inquiry phases.

Execution order (HARD):
- Evaluate PHASE 1–2 trigger conditions BEFORE evaluating SERVICE ROUTING routes.
- If any PHASE 1–2 condition matches → execute PHASE 1–2 output and suppress SERVICE ROUTING for that turn.
- If no PHASE 1–2 condition matches → proceed to SERVICE ROUTING.

Rationale:
- PHASE 1–2 rules are guardrails for exploratory browsing; they must not be overridden by service routing logic.
- Service Routing assumes service_intent is known or being actively clarified; it cannot bypass PHASE 1–2 protection.

Implementation:
- At runtime: Check PHASE 1–2 conditions first.
- Match found → use PHASE 1–2 output only.
- No match → evaluate SERVICE ROUTING routes normally.
---

## QUALIFICATION NOT-READY SUPPRESSION (HARD)

Default trigger condition (any one):
- QUALIFICATION_STATUS = NOT_READY
- missing_fields is not empty
- allowed_next_actions includes ask_missing_info

Default output behavior (when no exception applies):
- Output MUST contain exactly 1 question total.
- That question MUST be from L.1 QUALIFICATION CLARIFIERS (VEHICLE DETAILS) using missing_info_ask_count variant (V1/V2/V3).
- Output MUST contain ONLY the question line(s) (no prefacing, no acknowledgements, no examples, no extra sentences).
- Suppress hooks, preferences, education, upsell blocks until QUALIFICATION_STATUS = READY.
- Do NOT ask preference questions until QUALIFICATION_STATUS = READY.

Exception A — Service Confirmed while NOT_READY (allowed minimal value + 1 question)
Applies when ALL are true:
- request_type == SERVICE_CONFIRMED
- service_intent != unknown
- missing_fields includes vehicle_model OR vehicle_year

Required output behavior:
- Include the Phase 6 service explanation block for the detected service_intent (NO PRICES, NO OFFERS).
- Append exactly 1 question from L.1 asking vehicle_model + vehicle_year (V1/V2/V3 as applicable).
- Do NOT include any other questions.
- Suppress hooks.

Exception B — Price Request while NOT_READY (allowed minimal value + 1 question)
Applies when ALL are true:
- request_type == PRICE_REQUEST
- service_intent != unknown
- missing_fields includes vehicle_model OR vehicle_year

Required output behavior:
- Include the Phase 6 service explanation block for the detected service_intent (NO PRICES, NO OFFERS).
- Append exactly 1 question from L.1 asking vehicle_model + vehicle_year (V1/V2/V3 as applicable).
- Do NOT include any other questions.
- Suppress hooks.

---
---


## SERVICE ROUTING (PHASE 6 — REQUIRED)

Purpose:
- Prevent suppression for valid customer questions by defining approved service response paths.
- Allow “What services do you offer?” to return the approved service overview (not invented).
- Bind Phase 6 service files into legal assembly paths.

Authority:
- Service wording MUST come from PHASE4_6_HUMAN_PHRASE_LIBRARY.md and/or PHASE6__SERVICE_*.md only.
- No generic listing or invention is allowed outside these blocks.

### Route Selector (input from QUALIFICATION_ENGINE output)

The runtime must route using these fields (no assumptions):
- request_type: BROWSING_GENERIC | SERVICE_CONFIRMED | SERVICE_INFERRED | PRICE_REQUEST
- service_intent: ceramic | ppf | tint | wrap | polishing | graphene | interior_ceramic | unknown
- missing_fields: may include vehicle_model, vehicle_year

- active_service_context: ceramic | ppf | tint | wrap | polishing | graphene | interior_ceramic | null
- detected_service_intent_in_message: ceramic | ppf | tint | wrap | polishing | graphene | interior_ceramic | unknown
### Service Context Continuity Gate (HARD PRE-ROUTE OVERRIDE)

This gate is evaluated BEFORE any Approved Routes.

Purpose:
- Prevent silent switching to a different service mid-conversation.

Trigger condition (all must be true):
- active_service_context != null
- detected_service_intent_in_message != unknown
- detected_service_intent_in_message != active_service_context

Required output behavior (override Route B):
- Do NOT route to any PHASE6__SERVICE_* explanation in this turn.
- Ask exactly 1 clarification question to confirm whether the customer wants:
  (a) to compare services, OR
  (b) to switch services.
- Suppress hooks, pricing, and technical deep dives.
- Ask exactly 1 clarification question using:
  PHASE4_6_HUMAN_PHRASE_LIBRARY.md → L.3 SERVICE CONTEXT CLARIFIER (ONE QUESTION)
- Suppress hooks, pricing, and technical deep dives.
After clarification:
- If switch confirmed → update active_service_context and proceed with Route B on next turn.
- If comparison confirmed → proceed via Phase 8 comparison/education path (if available) on next turn.

### Approved Routes

Route 0C — Brand Refinement (service context already active)
IF constraints includes brand_keyword_detected = true AND active_service_context != null:
- Use ONLY: PHASE4_6_HUMAN_PHRASE_LIBRARY.md → L.6 (BRAND REFINEMENT — NO QUESTION)
- Output MUST render VERBATIM.
- Suppress hooks.
- Do NOT ask vehicle questions in this route.

Route A — Universal Service Inquiry (customer asks generally)
IF request_type == BROWSING_GENERIC AND service_intent != unknown:
- Use phrase block: PHASE4_6_HUMAN_PHRASE_LIBRARY.md → L.2 (BROWSING_GENERIC — SERVICE OVERVIEW)
- Append 1 qualifier question only (per OUTPUT_RESPONSE_TEMPLATE rules):
  Ask for vehicle_model + vehicle_year using PHASE4_6 → L.1

Route B — Specific Service Confirmed (customer says “ceramic/ppf/tint/wrap/polish/graphene”)
IF request_type == SERVICE_CONFIRMED AND service_intent != unknown:
- Use service explanation block from Phase 6:
  - ceramic → PHASE6__SERVICE_CERAMIC.md
  - ppf → PHASE6__SERVICE_PPF.md
  - tint → PHASE6__SERVICE_TINT.md
  - wrap → PHASE6__SERVICE_WRAP.md
  - polishing → PHASE6__SERVICE_POLISHING.md
  - graphene → PHASE6__SERVICE_GRAPHENE.md
  - interior_ceramic → PHASE6__SERVICE_INTERIOR_CERAMIC.md
- If missing vehicle_model/vehicle_year:
  ask using PHASE4_6 → L.1 (one question only)

Route C — Service Inferred (customer implies protection/shine, but doesn’t name service)
IF request_type == SERVICE_INFERRED:
- Use neutral clarifier (no listing):
  ask preference-based clarifier from PHASE4_6 (qualification clarifier set)
- Do NOT list services unless Route A applies.

Route D — Price Request while NOT_READY (handled by NOT-READY Exceptions)
IF request_type == PRICE_REQUEST AND (missing_fields includes vehicle_model OR vehicle_year):
- Do NOT use PRICE_LADDER_ENGINE here.
- Follow: "Exception B — Price Request while NOT_READY" under QUALIFICATION NOT-READY SUPPRESSION (HARD).
  (That exception provides: Phase 6 service explanation (NO PRICES) + exactly 1 vehicle_model/year question.)

Route E — Price Request while READY (pricing allowed)
IF request_type == PRICE_REQUEST AND missing_fields is empty:
- Use PRICE_LADDER_ENGINE.md output (pricing allowed ONLY inside that engine’s constraints).
- Do NOT add additional questions unless PRICE_LADDER_ENGINE explicitly requires a single clarifier.
- Suppress hooks unless hook gates pass AND question-cap remains respected.

Route F — Price Resistance / Comparison (Phase 7 controlled pricing response)
IF constraints includes price_resistance = true AND missing_fields is empty:

- Use PRICE_LADDER_ENGINE.md output (pricing allowed ONLY inside that engine’s constraints).
- Require EXACTLY 1 controlled clarifier (coverage / priority) IF the price ladder output requires it.
- Do NOT end with a comfort-only line.
- Suppress hooks unless hook gates pass AND question-cap remains respected.



## HOOK SLOT WIRING (LOCKED BEHAVIOR)

Hook Slot (H1) inclusion is permitted ONLY when ALL conditions pass:

Gate A — Tone Allowance (4.5):
- Tone must explicitly allow hooks

Gate B — Suppression Clearance (runtime):
- No silence suppression
- No objection suppression
- No price-tension suppression
- No closing-lock suppression

Gate C — Core Value Delivered (assembly):
- If B2 is present, H1 must come after B2
- If B2 is absent, H1 is allowed only when the customer explicitly asked a question that requires a follow-up question

Gate D — Question Cap:
- Adding H1 must not exceed max questions (=1)

If any gate fails → H1 is excluded (no fallback hook).


---

## PHASE 7 — CLOSING & FOLLOW-UP ROUTING (REQUIRED)

Purpose:
- Wire Phase 7 states into legal assembly paths using existing phrase authority only.
- Phase 7 must NOT introduce service education, pricing, negotiation, or new wording.

Authority:
- Execution authority: Production runtime state + routing only (this file + QUALIFICATION_ENGINE.md + RUNTIME_EXECUTION_FLOW.md)
- Customer-facing wording authority: PHASE4_6_HUMAN_PHRASE_LIBRARY.md only
- Pricing wording authority: PRICE_LADDER_ENGINE.md only (NOT used in Phase 7)

### State: REENTERED (Clarified Intent)

Behavior intent:
- Resume the conversation without resetting context.
- Do NOT repeat comfort-only language (e.g., “take your time”).
- Signal availability and readiness to continue.

Assembly rules (unchanged):
- Use PHASE4_6 → B (Context acknowledgement)
- Use PHASE4_6 → L (Neutral transition)
- Questions: 0

### Phase 7 Eligibility Gate (Hard)

Phase 7 may execute ONLY if a valid Phase 7 entry condition is true (per production runtime state keys):
- READY_TO_PROCEED
- THINKING
- SILENT
- DEFERRED
- REENTERED

If Phase 7 is triggered without a valid entry condition:
- Output exactly: [ARCHITECTURE VIOLATION — RESPONSE SUPPRESSED]

### Service Context Persistence Rule (MANDATORY)

Rule:
- Phase 7 MUST NOT clear, reset, or overwrite active_service_context.

Clarification:
- Silence, deferral, or re-entry does NOT imply loss of service context.
- active_service_context remains the last confirmed service unless:
  (a) customer explicitly switches service, OR
  (b) conversation is explicitly reset as a NEW CHAT.

Impact:
- Enables Service Context Continuity Gate to work correctly after Phase 7.
- Prevents accidental service drift on re-entry or late technical questions.

### Phase 7 Assembly Rules (Hard)

- Hooks are suppressed in Phase 7 (no H1)
- No Phase 6 service explanation in Phase 7
- No PRICE_LADDER_ENGINE output in Phase 7
- Max questions per response: 0 (default)

### Phase 7 State → Approved Phrase Sources

State: THINKING
- Use:
  - PHASE4_6 → G (COMMON CONCERNS) — select one line
  - PHASE4_6 → L (NEUTRAL TRANSITION) — select one line
- Questions: 0

State: DEFERRED
- Use:
  - PHASE4_6 → G (COMMON CONCERNS) — select one line
  - PHASE4_6 → L (NEUTRAL TRANSITION) — select one line
- Questions: 0

State: SILENT
- Use:
  - PHASE4_6 → L (NEUTRAL TRANSITION) — select one line
- Questions: 0

State: REENTERED
- Use:
  - PHASE4_6 → B (CONTEXT ACKNOWLEDGEMENT) — select one line
  - PHASE4_6 → L (NEUTRAL TRANSITION) — select one line
- Questions: 0

State: READY_TO_PROCEED
- Use:
  - PHASE4_6 → L (NEUTRAL TRANSITION) — select one line
- Questions: 0
- Note: Although Phase 7 allows one logistical question, no locked logistical question exists in Phase 4.6.
  To avoid invention, READY_TO_PROCEED remains question-free.

---

## SUPPRESSION PRECEDENCE (HARD)

When multiple constraints apply, precedence is:

1) Closing Lock (highest)
2) Objection / Resistance
3) Silence / Non-response risk
4) Price Tension
5) Tone Restrictions
6) Repetition Avoidance
7) Hook Opportunity (lowest)

### Phase 7 Override (Hard)

If Phase 7 is active (valid Phase 7 entry condition met per production runtime state keys):
- Suppress hooks (H1) unconditionally
- Suppress Phase 6 service explanation blocks
- Suppress PRICE_LADDER_ENGINE output
- Assemble ONLY from "PHASE 7 — CLOSING & FOLLOW-UP ROUTING"

Interpretation:
- Suppression always reduces complexity (fewer blocks).
- Suppression never changes wording; it only excludes blocks.

---

## NON-ESCALATION SAFETY (HARD)

Assembly must enforce:
- No urgency stacking
- No persuasion + price pressure in the same message
- No hook immediately after objection or tension
- No repeated structural pattern in consecutive turns when alternatives exist

If safety risk detected → default to minimal build (B1 or B2 only) with no hook.

---

## MINIMAL BUILD POLICY (DEFAULT)

Default assembly target:
- 1–2 blocks total
- 0 hooks unless clearly safe and allowed
- Prefer clarity over completeness

---

## GOVERNANCE / LOCK CONDITIONS

This file is ready to lock when:
- Phase 4.6 remains locked (no phrase changes)
- Phase 4.7 remains locked (no hook logic changes)
- Phase 4.5 tone constraints remain enforceable at assembly level

After lock:
- Any change requires a version bump and a change-log entry.

---

