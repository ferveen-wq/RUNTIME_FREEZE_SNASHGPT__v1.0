class RuntimeDecisionState:

    def __init__(self):

        # vehicle info
        self.vehicle_model = None
        self.vehicle_year = None

        # service intent
        self.service_intent = None
        self.sku_selected = None

        # negotiation
        self.price_tier = None
        self.negotiation_state = None

        # objections
        self.objection_state = None
        self.objection_count = 0

        # silence handling
        self.silence_state = None

        # routing signals
        self.request_type = None

    def debug_print(self):

        print("\nRUNTIME STATE SNAPSHOT\n")

        for k, v in self.__dict__.items():
            print(f"{k}: {v}")

        print()
