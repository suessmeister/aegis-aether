from src.core.node_autonomy import AutonomousNode
import random

# Initialize nodes
node_a = AutonomousNode(0)
node_b = AutonomousNode(1)

# Simple "game": Nodes compete to generate higher evolution scores
print(f"Starting Evolution Scores: Node A: {node_a.state['evolution_score']}, Node B: {node_b.state['evolution_score']}")

for round_num in range(1, 6):
    print(f"\n### Round {round_num} ###")
    action_a = random.choice(["evolve", "wait"])
    action_b = random.choice(["evolve", "wait"])

    if action_a == "evolve":
        node_a.evolve()
    if action_b == "evolve":
        node_b.evolve()

    print(f"Node A: {action_a}, Evolution Score: {node_a.state['evolution_score']}")
    print(f"Node B: {action_b}, Evolution Score: {node_b.state['evolution_score']}")

# Determine the winner
if node_a.state["evolution_score"] > node_b.state["evolution_score"]:
    print("\nNode A Wins!")
elif node_a.state["evolution_score"] < node_b.state["evolution_score"]:
    print("\nNode B Wins!")
else:
    print("\nIt's a tie!")