# PRICE_LADDER_ENGINE.md

ENGINE_NAME: Price Ladder Execution Engine  
ENGINE_VERSION: v1.1  
ENGINE_PHASE: Phase 3  
ENGINE_STATUS: Locked  

---

ASSUMPTION — UPSTREAM STEERING COMPLETE

This engine assumes:
- Service fit and solution framing have already been handled upstream (Phase 2 — Negotiation Logic)
- This engine does NOT educate, correct, or re-steer service choices
- This engine only controls pricing expression, option framing, and escalation

If a fit mismatch still exists, the ladder must reduce pricing options
or escalate to quote/human — it must NOT introduce new services.

## PHASE 0 GUARD — SUBSTITUTION CONTROL

All ladder movements are SUGGESTIVE only.

Rules:
- No service substitution may occur automatically
- All up-ladder or down-ladder actions require explicit customer acknowledgment
- Ladder logic may recommend but must not enforce substitutions
- Manual assistant confirmation is mandatory for execution
---

## VERSION_CONTROL

- VERSION: 1.1

- CREATED_ON: 2026-01-06  
- STATUS: Locked 

---

## LOCK NOTE

This file is LOCKED after Phase 3 approval.

Allowed changes:
- Version bump only (v1.1+)
- Minor wording clarifications that do not change behavior

Disallowed changes:
- Allowing exact pricing
- Changing gating rules
- Changing escalation rules
- Adding solution steering logic (must remain upstream)

---

## 1. ENGINE PURPOSE

The Price Ladder Engine governs **how pricing is expressed and controlled**
once pricing discussion is allowed.

It does NOT:
- Decide service fit
- Recommend services, packages, or brands
- Educate or reframe solutions

It ONLY:
- Controls price anchors and ranges
- Manages escalation boundaries
- Protects against price pressure and sticker shock

---

## 2. ENTRY CONDITIONS (STRICT)

### 2.1 Negotiation Gate (hard)

This engine executes ONLY IF:

QUALIFICATION_STATUS == READY_FOR_NEGOTIATION
OR
QUALIFICATION_STATUS == READY

Interpretation:
- READY implies car model + year + service category are confirmed.
- READY_FOR_NEGOTIATION is the preferred explicit state when available.

If NOT met:
- Do not discuss pricing
- Ask for missing information (max 1–2 questions)
- Or route back to Qualification flow

### 2.2 Minimum Qualification Gate (hard vs soft)

## PHASE 0 GUARD — INSPECTION HANDLING

Inspection logic is advisory, not blocking.

Rules:
- Inspection may be satisfied verbally or logically
- Pricing and ladder flow may proceed based on customer affirmation
- Physical inspection may occur prior to execution
- If post-confirmation issues arise, scope is handled manually
- Engines must flag inspection dependency but must not halt closure

Hard gate (must have before any pricing anchor or range):
- Car model
- Model year
- Service category (PPF / ceramic / tint / wrap / polish)

Soft gate (nice to have; ask once only if it materially affects scope):
- Usage context (city vs highway / daily vs weekend)

If soft gate is missing:
- Proceed with wider ranges and clear conditions
- Do NOT block pricing
- Do NOT repeat usage questions

### Old Vehicle Routing Override (7+ Years)

Rule:
- If vehicle model year indicates age ≥ 7 years:

Behavior:
- Usage context (city / highway / desert) becomes OPTIONAL
- Paint condition becomes the preferred soft gate

Replacement soft gate question (ask once only):
- “How is the current paint condition — mostly clean, or does it have visible marks/scratches?”

Routing rules:
- If paint condition is POOR or UNKNOWN:
  → Allow routing to:
    - Lower-tier PPF
    - Front-only PPF
    - OR alternative services (ceramic / polishing)
- Do NOT block pricing
- Do NOT repeat usage questions for old vehicles

---

## 3. INPUT SIGNALS (READ-ONLY)

From Qualification Engine:
- QUALIFICATION_STATUS

From Phase 2 (Negotiation Logic Module) + Dynamic Parameters (canonical names):
- PRICE_PRESSURE_LEVEL
- FRICTION_LEVEL
- OBJECTION_DENSITY
- INFO_COMPLETENESS
- BOOKING_READINESS
- COMPETITOR_QUOTE_STATUS (if present)
- DISCOUNT_EXPECTATION_RISK (if present)

Optional routing/steering tags from Phase 2 (only if emitted; otherwise ignore safely):
- SOLUTION_DIRECTION
- RECOMMENDED_TIER
- PRICE_EXPOSURE_RISK
- QUOTE_REQUIRED_FLAG

From Global Core Parameters (canonical names):
- VEHICLE_SEGMENT
- REGIONAL_SENSITIVITY
- TRUST_LEVEL (if present)
- CUSTOMER_DECISION_STAGE (if present)

---

### 3.1 Signal Compatibility Bridge (NON-BINDING)

Purpose:
- Allow downstream pricing behavior to remain stable even if upstream engines emit
  different-but-equivalent negotiation or pressure tags.
- This is a READ-ONLY interpretation layer.
- Canonical fields always win if present.

Compatibility rules (examples):

- If signal_tags[] contains PRICE_PUSHY_EARLY or PRICE_LOOP_RISK:
  → treat PRICE_PRESSURE_LEVEL as HIGH (if not already set)

- If signal_tags[] contains EXTERNAL_QUOTE_MENTIONED or COMPETITOR_REFERENCE_PRESENT:
  → set COMPETITOR_QUOTE_STATUS = PRESENT (if not already set)

- If signal_tags[] contains NEEDS_REASSURANCE or DECISION_RISK_HIGH:
  → allow one reassurance anchor sentence after price (no option expansion)

- If signal_tags[] contains TECH_JARGON_INFLUENCED or SPEC_OVERLOAD_RISK:
  → suppress feature-heavy explanations; prioritize outcome framing

Rules:
- This bridge MUST NOT invent new tags
- This bridge MUST NOT override explicit canonical parameters
- Unknown tags must be ignored safely

Note on Tag Naming:
- External documents may refer to conceptual "SIG_*" signals.
- Runtime MUST NOT emit SIG_* tags.
- All such concepts must map into the canonical taxonomy defined above.
- PRICE_LADDER_ENGINE may interpret these tags via its Signal Compatibility Bridge.

---

## 4. OUTPUT CONTRACT

All outputs must:
- Use simple, human language
- Avoid sales or marketing tone
- Avoid robotic phrasing

Format rules:
- Maximum 2 options per response
- Ask only 1 micro-question
- Never repeat the same price range without new information

Outputs must comply with:
- OUTPUT_RESPONSE_TEMPLATE.md

### 4.1 Emitted Control Tag (REQUIRED)

This engine MUST emit a terminal control tag for downstream orchestration:

- price_ladder_state: ENUM
  - Meaning: Terminal execution state of the pricing ladder (not a ladder level).
  - Values:
    - IN_PROGRESS
    - FINAL_PRICE_REACHED
    - ESCALATED_TO_QUOTE
    - TERMINATED_NO_PRICE

Notes:
- This tag is internal (non-customer-facing).
- This tag does not reveal exact prices.

### 4.2 Customer-facing output template (EN then AR)

EN:
Based on what you confirmed, here are the two PPF options to check:
Option A: <SKU_NAME_A>
Option B: <SKU_NAME_B>
If you’re aiming for something more cost-effective, we also have a lighter option that focuses on the high-impact areas.
Which one do you want to check first, A or B?

AR:
حسب اللي تم تأكيده، هذي خيارين PPF نقدر نبدأ فيهم:
الخيار A: <SKU_NAME_A>
الخيار B: <SKU_NAME_B>
وإذا تبي خيار أوفر، عندنا خيار أخف يركّز على المناطق الأكثر تعرّضاً.
أي واحد تحب نبدأ فيه، A أو B؟

---

## 5. PRICING DISCIPLINE (LOCKED)

Non-negotiable rules:
1. Context → Fit → Price
2. One price at a time
3. No discount reflex
4. No apology for pricing
5. “Price is high” → acknowledge + reframe + clarify (never discount)
6. No invented coverage variants
   - Do NOT imply “partial panels / key areas / basic coverage” for Ceramic unless PRODUCT_SERVICE_CANON explicitly defines such variants.
   - Default assumption for Ceramic pricing language is full coverage only.
---

## 5.1 STEERING SIGNAL MODIFIERS (PRICING ONLY)

If optional Phase 2 signals exist, they modify pricing behavior only:

- PRICE_EXPOSURE_RISK = HIGH  
  → Keep ranges wide, avoid narrowing, escalate earlier if pushed

- QUOTE_REQUIRED_FLAG = TRUE  
  → Skip directly to escalation when exact pricing is demanded

- RECOMMENDED_TIER present  
  → Use tier language only (standard / premium), no brands or prices

- SOLUTION_DIRECTION present  
  → Maintain consistency with upstream framing (no re-steering)

If signals are absent:
- Operate using default ladder logic

---

## 6. PRICE LADDER LEVELS

| Level | Name | Usage |
|------|------|------|
| L0 | Qualification Gate | Missing required info |
| L1 | Soft Anchor | Controlled exception only |
| L2 | Contextual Range | Core pricing discussion |
| L3 | Conditional Narrowing | Scope clearer |
| L4 | Boundary Signal | Pressure control |
| L5 | Escalation Gate | Quote / human handoff |

---

## 7. LADDER LEVEL LOGIC

L0 — Qualification Gate  
- Ask max 1–2 questions
- Do not anchor pricing

L1 — Soft Anchor  
- “Starts from” language only
- Immediately ask one clarifying question

L2 — Contextual Range  
- Broad range tied to variables
- Max 2 options

L3 — Conditional Narrowing  
- If/then narrowing based on scope

L4 — Boundary Signal  
- Set limits
- Avoid argument
- Move toward verification

L5 — Escalation Gate  
- Stop pricing
- Route to quote or human

Deterministic selection rules:

Coverage handling rule (business-safe):
- If PPF_COVERAGE_SELECTED == UNKNOWN:
  - Do NOT ask "front vs full" automatically.
  - Default ladder output to FULL-BODY style options (two SKUs) based on brand/warranty intent.
  - Add ONE soft line that a lighter "high-impact areas" option exists for cost-conscious customers,
    without naming "front PPF" unless the customer explicitly asks.

────────────────────────────────────────────────────────────
PHASE 3B — NON-PPF SELECTION RULES (LOCKED — SKU-TRUE)
────────────────────────────────────────────────────────────

Purpose:
- Convert Phase 3A readiness + minimal qualifiers into a deterministic SKU shortlist.
- No invention: only use SKU IDs that exist in GLOBAL_PRODUCT_NAMING_REGISTRY_v1.0.md.
- Do not create new SKUs, durations, or “coverage variants” that do not exist in the registry.

Inputs assumed (read-only if present):
- VEHICLE_CLASS_BAND: ENUM (VCB_1 | VCB_2 | VCB_3)
- VEHICLE_AGE_BAND: ENUM (0_3 | 3_6 | 7_PLUS)  (optional; if absent, treat as 0_3)
- SERVICE_INTENT_PRIMARY: ENUM (PPF | CERAMIC_COATING | GRAPHENE_COATING | WINDOW_TINT | PAINT_POLISHING | WRAP)
- SERVICE_INTENT_SECONDARY: optional list (same enums)
- BRAND_EXPLICIT_REQUEST: ENUM (NONE | XPEL)  (only if customer explicitly asked)
- TINT_COVERAGE_SELECTED: ENUM (UNKNOWN | TINT_WINDSHIELD_ONLY | TINT_SIDES_BACK | TINT_FULL_CAR | TINT_FULL_WITH_SUNROOF)

Hard rules:
1) One service per ladder run:
   - If multiple services are asked, pick one PRIMARY service to price first.
   - Do not bundle. Do not merge anchors.
   - Secondary services remain tagged for later pricing after the primary ladder completes.

2) Brand mention control:
   - Do NOT surface brands unless the customer explicitly requested a brand (e.g., asked “XPEL?”).
   - Brand is a selection modifier only.

3) Clarification discipline:
   - If a required selector is UNKNOWN, ask ONE question only.
   - If still unknown or customer pushes exact price → escalate per L5 rules.

────────────────────────────────────────────────────────────
3B.1 — CERAMIC / GRAPHENE SKU DEFAULTS (FULL COVERAGE ONLY)
────────────────────────────────────────────────────────────

Allowed SKUs:
- CERAMIC_1Y | CERAMIC_3Y | CERAMIC_5Y
- GRAPHENE_1Y | GRAPHENE_3Y | GRAPHENE_5Y

Selection defaults (two options max at L2):

A) VEHICLE_AGE_BAND == 0_3 (or missing)
  - Default option 1: CERAMIC_3Y
  - Default option 2: CERAMIC_5Y
  - Upladder 1: GRAPHENE_3Y
  - Upladder 2: GRAPHENE_5Y
  - Downladder 1: CERAMIC_1Y
  - Downladder 2: GRAPHENE_1Y

B) VEHICLE_AGE_BAND == 3_6
  - Default option 1: CERAMIC_1Y
  - Default option 2: CERAMIC_3Y
  - Upladder 1: CERAMIC_5Y
  - Upladder 2: GRAPHENE_3Y
  - Downladder 1: GRAPHENE_1Y
  - Downladder 2: (stay within Ceramic/Graphene only; do not introduce polishing here)

C) VEHICLE_AGE_BAND == 7_PLUS
  - Default option 1: CERAMIC_1Y
  - Default option 2: GRAPHENE_1Y
  - Upladder 1: CERAMIC_3Y
  - Upladder 2: GRAPHENE_3Y
  - Downladder: (no “partial ceramic” variants allowed; if customer is not ready → escalate or re-qualify paint condition upstream)

Note (segment tuning):
- VEHICLE_CLASS_BAND may influence the order (VCB_3 tends to start at 3Y+), but MUST NOT change allowed SKUs.
- If you later want segment-specific ordering, edit ordering only (no new SKUs).

────────────────────────────────────────────────────────────
3B.2 — POLISHING SKU DEFAULTS
────────────────────────────────────────────────────────────

Allowed SKUs:
- POLISH_SILVER | POLISH_GOLD

Defaults:
- Default option 1: POLISH_SILVER
- Default option 2: POLISH_GOLD
- No invented sub-variants.

────────────────────────────────────────────────────────────
3B.3 — WINDOW TINT SKU DEFAULTS + COVERAGE SELECTOR
────────────────────────────────────────────────────────────

Allowed SKUs:
- Film: TINT_NANO_CERAMIC | TINT_XPEL_XR_PLUS
- Coverage: TINT_WINDSHIELD_ONLY | TINT_SIDES_BACK | TINT_FULL_CAR | TINT_FULL_WITH_SUNROOF

Film selection:
- If BRAND_EXPLICIT_REQUEST == XPEL → use TINT_XPEL_XR_PLUS
- Else → use TINT_NANO_CERAMIC

Coverage selection:
- If TINT_COVERAGE_SELECTED == UNKNOWN:
    Ask ONE question: windshield only / sides+back / full car / full with sunroof
    Map directly to the coverage SKU above.

Output rule:
- Tint output must include (FILM SKU + COVERAGE SKU) as the selected pair.

────────────────────────────────────────────────────────────
3B.4 — WRAP SKU DEFAULTS
────────────────────────────────────────────────────────────

Allowed SKUs:
- WRAP_GLOSS | WRAP_MATTE | WRAP_SATIN | ROOF_WRAP_BLACK

Defaults:
- If customer explicitly asked for “roof” or “black roof” → ROOF_WRAP_BLACK
- Else if finish is unknown:
    Ask ONE question: gloss / matte / satin
    Default if customer refuses to choose: WRAP_GLOSS

────────────────────────────────────────────────────────────
END — PHASE 3B NON-PPF SELECTION RULES
────────────────────────────────────────────────────────────

---

## ROOF PPF HANDLING NOTE

- ROOF_ONLY PPF is a valid coverage variant
- Execution may use existing PPF SKUs
- Dedicated ROOF_PPF SKUs are not required
- Assistant confirmation or manual mapping is permitted

## 8. MULTI-SERVICE RULE

If multiple services are asked:
- Give separate anchors
- Do not bundle
- Do not upsell inside pricing

---

## 9. CLARIFICATION LIMIT

- Max 2 clarification questions total
- Do not repeat price ranges without new info
- If stuck → escalate to L5

---

## 10. INTEGRATION POINTS (READ-ONLY)

Integrates with:
- RUNTIME_EXECUTION_FLOW.md
- RUNTIME_STATE_MACHINE.md
- OUTPUT_RESPONSE_TEMPLATE.md
- Parameter Layer files

---

## 11. END STATE

This engine MUST always set `price_ladder_state` before exiting.

Terminal `price_ladder_state` rules:

- FINAL_PRICE_REACHED
  - Set when a final price/range has been presented AND the ladder will not narrow further
  - This is the “pricing completed” terminal state

- ESCALATED_TO_QUOTE
  - Set when the engine routes to quote / human handoff due to:
    - exact pricing demand
    - repeated pressure beyond ladder limits
    - scope ambiguity that requires manual quoting
    - policy/approval gating

- TERMINATED_NO_PRICE
  - Set when pricing is not permitted or cannot proceed safely due to:
    - QUALIFICATION_STATUS != READY_FOR_NEGOTIATION
    - required minimum qualification missing (hard gate)
    - conversation terminated before pricing

- IN_PROGRESS
  - Set only while still actively running ladder levels (L0–L5)
  - Must NOT be left as the final value if the engine exits

Exit conditions (when the engine stops executing):
- Customer proceeds to booking / visit
- Quote or human handoff occurs
- Qualification is incomplete or pricing gate fails

---

## PHASE 3 LOCK CONFIRMATION

STATUS: LOCKED  
ENGINE: PRICE_LADDER_ENGINE  
VERSION: v1.1  

Lock conditions confirmed:
- Phase 0 (Identity & Guardrails): LOCKED
- Phase 1 (Qualification Engine): LOCKED
- Phase 2 (Negotiation Logic Module): LOCKED
- Runtime wiring completed and verified
- No pending patches or open dependencies

This engine is finalized and frozen.
Any modification requires a version bump (v1.1+) and formal architecture review.

LOCKED_ON: 2026-01-08