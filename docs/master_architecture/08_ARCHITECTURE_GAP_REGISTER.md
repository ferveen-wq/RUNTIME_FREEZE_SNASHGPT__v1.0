
GAP-013
Type: ARCHITECTURE_CONFLICT
Title: Wrap Phase 0–2 Route B historical-vs-current contract drift
Source:
- PHASE4_8_MESSAGE_ASSEMBLY_MAP.md
- PHASE6__SERVICE_CANON_BUNDLE.md
- Git history
Impact:
- Confirms systemic Phase 0–2 Route B drift pattern
Status: OPEN

---

GAP-012
Type: ARCHITECTURE_CONFLICT
Title: Polishing Phase 0–2 Route B historical-vs-current contract drift
Source:
- PHASE4_8_MESSAGE_ASSEMBLY_MAP.md
- PHASE6__SERVICE_CANON_BUNDLE.md
- Git history
Impact:
- Confirms systemic Phase 0–2 Route B drift pattern
Status: OPEN

---
GAP-025
Type: ARCHITECTURE_CONFLICT
Title: Phase 5 PPF branch differentiation collapses into single deepen route

Source:
- tests/uat/phase5_ppf_verbatim_strict_v1.json
- notes/evidence_audits/tier_revalidation/TIER3_PPF_PHASE5_BRANCH_COLLAPSE_20260419.md
- 00__LOCKED__UPLOAD_SET/00__Runtime/PHASE4_6_HUMAN_PHRASE_LIBRARY.md

Impact:
- multiple distinct Phase 5 decision paths (narrow, technical deepen, exit fork) collapse into PHASE5_PPF_PRICE_GAP_DEEPEN_L1
- late-stage routing loses branch-level differentiation
- incorrect phase fallback observed in exit scenarios

Observed Behavior:
- repeated selection of PHASE5_PPF_PRICE_GAP_DEEPEN_L1 across different intent paths

Expected Behavior:
- branch-specific phrase IDs:
  - PHASE5_PPF_NARROW_L2
  - PHASE5_PPF_TECHNICAL_DEEPEN_L1
  - PHASE5_PPF_EXIT_FORK_L3

Classification:
- Trusted failure
- Branch collapse
- Late-stage routing failure

Decision:
- Do NOT patch during evidence capture
- Reconcile Phase 5 branch routing logic after full Tier 3 mapping

Status: OPEN

---









GAP-032
Title: Phase 5 repeat-count contract mismatch between objection engine and assembly map

Files inspected:
- 00__LOCKED__UPLOAD_SET/01__Engines/OBJECTION_RESOLUTION_ENGINE.md
- 00__LOCKED__UPLOAD_SET/00__Runtime/PHASE4_8_MESSAGE_ASSEMBLY_MAP.md
- runner/context_reset_prompt.txt
- tests/uat/phase5_ceramic_verbatim_strict_v1.json
- tests/uat/phase5_polish_verbatim_strict_v1.json
- tests/uat/phase5_ppf_verbatim_strict_v1.json

Confirmed findings:
- OBJECTION_RESOLUTION_ENGINE defines repeat_count_meaning as:
  - 0 = first occurrence
  - 1 = second occurrence
  - 2 = third occurrence or more
- OBJECTION_RESOLUTION_ENGINE sets:
  - max_automation_repeats = 1
  - force_escalation_repeat_count = 2
- PHASE4_8_MESSAGE_ASSEMBLY_MAP defines Phase 5 tiers as:
  - <= 1 = L1
  - == 2 = L2
  - >= 3 = L3
- Current UAT cases use:
  - 1 for L1
  - 2 for L2
  - 3 for L3

Assessment:
- Repeat-count semantics are not aligned across engine, assembly, and UAT
- L3 exit-fork instability is consistent with this mismatch
- Prompt-bridge patching alone cannot be treated as the root fix while this contract mismatch remains unresolved

Decision:
- Freeze additional routing edits until repeat-count source of truth is chosen
- Resolve repeat-count contract at architecture level first
- After that, patch downstream authority files and UAT together in one aligned change

Status: OPEN

---
GAP-031
Title: Phase 5 non-PPF collapse persists after polishing authority correction

Files inspected:
- 00__LOCKED__UPLOAD_SET/01__Engines/QUALIFICATION_ENGINE.md
- runner/context_reset_prompt.txt
- 00__LOCKED__UPLOAD_SET/00__Runtime/PHASE4_8_MESSAGE_ASSEMBLY_MAP.md
- runner/run_uat.py
- tests/uat/phase5_polish_verbatim_strict_v1.json
- tests/uat/phase5_ceramic_verbatim_strict_v1.json

Confirmed findings:
- polishing was added to QUALIFICATION_ENGINE service authority contract
- polish-only UAT still fully collapses into PPF family
- ceramic already showed the same collapse pattern
- runtime_signals and phase5 assembly owner contract remain correct
- behavior did not change after upstream polishing authority correction

Assessment:
- polishing is not only an enum/authority omission
- polishing and ceramic now both point to a deeper precedence / owner-resolution leak
- prompt-bridge and qualification edits are no longer producing route ownership change
- next useful work is owner-trace only, not more local patching

Decision:
- revert unvalidated polishing authority patch
- do not commit runtime or qualification changes from this attempt
- continue trace toward the true phase5 owner / precedence source

Status: OPEN

---
GAP-030
Title: Phase 5 non-PPF collapse split into confirmed polishing authority gap and ceramic precedence leak

Files inspected:
- 00__LOCKED__UPLOAD_SET/01__Engines/QUALIFICATION_ENGINE.md
- 00__LOCKED__UPLOAD_SET/00__Runtime/PHASE4_8_MESSAGE_ASSEMBLY_MAP.md
- runner/context_reset_prompt.txt
- runner/run_uat.py
- tests/uat/phase5_ceramic_verbatim_strict_v1.json
- tests/uat/phase5_polish_verbatim_strict_v1.json
- tests/uat/phase5_ppf_verbatim_strict_v1.json
- notes/evidence_audits/tier_revalidation/TIER3_CERAMIC_PHASE5_VERBATIM_PASS_20260419.md
- notes/evidence_audits/tier_revalidation/TIER3_POLISH_PHASE5_VERBATIM_PASS_20260419.md

Historical finding:
- At this investigation stage, ceramic and polishing appeared to collapse into PPF and were separated into:
  - polishing authority-gap hypothesis
  - ceramic precedence-leak hypothesis

Reconciliation:
- Later trusted evidence audits superseded this intermediate conclusion.
- Ceramic Phase 5 verbatim strict now passes in trusted mode.
- Polishing Phase 5 verbatim strict now passes in trusted mode.
- The remaining trusted Phase 5 issue is the separate PPF narrow L2 contract mismatch.

Assessment:
- GAP-030 should be preserved as investigation history only.
- It should not be used as current authority for new runtime or qualification patches.

Decision:
- Keep as historical investigation record.
- Use current Tier 3 evidence audits plus control-tower reconciliation as the active truth.

Status: SUPERSEDED BY LATER EVIDENCE


---
GAP-029
Title: Phase 5 non-PPF routing still collapses into PPF despite prompt-bridge precedence split

Files inspected:
- runner/context_reset_prompt.txt
- runner/context_reset_prompt.txt.bak_wrap_handoff5
- runner/run_uat.py
- 00__LOCKED__UPLOAD_SET/00__Runtime/PHASE4_8_MESSAGE_ASSEMBLY_MAP.md
- 00__LOCKED__UPLOAD_SET/00__Runtime/PHASE4_6_HUMAN_PHRASE_LIBRARY.md

Observed stable result:
- PPF phase5 routing holds after precedence split
- Ceramic phase5 repeat/exit still resolves to PPF family
- Polishing phase5 expectation/narrow/exit still resolves to PPF family
- Local prompt-bridge splitting did not reconcile non-PPF owner

Evidence:
- ceramic_phase5_repeat_objection_verbatim_strict -> PHASE5_PPF_NARROW_L2
- ceramic_phase5_exit_fork_verbatim_strict -> PHASE5_PPF_EXIT_FORK_L3
- polish_phase5_expectation_verbatim_strict -> PHASE5_PPF_PRICE_GAP_DEEPEN_L1
- polish_phase5_narrow_verbatim_strict -> PHASE5_PPF_NARROW_L2
- polish_phase5_exit_fork_verbatim_strict -> PHASE5_PPF_EXIT_FORK_L3

Assessment:
- This is no longer a local phrase-guard issue
- Likely owner-resolution weakness in prompt composition / instruction precedence
- Further patching of runner/context_reset_prompt.txt without owner isolation risks duplicate authority

Decision:
- Stop local patch loop on prompt bridge
- Keep prompt file at committed baseline
- Continue with owner-trace only before next runtime patch

Status: OPEN

---
GAP-028
Type: ARCHITECTURE_CONFLICT
Title: Phase 5 ceramic and polishing exit-fork lanes collapse into PPF exit-fork authority

Source:
- tests/uat/phase5_ceramic_verbatim_strict_v1.json
- tests/uat/phase5_polish_verbatim_strict_v1.json
- runner/context_reset_prompt.txt
- 00__LOCKED__UPLOAD_SET/00__Runtime/PHASE4_8_MESSAGE_ASSEMBLY_MAP.md
- 00__LOCKED__UPLOAD_SET/00__Runtime/PHASE4_6_HUMAN_PHRASE_LIBRARY.md

Impact:
- ceramic exit-fork does not hold service-family isolation
- polishing exit-fork does not hold service-family isolation
- runtime repeatedly selects PHASE5_PPF_EXIT_FORK_L3 for non-PPF services
- prompt-bridge local guard additions did not reconcile the owner cleanly

Observed Behavior:
- ceramic_phase5_exit_fork_verbatim_strict -> selected_phrase_id = PHASE5_PPF_EXIT_FORK_L3
- polish_phase5_exit_fork_verbatim_strict -> selected_phrase_id = PHASE5_PPF_EXIT_FORK_L3

Expected Behavior:
- ceramic exit lane -> PHASE5_CERAMIC_EXIT_FORK_L3
- polish exit lane -> PHASE5_POLISH_EXIT_FORK_L3

Classification:
- Trusted failure
- Cross-service phase5 exit authority leak
- Likely owner/precedence issue beyond local negative guards

Decision:
- Do NOT commit current prompt-bridge patch attempt
- Restore prompt file to last known committed state
- Continue with owner-trace evidence before next runtime patch

Status: OPEN

---

GAP-027
Type: TEST_CONTRACT_MISMATCH
Title: PHASE5_PPF_NARROW_L2 wording contract mismatch between strict pack and governed phrase intent

Source:
- tests/uat/phase5_ppf_verbatim_strict_v1.json
- notes/evidence_audits/tier_revalidation/TIER3_PPF_NARROW_CONTRACT_MISMATCH_20260419.md
- 00__LOCKED__UPLOAD_SET/00__Runtime/PHASE4_6_HUMAN_PHRASE_LIBRARY.md
- 00__LOCKED__UPLOAD_SET/00__Runtime/RUNTIME_CHANGE_LEDGER.md

Impact:
- strict pack forbids price wording
- governed PHASE5_PPF_NARROW_L2 phrase remains affordability-aware by design
- can create false failure even when runtime routing is correct

Observed Behavior:
- phase = 5
- selected_phrase_id = PHASE5_PPF_NARROW_L2
- remaining failure is forbidden-word mismatch only

Expected Behavior:
- strict pack and phrase-library intent should agree on whether affordability wording is allowed

Classification:
- Trusted failure
- Test contract mismatch
- Not a runtime routing defect

Decision:
- Do NOT patch runtime or locked phrase library during this reconciliation step
- Reconcile strict pack wording expectations separately

Status: OPEN

---

GAP-026
Type: ARCHITECTURE_CONFLICT
Title: Phase 5 tint exit fork returns correct phrase but incorrect phase

Source:
- tests/uat/phase5_tint_verbatim_strict_v1.json
- notes/evidence_audits/tier_revalidation/TIER3_TINT_PHASE5_EXIT_FORK_20260419.md

Impact:
- correct phrase selection but incorrect phase reporting
- phase-boundary enforcement inconsistency
- exit flow may behave unpredictably in orchestration

Observed Behavior:
- selected_phrase_id = PHASE5_TINT_EXIT_FORK_L3
- phase = 4 (incorrect)

Expected Behavior:
- phase = 5
- selected_phrase_id = PHASE5_TINT_EXIT_FORK_L3

Classification:
- Trusted failure
- Phase-boundary enforcement issue

Decision:
- Do NOT patch during evidence capture
- Reconcile phase assignment logic after mapping Phase 5 exit flows

Status: RESOLVED (validated after tint phase-boundary enforcement patch)

---


GAP-011
Type: ARCHITECTURE_CONFLICT
Title: Tint Phase 0–2 Route B historical-vs-current contract drift
Source:
- PHASE4_8_MESSAGE_ASSEMBLY_MAP.md
- PHASE6__SERVICE_CANON_BUNDLE.md
- Git history
Impact:
- Confirms systemic Phase 0–2 Route B drift pattern
Status: OPEN

---
# 08_ARCHITECTURE_GAP_REGISTER.md

Status: ACTIVE
Purpose: Single source of truth for ALL confirmed architecture gaps, conflicts, and patch candidates across Phase 0–4.
Authority Level: ROLLOUT CONTROL (highest for fixing decisions)

────────────────────────────────────────────
SECTION 1 — USAGE RULES (NON-NEGOTIABLE)
────────────────────────────────────────────

1) Every confirmed gap MUST be logged here before patching.

2) Do NOT patch directly from:
- chat findings
- alignment notes
- memory

3) Each gap must include:
- Source (where it was found)
- Impact (what breaks)
- Type (classification)
- Status (lifecycle stage)

4) No duplicate entries.
- If similar gap exists → update existing entry.

5) This file drives:
- patch priority
- rollout readiness
- regression validation

────────────────────────────────────────────
SECTION 2 — GAP CLASSIFICATION
────────────────────────────────────────────

Each gap MUST be tagged as one of:

DOC_MISMATCH
- Documentation inconsistent with runtime behavior

RUNTIME_BUG
- System behaves incorrectly

ARCHITECTURE_CONFLICT
- Two files define competing logic

PHRASE_LAYER_DRIFT
- Phrase library / assembly mismatch

DATA_DEPENDENCY
- SKU / pricing / parameter issue

VALIDATION_GAP
- Missing enforcement or unclear contract

────────────────────────────────────────────
SECTION 3 — GAP STATUS
────────────────────────────────────────────

Each gap must have ONE status:

OPEN
- Identified, not yet fixed

PATCH_PLANNED
- Fix decided, not yet applied

PATCHED
- Fix applied in runtime/docs

VALIDATED
- Confirmed working in test

DEFERRED
- Intentionally postponed

────────────────────────────────────────────
SECTION 4 — PHASE 0–2 GAPS
────────────────────────────────────────────

GAP-001
Type: VALIDATION_GAP
Title: Phase 3A control vs Phrase Layer coupling not fully unified
Source: Phase 3 due diligence + PHASE4_8_MESSAGE_ASSEMBLY_MAP
Impact:
- Risk of duplicate qualifier questions
- Risk of incorrect phrase selection
- Possible mismatch between qualification and output layer
Status: OPEN

---

GAP-002
Type: ARCHITECTURE_CONFLICT
Title: READY vs READY_FOR_NEGOTIATION mismatch
Source: PRICE_LADDER_ENGINE.md + runtime flow + architecture docs
Impact:
- Potential routing inconsistency
- Edge-case flow drift during partial qualification
Status: OPEN
Notes:
- Documented in architecture
- Controlled but not resolved

---

GAP-003
Type: VALIDATION_GAP
Title: Phase 2 → Phase 3A handshake contract not formally defined
Source: NEGOTIATION_LOGIC_MODULE.md
Impact:
- Missing clarity on required inputs for Phase 3A
- Possible re-asking or skipping of required data
Status: OPEN

---

GAP-004
Type: PHRASE_LAYER_DRIFT
Title: Deprecated Phase 3B phrase blocks still present
Source: PHASE4_6_HUMAN_PHRASE_LIBRARY.md
Impact:
- Risk of incorrect routing to deprecated phrases
- Tone inconsistency
Status: OPEN

────────────────────────────────────────────
SECTION 5 — PHASE 3 GAPS
────────────────────────────────────────────

GAP-005
Type: DOC_MISMATCH
Title: Rollout source-of-truth file contains stale status flags
Source: SNASHGPT_PHASE0–4_ROLLOUT_SOURCE_OF_TRUTH.md
Impact:
- Misleading rollout readiness perception
Status: OPEN

---

GAP-006
Type: ARCHITECTURE_CONFLICT
Title: Wrap scope vs full-vehicle-only enforcement wording drift
Source:
- PHASE3A_QUALIFICATION_DECISION_MATRIX.md
- QUALIFICATION_ENGINE.md
Impact:
- Confusion in qualification vs pricing behavior
Status: OPEN

---

GAP-007
Type: PHRASE_LAYER_DRIFT
Title: Wrap phrasing implies partial coverage while system enforces full vehicle only
Source: PHASE4_6_HUMAN_PHRASE_LIBRARY.md
Impact:
- Customer confusion
- Misalignment with SKU_SELECTION_MATRIX
Status: OPEN

GAP-008
Type: ARCHITECTURE_CONFLICT
Title: RESOLVED — Phase 6 service-truth authority is runtime-active and the render contract between Phase 6 canon and Phase 4.8 assembly is now explicitly reconciled
Source:
- PHASE4_8_MESSAGE_ASSEMBLY_MAP.md
- PHASE6__SERVICE_CANON_BUNDLE.md
- RUNTIME_LOAD_MANIFEST.md
Impact:
- Historical ambiguity existed over when Phase 6 service truth may be surfaced in customer-facing output
- Historical ambiguity existed over whether Phase 4.8 was selecting bounded service content from Phase 6 versus blocking direct raw canon emission in specific routes
- This ambiguity is now reconciled and Phase 6 Route B testing is trusted in the focused runner-hardened single-turn lane
Status: OPEN
Notes:
- PHASE6__SERVICE_CANON_BUNDLE.md is manifest-proven runtime-active
- PHASE4_8_MESSAGE_ASSEMBLY_MAP.md remains the final assembly/render authority
- Resolution: Phase 6 remains internal truth/constraint authority; PHASE4_8_MESSAGE_ASSEMBLY_MAP.md defines routing/selection; PHASE4_6_HUMAN_PHRASE_LIBRARY.md is the customer-facing render authority

---

────────────────────────────────────────────

GAP-009
Type: ARCHITECTURE_CONFLICT
Title: PPF Phase 0–2 Route B historical-vs-current contract drift
Source:
- PHASE4_8_MESSAGE_ASSEMBLY_MAP.md
- PHASE6__SERVICE_CANON_BUNDLE.md
- Git history (historical Route B wiring)
Impact:
- Documentation can misstate whether Phase 6 is directly used in customer-facing Route B
- Historical and current Route B behavior may be collapsed into one false narrative
- PPF Phase 0–2 audit accuracy depends on separating current live behavior from historical intent
Status: OPEN
Notes:
- Current live Route B uses PHASE4_6-only customer-facing blocks for PPF
- PHASE6__SERVICE_CANON_BUNDLE.md remains internal truth/constraint authority
- Focused GAP-008 trusted-lane UAT evidence:
  - tests/uat/gap008_routeb_service_confirmed_v1.json
  - runner/run_uat.py PASS in strict raw focused lane
  - PPF / Ceramic / Tint / Wrap Route B service-confirmed cases passing without direct Phase 6 leakage
- Historical Route B previously used Phase 6 bundle sections before later rewrite

---


GAP-010
Type: ARCHITECTURE_CONFLICT
Title: Ceramic Phase 0–2 Route B historical-vs-current contract drift
Source:
- PHASE4_8_MESSAGE_ASSEMBLY_MAP.md
- PHASE6__SERVICE_CANON_BUNDLE.md
- Git history
Impact:
- Same pattern as PPF
- Confirms systemic documentation drift, not service-specific
Status: OPEN

---

SECTION 6 — FUTURE PHASE 4 LOGGING
────────────────────────────────────────────

All Phase 4 findings MUST be logged below using same format:

GAP-XXX
Type:
Title:
Source:
Impact:
Status: OPEN



GAP-014
Type: ARCHITECTURE_CONFLICT
Title: Wrap manual-handover business decision is not yet proven in live runtime authority
Source:
- runtime inspection of QUALIFICATION_ENGINE.md
- runtime inspection of CLOSING_HANDOVER_ENGINE.md
- runtime inspection of PHASE4_8_MESSAGE_ASSEMBLY_MAP.md
Impact:
- Wrap may be discussed as manual-handover policy in governance/history, but runtime wiring is not yet explicit
- Rollout trust for wrap remains incomplete until authority ownership is written and validated
Status: OPEN

---


GAP-015
Type: ARCHITECTURE_CONFLICT
Title: Phase 4/5 naming and ownership split remains ambiguous between objection-deepening Phase 5 and closing/handover Phase 5
Source:
- 00__LOCKED__UPLOAD_SET/00__Runtime/PHASE4_8_MESSAGE_ASSEMBLY_MAP.md
- 00__LOCKED__UPLOAD_SET/01__Engines/CLOSING_HANDOVER_ENGINE.md
- 00__LOCKED__UPLOAD_SET/01__Engines/PHASE_5__CLOSING_HANDOVER/PHASE5_LOCK.md
- 00__LOCKED__UPLOAD_SET/00__Runtime/RUNTIME_LOAD_MANIFEST.md
Impact:
- Runtime behavior may be validated while architecture naming remains misleading
- Phase 4 and Phase 5 authority ownership can be explained inconsistently across docs
- Final rollout confidence needs one clean authority statement for deepening vs closing/handover
Status: OPEN

---

GAP-016
Type: ARCHITECTURE_CONFLICT
Title: Phase 7 name is currently split between runtime closing/follow-up routing and education snippet support layer
Source:
- 00__LOCKED__UPLOAD_SET/00__Runtime/PHASE4_8_MESSAGE_ASSEMBLY_MAP.md
- 00__LOCKED__UPLOAD_SET/00__Runtime/PHASE7_EDUCATION_SNIPPETS.md
- 00__LOCKED__UPLOAD_SET/01__Engines/PHASE_4_7_HOOK_QUESTION_ENGINE.md
- 00__LOCKED__UPLOAD_SET/00__Runtime/PHRASE_GOVERNANCE_STANDARD.md
- 00__LOCKED__UPLOAD_SET/00__Runtime/RUNTIME_LOAD_MANIFEST.md
Impact:
- “Phase 7” can be misread as one owner when repo evidence shows two distinct layers
- closing/follow-up routing and education explanation support can be collapsed into one false execution model
- rollout trust needs an explicit split between runtime route ownership and explanation support ownership
Status: OPEN

---

GAP-017
Type: ARCHITECTURE_CONFLICT
Title: Phase 8 is promoted in runtime notes and assembly routing, but execution-path proof remains narrower than repo-level promotion
Source:
- 00__LOCKED__UPLOAD_SET/00__Runtime/PHASE4_8_MESSAGE_ASSEMBLY_MAP.md
- 00__LOCKED__UPLOAD_SET/00__Runtime/PHASE8_VISUAL_INTELLIGENCE_MAP.md
- 00__LOCKED__UPLOAD_SET/00__Runtime/PHASE8_VIDEO_LIBRARY.md
- 00__LOCKED__UPLOAD_SET/00__Runtime/RUNTIME_CHANGE_LEDGER.md
- 00__LOCKED__UPLOAD_SET/00__Runtime/RUNTIME_EXECUTION_FLOW.md
Impact:
- Phase 8 may be overstated as fully runtime-active if assembly promotion is mistaken for end-to-end execution proof
- rollout confidence needs a cleaner statement separating promoted routing from proven delivery execution
Status: OPEN

---

GAP-019
Type: ARCHITECTURE_CONFLICT
Title: Phase 7 runtime state family is broader in architecture than in runner-hardened prompt-bridge proof
Source:
- runner/context_reset_prompt.txt
- tests/uat/reentered_context_strict_pack.json
- tests/uat/phase7_reentered_only_v1.json
- 00__LOCKED__UPLOAD_SET/00__Runtime/PHASE4_8_MESSAGE_ASSEMBLY_MAP.md
Impact:
- REENTERED_CONTINUE is runner-proven, but THINKING / SILENT / DEFERRED / READY_TO_PROCEED are not yet proven in the tested prompt bridge
- Phase 7 can be overstated as fully tested if architecture-defined states are confused with runner-hardened coverage
- Further Phase 7 testing needs explicit signal-shape / prompt-bridge proof before broader trusted-lane claims
Status: OPEN

---

GAP-020
Type: ARCHITECTURE_CONFLICT
Title: Phase 7 education support layer is runtime-consumable, but snippet structure and governance contract are not yet fully normalized
Source:
- 00__LOCKED__UPLOAD_SET/00__Runtime/PHASE7_EDUCATION_SNIPPETS.md
- 00__LOCKED__UPLOAD_SET/00__Runtime/PHRASE_GOVERNANCE_STANDARD.md
- 00__LOCKED__UPLOAD_SET/00__Runtime/EDUCATION_TRIGGER_MATRIX.md
- 00__LOCKED__UPLOAD_SET/01__Engines/PHASE_4_7_HOOK_QUESTION_ENGINE.md
Impact:
- support-layer entries can be misread as equally normalized when EDU_PPF_SELF_HEAL uses a materially different structure from the main snippet set
- governance requires permission / return-anchor discipline, but the snippet file does not express that contract consistently
- Phase 8 should not inherit Phase 7 education/visual linkage until the Phase 7 support-layer contract is documented cleanly
Status: OPEN

---

GAP-021
Type: ARCHITECTURE_CONFLICT
Title: Phase 4 PPF technical-sensitivity phrase exists but is not reachable under current prompt-bridge TRUST_OR_RISK contract

Source:
- tests/uat/phase4_ppf_technical_sensitivity_strict_v2.json
- runner/context_reset_prompt.txt
- 00__LOCKED__UPLOAD_SET/00__Runtime/PHASE4_6_HUMAN_PHRASE_LIBRARY.md

Impact:
- Technical sensitivity questions (e.g. thickness, specs) are routed to PHASE4_PPF_BRAND_FIXATION_L1 instead of PHASE4_PPF_TECHNICAL_L1
- Phrase library contains a technical-response block, but runtime contract does not expose a valid path to it
- Creates mismatch between:
  - phrase library intent
  - prompt-bridge routing logic
  - UAT strict expectations

Observed Behavior:
- objection_signal = TRUST_OR_RISK
- non-warranty technical question -> forced to BRAND_FIXATION path

Expected Behavior (per test pack intent):
- technical sensitivity -> PHASE4_PPF_TECHNICAL_L1

Classification:
- Trusted failure (validated harness, valid pack)
- Contract mismatch (not runner issue)

Decision:
- Do NOT patch during revalidation phase
- Defer resolution until Tier 2 evidence window is complete

Status: OPEN

---

GAP-022
Type: ARCHITECTURE_CONFLICT
Title: Phase 4 PPF price-resistance strict pack expectation does not match trusted-mode runtime phrase selection

Source:
- tests/uat/phase4_ppf_price_resistance_strict_v4.json
- notes/evidence_audits/tier_revalidation/TIER2_PPF_PRICE_RESISTANCE_RECHECK_20260419.md
- runner/run_uat.py
- 00__LOCKED__UPLOAD_SET/00__Runtime/PHASE4_6_HUMAN_PHRASE_LIBRARY.md

Impact:
- trusted-mode rerun selects PHASE4_PPF_PRICE_SENSITIVITY_L1 instead of expected PHASE4_PPF_PRICE_PRESSURE_L1
- earlier green result for this pack was tainted by runner expectation leakage
- current Phase 4 PPF price-resistance contract is not yet aligned across strict pack expectation and runtime behavior

Observed Behavior:
- objection_signal = PRICE_SENSITIVITY
- selected_phrase_id = PHASE4_PPF_PRICE_SENSITIVITY_L1

Expected Behavior (per strict pack):
- selected_phrase_id = PHASE4_PPF_PRICE_PRESSURE_L1

Classification:
- Trusted failure
- Contract mismatch

Decision:
- Do NOT patch during evidence capture
- Reconcile strict expectation vs runtime route after trusted rerun window is complete

Status: RESOLVED (validated after prompt-bridge price-pressure reconciliation)

---

GAP-023
Type: ARCHITECTURE_CONFLICT
Title: Phase 4 ceramic silence lane leaks into PPF silence route under trusted-mode rerun

Source:
- tests/uat/phase4_ceramic_silence_strict_v1.json
- notes/evidence_audits/tier_revalidation/TIER2_CERAMIC_SILENCE_RECHECK_20260419.md
- 00__LOCKED__UPLOAD_SET/00__Runtime/PHASE4_6_HUMAN_PHRASE_LIBRARY.md

Impact:
- ceramic silence handling is not holding service-specific phrase routing
- runtime selected PPF silence phrase and PPF wording inside ceramic lane
- service continuity under Phase 4 silence handling is not yet trustworthy

Observed Behavior:
- objection_signal = SILENCE_AFTER_PRICE
- selected_phrase_id = PHASE4_PPF_SILENCE_PRIMARY

Expected Behavior (per strict pack):
- selected_phrase_id = PHASE4_CERAMIC_SILENCE_L1

Classification:
- Trusted failure
- Cross-service routing mismatch
- Silence lane service-context leak candidate

Decision:
- Do NOT patch during evidence capture
- Reconcile silence-lane service continuity after Tier 2 trusted rerun evidence is complete

Status: RESOLVED (validated after ceramic silence guard reconciliation)

---

GAP-024
Type: ARCHITECTURE_CONFLICT
Title: Phase 4 ceramic brand-fixation lane escalates to Phase 5 deepen path under trusted-mode rerun

Source:
- tests/uat/phase4_ceramic_brand_fixation_strict_v2.json
- notes/evidence_audits/tier_revalidation/TIER2_CERAMIC_BRAND_FIXATION_RECHECK_20260419.md
- runner/context_reset_prompt.txt
- 00__LOCKED__UPLOAD_SET/00__Runtime/PHASE4_6_HUMAN_PHRASE_LIBRARY.md

Impact:
- ceramic brand-fixation question does not remain in expected Phase 4 authority path
- runtime escalates to Phase 5 ceramic deepen lane while objection_repeat_count remains 0 and price_ladder_state remains INITIAL
- phase-boundary enforcement for ceramic trust/risk handling is not yet trustworthy

Observed Behavior:
- phase = 5
- selected_phrase_id = PHASE5_CERAMIC_PRICE_GAP_DEEPEN_L1

Expected Behavior (per strict pack):
- phase = 4
- selected_phrase_id = PHASE4_CERAMIC_BRAND_FIXATION_L2

Classification:
- Trusted failure
- Premature phase escalation candidate
- Contract mismatch

Decision:
- Do NOT patch during evidence capture
- Reconcile ceramic phase-boundary routing after trusted rerun evidence window is complete

Status: RESOLVED (validated after ceramic trust/brand phase-boundary reconciliation)

---

GAP-018
Type: ARCHITECTURE_CONFLICT
Title: Phase 9 trust / persuasion references exist in repo, but trusted runtime-active ownership is not yet promoted
Source:
- 00__LOCKED__UPLOAD_SET/00__Runtime/RUNTIME_CHANGE_LEDGER.md
- 00__LOCKED__UPLOAD_SET/03__Playbooks/PHASE7_TO_PHASE9_CONCEPT_EXTRACTION.md
- 00__LOCKED__UPLOAD_SET/00__Runtime/SNASHGPT_MASTER_GOVERNANCE.md
Impact:
- repo readers may assume a live runtime Phase 9 owner that is not yet proven
- deferred/reference-only status must be made explicit before rollout documentation expands further
Status: OPEN

----

────────────────────────────────────────────
END OF FILE