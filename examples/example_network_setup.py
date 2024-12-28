from src.core.lattice_engine import LatticeEngine
from src.core.node_autonomy import AutonomousNode
from src.network.node_communication import NodeCommunication

# Initialize the lattice
lattice = LatticeEngine()

# Create nodes
nodes = [AutonomousNode(i) for i in range(5)]
for node in nodes:
    lattice.add_node(node)

# Set up communication
comm = NodeCommunication()

# Connect nodes
for i in range(len(nodes) - 1):
    comm.connect_nodes(nodes[i], nodes[i + 1])

# Propagate a signal through the lattice
lattice.propagate_signal("Test Signal", start_node_id=0)

# Simulate message exchange
comm.send_message(sender_id=0, receiver_id=1, message="Hello, Node 1!")
comm.send_message(sender_id=1, receiver_id=2, message="Hi, Node 2!")