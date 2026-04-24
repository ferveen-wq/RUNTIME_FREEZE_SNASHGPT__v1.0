────────────────────────────────────────────────────────────
PPF SCOPE QUESTION SUPPRESSION (LOCKED — BUSINESS-SAFE)
────────────────────────────────────────────────────────────

Goal:
Avoid asking "full vs front" by default when customer says "PPF".
Scope should only be asked if the customer explicitly requests it.
Otherwise, Phase 0–2 captures vehicle, and Phase 3A captures usage/exposure first.

Rule:
- If customer explicitly asks for FRONT / PARTIAL / HIGH-IMPACT → allow scope confirmation.
- If customer explicitly asks for FULL / FULL BODY / WHOLE CAR → allow scope confirmation.
- Otherwise:
	- Do NOT ask scope here.
	- Ask only for vehicle model + year (one question).

Note:
- This file may be referenced by test harnesses; this suppression prevents scope-first drift.


# PHASE 6 — SERVICE CANON BUNDLE

Status: ACTIVE (BUNDLED)
Scope: Consolidated Phase 6 service wording blocks. All content under each section is VERBATIM from the original PHASE6__SERVICE_*.md files.

--------------------------------------------------------------------------
RUNTIME OUTPUT GUARD (HARD)
--------------------------------------------------------------------------
Purpose:
- Prevent customer-facing drift by enforcing a single source of customer copy.

Hard rules:
1) Phase 6 canon is FACTS + CONSTRAINTS only. It must NOT be emitted to customers directly.
2) Customer-facing bilingual copy (EN/AR) must come ONLY from:
	- PHASE4_6_HUMAN_PHRASE_LIBRARY.md (selected by PHASE4_8_MESSAGE_ASSEMBLY_MAP.md)
3) The only exception is the PHASE_0_2_MIN blocks below, which are explicitly marked for Phase 0–2 intake use only.
4) No engine may paraphrase Phase 6 canon into customer text. If a customer-facing response is required, select an approved phrase ID.

---
## PHASE 0–2 — APPROVED BRAND DISCLOSURE (v1.0)
Rule:
- In Phase 0–2, the assistant may only mention brand names listed here.
- If customer asks about another brand, do NOT confirm availability; proceed with qualification.

Approved brand names (Phase 0–2):
- XPEL
- Global Hi-Tech Films
---

---

# ============================================================
# PHASE 0–2: MINIMAL SERVICE BLOCKS ONLY (NO TIERS / NO SHADES)
# Hard rule: Each MIN block must include (1) minimal definition + (2) exactly ONE next-step question.
# These blocks are the ONLY Phase 6 content allowed in Phase 0–2.
# ============================================================

## PHASE_0_2_MIN

### PHASE_0_2_MIN__PPF
EN: Paint Protection Film (PPF) is a clear protective film applied to the paint to help reduce stone chips and light scratches. What’s the car model and year?
AR: حماية PPF هي فيلم شفاف يُركّب على الطلاء ويساعد على تقليل ضربات الحصى والخدوش الخفيفة. شنو موديل السيارة وأي سنة؟

### PHASE_0_2_MIN__PPF_SCOPE_CONFIRMED_NEXT
EN: Got it. What’s the car model and year?
AR: تمام. شنو موديل السيارة وأي سنة؟

### PHASE_0_2_MIN__TINT
EN: Sure. To guide you correctly, what’s the car model and year?
AR: أكيد. عشان أوجّهك صح، شنو موديل السيارة وأي سنة؟

### PHASE_0_2_MIN__CERAMIC
EN: Ceramic coating is a protective layer applied to the paint to help with shine and easier cleaning. To guide you correctly, what’s the car model and year?
AR: السيراميك طبقة حماية تُركّب على الطلاء تساعد في اللمعة وسهولة التنظيف. عشان أوجّهك صح، شنو موديل السيارة وأي سنة؟

### PHASE_0_2_MIN__POLISHING
EN: Polishing helps improve gloss and reduce light swirls on the paint. To guide you correctly, what’s the car model and year?
AR: التلميع يساعد على تحسين اللمعة وتقليل آثار الخدوش الخفيفة على الطلاء. عشان أوجّهك صح، شنو موديل السيارة وأي سنة؟

# ============================================================
# PHASE 0–2 — MINIMAL SERVICE DEFINITIONS (LOCKED)
# These blocks are the ONLY Phase 6 content accessible in Phase 0–2
# All other sections unlock in Phase 3+
# ============================================================




## SERVICE — TINT

### BEGIN VERBATIM

# PHASE 6 — SERVICE CANON: TINT (Window Tinting)

## What it is
Window tint is a thin film applied to the glass to improve driving comfort by reducing heat, glare, and harsh sunlight. It also helps protect the interior from sun exposure.

## Why customers choose it
Tinting is commonly done for comfort and daily usability, especially in strong sun conditions. The quality of installation and film choice affects clarity and long-term performance.

## What to keep realistic
Good tint helps reduce heat and glare, but results vary based on film type, vehicle glass, and installation quality.

## Next step (qualification)
[BUNDLE_SOURCE_V1]
To guide you correctly, we'll need the car model and year.

### END VERBATIM

### TINT — DIFFERENTIATION LAYER (PHASE 3+ CANON, INTERNAL-ONLY)

Purpose:
- Provide truthful, non-salesy differentiation facts that Phase 3B/4 can draw from.
- This section is NOT customer-facing copy. Customer wording must be selected from PHASE4_6_HUMAN_PHRASE_LIBRARY.md.

Core positioning (canonical):
- Tint value is not “darkness” (VLT) alone — real comfort depends on:
	- IR heat rejection behavior (material + construction)
	- clarity / haze control (optical quality + install discipline)
	- edge finishing + cleanliness (install quality drives long-term look)
	- legal/compliance targeting (choose a shade that matches local rules)

GCC realities that shape tint outcomes (canonical):
- High heat + strong sun + frequent glass cleaning can amplify:
	- visible haze complaints if film/installation quality is poor
	- premature edge lift risk if edges are contaminated or poorly finished
	- “it feels hot” complaints if only some glass areas are tinted (coverage limits)

Customer-safe truth (comparison-safe):
- Darker does not automatically mean cooler.
- Two films with similar darkness can feel different depending on IR performance.
- Installation quality affects both appearance and durability (bubbles/edges are often install-driven).

Language guardrails:
- Do NOT quote legal VLT numbers unless a Bahrain/GCC compliance policy is canonized elsewhere.
- Avoid absolutes (“blocks all heat” / “no bubbles ever”).
- Use “helps reduce heat/glare” and “results depend on film + coverage + installation”.

--------------------------------------------------------------------------
## TINT — STRUCTURAL EXECUTION MODEL (v1.0 LOCKED)

Exposure Model:
- INTERNAL_ONLY → Never printed directly.
- PHASE_4_ALLOWED → May be framed in simplified customer-safe wording.
- PHASE_5_ALLOWED → Allowed during negotiation / comparison / objection.
- PHASE_7_ALLOWED → Allowed inside structured education modules.

This section defines the complete operational truth of Tint service for later-phase reuse.

────────────────────────────────────────────────────────────
1) PERFORMANCE REALITY MODEL (HEAT / GLARE / CLARITY)
Exposure: PHASE_4_ALLOWED + PHASE_7_ALLOWED

Canonical facts:
- Heat comfort is influenced by film IR behavior, total glass coverage, and vehicle glass geometry.
- Darkness (VLT) and heat comfort are not the same thing.
- Windshield angle, large glass/roof areas, and partial coverage can reduce perceived effect.

Hard constraints:
- Do NOT promise temperature outcomes (“X degrees cooler”).
- Do NOT state legal limits unless separately canonized.

────────────────────────────────────────────────────────────
2) INSTALLATION QUALITY MODEL (APPEARANCE + DURABILITY)
Exposure: PHASE_5_ALLOWED + PHASE_7_ALLOWED (PHASE_4_ALLOWED simplified)

Canonical truths:
- Long-term look depends heavily on surface prep/cleanliness and edge finishing.
- Most early “bubbles/edges” complaints are strongly correlated with install discipline and contamination control.

Hard constraints:
- Avoid blaming competitors. Frame as “install quality varies”.

────────────────────────────────────────────────────────────
3) AFTERCARE & CLEANING DISCIPLINE (CUSTOMER-SAFE)
Exposure: PHASE_4_ALLOWED + PHASE_7_ALLOWED

Canonical:
- Gentle cleaning reduces avoidable edge stress and premature wear.
- Avoid harsh chemicals and aggressive tools that can degrade film over time.

────────────────────────────────────────────────────────────
4) EXECUTION RULES (HARD CONSTRAINTS)

- No pricing inside canon.
- No “free” language.
- No legal-number claims unless separately canonized.
- Customer-facing wording must come ONLY from PHASE4_6 library.
- Assembly must NEVER print canon verbatim.

---

## SERVICE — CERAMIC
### BEGIN VERBATIM

# PHASE 6 — SERVICE CANON: CERAMIC COATING

## What it is
Ceramic coating is a protective layer applied over the paint to improve gloss and make the surface easier to clean. It helps reduce minor water spotting and makes washing simpler, but it's not a replacement for physical protection like PPF.

## Why customers choose it
Customers choose ceramic for easier maintenance, better shine, and a cleaner look. It's often chosen for daily-driven cars to keep the paint looking fresher.

## What to keep realistic
Ceramic helps with ease of cleaning and gloss, but it does not prevent stone chips and deep scratches. Proper prep and application matter for the final result.

--------------------------------------------------------------------------
### CERAMIC — DIFFERENTIATION LAYER (PHASE 3+ CANON, INTERNAL-ONLY)

Purpose:
- Provide truthful, non-salesy differentiation facts that Phase 3B/4 can draw from.
- This section is NOT customer-facing copy. Customer wording must be selected from PHASE4_6_HUMAN_PHRASE_LIBRARY.md.

Core positioning (canonical):
- Ceramic is not “just applying a coating once”. Long-term results depend on:
	- surface preparation depth before application
	- controlled curing discipline
	- and how the surface is managed during the coverage window
- GCC realities that reduce performance if unmanaged:
	- regular washing (any style), dusty conditions, heat exposure
	- water spotting/mineral deposits and wash-induced micro-marring over time

What makes our ceramic offer structurally different (canonical):
- We operate a recall-based care loop to keep gloss + water behavior stable through the coverage window.
- Recall is not a “renewal sales pitch”; it is a performance continuity check + surface reset when required.

Recall schedule logic (canonical):
- 1-year tier: recall window at ~6 months and ~12 months
- multi-year tiers: recall window every ~6 months through the coverage window
Hard rule:
- Missing a recall visit does NOT void coverage by itself.
- Coverage remains valid; recalls can be completed later within the coverage window.

Recall content (customer-safe summary, internal facts):
- detailed wash + decontamination to remove bonded contamination from regular use
- light gloss refinement when condition requires it (paint-safe)
- surface performance check (water behavior + gloss stability)
- controlled recoat when required (tier-appropriate)

Paid service note (hard constraint):
- Recall includes a paid detailing/decontamination component.
- Do NOT introduce fees in first-price exposure.
- Mention only during closing, when asked, or when clarification is required to set expectations.

Tier architecture (internal-only; not customer-facing):
- multilayer structure is tier-dependent
- recoat during recall is standard (condition-based execution, but performed as part of the managed coverage approach)

Bundling/value adds (guardrails):
- Interior/engine bay restoration may be included conditionally (car-age/condition dependent).
- Do NOT promise this upfront for new cars.
- Use only when the customer is comparing, negotiating, or explicitly asks “what’s included/why you”.

Language guardrails:
- Avoid heavy chemical terms (iron fallout, traffic film, mineral neutralization).
- Use layman framing: “deep wash + decontamination”, “surface reset”, “light gloss refinement”, “recoat when needed”.

--------------------------------------------------------------------------
## CERAMIC — STRUCTURAL EXECUTION MODEL (v2.0 LOCKED)

Exposure Model:
- INTERNAL_ONLY → Never printed directly.
- PHASE_4_ALLOWED → May be framed in simplified customer-safe wording.
- PHASE_5_ALLOWED → Allowed during negotiation / comparison / objection.
- PHASE_7_ALLOWED → Allowed inside structured education modules.

This section defines the complete operational truth of Ceramic service.

────────────────────────────────────────────────────────────
1) INSTALLATION DEPTH ARCHITECTURE
Exposure: INTERNAL_ONLY + PHASE_5_ALLOWED (partial framing in PHASE_4_ALLOWED)

First Installation Includes:

A) Surface Preparation
- Detailed wash protocol
- Edge and emblem cleaning
- Controlled decontamination (layman framing only)
- Overspray removal when required
- Paint condition assessment

B) Condition-Based Paint Correction
- Correction depth determined by paint condition
- Always refinement as required
- Uses 3M 2-step polishing system:
	- 3M Fast Cut Plus
	- 3M Ultrafina
	- 3M Green & Blue pads
- Thickness-safe execution only

C) Surface Preparation Chemistry
- Ceramic Prep Cleaner (Envoz)
- Surface Primer (Envoz)

D) Coating Application (Tier Dependent – Internal Logic)
- 1-Year → Bronze (Primer + 9H coat)
- 3-Year → Silver (Primer + 10H + Reboot)
- 5-Year → Gold (Primer + 9H + 10H + Reboot)

Internal Note:
- Multi-layer structure depends strictly on selected tier.
- This structure is NOT disclosed as layer counts in early phases.

E) Exterior Extensions
- Glass coating (Envoz)
- Trim & exterior fiber coating (Envoz)

F) Interior & Engine Bay Handling
Exposure: PHASE_5_ALLOWED (conditional reveal)
- Included across ceramic tiers.
- First installation:
	- Condition-based interior refresh (older cars only).
- Maintenance visits:
	- Light interior vacuum & dressing only.
- New vehicles: minimal exposure unless asked.

────────────────────────────────────────────────────────────
2) PERFORMANCE CONTINUITY MODEL (RECALL-BASED)
Exposure: PHASE_4_ALLOWED + PHASE_5_ALLOWED + PHASE_7_ALLOWED

Ceramic is delivered as a managed coverage model.

Recall Structure:
- 1-Year Tier:
	- Recall window at ~6 months and ~12 months.
- Multi-Year Tiers (3 / 5):
	- Recall window approximately every 6 months throughout coverage.

Policy Integrity:
- Missing a recall visit does NOT void coverage.
- Coverage remains valid during selected warranty window.
- Recall visits may be completed later within coverage period.

Execution During Recall:
- Deep wash & surface reset
- Controlled decontamination
- Light gloss refinement (condition-based)
- Recoat layer application (standard execution)
- Hydrophobic behavior check
- Surface condition review

Mandatory Note:
- Surface decontamination & detailing charge applies.
- Fee structure handled outside canon (pricing tables).

────────────────────────────────────────────────────────────
3) GCC ENVIRONMENT PERFORMANCE LOGIC
Exposure: PHASE_4_ALLOWED + PHASE_7_ALLOWED

Ceramic durability must address:

- Regular washing impact
- Dust-heavy environment
- High heat exposure
- Mineral deposits from water
- White/light colors → yellowing tendency
- Dark colors → swirl visibility

Performance Stability Is Managed Through:
- Proper preparation depth
- Multi-layer tier structure
- Recall-based continuity
- Condition-based refinement

Ceramic longevity is determined more by surface management than by liquid branding alone.

────────────────────────────────────────────────────────────
4) DIFFERENTIATION PRINCIPLE (DEALER / COMPETITOR SAFE)

Exposure: PHASE_4_ALLOWED + PHASE_5_ALLOWED

Canonical Truth:

- The ceramic chemical matters.
- However, long-term stability depends more on:
	- Preparation depth
	- Correction stage
	- Surface priming
	- Application control
	- Post-installation management

Positioning Framework:
Ceramic is not a one-time application.
It is a managed surface system delivered through structured coverage.

────────────────────────────────────────────────────────────
5) EXECUTION RULES (HARD CONSTRAINTS)

- No pricing inside canon.
- No “free” language.
- No exaggerated chemical superiority claims.
- No heat-lamp curing claims.
- No tier layer count disclosure during Phase 3–4.
- Customer-facing wording must come ONLY from PHASE4_6 library.
- Assembly must NEVER print canon verbatim.

--------------------------------------------------------------------------
### CERAMIC MAINTENANCE (CANONICAL ADD-ON)
Name: Ceramic Recall / Maintenance Visit
Purpose:
- Maintain coating performance and appearance over time in Bahrain/GCC conditions.
Hard constraints:
- Do NOT promise “free” / “included” / “warranty coverage” unless warranty policy is separately canonical.
- Do NOT mention any fees at first-price exposure.
- Pricing/eligibility is handled later by pricing tables / policy.

## Next step (qualification)
[BUNDLE_SOURCE_V1]
To guide you correctly, we'll need the car model and year.

### END VERBATIM

---

## SERVICE — GRAPHENE (CERAMIC VARIANT)

### BEGIN VERBATIM

# PHASE 6 — SERVICE CANON: GRAPHENE COATING

## What it is
Graphene coating is a premium coating option in the same category as ceramic. It's applied over the paint to improve gloss and make the surface easier to clean, with a focus on durability and performance when applied correctly.

## Why customers choose it
Graphene is usually chosen by customers who want a premium coating option and care about long-term ease of cleaning and appearance.

## What to keep realistic
Graphene is still a coating: it does not stop stone chips and heavy impacts. The prep work and installation quality matter most.

## Next step (qualification)
[BUNDLE_SOURCE_V1]
To guide you correctly, we'll need the car model and year.

### END VERBATIM

---

## SERVICE — INTERIOR CERAMIC (CERAMIC VARIANT)

### BEGIN VERBATIM

# PHASE 6 — SERVICE CANON: INTERIOR CERAMIC PROTECTION

## What it is
Interior ceramic protection is a coating applied to interior surfaces (depending on material) to help reduce staining and make cleaning easier. It's a protection layer for maintenance, not a cosmetic restoration.

## Why customers choose it
Customers choose it to keep interiors cleaner and reduce staining from daily use. It's often chosen for easier interior maintenance.

## What to keep realistic
It helps with maintenance and stain resistance, but it doesn't make interiors immune to damage. Surface condition and correct application matter.

## Next step (qualification)
[BUNDLE_SOURCE_V1]
To guide you correctly, we'll need the car model and year.

### END VERBATIM

---

## SERVICE — POLISHING
### BEGIN VERBATIM

# PHASE 6 — SERVICE CANON: POLISHING (Paint Correction)

## What it is
Polishing, also known as paint correction, is a cosmetic process that improves the appearance of your car's paint. It helps reduce swirl marks, light scratches, oxidation, and surface dullness, making the paint look cleaner and more even again.

## What to keep realistic
Polishing improves appearance, but it doesn't add a protective layer by itself. Protection decisions depend on the paint condition and your goals.

## Next step (qualification)
[BUNDLE_SOURCE_V1]
To guide you correctly, we'll need the car model and year.

### END VERBATIM

### POLISHING — DIFFERENTIATION LAYER (PHASE 3+ CANON, INTERNAL-ONLY)

Purpose:
- Provide truthful, non-salesy differentiation facts that Phase 3B/4 can draw from.
- This section is NOT customer-facing copy. Customer wording must be selected from PHASE4_6_HUMAN_PHRASE_LIBRARY.md.

Core positioning (canonical):
- Polishing = appearance restoration (shine + clarity) by reducing light defects.
- It is NOT a protective layer by itself.
- Results depend on paint condition (light vs moderate vs heavy defects).

Silver vs Gold (canonical, package-scope only):
- Silver: exterior appearance refresh focus.
- Gold: exterior appearance refresh + interior deep cleaning (and engine bay only if separately defined elsewhere).
- Do NOT frame Gold as “better correction”; it is “wider refresh scope”.

Expectation control (canonical):
- Light marks and swirls improve clearly.
- Deep scratches / chips / peeling clear coat may not fully correct.
- Always use “reduces” / “improves” language, not absolutes.

Cross-service discipline (non-negotiable):
- Do NOT position polishing as an “add-on price” inside ceramic conversations.
  Ceramic canon should refer to “paint prep / correction step” (not “polishing service”) to avoid double-pricing drift.
- Do NOT recommend polishing on top of PPF surfaces. If the customer asks:
  route to PPF aftercare / inspection wording, not polishing.

Language guardrails:
- Avoid technical detailing terms in early phases (compound/pad/DA/rotary/stage levels).
- Avoid “100% scratch removal” / “brand new guaranteed”.

--------------------------------------------------------------------------
## POLISHING — STRUCTURAL EXECUTION MODEL (v1.0 LOCKED)

Exposure Model:
- INTERNAL_ONLY → Never printed directly.
- PHASE_4_ALLOWED → May be framed in simplified customer-safe wording.
- PHASE_5_ALLOWED → Allowed during negotiation / comparison / objection.
- PHASE_7_ALLOWED → Structured education modules.

This section defines the complete operational truth of Polishing service for later-phase reuse.

────────────────────────────────────────────────────────────
1) OUTCOME REALITY MODEL (SHINE / LIGHT DEFECT REDUCTION)
Exposure: PHASE_4_ALLOWED + PHASE_7_ALLOWED

Canonical truths:
- Polishing improves gloss and reduces light swirls/marks; depth of correction depends on paint condition.
- It does not add protection; protection comes from ceramic/PPF decisions in their own flows.

Hard constraints:
- Do NOT promise full removal of deep scratches.
- Do NOT use “100%” outcomes or “better than new”.

────────────────────────────────────────────────────────────
2) PACKAGE SCOPE MODEL (SILVER vs GOLD)
Exposure: PHASE_4_ALLOWED (light) + PHASE_5_ALLOWED + PHASE_7_ALLOWED

Canonical:
- Silver = exterior refresh scope.
- Gold = exterior refresh + interior deep cleaning scope.
- Gold is not “more aggressive correction” by default.

Hard constraints:
- Do NOT introduce “tiers” beyond Silver/Gold unless separately canonized.

────────────────────────────────────────────────────────────
3) CROSS-SERVICE DISCIPLINE (ANTI-DRIFT)
Exposure: INTERNAL_ONLY

Canonical:
- Ceramic flows should not name “polishing service” as a separate priced line item.
  Use “paint prep / correction step” language inside ceramic canon to prevent double-pricing drift.
- Polishing should not be offered over PPF surfaces; do not imply it’s a maintenance method for film.

Hard constraints:
- If customer goal is “older paint + ceramic longevity”: route as “prep step inside ceramic flow”, not two separate services in messaging.
- If customer asks to “polish over PPF”: route to PPF aftercare/inspection path.

────────────────────────────────────────────────────────────
4) EXECUTION RULES (HARD CONSTRAINTS)

- No pricing inside canon.
- No “guarantee perfect scratch removal”.
- Customer-facing wording must come ONLY from PHASE4_6 library.
- Assembly must NEVER print canon verbatim.

## SERVICE — PPF
[BUNDLE_ACTIVE_V1]

### BEGIN VERBATIM

# PHASE 6 — SERVICE CANON: PPF (Paint Protection Film)

## What it is
PPF is a transparent protective film applied over painted panels. It helps reduce stone chips, light scratches, and daily road wear. It's protection-focused, not a repair, and works best when installed on clean, healthy paint. [BUNDLE_PROOF_V1]

## When it makes sense
PPF is chosen when the priority is preserving the factory paint and reducing impact damage from daily driving. It's commonly applied to high-impact areas or the full vehicle depending on how much coverage you want.

## Common coverage options (high level)
Front PPF usually focuses on the most exposed areas at the front of the car.
Full PPF covers most painted panels for maximum protection.

## What it helps with (realistic)
- Stone chips and road debris impact (reduction, not elimination)
- Light scratches and daily wear marks
- Keeping paint looking cleaner for longer

## What to keep realistic
PPF reduces risk, but it doesn't make the car damage-proof. Deep scratches, heavy impacts, or existing paint issues may still show.

## Next step (qualification)
[BUNDLE_SOURCE_V1]
[SRC:PHASE6_BUNDLE_V1]
To guide you correctly, we'll need the car model and year.

### END VERBATIM

### PPF — DIFFERENTIATION LAYER (PHASE 3+ CANON, INTERNAL-ONLY)

Purpose:
- Provide truthful, non-salesy differentiation facts that Phase 3B/4 can draw from.
- This section is NOT customer-facing copy. Customer wording must be selected from PHASE4_6_HUMAN_PHRASE_LIBRARY.md.

Core positioning (canonical):
- PPF value is not only “film thickness” — long-term outcome depends on:
	- brand traceability + manufacturer-backed support
	- adhesive stability + UV stability (GCC heat + washing exposure)
	- edge management + coverage decisions (where the film ends matters)
	- installer execution quality (pattern fit, stretch control, finishing)

GCC realities that shape PPF outcomes (canonical):
- High heat cycles + dusty conditions + frequent washing accelerate:
	- edge stress and early lift risk (if edges are exposed / poorly finished)
	- staining / dulling risk (if aftercare is poor)
	- appearance degradation before functional failure (gradual, not sudden)

What makes our PPF offer structurally different (canonical facts only):
- We install manufacturer-backed series (XPEL + Global Hi-Tech Film) with recorded series identification.
- Proof/traceability methods (availability depends on brand):
	- XPEL: portal-based manufacturer registration is available (e-warranty portal).
	- Global Hi-Tech Film: physical warranty card is available.
- Film series is recorded for verification purposes (invoice/recordkeeping).
- Brand verification is possible via manufacturer/distributor channels if the customer requests it
	(do NOT claim “official distributor” in early phases; only confirm verification path when asked).

Comparison-safe principle (canonical):
- Do NOT attack competitor brands or claim “fake”.
- Allowed framing: “manufacturer-backed registration / traceability vs installer-only paperwork”
	ONLY if customer raises comparison / cheaper quote / warranty questions.

Coverage + installation behavior (canonical, high-level):
- We can support computer-cut patterns when required.
- Manual cutting is also available.
- Do NOT present “manual is better” in early phases.
	Allowed later (Phase 4+ / Phase 5) as education if the customer asks about cutting methods.
- Edge finishing: we tuck/wrap edges in many areas where geometry allows (panel dependent).
	Do NOT promise “full edge wrap everywhere” (geometry constraints apply).

Removability + paint safety (canonical, guarded):
- On OEM / healthy paint, film removal is generally designed to be safe when done correctly.
- Do NOT introduce edge-case risk upfront.
- If customer asks directly, use a guarded framing: removal depends on paint health and prior paint history.

Language guardrails:
- Avoid aggressive “white-label / fake brand” claims.
- Avoid chemical-heavy failure terms in early phases.
- Use simple, customer-safe words: “traceable warranty”, “registered coverage”, “edge finishing”, “aftercare”.



--------------------------------------------------------------------------
## PPF — STRUCTURAL EXECUTION MODEL (v2.0 LOCKED)

Exposure Model:
- INTERNAL_ONLY → Never printed directly.
- PHASE_4_ALLOWED → May be framed in simplified customer-safe wording.
- PHASE_5_ALLOWED → Allowed during negotiation / comparison / objection.
- PHASE_7_ALLOWED → Allowed inside structured education modules.

This section defines the complete operational truth of PPF service for later-phase reuse.

────────────────────────────────────────────────────────────
1) AUTHENTICITY + TRACEABILITY MODEL
Exposure: PHASE_4_ALLOWED (light) + PHASE_5_ALLOWED + PHASE_7_ALLOWED

Canonical facts:
- Manufacturer-backed film series are used (XPEL + Global Hi-Tech Film).
- Traceability artifacts (brand-dependent):
	- XPEL: portal-based manufacturer registration is available.
	- Global Hi-Tech Film: warranty card is available.
- Series identification is recorded for aftercare and verification.
- Customer verification path exists if requested (manufacturer/distributor contact route).

Hard constraints:
- Do NOT claim exclusivity (“only us can do this”).
- Do NOT claim competitor films are “fake”.
- Do NOT claim “official distributor” unless the customer explicitly asks and we can safely frame as “verifiable”.

────────────────────────────────────────────────────────────
2) WARRANTY STRUCTURE (FACTS, NO SALES LANGUAGE)
Exposure: PHASE_5_ALLOWED + PHASE_7_ALLOWED

Canonical:
- Warranty terms are governed by the specific film series and manufacturer documentation.
- Warranty support may involve installer + manufacturer pathways (brand-dependent process).
- Installer execution issues and manufacturer material defects are conceptually different categories.

Hard constraints:
- Do NOT promise approval outcomes.
- Do NOT state exact exclusions unless they are already canonical elsewhere in runtime.

────────────────────────────────────────────────────────────
3) INSTALLATION METHOD OPTIONS (COMPUTER-CUT / MANUAL)
Exposure: PHASE_4_ALLOWED (only if asked) + PHASE_5_ALLOWED + PHASE_7_ALLOWED

Canonical:
- Computer-cut patterns are available.
- Manual cutting is available.
- Education on “why/when” belongs later (Phase 4+ / Phase 5), not at first quote.

────────────────────────────────────────────────────────────
4) EDGE MANAGEMENT PRINCIPLE (GEOMETRY-DEPENDENT)
Exposure: PHASE_4_ALLOWED + PHASE_7_ALLOWED

Canonical:
- Many areas can be tucked/wrapped depending on panel design.
- Some edges cannot be fully wrapped due to geometry constraints.
- Edge finishing quality affects long-term appearance and early lift risk.

────────────────────────────────────────────────────────────
5) GCC ENVIRONMENT PERFORMANCE LOGIC
Exposure: PHASE_4_ALLOWED + PHASE_7_ALLOWED

PPF stability is shaped by:
- Regular washing frequency and technique
- Dusty conditions + abrasive particles
- Heat cycling and sun exposure

Customer-safe truth:
- Long-term clarity and edge stability are influenced more by film quality + installation + aftercare
	than by “day-one look”.

────────────────────────────────────────────────────────────
6) EXECUTION RULES (HARD CONSTRAINTS)

- No pricing inside canon.
- No “free” language.
- No competitor attacks / “fake brand” claims.
- Do not promise edge wrap everywhere.
- Do not introduce removal risk unless asked directly.
- Customer-facing wording must come ONLY from PHASE4_6 library.
- Assembly must NEVER print canon verbatim.

---
Language guardrails:
- Keep phrasing layman and non-threatening.
- Avoid scary chemistry terms and avoid over-promising “no yellowing / no bubbling” as absolutes.
- Use “designed to reduce” / “helps reduce” / “depends on use and care” framing.

--------------------------------------------------------------------------
---

## SERVICE — WRAP

### BEGIN VERBATIM

# PHASE 6 — SERVICE CANON: WRAP (Color Change / Vinyl Wrap)

## What it is
A wrap is a vinyl film applied over the paint to change the look of the car without repainting. It can be done in different finishes like gloss, matte, or satin. The final result depends heavily on surface condition and installation quality.

## Why customers choose it
Wrap is mainly chosen for styling and appearance changes, not protection. It's popular when customers want a new look without permanent paint changes.

## What to keep realistic
Wrap is not the same as PPF. It changes appearance, but it does not offer the same level of impact protection as PPF.

## Next step (qualification)
[BUNDLE_SOURCE_V1]
To guide you correctly, we'll need the car model and year.

### END VERBATIM

### WRAP — DIFFERENTIATION LAYER (PHASE 3+ CANON, INTERNAL-ONLY)

Purpose:
- Provide truthful, non-salesy differentiation facts that Phase 3B/4 can draw from.
- This section is NOT customer-facing copy. Customer wording must be selected from PHASE4_6_HUMAN_PHRASE_LIBRARY.md.

Core positioning (canonical):
- Wrap is a styling service (color/finish change), not an impact-protection service.
- Wrap outcome depends on:
	- paint/surface condition before install
	- film type + finish behavior (gloss/matte/satin)
	- edge strategy + panel geometry (where seams/edges land)
	- installer execution quality (stretch control, alignment, clean finishing)

Customer-safe truths (comparison-safe):
- Wrap changes appearance; it does not replace PPF for stone chips.
- On imperfect paint, wrap can “show what’s underneath” (it doesn’t erase defects).
- Door jambs/inner edges coverage is a scope choice, not a default promise.

GCC realities that shape wrap outcomes (canonical):
- High heat + sun exposure increase importance of:
	- correct film handling during install (stretch/relax control)
	- correct aftercare (washing style affects finish longevity)
- Matte/satin finishes show handling marks more easily than gloss if aftercare is rough.

Surface condition logic (canonical, guarded):
- If paint has heavy defects (deep scratches, peeling clear coat, unstable repaint), results are limited.
- If customer asks “will it look perfect?” → answer must be guarded and inspection-based.

Language guardrails:
- Avoid aggressive “fake/cheap” claims.
- Avoid absolutes (“will never peel / will never fade”).
- Keep wrap positioned as styling-first, not protection-first.

ROOF BLACK (ANTI-DRIFT GUARD — CANONICAL):
- If customer asks for “black roof” (even if they say “wrap”), default routing is:
	- ROOF_PPF_BLACK_GLOSS (PPF only) per Global Product Registry / SKU set.
- Do NOT position roof-black as WRAP. Even if customer says “roof wrap”, fulfill via ROOF_PPF_BLACK_GLOSS.
- REPO-CONFLICT GUARD (LOCKED):
	- Even if legacy repositories contain roof-wrap entries, do NOT quote or offer roof-wrap by default. Use ROOF_PPF_BLACK_GLOSS only.
	- “Black roof” must remain PPF-first per business rule; roof-wrap is only discussed if the customer explicitly insists on vinyl AND availability is confirmed (no invention).
- Allowed customer-safe framing when asked:
	- “For a black roof look, we usually do it as Black PPF for a cleaner, longer-lasting finish.”
- If customer insists on vinyl specifically:
	- Treat as a separate styling request that requires availability confirmation via the product registry (no invention).

--------------------------------------------------------------------------
## WRAP — STRUCTURAL EXECUTION MODEL (v1.1 LOCKED)

Exposure Model:
- INTERNAL_ONLY → Never printed directly.
- PHASE_4_ALLOWED → May be framed in simplified customer-safe wording.
- PHASE_5_ALLOWED → Allowed during negotiation / comparison / objection.
- PHASE_7_ALLOWED → Allowed inside structured education modules.

This section defines the complete operational truth of Wrap service for later-phase reuse.

────────────────────────────────────────────────────────────
1) SERVICE IDENTITY MODEL (WRAP vs PPF vs PAINT)
Exposure: PHASE_4_ALLOWED + PHASE_5_ALLOWED + PHASE_7_ALLOWED

Canonical:
- Wrap = appearance change (color/finish) using vinyl film.
- PPF = protection film (impact/stone chip reduction).
- Paint work = repair/refinish; wrap does not repair paint.

Hard constraints:
- Do NOT position wrap as “protection like PPF”.
- Do NOT promise “paint-like” permanence.

────────────────────────────────────────────────────────────
2) FINISH + LOOK MODEL (GLOSS / MATTE / SATIN)
Exposure: PHASE_4_ALLOWED (simple) + PHASE_7_ALLOWED

Canonical:
- Finish choice affects appearance and aftercare sensitivity.
- Matte/satin: more sensitive to handling marks and aggressive washing.
- Gloss: generally more forgiving visually.

Hard constraints:
- Do NOT promise identical look across all panels without inspection.

────────────────────────────────────────────────────────────
3) SURFACE CONDITION MODEL (PRE-INSTALL REALITY)
Exposure: PHASE_5_ALLOWED + PHASE_7_ALLOWED (PHASE_4_ALLOWED guarded)

Canonical:
- Wrap follows the surface; it can highlight underlying defects under certain lighting.
- Poor repaint / unstable clear coat requires inspection and may be refused or scoped differently.

Hard constraints:
- Do NOT promise “defects disappear”.
- Inspection-first when customer asks about “perfect result”.

────────────────────────────────────────────────────────────
4) EDGES + SEAMS MODEL (GEOMETRY CONSTRAINTS)
Exposure: PHASE_5_ALLOWED + PHASE_7_ALLOWED

Canonical:
- Edge wrapping depends on panel geometry and access.
- Seams may be required on complex shapes; placement is an execution decision.

Hard constraints:
- Do NOT promise “full edge wrap everywhere”.
- Do NOT promise “no seams ever”.

────────────────────────────────────────────────────────────
5) REMOVABILITY + PAINT RISK (GUARDED)
Exposure: PHASE_7_ALLOWED (default) + PHASE_5_ALLOWED if customer insists

Canonical (guarded):
- On healthy OEM paint, removal is generally designed to be safe when done correctly.
- Risk increases with weak paint, prior repaint, or degraded clear coat.

Hard constraints:
- Never guarantee “zero risk removal” before inspection.
- If asked directly: “depends on paint health and repaint history”.

────────────────────────────────────────────────────────────
6) AFTERCARE MODEL (CUSTOMER-SAFE)
Exposure: PHASE_4_ALLOWED + PHASE_7_ALLOWED

Canonical:
- Gentle washing improves longevity and appearance.
- Avoid aggressive washing tools; finish sensitivity varies by type.

Hard constraints:
- Avoid harsh chemical language; keep it customer-safe.
- No brand/product recommendations unless separately canonized.

────────────────────────────────────────────────────────────
8) BLACK ROOF ROUTING RULE (PPF-FIRST, REPO-SAFE)
Exposure: PHASE_4_ALLOWED (light) + PHASE_5_ALLOWED + PHASE_7_ALLOWED

Canonical (hard truth):
- “Black roof” is fulfilled ONLY by ROOF_PPF_BLACK_GLOSS as the default offer.
- Even if the customer says “roof wrap”, do not quote/price “roof wrap” unless the SKU exists in:
	- Global Product Naming Registry + Pricing/SKU repositories.
- REPO-CONFLICT GUARD (LOCKED):
	- If roof-wrap SKUs exist in legacy tables, they are BLOCKED-BY-DEFAULT for quoting unless explicitly enabled in the SKU selection + pricing engines.
	- Roof-black pricing must be generated via the approved pricing engine path for ROOF_ONLY PPF (no ad-hoc numbers, no manual SKU invention).
- If the customer insists on vinyl:
	- Confirm availability first (no invention), then proceed.

Hard constraints:
- Do NOT let wrap canon override the product registry (repo is the final authority for what we sell/price).
- Do NOT create new wrap sub-services (“chrome delete”, “pillar kit”, etc.) unless they exist in repositories.

────────────────────────────────────────────────────────────
7) EXECUTION RULES (HARD CONSTRAINTS)
- No pricing inside canon.
- No warranty durations inside canon.
- Customer-facing wording must come ONLY from PHASE4_6 library.
- Assembly must NEVER print canon verbatim.
