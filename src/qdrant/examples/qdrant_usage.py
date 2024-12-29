from src.integrations.qdrant.qdrant_client import QdrantClientWrapper

# Initialize Qdrant client
qdrant = QdrantClientWrapper(collection_name="agents")

# Create collection
qdrant.create_collection(vector_size=3)

# Add a vector
qdrant.add_vector([0.1, 0.2, 0.3], {"name": "Agent-1", "role": "worker"})

# Search for similar vectors
results = qdrant.search([0.1, 0.2, 0.3])
print(f"Search results: {results}")