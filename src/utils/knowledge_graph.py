import networkx as nx


class KnowledgeGraph:
    """Manages a knowledge graph for AI agents."""

    def __init__(self):
        self.graph = nx.DiGraph()  # Directed graph for knowledge representation

    def add_concept(self, concept, attributes=None):
        """Add a concept to the graph."""
        if attributes is None:
            attributes = {}
        self.graph.add_node(concept, **attributes)
        print(f"Added concept: {concept} with attributes: {attributes}")

    def add_relationship(self, concept1, concept2, relationship_type):
        """Add a relationship between two concepts."""
        self.graph.add_edge(concept1, concept2, relationship=relationship_type)
        print(f"Added relationship: {concept1} -> {concept2} ({relationship_type})")

    def query_concept(self, concept):
        """Retrieve details about a concept."""
        if concept in self.graph:
            attributes = self.graph.nodes[concept]
            relationships = list(self.graph.edges(concept, data=True))
            return {
                "concept": concept,
                "attributes": attributes,
                "relationships": relationships
            }
        else:
            print(f"Concept {concept} not found.")
            return None

    def visualize_graph(self, output_path="knowledge_graph.png"):
        """Visualize the knowledge graph and save as an image."""
        try:
            import matplotlib.pyplot as plt
            plt.figure(figsize=(12, 8))
            pos = nx.spring_layout(self.graph)
            nx.draw(
                self.graph, pos, with_labels=True, node_color="lightblue", edge_color="gray",
                node_size=2000, font_size=10, font_weight="bold"
            )
            edge_labels = nx.get_edge_attributes(self.graph, "relationship")
            nx.draw_networkx_edge_labels(self.graph, pos, edge_labels=edge_labels)
            plt.savefig(output_path)
            print(f"Knowledge graph visualized and saved to {output_path}")
        except ImportError:
            print("Visualization requires matplotlib. Install it using `pip install matplotlib`.")