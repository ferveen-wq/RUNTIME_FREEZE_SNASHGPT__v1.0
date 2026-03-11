import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from runtime_guard.phase_drift_detector import PhaseDriftDetector

detector = PhaseDriftDetector()

detector.update_phase("Phase0")
detector.update_phase("Phase1")
detector.update_phase("Phase3")

# simulate drift
detector.update_phase("Phase2")

