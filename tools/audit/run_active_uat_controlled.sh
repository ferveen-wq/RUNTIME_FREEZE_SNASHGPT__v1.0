#!/usr/bin/env bash
set -euo pipefail

printf '\n===== CONTROLLED ACTIVE UAT =====\n'

if [ -z "${UAT_CASES_FILE:-}" ]; then
  echo "[FAIL] UAT_CASES_FILE is required"
  exit 1
fi

case "$UAT_CASES_FILE" in
  tests/active_rollout_uat/*) ;;
  *)
    echo "[FAIL] Active UAT must use tests/active_rollout_uat/"
    echo "Got: $UAT_CASES_FILE"
    exit 1
    ;;
esac

printf '\n===== PRE-UAT GUARD =====\n'
python tools/audit/pre_uat_guard.py

printf '\n===== RAW ACTIVE UAT =====\n'
python runner/run_active_uat_raw.py

printf '\n===== REPORT ANALYZER =====\n'
python tools/audit/report_analyzer.py

printf '\n[OK] Controlled active UAT completed.\n'
