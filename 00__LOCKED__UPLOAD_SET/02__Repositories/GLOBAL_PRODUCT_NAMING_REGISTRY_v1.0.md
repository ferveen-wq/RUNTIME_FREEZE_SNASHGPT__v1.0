# GLOBAL_PRODUCT_NAMING_REGISTRY

Version: 1.0  
Phase: 0 — Authority Layer  
Status: DRAFT (Not Locked)  
Role: Global Product Naming & SKU Registry (Read-Only Authority)

---

## 1) Purpose & Authority

This document defines the **ONLY valid internal product and SKU names** permitted across the system.

All engines MUST:
- Use product names EXACTLY as defined here
- Reject any invented, shortened, or modified names

If a product name does not exist in this registry:
→ The engine MUST halt and escalate to system owner.

This registry OVERRIDES:
- Qualification Engine
- Price Ladder Engine
- Negotiation Engine
- Objection Handling Engine
- Silence Handling Engine
- Tone Engine
- Human Phrase Libraries

---

## 2) Absolute Naming Rules (Non-Negotiable)

- No product names may be shortened
- No aliases or synonyms are allowed
- No variants may be invented
- No durability years may be altered
- No tier labels may replace product names

Wrong examples:
- “Global 8”
- “Fusion”
- “Matte 8Y”
- “Ceramic Platinum”

Correct examples:
- GLOBAL_ELITE_8Y
- XPEL_FUSION_10Y
- GLOBAL_MATTE_10Y
- CERAMIC_5Y

---

## 2.1 Alias Map (INPUT Detection Only — Output Must Stay Canonical)

Rule:
- Aliases/synonyms are allowed ONLY for understanding customer messages (parsing/detection).
- The assistant MUST NOT output aliases as product names; always output canonical names from this registry.
- If input is ambiguous, ask a clarification question; do NOT invent a new SKU.

PPF detection aliases (map to service intent PPF / brand hint only):
- "ppf", "paint protection film", "film", "clear film", "شفاف", "فلم حماية", "حماية بوية", "حماية طلاء"
- XPEL brand hints: "xpel", "اكسبل", "إكسبل", "stealth", "ستيلث"
- Global brand hints: "global", "جلوبال"

Ceramic detection aliases (map to service intent CERAMIC_COATING):
- "ceramic", "ceramic coating", "coating", "nano ceramic", "سيراميك", "سيراميك كوتنغ", "نانو"

Graphene detection aliases (map to service intent GRAPHENE_COATING):
- "graphene", "جرافين"

Tint detection aliases (map to service intent WINDOW_TINT):
- "tint", "window tint", "film tint", "sun control", "heat control", "rayban", "ray-ban", "تظليل", "عازل", "عازل حراري", "سولار", "حماية حرارية"

Polishing detection aliases (map to service intent PAINT_POLISHING):
- "polish", "polishing", "paint correction", "buffing", "compound", "cut and polish", "تلميع", "تلميع بوية", "تصحيح بوية", "بوليش"

Wrap detection aliases (map to service intent VEHICLE_WRAP):
- "wrap", "vinyl", "ppf color", "color wrap", "تغليف", "تلبيس", "فيلم لون", "راب"

---

## 3) PAINT PROTECTION FILM (PPF)

### GLOBAL SERIES
- GLOBAL_LUXE_5Y
- GLOBAL_ELITE_8Y
- GLOBAL_SIGNATURE_10Y
- GLOBAL_MATTE_10Y

### XPEL SERIES
- XPEL_EXO_7Y
- XPEL_UP_10Y
- XPEL_UP10_10Y
- XPEL_FUSION_10Y
- XPEL_STEALTH_10Y

### FRONT PPF PACKAGES
- PPF_FRONT_GLOBAL
- PPF_FRONT_XPEL

---

## 4) CERAMIC COATING

- CERAMIC_1Y
- CERAMIC_3Y
- CERAMIC_5Y

---

## 5) GRAPHENE COATING

- GRAPHENE_1Y
- GRAPHENE_3Y
- GRAPHENE_5Y

---

## 6) INTERIOR PROTECTION

- INTERIOR_CERAMIC

Naming constraints:
- Do NOT invent duration-based interior variants
- Do NOT create seat-specific ceramic names

---

## 7) WINDOW TINT

### TINT PRODUCTS
- TINT_NANO_CERAMIC
- TINT_XPEL_XR_PLUS

### COVERAGE OPTIONS
- TINT_WINDSHIELD_ONLY
- TINT_SIDES_BACK
- TINT_FULL_CAR
- TINT_FULL_WITH_SUNROOF

---

## 8) POLISHING

- POLISH_SILVER
- POLISH_GOLD

---

## 9) WRAP PRODUCTS

- WRAP_GLOSS
- WRAP_MATTE
- WRAP_SATIN
- ROOF_WRAP_BLACK

---

## 10) Engine Usage Rules (Critical)

Engines MAY:
- Refer to products ONLY using names in this registry
- Use tier-language ONLY when abstracted (e.g. “one step down”)

Engines MAY NOT:
- Invent new product names
- Modify durability years
- Create new series or editions
- Rebrand existing products

If an alternative is required:
- Engine must request Ladder Engine output
- Engine must NOT invent fallback names

---

## 11) Governance & Change Control

- This registry is READ-ONLY
- Any addition or change requires:
  - Phase 0 unlock
  - Version bump
  - Explicit approval

---

END OF DOCUMENT