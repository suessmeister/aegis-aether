from src.integrations.neo4j.neo4j_client import Neo4jClient

# Initialize Neo4j client
neo4j_client = Neo4jClient(password="your_password")

# Create a node
node_id = neo4j_client.create_node("Agent", {"name": "Agent-1", "role": "worker"})
print(f"Node created with ID: {node_id}")

# Find a node
node = neo4j_client.find_node("Agent", "name", "Agent-1")
print(f"Found node: {node}")

# Close connection
neo4j_client.close()