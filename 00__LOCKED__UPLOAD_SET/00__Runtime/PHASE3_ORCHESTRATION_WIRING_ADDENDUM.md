# PHASE 3 — WIRING ADDENDUM (Silence ↔ Follow-Up ↔ PIM) — v1.0

## A.2) PHASE 3A GATE QUESTION SELECTION (PPF ONLY — BINDING)

Rule:
- When Phase 3A returns missing_details[], the orchestrator MUST ask exactly ONE missing detail question.

Priority (top wins):
1) If "paint_condition" is present in missing_details[]:
	- Ask paint condition (old-vehicle override)
	- Do NOT ask usage exposure in the same turn
2) Else if "ppf_usage_exposure" is present in missing_details[]:
	- Ask usage exposure (city / highway / desert / mixed)

This does NOT change any Phase 3B SKU logic.
It only ensures the right gate question is asked.

## A) STATE OWNERSHIP (single source of truth)
OWNED BY ORCHESTRATOR (write authority):
- LAST_COUNTED_OUTBOUND_TIMESTAMP
- LAST_CUSTOMER_SIGNAL_TIMESTAMP
- FOLLOW_UP_COUNT
- INPUT_MODE (LIVE | BACKFILL_BATCH)
- SILENCE_SUPPRESSED (bool) + SILENCE_SUPPRESSION_REASON (enum)
- CONVERSATION_STATUS (OPEN/CLOSED/DISQUALIFIED)
- AGENT_TAKEOVER_FLAG

OWNED BY SILENCE_ENGINE (write authority):
- SILENCE_STAGE (NONE|S1|S2|S3)
- SILENCE_ACTIVE (bool)
- ALLOW_ACTION (bool)
- EXIT_FLAG (bool)

## A.1) PHASE 3 CANONICAL KEYS + MAPPING LAYER (LOCKED)

Purpose:
- Prevent cross-engine key mismatches (case/spelling) from breaking routing.
- Engines may emit their native keys, but the ORCHESTRATOR must normalize into canonical keys.

Non-negotiable rules:
- Do NOT rename keys inside locked engines to “make it match”.
- The ORCHESTRATOR performs normalization once, immediately after reading engine outputs.
- After normalization, ONLY canonical keys are used for routing/state decisions.

### Canonical keys (Phase 3)
Canonical keys use SHOUT_CASE for cross-file consistency:

- QUALIFICATION_STATUS
- NEGOTIATION_STATE
- PRICE_LADDER_STATE
- OBJECTION_SIGNAL

Phase 3A gate keys (canonical):
- PHASE3A_SCOPE
- PHASE3A_READY_PPF
- PPF_COVERAGE_SELECTED
- PPF_BRAND_INTENT
- PPF_WARRANTY_INTENT
- MISSING_DETAILS

Note:
- Phase 3A gate keys are tag-only control signals. They do not contain pricing.

Control flags (canonical):
- QUOTE_REQUIRED_FLAG
- AUTOMATION_ALLOWED_FLAG

Analytics / safety counters (canonical):
- OBJECTION_REPEAT_COUNT
- CUSTOMER_RESPONSE_LATENCY

### Engine → Canonical mappings (single source of truth)
Apply these mappings immediately after reading outputs:

Objection Resolution Engine (native → canonical):
- qualification_status        → QUALIFICATION_STATUS
- negotiation_state           → NEGOTIATION_STATE
- price_ladder_state          → PRICE_LADDER_STATE
- objection_signal            → OBJECTION_SIGNAL
- quote_required              → QUOTE_REQUIRED_FLAG
- automation_allowed          → AUTOMATION_ALLOWED_FLAG
- objection_repeat_count      → OBJECTION_REPEAT_COUNT
- customer_response_latency   → CUSTOMER_RESPONSE_LATENCY

Price Ladder Engine (already canonical / no-op):
- QUALIFICATION_STATUS        → QUALIFICATION_STATUS
- NEGOTIATION_STATE           → NEGOTIATION_STATE
- PRICE_LADDER_STATE          → PRICE_LADDER_STATE
- QUOTE_REQUIRED_FLAG         → QUOTE_REQUIRED_FLAG

Negotiation Logic Module (native → canonical):
- qualification_status        → QUALIFICATION_STATUS
- negotiation_state           → NEGOTIATION_STATE
- missing_details             → MISSING_DETAILS
- PHASE3A_SCOPE               → PHASE3A_SCOPE
- PHASE3A_READY_PPF           → PHASE3A_READY_PPF
- PPF_COVERAGE_SELECTED       → PPF_COVERAGE_SELECTED
- PPF_BRAND_INTENT            → PPF_BRAND_INTENT
- PPF_WARRANTY_INTENT         → PPF_WARRANTY_INTENT

Normalization rule:
- If missing_details and MISSING_DETAILS both exist, MISSING_DETAILS wins.

Objection Resolution Engine (native → canonical):
- qualification_status        -> QUALIFICATION_STATUS
- negotiation_state           -> NEGOTIATION_STATE
- price_ladder_state          -> PRICE_LADDER_STATE
- objection_signal            -> OBJECTION_SIGNAL
- quote_required              -> QUOTE_REQUIRED_FLAG
- automation_allowed          -> AUTOMATION_ALLOWED_FLAG

Silence Handling Engine (separate domain; no quote flag required):
- SILENCE_STAGE / SILENCE_ACTIVE / ALLOW_ACTION / EXIT_FLAG remain as-is in this file.

### Normalization precedence rule
If both native + canonical versions exist at the same time:
- Canonical wins.
- Native is ignored after mapping.

STATUS: LOCKED
LOCK_REASON:
- Prevents hidden cross-file bugs due to key naming mismatch
- Avoids modifying locked engines (Phase 3 engines remain untouched)

## A.2) PHASE 3A GATE ENFORCEMENT (PPF ONLY — BINDING)

Purpose:
Prevent price ladder execution for PPF unless minimum PPF qualifiers are present.

Binding rule:
- If SERVICE_INTEREST_PPF is present AND PHASE3A_READY_PPF != true:
	- The orchestrator MUST NOT call PRICE_LADDER_ENGINE for PPF.
	- Control must return to clarification using MISSING_DETAILS (or missing_details).

Clarification contract:
- Ask ONLY ONE clarifier per message (Phase 0–2 / Phase 3 constraints still apply).
- Use MISSING_DETAILS to choose the single most important missing item.

Recommended missing_details priority (PPF):
1) vehicle_model_year
2) ppf_usage_exposure
3) ppf_coverage_front_vs_full (ONLY if customer explicitly asked for front/full scope)

Old vehicle priority override (PPF, 7+ years):
- If vehicle age >= 7 years:
	- paint_condition MUST be asked before ppf_usage_exposure
	- ppf_usage_exposure becomes OPTIONAL (must not block ladder)
	- Do NOT loop questions if refused

Binding orchestration rule:
- If SERVICE_INTEREST_PPF is present AND vehicle age >= 7 years:
	- missing_details priority becomes:
		1) paint_condition
		2) (optional) ppf_usage_exposure
		3) ppf_scope only if explicitly requested

Notes:
- This is a gating rule only. It does NOT change the customer’s chosen service.
- Brand/warranty intent may be captured but must not block ladder if scope is confirmed.

## B) CUSTOMER SIGNAL GATE (non-negotiable)
Update LAST_CUSTOMER_SIGNAL_TIMESTAMP ONLY when:
- new customer message OR
- new screenshot that contains customer message OR
- call/visit/audio note summary that confirms customer interaction

Do NOT update timestamps for:
- re-pasted old transcript
- internal drafting / translation / “should we follow up?”
- assistant-only notes without new customer interaction

## C) CALL TRIGGERS
Call SILENCE_ENGINE when:
1) runtime_tick
2) outbound_sent AND outbound_is_counted == TRUE
3) inbound_customer_signal (for reset evaluation)

## D) HARD BLOCKERS (must be checked before calling)
If any is true → do not allow silence actions:
- CONVERSATION_STATUS != OPEN
- AGENT_TAKEOVER_FLAG == TRUE
- INPUT_MODE == BACKFILL_BATCH
- SILENCE_SUPPRESSED == TRUE
- NEGOTIATION_ACTIVE == TRUE
- VISIT_SCHEDULING_ACTIVE == TRUE

## E) FOLLOW-UP ENGINE PRECEDENCE (must not conflict)
FOLLOW_UP_ENGINE may run ONLY IF:
- explicit_followup_request == TRUE
- AND silence_active == FALSE
- AND silence_window != S3_LONG
(aligns with Follow-Up engine blockers)