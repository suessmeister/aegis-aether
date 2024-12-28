class DecisionEngine:
    def __init__(self, node):
        self.node = node

    def make_decision(self, signal):
        """Simulate a decision-making process based on node state and signal."""
        if "urgent" in signal.lower() and self.node.state["energy"] > 50:
            decision = "Accepted"
        elif self.node.state["energy"] < 20:
            decision = "Rejected due to low energy"
        else:
            decision = "Deferred for further analysis"
        print(f"Node {self.node.id} Decision: {decision}")
        return decision

# Example usage
if __name__ == "__main__":
    from src.core.node_autonomy import AutonomousNode

    node = AutonomousNode(0)
    engine = DecisionEngine(node)
    engine.make_decision("Urgent request to process data")