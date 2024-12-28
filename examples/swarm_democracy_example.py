from src.ai.ai_agent import AIAgent
from src.swarm.swarm_voting import SwarmVoting

# Create agents
agents = [
    AIAgent(agent_id=1, role="worker"),
    AIAgent(agent_id=2, role="manager"),
    AIAgent(agent_id=3, role="worker"),
]

# Initialize SwarmVoting
swarm = SwarmVoting(agents)

# Create a proposal and vote
description = "Should we prioritize reinforcement learning over swarm optimization?"
expiration_time = 60  # 60 seconds
results = swarm.create_and_vote(description, expiration_time)

print("Voting Results:", results)