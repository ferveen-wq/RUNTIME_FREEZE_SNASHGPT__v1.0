print("\nSNASHGPT CONVERSATION SIMULATOR V2\n")

conversations = [

    [
        "How much is PPF and does it protect from stone chips?",
        "2023 Nissan Patrol",
        "Is XPEL better than other brands?",
        "Ok what is the price?"
    ],

    [
        "Ceramic or PPF which is better?",
        "My car is a 2024 Land Cruiser",
        "How much does ceramic cost?"
    ],

    [
        "Price for Global and XPEL PPF?",
        "Car is BMW X5 2022",
        "Does PPF self heal?"
    ],

    [
        "just price",
        "don't ask questions just price",
        "how much full PPF",
        "my car is 2023 Land Cruiser"
    ],

    [
        "Is XPEL better than other brands?",
        "My friend said Suntek is same but cheaper",
        "Why should I choose XPEL then?"
    ],

    [
        "PPF vs ceramic vs tint what is best?",
        "Which one protects the paint?",
        "Which one lasts longer?"
    ],

    [
        "hi",
        "price?",
        "2023 patrol",
        "ppf good?",
        "xpel better?",
        "how much?"
    ]

]

phase = "Phase0"
conversation_phase_max = "Phase0"

phase_order = [
    "Phase0",
    "Phase1",
    "Phase2",
    "Phase3",
    "Phase4",
    "Phase5",
    "Phase7",
    "Phase8",
    "Phase9"
]

def update_phase(new_phase):
    global phase, conversation_phase_max

    phase = new_phase

    if phase_order.index(new_phase) > phase_order.index(conversation_phase_max):
        conversation_phase_max = new_phase


def simulate_message(msg):

    msg_lower = msg.lower()

    if "price" in msg_lower or "how much" in msg_lower:
        update_phase("Phase3")

    if "ceramic" in msg_lower or "ppf" in msg_lower:
        update_phase("Phase7")

    if "better" in msg_lower or "brand" in msg_lower:
        update_phase("Phase9")

    if "202" in msg_lower:
        update_phase("Phase4")


for conv in conversations:

    print("\n----------------------------------")
    print("NEW CONVERSATION")
    print("----------------------------------")

    phase = "Phase0"
    conversation_phase_max = "Phase0"

    step = 1

    for msg in conv:

        print(f"\nSTEP {step}")
        print("Customer:", msg)

        simulate_message(msg)

        print("Current Phase:", phase)
        print("Max Phase Reached:", conversation_phase_max)

        step += 1


print("\nSimulation complete.\n")
