from src.swarm.advanced_swarm_behavior import Swarm

def resource_allocation_simulation():
    """Simulate resource allocation in a swarm."""
    swarm = Swarm(10)

    print("\n--- Initial Swarm State ---")
    for node in swarm.nodes:
        print(f"Node {node.id}: Role={node.role}, Energy={node.energy}")

    # Simulate with fault tolerance
    swarm.simulate(5)

    print("\n--- Final Swarm State ---")
    for node in swarm.nodes:
        print(f"Node {node.id}: Role={node.role}, Energy={node.energy}, Tasks Completed={node.tasks_completed}")

if __name__ == "__main__":
    resource_allocation_simulation()