from src.swarm.llm_agent import LLMAgent

if __name__ == "__main__":
    # Create nodes with different LLM providers
    openai_node = LLMAgent(id=1, role="worker", provider="openai", base_url="https://api.openai.com")
    llama_node = LLMAgent(id=2, role="worker", provider="ollama", base_url="http://localhost:11434")
    anthropic_node = LLMAgent(id=3, role="coordinator", provider="anthropic", base_url="https://api.anthropic.com")

    # Nodes interact with each other
    openai_node.interact(llama_node)
    llama_node.interact(anthropic_node)