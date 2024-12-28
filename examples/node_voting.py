from src.core.node_autonomy import AutonomousNode

# Initialize nodes
nodes = [AutonomousNode(i) for i in range(5)]

# Voting system: Nodes vote based on their energy levels
signal = "Process urgent data"
print(f"Signal: {signal}")

votes = {}
for node in nodes:
    vote = "yes" if node.state["energy"] > 50 else "no"
    votes[node.id] = vote
    print(f"Node {node.id} votes {vote}")

# Count votes
yes_votes = sum(1 for vote in votes.values() if vote == "yes")
no_votes = len(nodes) - yes_votes

# Determine outcome
if yes_votes > no_votes:
    print("Outcome: Signal Approved")
else:
    print("Outcome: Signal Rejected")