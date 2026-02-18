────────────────────────────────────────────────────────────
WRAP (FULL VEHICLE) — PHASE 3A GATE (LOCKED)
────────────────────────────────────────────────────────────
Trigger:
- service_intent == wrap

Hard rules:
- WRAP Phase 3A asks FINISH ONLY (no scope questions).
- Do NOT ask/route PHASE3A_Q_WRAP_SCOPE.

Decision:
- If WRAP_FINISH is missing or UNKNOWN:
	- phase3a_required = true
	- phase3a_qualifier_id = PHASE3A_Q_WRAP_FINISH
	- phase3a_complete = false
- Else:
	- phase3a_required = true
	- phase3a_qualifier_id = null
	- phase3a_complete = true

Downstream eligibility:
- If phase3a_complete == true AND request_type == PRICE_REQUEST:
	- allow PRICE_LADDER_ENGINE to compute PHASE3B_WRAP_RANGE (FULL wrap only)

────────────────────────────────────────────────────────────
ROOF BLACK (PPF) — PHASE 3A OVERRIDE (LOCKED — REPO SAFE)
────────────────────────────────────────────────────────────
Trigger:
- detected_product_sku == ROOF_PPF_BLACK_GLOSS
  OR product_alias_route == ROOF_PPF_BLACK_GLOSS

Hard rules:
- This is NOT a WRAP product.
- Do NOT run PPF Phase 3A chain (coverage/driving/comparison).
- Model/year remains the only gating detail before pricing.

Decision:
- force service_intent = ppf
- set PPF_COVERAGE_INTENT = ROOF_ONLY
- phase3a_required = true
- phase3a_qualifier_id = null
- phase3a_complete = true

Downstream eligibility:
- If request_type == PRICE_REQUEST:
	- output range using ROOF_PPF_BLACK_GLOSS (single-SKU min=max)
