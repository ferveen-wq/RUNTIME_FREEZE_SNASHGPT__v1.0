# ROLLOUT ALIGNMENT NOTES
Status: WORKING
Purpose: Record evidence-backed architecture alignment notes, mismatches, and deferred runtime patch items during documentation rebuild.
Scope: Documentation alignment only. No direct runtime authority.

## 0. Working rules

- Do not patch runtime files directly from architecture drafting.
- Patch runtime files only after due diligence against authoritative runtime files, dependencies, and lock indexes.
- If two authoritative sources appear to conflict, record the conflict here first.
- Prefer documenting confirmed authority boundaries before changing runtime behavior.
- Keep runtime patch items separate from architecture wording updates.

---

## 1. Phase 0-2 status

Current status:
- Core architecture documentation largely rebuilt across:
  - `00_RUNTIME_FILE_INVENTORY.md`
  - `01_SYSTEM_OPERATING_MODEL.md`
  - `02_OWNERSHIP_MODEL.md`
  - `03_STATE_MODEL.md`
  - `04_PHASE_ARCHITECTURE.md`
  - `05_ASSISTANT_OPERATING_MODEL.md`
  - `06_MESSAGE_CONSTRUCTION_MODEL.md`
  - `07_COMMUNICATION_RULES.md`
  - `09_ASSISTANT_INTELLIGENCE_LAYER.md`

Notes:
- Assistant-facing/internal analysis is now separated from customer-facing runtime output at architecture level.
- Runtime patching for additional intake coverage remains deferred pending due diligence.

Deferred check:
- `CUSTOMER_CHAT_INTAKE_RULES.md` may not yet explicitly cover assistant-entered operational updates strongly enough
  (call notes, visit notes, audio summaries, baton handoff notes, operational status entries).

---

## 2. Phase 3A evidence-backed notes

Confirmed from runtime:
- Phase 3A runs after Phase 0-2 when service_intent, vehicle_model, and vehicle_year are known.
- Runtime phase label must remain `PHASE_3`; 3A vs 3B is represented by:
  - `phase3a_required`
  - `phase3a_complete`
  - `phase3a_qualifier_id`
  - `price_ladder_state`
- One question max.
- No pricing in Phase 3A.
- If qualifier is ignored:
  - nudge once
  - repeat same qualifier
  - then set UNKNOWN / UNSURE and proceed safely
- `QUALIFICATION_ENGINE.md` is the effective last writer for:
  - `phase3a_required`
  - `phase3a_complete`
  - `phase3a_qualifier_id`
- `PHASE4_8_MESSAGE_ASSEMBLY_MAP.md` maps `phase3a_qualifier_id` to verbatim phrase blocks only.

Deferred runtime/doc conflict:
- WRAP Phase 3A conflict detected:
  - `PHASE3A_QUALIFICATION_DECISION_MATRIX.md` describes WRAP finish first, then scope
  - `QUALIFICATION_ENGINE.md` says wrap automation is full vehicle only and do NOT ask `WRAP_SCOPE`
- This conflict must be resolved before any runtime patch or final architecture wording freeze.

Additional confirmed Phase 3A details:
- Roof black override uses PPF path and skips normal PPF qualifier chain.
- Same-message fallback exists for some PPF qualifier values.
- Previous-turn qualifier answer capture is explicit and required for correct sequencing.

---

## 3. Phase 3B evidence-backed notes

Confirmed from runtime:
- Phase 3B pricing authority is `PRICE_LADDER_ENGINE.md` only.
- Dependencies:
  - `SKU_SELECTION_MATRIX.md`
  - `PRICE_TABLE_VAT_INCL.md`
- `PRICE_LADDER_ENGINE.md` must not redefine SKU defaults.
- `price_ladder_state` is written only by `PRICE_LADDER_ENGINE.md`.
- Assembly and template are forbidden writers of `price_ladder_state`.
- Pricing may be shown only through price ladder output within engine constraints.
- Raw SKU IDs must not appear in customer-facing text.

Confirmed hard/soft gates:
- Hard gate:
  - car model
  - model year
  - service category
- Soft gate:
  - usage context only when materially relevant

Confirmed restrictions:
- no automatic service substitution
- no invented ranges
- no fabricated coverage variants
- no wrap partial automation pricing
- roof-black styling belongs to PPF path, not wrap path

Potential wording drift to watch:
- some architecture docs currently phrase Phase 3B entry too narrowly as only `READY_FOR_NEGOTIATION`
- runtime engine currently allows `READY_FOR_NEGOTIATION` or `READY`

---

## 4. Deferred runtime patch candidates
## 3A. Phase 3 closure notes

READY vs READY_FOR_NEGOTIATION:
- Runtime negotiation gate is still documented/enforced primarily as `READY_FOR_NEGOTIATION`.
- `PRICE_LADDER_ENGINE.md` currently tolerates `QUALIFICATION_STATUS == READY` or `QUALIFICATION_STATUS == READY_FOR_NEGOTIATION`.
- This is an evidence-backed mismatch/tolerance condition, not yet a fully reconciled architecture rule.
- Until reconciled, orchestration and testing should treat `READY_FOR_NEGOTIATION` as the primary progression gate.

Wrap / roof-black wording drift:
- Roof-black routing is consistently confirmed as PPF-path only.
- However, wrap-related wording remains partially inconsistent across runtime assets:
  - `PHASE3A_QUALIFICATION_DECISION_MATRIX.md` still describes `WRAP_SCOPE`
  - `PHASE4_6_HUMAN_PHRASE_LIBRARY.md` still includes wording that implies section-based wrap pricing direction
  - `QUALIFICATION_ENGINE.md` states wrap automation is full-vehicle only and roof-black is excluded to PPF handling
- This remains a tracked authority conflict and must not be silently normalized in runtime patching.

Rollout source-of-truth stale note:
- `SNASHGPT_PHASE0–4_ROLLOUT_SOURCE_OF_TRUTH.md` still contains stale checklist wording that shows:
  - `SKU_SELECTION_MATRIX.md` as pending
  - `PRICE_TABLE_VAT_INCL.md` as pending
- Current runtime evidence shows both files are active dependencies.
- Treat that rollout document as historical/stale unless refreshed in a later documentation pass.


These are NOT approved runtime patches yet. They are only candidates for due diligence later.

### 4.1 Intake coverage candidate
Possible runtime patch area:
- `CUSTOMER_CHAT_INTAKE_RULES.md`

Reason:
- accepted input types may not explicitly cover assistant-entered operational updates strongly enough

Evidence sources already found:
- `RUNTIME_EXECUTION_FLOW.md`
- `SILENCE_HANDLING_ENGINE.md`
- contract/addendum discussions
- architecture notes

Examples to verify before any patch:
- call note / call summary with customer response
- visit note / visit summary with customer response
- WhatsApp audio summary / voice note transcript
- baton handoff note
- wrong transcript pasted in wrong customer window

Validation requirement before runtime patch:
- confirm no equivalent logic already exists elsewhere in authoritative intake/runtime files
- confirm no duplicate authority would be created
- add only minimal wording in the correct file

### 4.2 Phase 3A wrap conflict candidate
Possible runtime/doc reconciliation area:
- `PHASE3A_QUALIFICATION_DECISION_MATRIX.md`
- `QUALIFICATION_ENGINE.md`

Reason:
- wrap qualifier sequence appears inconsistent between decision matrix and engine behavior

Validation requirement before any patch:
- identify which file is intended final authority for wrap automation behavior
- check load order, lock notes, UAT references, and actual downstream usage
- resolve in one place only, without parallel authority

---

## 5. Next documentation pass

Recommended next pass order:
1. Patch master docs for non-conflicting Phase 3A evidence
2. Patch master docs for non-conflicting Phase 3B evidence
3. Log wrap conflict explicitly in architecture notes/gap register if not already captured
4. Then begin Phase 4 due diligence using locked runtime files
5. Return later for intake runtime patch only after documented review


### 4.3 Wrap automation boundary decision candidate

Status: OPEN — do not patch runtime directly until authority decision is finalized.

Observed during controlled runtime validation:
- Wrap is currently canonically wired as an automated service across:
  - QUALIFICATION_ENGINE.md
  - PHASE4_8_MESSAGE_ASSEMBLY_MAP.md
  - PRICE_LADDER_ENGINE.md
  - SKU_SELECTION_MATRIX.md
  - PRICE_TABLE_VAT_INCL.md
  - GLOBAL_PRODUCT_NAMING_REGISTRY_v1.0.md
  - PHASE6__SERVICE_CANON_BUNDLE.md
- Controlled tests confirmed:
  - known-vehicle Phase 3A works
  - Phase 3B readiness works
  - Phase 5 required bridge-only guards to prevent cross-service leakage
- Existing authority conflict remains:
  - PHASE3A_QUALIFICATION_DECISION_MATRIX.md still describes WRAP_SCOPE
  - QUALIFICATION_ENGINE.md states wrap automation is full-vehicle only and do NOT ask WRAP_SCOPE

Business-direction note:
- Wrap may be lower-priority for full automation than PPF / ceramic / tint / polishing.
- Preferred future model may be:
  - minimum qualification only
  - finish capture
  - basic price-stage acknowledgment
  - then manual handoff to chat/sales team for callback and quoting

Governance decision:
- Do NOT continue ad hoc wrap runtime patching until the final authority model is chosen.
- Final decision must choose one path only:
  1. Wrap remains fully automated (full-vehicle only), or
  2. Wrap becomes qualification + handoff after finish/basic price-stage.

### 4.4 Wrap final authority decision

Status: DECIDED

Final business direction:
- Wrap will NOT remain a fully automated runtime path.
- Wrap will use:
  1. initial qualification
  2. finish capture
  3. basic price-stage acknowledgment
  4. manual handoff to chat/sales team for callback / quoting

Authority consequence:
- Runtime files must be aligned to one-way wrap flow only.
- Wrap should not continue into deep automated negotiated objection routing as a normal closed-loop service.
- Any previous wrap automation behavior that conflicts with this model must be treated as deprecated and removed in authority order.

Implementation rule:
- Patch in this order only:
  1. authority docs
  2. qualification / assembly authority
  3. bridge alignment
  4. UAT validation

### 4.5 Wrap runtime handoff implementation blockage

Status: BLOCKED AFTER AUTHORITY ALIGNMENT

What was attempted:
- decision matrix aligned to finish + handoff model
- assembly map aligned to remove standard wrap Phase 5 automation
- prompt bridge aligned to prevent PHASE3B_WRAP_RANGE and PHASE5_WRAP_* continuation
- explicit post-finish handoff override added
- early wrap finish override bypass added

Observed result:
- UAT still re-asks PHASE3A_Q_WRAP_FINISH even when WRAP_FINISH is already present in runtime signals
- Runtime remains in Phase 3A instead of moving to approved handoff behavior

Conclusion:
- Wrap handoff model is decided architecturally but is NOT yet reliably implemented in runtime
- Further prompt-only patching should stop here to avoid drift
- Next work must be deeper runtime execution analysis, not more surface bridge edits


### 4.6 Wrap blockage root-cause clarification

Status: CONFIRMED

Root cause:
- The intended handoff path for wrap belongs to Phase 3 orchestration/state emission.
- However, in the current branch, Phase 3 orchestration exists as architecture/spec documentation only:
  - RUNTIME_EXECUTION_FLOW.md
  - RUNTIME_STATE_MACHINE.md
  - PHASE3_ORCHESTRATION_WIRING_ADDENDUM.md
- No separate executable orchestration layer was identified that can emit wrap-specific:
  - QUALIFICATION_STATUS transition for post-finish pricing intent
  - QUOTE_REQUIRED_FLAG
  - PRICE_LADDER_STATE = ESCALATED_TO_QUOTE

Operational consequence:
- The current UAT/runtime harness is still effectively controlled by:
  - runner/run_uat.py
  - runner/context_reset_prompt.txt
- Therefore wrap cannot be cleanly fixed through a true orchestration patch in this branch, because no such executable patch point is present.

Governance conclusion:
- Do not force orchestration ownership into QUALIFICATION_ENGINE.md
- Do not continue prompt-only wrap behavior patching
- Next valid step requires either:
  1. implementing an actual executable orchestration layer, or
  2. formally accepting that the runner prompt is the temporary execution authority for UAT behavior
