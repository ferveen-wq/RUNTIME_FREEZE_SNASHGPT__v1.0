#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
LOCKED_ROOT="$ROOT/00__LOCKED__UPLOAD_SET"

PHASE46="$LOCKED_ROOT/00__Runtime/PHASE4_6_HUMAN_PHRASE_LIBRARY.md"
ASSEMBLY="$LOCKED_ROOT/00__Runtime/PHASE4_8_MESSAGE_ASSEMBLY_MAP.md"
QUALENG="$LOCKED_ROOT/01__Engines/QUALIFICATION_ENGINE.md"

fail() {
  echo "FAIL: $*" >&2
  exit 1
}

echo "== audit_runtime: start =="

[[ -f "$PHASE46" ]] || fail "Missing file: $PHASE46"
[[ -f "$ASSEMBLY" ]] || fail "Missing file: $ASSEMBLY"
[[ -f "$QUALENG" ]] || fail "Missing file: $QUALENG"

# ------------------------------------------------------------
# 1) Duplicate PHASE3A_Q_* headings in PHASE4_6
# ------------------------------------------------------------
dup_count="$(
  rg -n '^### PHASE3A_Q_' "$PHASE46" \
    | awk '{print $2}' \
    | sort \
    | uniq -c \
    | awk '$1>1{print}' \
    | wc -l \
    | tr -d ' '
)"
if [[ "$dup_count" != "0" ]]; then
  echo "Duplicate PHASE3A_Q_* headings found:"
  rg -n '^### PHASE3A_Q_' "$PHASE46" \
    | awk '{print $2}' \
    | sort \
    | uniq -c \
    | awk '$1>1{print}'
  fail "PHASE4_6_HUMAN_PHRASE_LIBRARY has duplicate PHASE3A_Q_* headings"
fi
echo "OK: no duplicate PHASE3A_Q_* headings in PHASE4_6"

# ------------------------------------------------------------
# Helper: check referenced IDs exist as headings in PHASE4_6
# ------------------------------------------------------------
heading_exists() {
  local id="$1"
  rg -q "^### ${id}$" "$PHASE46"
}

check_refs_in_file() {
  local label="$1"
  local file="$2"
  local missing=0
  while IFS= read -r id; do
    [[ -z "$id" ]] && continue
    if ! heading_exists "$id"; then
      echo "Missing in PHASE4_6: ${id} (referenced by ${label})"
      missing=1
    fi
  done < <(rg -o "PHASE3A_Q_[A-Z0-9_]+" "$file" | sort -u)

  [[ "$missing" == "0" ]] || fail "Some PHASE3A_Q_* references in ${label} are missing in PHASE4_6"
  echo "OK: all PHASE3A_Q_* referenced by ${label} exist in PHASE4_6"
}

# ------------------------------------------------------------
# 2) All Phase3A qualifier IDs referenced by Qualification Engine exist in PHASE4_6
# ------------------------------------------------------------
check_refs_in_file "QUALIFICATION_ENGINE.md" "$QUALENG"

# ------------------------------------------------------------
# 3) All Phase3A qualifier IDs referenced by Assembly Map exist in PHASE4_6
# ------------------------------------------------------------
check_refs_in_file "PHASE4_8_MESSAGE_ASSEMBLY_MAP.md" "$ASSEMBLY"

# ------------------------------------------------------------
# 4) Forbidden routing sanity: WRAP_SCOPE should not be routable by the Phase 3A chain.
#    (It may exist as a phrase block, but must NOT appear as a selectable mapping target.)
# ------------------------------------------------------------
if rg -n "Mapping \(phase3a_qualifier_id → Phrase block\):" "$ASSEMBLY" >/dev/null 2>&1; then
  if rg -n "PHASE3A_Q_WRAP_SCOPE" "$ASSEMBLY" >/dev/null 2>&1; then
    # If it's present in the mapping list, that's a drift risk.
    # Allow it only if it's clearly labeled deprecated/non-route in the assembly map.
    if ! rg -n "PHASE3A_Q_WRAP_SCOPE.*(DEPRECATED|DO NOT ROUTE|NON-AUTHORITY)" "$ASSEMBLY" >/dev/null 2>&1; then
      fail "PHASE3A_Q_WRAP_SCOPE appears in Assembly Map without an explicit non-route/deprecated label"
    fi
  fi
fi
echo "OK: WRAP_SCOPE routing sanity check passed (no unsafe routing detected)"

echo "== audit_runtime: passed =="
