from src.integrations.mongodb.mongodb_client import MongoDBClient

# Initialize MongoDB client
mongo_client = MongoDBClient()

# Insert a document
doc_id = mongo_client.insert_document("agents", {"name": "Agent-1", "role": "worker"})
print(f"Document inserted with ID: {doc_id}")

# Find a document
document = mongo_client.find_document("agents", {"name": "Agent-1"})
print(f"Found document: {document}")

# Delete a document
deleted_count = mongo_client.delete_document("agents", {"name": "Agent-1"})
print(f"Deleted {deleted_count} document(s)")

# Close connection
mongo_client.close_connection()