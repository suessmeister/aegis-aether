from neo4j import GraphDatabase

class Neo4jClient:
    def __init__(self, uri="bolt://localhost:7687", user="neo4j", password="password"):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    def create_node(self, label, properties):
        query = f"CREATE (n:{label} {{ {', '.join(f'{k}: ${k}' for k in properties.keys())} }}) RETURN id(n)"
        with self.driver.session() as session:
            return session.run(query, **properties).single()[0]

    def find_node(self, label, property_key, property_value):
        query = f"MATCH (n:{label} {{ {property_key}: $value }}) RETURN n"
        with self.driver.session() as session:
            return session.run(query, value=property_value).single()