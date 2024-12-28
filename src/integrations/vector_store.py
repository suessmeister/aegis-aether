from pymongo import MongoClient

class VectorStore:
    def __init__(self, connection_string):
        self.client = MongoClient(connection_string)
        self.db = self.client['vector_db']
        self.collection = self.db['vectors']

    def insert_vector(self, vector_id, vector_data):
        self.collection.insert_one({'_id': vector_id, 'vector': vector_data})

    def get_vector(self, vector_id):
        return self.collection.find_one({'_id': vector_id})

# Example usage
if __name__ == "__main__":
    store = VectorStore("mongodb://localhost:27017/")
    store.insert_vector("vec1", [0.1, 0.2, 0.3])
    print(store.get_vector("vec1"))