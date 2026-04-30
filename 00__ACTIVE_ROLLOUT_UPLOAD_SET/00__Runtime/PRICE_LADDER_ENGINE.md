# PRICE_LADDER_ENGINE.md

- Pricing authority source: 02__Parameters/PRICE_TABLE_VAT_INCL.md (VAT-included, locked)
ENGINE_NAME: Price Ladder Execution Engine  
ENGINE_VERSION: v1.2  
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

- VERSION: 1.2

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
- Set price_ladder_state = none
- Set ladder_terminal_state = TERMINATED_NO_PRICE
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

### OUTPUT FORMAT RULES
- When rendering pricing:
  - If ladder returns multiple valid SKU prices: display a range:
      FROM {lowest_valid_price} TO {highest_valid_price} BD VAT included.
  - If ladder returns a single valid SKU price: display that price only:
      {price} BD VAT included.
  - Do not fabricate synthetic ranges or invented upper bounds.
  - All prices must strictly match PRICE_TABLE_VAT_INCL.md.
- Output pricing for cheapest push:
  - CONSTRAINT: Use only the lowest SKU price. Do not combine into ranges unless inherent to ladder.

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

---

## SUPPORTED SERVICE PRICE EXECUTOR (LOCKED)

Purpose:
- Deterministically execute supported Phase 3B service pricing.
- Stop relying on model inference from loaded pricing tables.

Applies when:
- request_type == PRICE_REQUEST
- QUALIFICATION_STATUS == READY_FOR_NEGOTIATION
- service_intent is one of: ppf, ceramic, tint, polishing
- vehicle_model and vehicle_year are known
- service_intent is NOT wrap

Authority boundaries:
- GLOBAL_VEHICLE_CLASSIFICATION_REPOSITORY.md owns model → VCB.
- SKU_SELECTION_MATRIX.md owns SKU ordering.
- PRICE_TABLE_VAT_INCL.md owns numeric prices.
- PRICE_LADDER_ENGINE.md owns SKU-to-price execution and price_ladder_state.

Universal execution rules:
1) Resolve CANONICAL_MODEL and VCB using GLOBAL_VEHICLE_CLASSIFICATION_REPOSITORY.md.
2) PRICE_TABLE_VAT_INCL.md column MUST be VCB, not VEHICLE_SEGMENT.
3) If VCB is NULL or UNMAPPED_MODEL == TRUE:
   - Do NOT default to VCB_1.
   - Set price_ladder_state = ESCALATED_TO_QUOTE.
   - Route to manual VCB assignment / quote.
4) Select supported-service SKU path:
   - ppf front/matte priority:
     - Resolve FRONT and MATTE before gloss full-body logic.
     - If PPF_COVERAGE_INTENT == FULL_FRONT AND PPF_FINISH_INTENT != MATTE:
       - Treat FULL_FRONT as PRIMARY customer intent, not as Downladder.
       - selected_skus MUST be [PPF_FRONT_GLOBAL].
       - Select ONLY PPF_FRONT_GLOBAL.
       - Do NOT use DEFAULT / SECOND / UPLADDER / DOWNLADDER logic.
       - Do NOT generate multiple SKUs.
       - Do NOT evaluate gloss full-body/highway PPF rules.
       - Output single price only from PRICE_TABLE_VAT_INCL.md using resolved VCB.
       - Do NOT set FINAL_PRICE_REACHED if selected_skus != [PPF_FRONT_GLOBAL].
     - If PPF_COVERAGE_INTENT == FULL_FRONT AND PPF_FINISH_INTENT == MATTE:
       selected_skus = [GLOBAL_MATTE_FRONT_10Y]
     - If PPF_COVERAGE_INTENT == FULL_BODY AND PPF_FINISH_INTENT == MATTE AND brand_intent == DEFAULT:
       selected_skus = [GLOBAL_MATTE_10Y]
     - If PPF_COVERAGE_INTENT == FULL_BODY AND PPF_FINISH_INTENT == MATTE AND brand_intent == XPEL:
       selected_skus = [XPEL_STEALTH_10Y]
     - Front/matte selected_skus override all gloss/full-body/default/highway PPF rules.
     - If PPF_FINISH_INTENT == MATTE, do NOT use GLOBAL_SIGNATURE_10Y, GLOBAL_ELITE_8Y, XPEL_EXO_7Y, or XPEL_UP_10Y unless explicitly listed in the matte rule above.
     - HARD MATTE LOCK:
       If PPF_FINISH_INTENT == MATTE AND PPF_COVERAGE_INTENT == FULL_BODY AND brand_intent == DEFAULT:
       selected_skus MUST be [GLOBAL_MATTE_10Y].
       Any output using GLOBAL_SIGNATURE_10Y, GLOBAL_ELITE_8Y, XPEL_EXO_7Y, or XPEL_UP_10Y is invalid.
       Do NOT set FINAL_PRICE_REACHED if selected_skus != [GLOBAL_MATTE_10Y].
     - HARD MATTE XPEL LOCK:
       If PPF_FINISH_INTENT == MATTE AND PPF_COVERAGE_INTENT == FULL_BODY AND brand_intent == XPEL:
       selected_skus MUST be [XPEL_STEALTH_10Y].
       Any output using GLOBAL_SIGNATURE_10Y, GLOBAL_ELITE_8Y, XPEL_EXO_7Y, XPEL_UP_10Y, or GLOBAL_MATTE_10Y is invalid.
       Do NOT set FINAL_PRICE_REACHED if selected_skus != [XPEL_STEALTH_10Y].
   - ppf gloss full body:
     - This section applies ONLY if PPF_COVERAGE_INTENT == FULL_BODY.
     - If PPF_COVERAGE_INTENT == FULL_FRONT, this section MUST NOT execute.
     - If PPF_COVERAGE_INTENT == FULL_FRONT, the earlier FULL_FRONT terminal lock is final.
     - Match exactly ONE SKU_SELECTION_MATRIX.md row using:
       resolved VCB + brand intent + PPF_DRIVING_PATTERN.
     - If brand intent is not explicit, use the DEFAULT row for that VCB + PPF_DRIVING_PATTERN.
     - If brand intent is XPEL, use the XPEL row for that VCB + PPF_DRIVING_PATTERN.
     - selected_skus MUST equal Default (A) + Second (B) from the matched row only.
     - Do NOT reuse Second (B), Upladder, or Downladder from any other PPF row.
     - Standard range output must NOT use Upladder or Downladder unless the active runtime route explicitly asks for ladder movement.
     - Brand intent (e.g., XPEL) selects the correct matrix row ONLY.
     - Brand intent does NOT trigger Upladder selection.
     - Upladder must only be used after explicit customer upgrade intent after price exposure.
     - Deterministic PPF selected_skus MUST be resolved by exact condition, same style as ceramic:
       - If VCB == VCB_1 AND brand_intent == DEFAULT AND PPF_DRIVING_PATTERN == HIGHWAY:
         selected_skus = [GLOBAL_ELITE_8Y, GLOBAL_SIGNATURE_10Y]
       - If VCB == VCB_2 AND brand_intent == DEFAULT AND PPF_DRIVING_PATTERN == HIGHWAY:
         selected_skus = [GLOBAL_SIGNATURE_10Y, GLOBAL_ELITE_8Y]
       - If VCB == VCB_2 AND brand_intent == XPEL AND PPF_DRIVING_PATTERN == HIGHWAY:
         selected_skus = [XPEL_EXO_7Y, GLOBAL_SIGNATURE_10Y]
       - If VCB == VCB_3 AND brand_intent == DEFAULT AND PPF_DRIVING_PATTERN == HIGHWAY:
         selected_skus = [GLOBAL_SIGNATURE_10Y, GLOBAL_ELITE_8Y]
     - These exact selected_skus override generic brand-upgrade reasoning.
     - Do NOT substitute XPEL_UP_10Y for GLOBAL_SIGNATURE_10Y unless customer explicitly asks to upgrade after price exposure.
     - If no exact deterministic PPF condition matches, do NOT infer; escalate to quote.

   - ceramic:
     - Derive vehicle_age = CURRENT_YEAR - vehicle_year.
     - Select ceramic SKU path by exact age boundary:
       - If vehicle_age <= 3: selected_skus = [CERAMIC_3Y, CERAMIC_5Y]
       - If vehicle_age >= 4 AND vehicle_age <= 6: selected_skus = [CERAMIC_1Y, CERAMIC_3Y]
       - If vehicle_age >= 7: selected_skus = [CERAMIC_1Y, GRAPHENE_1Y]
     - These selected_skus mirror SKU_SELECTION_MATRIX.md Default (A) + Second (B).
     - Do NOT use Upladder / Downladder for standard ceramic range output.
   - tint:
     - Use TINT_NANO_CERAMIC + TINT_XPEL_XR_PLUS from PRICE_TABLE_VAT_INCL.md.
   - polishing exterior:
     - Use POLISH_SILVER from PRICE_TABLE_VAT_INCL.md.
     - selected_skus MUST equal [POLISH_SILVER].
     - Select ONLY POLISH_SILVER.
     - Do NOT include POLISH_GOLD for standard exterior polishing price.
     - Do NOT render a range from catalog/table rows.
     - Do NOT set FINAL_PRICE_REACHED if selected_skus != [POLISH_SILVER].
5) Lookup selected SKU prices in PRICE_TABLE_VAT_INCL.md using the resolved VCB column.
   - Once VCB is resolved, ALL selected SKU prices MUST be read strictly from the SAME resolved VCB column.
   - Do NOT mix VCB columns across selected_skus under any condition.
   - price_source_rows MUST include full trace per SKU:
     {SKU: <sku>, VCB: <resolved_vcb>, PRICE: <value>}
   - If any SKU resolves to a different VCB column or missing value:
     - DO NOT render price
     - DO NOT set FINAL_PRICE_REACHED
     - Route to ESCALATED_TO_QUOTE

6) Render only the approved price or range:
   - Multiple prices: FROM {lowest_valid_price} TO {highest_valid_price} BD VAT included.
   - Single price: {price} BD VAT included.
7) Set price_ladder_state = FINAL_PRICE_REACHED only after the customer-facing price/range is rendered.

Hard prohibitions:
- Do NOT use VEHICLE_SEGMENT as the price-table column.
- Do NOT default unknown or missing VCB to VCB_1.
- Do NOT select catalog-only SKUs just because they exist in GLOBAL_PRODUCT_NAMING_REGISTRY_v1.0.md or PRICE_TABLE_VAT_INCL.md.
- Do NOT use Upladder / Downladder SKUs for standard price range unless the active runtime route explicitly asks for ladder movement.
- Do NOT set FINAL_PRICE_REACHED without rendering actual customer-facing price/range.
- Do NOT output any customer-facing numeric price unless every price number is traceable to:
  resolved vehicle VCB + selected SKU(s) + PRICE_TABLE_VAT_INCL.md.
- Any price not found through selected_skus + resolved VCB + PRICE_TABLE_VAT_INCL.md is forbidden, even if it appears in older tests, reports, examples, or prior conversation history.

---
## WRAP — MINIMUM RANGE SUPPORT (TEMPORARY)

STATUS: MINIMAL IMPLEMENTATION (flow stability first)
GAP NOTE: Finish-specific reordering and richer wrap ladders remain governed by
SKU_SELECTION_MATRIX.md and can be refined later without changing this engine.

Applies when:
- service_intent == wrap
- phase3a_complete == true
- PRECONDITION: request_type == PRICE_REQUEST (request_type is written only by QUALIFICATION_ENGINE.md)

Inputs:
- vehicle_segment ∈ {VCB_1, VCB_2, VCB_3}
- WRAP_SCOPE ∈ {FULL_VEHICLE, UNKNOWN}
- WRAP_FINISH ∈ {GLOSS, MATTE, SATIN, UNKNOWN}

Steps:
1) Select SKUs from SKU_SELECTION_MATRIX.md (do NOT implement selection logic here):
  - WRAP is supported ONLY for FULL VEHICLE:
    - sku_a = WRAP_DEFAULT_A   (as returned by SKU_SELECTION_MATRIX for WRAP)
    - sku_b = WRAP_SECOND_B    (as returned by SKU_SELECTION_MATRIX for WRAP)

REPO-SAFETY NOTE (LOCKED):
- Do NOT hard-code any roof-wrap SKU here. Roof-black styling is fulfilled ONLY by ROOF_PPF_BLACK_GLOSS (PPF), governed by the product registry + routing.
- Partial/section wrap pricing is not supported by automation (FULL VEHICLE WRAP only).

2) Price lookup:
  - price_a = PRICE_TABLE_VAT_INCL[sku_a][vehicle_segment]
  - price_b = PRICE_TABLE_VAT_INCL[sku_b][vehicle_segment]

3) Range:
  - RANGE_MIN_BD = min(price_a, price_b)
  - RANGE_MAX_BD = max(price_a, price_b)

Hard rules:
- No clarifier questions inside the ladder engine.
- Do not list SKUs.
- Output range only.
- If roof-black styling is requested, WRAP ladder must NOT execute. Route to ROOF_PPF_BLACK_GLOSS handling in the PPF path.

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

---

## ROOF PPF HANDLING NOTE
- Roof-black styling is fulfilled ONLY by ROOF_PPF_BLACK_GLOSS.
- Pricing behavior:
  - price = PRICE_TABLE_VAT_INCL[ROOF_PPF_BLACK_GLOSS][vehicle_segment]
  - RANGE_MIN_BD = price
  - RANGE_MAX_BD = price
- Do NOT treat roof-black as WRAP. Do NOT output roof-wrap pricing.

- ROOF_ONLY PPF is a valid coverage variant
- Execution may use existing PPF SKUs
- Dedicated ROOF_PPF SKUs are not required
- Assistant confirmation or manual mapping is permitted
- If roof-black styling is requested, use ROOF_PPF_BLACK_GLOSS SKU if present in repositories.

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

LOCKED_ON: 2026-01-08PHASE 3B — SKU SELECTION AUTHORITY (LOCKED)
────────────────────────────────────────────────────────────

Selection rules (DEFAULT / SECOND / UPLADDER / DOWNLADDER) are defined ONLY in:
- 02__Parameters/SKU_SELECTION_MATRIX.md

Hard rule:
- PRICE_LADDER_ENGINE.md MUST NOT redefine or duplicate SKU defaults here.
- If SKU ordering needs changes, edit SKU_SELECTION_MATRIX.md only.


---

## CUSTOMER-FACING LABEL RULE (LOCKED)

When presenting any option(s) to the customer (A/B, upladder/downladder, etc.):

1) DO NOT display raw SKU IDs (e.g., GLOBAL_ELITE_8Y, XPEL_UP_10Y) in customer-facing text.
2) Instead, render:
   - display_name (from GLOBAL_PRODUCT_NAMING_REGISTRY_v1.0.md)
   - warranty (from GLOBAL_PRODUCT_NAMING_REGISTRY_v1.0.md)
   Example format:
   - Option A: <display_name> — <warranty>

3) short_description may be used ONLY when a single neutral clarification is needed,
   and must remain one sentence max (no marketing claims).

Single source of truth for these fields:
- 02__Repositories/GLOBAL_PRODUCT_NAMING_REGISTRY_v1.0.md

