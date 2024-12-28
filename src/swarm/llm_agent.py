from src.swarm.advanced_swarm_behavior import SwarmNode
from src.utils.llm_client import LLMClient

class LLMAgent(SwarmNode):
    """A SwarmNode that interacts with LLMs."""

    def __init__(self, id, role, provider, base_url):
        super().__init__(id, role)
        self.llm_client = LLMClient(provider, base_url)

    def generate_response(self, prompt, model="gpt-4"):
        """Generate a response using the LLM client."""
        try:
            response = self.llm_client.send_request(prompt, model)
            return response
        except Exception as e:
            print(f"Error generating response: {e}")
            return None

    def interact(self, other_node):
        """Interact with another node using LLM responses."""
        prompt = f"Generate a message for Node {other_node.id}"
        response = self.generate_response(prompt)
        if response:
            print(f"Node {self.id} to Node {other_node.id}: {response}")
        else:
            print(f"Node {self.id} failed to generate a response.")