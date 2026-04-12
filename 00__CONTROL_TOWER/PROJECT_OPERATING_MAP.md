# PROJECT_OPERATING_MAP.md

Status: ACTIVE  
Owner: Control Tower  
Purpose: Single operating map for understanding the SNASHGPT repo without relying on chat memory.  
Scope: Repo structure, authority boundaries, tooling, UAT flow, reference layers, and patch discipline.

---

## 1. Project Purpose

SNASHGPT is a structured customer-conversation runtime for automotive protection and detailing services.

Core business scope includes:
- PPF
- ceramic
- tint
- wrap
- related customer-routing, explanation, pricing, objection, and handover behavior

The repo must support:
- stable runtime behavior
- authority-safe patching
- strict UAT validation
- low-drift operations
- clear separation between live runtime, tooling, tests, control references, and legacy material

This file is the operational entry point for the project.

It is not a runtime file.

---

## 2. Live Runtime Authority Layer

The live runtime authority is inside:

- `00__LOCKED__UPLOAD_SET/00__Runtime`
- `00__LOCKED__UPLOAD_SET/01__Engines`
- `00__LOCKED__UPLOAD_SET/02__Repositories`
- `00__LOCKED__UPLOAD_SET/03__Parameters`
- `00__LOCKED__UPLOAD_SET/03__Playbooks`

These are the files that determine actual behavior for runtime logic, phrase selection, routing, repositories, and parameter truth.

### 2.1 Runtime governance and authority control
These files define the live governance rules for runtime patching and authority boundaries:

- `00__LOCKED__UPLOAD_SET/00__Runtime/AUTHORITY_INDEX.md`
- `00__LOCKED__UPLOAD_SET/00__Runtime/PATCH_PROTOCOL.md`
- `00__LOCKED__UPLOAD_SET/00__Runtime/PHRASE_GOVERNANCE_STANDARD.md`
- `00__LOCKED__UPLOAD_SET/00__Runtime/RUNTIME_CHANGE_LEDGER.md`

Rule:
If a runtime behavior is being patched, authority must be traced through these files first.

### 2.2 Core runtime execution layer
These files define how the runtime is assembled and executed at system level:

- `00__LOCKED__UPLOAD_SET/00__Runtime/RUNTIME_LOAD_MANIFEST.md`
- `00__LOCKED__UPLOAD_SET/00__Runtime/RUNTIME_EXECUTION_FLOW.md`
- `00__LOCKED__UPLOAD_SET/00__Runtime/RUNTIME_STATE_MACHINE.md`
- `00__LOCKED__UPLOAD_SET/00__Runtime/OUTPUT_RESPONSE_TEMPLATE.md`

Patch risk:
High. These files affect broad system behavior and should not be patched casually.

### 2.3 Customer intake and early routing layer
These files govern intake behavior before deeper qualification/assembly logic:

- `00__LOCKED__UPLOAD_SET/00__Runtime/CUSTOMER_CHAT_INTAKE_RULES.md`

Patch risk:
High when defects appear early in the conversation. Confirm whether the defect belongs here before touching Phase 3A or Phase 4 files.

### 2.4 Core qualification and Phase 3A layer
These files govern qualification, readiness, and qualification-stage transitions:

- `00__LOCKED__UPLOAD_SET/01__Engines/QUALIFICATION_ENGINE.md`
- `00__LOCKED__UPLOAD_SET/00__Runtime/PHASE3A_QUALIFICATION_DECISION_MATRIX.md`

Typical ownership:
- missing field handling
- readiness gating
- qualification order
- qualifier capture
- early phase advancement defects

Patch risk:
Very high. Many Phase 0–2 / Phase 3A defects are actually qualification output-shape defects.

### 2.5 Phase 3B pricing and orchestration layer
These files govern price-ready routing and structured price exposure:

- `00__LOCKED__UPLOAD_SET/01__Engines/PRICE_LADDER_ENGINE.md`
- `00__LOCKED__UPLOAD_SET/00__Runtime/PHASE3_ORCHESTRATION_WIRING_ADDENDUM.md`
- `00__LOCKED__UPLOAD_SET/03__Parameters/PRICE_TABLE_VAT_INCL.md`
- `00__LOCKED__UPLOAD_SET/03__Parameters/SKU_SELECTION_MATRIX.md`

Typical ownership:
- price ladder sequencing
- ready-for-negotiation transition
- table-backed pricing output
- strict price-ready behavior

Patch risk:
Very high. Always rule out UAT harness shaping or prompt forcing before changing runtime doctrine here.

### 2.6 Phase 4 assembly and phrase authority layer
These files control phrase selection and runtime customer-facing output:

- `00__LOCKED__UPLOAD_SET/00__Runtime/PHASE4_8_MESSAGE_ASSEMBLY_MAP.md`
- `00__LOCKED__UPLOAD_SET/00__Runtime/PHASE4_6_HUMAN_PHRASE_LIBRARY.md`

Typical ownership:
- selected phrase selection
- route precedence
- phrase block output
- support-routing precedence
- silence / reassurance / comparison phrase selection

Rule:
Do not patch phrase wording until assembly precedence, selected_phrase_id, prompt forcing, and UAT harness behavior have been checked.

### 2.7 Behavior control engine layer
These files govern negotiation, objections, silence, hook questions, and tone behavior:

- `00__LOCKED__UPLOAD_SET/01__Engines/NEGOTIATION_LOGIC_MODULE.md`
- `00__LOCKED__UPLOAD_SET/01__Engines/OBJECTION_RESOLUTION_ENGINE.md`
- `00__LOCKED__UPLOAD_SET/01__Engines/SILENCE_HANDLING_ENGINE.md`
- `00__LOCKED__UPLOAD_SET/01__Engines/PHASE_4_7_HOOK_QUESTION_ENGINE.md`
- `00__LOCKED__UPLOAD_SET/01__Engines/phase_4_5_tone_engine.md`

Typical ownership:
- objection response logic
- silence routing behavior
- hook question handling
- tone-safe follow-up logic

### 2.8 Phase 5 closing and handover layer
These files govern closing, escalation, and post-decision handover behavior:

- `00__LOCKED__UPLOAD_SET/01__Engines/CLOSING_HANDOVER_ENGINE.md`
- `00__LOCKED__UPLOAD_SET/01__Engines/PHASE_5__CLOSING_HANDOVER/PHASE5_LOCK.md`
- `00__LOCKED__UPLOAD_SET/01__Engines/PHASE_5__CLOSING_HANDOVER/PHASE5_1__CLOSING_STATE_MACHINE.md`
- `00__LOCKED__UPLOAD_SET/01__Engines/PHASE_5__CLOSING_HANDOVER/PHASE5_2__HANDOVER_WORKFLOW.md`
- `00__LOCKED__UPLOAD_SET/01__Engines/PHASE_5__CLOSING_HANDOVER/PHASE5_3__END_ESCALATE_RULES.md`
- `00__LOCKED__UPLOAD_SET/01__Engines/PHASE_5__CLOSING_HANDOVER/PHASE5_4__YES_LATER_SILENCE_PLAYBOOK.md`
- `00__LOCKED__UPLOAD_SET/01__Engines/PHASE_5__CLOSING_HANDOVER/PHASE5_5__WHATSAPP_NEXT_STEP_TEMPLATES__EN_AR.md`

### 2.9 Knowledge and canon layer
These files define service truth, product canon, and runtime knowledge boundaries:

- `00__LOCKED__UPLOAD_SET/00__Runtime/KNOWLEDGE__RUNTIME_CORE_BUNDLE.md`
- `00__LOCKED__UPLOAD_SET/00__Runtime/PHASE6__SERVICE_CANON_BUNDLE.md`
- `00__LOCKED__UPLOAD_SET/02__Repositories/PRODUCT_SERVICE_CANON.md`
- `00__LOCKED__UPLOAD_SET/02__Repositories/GLOBAL_PRODUCT_NAMING_REGISTRY_v1.0.md`
- `00__LOCKED__UPLOAD_SET/02__Repositories/GLOBAL_VEHICLE_CLASSIFICATION_REPOSITORY.md`

Rule:
Service truth and repository truth must not be invented in phrase files or test packs.

### 2.10 Education layer
These files govern structured education and reusable explanation assets:

- `00__LOCKED__UPLOAD_SET/00__Runtime/PHASE7__CORE_EDUCATION.md`
- `00__LOCKED__UPLOAD_SET/00__Runtime/PHASE7_EDUCATION_SNIPPETS.md`
- `00__LOCKED__UPLOAD_SET/00__Runtime/EDUCATION_TRIGGER_MATRIX.md`

### 2.11 Visual intelligence layer
These files govern approved visual routing and video references:

- `00__LOCKED__UPLOAD_SET/00__Runtime/PHASE8_VISUAL_INTELLIGENCE_MAP.md`
- `00__LOCKED__UPLOAD_SET/00__Runtime/PHASE8_VIDEO_LIBRARY.md`

Related control references:
- `00__CONTROL_TOWER/VIDEO_LIBRARY_INDEX.md`
- `00__CONTROL_TOWER/VIDEO_TRIGGER_MATRIX.md`

### 2.12 Parameter layer
These files define global and dynamic runtime parameters:

- `00__LOCKED__UPLOAD_SET/03__Parameters/GLOBAL_CORE_CONTEXT_PARAMETERS.md`
- `00__LOCKED__UPLOAD_SET/03__Parameters/CONVERSATION_DYNAMIC_PARAMETERS.md`

Rule:
If behavior depends on a parameter, confirm the parameter layer before patching phrase or engine logic.

### 2.13 Practical patch tracing rule
When a defect appears, trace it in this order:

1. intake / qualification output shape
2. orchestration and readiness
3. assembly precedence
4. phrase selection
5. runner prompt forcing
6. UAT harness normalization/injection
7. test expectation shape

This prevents patching the wrong authority file.

## 3. Tooling and Enforcement Layer

The repo has an active validation and enforcement layer through:

### GitHub workflows
- `.github/workflows/governance.yml`
- `.github/workflows/runtime_checks.yml`
- `.github/workflows/runtime_freeze.yml`
- `.github/workflows/uat.yml`

### Runner layer
- `runner/governance_pipeline.py`
- `runner/check_arch_changelog.py`
- `runner/lint_authority.py`
- `runner/check_phrase_authority.py`
- `runner/check_phrase_trigger_conflicts.py`
- `runner/phrase_library_validator.py`
- `runner/run_uat.py`

### Tooling layer
- `tools/runtime_integrity_check.py`
- `tools/file_authority_guard.py`
- `tools/conversation_governance_check.py`
- `tools/control_tower.py`

Purpose of this layer:
- block invalid runtime changes
- reduce duplicate authority creation
- validate phrase integrity
- validate routing references
- validate repo hygiene before commit

Rule:
A patch is not considered safe just because the text looks correct.
It must pass through the enforcement layer.

---

## 4. Test and UAT Layer

Main test layers include:

- `tests/regression_cases_uat.json`
- `tests/smoke/post_merge_smoke.json`
- `tests/uat/`
- `tests/reports/`

Meaning of layers:

- regression = broad behavior protection
- smoke = quick confidence checks
- tests/uat = focused audit packs and targeted defect guards
- reports = execution evidence

Recent targeted packs added for strict validation include:
- reentered-context audit
- reentered-context strict phrase check
- Phase 3B transition verbatim audit
- Phase 3 gate and behavior packs

Rule:
When a defect is identified, create or strengthen the narrowest failing pack first before changing runtime authority.

---

## 5. Control Tower Layer

Control Tower files exist to explain, organize, and track the project.

This layer must not be treated as runtime execution authority unless a specific tool explicitly depends on a file.

Current control-tower files include:
- `00__CONTROL_TOWER/ARCHITECTURE_DECISIONS.md`
- `00__CONTROL_TOWER/ARCHITECTURE_TASK_LEDGER.md`
- `00__CONTROL_TOWER/RUNTIME_FILE_INVENTORY.md`
- `00__CONTROL_TOWER/SNASH_PHASE_REGISTRY.md`
- `00__CONTROL_TOWER/SYSTEM_STATE.md`
- roadmap / visual / trust working references

Control Tower use:
- project understanding
- architecture tracking
- state summaries
- future planning
- phase registry
- non-runtime working references

Rule:
Control Tower explains the system.
Locked runtime executes the system.

---

## 6. Legacy and Reference Archive Layer

Legacy or shadow documents that may still have historical value must not sit in the active root if they can be mistaken for live authority.

Current legacy archive location:
- `notes/legacy_root_docs_20260412/`

These files are preserved for reference/history only.

They are not live runtime authority unless explicitly restored and re-approved.

Rule:
Preserve history, but do not let old root files compete with active runtime governance.

---

## 7. Notes and Evidence Layer

Working evidence, audits, and patch investigation notes belong under:

- `notes/patch_sessions/`

These notes may contain:
- defect findings
- audit reasoning
- test observations
- gate rules
- local due-diligence conclusions

These are useful for investigation and traceability, but they are not runtime authority.

Rule:
Notes may support a patch decision.
Notes must not override runtime authority.

---

## 8. Patch Workflow (Operational)

Every patch should follow this order:

1. Confirm the file role
   - runtime authority
   - control tower
   - tooling
   - test/UAT
   - legacy/reference

2. Prove the raw defect
   - failing output
   - failing debug state
   - failing pack or reproducible case

3. Check whether the issue is actually in:
   - runtime doctrine
   - runner prompt forcing
   - UAT harness behavior
   - test expectation
   - tool logic
   - duplicate or shadow authority

4. Choose the narrowest correct patch target

5. Define validation before patching
   - exact packs
   - nearby smoke/regression
   - integrity/governance checks

6. Patch

7. Validate

8. Commit runtime/tooling changes separately from cleanup/archive changes

Rule:
Never mix runtime fixes and repo cleanup in the same commit unless there is a very strong reason.

---

## 9. Current Known Live Branch Context

Current working branch for cleanup and patch discipline:
- `chore/pre_cleanup_snapshot_20260412`

Recent confirmed commits on this branch include:
- validated runtime/UAT checkpoint for reentered continue and strict Phase 3B guards
- relocation of legacy root governance docs into notes archive

This branch has been used to:
- clean authority confusion
- preserve reference documents safely
- keep validated runtime changes separate from cleanup work

---

## 10. Current High-Risk Areas

High-risk areas where wrong-file patching can happen:

- Phase 0–2 vs Phase 3A boundary
- Phase 3B strict price-ready behavior
- assembly precedence vs missing-phrase confusion
- support-routing vs business-info precedence
- duplicate governance text in root vs locked runtime
- tooling/UAT normalization falsely shaping output

Rule:
If the same concept appears in multiple files, authority must be confirmed before patching.

---

## 11. What Must Never Be Patched Blindly

Never patch blindly when the issue may actually belong to:
- `runner/context_reset_prompt.txt`
- `runner/run_uat.py`
- `tools/runtime_integrity_check.py`
- `00__LOCKED__UPLOAD_SET/00__Runtime/PHASE4_8_MESSAGE_ASSEMBLY_MAP.md`
- `00__LOCKED__UPLOAD_SET/01__Engines/QUALIFICATION_ENGINE.md`
- test pack expectations

Never patch customer-facing phrases just because output looks wrong before checking:
- route selection
- prompt forcing
- harness token injection
- wrong selected_phrase_id
- missing authority precedence

---

## 12. Operating Rule for Future Work

Before any future runtime patch:
- start from this file
- identify the layer involved
- identify the true authority file
- identify the validation path
- only then patch

This file is the repo operating map.
It exists to reduce memory dependence, prevent drift, and keep patching traceable.
