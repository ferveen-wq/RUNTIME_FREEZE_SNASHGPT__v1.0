# PHASE3A_QUALIFICATION_DECISION_MATRIX.md
# LOCK_METADATA
# LOCK_STATUS: LOCKED
# LOCK_SCOPE: PHASE 3A - Decision Matrix (qualifier order + gating logic)
# LOCK_DATE: 2026-02-09
# LOCK_REASON: Phase 3A UAT passed; prevent qualifier drift or reordering
# CHANGE_CONTROL: Architecture approval required
#
# Role:
# - Phase 3A runs AFTER Phase 0–2 is complete (service_intent + vehicle_model + vehicle_year are known).
# - Phase 3A is a mini-consultation: collect just enough inputs to make Phase 3B pricing feel logical.
# - One question per assistant turn (max). No pricing in Phase 3A.
#
# Hard rules:
# - Max 1 question per turn.
# - If user ignores the current qualifier and pushes price / changes topic:
#   - Nudge once (why we ask) + repeat SAME qualifier.
#   - If still not answered: set UNKNOWN and proceed to Phase 3B safely.
#
# Dependencies:
# - GLOBAL_CORE_CONTEXT_PARAMETERS.md (canonical parameter names + allowed values)
# - PHASE6__SERVICE_CANON_BUNDLE.md (service definitions; no invented services)
# - GLOBAL_PRODUCT_NAMING_REGISTRY_v1.0.md (only approved product names)
#

────────────────────────────────────────────────────────────
3A.0 GLOBAL SEQUENCING - VEHICLE_AGE_BUCKET (HARD)
────────────────────────────────────────────────────────────

PAINT CONDITION GATE PARAM:
- PAINT_CONDITION_GATE ∈ {CLEAR, REQUIRES_REVIEW, UNKNOWN}

AGE_7_PLUS_YEARS:
- Ask PAINT_CONDITION_GATE FIRST (repaint/deep scratches).
- If REQUIRES_REVIEW → proceed to Phase 3B with constrained posture (no confident prep claims).
- If CLEAR → proceed to service qualifiers.

AGE_0_3_YEARS / AGE_3_6_YEARS:
- No forced paint gate first unless customer mentions repaint/deep scratches.

PAINT CONDITION GATE QUESTION (one question):
- "Before we guide the price, is there any repaint work or deep scratches on the panels?"

Normalization (strict):
- YES patterns → REQUIRES_REVIEW
- NO patterns → CLEAR
- Otherwise → UNKNOWN

────────────────────────────────────────────────────────────
3A.1 PPF - MINI-CONSULTATION (BENCHMARK BEHAVIOR)
────────────────────────────────────────────────────────────

PPF qualifiers (max 2 core + 1 conditional):
Q1) Coverage intent (PRIMARY)
Q2) Driving pattern (SECOND)
Q3) Comparison focus (CONDITIONAL only if price/competitor pressure)

Q1 - PPF_COVERAGE_INTENT (required before pricing posture)
Allowed values:
- FULL_BODY
- FULL_FRONT
- PARTIAL_OR_CUSTOM
- UNSURE

Ask (one question):
- "To guide you properly for PPF, would you prefer maximum protection for the whole car, a more practical protection focused on the front impact areas, or are you still deciding?"

Normalize:
- "full / كامل" → FULL_BODY
- "front / front only / قدام / أمامي" → FULL_FRONT
- custom panels list → PARTIAL_OR_CUSTOM
- otherwise → UNSURE (or UNKNOWN if totally unclear)

Fallback:
- One nudge max, then set UNSURE and proceed.

Q2 - PPF_DRIVING_PATTERN
Allowed values:
- CITY
- HIGHWAY
- MIXED
- UNKNOWN

Ask (one question):
- "Is your driving mostly highway/travel (more stone chips), or mostly city (more parking/contact)?"

Fallback:
- One nudge max, then UNKNOWN and proceed.

Q3 - PPF_COMPARISON_FOCUS (only if triggered)
Trigger if ANY:
- repeated "how much"
- competitor cheaper / quote mention
- film thickness / brand fixation

Allowed values:
- COVERAGE
- FILM_QUALITY
- HEADLINE_PRICE
- MIXED
- UNKNOWN

Ask (one question):
- "When you compare, is it mainly about coverage, film quality, or headline price?"

If "all" → MIXED.

Phase 3B READY for PPF when:
- PPF_COVERAGE_INTENT is known (or UNSURE)
- PPF_DRIVING_PATTERN is known (or UNKNOWN)

────────────────────────────────────────────────────────────
3A.2 CERAMIC - MAINTENANCE-OUTCOME LED
────────────────────────────────────────────────────────────

CERAMIC qualifiers:
Q1) CERAMIC_GOAL (PRIMARY)
Q2) CERAMIC_WASH_PATTERN (SECOND)

Q1 - CERAMIC_GOAL
Allowed values:
- EASY_CLEAN_LONG_TERM
- LOOKS_FRESH_SHORT_TERM
- UNKNOWN

Ask (one question):
- "For ceramic, is your main goal long-term gloss and easier maintenance, or mainly to refresh the look for now?"

Immediately after Q1 (spec note for phrasing layer, not pricing):
- Mention "6-month refresh approach" ONLY as a maintenance concept,
  and ONLY because it is a canonical service add-on (see Service Canon patch).

Fallback:
- One nudge max, then UNKNOWN and proceed.

Q2 - CERAMIC_WASH_PATTERN
Allowed values:
- BUCKET_LOCALITY
- AUTO_TUNNEL
- WATERLESS_MALL
- PRO_WASH_CENTER
- MIXED
- UNKNOWN

Ask (one question):
- "How do you usually wash - bucket/hand wash, tunnel/automatic, mall waterless, wash center, or mixed?"

Phase 3B READY for CERAMIC when:
- CERAMIC_GOAL known (or UNKNOWN)
- CERAMIC_WASH_PATTERN known (or UNKNOWN)

────────────────────────────────────────────────────────────
3A.3 TINT - OUTCOME FIRST, THEN COVERAGE
────────────────────────────────────────────────────────────

TINT qualifiers:
Q1) TINT_GOAL (PRIMARY)
Q2) TINT_COVERAGE (REQUIRED for pricing)

Q1 - TINT_GOAL
Allowed values:
- HEAT_COMFORT
- PRIVACY
- MIXED
- UNKNOWN

Ask (one question):
- "For tint, is your main goal heat comfort, privacy, or both?"

Fallback:
- One nudge max, then UNKNOWN and proceed to coverage.

Q2 - TINT_COVERAGE
Allowed values:
- FRONT_ONLY
- SIDES_REAR
- FULL
- UNKNOWN

Ask (one question):
- "For tint coverage, do you want front only, sides and back, or full?"

Phase 3B READY for TINT when:
- TINT_COVERAGE known (or UNKNOWN)


────────────────────────────────────────────────────────────
3A.4 WRAP - FINISH FIRST, THEN SCOPE
────────────────────────────────────────────────────────────

WRAP qualifiers:
Q1) WRAP_FINISH (PRIMARY)
Q2) WRAP_SCOPE (REQUIRED for pricing)

Q1 - WRAP_FINISH
Allowed values:
- GLOSS
- SATIN
- MATTE
- UNKNOWN

Ask (one question):
- "For wrap, which finish are you leaning toward - gloss, satin, or matte?"

Fallback:
- One nudge max, then UNKNOWN and proceed to scope.

Q2 - WRAP_SCOPE
Allowed values:
- FULL_COLOR_CHANGE
- PARTIAL_AREA
- UNKNOWN

Ask (one question):
- "Are you thinking a full color-change wrap, or only a specific area?"

Phase 3B READY for WRAP when:
- WRAP_SCOPE known (or UNKNOWN)

────────────────────────────────────────────────────────────
3A.5 POLISHING - SCOPE FIRST, THEN PAINT HISTORY
────────────────────────────────────────────────────────────

POLISHING qualifiers:
Q1) POLISHING_SCOPE (PRIMARY)
Q2) PAINT_CONDITION_REPAINT_SCRATCH (SECOND)

Q1 - POLISHING_SCOPE
Allowed values:
- EXTERIOR_ONLY
- FULL_DETAILING
- UNKNOWN

Ask (one question):
- "For polishing, are you looking for exterior paint correction only, or full detailing including interior and engine bay?"

Fallback:
- One nudge max, then UNKNOWN and proceed.

Q2 - PAINT_CONDITION_REPAINT_SCRATCH
Allowed values:
- YES
- NO
- UNKNOWN

Ask (one question):
- "Before we proceed, has the car had any repaint work or deep scratches?"

Phase 3B READY for POLISHING when:
- POLISHING_SCOPE known (or UNKNOWN)
- PAINT_CONDITION_REPAINT_SCRATCH known (or UNKNOWN)

────────────────────────────────────────────────────────────
END

