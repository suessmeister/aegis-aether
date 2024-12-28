import plotly.graph_objects as go
from src.swarm.advanced_swarm_behavior import Swarm

def visualize_swarm(swarm):
    """Visualize the swarm's state using Plotly."""
    node_ids = [node.id for node in swarm.nodes]
    node_roles = [node.role for node in swarm.nodes]
    node_energy = [node.energy for node in swarm.nodes]
    tasks_completed = [node.tasks_completed for node in swarm.nodes]

    fig = go.Figure()

    # Scatter plot for node energy
    fig.add_trace(go.Scatter(
        x=node_ids,
        y=node_energy,
        mode="markers+text",
        marker=dict(size=15, color="blue"),
        text=[f"Role: {role}" for role in node_roles],
        textposition="top center",
        name="Energy Levels"
    ))

    # Bar plot for tasks completed
    fig.add_trace(go.Bar(
        x=node_ids,
        y=tasks_completed,
        name="Tasks Completed",
        marker=dict(color="green")
    ))

    # Layout updates
    fig.update_layout(
        title="Swarm Visualization",
        xaxis_title="Node IDs",
        yaxis_title="Value",
        showlegend=True
    )

    fig.show()

# Example usage
if __name__ == "__main__":
    swarm = Swarm(5)
    swarm.simulate(2)

    # LLM decision-making example
    prompt = "What is the best strategy for resource allocation?"
    for node in swarm.nodes:
        node.make_decision_with_llm(prompt)