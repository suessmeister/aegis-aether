import random

class SwarmNode:
    """A single node in an AI swarm."""
    def __init__(self, id):
        self.id = id
        self.state = random.random()

    def interact(self, other_node):
        """Simulate interaction between nodes."""
        self.state = (self.state + other_node.state) / 2

class Swarm:
    """A collection of swarm nodes."""
    def __init__(self, node_count):
        self.nodes = [SwarmNode(i) for i in range(node_count)]

    def simulate(self, iterations):
        for _ in range(iterations):
            node1, node2 = random.sample(self.nodes, 2)
            node1.interact(node2)

# Example usage
if __name__ == "__main__":
    swarm = Swarm(10)
    swarm.simulate(5)
    for node in swarm.nodes:
        print(f"Node {node.id} state: {node.state}")