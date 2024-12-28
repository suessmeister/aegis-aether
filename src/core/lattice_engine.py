import time

class LatticeEngine:
    def __init__(self):
        self.nodes = []
        self.network_map = {}

    def add_node(self, node):
        """Add a new node to the lattice."""
        self.nodes.append(node)
        self.network_map[node.id] = []

    def connect_nodes(self, node_a, node_b):
        """Create a bidirectional connection between two nodes."""
        if node_a.id not in self.network_map or node_b.id not in self.network_map:
            raise ValueError("Both nodes must be added to the lattice first.")
        self.network_map[node_a.id].append(node_b)
        self.network_map[node_b.id].append(node_a)

    def propagate_signal(self, signal, start_node_id, energy_cost=5):
        """Propagate a signal through the lattice with energy cost."""
        visited = set()

        def dfs(node):
            if node.id in visited or node.state["energy"] < energy_cost:
                return
            visited.add(node.id)
            node.process_signal(signal)
            node.state["energy"] -= energy_cost  # Deduct energy for processing the signal
            for neighbor in self.network_map[node.id]:
                dfs(neighbor)

        start_node = next((n for n in self.nodes if n.id == start_node_id), None)
        if start_node:
            dfs(start_node)
        else:
            print(f"Start node {start_node_id} not found in the lattice.")

    def simulate_activity(self, duration=5):
        """Simulate random activity for a set duration."""
        import random

        print("Simulating lattice activity...")
        for _ in range(duration):
            active_node = random.choice(self.nodes)
            random_signal = f"Signal-{random.randint(1000, 9999)}"
            print(f"Node {active_node.id} emitting signal: {random_signal}")
            self.propagate_signal(random_signal, start_node_id=active_node.id)
            time.sleep(1)