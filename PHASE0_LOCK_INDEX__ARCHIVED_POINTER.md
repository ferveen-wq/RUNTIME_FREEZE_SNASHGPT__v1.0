# PHASE0_LOCK_INDEX.md

Version: 1.0
Status: LOCKED
Scope: Phase 0 — Lock Index (Audit Anchor)

Locked Files:
1) RUNTIME_LOAD_MANIFEST.md (v1.3)
2) KNOWLEDGE__RUNTIME_CORE_BUNDLE.md (v1.0)

Lock Rule:
- No edits to locked files unless:
  - architecture review is done
  - version increment is applied
  - change is logged in this file

Change Log:
- 2026-01-05 – Phase 0 locked (manifest + core bundle)
- 2026-01-05 – Manifest updated to v1.2 (Visual Playbook provision added)
- 2026-01-06 – Orchestration integrity sealed: Qualification emits QUALIFICATION_STATUS gate; Negotiation enforces entry precondition; Output template added; Legacy qualification matrix archived.

## Parameter Layer (v1.0) — LOCKED
- 02__Parameters/GLOBAL_CORE_CONTEXT_PARAMETERS.md
- 02__Parameters/CONVERSATION_DYNAMIC_PARAMETERS.md

Status: LOCKED
Notes:
- Core and dynamic parameter layers finalized and frozen.
- All engines must read parameters from these files only.
- Any changes require version bump and review.