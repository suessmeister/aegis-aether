from src.agents.ai_agent import AIAgent

if __name__ == "__main__":
    # Create multiple agents in the swarm
    agent1 = AIAgent(agent_id=1, role="worker", provider="openai", base_url="https://api.openai.com")
    agent2 = AIAgent(agent_id=2, role="worker", provider="openai", base_url="https://api.openai.com")
    agent3 = AIAgent(agent_id=3, role="worker", provider="openai", base_url="https://api.openai.com")

    # Agents propose tasks
    proposal1 = agent1.propose_task_to_swarm("Analyze market trends for the last year.")
    proposal2 = agent2.propose_task_to_swarm("Generate a report on AI innovation trends.")

    # Agents vote on proposals
    agent1.vote_on_task(proposal1)
    agent2.vote_on_task(proposal1)
    agent3.vote_on_task(proposal2)

    # Check if consensus has been reached
    consensus_task = agent1.check_consensus()
    if consensus_task:
        print(f"Swarm consensus: Task '{consensus_task['task']}' was selected.")
    else:
        print("No consensus reached yet.")