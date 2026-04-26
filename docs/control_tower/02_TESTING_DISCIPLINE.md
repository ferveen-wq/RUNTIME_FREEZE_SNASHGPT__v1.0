# 02_TESTING_DISCIPLINE.md

Status: DRAFT
Purpose: Define how testing is executed, isolated, and interpreted so results are reliable and do not introduce drift.
Scope: Testing discipline only. This file does not define runtime behavior or patch logic.

---

## 1. Core Rule

Testing must reveal behavior — not create behavior.

Do not mix testing with fixing, patching, or architecture decisions in the same step.

---

## 2. Testing Modes

### 2.1 New Chat (Fresh Context)

Use when:
- validating baseline behavior
- testing first-turn responses
- testing price, routing, or qualification entry
- testing clean scenarios without prior context

Definition:
- completely fresh conversation
- no prior turns influencing behavior

Rule:
- new chat is the default testing mode unless explicitly stated otherwise

---

### 2.2 Continuing Chat (Context-Carried)

Use when:
- testing multi-turn flows
- testing qualification progression
- testing objection handling after recommendation
- testing service switching or re-entry behavior

Definition:
- conversation continues from prior turns
- context intentionally influences behavior

Rule:
- do not use continuation unless the test explicitly requires it

---

## 3. Context Control Rules

### 3.1 New Chat Reset Discipline

Observed evidence:
- new chat does not always guarantee clean state
- project context may still attach
- long sessions cause memory stacking and instability

Required practice:
- use NEW CHAT for each test block unless continuation is required
- after 3–5 blocks, reset to a new chat
- avoid long, unbroken test sessions

---

### 3.2 Inside vs Outside Project

Observed behavior:
- inside project → controlled behavior (instructions + memory)
- outside project → baseline model behavior
- behavior may differ between the two

Usage rule:
- INSIDE PROJECT:
  - final QA
  - behavior validation against architecture
  - sensitive flows (ghosting, objection, multi-step)
- OUTSIDE PROJECT:
  - baseline sanity checks
  - drift detection
  - comparison testing

Rule:
- do not mix conclusions between inside/outside without noting the context

---

## 4. Test Isolation Rule

Each test must clearly define:
- new chat or continuation
- inside project or outside project
- exact prompt used
- expected behavior type (routing, qualification, tone, etc.)

Rule:
- unclear test setup = unreliable result

---

## 5. Observation-Only Rule

During testing:
- do not fix
- do not patch
- do not adjust prompts to "force" correct behavior
- do not assign file ownership prematurely

Instead:
- capture behavior as-is
- classify issue:
  - runtime issue
  - harness/test issue
  - governance issue
  - unclear / needs investigation

Rule:
- testing produces evidence, not solutions
- any attempt to "correct" behavior during testing invalidates the test

---

## 6. Drift Detection Signals

Treat these as indicators of potential drift:
- inconsistent answers across new chats
- different behavior inside vs outside project
- loss of context continuity
- restart-like responses mid-conversation
- routing inconsistency
- unexpected phrasing or tone variation

Rule:
- detect first, diagnose later

---

## 7. Multi-Turn Testing Discipline

For multi-turn scenarios:
- start from a clean new chat
- allow conversation to naturally reach the required state
- do not inject late-stage prompts without setup
- do not skip qualification phases artificially

Rule:
- invalid setup leads to false failures

---

## 8. Test-to-Patch Separation

After testing:
- summarize findings
- verify against runtime evidence
- determine ownership (runtime vs harness vs governance)

Only then:
- move to patching (via governance/change-control rules)

Rule:
- testing and patching are separate modes

---

## 8.1 Pattern Library Enforcement

Before any patch:
- classify the failure pattern
- check whether the same pattern already exists in issue logs, active memory, failure snapshots, or prior UAT reports
- reuse the existing diagnosis/fix playbook if available
- do not re-run a full investigation loop if a trusted prior pattern applies

After any validated patch:
- record the root-cause pattern
- link the issue, failing evidence, fixed evidence, and protecting UAT pack
- note whether the fix changed runtime logic, control prompt, tooling, test contract, or documentation only

Rule:
- every validated patch must leave behind a reusable pattern trail so future fixes become faster and less repetitive

---

## 9. Repeatability Rule

A valid test should be:
- repeatable in a new chat
- consistent across multiple runs (within expected variance)
- explainable via runtime logic or known limitations

Rule:
- non-repeatable behavior must be investigated before patching

---

## 10. Hard Prohibitions

Do not:
- test and patch in the same step
- assume one test = system truth
- ignore context conditions (new vs continuation)
- mix inside/outside project results blindly
- treat unstable chat sessions as valid evidence

---

## 11. Current Verified Testing Signals

Verified from project evidence:
- new chat isolation is required for reliable testing
- context overflow and memory stacking affect behavior
- inside vs outside project produces different outputs
- structured block-by-block testing improves reliability
- testing must be explicitly controlled (chat type + context)

---

## 12. Status Note

This file is derived from:
- `docs/control_tower/00_FOUNDATION_EVIDENCE.md`

It should be revised only when stronger written evidence changes testing discipline.
