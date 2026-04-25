#!/usr/bin/env bash
set -euo pipefail

echo ""
echo "===== PHASE 0–2 CLOSEOUT RUN ====="
echo ""

if [ "${CLOSEOUT_CONFIRM:-NO}" != "YES" ]; then
  echo "[FAIL] Full closeout runs multiple API-backed UAT cases."
  echo "Set CLOSEOUT_CONFIRM=YES only when you intentionally want to spend credits."
  echo "For debugging, run a single CASE_ID with tools/audit/run_active_uat_controlled.sh."
  exit 1
fi

# 1. Activate environment
source .venv/bin/activate

# 2. Pre-guard check
echo ""
echo "===== PRE-GUARD ====="
python3 tools/audit/pre_uat_guard.py

# 3. Run intake matrix
echo ""
echo "===== INTAKE MATRIX ====="
RAW_UAT_CONFIRM=YES \
UAT_CASES_FILE=tests/active_rollout_uat/phase0_2_intake_matrix.json \
tools/audit/run_active_uat_controlled.sh

# 4. Run alias + offscope + support matrix
echo ""
echo "===== ALIAS / OFFSCOPE / SUPPORT ====="
RAW_UAT_CONFIRM=YES \
UAT_CASES_FILE=tests/active_rollout_uat/phase0_2_alias_offscope_support.json \
tools/audit/run_active_uat_controlled.sh

# 5. Final status
echo ""
echo "===== PHASE 0–2 CLOSEOUT COMPLETE ====="
echo ""
echo "Review report analyzer output above. Any FAIL means Phase 0–2 is NOT closed."
