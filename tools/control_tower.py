import os
import subprocess
import sys


def run(cmd):
    subprocess.run(cmd, shell=True)


mode = sys.argv[1] if len(sys.argv) > 1 else "--audit"

print("\nSNASHGPT CONTROL TOWER\n")

if mode == "--design":
    print("Running design checks...\n")
    run("python tools/audit/runtime_architecture_map.py")
    run("python tools/audit/governance_file_scan.py")

elif mode == "--commit":
    print("Running commit governance checks...\n")
    run("python tools/file_authority_guard.py")
    run("python tools/runtime_dependency_guard.py")

elif mode == "--audit":
    print("Running full architecture audit...\n")
    run("python tools/audit/runtime_architecture_map.py")
    run("python tools/audit/dev_tools_inventory.py")
    run("python tools/audit/architecture_graph.py")
    run("python tools/runtime_dependency_guard.py")
    run("python tools/file_authority_guard.py")
    run("python runtime_guard/test_phase_drift.py")

elif mode == "--ci":
    print("Running CI architecture checks...\n")
    run("python tools/runtime_dependency_guard.py")
    run("python tools/file_authority_guard.py")

# --- IDEA GOVERNANCE CHECK ---------------------------------

BACKLOG = "00__CONTROL_TOWER/IDEA_BACKLOG.md"

if os.path.exists(BACKLOG):
    with open(BACKLOG) as f:
        backlog = f.read().strip()

    if len(backlog) < 20:
        print("\n⚠ CONTROL TOWER NOTICE")
        print("Idea backlog appears empty or very small.")
        print("Capture architecture ideas using:")
        print('python tools/capture_idea.py "Idea description"')

# --- PHASE ARCHITECTURE REGISTRY CHECK -------------------------

PHASE_REGISTRY = "00__CONTROL_TOWER/SNASH_PHASE_REGISTRY.md"


def check_phase_registry():
    if not os.path.exists(PHASE_REGISTRY):
        print("⚠ Phase registry missing.")
        return

    with open(PHASE_REGISTRY) as f:
        registry = f.read()

    required_phases = [
        "PHASE 0-2",
        "PHASE 3",
        "PHASE 4",
        "PHASE 5",
        "PHASE 6",
        "PHASE 7",
        "PHASE 8",
        "PHASE 9",
        "PHASE 10",
    ]

    missing = [p for p in required_phases if p not in registry]

    if missing:
        print("⚠ Phase registry incomplete:")
        for m in missing:
            print(" -", m)
    else:
        print("Phase architecture registry verified.")


check_phase_registry()
