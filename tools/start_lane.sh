#!/usr/bin/env bash
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$REPO_ROOT"

printf '\n============================================================\n'
printf 'SNASH START LANE\n'
printf '============================================================\n'
printf 'Repo: %s\n' "$REPO_ROOT"
printf 'Date: %s\n' "$(date)"

printf '\n===== 1) SESSION BOOTSTRAP =====\n'
bash tools/session_bootstrap.sh

printf '\n===== 2) PATCH GATE =====\n'
bash tools/patch_gate.sh

printf '\n===== 3) ACTIVE PHASE4 UAT =====\n'
find tests/uat -maxdepth 1 -type f | sort | grep 'phase4' || true

printf '\n===== 4) GIT STATUS =====\n'
git status --short || true

printf '\n[OK] start lane completed\n'

touch .snash_session_started
touch .snash_patch_gate_reviewed
