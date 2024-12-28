from src.agents.ai_agent import AIAgent

if __name__ == "__main__":
    # Create agents with different roles
    data_agent = AIAgent(agent_id=1, role="data analysis", provider="openai", base_url="https://api.openai.com")
    social_agent = AIAgent(agent_id=2, role="social media management", provider="openai", base_url="https://api.openai.com")
    blockchain_agent = AIAgent(agent_id=3, role="blockchain operations", provider="ollama", base_url="http://localhost:11434")

    # Agents perform tasks
    data_agent.execute_task("Analyze sales data for the last quarter.")
    social_agent.execute_task("Generate a social media post about AI innovation.")
    blockchain_agent.execute_task("Prepare a smart contract deployment workflow.")

    # Save and load knowledge base
    data_agent.save_knowledge_base("data_agent_knowledge.json")
    data_agent.load_knowledge_base("data_agent_knowledge.json")

    # Add and process tasks in a priority queue
    social_agent.add_task(priority=1, task_description="Create a tweet about decentralized AI.")
    social_agent.add_task(priority=2, task_description="Schedule a blog post.")
    social_agent.process_next_task()

    # Agents interact with each other
    data_agent.interact_with_agent(social_agent, "Share data insights for social media campaign.")