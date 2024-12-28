from src.core.lattice_engine import LatticeEngine
from src.core.node_autonomy import AutonomousNode

# Initialize the lattice and nodes
lattice = LatticeEngine()
nodes = [AutonomousNode(i, llm_api_key="your-openai-api-key") for i in range(3)]
for node in nodes:
    lattice.add_node(node)
lattice.connect_nodes(nodes[0], nodes[1])
lattice.connect_nodes(nodes[1], nodes[2])

# Collaborative task: Nodes generating a story together
story_part1 = nodes[0].query_llm("Start a short story about an AI revolution.")
story_part2 = nodes[1].query_llm(f"Continue the story: {story_part1}")
story_part3 = nodes[2].query_llm(f"Conclude the story: {story_part2}")

print("### Collaborative Story ###")
print(f"Part 1: {story_part1}")
print(f"Part 2: {story_part2}")
print(f"Part 3: {story_part3}")