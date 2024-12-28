from src.core.lattice_engine import LatticeEngine
from src.core.node_autonomy import AutonomousNode

# Initialize the lattice
lattice = LatticeEngine()

# Create nodes
nodes = [AutonomousNode(i) for i in range(5)]
for node in nodes:
    lattice.add_node(node)

# Connect nodes
for i in range(len(nodes) - 1):
    lattice.connect_nodes(nodes[i], nodes[i + 1])

# Multi-agent strategy: Sharing resources
print("### Initial Node States ###")
for node in nodes:
    print(f"Node {node.id}: {node.state}")

print("\n### Resource Sharing ###")
for i in range(len(nodes) - 1):
    nodes[i].share_resources(nodes[i + 1], 10)

print("\n### Updated Node States ###")
for node in nodes:
    print(f"Node {node.id}: {node.state}")