from flask import Flask, jsonify
from src.core.lattice_engine import LatticeEngine
from src.core.node_autonomy import AutonomousNode

app = Flask(__name__)

# Initialize lattice and nodes
lattice = LatticeEngine()
nodes = [AutonomousNode(i) for i in range(5)]
for node in nodes:
    lattice.add_node(node)
lattice.connect_nodes(nodes[0], nodes[1])
lattice.connect_nodes(nodes[1], nodes[2])
lattice.connect_nodes(nodes[2], nodes[3])
lattice.connect_nodes(nodes[3], nodes[4])

@app.route("/nodes", methods=["GET"])
def get_nodes():
    """Return the current state of all nodes."""
    return jsonify([
        {"id": node.id, "state": node.state}
        for node in nodes
    ])

@app.route("/lattice", methods=["GET"])
def get_lattice():
    """Return the lattice structure."""
    return jsonify(lattice.network_map)

if __name__ == "__main__":
    app.run(debug=True, port=5001)