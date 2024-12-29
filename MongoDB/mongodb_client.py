from pymongo import MongoClient

class MongoDBClient:
    def __init__(self, uri="mongodb://localhost:27017", db_name="aether"):
        self.client = MongoClient(uri)
        self.db = self.client[db_name]

    def insert_document(self, collection_name, document):
        collection = self.db[collection_name]
        return collection.insert_one(document).inserted_id

    def find_document(self, collection_name, query):
        collection = self.db[collection_name]
        return collection.find_one(query)

    def delete_document(self, collection_name, query):
        collection = self.db[collection_name]
        return collection.delete_one(query).deleted_count

    def close_connection(self):
        self.client.close()