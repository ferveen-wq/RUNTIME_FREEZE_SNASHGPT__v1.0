# 07_CONTROL_TOWER_OPERATING_MODEL.md

Status: DRAFT
Purpose: Define how all control-tower files are used together during real work.
Scope: Operational usage only. This file does not define runtime behavior.

---

## 1. Core Principle

Control Tower exists to:
- prevent drift
- enforce correct sequencing
- separate thinking modes
- ensure correct authority usage

---

## 2. Operating Modes (MANDATORY)

Every action must be in ONE mode:

### 2.1 Testing Mode
Use:
- 02_TESTING_DISCIPLINE.md
- 03_DRIFT_AND_FAILURE_CLASSIFICATION.md

Goal:
- observe behavior
- classify issue

Do NOT:
- patch
- fix
- assume cause

---

### 2.2 Classification Mode
Use:
- 03_DRIFT_AND_FAILURE_CLASSIFICATION.md
- 01_SOURCE_OF_TRUTH_ORDER.md

Goal:
- identify correct issue type
- identify correct authority layer

---

### 2.3 Patch Decision Mode
Use:
- 01_SOURCE_OF_TRUTH_ORDER.md
- 04_GOVERNANCE_AND_CHANGE_CONTROL.md

Goal:
- decide if patch is required
- confirm correct file ownership

---

### 2.4 Runtime Patch Mode
Use:
- 04_GOVERNANCE_AND_CHANGE_CONTROL.md
- RUNTIME_CHANGE_LEDGER.md
- tools/patch_gate.sh

Goal:
- execute controlled patch

---

### 2.5 Repo Commit Mode
Use:
- 05_GIT_WORKFLOW_AND_CHECKPOINTS.md

Goal:
- commit clean, validated changes

---

### 2.6 Control Tower Update Mode
Use:
- 06_PHASE_AUDIT_BOARD.md

Goal:
- reflect REAL system state
- not assumptions

---

## 3. Mandatory Sequence

Every issue must follow:

1. TEST (observe only)
2. CLASSIFY (type of issue)
3. VERIFY (against runtime authority)
4. DECIDE (patch vs defer)
5. PATCH (if required)
6. VALIDATE
7. COMMIT
8. UPDATE CONTROL TOWER

---

## 4. Hard Rules

- No skipping steps
- No patch before classification
- No classification without clean test
- No commit without validation
- No control-tower update without proof

---

## 5. Anti-Drift Enforcement

This system prevents:
- memory-based decisions
- duplicate authority creation
- incorrect patch ownership
- mixing testing and fixing
- repo history confusion

---



## 6A. Mandatory Shell Entry

For a fresh shell session, operational entry should begin with:

- `snash`

This routes through:
- `tools/start_lane.sh`
- `tools/session_bootstrap.sh`
- `tools/patch_gate.sh`

Purpose:
- reduce memory-based startup drift
- expose repo state before work starts
- keep bootstrap and gate usage consistent

This does not replace source-of-truth review.
It enforces the startup path that leads into it.

## 6. Daily Usage

At any point ask:

- “Which mode am I in?”
- “Which file governs this step?”
- “Am I skipping a layer?”

If unclear:
→ return to SOURCE_OF_TRUTH_ORDER.md

---

## 7. Status Note

This file binds together:

- 00_FOUNDATION_EVIDENCE.md
- 01_SOURCE_OF_TRUTH_ORDER.md
- 02_TESTING_DISCIPLINE.md
- 03_DRIFT_AND_FAILURE_CLASSIFICATION.md
- 04_GOVERNANCE_AND_CHANGE_CONTROL.md
- 05_GIT_WORKFLOW_AND_CHECKPOINTS.md
- 06_PHASE_AUDIT_BOARD.md

It is the operational entry point for all future work.
