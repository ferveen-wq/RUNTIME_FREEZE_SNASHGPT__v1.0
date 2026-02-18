

# QUALIFICATION_ENGINE.md

Status: LOCK CANDIDATE
LOCK_SCOPE: PHASE 1 — QUALIFICATION ENGINE ONLY
LOCK_REASON: Phase-1 boundaries hardened to prevent drift (no pricing, no negotiation, no tone logic, no silence handling, no customer-facing redirection).
LAST_CHANGE: 2026-01-05
CHANGE_SUMMARY:
- Clarified readiness as context readiness (not buying readiness)
- Clarified confidence as classification certainty (not conversion likelihood)
- Allowed coarse request classification strictly for routing safety only
- Explicitly blocked recommendation or redirection behavior in Phase 1
EDIT_POLICY: NO FURTHER EDITS ALLOWED WITHOUT ARCHITECTURE APPROVAL

## FILE_METADATA

## PURPOSE

Define a deterministic qualification layer that evaluates incoming context and signals to determine readiness, constraints, and routing requirements before any response, tone, or service framing is applied.

The engine exists to reduce friction, minimize unnecessary questioning, prevent assumption-based progression, and ensure downstream engines operate only on validated context.

## SCOPE


This engine operates exclusively on pre-response context evaluation. It processes available signals to determine qualification completeness, identify missing critical context, and establish whether downstream engines may proceed.

The scope includes readiness assessment, constraint detection, routing eligibility validation, and coarse request classification strictly for routing safety (e.g., customer vs non-customer contact, on-scope vs off-scope request, and service-adjacent vs direct request).

This engine does not generate responses, recommend or redirect the user to services, influence tone, or interact with pricing, discounts, offers, or promotional logic. Any customer-facing redirection or service suggestion is downstream responsibility and is out of scope here.

## NON_GOALS

This engine does not infer buying intent, predict conversion likelihood, or determine service suitability in a sales sense.

It may only classify the request at a coarse level for routing safety (e.g., non-customer contact such as job inquiry/vendor pitch, off-scope request, or service-adjacent issue) without making recommendations or customer-facing suggestions.

It does not generate customer-facing language, recommend actions, trigger offers, or influence pricing, discounts, or promotions.

It does not replace routing, tone selection, sales logic, or response generation engines, nor does it perform data enrichment or external lookups.

## INPUT_CHANNELS

This engine consumes structured and unstructured context provided by upstream layers, including but not limited to user messages, session metadata, language detection output, and routing pre-signals.

Inputs are limited to data already available at runtime and explicitly passed by prior engines. No direct user interrogation, external data retrieval, or implicit context inference is permitted.

## PARAMETER_COMPATIBILITY (REFERENCE ONLY)

This engine is orchestration/gating only.
- Global parameters (core + dynamic) are loaded upstream via the runtime manifest.
- This engine may READ existing parameters from context, but must NOT create or mutate parameter values.
- Parameter sources of truth:
  - 02__Parameters/GLOBAL_CORE_CONTEXT_PARAMETERS.md
  - 02__Parameters/CONVERSATION_DYNAMIC_PARAMETERS.md

This engine’s only mandatory orchestration alias output is:
- QUALIFICATION_STATUS (READY_FOR_NEGOTIATION | NOT_READY)

## OUTPUT_CHANNELS

This engine emits a single qualification result object intended for consumption by routing and downstream engines.

The output must include:
- qualification_state: A discrete state label from QUALIFICATION_STATES.
- context_completeness: A boolean indicating whether minimum required context is satisfied.
- missing_fields: An ordered list of missing context keys required to proceed.
- missing_info_ask_count (integer)
  - Meaning: how many times we have asked for the same missing minimum fields in this session
  - Range: 1–3
  - Used by Assembly to choose L.1 variant (V1/V2/V3) and avoid repetitive wording
### REQUIRED FIELD KEYS (FOR ASSEMBLY + ORCHESTRATION)

To prevent runtime improvisation, missing_fields MUST use these exact keys when applicable:
- vehicle_model
- vehicle_year

To support Phase 4.8 suppression rules, this engine MUST also emit:
- request_type: one of
  - BROWSING_GENERIC (customer asking generally: “what do you offer / services?”)
  - GREETING_ONLY (greeting-only with no other details AND no prior context)
  - REENTERED_CONTINUE (greeting-like message AND prior context exists; continue without reset)
  - SERVICE_CONFIRMED (explicit service keyword: ceramic / ppf / tint / wrap)
  - SERVICE_INFERRED (implied protection intent without naming a service)
- service_intent: one of
  - ceramic | ppf | tint | wrap | unknown

  To support service-context continuity gating (Phase 4.8), this engine MUST also emit:
- active_service_context: ceramic | ppf | tint | wrap | null
- detected_service_intent_in_message: ceramic | ppf | tint | wrap | unknown

Rule (non-overwrite):
- detected_service_intent_in_message is derived from the CURRENT message only.
- active_service_context is the LAST CONFIRMED service in the conversation.
- active_service_context MUST NOT be overwritten just because a different service keyword is detected in the current message.
- Only update active_service_context after explicit customer confirmation to switch services.

Notes:
- This is not sales logic. It is routing classification only.
- This does not set price, package, or recommendations.

--------------------------------------------------------------------------
## PHASE 3A — SERVICE-SPECIFIC QUALIFIER SEQUENCING (Decision Matrix Aligned)

# ============================================================
PHASE 3A — EMOTIONAL QUALIFICATION ARCHITECTURE
GOVERNED BY PHASE 6 CANON
# ============================================================

PURPOSE:
Standardize how qualification questions are structured across all services.

Core rule:
One emotional axis per question.
Maximum one question per reply.
Never stack axes.

------------------------------------------------------------
AXIS 1 — RISK AXIS
------------------------------------------------------------

Purpose:
Identify damage anxiety or regret prevention motive.

Used for:
- PPF
- Ceramic (light risk)
- Wrap (fading concerns)
- Tint (heat discomfort risk)

Example internal mapping:
PPF → chip anxiety
Ceramic → washing frustration
Wrap → durability worry
Tint → heat discomfort

Never mix with usage in same question.

------------------------------------------------------------
AXIS 2 — USAGE AXIS
------------------------------------------------------------

Purpose:
Understand exposure pattern.

Examples:
- Highway vs city
- Outdoor parking vs shaded
- Daily commute vs weekend car

Used heavily for:
- PPF
- Ceramic
- Tint

Less relevant for:
- Wrap
- Polishing

------------------------------------------------------------
AXIS 3 — PERFORMANCE AXIS
------------------------------------------------------------

Purpose:
Clarify outcome expectation.

Examples:
- “Maximum protection”
- “Long-term gloss”
- “Heat reduction priority”
- “Quick refresh”

Used for:
- All services

This axis determines ladder width in Phase 3B.

------------------------------------------------------------
AXIS 4 — INTENT AXIS
------------------------------------------------------------

Purpose:
Clarify styling vs preservation vs refresh motive.

Examples:
- Matte look
- Black roof
- Full color change
- Shine back
- Comfort upgrade

Primary for:
- Wrap
- Tint
- Polishing

------------------------------------------------------------
SERVICE → AXIS PRIORITY MAP
------------------------------------------------------------

PPF:
1) Risk
2) Usage
3) Performance

Ceramic:
1) Performance
2) Usage

Polishing:
1) Intent
2) Paint condition (inspection)

Tint:
1) Intent (comfort/privacy)
2) Performance (heat vs shade)

Wrap:
1) Intent (finish)
2) Performance (durability expectation)

Roof-Black (ROOF_PPF_BLACK_GLOSS):
Only vehicle model/year needed.
No emotional axis required.

------------------------------------------------------------
PROHIBITED BEHAVIOR
------------------------------------------------------------

- No multi-axis questions.
- No emotional stacking.
- No technical interrogation.
- No leading language.
- No selling inside qualification.
- No pricing hints.

------------------------------------------------------------
END OF ARCHITECTURE
------------------------------------------------------------

Hard constraints:
- Phase 0–2 must remain unchanged.
- Phase 3A runs only when vehicle_model + vehicle_year are already known.

PHASE LABELING RULE (LOCKED):
- Runtime `phase` MUST remain `PHASE_3` throughout Phase 3.
- Phase 3A vs 3B is represented ONLY by:
  - phase3a_required / phase3a_complete
  - price_ladder_state
- Do NOT emit phase = PHASE_3A or phase = PHASE_3B as runtime phase values.
- Emit exactly ONE qualifier per turn via:
  - phase3a_required=true
  - phase3a_qualifier_id=<PHASE3A_Q_* ID>

────────────────────────────────────────────────────────────
ROOF BLACK PPF OVERRIDE (LOCKED — REPO SAFE)
────────────────────────────────────────────────────────────
Purpose:
- If the detected SKU/intent is ROOF_PPF_BLACK_GLOSS, do NOT run standard PPF Phase 3A (coverage/driving/comparison).
- Treat as a fixed SKU styling request fulfilled via PPF.

IF detected_product_sku == ROOF_PPF_BLACK_GLOSS OR product_alias_route == ROOF_PPF_BLACK_GLOSS:
  - force service_intent = ppf
  - set active_service_context = ppf
  - set PPF_COVERAGE_INTENT = ROOF_ONLY
  - phase3a_required = true
  - phase3a_complete = true   # qualifiers are not needed beyond model/year
  - phase3a_qualifier_id = null
  - return (skip normal PPF Phase 3A chain)

PPF Phase 3A (Q1 → Q2 → conditional Q3):
Q1: PPF_COVERAGE_INTENT  → PHASE3A_Q_PPF_COVERAGE_INTENT
Q2: PPF_DRIVING_PATTERN  → PHASE3A_Q_PPF_DRIVING_PATTERN
Q3: PPF_COMPARISON_FOCUS → PHASE3A_Q_PPF_COMPARISON_FOCUS (only if triggered by price/competitor/brand fixation)

CERAMIC Phase 3A:
Q1: CERAMIC_GOAL        → PHASE3A_Q_CERAMIC_GOAL
Q2: CERAMIC_WASH_PATTERN→ PHASE3A_Q_CERAMIC_WASH_PATTERN

TINT Phase 3A:
Q1: TINT_GOAL           → PHASE3A_Q_TINT_GOAL
Q2: TINT_COVERAGE       → PHASE3A_Q_TINT_COVERAGE

WRAP Phase 3A (FULL VEHICLE ONLY — LOCKED):
Q1: WRAP_FINISH → PHASE3A_Q_WRAP_FINISH
NOTE: Do NOT ask WRAP_SCOPE. Partial/roof wrap is not offered via automation; roof-black is handled via ROOF_PPF_BLACK_GLOSS.

--------------------------------------------------------------------------
### Phase 3A qualifier selection (PPF)
# LOCK_METADATA
# LOCK_STATUS: LOCKED
# LOCK_SCOPE: PHASE 3A — qualifier selection, single-chain enforcement
# LOCK_DATE: 2026-02-09
# LOCK_REASON: Phase 3A UAT passed; prevent overwrite or multi-question regressions
# CHANGE_CONTROL: Architecture approval required

IF service_intent == PPF
AND vehicle_model is present
AND vehicle_year is present:

  - phase3a_required = true

    # Intake-to-Qualification fallback (HARD, same-message)
    # Purpose: Prevent asking Q1 when Intake already implied FULL_BODY / FULL_FRONT,
    # or when the same message clearly states it.
    # NOTE: Do NOT overwrite if already set.
    - IF (PPF_COVERAGE_INTENT is missing) OR (PPF_COVERAGE_INTENT == UNKNOWN):
      - IF current_user_message contains any of: "full", "full body", "whole car", "entire car":
        - set PPF_COVERAGE_INTENT = FULL_BODY
      - ELSE IF current_user_message contains any of: "front", "front only", "front protection", "impact zones":
        - set PPF_COVERAGE_INTENT = FULL_FRONT

    - IF (PPF_DRIVING_PATTERN is missing) OR (PPF_DRIVING_PATTERN == UNKNOWN):
      - IF current_user_message contains "highway" OR "mostly highway":
        - set PPF_DRIVING_PATTERN = HIGHWAY
      - ELSE IF current_user_message contains "city":
        - set PPF_DRIVING_PATTERN = CITY

  --------------------------------------------------------------------------
  # Phase 3A answer capture (HARD)
  #
  # Purpose:
  # - Persist the user's answer to the LAST asked PHASE3A_Q_* question into
  #   the correct normalized parameter (per PHASE3A_QUALIFICATION_DECISION_MATRIX.md).
  # - This is REQUIRED so Q1→Q2 sequencing works and we don't keep skipping Q1
  #   or falling back to legacy single-question behavior.
  #
  # Rule:
  # - If the previous assistant turn asked a PHASE3A_Q_* question,
  #   attempt normalization from the current user message.
  # - If the current user message is greeting-only / unrelated and does NOT answer:
  #   do NOT overwrite; keep the qualifier pending (nudge logic handles interruptions).

  - IF previous_turn.selected_phrase_id startswith "PHASE3A_Q_":
      - phase3a_last_qualifier_id = previous_turn.selected_phrase_id
      - attempt_normalize_phase3a_answer(phase3a_last_qualifier_id, current_user_message)

  # Normalization helper rules (strict, per Decision Matrix):
  #
  # PHASE3A_Q_PPF_COVERAGE_INTENT  -> set PPF_COVERAGE_INTENT =
  #   FULL_BODY | FULL_FRONT | PARTIAL_OR_CUSTOM | UNSURE
  #
  # PHASE3A_Q_PPF_DRIVING_PATTERN  -> set PPF_DRIVING_PATTERN =
  #   CITY | HIGHWAY | MIXED | UNKNOWN
  #
  # PHASE3A_Q_PPF_COMPARISON_FOCUS -> set PPF_COMPARISON_FOCUS =
  #   COVERAGE | FILM_QUALITY | HEADLINE_PRICE | MIXED | UNKNOWN
  #
  # NOTE: "missing" MUST treat absent/NULL the same as UNKNOWN.

    - define_missing(x):
      - return (x is missing) OR (x == UNKNOWN)

    # Phase 3A capture integrity (HARD)
    # If a value is "defaulted" upstream (commonly UNSURE) but the system has not
    # actually asked that qualifier yet, we must still ask it.
    - define_missing_ppf_coverage():
      - return (PPF_COVERAGE_INTENT is missing)
      OR (PPF_COVERAGE_INTENT == UNKNOWN)
      OR (
        PPF_COVERAGE_INTENT == UNSURE
        AND phase3a_last_qualifier_id != PHASE3A_Q_PPF_COVERAGE_INTENT
         )

  # PPF Phase 3A qualifier selection MUST be a single flat exclusive chain.
  # (Same indentation for IF / ELSE IF / ELSE IF; no nested IF that can overwrite.)

  - IF define_missing_ppf_coverage():
      - phase3a_qualifier_id = PHASE3A_Q_PPF_COVERAGE_INTENT
      - STOP

  - ELSE IF define_missing(PPF_DRIVING_PATTERN):
      - phase3a_qualifier_id = PHASE3A_Q_PPF_DRIVING_PATTERN
      - STOP

  - ELSE IF (PRICE_PRESSURE_LEVEL == HIGH) OR (COMPETITOR_QUOTE_STATUS in {MENTIONED, HAS_QUOTE_DETAILS}) OR (COMPETITOR_INFLUENCE_LEVEL == HIGH) OR (brand_fixation == true)
    AND (define_missing(PPF_COMPARISON_FOCUS)):
      - phase3a_qualifier_id = PHASE3A_Q_PPF_COMPARISON_FOCUS
      - STOP

  # If we reach here, all required qualifiers are already captured (and conditional Q3 is either not triggered or already known).
  - phase3a_required = false
  - phase3a_complete = true

--------------------------------------------------------------------------
### Phase 3A qualifier selection (CERAMIC)

IF service_intent == CERAMIC
AND vehicle_model is present
AND vehicle_year is present:

  - phase3a_required = true

  - IF previous_turn.selected_phrase_id startswith "PHASE3A_Q_":
    - phase3a_last_qualifier_id = previous_turn.selected_phrase_id
    - attempt_normalize_phase3a_answer(phase3a_last_qualifier_id, current_user_message)

  - IF define_missing(CERAMIC_GOAL):
    - phase3a_qualifier_id = PHASE3A_Q_CERAMIC_GOAL
    - STOP

  - ELSE IF define_missing(CERAMIC_WASH_PATTERN):
    - phase3a_qualifier_id = PHASE3A_Q_CERAMIC_WASH_PATTERN
    - STOP

  - phase3a_required = false
  - phase3a_complete = true

--------------------------------------------------------------------------
### Phase 3A qualifier selection (TINT)

IF service_intent == TINT
AND vehicle_model is present
AND vehicle_year is present:

  - phase3a_required = true

  - IF previous_turn.selected_phrase_id startswith "PHASE3A_Q_":
    - phase3a_last_qualifier_id = previous_turn.selected_phrase_id
    - attempt_normalize_phase3a_answer(phase3a_last_qualifier_id, current_user_message)

  - IF define_missing(TINT_GOAL):
    - phase3a_qualifier_id = PHASE3A_Q_TINT_GOAL
    - STOP

  - ELSE IF define_missing(TINT_COVERAGE):
    - phase3a_qualifier_id = PHASE3A_Q_TINT_COVERAGE
    - STOP

  - phase3a_required = false
  - phase3a_complete = true

## PHASE 3A — QUALIFIER-ID RESOLUTION (FINAL AUTHORITY — NO OVERRIDE)

Purpose:
- Prevent any legacy Phase 3A blocks (older single-question matrices) from overwriting phase3a_qualifier_id.
- This section MUST be treated as the last writer of: phase3a_required, phase3a_qualifier_id, phase3a_complete.

Hard rule:
- If this section sets phase3a_qualifier_id, nothing after it may modify it in the same turn.

FINAL OVERRIDE RULE:
IF phase3a_required == true
AND phase3a_qualifier_id is present:
  - STOP

--------------------------------------------------------------------------
## 2.X) GREETING ROUTING (HARD — Phase-agnostic, no drift)

Purpose:
- Ensure “hi/hello/السلام عليكم” does NOT get converted into BROWSING_GENERIC.
- New/unknown context → onboarding greeting (ask model+year).
- Returning/mid-flow context → treat as re-entry and continue current phase.

Definitions:
- greeting_only_message == true when the normalized message contains ONLY a greeting token.
  Examples: "hi", "hello", "hey", "السلام عليكم", "مرحبا", "هلا"
  (No service keywords, no vehicle tokens, no year, no pricing words.)

- context_exists == true when ANY of the following are present from previous turns:
  - previous_turn.active_service_context is not null
  - OR previous_turn.vehicle_model is present
  - OR previous_turn.vehicle_year is present

Rule:
IF greeting_only_message == true:
  IF context_exists == true:
    - request_type = REENTERED_CONTINUE
    - Preserve previous_turn.service_intent / active_service_context / missing_fields as-is
    - Do NOT set BROWSING_GENERIC
  ELSE:
    - request_type = GREETING_ONLY
    - qualification_state = NOT_READY
    - missing_fields = [vehicle_model, vehicle_year]
    - allowed_next_actions includes ask_missing_info
    - QUALIFICATION_STATUS = NOT_READY

Precedence:
- This rule must run BEFORE any “browsing” / “service inquiry” mapping.
- If the message includes a service keyword or pricing request, this rule must NOT trigger (not greeting-only).

- constraints: A list of detected constraints that limit downstream behavior (e.g., unknown language, ambiguous target, insufficient identifiers).
- allowed_next_actions: An ordered list of permitted downstream actions (e.g., proceed, request_minimum_context, route_to_human, hold_for_clarification).
- confidence: A bounded indicator (low/medium/high) representing certainty of the qualification classification and completeness decision (NOT likelihood of purchase or conversion).

### Orchestration Compatibility Gate (REQUIRED)

To ensure seamless wiring with orchestration (Execution Flow + Runtime State Machine),
this engine MUST also emit the following alias output:

- QUALIFICATION_STATUS

Mapping:
- If qualification_state is QUALIFIED_READY or QUALIFIED_WITH_CONSTRAINTS:
  - QUALIFICATION_STATUS = READY_FOR_NEGOTIATION
- Otherwise:
  - QUALIFICATION_STATUS = NOT_READY

Notes:
- This alias does not change qualification logic.
- It exists only to keep downstream orchestration gating stable and deterministic.

This engine does not emit customer-facing text. Outputs are strictly internal signals.

## QUALIFICATION_STATES

- QUALIFIED_READY
  - Definition: Minimum required context is present and no blocking constraints are detected.
  - Downstream Eligibility: proceed.

- QUALIFIED_WITH_CONSTRAINTS
  - Definition: Minimum required context is present, but one or more constraints are detected that limit downstream behavior.
  - Downstream Eligibility: proceed_with_constraints.

- NEEDS_MINIMUM_CONTEXT
  - Definition: Minimum required context is missing; only the smallest set of missing fields may be requested.
  - Downstream Eligibility: request_minimum_context.

- AMBIGUOUS_TARGET
  - Definition: The target of the request cannot be determined (e.g., vehicle/service/object is unclear) and prevents safe progression.
  - Downstream Eligibility: hold_for_clarification.

- UNROUTABLE_OR_UNSUPPORTED
  - Definition: The request cannot be processed by available routing paths due to unsupported content, missing channel support, or invalid format.
  - Downstream Eligibility: route_to_human or fail_safe.

- FAIL_SAFE
  - Definition: Engine cannot reliably assess qualification due to corrupted inputs, missing upstream signals, or internal inconsistency.
  - Downstream Eligibility: fail_safe.

## DECISION_RULES

### Rule Priority Order
Decisions must be evaluated in the following order, top to bottom. First match wins.

1) FAIL_SAFE
- Trigger if any of the following are true:
  - Inputs are missing or structurally invalid (no user message, null context object, corrupted payload).
  - Upstream signals required for evaluation are absent when declared mandatory by this engine.
  - Internal contradictions exist (e.g., context_completeness=true while missing_fields is non-empty).

2) UNROUTABLE_OR_UNSUPPORTED
- Trigger if the request cannot be processed through available system paths due to:
  - Unsupported channel or input format (e.g., attachments-only with no text when text is mandatory).
  - Content class outside system handling scope (as defined by routing governance).
  - Missing capability flags required to proceed.

### 2.46) SERVICE_CONFIRMED_CARRY_FORWARD (HARD)

Trigger condition:
- If the current message provides vehicle_model OR vehicle_year
- AND previous_turn.request_type == SERVICE_CONFIRMED
- AND previous_turn.service_intent != unknown
- AND the current message does NOT introduce a new service keyword (ppf/ceramic/tint/wrap/polishing)

Emit:
- request_type = VEHICLE_DETAILS_PROVIDED
- service_intent = previous_turn.service_intent
- active_service_context = previous_turn.service_intent

  2.5) SERVICE_CONFIRMED_PRIORITY (HARD)

Trigger:
- User explicitly mentions a known service keyword
  (ceramic, ppf, tint, wrap)

Behavior:
- Treat intent as SERVICE_CONFIRMED
- Do NOT downgrade to generic discovery
- Enforce minimum vehicle context first
- Set active_service_context = service_intent

If minimum vehicle context is missing:
- Set qualification_state = NOT_READY
- Populate missing_fields with:
  - vehicle_model
  - vehicle_year
- Set allowed_next_actions to include:
  - ask_missing_info
- Set QUALIFICATION_STATUS = NOT_READY

Restrictions:
- Do NOT ask preference questions
- Do NOT proceed to pricing or negotiation

3) AMBIGUOUS_TARGET
- Trigger if the system cannot identify the minimum target needed to proceed safely, including:
  - No discernible vehicle/object/entity reference when downstream requires one.
  - Conflicting targets in the same request without a dominant target signal.

4) NEEDS_MINIMUM_CONTEXT
- Trigger if minimum required context keys are missing and must be requested before proceeding.
- missing_fields must contain only the minimum set required to unlock routing progression.

5) QUALIFIED_WITH_CONSTRAINTS
- Trigger if minimum required context is present but constraints exist that limit downstream behavior, such as:
  - Unknown or mixed language with low confidence.
  - Uncertain user role or intent ambiguity that does not block safe progression.
  - Conflicting non-blocking metadata (e.g., multiple possible locations) requiring cautious handling.

6) QUALIFIED_READY
- Trigger if minimum required context is present and no blocking or limiting constraints exist.

### Output Consistency Rules
- qualification_state must be exactly one state from QUALIFICATION_STATES.
- context_completeness is true only when missing_fields is empty.
- missing_fields must be ordered by impact (most blocking first) and contain no duplicates.
- constraints must be explicit, human-readable internal labels (no customer-facing phrasing).
- allowed_next_actions must align with qualification_state eligibility definitions.
- confidence must be low/medium/high and must not be "high" when AMBIGUOUS_TARGET, NEEDS_MINIMUM_CONTEXT, UNROUTABLE_OR_UNSUPPORTED, or FAIL_SAFE is selected.

## QUESTION_MINIMIZATION_LOGIC

The engine must minimize clarification requests by applying the following rules:

1) Use existing context first
- If any required field can be derived directly from already-provided user text or upstream metadata, do not ask for it.

NEWNESS SHORT-CIRCUIT (HARD)
- If user clearly signals the car is brand new / new delivery / from showroom (e.g., “brand new”, “new car”, “just bought”, “from dealership”, “0 km”):
  - Treat vehicle_year as satisfied for qualification gating (do not ask “what year?”).
  - Keep vehicle_model as required if not provided.
  - Add constraint: vehicle_year_inferred = NEW (not a numeric year).
  - missing_fields must NOT include vehicle_year in this case.

  MISSING-INFO ASK COUNT (HARD)
- If missing_fields set is unchanged since the last assistant turn and allowed_next_actions still includes ask_missing_info:
  - Increment missing_info_ask_count by 1 (cap at 3).
- Otherwise:
  - Set missing_info_ask_count = 1.

2) Ask only when blocking
- Only request information when the current qualification_state would otherwise be AMBIGUOUS_TARGET or NEEDS_MINIMUM_CONTEXT.

3) Ask the smallest set
- missing_fields must include only the minimum set of keys required to move from a blocking state to a proceed-eligible state.

4) One-turn maximum by default
- Default behavior is to request all minimum missing fields in a single step rather than multi-turn back-and-forth.

5) Preserve user effort
- Do not ask questions the user has already answered earlier in the session unless the value is explicitly conflicting or invalid.

6) Avoid intent questions
- Do not ask what service the user wants unless downstream routing cannot proceed without it and no other safe target exists.

7) Prioritize identifiers over preferences
- If both are missing, request hard identifiers first (e.g., entity/vehicle reference) before optional preferences.

8) Stop asking when constrained
- If constraints indicate low-confidence comprehension (e.g., unknown language, heavily ambiguous text), prefer route_to_human or hold_for_clarification over repeated questioning.

## ASSUMPTION_GUARDS

The engine must enforce the following guards to prevent assumption-based progression:

1) No implicit intent inference  
- Do not infer urgency, purchase readiness, or likelihood of purchase/conversion.
- Coarse classification is allowed only for routing safety (e.g., non-customer contact, off-scope request, service-adjacent issue), and must not be treated as permission to recommend or redirect in customer-facing language.

2) No default target assignment  
- Do not assume a vehicle, service, product, or object when multiple interpretations are possible or when no explicit reference exists.

3) No silent context filling  
- Do not populate missing required fields using defaults, heuristics, or historical assumptions.

4) No preference extrapolation  
- Do not infer preferences (e.g., premium vs basic, speed vs quality) from partial or unrelated signals.

5) Conflict blocks certainty  
- When conflicting signals exist, reduce confidence and apply constraint handling rather than selecting a dominant interpretation.

6) Explicit override only  
- Any override of ambiguity or incompleteness must be driven by explicit upstream signals, not engine-local judgment.

7) Fail toward safety  
- When uncertainty cannot be resolved without assumptions, prefer NEEDS_MINIMUM_CONTEXT, AMBIGUOUS_TARGET, or FAIL_SAFE over QUALIFIED_READY.

## CONTEXT_INHERITANCE_RULES

The engine must enforce the following rules governing context propagation to downstream engines:

1) Explicit pass-through only  
- Only context elements explicitly validated or marked as safe by this engine may be inherited downstream.

2) Freeze qualified context  
- Once a context element is validated and contributes to qualification_state, it must not be reinterpreted or mutated by downstream engines unless explicitly overridden by new user input.

3) Block unqualified fields  
- Context elements associated with missing_fields, ambiguity, or unresolved constraints must not be treated as confirmed downstream.

4) Constraint-aware inheritance  
- When qualification_state includes constraints, downstream engines must receive both the validated context and the active constraints together.

5) No retroactive inference  
- Downstream engines must not infer or backfill missing context based on later assumptions or response logic.

6) Session continuity  
- Validated context may persist across turns within the same session unless contradicted or invalidated by new input.

7) Fail-safe isolation  
- When qualification_state is FAIL_SAFE, no context is inherited beyond minimal session metadata required for recovery or human escalation.

## ENGINE_SEQUENCE_POSITION

This engine executes after initial input normalization and routing pre-processing, and before any tone selection, sales logic, or response generation engines.

Execution guarantees:
- Must run before any customer-facing content is produced.
- Must complete before downstream routing decisions are finalized.
- Must block progression to response engines until qualification_state is resolved.

Upstream requirements:
- Normalized user input
- Session metadata
- Language detection and basic routing signals (if available)

Downstream gating:
- Only engines permitted by allowed_next_actions may execute next.
- Engines that depend on validated context must not run when qualification_state is NEEDS_MINIMUM_CONTEXT, AMBIGUOUS_TARGET, UNROUTABLE_OR_UNSUPPORTED, or FAIL_SAFE.


## FAILURE_HANDLING

The engine must apply the following failure-handling rules:

1) Internal evaluation failure  
- If the engine cannot complete evaluation due to missing mandatory inputs, structural corruption, or logical inconsistency, qualification_state must be set to FAIL_SAFE.

2) Signal integrity failure  
- If required upstream signals are malformed, contradictory, or incomplete beyond safe recovery, processing must halt and transition to FAIL_SAFE.

3) Partial evaluation prevention  
- The engine must not emit partial or speculative outputs when failure conditions are detected.

4) Deterministic fallback  
- All failures must resolve to a known, deterministic state with explicit allowed_next_actions.

5) Safe downstream isolation  
- When in FAIL_SAFE, downstream engines must not receive inferred or unvalidated context.

6) Escalation readiness  
- Failure output must preserve minimal metadata required for recovery handling or human escalation.

## EDGE_CASE_HANDLING

The engine must handle the following edge cases deterministically:

1) Mixed-language or code-switched input  
- If language detection is uncertain but content remains interpretable, set QUALIFIED_WITH_CONSTRAINTS and add constraint: language_uncertain.

2) Ultra-short messages  
- If the message is too short to identify a safe target (e.g., single word, emoji, generic “price?”), set AMBIGUOUS_TARGET or NEEDS_MINIMUM_CONTEXT based on whether any target tokens exist.

3) Multi-intent messages  
- If multiple requests exist, prefer the primary request if a dominant target signal is present; otherwise set AMBIGUOUS_TARGET with constraint: multiple_targets.

4) Conflicting session context  
- If prior session context conflicts with the latest user message, prefer the latest explicit user input and add constraint: context_conflict.

5) Attachment-heavy inputs  
- If attachments exist but text is sufficient for qualification, proceed normally.
- If qualification depends on attachment content that is not available as parsed text, set NEEDS_MINIMUM_CONTEXT with constraint: attachment_unreadable.

6) Repeated clarification loops  
- If the same minimum missing_fields have been requested previously without resolution, set UNROUTABLE_OR_UNSUPPORTED with constraint: clarification_loop and allow escalation.

7) Non-actionable or empty content  
- If content is empty, purely noise, or not actionable, set UNROUTABLE_OR_UNSUPPORTED with constraint: non_actionable_input.

## DEPENDENCIES

### Governance (Must Comply)
- 2-Doctrine - Core decision logic/ARCHITECTURE_INTEGRITY_CHECKLIST.md

### Upstream Dependencies (Required Inputs / Contracts)
- 4-Ops - Execution Support/CHAT_CONTEXT_RESUME_RULE_v1.0.txt
- 4-Ops - Execution Support/ARCHITECTURE_SEQUENCE_CONTRACT.md.txt
- 2-Doctrine - Core decision logic/FILE — LANGUAGE_OUTPUT_DISCIPLINE_GUARD_v1.0.txt

### Downstream Consumers (Uses This Engine Output)
- 4-Ops - Execution Support/ARCHITECTURE_SEQUENCE_CONTRACT.md.txt
- 3-Engines/FILE 4 — PRICING_ENGINE_v1_LOCKED.txt
- 3-Engines/FILE 5 — VISUAL_SHARING_RULES_v1_LOCKED.txt
- 3-Engines/FILE 6 — SILENCE_RECOVERY_RULE_v1_LOCKED.txt
- 3-Engines/FILE 7 — SALES_HANDOVER_RULE_v1_LOCKED.txt
- 3-Engines/FILE 8 — SHADOW_MODE_OPERATING_CONTRACT_v1_LOCKED.txt

### Known Adjacent / Potential Overlap (Drift Watch)
- 3-Engines/FILE 3 — QUALIFICATION_ENGINE_v4_LOCKED.txt
  - Note: Ensure only one Qualification Engine is runtime-loaded. This file is legacy/archived.

### Placeholders (NOT YET CREATED — Do Not Load Until Built)
- 3-Engines/ROUTING_ORCHESTRATION_ENGINE.md (PLACEHOLDER)
- 3-Engines/INPUT_NORMALIZATION_ENGINE.md (PLACEHOLDER)
- 3-Engines/LANGUAGE_DETECTION_ENGINE.md (PLACEHOLDER)
- 3-Engines/RESPONSE_COMPOSER_ENGINE.md (PLACEHOLDER)
- 3-Engines/TONE_ENGINE.md (PLACEHOLDER)

### External Calls
- None. This engine performs no external lookups and does not call external services.

## INTEGRITY_CONSTRAINTS

The following constraints are mandatory and enforce architectural compliance:

1) Checklist compliance lock  
- This engine must remain compliant with ARCHITECTURE_INTEGRITY_CHECKLIST.md at all times.

2) Logic-only enforcement  
- No customer-facing language, examples, pricing logic, or tone decisions may exist in this file.

3) Determinism requirement  
- Given the same inputs, the engine must always produce the same outputs.

4) Single-state resolution  
- Exactly one qualification_state must be emitted per execution cycle.

5) No cross-engine mutation  
- This engine must not modify, override, or reinterpret outputs from other engines outside its declared scope.

6) No hidden side effects  
- The engine must not trigger downstream behavior implicitly; all downstream actions must be driven only by explicit outputs.

7) Section isolation  
- Each section in this file has a single responsibility and must not duplicate logic from other sections.

8) Drift prevention  
- Any change to this file requires explicit architecture approval and version increment.

## VERSION_CONTROL

- Current Version: 1.0.1
- Status: Frozen
- Last Updated: 2026-01-01
- Change Authority: Architecture Control Mode Only
- Lock Note: 3-Engines/QUALIFICATION_ENGINE_LOCK_NOTE.md
- Version note: Added orchestration compatibility gate QUALIFICATION_STATUS

Versioning rules:
- Any functional change requires a minor or major version increment.
- Any structural or wording change requires a patch version increment.
- All changes must be reviewed against ARCHITECTURE_INTEGRITY_CHECKLIST.md before approval.
- Deprecated behavior must not be removed without an explicit replacement and migration note.