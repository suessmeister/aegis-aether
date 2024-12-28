from src.core.node_autonomy import AutonomousNode

# Initialize nodes with LLM integration
node = AutonomousNode(0, llm_api_key="your-openai-api-key")

# Example dataset
dataset = [
    "Climate change is accelerating.",
    "AI is transforming healthcare.",
    "Quantum computing is the next big thing.",
]

# Node analyzes the dataset
for data in dataset:
    response = node.query_llm(f"Analyze this statement: {data}")
    print(f"Analysis of '{data}': {response}")