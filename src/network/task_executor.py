import threading

class TaskExecutor:
    def __init__(self):
        self.tasks = []

    def add_task(self, function, args=()):
        """Add a task to the execution queue."""
        task = threading.Thread(target=function, args=args)
        self.tasks.append(task)

    def run_all(self):
        """Execute all tasks in parallel."""
        for task in self.tasks:
            task.start()
        for task in self.tasks:
            task.join()
        print("All tasks completed.")

# Example usage
if __name__ == "__main__":
    def sample_task(name):
        print(f"Task {name} is running.")

    executor = TaskExecutor()
    executor.add_task(sample_task, args=("A",))
    executor.add_task(sample_task, args=("B",))
    executor.run_all()