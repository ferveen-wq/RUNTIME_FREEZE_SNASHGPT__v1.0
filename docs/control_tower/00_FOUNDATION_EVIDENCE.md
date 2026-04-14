# 00_FOUNDATION_EVIDENCE.md

Status: WORKING
Purpose: Capture only verified foundation evidence for control-tower drafting.
Rule: Do not draft policy from chat memory. Only use written evidence captured here.

---

## 1. ACTIVE GOVERNANCE FILES (REPO VERIFIED)

Status:
- populated from repo existence checks
- populated from repo reference checks

Source:
- current repo scan on 2026-04-14
- existence check:
  - 00__LOCKED__UPLOAD_SET/00__Runtime/RUNTIME_CHANGE_LEDGER.md
  - 00__LOCKED__UPLOAD_SET/00__Runtime/PATCH_PROTOCOL.md
  - 00__LOCKED__UPLOAD_SET/00__Runtime/PHRASE_GOVERNANCE_STANDARD.md
- reference check across:
  - 00__LOCKED__UPLOAD_SET
  - runner
  - tools
  - .github
  - docs

Verified active files:
- `00__LOCKED__UPLOAD_SET/00__Runtime/RUNTIME_CHANGE_LEDGER.md`
- `00__LOCKED__UPLOAD_SET/00__Runtime/PATCH_PROTOCOL.md`
- `00__LOCKED__UPLOAD_SET/00__Runtime/PHRASE_GOVERNANCE_STANDARD.md`

Cross-reference evidence:
- `PATCH_PROTOCOL.md` references:
  - `PHRASE_GOVERNANCE_STANDARD.md`
  - `RUNTIME_CHANGE_LEDGER.md`
- `RUNTIME_CHANGE_LEDGER.md` references:
  - `PATCH_PROTOCOL.md`
  - `PHRASE_GOVERNANCE_STANDARD.md`
- `SNASHGPT_MASTER_GOVERNANCE.md` references:
  - `PATCH_PROTOCOL.md`
  - `RUNTIME_CHANGE_LEDGER.md`
- `docs/master_architecture/06_MESSAGE_CONSTRUCTION_MODEL.md` references:
  - `PHRASE_GOVERNANCE_STANDARD.md`
- `docs/master_architecture/00_RUNTIME_FILE_INVENTORY.md` includes:
  - `PATCH_PROTOCOL.md`
  - `PHRASE_GOVERNANCE_STANDARD.md`
  - `RUNTIME_CHANGE_LEDGER.md`

Current evidence status:
- confirmed present in repo
- confirmed referenced in repo
- not treated as deprecated by current evidence

Notes:
- These files are active governance-layer artifacts in the current repo.
- No deprecation claim is allowed unless later repo evidence proves it.


## 2. GOVERNANCE ENFORCEMENT LAYER (REPO VERIFIED)

Status:
- populated from repo scan of runner / tools / workflows
- repo-verified only

Source:
- current repo scan on 2026-04-14
- directories scanned:
  - .github
  - runner
  - tools
  - 00__LOCKED__UPLOAD_SET

Repo-verified enforcement files:
- `.github/workflows/governance-check.yml`
- `.github/workflows/governance.yml`
- `runner/check_arch_changelog.py`
- `runner/check_phrase_authority.py`
- `runner/check_phrase_trigger_conflicts.py`
- `runner/generate_arch_changelog.py`
- `runner/governance_pipeline.py`
- `runner/lint_authority.py`
- `runner/phrase_diff_visualizer.py`
- `runner/phrase_library_validator.py`
- `runner/runtime_diff_sentinel.py`
- `tools/control_tower.py`
- `tools/conversation_governance_check.py`
- `tools/governance_phrase_scan.py`
- `tools/audit/governance_file_scan.py`
- `tools/audit/runtime_architecture_map.py`
- `tools/audit/architecture_graph.py`
- `tools/phrase_library_lock.py`
- `tools/phrase_risk_audit.py`
- `tools/bilingual_phrase_audit.py`

Governance-layer runtime files present in repo:
- `00__LOCKED__UPLOAD_SET/00__Runtime/SNASHGPT_MASTER_GOVERNANCE.md`
- `00__LOCKED__UPLOAD_SET/00__Runtime/PATCH_PROTOCOL.md`
- `00__LOCKED__UPLOAD_SET/00__Runtime/RUNTIME_CHANGE_LEDGER.md`
- `00__LOCKED__UPLOAD_SET/00__Runtime/PHRASE_GOVERNANCE_STANDARD.md`
- `00__LOCKED__UPLOAD_SET/00__Runtime/PHRASE_INDEX.md`

Evidence summary:
- governance enforcement is not document-only
- repo contains workflow, runner, audit, validator, and sentinel layers
- control-tower/governance concepts already exist in the repo surface
- current control-tower drafting must not ignore these existing enforcement layers

Notes:
- This section records existence and enforcement surface only.
- It does not yet claim exact execution order or exact mandatory-use rules for each enforcement file.
- Those details must be verified before promotion into final control-tower policy.


## 3. PATCH DISCIPLINE (WRITTEN EVIDENCE + REPO CROSS-CHECK)

Status:
- populated from 2apr governance-priority extract
- cross-checked against current runtime governance files

Source:
- `/tmp/ct_scan/2apr_governance_priority.txt`
- `00__LOCKED__UPLOAD_SET/00__Runtime/RUNTIME_CHANGE_LEDGER.md`
- `00__LOCKED__UPLOAD_SET/00__Runtime/PATCH_PROTOCOL.md`
- `00__LOCKED__UPLOAD_SET/00__Runtime/PHRASE_GOVERNANCE_STANDARD.md`

Written-evidence findings from 2apr:
- `RUNTIME_CHANGE_LEDGER.md` was described as sequencing / source-of-truth for change status
- `PATCH_PROTOCOL.md` was described as patch discipline / due-diligence source
- `PHRASE_GOVERNANCE_STANDARD.md` was described as phrase compliance gate
- working method repeatedly described as:
  - audit before patch
  - check ledger status first
  - check governance/protocol before any patch
  - patch minimally
  - validate
  - then ledger update / commit / push
- written reconstruction also states:
  - do not treat chat discussion as official state unless ledger reflects it
  - memory recovery / context reconstruction is not patching mode
  - do not trust memory as behavior truth
  - runtime files remain source of truth for behavior

Repo cross-check evidence:
- `PATCH_PROTOCOL.md` states:
  - before any runtime phrase patch or runtime logic patch, due diligence is required
  - exact status must be recorded using ledger statuses only
  - next steps and pending items must be recorded in the ledger before moving to a different runtime topic
  - the ledger is the source of truth for:
    - what is discussed
    - what is approved
    - what is patched
    - what is deferred
  - no runtime patch should proceed if:
    - phrase governance has not been checked for phrase-related edits
    - ledger status is missing or outdated
  - if a change is discussed but not patched, it must still be logged in the ledger
  - manual ledger update is mandatory before each runtime patch sequence
- `RUNTIME_CHANGE_LEDGER.md` contains:
  - formal status definitions
  - `DEFERRED`
  - `APPROVED_FOR_PATCH`
  - `AUDITED_ONLY`
  - `PATCHED_LOCAL`
  - `MERGED_MAIN`
  - `TAGGED_GREEN`
  - repeated records of:
    - `pre-commit: passed`
    - `lint passed`
    - governance-check passed
  - explicit warnings:
    - do not mark anything patched, validated, merged, or tagged unless it has actually happened
    - do not assume discussed phrases are patched
- `PHRASE_GOVERNANCE_STANDARD.md` is referenced by patch protocol and message-construction architecture as the phrase compliance gate

Evidence summary:
- patch discipline is a real governed workflow, not a chat habit
- patching requires status control, governance checks, and phrase-governance checks where relevant
- discussed work and patched work are explicitly separated
- patch sequencing and patch truth are controlled through the ledger
- memory recovery and patching are separate modes

Notes:
- This section records evidence-backed patch discipline only.
- It does not yet define final control-tower wording.
- Final policy drafting must still distinguish:
  - runtime patch workflow
  - architecture-doc promotion workflow
  - testing-only observation workflow


## 4. GIT / CHECKPOINT REALITY (REPO VERIFIED)

Status:
- populated from current repo state
- repo-verified only

Source:
- current repo scan on 2026-04-14
- `git branch --show-current`
- `git log --oneline -n 12`
- `git tag --sort=-creatordate`
- observed local commit flow on this page

Current branch:
- `fix/phase3-gate-alignment`

Recent commits:
cdaf936 fix: correct runtime lock index to use canonical manifest and core bundle files
d795081 docs: add architecture baseline and reconciliation working set
2896331 test: add phase3 closure and wording audit packs
7a3aaec test: finalize phase3 non-ppf closure coverage
9eee0e2 test: add phase3 ppf ready path verification pack
6fea724 fix: align phase3 runtime gates and qualifier routing
989ca44 test: harden phase3 strict guards and stabilize wrap roof routing
52a1a90 fix: align phase0-2 vehicle question shape across runtime and harness
1d1dc88 docs: start phase verification tracker and phase0-2 check packs
a4747b2 test: add strict model-only qualification precision guard
a57725c test: add qualification blocking investigation packs
0f45151 docs: add cursor agents guide for repo-safe patching

Recent tags:
phase3_full_service_uat_ready_20260413
phase3_uat_ready_20260413
phase3_checkpoint_clean_20260413
phase8_bridge_promotion_candidate_v1
runtime_freeze_2026_03_10
runtime_ceramic_phase4_phrase_refinement_v1
runtime_phase3a_ceramic_goal_v1
runtime_phase3a_ppf_comparison_v1
runtime_ppf_phrase_rebalance_v1
runtime_green_post_ppf_framing_patch1_20260307
runtime_green_post_confusion_detector_v1_20260307
runtime_green_pre_ppf_framing_patch1_20260307
runtime_green_post_phase8_comparison_v1_20260307
runtime_green_pre_confusion_detector_v1_20260307
runtime_green_pre_edu_recovery_v1_20260305
runtime_green_pre_edu_hooks_silence_v1_20260305
runtime_release_20260304_rare_vehicle_guardrail_v1
runtime_release_20260304_matte_baseline_v1
docs_governance_20260301_v1
runtime_freeze_checkpoint_20260301_uploadset_green_v1
runtime_freeze_checkpoint_20260301_full_sweep_green_v2
runtime_release_20260301_uat_harness_v1
runtime_freeze_checkpoint_20260301_full_sweep_green
tools_release_20260301_tests_sync_v1
runtime_freeze_checkpoint_20260301_matte_guardrails_allpacks_green
runtime_release_20260301_matte_guardrails_v1
runtime_tests_20260301_matte_downladder_guardrails_v2_wrapper
runtime_tests_20260301_matte_downladder_guardrails_v1
runtime_release_20260228_matte_v3_frozen
runtime_freeze_checkpoint_20260228_alltests_green
runtime_release_20260228_matte_v2_texture_note
runtime_release_20260228_matte_v1_impactzones_fix
matte_dimension_v2_registry_aligned
runtime_release_20260228_matte_v1
matte_dimension_v1
phase0_2_freeze_verified_20260227_v1
phase0_2_freeze_20260227_v1
arch_changelog_20260227_p0_2_patches_v1
matte_work_start_20260228_1814
runtime_green_pre_matte_20260228_0543

Repo-verified workflow evidence:
- controlled docs-only commit was completed on this branch
- separate runtime-fix commit was completed on this branch
- local commit flow triggered governance / validation checks before commit completion
- observed commit-time checks included:
  - arch changelog generation / gate
  - phrase authority gate
  - phrase trigger conflict detector
  - runtime diff sentinel
  - governance pipeline
  - phrase diff visualizer
  - control tower checks

Checkpoint evidence:
- commit history shows explicit checkpoint-style commits and tagged states
- recent history includes test/fix/docs separation rather than one mixed commit
- tag usage is active in current repo history

Notes:
- This section records current git/checkpoint reality only.
- It does not yet define final git policy wording.
- Final control-tower policy must distinguish:
  - repo reality already observed
  - workflow rules we want to require going forward


## 5. MEMORY / RECONSTRUCTION RULES (WRITTEN EVIDENCE)

Status:
- populated from 2apr + 6apr reconstruction evidence
- written-evidence only (no interpretation)

Source:
- `/tmp/ct_scan/2apr_governance_priority.txt`
- `/tmp/ct_scan/6apr_memory_priority.txt`

Written-evidence findings:

From 2apr:
- memory is NOT treated as source of truth
- runtime files are source of truth for behavior
- ledger is source of truth for change status
- reconstruction must be done before continuing work
- memory recovery / reconstruction mode is separate from patching mode
- do not treat chat discussion as official state unless reflected in ledger
- avoid drift by:
  - patching minimally
  - checking governance before patch
  - validating before commit

From 6apr (testing + execution evidence):
- new chat does NOT guarantee clean state:
  - project context may still attach in background
- repeated instruction:
  - use NEW CHAT for test isolation
  - after 3–5 blocks → reset to new chat
- context overload observed:
  - memory stacking
  - context overflow
  - render / execution instability
- explicit split between modes:
  - INSIDE PROJECT → architecture / controlled behavior
  - OUTSIDE PROJECT → execution testing / baseline behavior
- observed behavior:
  - inside project = different behavior vs outside project
  - drift can occur due to:
    - project instruction layer
    - context accumulation
    - multi-turn conversation paths
- explicit drift signals:
  - loss of context continuity
  - restart-like behavior
  - inconsistent routing between chats
- testing protocol signals:
  - many scenarios require NEW CHAT (fresh context)
  - some scenarios must remain INSIDE PROJECT
  - testing context must be explicitly controlled (new vs continuation)
- source-of-truth reinforcement:
  - runtime / repository defined as source of truth
  - lack of single source of truth leads to drift
- reconstruction requirement:
  - need to return to actual runtime context before proceeding
  - avoid continuing work on assumed or partially reconstructed state

Raw evidence extract (6apr priority lines):
4:30:give me the test senarios here block by block with exact prompt to be pasted and if its new chat and continuous chat, i'll paste the output here you provide me the next block and i paste the results back until the end of the tests.
5:36:🔹 BLOCK 1 — New Chat (Fresh Conversation)
6:57:give me the test senarios here block by block with exact prompt to be pasted and if its new chat and continuous chat, i'll paste the output here you provide me the next block and i paste the results back until the end of the tests.
7:64:🔹 BLOCK 1 — New Chat (Start Here)
8:65:👉 Open a NEW chat page
9:90:why is this frequently happening even in the new chat page?
11:105:Even in new chat → sometimes your project context is still heavy in background
13:127:If same error → open completely new chat (not duplicate tab)
14:163:# 🔹 BLOCK 1 — New Chat (Retry)
15:165:### 👉 Open NEW chat
16:180:this is chat gpt app. not browser. still having this issues. i'm already having issues with browsers as well. is there any issues with chatgpt server? how can i fix this? i just restarted my mac and facing these issues very frequent for every chat. last chat page was big, and log, so this was the new chatpage still coming up with this issues
17:192:New chat
19:243:New chat → immediately structured testing
20:267:3–5 blocks → new chat
21:315:🔹 BLOCK 1 — New Chat (Stable Mode)
22:316:👉 Open NEW chat
26:336:Happens in new chat ✅
29:376:Even in new chat → project context still attaches
32:403:Click New Chat (top level, NOT inside project)
34:422:Start chat OUTSIDE project
35:477:Open ChatGPT (outside project)
36:483:After 4–5 blocks → new chat again
37:488:1. Open NEW CHAT (outside project)
40:504:“If I move outside project, will I lose architecture + consistency?”
43:528:🧠 MODE 1 — “Architecture / Control Tower” (Inside Project)
44:541:⚙️ MODE 2 — “Execution / Testing” (Outside Project)
46:580:Inside project:
47:584:Memory stacking
48:591:context overflow + render failure
49:610:3. Run tests outside project
50:625:Will you struggle outside project?
51:631:🔹 BLOCK 1 — New Chat (Outside Project)
53:674:That’s your source of truth
54:676:If you dilute it → behavior drift
56:727:Inside project:
58:732:Outside project:
59:744:Source of truth
60:756:Will I struggle outside project?
61:769:🔹 BLOCK 1 — New Chat (Outside Project)
63:1071:Outside project
64:1095:🔹 BLOCK 1 — New Chat (Price-Sensitive Scenario)
65:1096:👉 Start a NEW chat (outside project)
66:1159:This is exactly the kind of drift you need to catch.
68:1281:inside project = different behavior
69:1282:outside project = different behavior
70:1287:🟢 Inside Project:
71:1296:🔴 Outside Project:
72:1338:Stable execution (outside project)
73:1340:Correct behavior (inside project)
74:1344:👉 Continue testing INSIDE project
75:1615:Outside project → model defaults to:
76:1653:ghosting scenario. - inside the chat inside project context ( customer cummunication project) or outside it?
77:1658:👉 INSIDE PROJECT (customer communication project)
78:1673:⚖️ If you test outside project:
79:1688:Ghosting / hesitation	✅ INSIDE PROJECT ONLY
80:1689:Final QA	✅ INSIDE PROJECT
81:1691:🔹 BLOCK 1 — New Chat (INSIDE PROJECT)
83:1705:🔹 BLOCK 1 — New Chat (INSIDE PROJECT)
84:1706:👉 Open a NEW chat inside your project
88:2009:comparison scenario - is this with out the chat context senario with out any initial prompt in the new chatwindow or the existing chat which i used for ghost handling?
89:2014:👉 NEW CHAT (inside project)
90:2016:❌ Not outside project
92:2032:Normal flow	New chat
93:2033:Price-sensitive	New chat
94:2035:Comparison	✅ New chat
95:2037:🔹 BLOCK 1 — New Chat (INSIDE PROJECT)
99:2340:👉 Feels like restart / loss of context
100:2422:You’re not wasting time, but we did drift slightly from the most useful test path.
101:2493:inside project
102:2510:For objection handling scenario, we should do it in a new chat inside project, and let the conversation reach recommendation first before the objection appears.
103:2517:🔹 BLOCK 1 — New Chat (INSIDE PROJECT)
104:2670:Good — but this is slightly drifting again ⚠️
105:2831:price shopper scenario 👍 - new chat window in the project context?
106:2833:Perfect — yes, this MUST be in a NEW CHAT inside the project ✅
107:2846:⚠️ If you test outside project:
108:2858:🔹 BLOCK 1 — New Chat (INSIDE PROJECT)
111:3298:Your concern was right. We have enough to assess behavioral drift, but not enough to assign final file-level patch ownership safely.
125:5684:LOCK_REASON: Phase-1 boundaries hardened to prevent drift (no pricing, no negotiation, no tone logic, no silence handling, no customer-facing redirection).
138:5766:  To support service-context continuity gating (Phase 4.8), this engine MUST also emit:
151:6384:GREETING ROUTES (HARD OVERRIDE — NO DRIFT)
156:6487:It enforces identity integrity, context continuity, and cross-platform searchability
162:6669:Those files are mostly control/state/gating, not the source of the customer-facing drift you found.
163:6694:2) Phrase library clearly contains the drift
165:6894:the core drift is not mainly in pricing engine or objection engine
166:6896:the core drift is phrase design + assembly stage control
188:7132:769:### Service Context Continuity Gate (HARD PRE-ROUTE OVERRIDE)
205:7192:969:- Enables Service Context Continuity Gate to work correctly after Phase 7.
206:7193:970:- Prevents accidental service drift on re-entry or late technical questions.
208:7237:service context continuity gate
209:7271:service context continuity gate
211:7364:### Service Context Continuity Gate (HARD PRE-ROUTE OVERRIDE)
222:7544:The Service Context Continuity Gate is important.
230:7704:  (b) conversation is explicitly reset as a NEW CHAT.
231:7707:- Enables Service Context Continuity Gate to work correctly after Phase 7.
232:7708:- Prevents accidental service drift on re-entry or late technical questions.
236:7824:drifting back instead of moving forward
245:8289:this line is a likely source of drift.
246:8503:1. Phase 5 is likely a real source of drift
247:8773:conversational drift
250:8944:also we were finishing 80% of the phase 8 ( visual engines etc) and begining phase 9 before we start the testing and then drifted bcoz the testing was not actually looking into the files. i suggest you to go back to the actual context first and then relook what we need to do before we proceed. so you get a better understanding on where we stand. you can looking o the uat files etc which we already have and know where the system is now and what are the pending items before we rollout.
256:9182:We drifted into analysis without grounding in your actual build history
259:9239:⚠️ Important (so we don’t drift again)
265:9347:This is the key mistake (and where drift started):
266:9473:So conversation drifted.
268:9495:And we’ll resume exactly from the correct point — no drift this time.
274:9652:👉 So repeating audit = waste + risk of drift again
276:9680:👉 loss of context continuity
282:9806:👉 Exact next step (no audit, no rework, no drift)
291:10287:These decisions protect the system from accidental design drift.
295:10528:Purpose: Track runtime changes from discussion to freeze, so patching stays sequential, auditable, and non-drifting.
313:10795:   - The ledger is the source of truth for:
325:11092:The runtime ledger is the source of truth
327:11166:5387877 control tower: idea captured - Conversation Drift Simulator for detecting phase s
328:11173:042e56e control tower: idea captured - Add runtime architecture drift detection
352:12898:That will give you the clean breakpoint without drift.
383:13982:Yes — you should have one, and based on what we just found, you do not yet have a strong single source of truth for current runtime state.
387:14053:2. Source of Truth Map
389:14124:That way every new chat starts from the same anchor.
390:14170:That becomes too big, slow, and easy to drift.
396:14422:./00__LOCKED__UPLOAD_SET/PHASE 0–2 — SINGLE SOURCE OF TRUTH (CONTRACT + ADDENDUM + FILE MAP).md
397:14542:Phase Drift Detector
402:14658:PHASE 0–2 — SINGLE SOURCE OF TRUTH
404:14700:If any module or explanation contradicts this structure, it must be flagged as phase drift.
405:14706:Tracks unfinished architecture tasks so discussion drift does not lose them.
407:14733:[ ] Phase drift detector expansion
455:17223:Tracks unfinished architecture tasks so discussion drift does not lose them.
457:17250:[ ] Phase drift detector expansion
459:17308:[ ] Phase drift detector expansion
468:17394:Tracks unfinished architecture tasks so discussion drift does not lose them.
471:17422:[ ] Phase drift detector expansion
476:17600:We now lock Phase 8 properly so future work doesn’t drift.
519:19451:No drift
589:25564:If you want, next I can give you the exact remaining Phase 8 work priority order so you know what to do next without drifting.
593:26401:trust-layer drift
643:31533:I can give you a daily rollout checklist (very practical) so you don’t drift during live testing.
775:34042:prevents unintended behavior drift
779:34272:so for the testing provide me instructions whether its new context or continuing chat. block by block. in case of test context reset for the fresh chat, give me the prompt as well. so i'll execute the testing and give you output for each block and you can provide me the next block.
781:34280:👉 NEW CHAT (fresh start)
784:34467:system inventing outside project context
786:34504:we havent given instruction to stay inside project context
790:34803:assistants will drift
793:35046:no instruction to stay inside project context
795:35172:./00__LOCKED__UPLOAD_SET/PHASE 0–2 — SINGLE SOURCE OF TRUTH (CONTRACT + ADDENDUM + FILE MAP).md:23:- Do pricing, negotiation, persuasion, or sales-heavy education.
815:35287:./00__LOCKED__UPLOAD_SET/02__Repositories/GLOBAL_VEHICLE_CLASSIFICATION_REPOSITORY.md:63:- Any PPF-specific complexity multipliers / adjustments (keep those in service pricing logic, not in SOURCE OF TRUTH)
820:35486:Start a new chat in the same project and run this exact test again:
831:36013:the existing runtime logic is already correct and the issue is just project instruction drift, or
832:36117:the project assistant is still drifting and paraphrasing/inferencing anyway
833:36154:Start a fresh chat after updating the project instructions and send:
835:36261:After that, start a fresh chat and test this exact block:
837:36328:This is very solid now — you’re close. I’ll give you the final cleaned version so you don’t accumulate drift later.
839:36432:Start fresh chat and run:
850:36828:👉 So this is compliant evolution, not drift
856:37147:👉 Start NEW CHAT (fresh context)
859:37271:Start NEW CHAT
888:37803:   - The ledger is the source of truth for:
911:38427:1054:  - Remove cross-service mention (PPF / ceramic) to avoid service trigger drift
912:38429:1068:  - Remove service-drift phrasing referencing PPF or ceramic
915:38492:the project layer can still drift because of:
917:38525:A. Project execution drift
922:38551:Test 1 — Fresh project vs fresh chat behavior
923:38552:Do this in the same project, but use a brand new chat and send only this single line:
924:38560:project retrieval/instruction drift
925:38564:If it gives correct pricing or correctly routes, then the earlier multi-turn path may have caused drift
926:38567:In another new chat, ask this exact meta question:
927:38578:“route to PRICE_LADDER_ENGINE” → files are probably fine, project execution is drifting
929:38583:In another new chat, send:
933:38693:Once service + vehicle are known, the system stops asking and starts pricing, but in a controlled, engine-driven way only — no improvisation, no extra conversation drift.
935:38738:fresh chat behavior repeated the same routing
939:39006:# LOCK_REASON: Phase 3A UAT passed; prevent qualifier drift or reordering
941:39286:Use the same project, new chat, and send:
952:39746:👉 NEW CHAT (fresh start)
956:40205:We now have a stronger case that there is a real authority conflict or execution drift, not just strict qualification.
964:40739:or Phase 3A chain execution drift
966:40889:That looks very much like project-level behavior drift.
967:40891:Then test again in a fresh chat
974:41310:A. Vehicle classification drift
975:41313:B. Price rendering drift
984:42106:→ Repository (SOURCE OF TRUTH) ✅
985:42204:project execution / retrieval drift
988:42676:2) Use a separate debug audit prompt in a fresh chat when something looks wrong
989:42699:Use this in a new fresh chat inside the same project
990:42815:or project-file binding drift.
993:43251:👉 This is authority drift between files and execution

Evidence summary:
- memory is unreliable as continuity layer
- context persistence across chats is inconsistent
- explicit reconstruction and reset protocols were used during testing
- drift is a known and repeatedly observed failure mode
- testing discipline includes forced context resets and environment control

Notes:
- This section records evidence only.
- It does NOT yet define final control-tower rules.
- Final policy must separate:
  - memory limitations
  - chat-context behavior
  - required reconstruction protocol
  - testing context discipline



### Addendum — SNASHGPT_MASTER_GOVERNANCE.md (REPO VERIFIED)

Source:
- `00__LOCKED__UPLOAD_SET/00__Runtime/SNASHGPT_MASTER_GOVERNANCE.md`
- repo inspection on 2026-04-14

Repo-verified findings:
- file header explicitly states:
  - `NOT WIRED TO RUNTIME`
- purpose explicitly states:
  - human governance ledger to prevent drift
- file indicates:
  - it is intentionally not referenced/wired by any runtime engine
- file contains:
  - behavioral risk logs
  - UAT packs inventory
  - work queue
  - governance-oriented re-anchoring content
- file references runtime governance artifacts including:
  - `RUNTIME_CHANGE_LEDGER.md`
  - `AUTHORITY_INDEX.md`
- file includes guidance such as:
  - keep discussion discipline aligned with repo governance
  - reduce drift without creating duplicate governance files
  - governance-only edits reviewed before commit
  - runtime-sensitive edits follow lint / pre-commit / UAT discipline
  - exists to reduce drift and speed re-anchoring in future sessions

Evidence impact:
- `SNASHGPT_MASTER_GOVERNANCE.md` is governance-supporting, not runtime-authoritative
- it should be treated as:
  - human governance / re-anchoring layer
- it should not be treated as:
  - wired runtime behavior source
  - final runtime authority



### Addendum — tools/control_tower.py (REPO VERIFIED)

Source:
- `tools/control_tower.py`
- repo inspection on 2026-04-14

Repo-verified findings:
- file is a command wrapper / helper for governance and architecture audit tasks
- supported modes include:
  - `--design`
  - `--commit`
  - `--audit`
  - `--ci`
- file runs supporting checks such as:
  - `tools/audit/runtime_architecture_map.py`
  - `tools/audit/governance_file_scan.py`
  - `tools/audit/dev_tools_inventory.py`
  - `tools/audit/architecture_graph.py`
  - `tools/audit/phase7_wiring_check.py`
  - `tools/runtime_dependency_guard.py`
  - `tools/file_authority_guard.py`
  - `runtime_guard/test_phase_drift.py`
- file also checks for:
  - `00__CONTROL_TOWER/IDEA_BACKLOG.md`
  - `00__CONTROL_TOWER/SNASH_PHASE_REGISTRY.md`

Evidence impact:
- `tools/control_tower.py` is audit/support tooling
- it is not a runtime authority file
- it is not a policy/source-of-truth document
- it should be treated as:
  - governance support layer
  - audit wrapper
- it should not be treated as:
  - final control-tower authority
  - runtime behavior source



### Addendum — Repo Tooling / Pre-Commit / GitHub Workflow Evidence (REPO VERIFIED)

Source:
- `.gitignore`
- `.pre-commit-config.yaml`
- `.github/workflows/governance-check.yml`
- `.github/workflows/governance.yml`
- `.github/workflows/runtime_checks.yml`
- `.github/workflows/runtime_freeze.yml`
- `.github/workflows/uat.yml`
- repo workflow/tooling scan on 2026-04-14

Repo-verified findings:
- local Python virtual environment is intentionally excluded from git tracking:
  - `.venv/` is listed in `.gitignore`
- local validation is formally configured through `.pre-commit-config.yaml`
- pre-commit config includes:
  - `check-json`
  - `ruff`
  - `runner/generate_arch_changelog.py`
  - `runner/check_arch_changelog.py`
  - `runner/check_phrase_authority.py`
  - `runner/check_phrase_trigger_conflicts.py`
  - `runner/runtime_diff_sentinel.py`
  - `runner/governance_pipeline.py`
  - `runner/phrase_diff_visualizer.py`
  - `tools/control_tower.py --commit`
- GitHub workflow layer is present in repo:
  - `governance-check.yml`
  - `governance.yml`
  - `runtime_checks.yml`
  - `runtime_freeze.yml`
  - `uat.yml`
- GitHub workflow triggers evidenced in repo include:
  - `push`
  - `pull_request`
  - `workflow_dispatch`
- repo evidence confirms `ruff` is enforced in both:
  - GitHub workflow layer
  - local pre-commit layer
- runtime freeze workflow includes automated tag creation and push
- UAT workflow references CI secret / trigger constraints

Evidence impact:
- repo governance exists at both:
  - local pre-commit level
  - GitHub workflow / CI level
- repo workflow discipline is stronger than local chat habit alone
- control-tower docs must account for:
  - local validation
  - CI / GitHub validation
  - branch / push / PR governance reality


## 6. OPEN QUESTIONS / UNCERTAINTIES

Status:
- populated from current evidence review
- not yet resolved

Rule:
- anything not fully verified must stay here
- nothing in this section may be promoted as final policy without further repo or written-evidence confirmation

Open questions / uncertainties:
- exact execution order of governance enforcement files is not yet verified
  - workflows, runner checks, audit tools, and control-tower tools are confirmed present
  - mandatory invocation order is not yet fully documented
- exact relationship between:
  - `SNASHGPT_MASTER_GOVERNANCE.md`
  - `PATCH_PROTOCOL.md`
  - `RUNTIME_CHANGE_LEDGER.md`
  - `PHRASE_GOVERNANCE_STANDARD.md`
  is not yet fully normalized into one hierarchy
- current repo reality confirms git/tag/checkpoint usage, but not yet the final required policy for:
  - branch naming
  - checkpoint naming
  - tag creation threshold
  - push timing
- 2apr confirms reconstruction / memory-recovery method, but this is still historical reconstruction evidence
  - it is not yet fully converted into final operating policy
- 6apr confirms testing-context instability and project-context drift, but:
  - exact product/platform cause is not verified
  - only the operational symptoms and working mitigations are evidenced
- inside-project vs outside-project testing split is evidenced operationally, but:
  - final long-term policy for when each mode must be used is not yet fully written
- higher-phase orchestration (especially later-phase control structure) was repeatedly described as only partially reconstructed
  - no final control-tower policy should overstate later-phase certainty
- architecture-doc promotion workflow is evidenced in current project practice, but has not yet been converted into a separate final control-tower policy document
- no final source-of-truth ladder has yet been written as a dedicated control-tower artifact
  - only evidence for writing it is now assembled here

Next required follow-up before drafting control-tower policy files:
- verify whether key governance runners define operational sequencing beyond current evidence
- then draft foundation control-tower files from this evidence base only

