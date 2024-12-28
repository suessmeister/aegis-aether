class MultiObjectiveOptimizer:
    """Optimize multiple objectives for the swarm."""
    def __init__(self, objectives):
        self.objectives = objectives  # List of objective functions

    def evaluate(self, node_states):
        """Evaluate all objectives for the current swarm state."""
        scores = {}
        for obj_name, obj_func in self.objectives.items():
            scores[obj_name] = obj_func(node_states)
        return scores

# Example usage
if __name__ == "__main__":
    def energy_efficiency(states):
        return sum(node["energy"] for node in states) / len(states)

    def task_completion(states):
        return sum(node["tasks_completed"] for node in states)

    objectives = {
        "energy_efficiency": energy_efficiency,
        "task_completion": task_completion,
    }

    optimizer = MultiObjectiveOptimizer(objectives)
    node_states = [{"energy": 80, "tasks_completed": 5}, {"energy": 60, "tasks_completed": 8}]
    print(optimizer.evaluate(node_states))