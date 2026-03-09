import subprocess
import sys

checks = [
    "python tools/conversation_governance_check.py",
    "python tools/phrase_risk_audit.py",
    "python tools/snippet_return_anchor_check.py",
    "python tools/education_matrix_check.py",
    "python tools/bilingual_phrase_audit.py",
    "python tools/runtime_guardian.py"
]

print("Running governance validation pipeline...\n")

for check in checks:
    print(f"Running: {check}")
    result = subprocess.run(check, shell=True)

    if result.returncode != 0:
        print("\n❌ Governance check FAILED:", check)
        sys.exit(1)

print("\n✅ All governance checks passed.")
