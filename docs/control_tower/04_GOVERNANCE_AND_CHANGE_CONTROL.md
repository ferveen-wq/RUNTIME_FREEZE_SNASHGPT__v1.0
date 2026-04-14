# 04_GOVERNANCE_AND_CHANGE_CONTROL.md

Status: DRAFT
Purpose: Define how changes are governed, reviewed, promoted, deferred, and controlled so the system does not drift.
Scope: Governance and change-control only. This file does not define runtime behavior itself.

---

## 1. Core Governance Rule

No runtime, architecture, or control-tower change should proceed from memory, assumption, or chat momentum alone.

All meaningful changes must be grounded in written project evidence.

---

## 2. Change-Control Modes

### 2.1 Runtime Patch Mode

Use when:
- runtime behavior must change
- a runtime bug is confirmed
- a runtime authority file requires update

Required controls:
- confirm the target file is the correct authority using source-of-truth order
- check ledger status before patch execution
- check patch protocol before patch execution
- check phrase governance before phrase-related runtime edits
- patch minimally
- validate before status promotion

---

### 2.2 Architecture Promotion Mode

Use when:
- temp evidence is being promoted into architecture docs
- reconciled findings are being normalized
- runtime truth is being documented, not changed

Required controls:
- confirm evidence exists in written form
- confirm reconciliation is complete
- confirm no duplicate entry already exists
- confirm architecture summary does not override runtime authority
- record promotion trail

---

### 2.3 Control-Tower Drafting Mode

Use when:
- governance memory is being normalized into control-tower docs
- source-of-truth order is being documented
- testing discipline or git workflow is being formalized

Required controls:
- use foundation evidence first
- do not create new technical doctrine
- do not duplicate runtime authority
- do not turn historical reconstruction into final policy without verification

---

### 2.4 Testing / Observation Mode

Use when:
- behavior is being observed
- issue type is being classified
- runtime vs harness vs governance distinction is still unresolved

Required controls:
- do not fix during observation
- do not assign patch ownership too early
- do not promote observations directly into runtime or architecture
- capture evidence first

---

## 3. Audit-Before-Change Rule

Before any meaningful change:
- inspect the target file
- inspect surrounding logic
- inspect adjacent authority files when relevant
- check whether similar logic already exists
- confirm whether the issue is runtime, harness, governance, or documentation only

Rule:
- no patch-on-patch behavior
- no parallel authority creation
- no change from partial recollection

---

## 4. Ledger-First Rule

For runtime-affecting work:
- ledger status must be checked before patching
- discussed-but-unpatched work must not be treated as implemented
- deferred work must remain explicitly deferred until reactivated through normal governance flow

Rule:
- discussion is not implementation
- intention is not status
- memory is not status truth

---

## 5. Minimal-Patch Rule

All changes should be as small as possible while still resolving the confirmed issue.

Preferred behavior:
- update existing authority where possible
- avoid creating parallel files for the same behavior
- avoid broad rewrites when a local fix is sufficient
- separate docs-only, runtime, and test-only work where possible

---

## 6. No-Duplicate-Authority Rule

Do not:
- create a second authority for behavior already owned elsewhere
- let architecture docs compete with runtime files
- let governance notes compete with ledger/protocol truth
- let support tooling become undocumented authority

If a rule already exists:
- strengthen or clarify the existing authority
- do not create a competing version

---

## 7. Defer-vs-Patch Rule

Defer when:
- evidence is incomplete
- ownership is unclear
- runtime vs harness distinction is unresolved
- issue is historical but not currently proven
- later-phase certainty is partial

Patch when:
- issue is written, verified, and assigned to the correct authority
- file ownership is clear
- patch scope is minimal and testable

Rule:
- defer explicitly, not mentally

---

## 8. Promotion-Control Rule

Nothing should move into real architecture or control-tower policy unless:
- evidence is written
- uncertainty is known
- duplicate check is complete
- target document is the correct authority layer

Examples:
- temp evidence does not go straight into runtime docs
- reconstruction notes do not become policy without verification
- test findings do not become runtime bug claims without classification

---

## 9. Hard Prohibitions

Do not:
- patch from memory
- patch from chat pressure
- treat reconstruction as final truth
- promote unresolved uncertainty into policy
- mix runtime patching, testing, and architecture promotion into one uncontrolled step

---

## 10. Current Verified Governance Signals

Verified from current project evidence:
- audit before patch
- ledger-first runtime patch discipline
- protocol/governance checks before patch
- phrase-governance check before phrase-related runtime edits
- discussed work and patched work are distinct
- memory recovery is separate from patching
- control-tower docs must summarize and govern, not duplicate runtime doctrine

---

## 11. Status Note

This file is derived from:
- `docs/control_tower/00_FOUNDATION_EVIDENCE.md`
- `docs/control_tower/01_SOURCE_OF_TRUTH_ORDER.md`

It should be revised only when stronger written evidence changes the governance model.
