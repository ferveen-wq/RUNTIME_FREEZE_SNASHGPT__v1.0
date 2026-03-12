from graphviz import Digraph

dot = Digraph(comment="SNASHGPT Architecture")

# Core Runtime
dot.node("Runtime", "Runtime Core")

# Engines
dot.node("QualEngine", "Qualification Engine")
dot.node("MsgAssembly", "Message Assembly")

# Phrase Library
dot.node("PhraseLib", "Human Phrase Library")

# Governance
dot.node("ControlTower", "Control Tower")
dot.node("RuntimeGuard", "Runtime Guard")
dot.node("Simulator", "Edge Case Simulator")

# Database
dot.node("DB", "Conversation Database")

# Relationships
dot.edges(
    [
        ("Runtime", "QualEngine"),
        ("Runtime", "MsgAssembly"),
        ("MsgAssembly", "PhraseLib"),
        ("Runtime", "ControlTower"),
        ("Runtime", "RuntimeGuard"),
        ("Runtime", "Simulator"),
        ("Runtime", "DB"),
    ]
)

dot.render("snash_architecture_graph", format="png", view=True)
