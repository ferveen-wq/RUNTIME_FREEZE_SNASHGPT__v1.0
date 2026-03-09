### 2.4 Phrase library structural validator (required when touching PHASE4_6_HUMAN_PHRASE_LIBRARY.md)
Run the phrase library validator to catch truncations / missing phrase keys before edits:

- python runner/phrase_library_validator.py

If it fails, do not patch. Fix file integrity first.


## Shell / Patch Delivery Standard

- All runtime patch instructions must be delivered in zsh-safe copy/paste format by default.
- Do not use placeholders such as `<change_name>`, `(A)`, `(B)`, or angle-bracket tokens in shell commands.
- Do not include inline shell comments inside copy/paste command blocks unless they are confirmed zsh-safe.
- Prefer exact terminal commands for:
  - branch creation
  - tagging
  - file patching
  - validation
  - commit / push steps
- Use VC Codex only when:
  - the patch is large,
  - spans multiple files,
  - or exact block replacement is too risky in terminal-only form.
- For phrase-only or small runtime edits, prefer zsh-safe terminal patch commands over VC Codex.
- Any patch instruction that is not zsh-safe should be rewritten before execution.


## Phrase Governance and Change Ledger Enforcement

Before any runtime phrase patch or runtime logic patch:

1. Review phrase changes against:
   - 00__LOCKED__UPLOAD_SET/00__Runtime/PHRASE_GOVERNANCE_STANDARD.md

2. Update:
   - 00__LOCKED__UPLOAD_SET/00__Runtime/RUNTIME_CHANGE_LEDGER.md

3. Record the exact status of the change using ledger statuses only:
   - DISCUSSED
   - APPROVED_FOR_PATCH
   - PATCHED_LOCAL
   - VALIDATED_LOCAL
   - PR_OPEN
   - MERGED_MAIN
   - TAGGED_GREEN
   - FROZEN
   - DEFERRED
   - AUDITED_ONLY

4. Record next steps and pending items in the ledger before moving to a different runtime topic.

5. Do not rely on chat memory alone for runtime sequencing.
   - The ledger is the source of truth for:
     - what is discussed
     - what is patched
     - what is validated
     - what is merged
     - what is still pending

6. No runtime patch should proceed if:
   - phrase governance has not been checked for phrase-related edits
   - ledger status is missing or outdated

7. If a change is discussed but not patched, it must still be logged in the ledger as:
   - DISCUSSED
   - APPROVED_FOR_PATCH
   - or DEFERRED

8. If multiple related phrase changes are in progress, they must be tracked as separate ledger entries or clearly grouped under one active change record.

Note:
- This enforcement is process-mandatory.
- Full automatic enforcement may be added later through a checker or hook, but until then, manual ledger update is mandatory before each runtime patch sequence.


## Silence Recovery Enforcement

Before patching any silence-related phrase or recovery path:

1. Confirm the phrase follows this order:
   - clarification opener first
   - hook question only if clarification does not reopen the conversation
   - contextual guidance after hook
   - decision narrowing only after recovery succeeds

2. Do not patch silence phrases that:
   - introduce front PPF early
   - narrow scope before reopening the conversation
   - create comparison loops before the customer re-engages

3. For silence-related phrase edits, review against:
   - 00__LOCKED__UPLOAD_SET/00__Runtime/PHRASE_GOVERNANCE_STANDARD.md
   - 00__LOCKED__UPLOAD_SET/00__Runtime/RUNTIME_CHANGE_LEDGER.md





## PATCH REVIEW CHECKLIST

Before approving any phrase or education snippet patch confirm:

✓ Does not introduce over-education  
✓ Does not introduce early price anchoring  
✓ Does not introduce defensive brand positioning  
✓ Does not exceed education snippet compression limits  
✓ Supports at least one defined customer type  
✓ Maps to existing objection framework  
✓ Maps to buying signal framework  
✓ Does not bypass phase routing logic
