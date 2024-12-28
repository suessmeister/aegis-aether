from src.core.node_autonomy import AutonomousNode

# Initialize two nodes with LLM capabilities
node_a = AutonomousNode(0, llm_api_key="your-openai-api-key")
node_b = AutonomousNode(1, llm_api_key="your-openai-api-key")

# Debate topic
topic = "Is artificial intelligence a threat to humanity?"

# Node A's argument
argument_a = node_a.query_llm(f"Provide an argument supporting: {topic}")

# Node B's counter-argument
counter_argument_b = node_b.query_llm(f"Counter the argument: {argument_a}")

# Final argument by Node A
final_argument_a = node_a.query_llm(f"Respond to the counter-argument: {counter_argument_b}")

print("### AI Debate ###")
print(f"Topic: {topic}")
print(f"Node A's Argument: {argument_a}")
print(f"Node B's Counter-Argument: {counter_argument_b}")
print(f"Node A's Final Argument: {final_argument_a}")