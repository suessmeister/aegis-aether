import networkx as nx
import matplotlib.pyplot as plt
from src.core.lattice_engine import LatticeEngine
from src.core.node_autonomy import AutonomousNode

# Initialize the lattice and nodes
lattice = LatticeEngine()
nodes = [AutonomousNode(i) for i in range(5)]
for node in nodes:
    lattice.add_node(node)
lattice.connect_nodes(nodes[0], nodes[1])
lattice.connect_nodes(nodes[1], nodes[2])
lattice.connect_nodes(nodes[2], nodes[3])
lattice.connect_nodes(nodes[3], nodes[4])

# Create a NetworkX graph
graph = nx.Graph()
for node in nodes:
    graph.add_node(node.id)
for node, connections in lattice.network_map.items():
    for connection in connections:
        graph.add_edge(node, connection.id)

# Visualize the graph
plt.figure(figsize=(8, 6))
nx.draw(graph, with_labels=True, node_color="skyblue", font_weight="bold", node_size=700)
plt.title("Lattice Visualization")
plt.show()