from src.agents.ai_agent import AIAgent

if __name__ == "__main__":
    # Create an AI agent
    agent = AIAgent(agent_id=1, role="knowledge manager", provider="openai", base_url="https://api.openai.com")

    # Add concepts to the knowledge graph
    agent.add_knowledge("Artificial Intelligence", {"field": "Computer Science"})
    agent.add_knowledge("Machine Learning", {"type": "AI Technique"})
    agent.add_knowledge("Deep Learning", {"type": "AI Technique"})

    # Add relationships between concepts
    agent.add_knowledge_relationship("Artificial Intelligence", "Machine Learning", "includes")
    agent.add_knowledge_relationship("Machine Learning", "Deep Learning", "includes")

    # Query a concept
    query_result = agent.query_knowledge("Machine Learning")
    print("Query Result:", query_result)

    # Visualize the knowledge graph
    agent.visualize_knowledge_graph(output_path="knowledge_graph.png")