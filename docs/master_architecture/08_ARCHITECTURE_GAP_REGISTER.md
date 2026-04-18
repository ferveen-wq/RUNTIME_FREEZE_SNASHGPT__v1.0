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
Title: Phase 6 service-truth authority is runtime-active, but the render contract between Phase 6 canon and Phase 4.8 assembly is not explicitly defined
Source:
- PHASE4_8_MESSAGE_ASSEMBLY_MAP.md
- PHASE6__SERVICE_CANON_BUNDLE.md
- RUNTIME_LOAD_MANIFEST.md
Impact:
- Ambiguity over when Phase 6 service truth may be surfaced in customer-facing output
- Ambiguity over whether Phase 4.8 is selecting bounded service content from Phase 6 versus blocking direct raw canon emission in specific routes
- Phase 6 testing cannot be fully trusted until the routing/render contract is stated explicitly
Status: OPEN
Notes:
- PHASE6__SERVICE_CANON_BUNDLE.md is manifest-proven runtime-active
- PHASE4_8_MESSAGE_ASSEMBLY_MAP.md remains the final assembly/render authority
- The unresolved issue is not whether Phase 6 is active, but how Phase 6 content is legally consumed and rendered by Phase 4.8

---

────────────────────────────────────────────
SECTION 6 — FUTURE PHASE 4 LOGGING
────────────────────────────────────────────

All Phase 4 findings MUST be logged below using same format:

GAP-XXX
Type:
Title:
Source:
Impact:
Status: OPEN

────────────────────────────────────────────
END OF FILE
