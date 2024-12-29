from src.integrations.sqlite.sqlite_client import SQLiteClient

# Initialize SQLite client
sqlite = SQLiteClient()

# Create table
sqlite.create_table("agents", "id INTEGER PRIMARY KEY, name TEXT, role TEXT")

# Insert data
sqlite.insert_data("agents", "name, role", "'Agent-1', 'worker'")

# Query data
data = sqlite.query_data("agents", "*")
print(f"Query results: {data}")

# Close connection
sqlite.close()