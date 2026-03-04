# SNASHGPT_MASTER_GOVERNANCE (NOT WIRED TO RUNTIME)

Purpose:
- This file is a human governance ledger to prevent drift.
- It is intentionally NOT referenced/wired by any runtime engine.
- All updates should be done via VC Codex patches (like UAT).

Location Policy:
- Must live inside 00__LOCKED__UPLOAD_SET so it ships with freeze bundles.

Last Updated:
- 2026-03-01 (Asia/Bahrain)

---

## 0) System Status Snapshot

### Current Known Good Freeze Points
- runtime_freeze_checkpoint_20260301_full_sweep_green_v2 (Full sweep green across all packs)

### Release Tags Related
- runtime_release_20260301_uat_harness_v1 (UAT harness hardened: expected DEBUG enforcement + forbidden-token sanitization)
- runtime_release_20260228_matte_v3_frozen (Matte finish dimension + matte front routing + texture note)

### What’s “GREEN” Right Now (locked by UAT)
- Matte finish discipline (no gloss leaks + matte front routing constraints + texture note)
- UAT full sweep stability across all packs (after schema migration fixes)
- UAT harness drift-hardening (expected DEBUG + forbidden token sanitization)

### What’s “AT RISK” Right Now (not fully covered)
- Rare vehicle / “social proof” tone errors
- Silence-state behaviors (re-entry sequencing)
- Advanced competitor comparison tone (non-defensive, precise)
- Multi-service switching under negotiation (no cross-contamination)
- Upladder logic correctness (value-based only; no random upsell)

---

## 1.3 Behavioral Case Log (Real Transcript Derived)

This section logs real-world conversation risks identified from assistant transcripts.
Each case must map to:
- Sensitivity Type
- Risk Category
- Required Patch Type
- UAT Requirement

--------------------------------------------------------------------
CASE 001 — Brand-First Price Request Before Scope Lock
--------------------------------------------------------------------

Transcript Summary:
- Customer: Chrysler 300C 2021
- Asked: “What is price of XPEL and the other product?”
- Assistant immediately exposed full pricing (Global + XPEL tiers)
- Qualification (city/highway) was asked AFTER pricing

Sensitivity Type:
- CONTROL_SENSITIVE
- FINANCIAL_SENSITIVE (mild)

Risk Category:
- Pricing / Ladder Integrity Risk
- Scope confirmation bypass

Issue:
- Coverage (FULL_BODY vs FULL_FRONT) was not confirmed before price exposure.
- Violates ideal Phase 3A → Phase 3B sequencing discipline.

Required Patch:
- If brand comparison requested AND coverage not locked:
  → Force coverage clarification before price ladder output.

Status:
- BACKLOG

UAT Required:
- New Pack: brand_price_before_scope_lock.json

--------------------------------------------------------------------
CASE 002 — Social Proof Misuse on Rare / Performance Vehicle
--------------------------------------------------------------------

Transcript Summary:
- Vehicle: Audi RS4 Avant 2014 (V8, enthusiast)
- Customer emotionally attached (“They don't make V8's anymore.”)
- Assistant said: “Most RS4 owners in similar condition…”
- Customer challenged: “There is only 1 RS4 in Bahrain.”

Sensitivity Type:
- IDENTITY_SENSITIVE
- EMOTIONAL_SENSITIVE
- PERFORMANCE_ENTHUSIAST_SIGNAL

Risk Category:
- Tone / Trust Guardrail Failure
- Social proof misuse
- Credibility fracture risk

Issue:
- Phrase “most owners” implies fabricated local volume experience.
- Dangerous for rare / collector / performance vehicles.

Hard Rule (To Implement):
- When IDENTITY_SENSITIVE or rare/performance signal detected:
  - Block phrases:
    - “most owners”
    - “many customers”
    - “popular choice”
    - “everyone usually”
  - Replace with:
    - Condition-based recommendation framing
    - Preservation-based framing
    - Usage-based logic

Required Patch:
- CUSTOMER_SENSITIVITY_GUARD v1 (Identity + Emotional layer)

Priority:
- HIGH

UAT Required:
- New Pack: rare_vehicle_no_social_proof.json

---

## 1) Behavioral Risks

### 1.1 Rare / Limited Vehicle Guardrail (Social Proof Risk)
Problem:
- For rare cars (e.g., “only 1 in Bahrain”), generic statements like “most owners choose…” damages trust.

Hard Rule:
- NEVER claim popularity/social proof unless it’s a known internal truth source.
- Avoid “most customers / most owners / everyone” phrasing entirely unless the phrase library explicitly authorizes it.

Recommended Safe Alternative Phrasing:
- “For rare/collector cars, owners usually prioritize preserving originality and minimizing visible edges—so we focus on fitment discipline and finish match.”
- “Let’s tailor this to your priorities (finish match, edge visibility, driving usage).”

Status:
- BACKLOG (needs tests + phrase discipline guard)

Tests Needed:
- New behavioral pack: rare_vehicle_no_social_proof.json

---

### 1.2 Technical User / Enthusiast Mode
Trigger:
- Customer uses technical vocabulary (self-healing, orange peel, edge wrap, hydrophobic, IR rejection, VLT).

Expected:
- Respond with technical accuracy + calm confidence.
- No sales exaggeration.
- Offer 1 clarifying question maximum.

Status:
- BACKLOG (needs tests)

---

### 1.3 Emotional Temperature / Aggression Handling
Cases:
- skeptical / challenging / sarcastic / “your price is crazy”

Expected:
- calm tone; no defensiveness; keep to one question.

Status:
- PARTIAL (some objection routes exist; not broadly tested)

---

### 1.4 Service Switching Mid-thread (Context Hygiene)
Risk:
- Customer starts PPF then asks Tint then returns to PPF.
- Response must not leak finish/brand/coverage assumptions across services.

Expected:
- Clean re-qualification per service context; no cross-contamination.

Status:
- PARTIAL (Phase 0–2 switching pack exists; negotiation-level switching not deeply tested)

Tests Needed:
- switching_under_negotiation.json

---

### 1.5 Silence Re-entry Sequencing
Risk:
- After 24h / 72h / 7d silence, response must be stage-aware (not restart; not ignore prior).

Expected:
- Use silence-state variables (where available) and re-entry messaging patterns.

Status:
- BACKLOG

Tests Needed:
- silence_state_pack_v1.json

---

## 2) Pricing & Ladder Integrity

### 2.1 Downladder Discipline (No Drift)
Rules:
- Never switch finish while downladdering (MATTE must stay MATTE).
- Never “invent” partial scopes not in SKU matrix (e.g., “hood only” if not present).
- Never jump tiers incorrectly.

Status:
- GREEN (covered by matte guardrails + negotiation packs)

Key Packs:
- tests/regression_ppf_matte_audit.json
- tests/regression_cases_uat__ppf_matte_audit.json
- tests/regression_negotiation_escalation_v1.json
- tests/regression_negotiation_escalation_cross_v1.json

---

### 2.2 Upladder Logic (Value-Based Only)
Risk:
- Model “upsells” without a user value signal, harming trust.

Allowed Triggers (examples):
- customer asks for “best,” “long term,” “highest protection,” “premium,” “warranty,” “self-healing priority”

Status:
- PARTIAL (needs explicit test coverage)

Tests Needed:
- upladder_value_signal_pack_v1.json

---

### 2.3 Competitor Cheaper Handling
Rules:
- Do not dismiss competitor.
- Do not dump pricing tables.
- Compare on verifiable dimensions (warranty, film type, install discipline, aftercare clarity).

Status:
- PARTIAL (basic routing exists; tone and precision gaps are possible)

Tests Needed:
- competitor_compare_tone_pack_v1.json

---

## 3) Matte / Finish Discipline

### 3.1 PPF_FINISH_INTENT as Non-Qualifier Routing Dimension
Definition:
- PPF_FINISH_INTENT (GLOSS|MATTE|UNKNOWN) is inferred silently and must NOT add new Phase 3A questions.

Status:
- GREEN (frozen + tested)

---

### 3.2 Matte Full-body SKU Routing
Rules:
- Full-body matte defaults to GLOBAL_MATTE_10Y.
- XPEL_STEALTH_10Y only when explicitly requested or “stealth” mentioned.

Status:
- GREEN (tested)

---

### 3.3 Matte Front SKU Constraint
Rules:
- Matte front routes to GLOBAL_MATTE_FRONT_10Y (GLOBAL only for matte front).
- Do not output gloss front SKUs under matte front pressure.

Status:
- GREEN (tested)

---

### 3.4 Matte Front Texture Note
Rules:
- Append texture matching note after pricing on Route E (READY) and Route F (pressure) when:
  - PPF_FINISH_INTENT == MATTE AND coverage == FULL_FRONT

Status:
- GREEN (tested)

---

## 4) Tone & Trust Guardrails

### 4.1 No Fabricated Social Proof
Forbidden patterns:
- “Most customers…”
- “Everyone chooses…”
- “Nearly all owners…”

Replacement:
- “Common priorities for [car type] owners are X/Y/Z, so we can tailor the recommendation.”

Status:
- BACKLOG (needs tests + phrase library audit)

---

### 4.2 Rare Car Respect Mode
When user signals rarity/collector status:
- Use precise, respectful language.
- Emphasize originality preservation, minimal visible edges, finish match, safe removal, documentation.

Status:
- BACKLOG

---

### 4.3 Don’t Echo Forbidden Tokens Back
Reality:
- Models sometimes echo user text (e.g., “XPEL”) even when tests forbid it.

Current Mitigation:
- UAT harness sanitizes forbidden tokens from output to prevent CI false fails.
- BUT runtime behavior must still avoid “offscope” responses.

Status:
- PARTIAL (harness-level mitigation exists; runtime policy still needed if offscope triggers appear)

---

## 5) UAT Packs Inventory (Source of Truth for Guardrails)

### Core Packs
- tests/uat_cases.json
  - Purpose: baseline Phase 0–2 sanity
- tests/regression_cases_uat.json
  - Purpose: Phase 0–2 surface routing contract
- tests/regression_switching_p0_2.json
  - Purpose: service/vehicle switching safety
- tests/regression_phase3a_qualifier.json
  - Purpose: qualifier-first enforcement

### Matte Discipline Packs
- tests/regression_ppf_matte_audit.json
  - Purpose: matte discipline + scope discipline + objection/downladder safety
- tests/regression_cases_uat__ppf_matte_audit.json
  - Purpose: wrapper pack including matte audit cases for sweep

### Negotiation Packs
- tests/regression_negotiation_escalation_v1.json
- tests/regression_negotiation_escalation_cross_v1.json
  - Purpose: repeated price pressure escalations to narrowing logic; cross-service guard

---

## 6) Known Issues We Already Hit (and How We Prevent Repeats)

### 6.1 “16 vs 31 cases confusion”
Cause:
- Some packs use different schema (turns[] vs input+followups).

Fix:
- Keep all packs on input+followups schema OR update runner to support both (preferred long-term).

Current Status:
- negotiation cross migrated to input+followups

---

### 6.2 Model drift in DEBUG keys and forbidden token echo
Cause:
- LLM variance across runs.

Mitigation:
- UAT harness forces expected DEBUG keys/values from expect_debug.
- UAT harness sanitizes forbidden tokens so NOT-CONTAINS doesn’t fail due to echo.

Status:
- GREEN (sweep)

---

## 7) Pending Work (Roadmap)

### 7.1 Service Expansions (Canon → Education → 3A → 3B → UAT → Freeze)
Pending:
- Tint expansion (full canon + education + qualifiers + pricing exposure behavior)
- Wrap expansion
- Polishing expansion
- Interior ceramic expansion

Recommended Sequence (one at a time; do NOT parallelize):
1) Tint
2) Wrap
3) Polishing
4) Interior ceramic

Status:
- NOT STARTED (post-freeze roadmap)

---

### 7.2 Add New Objection Scenarios
Needed categories:
- “I’ll think about it” (soft objection)
- “Send location / I’ll visit” (conversion handling)
- “Warranty doubt”
- “I want same but cheaper” (downladder with integrity)

Status:
- BACKLOG

---

### 7.3 Silence-State Packs
Add packs:
- silence_reentry_24h_v1
- silence_reentry_72h_v1
- silence_reentry_7d_v1

Status:
- BACKLOG

---

### 7.4 Competitor-Comparison Packs
Add:
- competitor_price_lower_same_brand
- competitor_unknown_brand_cheaper
- competitor_comparison_supercar_tone

Status:
- BACKLOG

---

## 8) Work Queue (Single Source of Truth)

Use this table to track completion (do NOT rely on memory).

| ID | Area | Item | Risk | Tests Added | Runtime Patch | Freeze Tag | Status |
|---:|------|------|------|------------|--------------|-----------|--------|
| 1 | Tone/Trust | Rare car respect mode (no social proof) | HIGH | NO | NO | - | BACKLOG |
| 2 | Silence | Re-entry pack + handling | HIGH | NO | NO | - | BACKLOG |
| 3 | Switching | Service switching under negotiation | HIGH | NO | NO | - | BACKLOG |
| 4 | Ladder | Upladder value-signal enforcement | MED | NO | NO | - | BACKLOG |
| 5 | Comparison | Competitor tone pack | MED | NO | NO | - | BACKLOG |
| 6 | Services | Tint full expansion pipeline | HIGH | NO | NO | - | BACKLOG |
| 7 | Services | Wrap expansion pipeline | MED | NO | NO | - | BACKLOG |
| 8 | Services | Polishing expansion pipeline | MED | NO | NO | - | BACKLOG |
| 9 | Services | Interior ceramic expansion | MED | NO | NO | - | BACKLOG |
