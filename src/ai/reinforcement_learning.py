import random

class ReinforcementLearningAgent:
    def __init__(self, node, learning_rate=0.1, discount_factor=0.9):
        self.node = node
        self.q_table = {}  # State-action mapping
        self.learning_rate = learning_rate
        self.discount_factor = discount_factor

    def choose_action(self, state, actions):
        """Choose an action based on Q-values or explore randomly."""
        if random.random() < 0.1:  # Exploration rate
            return random.choice(actions)
        return max(actions, key=lambda action: self.q_table.get((state, action), 0))

    def update_q_value(self, state, action, reward, next_state, next_actions):
        """Update the Q-value using the Bellman equation."""
        current_q = self.q_table.get((state, action), 0)
        max_future_q = max(self.q_table.get((next_state, a), 0) for a in next_actions)
        new_q = current_q + self.learning_rate * (reward + self.discount_factor * max_future_q - current_q)
        self.q_table[(state, action)] = new_q

# Example usage
if __name__ == "__main__":
    from src.core.node_autonomy import AutonomousNode

    node = AutonomousNode(0)
    agent = ReinforcementLearningAgent(node)

    current_state = "low_energy"
    possible_actions = ["recharge", "wait"]
    chosen_action = agent.choose_action(current_state, possible_actions)
    print(f"Chosen action: {chosen_action}")

    reward = 10  # Reward for recharging
    agent.update_q_value(current_state, chosen_action, reward, "high_energy", ["work", "wait"])