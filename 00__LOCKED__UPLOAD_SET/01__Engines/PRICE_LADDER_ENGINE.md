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