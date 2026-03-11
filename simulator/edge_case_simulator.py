import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from runtime_state.runtime_decision_state import RuntimeDecisionState


class EdgeCaseSimulator:

    def __init__(self):
        self.test_cases = [
            "just price",
            "cheapest option",
            "my friend got cheaper",
            "is PPF self healing",
            "what thickness is the PPF",
            "ceramic vs PPF difference",
            "I only want tint",
            "do you have graphene coating",
            "is XPEL better than others",
            "what is the warranty"
        ]

    def run(self):

        print("\nSNASHGPT EDGE CASE SIMULATION\n")

        for case in self.test_cases:

            state = RuntimeDecisionState()

            print("CUSTOMER:", case)

            # simple simulation logic

            if "price" in case:
                state.request_type = "PRICE_REQUEST"

            if "PPF" in case:
                state.service_intent = "PPF"

            if "ceramic" in case:
                state.service_intent = "CERAMIC"

            if "tint" in case:
                state.service_intent = "TINT"

            if "wrap" in case:
                state.service_intent = "WRAP"

            state.debug_print()

        print("\nSimulation complete\n")


if __name__ == "__main__":

    simulator = EdgeCaseSimulator()
    simulator.run()
