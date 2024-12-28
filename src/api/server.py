from flask import Flask, request, jsonify
from src.core.lattice_engine import LatticeEngine
from src.core.node_autonomy import AutonomousNode

app = Flask(__name__)

# Initialize lattice and nodes
lattice = LatticeEngine()
nodes = [AutonomousNode(i) for i in range(3)]
for node in nodes:
    lattice.add_node(node)
lattice.connect_nodes(nodes[0], nodes[1])
lattice.connect_nodes(nodes[1], nodes[2])

@app.route("/nodes", methods=["GET"])
def get_nodes():
    return jsonify([{"id": node.id, "state": node.state} for node in nodes])

@app.route("/signal", methods=["POST"])
def propagate_signal():
    data = request.json
    signal = data.get("signal")
    start_node_id = data.get("start_node_id")
    lattice.propagate_signal(signal, start_node_id)
    return jsonify({"message": "Signal propagated successfully!"})

if __name__ == "__main__":
    app.run(debug=True, port=5000)