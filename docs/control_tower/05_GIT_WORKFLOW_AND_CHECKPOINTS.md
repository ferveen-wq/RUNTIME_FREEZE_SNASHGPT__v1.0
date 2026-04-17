# 05_GIT_WORKFLOW_AND_CHECKPOINTS.md

Status: DRAFT
Purpose: Define the repo workflow used to keep runtime, docs, testing, and governance work traceable and non-drifting.
Scope: Git workflow and checkpoint discipline only. This file does not define runtime behavior itself.

---

## 1. Core Rule

Repository history must make it possible to answer:
- what changed
- why it changed
- whether it was docs, runtime, test, or governance work
- whether it was validated
- whether it reached checkpoint / tag / merge status

If repo history cannot answer those questions cleanly, the workflow is too loose.

---

## 2. Working-Tree Discipline

Before staging or committing:
- inspect current status
- identify unrelated dirty files
- separate noise from intended work
- avoid mixing backup/scratch artifacts with real tracked changes

Rule:
- do not commit from a confused working tree
- do not let runtime, docs, and test changes blend accidentally

---

## 3. Commit Stream Separation

Preferred separation:
- docs-only commits
- runtime-fix commits
- test-pack commits
- governance/control-tower commits

Rule:
- keep different work types separate where reasonably possible
- do not hide runtime changes inside a docs commit
- do not hide docs-only updates inside a runtime fix commit

---

## 4. Validation Before Commit

Before completing a meaningful commit:
- run the required repo validation path
- use existing governance / validation checks
- confirm failures are understood before retrying

Current repo evidence confirms commit-time validation includes checks such as:
- arch changelog generation / gate
- phrase authority gate
- phrase trigger conflict detector
- runtime diff sentinel
- governance pipeline
- phrase diff visualizer
- control tower checks

Rule:
- validation comes before trust
- passing memory is irrelevant; passing checks matters

---
## 4A. Local Environment / Tooling Discipline

Current repo evidence confirms:
- `.venv/` is intentionally excluded from git tracking
- local validation is configured through `.pre-commit-config.yaml`
- `ruff` is part of local pre-commit enforcement

Operational rule:
- use the intended local environment for repo work
- do not treat ad hoc local setup as equivalent to validated repo workflow
- local validation setup should remain clean and reproducible

---

## 4B. Pre-Commit / Lint Discipline

Current repo evidence confirms local pre-commit includes:
- `check-json`
- `ruff`
- architecture changelog generation / gate
- phrase authority checks
- phrase trigger conflict checks
- runtime diff sentinel
- governance pipeline
- phrase diff visualizer
- control tower commit checks

Rule:
- pre-commit is part of normal repo workflow, not optional decoration
- lint / hook failures must be understood before commit completion
- do not bypass local validation mentally just because discussion says a change is correct

---

## 4C. GitHub Workflow / CI Discipline

Current repo evidence confirms GitHub workflow coverage for:
- governance checks
- runtime checks
- runtime freeze
- UAT

Current repo evidence also confirms workflow triggers include:
- `push`
- `pull_request`
- `workflow_dispatch`

Rule:
- local validation and GitHub validation are related but not identical
- passing local checks does not erase CI responsibility
- repo workflow decisions should remain aware of push / PR / CI consequences

---

## 5. Runtime Patch Commit Discipline

For runtime-affecting work:
- use governance/change-control rules before commit preparation
- confirm target authority before staging
- ensure ledger/protocol/governance requirements are already satisfied
- validate before status promotion
- only then finalize commit flow

Rule:
- this file governs repo workflow, not runtime patch authority by itself
- do not commit runtime-affecting work as if discussion alone proved completion

---



## 6A. Enforced Session Entry

Before real repo work in a fresh shell session, enter through the enforced repo entrypoint:

- shell command: `snash`
- underlying script: `tools/start_lane.sh`

This entry flow is expected to:
- move into the correct repo
- run session bootstrap
- run patch gate
- show current Phase 4 UAT inventory
- show working-tree state before patch/commit activity

Rule:
- do not start patching or commit work in a fresh shell session by relying on memory alone
- use enforced repo entry before real work begins
- if enforced entry tooling changes, update this document and the supporting tooling together

## 6. Docs / Architecture Commit Discipline

For docs-only work:
- confirm no runtime behavior is being changed
- keep docs changes explicit
- separate architecture alignment from runtime modification
- preserve promotion trace when moving evidence into architecture/control-tower docs

Rule:
- docs commits may document runtime truth
- docs commits must not pretend to be runtime fixes unless runtime actually changed

---

## 7. Checkpoint and Tag Discipline

Use checkpoints/tags when:
- a phase baseline becomes stable
- a meaningful runtime freeze point is reached
- a validated sweep is completed
- a bridge/release/promotable state is reached

Current repo evidence confirms:
- checkpoint-style tags are actively used
- phase-specific tags are actively used
- runtime release / freeze tags are actively used

Rule:
- tag meaningful states, not noise
- checkpoint names should help future re-anchoring, not add confusion

---

## 8. Branch Reality and Local Discipline

Current repo evidence confirms active branch-based work.

Operational rule:
- know the current branch before major work
- avoid patching blindly without branch awareness
- verify whether work belongs on the active branch before committing

This file does not yet define final branch naming policy.
That may be added later if stronger written evidence is collected.

---

## 9. Push / PR Discipline

Push after:
- change scope is clear
- validation has passed
- commit meaning is clean
- ledger/status truth is not contradicted

Current repo evidence confirms push / pull_request are part of GitHub workflow governance.

Rule:
- do not push ambiguous state
- do not treat push as a substitute for local discipline
- remain aware that repo governance continues at PR / CI level after local commit flow
- do not rely on remote history to clean up local governance confusion

---

## 10. Hard Prohibitions

Do not:
- commit from memory
- mix unrelated work streams casually
- treat tags as decoration
- claim validation without actual validation
- rely on chat recollection instead of repo history

---

## 11. Current Verified Repo Signals

Verified from current project evidence:
- active branch-based work is in use
- explicit docs / fix / test commit separation exists in recent history
- checkpoint and release tags are actively used
- governance and validation checks run during commit flow
- repo history is part of the project’s anti-drift control system

---

## 12. Status Note

This file is derived from:
- `docs/control_tower/00_FOUNDATION_EVIDENCE.md`
- `docs/control_tower/01_SOURCE_OF_TRUTH_ORDER.md`
- `docs/control_tower/04_GOVERNANCE_AND_CHANGE_CONTROL.md`

It should be revised only when stronger written evidence changes the repo workflow model.
