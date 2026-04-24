# PRODUCT_SERVICE_CANON

Version: 1.0  
Phase: 0 — Authority Layer  
Status: LOCKED 
Role: Product & Service Authority Canon (Read-Only)

---

## 1) Purpose & Authority

This document defines the authoritative rules for what services exist and how they are allowed to be offered.

It answers:
- What services are officially offered
- What service variants are valid
- When inspection logic applies
- What substitutions are allowed or forbidden
- What claims and positioning are prohibited

If a service or rule is not defined here → it is NOT allowed.

This document is read-only for all downstream systems.

---

## 2) Hard Boundaries (Non-Negotiable)

This canon MUST NOT contain:
- Pricing or price ranges
- Product SKUs or brand names
- Warranty or durability years
- Operational steps or process details
- Sales, persuasion, or negotiation language

This canon MAY contain:
- Eligibility rules
- Inspection logic
- Substitution constraints
- Positioning limits

---

## 3) Authoritative Service List

Only the following services are valid:

- PAINT_PROTECTION_FILM (PPF)
- CERAMIC_COATING
- GRAPHENE_COATING
- PAINT_POLISHING
- WINDOW_TINT
- INTERIOR_PROTECTION
- VEHICLE_WRAP

Any service not listed here is not offered.

---

## 4) Service Definitions & Constraints

### 4.1 PAINT_PROTECTION_FILM (PPF)

**Primary Positioning**
- Protection-first service
- May provide gloss enhancement and ease of cleaning
- Not framed as a coating service

**Allowed Coverage Variants**
- FRONT_ONLY
- FULL_FRONT
- FULL_VEHICLE
- ROOF_ONLY

**Constraints**
- Coverage definitions are fixed
- No custom or panel-level variants allowed

**Inspection Logic**
- Required only when paint condition is unclear
- Verbal or logical confirmation is sufficient to proceed
- Physical inspection may occur prior to execution

Note:
- ROOF_ONLY PPF is an allowed coverage variant
- It may be executed using existing PPF SKUs
- Dedicated ROOF_PPF SKUs are not required at Phase 0
- Manual confirmation or ladder mapping may be applied

---

### 4.2 CERAMIC_COATING

**Primary Positioning**
- Surface enhancement and ease of maintenance
- Not impact protection
- Not equivalent to PPF

**Allowed Variants**
- BRONZE
- SILVER
- GOLD

**Inspection Logic**
- Required when paint condition is unclear
- Polishing may be a prerequisite based on condition

---

### 4.3 GRAPHENE_COATING

**Primary Positioning**
- Surface enhancement and ease of maintenance
- Distinct material from ceramic
- Not impact protection
- Not equivalent to PPF

**Allowed Variants**
- BRONZE
- SILVER
- GOLD

**Inspection Logic**
- Same logic as ceramic coating

---

### 4.4 PAINT_POLISHING

**Primary Positioning**
- Corrective service only
- Improves appearance
- No protection role

**Allowed Variants**
- SILVER (exterior polishing)
- GOLD (exterior polishing + interior deep cleaning + engine bay)

**Constraints**
- Not bundled automatically with other services
- Offered based on paint condition

---

### 4.5 WINDOW_TINT

**Primary Positioning**
- Comfort, glare reduction, heat control, and privacy
- Subject to legal compliance

**Allowed Types**
- NANO_CERAMIC
- XPEL_XR_PLUS

**Allowed Coverage**
- WINDSHIELD_ONLY
- SIDES_AND_REAR
- FULL_VEHICLE
- FULL_WITH_SUNROOF

**Legal Logic**
- Compliance is mandatory
- Rules vary by country and customer category
- Engines enforce limits
- Edge cases may be handled manually

---

### 4.6 INTERIOR_PROTECTION

**Primary Positioning**
- Preventive interior surface protection
- Not restorative

**Allowed Variants**
- Single standardized service only

**Inspection Logic**
- Applied when interior condition is unclear or heavily worn

---

### 4.7 VEHICLE_WRAP

**Primary Positioning**
- Visual and cosmetic service only
- Not paint protection

**Allowed Finishes**
- GLOSS
- MATTE
- SATIN

**Roof Logic**
- ROOF_ONLY wrap remains valid
- If protection intent is detected, redirection to ROOF_PPF is allowed with customer acknowledgment

**Inspection Logic**
- Mandatory for wraps
- Physical condition verified prior to execution

---

## 5) Substitution & Redirection Rules

Allowed with customer acknowledgment:
- PPF → CERAMIC_COATING
- PPF → GRAPHENE_COATING
- CERAMIC_COATING → PPF
- GRAPHENE_COATING → PPF
- PAINT_POLISHING → CERAMIC_COATING
- PAINT_POLISHING → GRAPHENE_COATING
- VEHICLE_WRAP → ROOF_PPF (when protection intent exists)

Rules:
- No auto-substitution
- No silent conversion
- Inspection applies only when condition is unclear

---

## 6) Inspection Handling

- Inspection may be verbal or logical
- Inspection does not block business closure
- Physical inspection may occur prior to execution
- If issues arise later, scope is handled manually

Engines must flag inspection dependency but must not force hard stops.

---

## 7) Claims & Positioning Limits

The system MUST NOT claim:
- Lifetime protection
- Scratch-proof or damage-proof outcomes
- Guaranteed durability
- Universal suitability
- Service equivalence

All positioning must remain factual and bounded.

---

## 8) Downstream Consumption Rules

This canon may be consumed by:
- Qualification Engine
- Price Ladder Engine
- Negotiation Engine
- Objection Handling Engine
- Silence Handling Engine
- Runtime Orchestration

No downstream system may override this canon.

---

## 9) Locking Conditions

This document is locked when:
- All services are approved
- Substitution rules finalized
- Inspection logic agreed

Any future change requires:
- Phase 0 unlock
- Version increment
- Explicit approval

---

END OF DOCUMENT