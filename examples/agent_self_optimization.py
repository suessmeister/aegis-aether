from src.agents.ai_agent import AIAgent

if __name__ == "__main__":
    # Create an AI agent with self-optimization enabled
    agent = AIAgent(agent_id=1, role="optimizer", provider="openai", base_url="https://api.openai.com")

    # Simulate task execution and optimization
    for episode in range(10):  # Run multiple optimization episodes
        state = agent.get_environment_state()
        print(f"Episode {episode}: Current state: {state}")
        agent.optimize_task_execution(state)