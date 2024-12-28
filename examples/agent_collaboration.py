from src.agents.ai_agent import AIAgent

if __name__ == "__main__":
    # Create two agents
    agent1 = AIAgent(agent_id=1, role="coordinator", provider="openai", base_url="https://api.openai.com")
    agent2 = AIAgent(agent_id=2, role="worker", provider="openai", base_url="https://api.openai.com")

    # Agent 1 sends a message to Agent 2
    agent1.send_message(recipient_id=2, message="Please process the dataset for analysis.")

    # Agent 2 receives the message
    agent2.receive_messages()

    # Agent 1 delegates a task to Agent 2
    agent1.delegate_task(recipient_id=2, task_description="Analyze sales data for Q1 2024.")

    # Agent 2 receives the delegated task
    agent2.receive_messages()