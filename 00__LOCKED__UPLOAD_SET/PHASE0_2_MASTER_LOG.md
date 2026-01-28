# PHASE 0–2 MASTER LOG (Runtime Safe)
Last updated: 2026-01-23

Purpose:
This file is the single source of truth for Phase 0–2 stability work.
It separates “fix now” (routing/safety) from “polish later” (phrasing/tone) so we do not re-open loops.

---

## Status Legend
- [OPEN] Needs fix / not yet patched
- [PATCHED] Fixed by patch, awaiting re-test confirmation
- [VERIFIED] Fixed and re-tested successfully
- [DEFERRED] Valid behavior; improve later (Phase 7)
- [LOGGED—FUTURE] Not required for Phase 0–2; revisit later

---

## Scope Rules (Non-Negotiable for Phase 0–2)
1) Customer output must always be:
   English customer message → Arabic customer message → Timestamp
   Optional debug footer ONLY if debug_mode=on.
   No “Meaning/Assessment/Suggested reply” style meta blocks in customer output.

2) Max 1 customer-facing question per message.

3) Phase 0–2 goal:
   Pricing-safe classification + minimal qualification.
   Not “perfect identification” and not “sales education”.

---

# A) FIX NOW — Phase 0–2 HARD LOGIC (Must patch before locking)
These are production-breaking or brand-trust breaking.

## FIX-01 — Output-mode leak (customer sees internal coaching template)
- Symptom:
  Customer output contains “Meaning / Assessment / Suggested reply” or “What the customer means…”
- Risk:
  Breaks your customer tone rules and makes it look like AI / internal notes.
- Required fix:
  Route precedence and/or output template suppression so only approved bilingual message format is emitted.
- Status: [OPEN]
- Target files:
  PHASE4_8_MESSAGE_ASSEMBLY_MAP.md (+ possibly any output template routing used for “generic protection / noise”)

## FIX-02 — Service context resets on vehicle-only after service confirmed
- Symptom:
  Customer: “ppf” then “x90 2023” → system asks “which service?”
- Expected:
  If active_service_context exists, vehicle-only must inherit it and continue the same service flow.
- Status: [OPEN]
- Target files:
  QUALIFICATION_ENGINE.md + PHASE4_8_MESSAGE_ASSEMBLY_MAP.md (route precedence)

## FIX-03 — Vehicle ambiguity must resolve before scope / pricing / hooks
- Symptom:
  “x90 2023” sometimes bypasses VR2 and triggers scope (front/full) too early.
- Expected:
  VR0/VR1/VR2 must complete BEFORE scope questions or Phase 3/price ladder bridges.
- Status: [OPEN]
- Target files:
  PHASE4_8_MESSAGE_ASSEMBLY_MAP.md

## FIX-04 — “Color PPF” incorrectly mapped to Wrap
- Symptom:
  “color ppf” routed as wrap and explained as wrap.
- Expected:
  Color PPF is a PPF variant (parent = PPF). Wrap is separate.
- Status: [OPEN]
- Target files:
  QUALIFICATION_ENGINE.md (intent priority) + PHASE6 service canon wording (if needed)

## FIX-05 — Typo safety / over-confident normalization
- Symptom:
  “jetor x3 2022” becomes “Jetour X3 2022” without clarification.
- Risk:
  Guessing damages trust and breaks “never guess as fact”.
- Expected:
  Only normalize to a specific make/model if confidence is high; else set repo_missing and ask 1 clarifier.
- Status: [OPEN]
- Target files:
  QUALIFICATION_ENGINE.md (confidence threshold + repo-missing behavior)
## FIX-06 — Output-mode leak (customer sees internal coaching template)
- Symptom:
  Customer output contains "Meaning / Assessment / Suggested reply" or "What the customer means…"
- Risk:
  Breaks customer output contract and makes it look like internal notes.
- Required fix:
  Force assembly-only customer output; suppress any coaching/meta template routes in customer mode.
- Status: [OPEN]
- Target files:
  PHASE4_8_MESSAGE_ASSEMBLY_MAP.md (+ any fallback/output template route used for generic/noise/protection)

## FIX-07 — Color PPF incorrectly mapped to Wrap
- Symptom:
  "color ppf" routed as wrap and explained as wrap.
- Expected:
  Color PPF is a PPF variant (parent = PPF). Wrap is separate.
- Status: [OPEN]
- Target files:
  QUALIFICATION_ENGINE.md (intent priority) + PHASE6 service canon wording (if needed)

## FIX-08 — Roof "black roof ppf" needs 1-step expert clarifier (PPF vs wrap)
- Symptom:
  Inconsistent handling of "black roof ppf".
- Expected:
  ONE clarifier:
  "Do you want black look (style) or clear PPF on the roof for protection only?"
- Status: [OPEN]
- Target files:
  QUALIFICATION_ENGINE.md + PHASE4_6_HUMAN_PHRASE_LIBRARY.md (single canonical clarifier phrase)

## FIX-09 — Vehicle ambiguity must resolve before scope / pricing / hooks
- Symptom:
  "x90 2023" sometimes bypasses VR2 and triggers scope or explanation too early.
- Expected:
  VR0/VR1/VR2 must complete BEFORE any scope/price bridge.
- Status: [OPEN]
- Target files:
  PHASE4_8_MESSAGE_ASSEMBLY_MAP.md + QUALIFICATION_ENGINE.md (flag consistency)

## FIX-10 — Edge-intent intake routes (PPF removal/renewal/refresh, headlight restoration/PPF, dechrome, tint removal)
- Symptom:
  Edge service requests (PPF removal, headlight work, dechrome, tint removal) lacked dedicated intake routes.
- Expected:
  Phase 0–2 must stay intake-safe: 1 question + photo-forward, no promises, no deep education.
- Status: [FIXED—P0-2]
- Target files:
  QUALIFICATION_ENGINE.md (rules e-j), PHASE4_6_HUMAN_PHRASE_LIBRARY.md (L.4B1-L.4B6), PHASE4_8_MESSAGE_ASSEMBLY_MAP.md (VR7-VR12)
- Note:
  Phase 0–2 must stay intake-safe: 1 question + photo-forward, no promises, no deep education.

---

# B) DEFERRED — Phase 7 Global Polish (No Phase 0–2 logic changes)
These are valid behaviors but can be improved later.

## POL-01 — Greeting response variance
- Scenario: Customer says “hi”
- Observation: Different greeting styles across tests
- Fix phase: Tone engine / greeting canon polish
- Status: [DEFERRED]

## POL-02 — Early price phrasing looseness
- Scenario: “How much is ceramic?”
- Observation: Mentions “scope / preparation / levels”
- Fix phase: Pricing ladder integration + controlled bridge
- Status: [DEFERRED]

## POL-03 — Follow-up option set mismatch (ceramic)
- Scenario: After car model + year, asked “basic vs full”
- Fix phase: Phase 6 canon + Phase 7 bridge standardization
- Status: [DEFERRED]

## POL-04 — Operational queries over-qualified
- Scenario: location / hours questions
- Observation: sometimes appends vehicle question
- Fix phase: Phase 4.8 micro-routing refinement
- Status: [DEFERRED]

## POL-05 — Repetition of vehicle question
- Scenario: multiple early turns before intent clarity
- Fix phase: Qualification rhythm rules + re-ask suppression (Phase 7)
- Status: [DEFERRED]

## POL-06 — Switch-guard phrasing feels templated
- Scenario: wrap ↔ ppf ↔ wrap
- Fix phase: Phase 7 phrasing smoothing (same logic)
- Status: [DEFERRED]

## POL-07 — Debug visibility inconsistent on explanation-only routes
- Fix phase: debug footer standardization
- Status: [DEFERRED]

---

# C) SERVICE CANON VALIDATION NOTES (Informational; not “locked” until FIX NOW cleared)
Important:
Do not declare a service “locked” until FIX NOW items are VERIFIED.

## PPF — Observations
- Status: [DEFERRED] until FIX-02 / FIX-03 are VERIFIED
- Key notes:
  - Explanation repetition is acceptable for now; smooth in Phase 7.
  - Scope question (front/full) is the correct bridge when vehicle is resolved.

## Tint — Observations
- Status: [DEFERRED] until global fixes VERIFIED
- Key notes:
  - Variant ordering (VR2 vs explanation) is acceptable but can be polished later.

## Polishing — Observations
- Status: [DEFERRED]
- Key notes:
  - Buffing/paint correction alias works.
  - VR2 ordering variance is polish-level.

## Wrap — Observations
- Status: [DEFERRED]
- Key notes:
  - Switch-guard is correct; phrase smoothing later.

## Ceramic — Observations
- Status: [DEFERRED] (global fixes first)
- Key notes:
  - Contradiction handling is cautious (good).
  - Clarifier phrasing repetition: Phase 7 polish.

---

# D) LOGGED—FUTURE EXTENSIONS (Not required for Phase 0–2)
These should not block Phase 0–2 stabilization. They get handled after Phase 3+ is stable.

## FUT-01 — Headlight PPF
- Parent: PPF
- Needs: variant mapping + one clarifier (headlights only / full front / other)
- Status: [LOGGED—FUTURE]

## FUT-02 — PPF removal
- Parent: PPF
- Needs: safe handling (paint condition dependent), workflow later
- Status: [LOGGED—FUTURE]

## FUT-03 — Dechroming / chrome delete
- Parent: Wrap (styling family)
- Needs: alias mapping + minimal clarifier
- Status: [LOGGED—FUTURE]

## FUT-04 — Phase 3+ education blocks for edge intents
- Parent: Cross-service (PPF removal/refresh, headlight restoration/PPF, dechrome, tint removal)
- Needs: Deeper guidance only after qualification/inspection signals (avoid long explanations in Phase 0–2)
- Status: [LOGGED—FUTURE]
- Note:
  Add deeper guidance only after qualification/inspection signals (avoid long explanations in Phase 0–2).

## FUT-05 — Graphene pricing ladder separation
- Parent: Ceramic family
- Needs: separate ladder entries later (avoid in Phase 0–2)
- Status: [LOGGED—FUTURE]

## FUT-06 — Interior ceramic upsell / bundling behavior
- Parent: Ceramic family
- Needs: later-phase bundle logic (Phase 5–7), not Phase 0–2
- Status: [LOGGED—FUTURE]

## FUT-07 — Explanation depth ladder (Light / Medium / Deep)
- Needs: global selector based on customer signals (price push / “explain” / short replies)
- Fix phase: Phase 7 global polish module

---

# E) Action Plan (Controlled Sequence)
1) Patch FIX NOW items (A) with minimal edits.
2) Run the short re-test pack:
   - Output leak check
   - Service stickiness check
   - VR precedence check
   - Color PPF mapping check
   - Typo normalization safety check
3) Mark each FIX item as [VERIFIED].
4) Only then, declare Phase 0–2 “LOCK READY”.
5) After lock, move to Phase 7 polish bucket (B) without touching routing logic again.

---