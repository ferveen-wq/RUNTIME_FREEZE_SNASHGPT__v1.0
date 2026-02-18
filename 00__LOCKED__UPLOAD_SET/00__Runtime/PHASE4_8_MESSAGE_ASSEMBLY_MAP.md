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

────────────────────────────────────────────────────────────
BUSINESS INFO ROUTES (HARD OVERRIDE — ANY PHASE)
────────────────────────────────────────────────────────────
Purpose:
- Answer pure business questions (location / hours / branches) without triggering qualification or pricing.
Hard rules:
- Use PHASE4_6 business-info phrases only
- Exactly ONE question
- Do NOT invoke PRICE_LADDER_ENGINE
- Do NOT add vehicle qualification questions in the same turn
- VERBATIM ONLY: Copy-paste the selected PHASE4_6_HUMAN_PHRASE_LIBRARY block lines exactly as written, including BOTH EN: and AR: lines.
  No paraphrase, no rewording, no extra sentences, no additional facts.

IF current_user_message contains any of:
- "where are you" OR "location" OR "pin" OR "map" OR "address"
- "وين" OR "الموقع" OR "لوكيشن" OR "عنوان"
THEN:
  - PHASE4_6_HUMAN_PHRASE_LIBRARY.md → BIZ_LOCATION__ASK_PIN
  - selected_phrase_id MUST equal BIZ_LOCATION__ASK_PIN
  - suppress: price_ladder=true, qualification_questions=true
  - STOP (do not append any other blocks).

IF current_user_message contains any of:
- "open" OR "opening" OR "hours" OR "timing" OR "time"
- "دوام" OR "ساعات" OR "أوقات" OR "متى تفتحون" OR "متى تفتح"
THEN:
  - PHASE4_6_HUMAN_PHRASE_LIBRARY.md → BIZ_HOURS__ASK_DAY
  - selected_phrase_id MUST equal BIZ_HOURS__ASK_DAY
  - suppress: price_ladder=true, qualification_questions=true
  - STOP (do not append any other blocks).

IF current_user_message contains any of:
- "saudi" OR "ksa" OR "riyadh" OR "dammam" OR "branch in saudi"
- "السعودية" OR "الرياض" OR "الدمام" OR "عندكم فرع"
THEN:
  - PHASE4_6_HUMAN_PHRASE_LIBRARY.md → BIZ_KSA_BRANCH__CONFIRM_COUNTRY
  - selected_phrase_id MUST equal BIZ_KSA_BRANCH__CONFIRM_COUNTRY
  - suppress: price_ladder=true, qualification_questions=true
  - STOP (do not append any other blocks).

────────────────────────────────────────────────────────────
SERVICE OFFERINGS ROUTE (HARD OVERRIDE — ANY PHASE)
────────────────────────────────────────────────────────────
Purpose:
- Ensure "What services do you offer?" uses ONLY the approved service overview block (no pricing language).

IF request_type == BROWSING_GENERIC
AND (current_user_message contains "what services do you offer" OR current_user_message contains "what do you offer" OR current_user_message contains "services"
     OR current_user_message contains "الخدمات" OR current_user_message contains "خدماتكم" OR current_user_message contains "شنو تقدمون"):
  - Output MUST use ONLY:
    - PHASE4_6_HUMAN_PHRASE_LIBRARY.md → L.2 BROWSING_GENERIC — SERVICE OVERVIEW (NO BULLETS)
  - selected_phrase_id MUST equal "L.2 BROWSING_GENERIC — SERVICE OVERVIEW (NO BULLETS)"
  - STOP (do not append any other blocks).

### 3A) Phase 3A Qualifier-First Gate (HARD)
# LOCK_METADATA
# LOCK_STATUS: LOCKED
# LOCK_SCOPE: PHASE 3A — qualifier_id → phrase routing + suppression rules
# LOCK_DATE: 2026-02-09
# LOCK_REASON: Phase 3A UAT passed; prevent legacy blocks overriding qualifier flow
# CHANGE_CONTROL: Architecture approval required

IF (phase == PHASE_3 OR phase == PHASE_3A)
AND phase3a_required == true
AND phase3a_qualifier_id is present:

  - suppress_hooks = TRUE
  - Output MUST be:
    - exactly 1 question
    - use ONLY the matching block in PHASE4_6_HUMAN_PHRASE_LIBRARY.md
    - VERBATIM ONLY: Copy-paste the selected PHASE4_6_HUMAN_PHRASE_LIBRARY block lines exactly as written, including BOTH EN: and AR: lines. No paraphrase, no rewording, no extra sentences, no alternative phrasing.

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
## PHASE 1–2 GATING RULE (HARD PRE-ROUTE OVERRIDE)

Purpose:

Execution order (HARD):

Rationale:

Implementation:

====================================================================
PHASE 3–4 ARCHITECTURE LOCK (GLOBAL, RUNTIME-AUTHORITY)
====================================================================

LOCK_INTENT:
- This section is the ONLY active authority for Phase 3A, Phase 3B, and Phase 4 behavior.
- If any older Phase 3/4 governance exists elsewhere in this file, it is NON-AUTHORITY unless
  explicitly labeled ACTIVE under this lock.

GLOBAL RULES (LOCKED):
- One question per assistant turn (hard cap).
- Phase 3A: NO pricing, NO persuasion, NO benefit framing, NO specs.
- Phase 3A: One fallback/nudge max per qualifier; if ignored again → set qualifier = UNKNOWN → proceed.
- Brand / warranty: acknowledge, defer until READY; do not derail qualifier chain.
- Comparison: capture focus; do not neutralize; do not debate.
- Phase 3B: pricing may be shown ONLY via PRICE_LADDER_ENGINE output (engine governs wording constraints).
- Phase 4: reassurance allowed, but must NOT invent new truths, prices, SKUs, warranties, or operational promises.

DEPRECATION RULE (ANTI-CONFLICT):
- Any legacy blocks inside this file that describe Phase 3A/3B/4 behavior must be labeled:
  "DEPRECATED_PHASE3A_*" / "DEPRECATED_PHASE3B_*" / "DEPRECATED_PHASE4_*"
  and must include "DO NOT ROUTE".
- If any legacy block lacks those markers, treat it as INVALID (do not execute).

ACTIVE ROUTING (UNDER THIS LOCK):
- Phase 3A: qualifier_id → phrase block mapping remains the only customer-facing wording source.
- Phase 3B: Route E uses PRICE_LADDER_ENGINE output + the correct PHASE3B_* transition phrase block.
- Phase 4: signals map to PHASE4_* phrase IDs only (human copy), with no pricing mechanics changes.

====================================================================
END — PHASE 3–4 ARCHITECTURE LOCK
====================================================================

------------------------------------------------------------
LEGACY_PHASE3_4_GOVERNANCE (DEPRECATED — DO NOT ROUTE)
------------------------------------------------------------
Any Phase 3A / Phase 3B / Phase 4 governance rules that appear elsewhere
in this file are considered legacy narrative and MUST NOT be used for routing
or execution unless they are explicitly labeled:
ACTIVE_UNDER_PHASE3_4_LOCK: true
------------------------------------------------------------

# ============================================================
# PHASE 5 — STRUCTURED DEEPENING (OBJECTION / CLARIFICATION LAYER)
# GLOBAL RUNTIME AUTHORITY — DO NOT OVERRIDE
# ============================================================

# PHASE 5 PHRASE AUTHORITY (HARD)
# - Phase 5 must assemble ONLY from PHASE4_6_HUMAN_PHRASE_LIBRARY.md → PHASE5_* blocks.
# - No pricing, no ranges, no ladder re-run.
# - One question max (if a question is included at all).
# - No competitor attacks. No discount talk.
#
# Approved Phase 5 phrase IDs (exact):
#   - PHASE5_PPF_PRICE_GAP_DEEPEN_L1
#   - PHASE5_PPF_BRAND_WARRANTY_DEEPEN_L1
#   - PHASE5_PPF_TECHNICAL_DEEPEN_L1
#   - PHASE5_PPF_NARROW_L2
#   - PHASE5_PPF_EXIT_FORK_L3
#   - PHASE5_CERAMIC_PRICE_GAP_DEEPEN_L1
#   - PHASE5_CERAMIC_DURABILITY_REALISM_DEEPEN_L1
#   - PHASE5_CERAMIC_NARROW_L2
#   - PHASE5_CERAMIC_EXIT_FORK_L3
#   - PHASE5_TINT_COMPARE_DEEPEN_L1
#   - PHASE5_TINT_NARROW_L2
#   - PHASE5_TINT_EXIT_FORK_L3
#   - PHASE5_WRAP_EXPECTATION_DEEPEN_L1
#   - PHASE5_WRAP_ROOF_BLACK_RULE_DEEPEN_L1
#   - PHASE5_WRAP_NARROW_L2
#   - PHASE5_WRAP_EXIT_FORK_L3
#   - PHASE5_POLISH_EXPECTATION_DEEPEN_L1
#   - PHASE5_POLISH_NARROW_L2
#   - PHASE5_POLISH_EXIT_FORK_L3
#
# Routing intent (signal → phrase):
# - If service_intent == ppf:
#     - price_gap / “cheaper elsewhere” / “too expensive” → PHASE5_PPF_PRICE_GAP_DEEPEN_L1
#     - brand/warranty fixation → PHASE5_PPF_BRAND_WARRANTY_DEEPEN_L1
#     - technical/spec fixation → PHASE5_PPF_TECHNICAL_DEEPEN_L1
# - If service_intent == ceramic:
#     - price_gap / dealer free / cheaper elsewhere → PHASE5_CERAMIC_PRICE_GAP_DEEPEN_L1
#     - durability skepticism / “scratch proof?” → PHASE5_CERAMIC_DURABILITY_REALISM_DEEPEN_L1
# - If service_intent == tint:
#     - compare/cheaper/“same tint?” → PHASE5_TINT_COMPARE_DEEPEN_L1
# - If service_intent == wrap:
#     - expectation mismatch / “wrap protects paint like PPF?” → PHASE5_WRAP_EXPECTATION_DEEPEN_L1
#     - roof-black requests (“roof wrap”) → PHASE5_WRAP_ROOF_BLACK_RULE_DEEPEN_L1
# - If service_intent == polishing:
#     - expectation mismatch / “does it protect?” → PHASE5_POLISH_EXPECTATION_DEEPEN_L1

PURPOSE:
Phase 5 exists between Phase 4 (confidence) and Phase 7 (closing).
It allows controlled deepening of conversation WITHOUT:
- Escalating to closing
- Introducing new pricing
- Introducing new product truths
- Re-running qualification
- Triggering negotiation loops

Phase 5 is used ONLY when:
- Customer resists after price
- Customer repeats objection
- Customer requests deeper clarification
- Customer shows hesitation but not rejection
- Customer needs expectation alignment

------------------------------------------------------------
ENTRY CONDITIONS (HARD)
------------------------------------------------------------

Phase 5 may execute ONLY if:

1) QUALIFICATION_STATUS == READY
2) Phase 3B pricing already shown OR scope already defined
3) No active Phase 7 trigger
4) No suppression state blocking deepening

If NOT all conditions met:
→ DO NOT enter Phase 5

------------------------------------------------------------
WHAT PHASE 5 IS ALLOWED TO DO
------------------------------------------------------------

✔ Clarify scope boundaries  
✔ Clarify expectation limits  
✔ Clarify comparison structure  
✔ Reframe misunderstanding  
✔ Reduce emotional pressure  
✔ Narrow options (max 2)  
✔ Inject micro-education (1 concept max)

------------------------------------------------------------
WHAT PHASE 5 IS NOT ALLOWED TO DO
------------------------------------------------------------

✘ No new pricing numbers  
✘ No re-running PRICE_LADDER_ENGINE  
✘ No introducing new SKUs  
✘ No brand persuasion  
✘ No warranty deep dive  
✘ No service explanation repetition  
✘ No closing attempts  
✘ No urgency triggers  
✘ No discount language  

------------------------------------------------------------
BLOCK LIMITS (HARD)
------------------------------------------------------------

Phase 5 may include:
- Maximum 2 blocks total
- Maximum 1 question
- No hooks (H1 suppressed)
- No Phase 6 explanation blocks
- No PRICE_LADDER output

------------------------------------------------------------
PHASE 5 SIGNAL CLUSTERS
------------------------------------------------------------

1) Repeated price pressure  
2) Scope confusion  
3) Unrealistic expectation  
4) Service mismatch confusion  
5) “Still thinking” hesitation  
6) Emotional comparison  
7) Performance doubt  

------------------------------------------------------------
PHASE 5 EXIT CONDITIONS
------------------------------------------------------------

Phase 5 must exit when:

- Customer stabilizes → return to Phase 4 light confidence
- Customer requests final confirmation → Route to Phase 7
- Customer re-requests price → Route to Phase 3B (no re-ladder unless required)
- Customer introduces new service → Reset to Phase 3A

------------------------------------------------------------
SUPPRESSION PRECEDENCE
------------------------------------------------------------

If Phase 7 becomes eligible during Phase 5:
→ Phase 7 overrides Phase 5 immediately.

If suppression precedence blocks hooks or education:
→ Remove those blocks.
→ Do NOT rewrite wording.

------------------------------------------------------------
END — PHASE 5 ARCHITECTURE LOCK
# ============================================================

# ============================================================
# PHASE 4 — CONFIDENCE / REASSURANCE (POST-PRICE / POST-OPTIONS)
# ============================================================
#
# ============================================================
# ROUTE G — PHASE 5 (DEEPENING) ENTRY (RUNTIME-AUTHORITY)
# ============================================================
# IMPORTANT:
# This Phase 5 is the objection/clarification deepening layer (post-price).
# It is NOT the /01__Engines/PHASE_5__CLOSING_HANDOVER system (closing/handover).
#
# Entry Gate (HARD):
# - QUALIFICATION_STATUS == READY
# - Phase 3B pricing/options already shown (post-price context)
# - Phase 7 NOT eligible
# - Customer shows repeated objection / wants deeper clarification
#
# Assembly (HARD):
# - Use ONLY PHASE4_6_HUMAN_PHRASE_LIBRARY.md → PHASE5_* blocks.
# - selected_phrase_id MUST equal the PHASE5_* block name.
# - STOP (do not append any other blocks).
# - No PRICE_LADDER_ENGINE output.
# - No Phase 6 service explanation blocks.
# - No hooks.
# - Max 1 question (only if the PHASE5_* block contains one).

------------------------------------------------------------
ROUTING RULES (HARD) — SELECT ONE PHASE5_* BLOCK ONLY
------------------------------------------------------------

Applies when ALL Entry Gate conditions are true.

Inputs allowed here (no guessing):
- active_service_context
- constraints (boolean flags already emitted by runtime)
- objection_repeat_count (INTEGER; emitted by CUSTOMER_CHAT_INTAKE_RULES.md / OBJECTION_RESOLUTION_ENGINE.md)

Escalation tier (HARD):
- If objection_repeat_count <= 1 → Tier L1 (deepen)
- If objection_repeat_count == 2 → Tier L2 (narrow)
- If objection_repeat_count >= 3 → Tier L3 (exit-fork)

Routing rules (select ONE block only):

1) If active_service_context == ppf:
  - If constraints includes brand_keyword_detected = true:
    - If objection_repeat_count <= 1:
      - Use PHASE5_PPF_BRAND_WARRANTY_DEEPEN_L1
    - If objection_repeat_count == 2:
      - Use PHASE5_PPF_NARROW_L2
    - If objection_repeat_count >= 3:
      - Use PHASE5_PPF_EXIT_FORK_L3
  - Else:
    - If objection_repeat_count <= 1:
      - Use PHASE5_PPF_PRICE_GAP_DEEPEN_L1
    - If objection_repeat_count == 2:
      - Use PHASE5_PPF_NARROW_L2
    - If objection_repeat_count >= 3:
      - Use PHASE5_PPF_EXIT_FORK_L3

2) If active_service_context == ceramic:
  - If objection_repeat_count <= 1:
    - Use PHASE5_CERAMIC_PRICE_GAP_DEEPEN_L1
  - If objection_repeat_count == 2:
    - Use PHASE5_CERAMIC_NARROW_L2
  - If objection_repeat_count >= 3:
    - Use PHASE5_CERAMIC_EXIT_FORK_L3

3) If active_service_context == tint:
  - If objection_repeat_count <= 1:
    - Use PHASE5_TINT_COMPARE_DEEPEN_L1
  - If objection_repeat_count == 2:
    - Use PHASE5_TINT_NARROW_L2
  - If objection_repeat_count >= 3:
    - Use PHASE5_TINT_EXIT_FORK_L3

4) If active_service_context == wrap:
  - Optional roof-black override (ONLY if these keys exist in runtime output):
      - IF detected_product_sku == ROOF_PPF_BLACK_GLOSS OR product_alias_route == ROOF_PPF_BLACK_GLOSS:
          - Use PHASE5_WRAP_ROOF_BLACK_RULE_DEEPEN_L1
      - Else:
      - If objection_repeat_count <= 1:
        - Use PHASE5_WRAP_EXPECTATION_DEEPEN_L1
      - If objection_repeat_count == 2:
        - Use PHASE5_WRAP_NARROW_L2
      - If objection_repeat_count >= 3:
        - Use PHASE5_WRAP_EXIT_FORK_L3

Hard stop:
- After selecting the PHASE5_* block, STOP (do not append any other blocks).

------------------------------------------------------------
PHASE 4 — POLISHING (CONFIDENCE ROUTING)
------------------------------------------------------------

Applies when:
- active_service_context == polishing

Routing rules (select ONE block only):

1) Price pressure / “too expensive” / “cheaper elsewhere”:
  - Use PHASE4_POLISH_PRICE_PRESSURE_L1 (first push)
  - If repeated pressure → PHASE4_POLISH_PRICE_PRESSURE_L2
  - If still repeated → PHASE4_POLISH_PRICE_PRESSURE_L3

2) Scope ambiguity / “what’s included” / “full detail or just polish”:
  - Use PHASE4_POLISH_SCOPE_CLARITY_L1

3) Expectation mismatch / “will it remove everything?” / “make it new?”:
  - Use PHASE4_POLISH_EXPECTATION_REALISM_L1

4) Polishing vs protection confusion (“is this like ceramic/PPF?”):
  - Use PHASE4_POLISH_VS_PROTECTION_SIMPLE_L1

5) Silence recovery (post options / post price):
  - Primary: PHASE4_POLISH_SILENCE_PRIMARY
  - If still silent / needs a nudge: PHASE4_POLISH_SILENCE_SCOPE_NUDGE
## QUALIFICATION NOT-READY SUPPRESSION (HARD)

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

Exception C — Competitor Cheaper / Price Pressure while NOT_READY (pre-price only)
Applies when ALL are true:
- allowed_next_actions includes ask_missing_info
- (price_ladder_state == NONE OR price_ladder_state == NOT_APPLICABLE)
- current_user_message contains any of:
  - "cheaper" OR "cheaper elsewhere" OR "too expensive" OR "expensive" OR "price is high"
  - "أرخص" OR "غالي" OR "السعر عالي" OR "سعر عالي"

Required output behavior:
- Output MUST use ONLY:
  - PHASE4_6_HUMAN_PHRASE_LIBRARY.md → COMPETITOR CHEAPER — PHASE 0–2
- selected_phrase_id MUST equal "COMPETITOR CHEAPER — PHASE 0–2"
- Output MUST contain exactly 1 question total.
- Do NOT mention discounts, attacks on competitors, or any pricing numbers.
- STOP (do not append any other blocks).

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
IF (phase == PHASE_3 OR phase == PHASE_3B) AND request_type == PRICE_REQUEST AND all qualification fields complete:
- Select appropriate PHASE3B_* acknowledgement block (based on service + qualifier result)
- Use PRICE_LADDER_ENGINE.md output (pricing allowed ONLY inside that engine’s constraints).
- If phase4_anchor_used != true:
  - Append PHASE4_ANCHOR_AFTER_PRICE_ONCE
  - Set phase4_anchor_used = true
- Do NOT add additional questions unless PRICE_LADDER_ENGINE explicitly requires a single clarifier.
- Suppress hooks unless hook gates pass AND question-cap remains respected.

  ## PHASE 3B — TRANSITION ACKNOWLEDGEMENT (SERVICE STANDARD)
  (Route E selects the correct PHASE3B_* block based on service)
    - PHASE3B_PPF_RANGE                       → PHASE3B_PPF_RANGE
    - PHASE3B_CERAMIC_RANGE                   → PHASE3B_CERAMIC_RANGE
    - PHASE3B_TINT_RANGE                      → PHASE3B_TINT_RANGE
    - PHASE3B_POLISHING_RANGE                 → PHASE3B_POLISHING_RANGE
    - PHASE3B_WRAP_RANGE                      → PHASE3B_WRAP_RANGE

Route F — Price Resistance / Comparison (Phase 7 controlled pricing response)
IF (PRICE_PRESSURE_LEVEL == HIGH OR DISCOUNT_EXPECTATION_RISK == HIGH):

- Use PRICE_LADDER_ENGINE.md output (pricing allowed ONLY inside that engine’s constraints).
- If phase4_anchor_used != true:
  - Append PHASE4_ANCHOR_AFTER_PRICE_ONCE
  - Set phase4_anchor_used = true
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

- Do NOT propose hybrid, layered, "top-up later", or future upgrade service paths unless explicitly defined in:
  - SKU_SELECTION_MATRIX.md
  - GLOBAL_PRODUCT_NAMING_REGISTRY.md
- If such service path is not defined in those files, it is considered invention and must be suppressed.

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

