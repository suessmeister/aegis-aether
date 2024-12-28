from src.agents.ai_agent import AIAgent

if __name__ == "__main__":
    # Create an agent
    solana_agent = AIAgent(agent_id=1, role="blockchain logger", provider="openai", base_url="https://api.openai.com")

    # Define a task and result
    task_description = "Analyze market trends for decentralized AI."
    task_result = "Identified key trends: increased adoption of modular AI frameworks."

    # Log the task on-chain
    tx_signature = solana_agent.log_task_on_chain(task_description, task_result)
    print(f"Task logged with transaction signature: {tx_signature}")