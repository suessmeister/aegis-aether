from src.agents.ai_agent import AIAgent

if __name__ == "__main__":
    # Create agents
    agent1 = AIAgent(agent_id=1, role="data processor", provider="openai", base_url="https://api.openai.com")
    agent2 = AIAgent(agent_id=2, role="data analyzer", provider="openai", base_url="https://api.openai.com")

    # Agent 1 pushes tasks to the queue
    agent1.push_task_to_queue("Analyze market trends for Q1 2024.")
    agent1.push_task_to_queue("Generate a report on decentralized AI adoption.")

    # Agent 2 pulls tasks and processes them
    agent2.pull_task_from_queue()
    agent2.pull_task_from_queue()

    # Check task count in the queue
    agent1.redis_queue.task_count()