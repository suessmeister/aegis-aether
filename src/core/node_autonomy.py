class AutonomousNode:
    def __init__(self, id):
        self.id = id
        self.state = {
            "energy": 100,
            "evolution_score": 0,
            "message_log": [],
        }

    def evolve(self):
        """Simulate autonomous evolution."""
        if self.state["energy"] > 0:
            self.state["energy"] -= 5
            self.state["evolution_score"] += 1
            print(f"Node {self.id} evolves. State: {self.state}")
        else:
            print(f"Node {self.id} is out of energy and cannot evolve.")

    def recharge(self, amount=50):
        """Recharge the node's energy."""
        self.state["energy"] += amount
        print(f"Node {self.id} recharges by {amount}. Energy: {self.state['energy']}")

    def process_signal(self, signal):
        """Process an incoming signal and log it."""
        print(f"Node {self.id} processing signal: {signal}")
        self.state["message_log"].append(signal)
        self.evolve()

    def destroy(self):
        """Simulate node destruction."""
        print(f"Node {self.id} has self-destructed.")
        self.state = {"energy": 0, "evolution_score": 0, "message_log": []}