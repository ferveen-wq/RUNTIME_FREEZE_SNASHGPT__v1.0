# 07_ACTIVE_WORKING_MEMORY.md

Purpose:
Single active working-memory file for runtime patch sessions.
Do not rely on chat memory. Read this file first in every new session.

## 1. SOURCE OF TRUTH ORDER
1. Locked runtime authorities
2. Engine authorities
3. Parameter / repository authorities
4. Control-tower architecture notes
5. Deferred patch notes
6. Prompt-bridge alignment last

## 2. CLOSED SERVICE TRACKS
### Ceramic
Status: ACTIVE
- Phase 3A validated
- Phase 3B validated
- Phase 5 continuity / render leakage fixed
- Runtime path broadly stable
- Phase 4 strict UAT promotion now covers silence, brand fixation, and price resistance on branch
- Phase 5 strict canonical coverage is now complete in the trusted single-turn, state-injected lane for the active owner path and includes:
  - PHASE5_CERAMIC_PRICE_GAP_DEEPEN_L1
  - PHASE5_CERAMIC_NARROW_L2
  - PHASE5_CERAMIC_EXIT_FORK_L3
- Canonical UAT is now 35 / 35 PASS on branch
- Treat Ceramic as complete for Phase 5 in the trusted lane, while overall multi-turn harness continuity remains untrusted

### Tint
Status: CLOSED
- Phase 0-2 recognition validated
- Real Phase 3A validated
- Phase 3B validated
- Phase 5 strict canonical coverage is now complete in the trusted single-turn, state-injected lane for the active owner path and includes:
  - PHASE5_TINT_COMPARE_DEEPEN_L1
  - PHASE5_TINT_NARROW_L2
  - PHASE5_TINT_EXIT_FORK_L3
- Canonical UAT is now 38 / 38 PASS on branch
- Runtime path considered stable

### PPF
Status: ACTIVE
- Phase 3B price-ready path validated
- Phase 5 PPF verbatim rendering validated
- Phase 5 PPF strict canonical coverage is now complete in the trusted single-turn, state-injected lane and includes:
  - PHASE5_PPF_PRICE_GAP_DEEPEN_L1
  - PHASE5_PPF_NARROW_L2
  - PHASE5_PPF_TECHNICAL_DEEPEN_L1
  - PHASE5_PPF_BRAND_WARRANTY_DEEPEN_L1
  - PHASE5_PPF_EXIT_FORK_L3
- Earlier leakage concern was resolved as test-fixture / runner enforcement, not runtime drift
- Runtime path broadly stable
- Phase 4 strict UAT promotion now covers entry, first objection, silence, warranty sensitivity, technical sensitivity, brand fixation, and price resistance on branch
- Canonical UAT is now 32 / 32 PASS on branch
- Treat PPF as complete for Phase 5 in the trusted lane, while overall multi-turn harness continuity remains untrusted

### Polishing
Status: CLOSED
- Phase 0-2 recognition validated
- Phase 3A known-vehicle entry validated
- Phase 3A second qualifier continuity validated
- True Phase 3B readiness validated
- Phase 5 strict canonical coverage is now complete in the trusted single-turn, state-injected lane for the active owner path and includes:
  - PHASE5_POLISH_EXPECTATION_DEEPEN_L1
  - PHASE5_POLISH_NARROW_L2
  - PHASE5_POLISH_EXIT_FORK_L3
- Canonical UAT is now 41 / 41 PASS on branch
- Runtime path considered stable

## 3. DEFERRED / DO NOT PATCH NOW
### Wrap
Status: CLOSED
- Architecture path: qualification + manual handoff (CONFIRMED)
- Phase 3A finish capture validated
- Post-finish handoff behavior validated (ESCALATION_BLOCK_WRAP_QUOTE)
- Correct debug state enforced (phase=4, READY_FOR_NEGOTIATION, no price ladder)
- Earlier blockage traced to runner/harness execution-state enforcement, not runtime authority drift
- Runtime path considered stable

Rule:
- Do NOT expand wrap automation beyond handoff model
- Do NOT introduce Phase 5 wrap negotiation logic
- Only revisit if fresh runtime evidence contradicts current behavior

## 5. DO NOT TOUCH WITHOUT NEW EVIDENCE
- Ceramic runtime path outside active Phase 4 authority-alignment work
- Tint runtime path
- PPF runtime path outside active Phase 4 authority-alignment work
- Polishing runtime path
- Wrap runtime bridge for deep automation

## 6. SESSION START RULE
At the beginning of every new chat/session, run:

1. cat docs/control_tower/07_ACTIVE_WORKING_MEMORY.md
2. git status --short
3. git log --oneline -n 8

Then continue only from:
- CLOSED
- ACTIVE
- DEFERRED
states in this file.

## 7. PATCH RULE
Before any patch:
- confirm target file role
- inspect surrounding authority logic
- check for duplicate logic
- define validation method
- do not patch closed tracks without fresh failing evidence


### PHASE 0–2 VERIFIED SERVICE AUDITS

- PPF verified:
  - Current Route B is PHASE4_6-only for customer-facing output
  - PHASE6__SERVICE_CANON_BUNDLE.md remains internal truth/constraint authority
  - PPF scope suppression remains active in Phase 6
  - Historical Route B previously used Phase 6 bundle sections, but current live runtime does not

- Ceramic verified:
  - Current Route B is PHASE4_6-only for customer-facing output
  - PHASE6__SERVICE_CANON_BUNDLE.md remains internal truth/constraint authority
  - Historical Route B previously used Phase 6 bundle sections, but current live runtime does not



### PHASE 0–3B FILE-SURFACE COMPLETENESS (VERIFIED)

- Proven broader Phase 0–3B surface includes:
  - runtime control files
  - engine authority files
  - routing/render authority files
  - dependency/support files
  - tested-lane enforcement files
- NEGOTIATION_LOGIC_MODULE.md is materially relevant to Phase 3B as upstream signal/framing authority.
- PRICE_LADDER_ENGINE.md remains the sole pricing-state owner for price_ladder_state.
- PHASE3_LOCK_INDEX.md and PHASE3_ORCHESTRATION_WIRING_ADDENDUM.md must be included in Phase 3B due diligence.
- Runner/tested-lane enforcement must not be collapsed into runtime-authority truth.
- READY vs READY_FOR_NEGOTIATION remains a live reconciliation point across runtime wording, architecture wording, and tested-lane enforcement.


## 8. NEXT ALLOWED TASK

- Phase 6 Route B contract is CLOSED and validated.
- Additional UAT coverage added:
  - tint ready-path
  - polishing ready-path
  - wrap handoff guard
- No further runtime patching required for Phase 0–6.

Current active lane:
- Phase 0–7 TRUST REVALIDATION

Tier 1 (CRITICAL BASELINE PACKS) — STATUS: VERIFIED

Trusted packs:
- gap008_routeb_service_confirmed_v1.json
- phase7_reentered_only_v1.json
- reentered_context_strict_pack.json
- phase3_tint_ready_path_v1.json
- phase3_polish_ready_path_v1.json
- wrap_handoff_after_finish_v1.json

Validation notes:
- All packs executed using correct env-based runner invocation
- All packs are single-turn harness compatible
- Report summaries matched expected case counts (no positional drift)
- Debug outputs align with expected phase / routing / phrase IDs

Conclusion:
- Tier 1 baseline is TRUSTED
- No evidence of fake pass due to runner positional execution for these packs

Next:
- Tier 2 first-wave checkpoint complete

Tier 2 (PHASE 4 STRICT FIRST WAVE) — STATUS: MOSTLY VERIFIED

Trusted passes:
- phase4_ppf_silence_strict_v1.json
- phase4_ppf_price_resistance_strict_v4.json
- phase4_ppf_warranty_sensitivity_strict_v2.json
- phase4_ceramic_silence_strict_v1.json
- phase4_ceramic_brand_fixation_strict_v2.json

Trusted failure:
- phase4_ppf_technical_sensitivity_strict_v2.json

Tier 2 conclusion:
- Phase 4 strict first-wave packs are broadly stable
- One real contract mismatch exists in the PPF technical sensitivity lane
- GAP-021 now records that contradiction as OPEN

Focus:
- Determine manifest-active vs support-only files for:
  - Phase 7 (closing vs education split)
  - Phase 8 (visual system)
  - Phase 9 (persuasion layer)
- Resolve Phase 7 role ambiguity:
  - closing/follow-up routing vs education snippets
- Record tested-lane truth:
  - REENTERED_CONTINUE is runner-proven
  - THINKING / SILENT / DEFERRED / READY_TO_PROCEED are not yet runner-hardened
  - dict-shaped SILENT state pack is quarantined as harness-incompatible, not execution proof
- Record support-layer truth:
  - Phase 7 snippet/governance contract is not yet fully normalized
  - EDU_PPF_SELF_HEAL is structurally inconsistent with the main snippet pattern
- GAP-020 added:
  - support-layer normalization inconsistency within PHASE7_EDUCATION_SNIPPETS.md
  - runtime-consumable support layer must not be treated as structurally normalized yet

Rules:
- Do NOT expand Phase 7–9 behavior yet
- Do NOT introduce new logic
- Only classify ownership, wiring, and runtime participation

Goal:
- Establish clean authority map for Phase 7–9 before any testing or patching


### PHASE 0–6 DEPENDENCY AWARENESS (ACTIVE)

- Phase 0–6 validation must distinguish:
  - manifest-active runtime path
  - support-authority dependencies (canon, registry, SKU, price)

- Do NOT assume repo files are runtime-active unless proven via manifest / execution.

- Identified support-authority gaps (deferred):
  - ROOF_PPF_BLACK_GLOSS → runtime-active, metadata incomplete in naming registry
  - PPF_FRONT_GLOBAL → pricing-active, metadata incomplete in naming registry

- Decision:
  - No runtime patch applied
  - Parked for support-authority cleanup phase

- Rule:
  - Complete Phase 0–6 testing using current runtime path
  - Do NOT expand Phase 7–9 until support-authority layer is stabilized



- Tint verified:
  - Phase 4.6 output only
  - Phase 6 internal
  - No direct Phase 6 emission

- Polishing verified:
  - Phase 4.6 output only
  - Phase 6 internal
  - No direct Phase 6 emission

- Wrap verified:
  - Phase 4.6 output only
  - Phase 6 internal
  - No direct Phase 6 emission
