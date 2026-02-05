────────────────────────────────────────────────────────────
PHASE 0–4 — REQUIRED HUMAN PHRASE BLOCKS (SCOPE ONLY — LOCKED)
────────────────────────────────────────────────────────────

Purpose:
This section defines the COMPLETE and FINAL list of human-facing
phrase blocks that MUST exist before rollout.

This section defines SCOPE ONLY.
No wording is defined here.
No engine logic is defined here.

Once locked:
- No new phrase categories may be added
- No categories may be removed
- Only wording refinement is allowed later

────────────────────────────────────────────
PHASE 0–2 (INTAKE / EARLY FRAMING)
────────────────────────────────────────────

- Neutral service explanation (PPF)
- Neutral service explanation (Ceramic)
- Neutral service explanation (Graphene)
- Neutral service explanation (Polishing)
- Brand mention acknowledgment (XPEL / Global) — non-comparative
- Minimum qualifier question phrasing (vehicle / usage / washing)
- Soft redirection phrasing (fit mismatch, no correction)

────────────────────────────────────────────
PHASE 3A (PRE-PRICE — VALUE & DIRECTION)
────────────────────────────────────────────

- PPF analogy block (screen protector / impact protection)
- Ceramic analogy block (paint care / maintenance simplification)
- Graphene uplift explanation (durability framing only)
- City vs Highway usage framing (non-technical)
- Matte finish explanation (generic, brand-agnostic)
- Brand-explicit reassurance phrasing (only if requested)

────────────────────────────────────────────
PHASE 3B (SELECTION CONFIRMATION — NO PRICING)
────────────────────────────────────────────

- “Why these two options” justification phrasing
- Default vs Second option comparison phrasing
- Upladder explanation phrasing (no pressure)
- Downladder explanation phrasing (cost-conscious)
- Service switch confirmation phrasing (PPF ↔ Ceramic)

────────────────────────────────────────────
PHASE 4 (PRICE DELIVERY & POST-PRICE CONTROL)
────────────────────────────────────────────

- Pre-price value bridge (generic)
- Pre-price value bridge (PPF-specific)
- Pre-price value bridge (Ceramic / Graphene-specific)
- Controlled price presentation phrasing
- Post-price reassurance phrasing
- Sticker-shock stabilization phrasing
- Price loop boundary phrasing
- Escalation / inspection invitation phrasing

────────────────────────────────────────────
GLOBAL RULES (ALL PHASES)
────────────────────────────────────────────

- SKU IDs are NEVER customer-facing
- All product facts must defer to GLOBAL_PRODUCT_NAMING_REGISTRY
- Education depth is gated by customer signal
- No feature wars, no competitor defense
- No new phrase categories beyond this list

────────────────────────────────────────────
END — PHRASE SCOPE LOCK
────────────────────────────────────────────
# SNASHGPT_PHASE0–4_ROLLOUT_SOURCE_OF_TRUTH.md

Status: ACTIVE — AUTHORITATIVE  
Purpose: Single checklist & control document for Phase 0–4 rollout  
Rule: No work proceeds unless aligned with this file

────────────────────────────────────────────
SECTION A — WHAT IS COMPLETED (LOCKED)
────────────────────────────────────────────

A1. Phase 0–2 Intake & Qualification
Status: ✅ COMPLETED & LOCKED

- CUSTOMER_CHAT_INTAKE_RULES.md finalized
- Numeric-only model guard implemented (e.g., "Jetour 52")
- Clarification minimization rules applied
- No re-qualification loops
- Brand mentions handled safely (XPEL → intent only)
- Vehicle repo + alias handling confirmed

Authoritative files:
- CUSTOMER_CHAT_INTAKE_RULES.md
- QUALIFICATION_ENGINE.md
- GLOBAL_VEHICLE_CLASSIFICATION_REPOSITORY.md

No further changes allowed unless regression is found.


A2. Phase 3A — Readiness & Gating (PPF / Non-PPF)
Status: ✅ COMPLETED & LOCKED

- PPF readiness gates enforced
- No price ladder execution without readiness
- Paint condition / age gates respected
- Service interest ≠ final recommendation (correct)

Authoritative files:
- QUALIFICATION_DECISION_MATRIX.md
- PHASE3_LOCK_INDEX.md
- PHASE3_ORCHESTRATION_WIRING_ADDENDUM.md


A3. Phase 3B — SKU-True Selection Rules (Structure)
Status: ✅ COMPLETED (LOGIC), ❌ SKU ORDERING MOVED OUT

- Rule: Phase 3B selects SKUs, no education prose
- No SKU invention
- One service per ladder run
- Brand mention is modifier only
- Coverage selectors controlled

Authoritative file:
- PHASE3B selection logic inside PRICE_LADDER_ENGINE.md

NOTE:
SKU *ordering* is intentionally REMOVED from engines.
It must live only in a data matrix (see Section C).


A4. Phase 4 — Human Phrasing (Pre-Price)
Status: ✅ COMPLETED & LOCKED

- Natural education phrases for:
  - PPF vs Ceramic
  - Ceramic baseline
  - PPF baseline
- Analogies locked:
  - PPF → screen protector / peace of mind
  - Ceramic → skincare / keeps car looking new
- Washing pattern question for ceramic
- Highway vs city question for PPF
- No pricing language leakage

Authoritative file:
- PHASE4_6_HUMAN_PHRASE_LIBRARY.md

No pricing logic inside phrases.


A5. Negotiation / Objection / Silence Handling
Status: ✅ COMPLETED & LOCKED

- NEGOTIATION_LOGIC_MODULE.md is NOT a pricing engine
- Handles:
  - price loops
  - sticker shock
  - competitor signals
  - silence recovery
- Uses anchors only AFTER price exposure
- No SKU logic, no pricing math

Authoritative file:
- NEGOTIATION_LOGIC_MODULE.md

No changes required.


────────────────────────────────────────────
SECTION B — WHAT IS IN PROGRESS (ACTIVE)
────────────────────────────────────────────

B1. SKU Ordering Logic (PPF / Ceramic / Graphene / Polishing)
Status: 🟡 IN PROGRESS — MUST BE CENTRALIZED

Problem identified:
- SKU ordering (default / second / upladder / downladder)
  is currently implicit and causing drift.

Decision (LOCKED):
- SKU ordering must exist in ONE place only
- Engines must READ, not decide

This applies to:
- PPF (segment + driving + brand + age)
- Ceramic (age + wash pattern)
- Graphene (age)
- Polishing (paint condition + age)

No engine will contain ordering rules.


────────────────────────────────────────────
SECTION C — WHAT MUST BE CREATED (NEXT)
────────────────────────────────────────────

C1. SKU_SELECTION_MATRIX.md
Status: ❌ NOT CREATED (NEXT STEP)

This file becomes the ONLY authority for:
- Which SKUs appear
- In what order
- Under what conditions

It MUST contain tables for:

PPF:
- Inputs:
  - VEHICLE_CLASS_BAND (VCB_1 / VCB_2 / VCB_3)
  - DRIVING_PATTERN (CITY / HIGHWAY)
  - BRAND_INTENT (NONE / XPEL)
  - VEHICLE_AGE_BAND (if applicable)
- Outputs:
  - Default SKU
  - Second SKU
  - Upladder SKU
  - Downladder SKU

Ceramic / Graphene:
- Inputs:
  - VEHICLE_AGE_BAND
  - WASH_PATTERN
- Outputs:
  - Default / Second / Upladder / Downladder

Polishing:
- Inputs:
  - VEHICLE_AGE_BAND
  - PAINT_CONDITION
- Outputs:
  - Allowed SKUs only

Rules:
- No prices
- No phrases
- No logic duplication
- SKU names must match GLOBAL_PRODUCT_NAMING_REGISTRY_v1.0.md exactly


C2. PRICE_TABLE_VAT_INCL.md
Status: 🟡 PARTIALLY AVAILABLE (NEEDS STRUCTURE)

Purpose:
- Map SKU → price per VCB
- VAT inclusive
- Base price for future discount/bundle engines

Rules:
- No logic
- No ordering
- No conditions
- Pure data table

Engines only READ from this file.


────────────────────────────────────────────
SECTION D — WHAT WILL HAPPEN AFTER
────────────────────────────────────────────

D1. Price Ladder Engine Wiring
Status: ⏳ PENDING

Once C1 + C2 are complete:
- PRICE_LADDER_ENGINE.md will:
  - Read SKU_SELECTION_MATRIX.md
  - Read PRICE_TABLE_VAT_INCL.md
  - Apply existing gating rules
- No new logic added

D2. Auto Price Pickup
Status: ⏳ PENDING

- Deterministic
- No improvisation
- No phrase changes required


## DEFERRED / LATER-PHASE ITEMS (ACKNOWLEDGED, NOT LOST)

- [DEFERRED] WhatsApp number capture
  - Triggered ONLY post-price or at closing intent
  - Optional, convenience-framed (never forced)
  - Implemented via Phase 4 overlay → Stage 7 handoff
  - Phrase authority: PHASE4_6_HUMAN_PHRASE_LIBRARY
  - Decision authority: DECISION_MATRIX / CLOSING_HANDOVER_ENGINE

- [DEFERRED] Visit request / inspection invitation
  - Triggered after pricing or when proof/reassurance is requested
  - Never pre-price
  - Phrase authority: PHASE4_6_HUMAN_PHRASE_LIBRARY
  - Routing authority: PHASE4_8_MESSAGE_ASSEMBLY_MAP


────────────────────────────────────────────
SECTION E — ROLLOUT CRITERIA
────────────────────────────────────────────

Phase 0–4 is READY FOR ROLLOUT when:
- [ ] SKU_SELECTION_MATRIX.md is finalized
- [ ] PRICE_TABLE_VAT_INCL.md is finalized
- [ ] Regression tests pass for:
      - PPF city vs highway
      - XPEL vs default
      - Service switch after price
      - Price loop handling

Until then:
❌ No new phrases
❌ No new engines
❌ No refactoring


────────────────────────────────────────────
END OF FILE
────────────────────────────────────────────