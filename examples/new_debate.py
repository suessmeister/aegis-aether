from src.agents.ai_agent import AIAgent

# Initialize two nodes with LLM capabilities
node_a = AIAgent(agent_id=0, role="worker", provider="openai", base_url="https://api.openai.com")
node_b = AIAgent(agent_id=1, role="worker", provider="openai", base_url="https://api.openai.com")

# Debate topic
topic = "Is artificial intelligence a threat to humanity?"

# Node A's argument
argument_a = node_a.execute_text_task(f"Provide an argument supporting: {topic}")

# Node B's counter-argument
counter_argument_b = node_b.execute_text_task(f"Counter the argument: {argument_a}")

# Final argument by Node A
final_argument_a = node_a.execute_text_task(
    f"Respond to the counter-argument: {counter_argument_b}"
)

print("### AI Debate ###")
print(f"Topic: {topic}")
print(f"Node A's Argument: {argument_a}")
print(f"Node B's Counter-Argument: {counter_argument_b}")
print(f"Node A's Final Argument: {final_argument_a}")
