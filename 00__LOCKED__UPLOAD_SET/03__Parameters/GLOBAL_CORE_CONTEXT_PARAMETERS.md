# GLOBAL_CORE_CONTEXT_PARAMETERS.md
Version: v1.0
Status: LOCKED (v1.0)

## LOCK NOTE
- This file defines **core, stable parameters** used across engines.
- Values must be **UPPERCASE_SNAKE_CASE** (no symbols, no slashes).
- Engines may **read** these parameters but must NOT invent new values.
- Any change requires a version bump (v1.1, v1.2...) and review.

---

## PURPOSE
This file standardizes customer + vehicle + usage + service-intent context so the system:
- stays consistent across Qualification, Pricing, Negotiation, Tone, and Recovery
- avoids vague words
- supports clean tags/labels without drift

This file contains:
- parameter definitions
- allowed values
- short notes on usage

This file contains **NO pricing**, **NO phrasing**, and **NO negotiation scripts**.

---

## GLOBAL RULES
- Parameter names: UPPERCASE_SNAKE_CASE
- Parameter values: UPPERCASE_SNAKE_CASE only
- Always support UNKNOWN when reality is unclear
- Capture reality first; guidance/decisions happen in engines (not here)

---

# CATEGORY 1 — CORE CUSTOMER CONTEXT

### PARAMETER: CUSTOMER_RELATIONSHIP_STATE
Description: Relationship context with Snash.
Allowed Values:
- NEW
- RETURNING
- REFERRED
- UNKNOWN

Used By:
- Tone Engine
- Negotiation Logic
- Handoff Strategy

---

### PARAMETER: CUSTOMER_BUYING_STAGE
Description: Where the customer is in decision journey (observed, not assumed).
Allowed Values:
- EXPLORING
- COMPARING
- READY_TO_BOOK
- UNKNOWN

Used By:
- Qualification Engine
- Tone Engine
- Closing/Handoff Strategy

---

### PARAMETER: TRUST_LEVEL
Description: How much trust is established so far (coarse, not psychological).
Allowed Values:
- LOW
- BUILDING
- ESTABLISHED
- UNKNOWN

Used By:
- Tone Engine
- Education Depth control (via system intent later)
- Recovery posture

---

### PARAMETER: REGIONAL_SENSITIVITY
Description: Regional/cultural sensitivity context for communication style.
Allowed Values:
- GCC
- BAHRAIN
- UAE
- INDIA
- OTHER
- UNKNOWN

Notes:
- This guides tone safety and ego handling.
- It does NOT change pricing.

Used By:
- Tone Engine
- Recovery posture

---

# CATEGORY 2 — VEHICLE CONTEXT

### PARAMETER: VEHICLE_SEGMENT
Description: Business + ego positioning of the vehicle.
Allowed Values:
- DAILY
- PREMIUM
- LUXURY_EXOTIC
- UNKNOWN

Used By:
- Tone Engine
- Pricing Ladder framing
- Inspection gating posture

---

### PARAMETER: VEHICLE_STATE
Description: Paint/condition state (ego-safe replacement for “new/old”).
Allowed Values:
- FACTORY_FRESH
- IN_USE
- AGED_OR_REPAINT_RISK
- UNKNOWN

Used By:
- Qualification Engine
- Pricing Ladder Engine (variability gating)

---

### PARAMETER: VEHICLE_AGE_BUCKET
Description: Age classification used for expectation setting and guidance framing.
Allowed Values:
- AGE_0_3_YEARS
- AGE_3_6_YEARS
- AGE_7_PLUS_YEARS
- UNKNOWN

Notes:
- This can be adjusted later (e.g., AGE_0_2_YEARS) via version bump.
- Age bucket supports guidance; VEHICLE_STATE controls paint/inspection risk.

Used By:
- Qualification Engine
- Pricing Ladder Engine
- Advisory framing

---

### PARAMETER: VEHICLE_COLOR_TYPE
Description: Visual sensitivity / care relevance.
Allowed Values:
- LIGHT
- DARK
- MATTE
- SPECIAL_FINISH
- UNKNOWN

Notes:
- Treated as a FACT here.
- Used later as an objection/recovery hook (no conflict).

Used By:
- Tone Engine
- Advisory framing
- Objection recovery hooks

---

# CATEGORY 3 — USAGE & ENVIRONMENT CONTEXT

### PARAMETER: USAGE_PATTERN
Description: Primary driving environment.
Allowed Values:
- CITY
- HIGHWAY
- MIXED
- UNKNOWN

Used By:
- Pricing Ladder framing
- Service guidance framing (no upsell)

---

### PARAMETER: PARKING_ENVIRONMENT
Description: Where the car is usually parked.
Allowed Values:
- COVERED
- OPEN
- MIXED
- UNKNOWN

Used By:
- Advisory framing
- Expectation setting

---

### PARAMETER: WASHING_STYLE_BUCKET
Description: Customer-recognizable washing behavior (do not judge; used sensitively).
Allowed Values:
- BUCKET_WASH_REGULAR
- BUCKET_WASH_OCCASIONAL
- TUNNEL_BRUSH_WASH
- PROFESSIONAL_CAR_CARE
- WATERLESS_MALL_WASH
- MIXED_OR_UNKNOWN

Notes:
- Ask only when relevant.
- Not a blocker for early pricing.

Used By:
- Advisory framing
- Objection recovery hooks

---

### PARAMETER: CLIMATE_EXPOSURE
Description: Environmental stress context (regional).
Allowed Values:
- HIGH_HEAT
- COASTAL
- DUSTY
- NORMAL
- UNKNOWN

Used By:
- Advisory framing
- Expectation setting

---

# CATEGORY 4 — SERVICE & COVERAGE INTENT (PRODUCT-ALIGNED)

### PARAMETER: SERVICE_INTENT
Description: Primary service customer is asking about (or implied).
Allowed Values:
- PPF
- CERAMIC
- TINT
- DETAILING
- WRAP
- MIXED_OR_UNDECIDED

Used By:
- Qualification Engine
- Pricing Ladder Engine

---

### PARAMETER: SCOPE_INTENT
Description: Scope customer has in mind, aligned to Snash offerings. System must not invent variants.
Allowed Values:
- FULL_COVERAGE
- PARTIAL_OR_CUSTOM
- UNSURE

Notes:
- If customer asks for partial/custom, assistant may clarify (limited).
- Do not decompose products unless customer explicitly asks.

Used By:
- Qualification Engine
- Pricing Ladder Engine

---

### PARAMETER: PPF_COVERAGE_INTENT
Description: PPF-only coverage detail when SERVICE_INTENT includes PPF.
Allowed Values:
- FULL_BODY
- FULL_FRONT
- PARTIAL_OR_CUSTOM
- UNSURE
- NOT_APPLICABLE

Used By:
- Pricing Ladder Engine
- Qualification Engine

---

# OPERATIONAL HIGH-LEVERAGE CONTEXT (ADDED)

### PARAMETER: DELIVERY_STATUS
Description: Whether customer already has the car or is receiving soon.
Allowed Values:
- HAS_CAR_NOW
- GETTING_SOON
- UNKNOWN

Used By:
- Qualification Engine
- Follow-up and scheduling strategy

---

### PARAMETER: OWNER_TIMELINE
Description: Customer’s intended timeframe (drives follow-up + closing posture).
Allowed Values:
- ASAP
- THIS_WEEK
- THIS_MONTH
- LATER
- UNKNOWN

Used By:
- Tone Engine
- Handoff/closing strategy
- Follow-up planning

---

### PARAMETER: DECISION_ROLE
Description: Whether the person chatting is the decision maker.
Allowed Values:
- DECISION_MAKER
- ASKING_FOR_SOMEONE_ELSE
- UNKNOWN

Used By:
- Qualification Engine
- Closing strategy (avoid loops)

---

### PARAMETER: CUSTOMER_LOCATION_BRANCH
Description: Location/branch context for handoff and logistics.
Allowed Values:
- BAHRAIN
- UAE
- INDIA
- UNKNOWN

Notes:
- If you want city-level later, add values via version bump (v1.1+).

Used By:
- Handoff strategy
- Scheduling

---

## ADDITIONAL CORE CONTEXT (DUE DILIGENCE ADD)

### PARAMETER: EXISTING_PROTECTION_STATUS
Description: Whether the vehicle already has protection installed (prevents wrong assumptions).
Allowed Values:
- NONE
- HAS_PPF
- HAS_CERAMIC
- HAS_TINT
- MIXED_OR_UNKNOWN

Used By:
- Qualification Engine
- Pricing Ladder Engine
- Advisory framing

---

### PARAMETER: PAINTWORK_HISTORY
Description: Known history of repaint/bodywork (explicit signal beyond VEHICLE_STATE).
Allowed Values:
- ORIGINAL_PAINT
- HAS_REPAINT_OR_BODYWORK
- UNKNOWN

Notes:
- If customer mentions repaint/bodywork, this overrides ambiguity.
- Impacts inspection gating and expectation setting.

Used By:
- Qualification Engine
- Pricing Ladder Engine

---

### PARAMETER: VEHICLE_BODY_STYLE
Description: Broad vehicle form factor (guidance-relevant, not technical spec).
Allowed Values:
- SEDAN
- SUV
- COUPE
- HATCHBACK
- PICKUP
- OTHER
- UNKNOWN

Used By:
- Pricing Ladder framing
- Coverage guidance framing

---

### PARAMETER: SERVICE_LOCATION_PREFERENCE
Description: Where customer prefers service delivery.
Allowed Values:
- IN_SHOP
- MOBILE
- NO_PREFERENCE
- UNKNOWN

Used By:
- Handoff strategy
- Scheduling

---


### PARAMETER: LANGUAGE_PREFERENCE
Description: Customer’s preferred language for communication.
Allowed Values:
- ARABIC
- ENGLISH
- UNKNOWN

Notes:
- Preference may be explicit or inferred from conversation.
- Used only to adapt phrasing, never to change logic or pricing.

Used By:
- Tone / Phrase Engine
- Handoff strategy
---

## END OF FILE