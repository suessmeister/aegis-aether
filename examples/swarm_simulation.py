from src.swarm.advanced_swarm_behavior import Swarm

# Initialize a swarm with 10 nodes
swarm = Swarm(10)

# Simulate swarm behavior with 5 iterations
print("Simulating swarm behavior...")
swarm.simulate(5)

# Add a new agent through breeding
parent_agent = swarm.nodes[0]
new_agent = swarm.breed_agent(parent_agent, role="researcher")

if new_agent:
    print(f"New agent created: ID {new_agent.id}, Role {new_agent.role}")

# Simulate additional rounds with the updated swarm
swarm.simulate(3)

# List final swarm state
print("\nFinal Swarm State:")
swarm.list_agents()