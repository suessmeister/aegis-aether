class TaskScheduler:
    """Dynamic task scheduling for swarm nodes."""
    def __init__(self):
        self.tasks = []

    def add_task(self, node_id, task, priority):
        """Add a task with a specific priority."""
        self.tasks.append({"node_id": node_id, "task": task, "priority": priority})
        self.tasks = sorted(self.tasks, key=lambda x: x["priority"], reverse=True)

    def assign_task(self, nodes):
        """Assign tasks to nodes based on priority."""
        for task in self.tasks[:]:
            node = next((n for n in nodes if n.id == task["node_id"] and n.role != "inactive"), None)
            if node:
                print(f"Task '{task['task']}' assigned to Node {node.id} with priority {task['priority']}.")
                node.perform_task()
                self.tasks.remove(task)

# Example usage
if __name__ == "__main__":
    from src.swarm.advanced_swarm_behavior import Swarm

    swarm = Swarm(5)
    scheduler = TaskScheduler()

    # Add tasks
    scheduler.add_task(0, "Process data", priority=3)
    scheduler.add_task(1, "Analyze signals", priority=1)
    scheduler.add_task(2, "Explore environment", priority=2)

    # Assign tasks
    scheduler.assign_task(swarm.nodes)