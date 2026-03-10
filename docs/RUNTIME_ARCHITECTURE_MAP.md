# SNASHGPT Runtime Architecture Map

Purpose:
This document explains the major components of the SNASHGPT system so the project remains understandable as it grows.

This file is documentation only and is NOT part of runtime execution.

---

# 1. Runtime Layer (AI Behaviour)

Location:
00__LOCKED__UPLOAD_SET/00__Runtime/

These files define how the AI speaks and makes decisions.

Examples:

PHASE4_6_HUMAN_PHRASE_LIBRARY.md  
Human conversational phrases used by the AI.

PHASE4_8_MESSAGE_ASSEMBLY_MAP.md  
Rules for building messages.

QUALIFICATION_ENGINE.md  
Logic for qualifying customers.

EDUCATION_TRIGGER_MATRIX.md  
Rules for when education responses should be used.

PHRASE_INDEX.md  
Index used to locate phrases and avoid conflicts.

---

# 2. Governance Layer (Safety)

Location:
runner/

These scripts protect runtime stability.

Examples:

check_arch_changelog.py  
Ensures architecture changes are logged.

generate_arch_changelog.py  
Auto-inserts changelog templates.

runtime_diff_sentinel.py  
Prevents dangerous deletions.

check_phrase_authority.py  
Prevents duplicate authoritative phrases.

check_phrase_trigger_conflicts.py  
Prevents trigger conflicts in phrase index.

---

# 3. Testing & Debugging

Location:
runner/

Tools used during testing and development.

Examples:

phrase_diff_visualizer.py  
Displays phrase changes during commits.

runtime_trace.py  
Shows runtime decision path during testing.

---

# 4. Infrastructure

Location:
.github/workflows/

Automation for CI and testing.

Examples:

governance.yml  
Runs governance checks in CI.

uat.yml  
Runs automated tests.

runtime_freeze.yml  
Creates runtime snapshots after successful runs.

---

# Development Rule

New files must belong to one of the following categories:

Runtime  
Governance  
Testing  
Infrastructure

If a file does not fit one of these categories, it should not be created.

