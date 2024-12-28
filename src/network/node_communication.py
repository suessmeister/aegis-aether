from src.utils.llm_integration import LLMIntegration
class AutonomousNode:
    def __init__(self, id, llm_api_key=None):
        self.id = id
        self.state = {
            "energy": 100,
            "evolution_score": 0,
            "message_log": [],
        }
        self.llm = LLMIntegration(api_key=llm_api_key) if llm_api_key else None

    def query_llm(self, prompt):
        """Query the LLM and log the response."""
        if self.llm:
            response = self.llm.query_gpt(prompt)
            if response:
                print(f"Node {self.id} LLM Response: {response}")
                self.state["message_log"].append(response)
            else:
                print(f"Node {self.id} failed to get LLM response.")

    def connect_nodes(self, node_a, node_b):
        """Establish a bidirectional connection between two nodes."""
        self.network.setdefault(node_a.id, []).append(node_b.id)
        self.network.setdefault(node_b.id, []).append(node_a.id)
        print(f"Connected Node {node_a.id} <--> Node {node_b.id}")

    def send_message(self, sender_id, receiver_id, message):
        """Simulate sending a message between nodes."""
        if receiver_id in self.network.get(sender_id, []):
            print(f"Message from Node {sender_id} to Node {receiver_id}: {message}")
        else:
            print(f"Error: Nodes {sender_id} and {receiver_id} are not connected.")