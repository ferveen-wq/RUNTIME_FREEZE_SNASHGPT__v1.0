# 03_DRIFT_AND_FAILURE_CLASSIFICATION.md

Status: DRAFT
Purpose: Define how observed issues are classified so the correct authority is targeted and incorrect patching is avoided.
Scope: Classification only. This file does not define runtime behavior or patch logic.

---

## 1. Core Rule

Not every incorrect output is a runtime bug.

Every issue must be classified before:
- patching
- assigning file ownership
- modifying architecture or governance

---

## 2. Primary Failure Types

### 2.1 Runtime Behavior Issue

Definition:
- behavior contradicts runtime authority files
- routing, qualification, or message logic is incorrect despite correct inputs

Examples:
- wrong service routing
- incorrect phase progression
- violating locked constraints (pricing too early, wrong sequence)
- message assembly breaking defined rules

Target:
- runtime authority files

Rule:
- patch only after verifying runtime logic is actually wrong

---

### 2.2 Test / Harness Issue

Definition:
- test setup is incorrect or incomplete
- prompts do not reflect real flow
- context conditions are invalid

Examples:
- skipping qualification steps
- injecting late-stage prompts without setup
- mixing new chat and continuation incorrectly
- testing outside project when scenario requires inside

Target:
- test design, not runtime

Rule:
- fix test setup, not system behavior

---

### 2.3 Context / Session Issue

Definition:
- behavior is affected by chat state, memory stacking, or session instability

Examples:
- inconsistent results across chats
- restart-like responses
- loss of context continuity
- degraded responses after long sessions

Target:
- testing discipline / session control

Rule:
- reset context and re-test before classifying as runtime issue

---

### 2.4 Project Instruction Drift

Definition:
- behavior differs due to project-layer instructions, not runtime logic

Examples:
- inside project vs outside project mismatch
- assistant paraphrasing or over-interpreting
- behavior not matching runtime files despite correct logic

Target:
- project instructions / execution layer

Rule:
- verify whether issue exists outside project before patching runtime

---

### 2.5 Phrase / Message Construction Issue

Definition:
- logic is correct but wording, tone, or phrasing is incorrect

Examples:
- wrong tone (too salesy, too weak, too generic)
- incorrect phrasing for sensitive scenarios
- phrase conflicts or leakage across services

Target:
- phrase library / message construction layer

Rule:
- do not patch routing/logic for wording problems

---

### 2.6 Governance / Process Issue

Definition:
- correct behavior exists but process was violated

Examples:
- patch done without ledger update
- patch done without validation
- patch applied to wrong file
- duplicate authority created

Target:
- governance discipline, not runtime

Rule:
- fix process, not system behavior

---

### 2.7 Unknown / Unclassified

Definition:
- issue cannot be confidently assigned

Examples:
- inconsistent behavior with no clear pattern
- conflicting signals across tests

Rule:
- do not patch
- gather more evidence
- escalate classification later

---

## 3. Misclassification Risks

Common mistakes:

### 3.1 Treating Test Issues as Runtime Bugs
Result:
- unnecessary patches
- system instability

---

### 3.2 Treating Phrase Issues as Logic Issues
Result:
- breaking working logic
- introducing new routing errors

---

### 3.3 Treating Context Issues as System Failures
Result:
- patching stable systems
- masking testing problems

---

### 3.4 Treating Project Drift as Runtime Failure
Result:
- incorrect file-level patching
- misaligned fixes

---

## 4. Classification Workflow

For every issue:

Step 1:
- confirm test setup (new vs continuation, inside vs outside)

Step 2:
- repeat test in clean conditions

Step 3:
- compare behavior:
  - consistent → likely real issue
  - inconsistent → likely context/session issue

Step 4:
- check against runtime authority

Step 5:
- assign category:
  - runtime
  - test/harness
  - context/session
  - project instruction
  - phrase layer
  - governance/process

Step 6:
- only after classification → move to patching (if required)

---

## 5. Hard Prohibitions

Do not:
- patch without classification
- assign file ownership before classification
- mix multiple issue types into one fix
- assume first observation is correct

---

## 6. Verified Signals from Project Evidence

- many observed issues were not runtime bugs
- testing context strongly affects behavior
- inside vs outside project creates different outputs
- phrase layer is a major source of drift
- incorrect classification leads to wrong patches

---

## 7. Status Note

This file is derived from:
- `docs/control_tower/00_FOUNDATION_EVIDENCE.md`
- `docs/control_tower/02_TESTING_DISCIPLINE.md`

It should be revised only when stronger written evidence changes classification logic.
