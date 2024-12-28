import unittest
from src.core.lattice_engine import LatticeEngine
from src.core.node_autonomy import AutonomousNode

class TestLatticeEngine(unittest.TestCase):
    def setUp(self):
        """Set up a lattice and some nodes for testing."""
        self.lattice = LatticeEngine()
        self.nodes = [AutonomousNode(i) for i in range(3)]
        for node in self.nodes:
            self.lattice.add_node(node)
        self.lattice.connect_nodes(self.nodes[0], self.nodes[1])
        self.lattice.connect_nodes(self.nodes[1], self.nodes[2])

    def test_signal_propagation(self):
        """Test that signals propagate correctly through the lattice."""
        self.lattice.propagate_signal("Test Signal", start_node_id=0)
        self.assertEqual(self.nodes[1].state["message_log"], ["Test Signal"])
        self.assertEqual(self.nodes[2].state["message_log"], ["Test Signal"])

    def test_energy_deduction(self):
        """Test that nodes lose energy during signal processing."""
        self.lattice.propagate_signal("Energy Test", start_node_id=0, energy_cost=10)
        self.assertTrue(self.nodes[0].state["energy"] < 100)

    def test_recharge(self):
        """Test that a node can recharge its energy."""
        node = self.nodes[0]
        node.recharge(20)
        self.assertEqual(node.state["energy"], 120)

if __name__ == "__main__":
    unittest.main()