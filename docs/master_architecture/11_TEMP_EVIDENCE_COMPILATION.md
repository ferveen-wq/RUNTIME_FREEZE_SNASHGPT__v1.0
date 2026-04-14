# TEMP EVIDENCE COMPILATION (CROSS-PAGE)

Status: WORKING
Purpose: Consolidate extracted truths from historical chat pages before updating architecture docs or gap register.

⚠️ This is NOT authority.
⚠️ This is NOT for patching.
⚠️ This is for consolidation only.

--------------------------------------------------
SECTION 1 — DOCUMENTATION SYSTEM STRUCTURE (CONFIRMED)
--------------------------------------------------

- Architecture docs created under docs/master_architecture:
  00–07 = core architecture docs
  08 = gap register (single fixing authority)
  09 = assistant intelligence layer (non-runtime)
  10 = rollout alignment notes (evidence log)

- notes/ folder = analysis only (non-authority)
- *.bak / *.broken / *.pre_* = snapshots only

Confirmed authority split:
- Runtime files = behavior authority
- 00–07 docs = documentation authority
- 08 = rollout fixing authority
- 10 = evidence / alignment log

--------------------------------------------------
SECTION 2 — WORKFLOW MODEL (CONFIRMED)
--------------------------------------------------

Confirmed operating flow:

shadow test → evidence → gap register → patch decision → runtime/doc patch → validation

Phase handling rule:
- Phase 0–3 → FIX → then TEST
- Phase 4+ → TEST → then FIX

Two-lane system:
- Lane 1 (this page): documentation + gap control
- Lane 2 (testing page): runtime behavior + UAT harness

--------------------------------------------------
SECTION 3 — PHASE 0–3 STATUS (CONFIRMED)
--------------------------------------------------

- Phase 0–3 documentation: largely rebuilt
- Considered:
  - structured
  - usable
  - not fully locked (needs reconciliation)

Known risks:
- docs may be cleaner than runtime
- testing page may be based on older assumptions

Action decided:
- do targeted reconciliation (not full re-test)

--------------------------------------------------
SECTION 4 — GAP MANAGEMENT MODEL (CONFIRMED)
--------------------------------------------------

08_ARCHITECTURE_GAP_REGISTER.md rules:

- All gaps MUST be logged before patching
- No patching from:
  - chat
  - notes
  - memory

Gap types:
- DOC_MISMATCH
- RUNTIME_BUG
- ARCHITECTURE_CONFLICT
- PHRASE_LAYER_DRIFT
- DATA_DEPENDENCY
- VALIDATION_GAP

--------------------------------------------------
SECTION 5 — PHASE 4 STRATEGY (CONFIRMED)
--------------------------------------------------

DO NOT:
- scan docs and fix proactively
- patch based on assumptions

DO:
- run shadow testing
- capture real behavior
- log issues into 08

Phase 4 nature:
- behavior-driven (not deterministic)
- requires runtime observation

--------------------------------------------------
SECTION 6 — IDENTIFIED RISKS (CONFIRMED)
--------------------------------------------------

- testing page may lack architecture awareness
- UAT harness evolved separately from docs
- runtime behavior may differ from rebuilt architecture
- risk of misleading Phase 4 conclusions

Critical example:
- one chat per customer rule not enforced earlier

--------------------------------------------------
SECTION 7 — CURRENT PROJECT POSITION (CONFIRMED)
--------------------------------------------------

- Architecture docs: READY (draft authority)
- Gap register (08): READY
- Alignment notes (10): ACTIVE
- Phase 0–3: PROVISIONALLY COMPLETE
- Phase 4: NOT STARTED PROPERLY (needs aligned entry)

--------------------------------------------------
END OF FILE

--------------------------------------------------
SECTION 8 — RUNTIME / FLOW EVIDENCE FROM PAGE 13 (CONFIRMED)
--------------------------------------------------

Confirmed from extracted runtime-flow references on the architecture-build page:

Sequencing / gating:
- Qualification MUST produce an explicit qualification status before downstream routing.
- Runtime MUST NOT proceed to negotiation unless qualification readiness is satisfied.
- Assembly MUST output exactly one Phase 3A qualifier question and STOP.
- Phase 3B MUST NOT execute until phase3a_complete == true.
- Load order is deterministic and must follow fixed sequencing.
- Runtime enforces no-bypass qualification gating.

Context continuity:
- Vehicle context must carry forward once confirmed.
- Service switches must NOT wipe vehicle context.
- Runtime must NOT lose vehicle context across flow progression.
- Missing context must be handled safely and re-evaluated when new customer data appears.

Alias / normalization discipline:
- Numeric-only model tokens must NEVER auto-normalize.
- Ambiguous aliases must clarify once.
- System must not assume brand/model from incomplete alias input.

Safety / anti-drift:
- No new files / no drift constraints are active governance principles.
- No hallucination / no invention enforcement is part of runtime behavior.
- Locked doctrine overrides conflicting lower-priority content.
- Conflicting or ambiguous identities must halt progression.

--------------------------------------------------
SECTION 9 — TESTING / UAT / GOVERNANCE EVIDENCE FROM PAGE 13 (CONFIRMED)
--------------------------------------------------

Confirmed from extracted testing/governance references on the architecture-build page:

Testing model:
- UAT and mega-sequence testing were used as validation evidence.
- Shadow testing is part of the working method.
- Assistant transcripts are part of testing / validation artifacts.

Validation rules:
- One question maximum per assistant reply is a real validation rule.
- No exact prices / no bundles / no assumptions are enforced in protected testing contexts.
- Architecture and testing must be separated so documentation does not drift into behavior truth.

Build discipline:
- Communication rules must NOT contain pricing logic.
- Phase architecture must NOT contain tone rules.
- Patching should be done through terminal / structured patch workflow, not casual manual edits.
- Patch-first and validator-first discipline is part of the governance approach.

--------------------------------------------------
SECTION 10 — ARCHITECTURE VS RUNTIME TENSIONS FROM PAGE 13 (CONFIRMED)
--------------------------------------------------

Confirmed from extracted conflict/drift references on the architecture-build page:

- Architecture docs must not hide unresolved runtime conflicts.
- If architecture docs conflict with active runtime files, active runtime files win.
- Phrase-library vs output-template hygiene conflict existed and should not be silently normalized.
- Ownership wording can drift if described too broadly.
- Conflict-resolution priority must be explicit.
- Intake / ownership / phrasing sections require caution to avoid creating documentation drift.
- The architecture rebuild process explicitly aimed to avoid creating a second conflicting doctrine layer.

--------------------------------------------------
SECTION 11 — PAGE 13 ROLE IN PROJECT (CONFIRMED)
--------------------------------------------------

Page 13 function:
- Build master architecture docs from extracted runtime truth.
- Separate documentation authority from runtime authority.
- Create / normalize rollout gap control.
- Prepare for Phase 4 by separating:
  - documentation-control page
  - testing / behavior-truth page

Important outcome:
- This page is documentation-control and evidence-planning, not the live runtime testing page.


--------------------------------------------------
SECTION 12 — 11 APR PAGE: HARNESS CONTINUITY / PHASE 4 TESTING EVIDENCE
--------------------------------------------------

Source:
- /tmp/page11_clean.txt
- focused extraction around lines ~68900–72900

Confirmed findings:

1. Multi-turn UAT continuity problem
- runner/run_uat.py was understood to handle multi-turn cases by sending each turn fresh.
- It used:
  - system prompt
  - one user message only
- It did not pass prior user/assistant conversation history.
- It did not persist prior runtime state between turns.
- Result:
  - no real post-price continuity
  - no real objection progression
  - no reliable objection_repeat_count growth
  - Phase 4 / Phase 5 testing could drift from real runtime behavior

2. Phase 4 testing risk
- The page explicitly concluded that continuing to build Phase 4 packs on this harness would test the wrong thing.
- Phase 4 drift was therefore not treated as only a phrase/routing issue.

3. Required audits identified on 11 Apr
- harness continuity audit
- canonical-key audit

4. Two safe options identified
- Path A:
  patch the harness so multi-turn UAT reflects real chat continuity
- Path B:
  keep harness unchanged, but restrict Phase 4 testing to single-turn, state-injected entry checks only

5. Directional preference at that time
- The page leaned toward Path A as more correct for architecture.

6. Broader interpretation
- UAT green was not treated as proof of runtime truth.
- Harness was already acting like a second runtime / shaping layer.
- Phase 3 being sealed/final did not mean behavior was fully stable.
- Assembly remained the selector authority; output template remained formatting-only authority.

Status:
- CONFIRMED HISTORICAL EVIDENCE
- NOT YET PATCH DECISION
- MUST be compared later against:
  - current runtime
  - current harness
  - current architecture docs
  - current gap register


--------------------------------------------------
SECTION 13 — 11 APR PAGE: HARNESS PATCH DECISION REVERSAL (CONFIRMED)
--------------------------------------------------

Source:
- /tmp/page11_clean.txt
- focused extraction around lines ~69180–69540 and later turning-point discussion

Confirmed sequence:

1. Initial finding
- runner/run_uat.py multi-turn handling was observed to send:
  - one system prompt
  - one user message
  - for each turn independently
- Prior turns were not preserved inside the harness call.
- This made the harness appear unsuitable for real Phase 4 multi-turn continuity testing.

2. Initial proposed direction
- Patch runner/run_uat.py so multi-turn cases preserve prior user turns and prior assistant replies.

3. Later correction after production-model clarification
- User clarified that real production usage is:
  - separate ChatGPT window per customer
  - full chat or last 4–5 messages pasted each time
  - context reconstructed from pasted transcript, not from internal persistent memory
- Based on that, the earlier harness patch was paused / rejected at that stage.

4. Correct historical interpretation
- The issue was not closed as “fixed.”
- The conclusion shifted from:
  - “patch multi-turn harness now”
  to:
  - “do not patch yet until production-model alignment is clearer”

5. Implication
- 11 Apr evidence shows an important architectural distinction:
  - stateful multi-turn harness simulation
  versus
  - stateless-by-design production flow using pasted transcript context
- Therefore this topic must be treated as:
  - architecture/testing-model decision
  - not a simple harness bug only

Status:
- CONFIRMED HISTORICAL EVIDENCE
- NO FINAL PATCH DECISION
- MUST later be compared against:
  - current testing method
  - current UAT harness
  - actual assistant operating workflow


--------------------------------------------------
SECTION 12 — 11 APR EVIDENCE SLICE A (FINAL STATE / HARNESS / PHASE 4 TURNING POINT)
--------------------------------------------------

Source:
- 11 apr.txt
- extracted via final-state / harness / runtime grep

Confirmed findings:
- PHASE4_8_MESSAGE_ASSEMBLY_MAP.md remained the active selector for Phase 4 / Phase 5 routing.
- selected_phrase_id must be chosen by PHASE4_8_MESSAGE_ASSEMBLY_MAP.md.
- output template is not routing authority.
- Phase 5 entry was governed by hard assembly routing / single-block selection.
- Phase 4 testing had drifted because the current UAT harness was effectively running each turn as a fresh turn, not a real persisted conversation.
- This meant multi-turn Phase 4 / Phase 5 behavior could be tested incorrectly if the harness shape was trusted blindly.
- Canonical / enum consistency was a live concern:
  - locked/runtime references used FINAL_PRICE_REACHED
  - UAT/debug outputs sometimes showed looser values like final
  - the page concluded this looked like harness bypass / canonical-mapping drift
- The page explicitly concluded there were two separate problems:
  1. real phase routing/assembly authority must be respected
  2. harness continuity was not simulating real chat flow correctly
- The recommended next move on that page was:
  - harness continuity audit
  - canonical-key audit
  - only then build the proper Phase 4 pack
- Path options recorded on page:
  - Path A: patch the harness so multi-turn UAT reflects real chat continuity
  - Path B: keep harness unchanged, but restrict Phase 4 testing to valid single-turn, state-injected entry checks only
- At that point in the page, Path A was considered more correct architecturally.
- The page also reaffirmed:
  - locked runtime remains final authority
  - chats/testing pages are evidence/history, not final doctrine

Interpretation status:
- Evidence only
- Not yet promoted to gap register
- Not a runtime patch instruction


--------------------------------------------------
SECTION 14 — 11 APR EVIDENCE SLICE C (PPF-LED STABILIZATION & SERVICE COVERAGE GAP)
--------------------------------------------------

Source:
- 11 apr.txt
- extracted from Phase 3 closure / service coverage discussion

Confirmed findings:
- Phase 3 stabilization was primarily driven using PPF as the main stress-test service.
- PPF exposed:
  - Phase 3A skipping issues
  - early pricing leakage
  - ready vs not-ready contradictions
  - routing inconsistencies
- Other services were NOT validated at the same depth:
  - Ceramic → partial validation (technical-hold issues)
  - Wrap → partial routing validation
  - Roof-black → treated as special-case routing
  - Tint → not deeply validated in this cycle
- The page explicitly warned:
  - “Phase 3 green” must not be interpreted as full system stability
  - risk: only PPF is fully tested while other services remain under-validated
- The correct interpretation recorded:
  - Phase 3 is architecturally more stable
  - but not uniformly verified across all services
- Recommended next-step strategy:
  - Freeze Phase 3 checkpoint
  - perform targeted non-PPF service sweep:
    - ceramic
    - tint
    - wrap
  - only then proceed to Phase 4
- A structured working model was defined:
  - Layer 1: frozen Phase 3 checkpoint (architecture baseline)
  - Layer 2: service coverage sweep (gap validation layer)
- Explicit governance rules:
  - do not reopen PPF unless regression appears
  - do not assume coverage from “green” status
  - do not proceed to Phase 4 without minimum cross-service validation

Interpretation status:
- CONFIRMED HISTORICAL EVIDENCE
- CRITICAL FOR GAP IDENTIFICATION
- NOT a runtime patch
- MUST be compared later against:
  - current Phase 3 coverage
  - service-specific UAT packs
  - actual runtime behavior across services


--------------------------------------------------
SECTION 15 — 11 APR EVIDENCE SLICE D (INTERMEDIATE HARNESS-FIRST CONCLUSION BEFORE PRODUCTION-MODEL CORRECTION)
--------------------------------------------------

Source:
- 11 apr.txt
- extracted from strict-raw / multi-turn harness review band
- supported by direct runner/run_uat.py inspection shown on the page

Confirmed findings:
- At this point in the 11 Apr page, the active conclusion was:
  - do NOT patch Phase 4 runtime files yet
  - fix the UAT harness first
- Reason recorded on the page:
  - Phase 4 UAT was considered not trustworthy because the harness was stateless across turns
- The page explicitly proposed this sequence:
  1. patch runner/run_uat.py multi-turn flow
  2. rerun the same Phase 4 multi-turn pack
  3. only then decide whether Phase 4 runtime had a real issue
- The inspected runner band supported that interpretation:
  - multi-turn cases iterated through turns
  - but each call sent only:
    - one system prompt
    - one user message
  - prior turns were not preserved in the API input payload
- Therefore, at that stage, the page treated multi-turn UAT continuity as the main blocker for trustworthy Phase 4 testing.

Interpretation status:
- CONFIRMED HISTORICAL EVIDENCE
- INTERMEDIATE CONCLUSION ONLY
- NOT final doctrine
- MUST be read together with the later 11 Apr correction that production usage is stateless-by-design via pasted transcript context
- Therefore this section records:
  - what the page concluded before that correction
  - not the final accepted project model


--------------------------------------------------
SECTION 17 — 11 APR EVIDENCE SLICE E (STRICT-HARNESS PATCH FAILURE / NO TRUSTWORTHY FAILING HARNESS YET)
--------------------------------------------------

Source:
- 11 apr.txt
- extracted from the early strict-raw / contradiction-guard hardening cluster

Confirmed findings:
- A patch attempt was made against `runner/run_uat.py` to harden contradiction detection.
- That patch attempt failed because the expected `validate_result` stub was not found exactly.
- The page explicitly recorded:
  - `run_uat.py` stayed unchanged
  - the “strict pack” remained observational only
  - bad behavior could still pass as `pass: true`
- The page concluded that, at that stage:
  - the immediate problem was not runtime
  - the project still did not have a trustworthy failing harness
- The recommended next step recorded on the page was:
  - do NOT patch runtime again yet
  - patch `runner/run_uat.py` correctly using the file’s real structure
  - then rerun the strict fail-first pack
- The expected benefit of that next move was:
  - real failures would surface
  - fake-green loops would stop
  - runtime patching could become evidence-based instead of guesswork

Interpretation status:
- CONFIRMED HISTORICAL EVIDENCE
- INTERMEDIATE HARNESS-HARDENING STATE
- NOT final runtime doctrine
- NOT yet a gap-register item
- MUST be read later together with:
  - later strict-raw hardening success
  - later production-model correction
  - later Phase 3 checkpoint evidence


--------------------------------------------------
SECTION 18 — 11 APR EVIDENCE SLICE F (PHASE 3 SCOPE UNDERSTANDING BEFORE PATCHING)
--------------------------------------------------

Source:
- 11 apr.txt
- extracted from Phase 3 scope audit discussion
- supported by runtime-file inspection commands referenced on that page

Confirmed findings:
- Before patching, the page explicitly shifted toward a Phase 3 scope audit rather than memory-based assumptions.
- The page treated runtime files as the authority for defining total Phase 3 scope.
- The scope audit direction focused on:
  - file inventory
  - cross-references
  - execution flow
  - load manifest
  - output template
  - qualification engine
  - negotiation logic
  - objection resolution
- The page recorded that Phase 3A and Phase 3B should not be described from memory.
- The page recorded that the authoritative chain had to be reconstructed from runtime files first.
- The extracted runtime discussion on that page indicated:
  - Phase 3A runs only when vehicle_model and vehicle_year are already known
  - runtime phase remains PHASE_3 throughout Phase 3
  - 3A vs 3B is represented by internal flags/signals, not by changing the phase label
- Therefore, this page contributed an important methodology correction:
  - do scope audit first
  - then patch
  - do not infer total Phase 3 design from UAT behavior alone

Interpretation status:
- CONFIRMED HISTORICAL EVIDENCE
- METHODOLOGY-IMPORTANT
- NOT a runtime patch
- MUST later be compared against:
  - current runtime Phase 3 authorities
  - architecture docs for Phase 3
  - any remaining Phase 3 gap-register entries


--------------------------------------------------
SECTION 05A — PHASE 0–2 HISTORICAL EVIDENCE SUMMARY
--------------------------------------------------

Source:
- 11 apr.txt
- extracted from Phase 0–2 evidence lines
- extracted from Phase 0–2 uncertainty / deferred lines

Confirmed findings:
- Phase 0–2 was treated as frozen enough to continue into Phase 3.
- It was repeatedly described as:
  - UAT-aligned
  - tagged green / good enough to freeze
  - protected by carried-forward guard packs
- A Phase 0–2 checkpoint commit was referenced:
  - `52a1a90`
  - described as alignment of vehicle-question shape across runtime and harness
- Historical evidence repeatedly treated the following as the carried-forward Phase 0–2 protection set:
  - ledgered UAT alignment state
  - `phase0_2_block_i`
  - `phase0_2_block_j`

Uncertainty still explicitly recorded:
- runtime and harness were not described as fully aligned
- Phase 0–2 was not described as pure runtime-only proof
- the checkpoint was described as built partly by harness control
- the ledger still contained open / non-final / deferred items

Deferred / unresolved themes explicitly mentioned in this historical slice:
- question-friction review
- adaptive low-friction / impatient-customer handling
- pricing output discipline

Correct interpretation:
- Phase 0–2 should be treated as:
  - frozen operational baseline
  - safe enough not to reopen casually
  - but not final proof that runtime and harness were fully reconciled
- Therefore Phase 0–2 should only be reopened if:
  - a later regression clearly proves leakage
  - or later alignment work proves a real authority mismatch

Status:
- CONFIRMED HISTORICAL EVIDENCE
- SUITABLE FOR DOCUMENTATION RECONCILIATION
- NOT a direct runtime patch instruction
- NOT yet a gap-register item by itself

--------------------------------------------------
SECTION 05B — PHASE 3 HISTORICAL EVIDENCE SUMMARY
--------------------------------------------------

Source:
- 11 apr.txt
- extracted from Phase 3 checkpoint / coverage lines
- extracted from Phase 3 harness-vs-runtime lines
- extracted from prior checkpoint / strict-raw / non-PPF sweep evidence already added in later sections

Confirmed findings:
- Phase 3 reached real checkpointed branch states, including:
  - `phase3_checkpoint_clean_20260413`
  - `phase3_full_service_uat_ready_20260413`
- The historical record described Phase 3 as:
  - clean
  - checkpointed
  - documented
  - UAT-ready for the branch
- Phase 3 stabilization was explicitly PPF-led first, then widened through non-PPF closure coverage.
- The page explicitly warned that “Phase 3 green” must not be misread as “PPF only.”
- A non-PPF sweep was then used to close minimum service-coverage gaps before Phase 4.
- The historical record also shows repeated harness hardening activity:
  - `strict_raw` introduction and repeated use
  - fake-green loop reduction
  - repeated warnings not to patch runtime blindly while harness truth was still weak
- The page later distinguished:
  - stateful harness ideas
  - versus the real production model, which is stateless-by-design using pasted transcript context

Correct interpretation:
- Phase 3 should be treated as:
  - checkpointed and operationally strong for the branch
  - but historically reached through both runtime fixes and harness hardening
- Therefore future review must keep separating:
  - real runtime authority
  - harness/test enforcement
  - production operating model

Status:
- CONFIRMED HISTORICAL EVIDENCE
- IMPORTANT FOR ARCHITECTURE / UAT ALIGNMENT
- NOT a direct runtime patch instruction



--------------------------------------------------
SECTION 06 — 9 APR HISTORICAL EVIDENCE SUMMARY
--------------------------------------------------

Source:
- 9 apr.txt

Purpose:
- Capture NEW findings only (delta vs 11 Apr)
- Do NOT repeat already captured evidence
- Do NOT compress or reinterpret beyond evidence

Rules:
- Evidence only
- No invention
- No architecture decisions
- No gap promotion yet

To capture:
- New runtime behaviors not seen in 11 Apr
- Earlier-stage issues later corrected in 11 Apr
- Any contradictions to 11 Apr conclusions
- Any signals about harness vs runtime differences
- Any early indicators of Phase 3 instability

Interpretation status:
- WORKING EXTRACTION
- NOT FINAL
- MUST BE COMPARED WITH SECTION 05A / 05B

--------------------------------------------------
SECTION 06A — 9 APR HISTORICAL EVIDENCE SUMMARY (PATCH-RESTRAINT / HARNESS-TRUST / RUNTIME-SUSPECTS)
--------------------------------------------------

Source:
- 9 apr.txt
- extracted from:
  - /tmp/9apr_patch_restraint.txt
  - /tmp/9apr_harness_trust.txt
  - /tmp/9apr_runtime_suspects.txt

Confirmed findings:
- 9 Apr was primarily an inspection-first / do-not-patch page, not a clean runtime-fix closure page.
- Strong repeated operating rule on that page:
  - do not patch unless evidence is strong enough
  - do not patch from memory
  - do not patch blindly
  - do not patch runtime when a supporting patch is enough
- The page repeatedly classified many candidate changes as:
  - supporting patch
  - inspection only
  - not ready for runtime commit
- Harness / runner trust was a major concern on that page:
  - `runner/run_uat.py` was treated as a real contamination / observability risk
  - `runner/context_reset_prompt.txt` was treated as a behavior-shaping layer
  - smoke-pack / runner invocation reliability was questioned
  - the harness could suppress or expose the same issue depending on constraints
- Therefore several defect signals on that page were treated as:
  - possibly harness-side
  - not yet safe to assign directly to runtime authority
- The main runtime files repeatedly inspected on that page were:
  - `QUALIFICATION_ENGINE.md`
  - `PHASE4_8_MESSAGE_ASSEMBLY_MAP.md`
  - `PRICE_LADDER_ENGINE.md`
- However, repeated conclusions on that page showed:
  - engine patch not yet justified
  - assembly patch not yet justified
  - exact sections / precedence / phrase blocks had to be inspected first
- One visible issue family on 9 Apr involved:
  - `YEAR_ONLY`
  - PPF Phase 3A routing / coverage-first logic
  - precedence / phrase-block / support-override inspection
- But this issue family was still under due diligence on that page, not yet recorded there as a final clean runtime root cause.

Correct interpretation:
- 9 Apr should be treated as:
  - historical evidence of patch restraint
  - historical evidence that harness trust was weak
  - historical evidence that runtime suspects were being narrowed carefully
- 9 Apr should NOT be treated as:
  - final proof of runtime defect
  - final closure of those issues
  - final architecture wording authority

Status:
- CONFIRMED HISTORICAL EVIDENCE
- IMPORTANT FOR TIMELINE / METHOD / TRUSTWORTHINESS
- NOT a runtime patch instruction
- NOT yet final gap-register content

--------------------------------------------------
SECTION 06B — 9 APR EVIDENCE SLICE (PPF PHASE 3A QUALIFIER DRIFT VS ENGINE / ROUTING)
--------------------------------------------------

Source:
- 9 apr.txt
- extracted from `/tmp/9apr_yearonly_ppf_slice.txt`

Confirmed findings:
- 9 Apr isolated a specific PPF Phase 3A issue family around:
  - coverage-first qualifier behavior
  - approved qualifier wording shape
  - phrase-block drift versus engine/routing stability
- The historical evidence repeatedly showed:
  - `QUALIFICATION_ENGINE.md` still selected `PHASE3A_Q_PPF_COVERAGE_INTENT` first
  - `PHASE4_8_MESSAGE_ASSEMBLY_MAP.md` still routed that qualifier verbatim
  - qualifier wiring remained clean
  - qualifier order remained coverage-first
- Therefore the page was narrowing away from:
  - engine-order defect
  - assembly-routing defect as first proven cause
- The strongest historical conclusion on that page was:
  - observed drift was mainly in the customer-facing phrase-block wording
  - not yet in the qualification engine routing key/order itself
- The page repeatedly described the issue as:
  - PPF Phase 3A coverage wording drift
  - qualifier regression in wording shape
  - narrowing from an older explicit 3-way coverage question into a changed / narrowed qualifier wording
- The page also showed that:
  - `YEAR_ONLY` and precedence/gating references were nearby in the investigation
  - but they were not the strongest proven root cause for this exact PPF qualifier issue
- The page’s direction at that stage was:
  - inspect phrase block exactly
  - patch phrase block only if the exact wording diff is confirmed
  - do not patch engine / assembly first without stronger proof

Correct interpretation:
- 9 Apr provides meaningful historical evidence that one visible Phase 3A defect was being localized to:
  - phrase-layer drift
  - not necessarily engine or routing failure
- This matters because later documentation must distinguish:
  - runtime control truth
  - phrase wording drift
  - harness influence
- Therefore this slice should be treated as:
  - a specific defect-localization milestone
  - not yet a final global architecture conclusion

Status:
- CONFIRMED HISTORICAL EVIDENCE
- HIGH VALUE FOR PHASE 3 ROOT-CAUSE TIMELINE
- NOT a direct runtime patch instruction
- NOT yet final architecture wording



--------------------------------------------------
SECTION 07 — 6 APR HISTORICAL EVIDENCE SUMMARY
--------------------------------------------------

Source:
- 6 apr.txt

Purpose:
- Capture NEW findings only (delta vs 9 Apr / 11 Apr)
- Do NOT repeat already captured evidence
- Do NOT compress or reinterpret beyond evidence

Rules:
- Evidence only
- No invention
- No architecture decisions
- No gap promotion yet

To capture:
- Earlier-stage instability before 9 Apr restraint phase
- Any raw runtime defects before harness hardening
- Early signs of Phase 3 or Phase 0–2 drift
- Any contradictions to later conclusions (9 Apr / 11 Apr)

Interpretation status:
- WORKING EXTRACTION
- NOT FINAL
- MUST BE COMPARED WITH SECTION 05A / 05B / 06A / 06B


--------------------------------------------------
SECTION 07A — 6 APR HISTORICAL EVIDENCE SUMMARY (PATCH-RESTRAINT / EARLY RUNTIME SUSPECTS / TESTING-CONTEXT NOISE)
--------------------------------------------------

Source:
- 6 apr.txt
- extracted from:
  - /tmp/6apr_patch_restraint.txt
  - /tmp/6apr_runtime_suspects.txt
  - /tmp/6apr_testing_noise_map.txt

Confirmed findings:
- 6 Apr was an early exploratory testing page, not a final runtime-fix page.
- Strong repeated operating rule on that page:
  - do not patch yet
  - do not patch blindly
  - do not patch before file integrity / audit / due diligence
  - do not patch repo/runtime files casually
- The page repeatedly treated many discussed items as:
  - not approved for rollout patch yet
  - audit first
  - inspect first
  - log first
- A large portion of the page was about testing-environment instability rather than runtime authority itself:
  - inside-project vs outside-project behavior
  - project-context heaviness
  - fresh-chat vs same-chat testing method
  - ghosting / price-sensitive / objection scenarios as test-flow setup
- Therefore a significant portion of 6 Apr must be treated as testing-process noise, not direct architecture truth.

Runtime-relevant evidence still visible on 6 Apr:
- The main runtime authority files repeatedly inspected were:
  - QUALIFICATION_ENGINE.md
  - PHASE4_8_MESSAGE_ASSEMBLY_MAP.md
  - PRICE_LADDER_ENGINE.md
- 6 Apr already reflected important phase logic expectations such as:
  - Phase 3A runs only when vehicle_model + vehicle_year are known
  - Phase 3A vs 3B represented by control flags
  - exactly one qualifier per turn
  - no invented coverage variants
  - PRICE_LADDER_ENGINE only for price exposure stage
  - YEAR_ONLY as an authoritative one-question route when only year is missing
- 6 Apr also contains early suspicion that:
  - assembly could be overriding / over-explaining instead of clean qualifier routing
  - qualification engine principles looked mostly correct already
  - assembly map was a likely higher-risk runtime surface than blindly patching engines first

Correct interpretation:
- 6 Apr should be treated as:
  - historical evidence of early instability and careful patch restraint
  - historical evidence that testing method itself was affecting confidence
  - historical evidence that runtime suspects were already being narrowed toward assembly + qualification surfaces
- 6 Apr should NOT be treated as:
  - final proof of runtime root cause
  - final closure page
  - direct architecture wording authority

Status:
- CONFIRMED HISTORICAL EVIDENCE
- IMPORTANT FOR TIMELINE / METHOD / EARLY SIGNALS
- NOT a runtime patch instruction
- NOT yet final gap-register content



--------------------------------------------------
SECTION 08 — 2 APR HISTORICAL EVIDENCE SUMMARY
--------------------------------------------------

Source:
- 2apr.txt

Purpose:
- Capture NEW findings only (delta vs 6 Apr / 9 Apr / 11 Apr)
- Focus on:
  - early rollout/UAT method
  - project-context usage
  - Phase 8 / later-phase references
  - anything that later became corrected, overridden, or deferred

Rules:
- Evidence only
- No invention
- No architecture decisions
- No gap promotion yet
- Ignore anything already clearly superseded by 6 Apr / 9 Apr / 11 Apr

To capture:
- New rollout/UAT governance signals
- New project-context / upload-pack decisions
- New phase-boundary assumptions later corrected
- New later-phase dependencies that may affect architecture docs
- Contradictions against later clean checkpoints

Interpretation status:
- WORKING EXTRACTION
- NOT FINAL
- MUST BE COMPARED WITH SECTION 05A / 05B / 06A / 07A

--------------------------------------------------
SECTION 08A — 2 APR HISTORICAL EVIDENCE SUMMARY (MEMORY-RECOVERY / PHASE8-9 / GOVERNANCE-ANCHOR)
--------------------------------------------------

Source:
- 2apr.txt
- extracted from:
  - /tmp/2apr_rollout_uat.txt
  - /tmp/2apr_later_phase.txt
  - /tmp/2apr_patch_restraint.txt
  - /tmp/2apr_runtime_authority.txt

Confirmed findings:
- 2 Apr was heavily focused on memory recovery, working-method reconstruction, and project-governance recovery.
- The page repeatedly treated uploaded historical pages as:
  - reconstruction material
  - continuity context
  - not direct patch instructions by themselves
- A strong anti-memory-drift rule was present:
  - latest date wins unless clearly superseded
  - runtime/governance files must anchor truth
  - chat summaries alone are not enough
- 2 Apr repeatedly reinforced patch discipline:
  - do not patch blindly
  - do not patch from memory
  - if sequencing or file integrity is unclear, stop and inspect/log first
  - deferred items must remain explicitly logged
- 2 Apr contains strong evidence that Phase 8 / Phase 9 were already real in repo history, including references to:
  - `PHASE8_VISUAL_INTELLIGENCE_MAP.md`
  - `EDUCATION_TRIGGER_MATRIX.md`
  - visual/video registry concepts
  - persuasion timing / concept extraction work
- At the same time, the page treated higher orchestration for Phase 8 / Phase 9 as:
  - partial
  - not fully reconstructed yet
  - requiring file-first inspection before new design work
- 2 Apr also contains authority-boundary evidence:
  - qualification first
  - downstream routing after qualification
  - message assembly after routing
  - output formatting owned separately
  - phrase/template/routing roles should not collapse into each other
- Repo-history evidence appearing on this page also included:
  - Phase 3A qualifier-first stabilization work
  - lowercase/uppercase `service_intent` gating fix references
  - Phase 0–2 routing hardening + harness stabilization references
- However, this page should still be treated primarily as:
  - governance/method recovery
  - architecture continuity recovery
  - not the final closure page for runtime truth

Correct interpretation:
- 2 Apr is valuable mainly for:
  - governance recovery
  - memory-reconstruction method
  - proof that later-phase visual/education architecture already existed in some form
  - authority-boundary discipline
- 2 Apr should NOT be treated as:
  - final runtime closure
  - final Phase 8/9 integration proof
  - stand-alone patch authority

Status:
- CONFIRMED HISTORICAL EVIDENCE
- IMPORTANT FOR TIMELINE / GOVERNANCE / LATER-PHASE CONTEXT
- NOT a direct runtime patch instruction
- NOT yet final gap-register content

