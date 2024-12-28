import random
from src.integrations.ipfs_communication import IPFSCommunication

class ReinforcementLearningAgent:
    """A basic RL agent for swarm nodes."""
    def __init__(self):
        self.q_table = {}
        self.learning_rate = 0.1
        self.discount_factor = 0.9

    def choose_action(self, state, actions):
        """Choose an action based on Q-values or explore."""
        if random.random() < 0.1:  # Exploration rate
            return random.choice(actions)
        return max(actions, key=lambda action: self.q_table.get((state, action), 0))

    def update_q_value(self, state, action, reward, next_state, next_actions):
        """Update the Q-value using the Bellman equation."""
        current_q = self.q_table.get((state, action), 0)
        max_future_q = max(self.q_table.get((next_state, a), 0) for a in next_actions)
        new_q = current_q + self.learning_rate * (reward + self.discount_factor * max_future_q - current_q)
        self.q_table[(state, action)] = new_q


class SwarmNode:
    """A single node in an AI swarm with advanced behaviors."""
    def __init__(self, id, role="worker"):
        self.id = id
        self.role = role
        self.state = random.random()  # Initial state
        self.energy = random.randint(50, 100)
        self.tasks_completed = 0
        self.knowledge = {}  # Shared knowledge
        self.rl_agent = ReinforcementLearningAgent()
        self.ipfs = IPFSCommunication()  # Add IPFS communication

    def interact(self, other_node):
        """Simulate interaction between nodes."""
        if self.role == "worker" and other_node.role == "explorer":
            self.knowledge.update(other_node.knowledge)
        self.state = (self.state + other_node.state) / 2
        print(f"Node {self.id} interacted with Node {other_node.id}")

    def perform_task(self):
        """Perform a task based on the node's role and reinforcement learning."""
        state = "normal"
        actions = ["explore", "process", "rest"]
        action = self.rl_agent.choose_action(state, actions)

        if action == "explore":
            self.explore()
        elif action == "process":
            self.process()
        elif action == "rest":
            self.rest()

        reward = random.randint(0, 10)  # Random reward for simplicity
        self.rl_agent.update_q_value(state, action, reward, "normal", actions)

    def explore(self):
        """Node explores and gathers data."""
        print(f"Node {self.id} (explorer) is gathering data.")
        self.knowledge[random.randint(0, 100)] = random.random()

    def process(self):
        """Node processes data."""
        print(f"Node {self.id} (worker) is processing data.")
        self.tasks_completed += 1

    def rest(self):
        """Node recharges energy."""
        print(f"Node {self.id} is resting to recharge energy.")
        self.energy = min(100, self.energy + 10)

    def send_message(self, other_node, message):
        """Send a message to another node."""
        print(f"Node {self.id} sends message to Node {other_node.id}: {message}")
        other_node.receive_message(self.id, message)

    def receive_message(self, sender_id, message):
        """Receive a message from another node."""
        print(f"Node {self.id} received message from Node {sender_id}: {message}")
        self.knowledge[sender_id] = message

    def fail(self):
        """Simulate node failure."""
        if self.role != "inactive":  # Ensure the node isn't already inactive
            self.role = "inactive"
            self.energy = 0
            self.tasks_completed = 0  # Reset any ongoing work
            self.knowledge.clear()  # Clear knowledge to simulate failure
            print(f"Node {self.id} has failed and is now inactive.")

    def recover(self):
        """Recover a failed node."""
        if self.role == "inactive":  # Only allow recovery for inactive nodes
            self.role = random.choice(["worker", "explorer", "coordinator"])
            self.energy = random.randint(50, 100)  # Assign new energy
            print(f"Node {self.id} has recovered and is now active with role: {self.role}.")

    def send_decentralized_message(self, message):
        """Send a message to IPFS."""
        print(f"Node {self.id} sending message to IPFS...")
        return self.ipfs.send_message(message)

    def retrieve_decentralized_message(self, ipfs_hash):
        """Retrieve a message from IPFS."""
        print(f"Node {self.id} retrieving message from IPFS...")
        return self.ipfs.retrieve_message(ipfs_hash)


class Swarm:
    """A collection of swarm nodes with specialized roles and behaviors."""
    def __init__(self, node_count):
        self.nodes = [
            SwarmNode(i, role=random.choice(["worker", "explorer", "coordinator"]))
            for i in range(node_count)
        ]

    def simulate(self, iterations):
        """Simulate swarm activity with interactions and tasks."""
        for _ in range(iterations):
            print("\n--- Iteration ---")
            for node in self.nodes:
                if node.role != "inactive":
                    node.perform_task()
                else:
                    if random.random() < 0.2:  # 20% chance of recovery
                        node.recover()

            # Randomly fail a node
            if random.random() < 0.2:  # 20% chance of failure
                random.choice(self.nodes).fail()

            # Random node interactions
            active_nodes = [node for node in self.nodes if node.role != "inactive"]
            if len(active_nodes) > 1:
                node1, node2 = random.sample(active_nodes, 2)
                node1.interact(node2)


# Example usage
if __name__ == "__main__":
    swarm = Swarm(10)
    swarm.simulate(5)