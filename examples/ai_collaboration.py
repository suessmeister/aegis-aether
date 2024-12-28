from src.core.lattice_engine import LatticeEngine
from src.core.node_autonomy import AutonomousNode

# Initialize the lattice and nodes
lattice = LatticeEngine()
nodes = [AutonomousNode(i, llm_api_key="your-openai-api-key") for i in range(3)]
for node in nodes:
    lattice.add_node(node)
lattice.connect_nodes(nodes[0], nodes[1])
lattice.connect_nodes(nodes[1], nodes[2])

# Query LLM through nodes
nodes[0].query_llm("Generate a creative idea for solving traffic congestion.")
nodes[1].query_llm("Summarize the latest research on renewable energy.")
nodes[2].query_llm("What are the ethical concerns of AI in medicine?")