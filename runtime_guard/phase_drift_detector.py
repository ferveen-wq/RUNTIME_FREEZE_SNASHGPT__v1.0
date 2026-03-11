class PhaseDriftDetector:

    PHASE_ORDER = [
        "Phase0",
        "Phase1",
        "Phase2",
        "Phase3",
        "Phase4",
        "Phase5"
    ]

    def __init__(self):
        self.current_phase = None

    def update_phase(self, phase):

        if self.current_phase is None:
            self.current_phase = phase
            return

        current_index = self.PHASE_ORDER.index(self.current_phase)
        new_index = self.PHASE_ORDER.index(phase)

        if new_index < current_index:
            print("⚠ PHASE DRIFT DETECTED")
            print("Previous phase:", self.current_phase)
            print("New phase:", phase)

        self.current_phase = phase
