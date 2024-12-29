from qdrant_client import QdrantClient
from qdrant_client.models import PointStruct

class QdrantClientWrapper:
    def __init__(self, host="localhost", port=6333, collection_name="aether"):
        self.client = QdrantClient(host=host, port=port)
        self.collection_name = collection_name

    def create_collection(self, vector_size):
        self.client.recreate_collection(self.collection_name, vector_size=vector_size)

    def add_vector(self, vector, payload):
        point = PointStruct(id=len(payload), vector=vector, payload=payload)
        self.client.upsert(self.collection_name, [point])

    def search(self, query_vector, top_k=5):
        return self.client.search(self.collection_name, query_vector=query_vector, top=top_k)