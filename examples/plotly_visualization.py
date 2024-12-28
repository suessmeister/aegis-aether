import plotly.graph_objects as go
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

# Prepare data for Plotly visualization
node_ids = [node.id for node in nodes]
node_energy = [node.state["energy"] for node in nodes]
edges = [(node.id, connection.id) for node in nodes for connection in lattice.network_map[node.id]]

# Create Plotly scatter plot for nodes
node_trace = go.Scatter(
    x=node_ids,
    y=node_energy,
    mode="markers+text",
    marker=dict(size=15, color=node_energy, colorscale="Viridis"),
    text=[f"Node {node.id}<br>Energy: {node.state['energy']}" for node in nodes],
    textposition="top center"
)

# Create edges for visualization
edge_traces = []
for edge in edges:
    x_coords = [edge[0], edge[1], None]
    y_coords = [node_energy[edge[0]], node_energy[edge[1]], None]
    edge_traces.append(
        go.Scatter(
            x=x_coords,
            y=y_coords,
            mode="lines",
            line=dict(width=2, color="gray"),
            hoverinfo="none"
        )
    )

# Combine all traces
fig = go.Figure()
fig.add_trace(node_trace)
for edge_trace in edge_traces:
    fig.add_trace(edge_trace)

# Update layout
fig.update_layout(
    title="Lattice Visualization",
    xaxis_title="Node IDs",
    yaxis_title="Energy Levels",
    showlegend=False
)

# Show the plot
fig.show()