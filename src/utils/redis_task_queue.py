import redis
import json


class RedisTaskQueue:
    """A distributed task queue using Redis."""

    def __init__(self, redis_host="localhost", redis_port=6379, queue_name="task_queue"):
        self.redis_client = redis.StrictRedis(host=redis_host, port=redis_port, decode_responses=True)
        self.queue_name = queue_name

    def push_task(self, task):
        """Push a new task to the queue."""
        self.redis_client.rpush(self.queue_name, json.dumps(task))
        print(f"Task added to queue: {task}")

    def pop_task(self):
        """Pop a task from the queue."""
        task = self.redis_client.lpop(self.queue_name)
        if task:
            task = json.loads(task)
            print(f"Task retrieved from queue: {task}")
            return task
        print("No tasks in the queue.")
        return None

    def task_count(self):
        """Get the number of tasks in the queue."""
        count = self.redis_client.llen(self.queue_name)
        print(f"Number of tasks in queue: {count}")
        return count