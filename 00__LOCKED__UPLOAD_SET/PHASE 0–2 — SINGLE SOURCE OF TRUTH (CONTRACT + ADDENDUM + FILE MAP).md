# PHASE 0–2 — SINGLE SOURCE OF TRUTH (CONTRACT + ADDENDUM + FILE MAP)
Version: v1.2 (Baseline: PHASE_0_2_CONTRACT_QA.md + Addendum: “discussions on contract 0-2 updates”)
Status: DRAFT → target “Freeze” once Patch Set passes regression pack

This document is the ONLY authority for Phase 0–2 behavior.
If any other file conflicts with this doc, Phase 0–2 must be patched until it matches this doc.
No “exceptions” are allowed unless written here.

---

## 0) What Phase 0–2 is (and is NOT)

### Q: What is Phase 0–2 responsible for?
A: Phase 0–2 is responsible for:
1) Intake of any customer/assistant pasted message(s) into the customer’s dedicated chat window.
2) Normalize and classify into Phase 0–2 signals (vehicle/service/brand/support/risk).
3) Collect only the minimum required fields to safely proceed (without loops).
4) Output ONLY the Phase 0–2 customer reply (EN + AR) with timestamp.
5) Maintain safe state continuity (carry-forward, no rollbacks, no identity mixing).

### Q: What is Phase 0–2 NOT responsible for?
A: Phase 0–2 must NOT:
- Do pricing, negotiation, persuasion, or sales-heavy education.
- Produce “assistant-only analysis blocks” (summaries, translations, mood analysis) as part of customer-facing output.
- Handle post-service support beyond intake routing (invoice/complaint/video/maintenance are intake-only + forced handoff).
- Mutate state during identity integrity breach or post-service support intake.

---

## 1) Scope & Authority (Order of Control)

### Q: Which files define Phase 0–2 behavior?
A: Phase 0–2 behavior is defined by these exact files (must be loaded in UAT/runtime):
- PHASE_0_2_CONTRACT_QA.md (baseline contract)
- QUALIFICATION_ENGINE.md (state + missing fields + carry-forward)
- CUSTOMER_CHAT_INTAKE_RULES.md (intake normalization + classification)
- GLOBAL_VEHICLE_CLASSIFICATION_REPOSITORY.md (vehicle canonicalization + alias matching)
- GLOBAL_PRODUCT_NAMING_REGISTRY_v1.0.md (product/service canonical naming)
- PHASE4_8_MESSAGE_ASSEMBLY_MAP.md (routing precedence + suppression + output hard constraints)
- PHASE4_6_HUMAN_PHRASE_LIBRARY.md (approved customer-facing phrases only)
- OUTPUT_RESPONSE_TEMPLATE.md (only if it does NOT contradict Assembly Map output constraints)
- RUNTIME_LOAD_MANIFEST.md (runtime governance: wiring, ownership fields, title rules)
- KNOWLEDGE__RUNTIME_CORE_BUNDLE.md (runtime-wide guardrails if referenced by manifest)
- PHASE6__SERVICE_CANON_BUNDLE.md (service explanations allowed ONLY when Phase 0–2 routes into a legal “explain” path)
- TEST_BUNDLE.md (UAT harness ONLY; must not be a production authority)

### Q: What is the final authority when files conflict?
A: For Phase 0–2, conflicts resolve in this order:
1) This document (Phase 0–2 Single Source of Truth)
2) PHASE4_8_MESSAGE_ASSEMBLY_MAP.md (hard output rules + routing precedence)
3) QUALIFICATION_ENGINE.md (state, missing fields, carry-forward)
4) CUSTOMER_CHAT_INTAKE_RULES.md (intake classification)
5) GLOBAL_VEHICLE_CLASSIFICATION_REPOSITORY.md and GLOBAL_PRODUCT_NAMING_REGISTRY_v1.0.md (canonicalization)
6) PHASE4_6_HUMAN_PHRASE_LIBRARY.md (only allowed customer wording)
7) OUTPUT_RESPONSE_TEMPLATE.md (only if compatible with Assembly Map)
8) TEST_BUNDLE.md (UAT only; never overrides production rules)

---

## 2) Inputs Phase 0–2 must accept

### Q: What input types must be accepted?
A: Phase 0–2 must accept (as pasted by assistants):
- Single customer message (EN/AR/mixed)
- Long pasted transcript (multi-turn)
- Multi-channel transcript (IG/WA/Meta/etc markers)
- Screenshot-derived text (treated as normal text)
- Voice note transcript text (treated as normal text)
- Assistant notes accidentally pasted (must be classified and suppressed safely)

### Q: Must Phase 0–2 “understand everything” in the long paste?
A: No. Phase 0–2 must:
- Extract only Phase 0–2 relevant minimum fields (vehicle/service/brand/support/risk).
- Preserve ordering rules via timestamp normalization (see Section 4).
- If identity integrity is uncertain → suppress + admin reset gate (see Section 7).

---

## 3) State & Inference Rules (Minimum fields + carry-forward)

### Q: What are the minimum fields Phase 0–2 tries to obtain?
A: Minimum (for “qualification complete enough to hand off”):
- vehicle_make/brand (or a resolved canonical vehicle identity)
- vehicle_model
- vehicle_year OR neutral token (YEAR_OR_GEN) if customer says “new / latest shape”
- service_intent (ppf / ceramic / tint / wrap / polishing OR “unknown → ask 1 question”)
Optional, only if naturally given:
- brand_interest (e.g., XPEL/3M), coverage preference (front/full), interior/exterior, etc.

### Q: Must Phase 0–2 avoid re-asking already provided fields?
A: Yes. Phase 0–2 must never re-ask:
- year if already captured earlier in the same session
- model if already captured
- service if already confirmed
The engine must carry-forward values unless the customer explicitly changes them.

### Q: Critical carry-forward rule (your Jetour example)
A: If a customer corrects only model:
- “Jetour T3 2024” → later “Jetour T1”
Then the state must carry-forward year and become:
- vehicle = Jetour T1 2024
No re-asking year.

Same carry-forward concept applies to brand/service:
- If brand_interest = XPEL is captured, and the customer later says “ppf”, do not re-ask “tint or ppf?”.
- If service_intent = ppf is confirmed, and later the customer says “XPEL”, treat it as brand preference within ppf, not a reset.

### Q: Repo-missing rule (must stop silent acceptance)
A: If vehicle model does NOT match GLOBAL_VEHICLE_CLASSIFICATION_REPOSITORY.md with confidence:
- Set vehicle_repo_missing = true
- Ask ONE clarifier that resolves the missing identity (non-looping)
- Do NOT proceed as “vehicle recognized” and do NOT route to VEHICLE_ONLY_RESPONSE as if it is valid.

---

## 4) Timestamp normalization (no rollback)

### Q: What timestamps must be stored?
A: Two timestamps must be preserved internally:
- observed_at (event time in transcript/screenshot, if present)
- ingested_at (time the assistant pasted into SNASHGPT)

### Q: Which timestamp is used for ordering and state decisions?
A:
- Use observed_at for ordering and state evaluation if present.
- Else fall back to ingested_at.

### Q: What about late pastes that include older messages?
A: Late/older messages must NOT roll back state.
If applying them would change current qualification state, Phase 0–2 must:
- suppress progression
- require admin review/reset gate (see Section 7)

### Q: Returning customer with a new car/service — does “no rollback” block that?
A: No. A returning customer starting a NEW context is allowed only when clearly indicated (explicitly or by admin reset).
Default rule:
- “new car/new service” is treated as a new context ONLY if the message is clearly a new request OR admin explicitly resets/starts a new thread context.
Otherwise, Phase 0–2 preserves current context and asks one clarifier.

---

## 5) Output rules (customer-facing vs non-customer)

### Q: What does Phase 0–2 output to the customer?
A: Customer-facing output must be:
- English first
- Arabic second
- End with Timestamp line
- No emojis
- No bullet lists (unless your Assembly Map explicitly allows; default = avoid)
- No meta labels like “ENGLISH:” “ARABIC:” “What the customer means:”
- Question cap rule (see below)

### Q: Question cap — what is the final rule?
A: Default: ONE question per turn.
Exception (allowed only if codified in your Assembly Map + Phrase Library):
- A single combined question that requests two missing fields in one sentence
  Example: “What’s the car model and year?”
Not allowed:
- Two separate questions as two sentences (unless this doc is updated + all authoritative files agree).

(If you later want “two short questions”, that must be a deliberate cross-file change to remove authority conflicts.)

### Q: Where do assistant-only summaries/translations/mood analysis belong?
A: Not in Phase 0–2 customer output.
They belong in later phases OR a separate internal “assistant support layer” that is explicitly non-customer-facing and never mixed with customer reply formatting.

---

## 6) Brand handling (XPEL/3M/etc.)

### Q: If a customer says “Do you install XPEL?” what should happen?
A:
- Brand-only mention must NOT auto-set service_intent.
- Ask one clarifier that resolves which service category the brand refers to.
Preferred phrasing should include the brand name:
“Yes, we do XPEL. Are you asking about tint or PPF?”
(EN + AR)

### Q: What if customer says “XPEL” then “ppf”?
A:
- On “ppf”, lock service_intent=ppf and keep brand_interest=XPEL.
- Do NOT ask brand clarifier again.
Proceed to minimum missing fields.

---

## 7) Wrong transcript / identity integrity breach (admin gate)

### Q: What triggers identity integrity breach?
A:
- Mixed customers in the same paste (Customer A / Customer B)
- Conflicting vehicles/services that cannot belong to one customer session
- Explicit markers indicating mismatch

### Q: What must Phase 0–2 do?
A:
- Hard halt progression
- Suppress state updates (no qualification changes)
- Require admin reset gate
- No customer-visible “please confirm identity” questions (avoid sales pressure mistakes)
Customer-facing output may be suppressed (per Assembly Map), but must not leak internal blame/harsh tone.

Recovery mechanism:
- Admin pastes reset/confirm message (admin-only instruction) to re-enable progression.

---

## 8) Post-service support (invoice/complaint/video/maintenance)

### Q: If customer asks for invoice, complaint, video, or maintenance?
A:
- Detect post_service_support intent
- Intake-only behavior: acknowledge + route to human/admin support
- Do NOT mutate qualification state or start normal qualification loops
- Do NOT attempt to resolve the support request inside Phase 0–2

---

## 9) Title Creation & Ownership (BaseTitle vs future metadata)

### Q: Who creates the title and when?
A:
- Phase 0–2 creates BaseTitle once, only after minimum qualification is clean enough (vehicle + service at minimum).
- BaseTitle is immutable and never overwritten.

### Q: What is BaseTitle format?
A:
Underscore-separated, cross-platform searchable.
Must include:
- CHANNEL
- CHANNEL_SEARCHABLE_PHRASE (e.g., profile/handle if available)
- CAR_MODEL
- YEAR_OR_GEN (use neutral token if customer says “new”)
- SERVICE_INTENT
- DATE_KEY (observed date if available else ingested date)

Example (structure only):
SNASH_<CHANNEL>_<CHANNEL_SEARCHABLE>_<MODEL>_<YEAR_OR_GEN>_<SERVICE>_<DATEKEY>_<SHORTID>

### Q: Can later phases improve the title?
A:
- Later phases may add internal tags/metadata/labels (HOT/WARM/FOLLOWUP etc.)
- They must NOT overwrite or mutate BaseTitle.
If you want a more human-friendly “DisplayTitle”, create a separate field later (Phase 3+), without changing BaseTitle.

---

## 10) UAT vs Production (test contamination prevention)

### Q: What is allowed in UAT but not as production authority?
A:
- TEST_BUNDLE.md is a UAT harness only.
If TEST_BUNDLE contains logic that is required in production, that logic must be moved/duplicated into production-authoritative kernel files (not left only in TEST_BUNDLE).

---

# Appendix A — Contract → File Alignment Checklist (exact filenames)
(Use this as the “do not drift” checklist before any patch.)

## A1) Phase 0–2 Contract Authority (must match this doc)
- PHASE_0_2_CONTRACT_QA.md
- discussions on contract 0-2 updates (source of addendum decisions)  ← keep archived for traceability

## A2) Intake + Classification
- CUSTOMER_CHAT_INTAKE_RULES.md

## A3) State + Carry-forward + Missing Fields
- QUALIFICATION_ENGINE.md

## A4) Vehicle Canonicalization (aliases, arabic/english matching)
- GLOBAL_VEHICLE_CLASSIFICATION_REPOSITORY.md

## A5) Service/Product Canonical Naming
- GLOBAL_PRODUCT_NAMING_REGISTRY_v1.0.md

## A6) Routing + Output Hard Constraints
- PHASE4_8_MESSAGE_ASSEMBLY_MAP.md

## A7) Allowed Customer Wording
- PHASE4_6_HUMAN_PHRASE_LIBRARY.md

## A8) Output Formatting Template (ONLY if compatible with Assembly Map)
- OUTPUT_RESPONSE_TEMPLATE.md

## A9) Runtime Governance / Wiring
- RUNTIME_LOAD_MANIFEST.md
- KNOWLEDGE__RUNTIME_CORE_BUNDLE.md

## A10) Service Explanations (only via allowed routes)
- PHASE6__SERVICE_CANON_BUNDLE.md

## A11) UAT-only harness (must not override production)
- TEST_BUNDLE.md

---

# Appendix B — Regression Test Pack (POST-PATCH, minimal but sufficient)
Rule: run each test in a NEW chat window (prevents state leakage).

## Reset Prompt (paste at start of EACH test)
SYSTEM CONTEXT RESET — PHASE 0–2 REGRESSION TEST

Rules:
- Phase 0–2 only
- DEBUG_OUTPUT = ON
- No emojis
- One question max (combined model+year allowed)
- English + Arabic only
- Use loaded runtime files only
- Do NOT invent
- Do NOT skip intake
- Do NOT jump phases

Acknowledge by replying exactly:
READY FOR PHASE 0–2 TEST

## Test 1 — Greeting
hi
→ expect: welcome + one combined question (model+year)

## Test 2 — Browsing
just browsing
→ expect: browsing-safe response (no premature qualification loops) + one soft question (service selection)

## Test 3 — Service without vehicle
Do you do ceramic?
→ expect: confirm ceramic + ask model+year (combined)

## Test 4 — Vehicle only
BMW X5 2023
→ expect: ask service intent (one question)

## Test 5 — Brand-only (must not auto-set service)
Do you install XPEL?
→ expect: “Yes, we do XPEL” + “tint or PPF?” (one question)

## Test 6 — Brand then service (no re-asking)
Do you install XPEL?
ppf
→ expect: lock ppf + keep XPEL, then ask missing fields only (no brand clarifier again)

## Test 7 — Repo-missing + model correction (carry-forward year)
Jetour T3 2024
→ expect: repo-missing clarifier (one question)
Jetour T1
→ expect: preserve year=2024 (do NOT re-ask year)

## Test 8 — Wrong transcript (admin gate)
Customer A: BMW X5 ceramic done last week.
Customer B: How much for tint?
→ expect: suppression + admin reset required; no state changes

---

# Appendix C — Freeze Criteria (Phase 0–2)
Phase 0–2 can be declared FROZEN only when:
1) All tests in Appendix B pass with deterministic routing.
2) Repo-missing never silently passes as VEHICLE_ONLY_RESPONSE.
3) Brand-only never defaults to PPF.
4) Year carry-forward works on model correction.
5) Wrong transcript always halts + requires admin reset.
6) Title rules are consistent: BaseTitle created once and never overwritten.

END