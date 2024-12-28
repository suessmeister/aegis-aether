import sqlite3

class Storage:
    def __init__(self, db_name="lattice.db"):
        self.conn = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS nodes (
            id INTEGER PRIMARY KEY,
            energy INTEGER,
            evolution_score REAL,
            message_log TEXT
        )
        """
        self.conn.execute(query)
        self.conn.commit()

    def save_node(self, node):
        query = """
        INSERT OR REPLACE INTO nodes (id, energy, evolution_score, message_log)
        VALUES (?, ?, ?, ?)
        """
        self.conn.execute(
            query,
            (
                node.id,
                node.state["energy"],
                node.state["evolution_score"],
                ",".join(node.state["message_log"]),
            ),
        )
        self.conn.commit()

    def load_node(self, node_id):
        query = "SELECT * FROM nodes WHERE id = ?"
        cursor = self.conn.execute(query, (node_id,))
        return cursor.fetchone()

# Example usage
if __name__ == "__main__":
    from src.core.node_autonomy import AutonomousNode

    node = AutonomousNode(0)
    storage = Storage()
    storage.save_node(node)
    print(storage.load_node(0))