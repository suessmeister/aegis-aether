import json
import queue
import threading
from src.utils.llm_client import LLMClient
from src.utils.multi_modal_handler import MultiModalHandler


class AIAgent:
    """An intelligent AI agent with multi-modal capabilities and task management."""

    def __init__(self, agent_id, role, provider, base_url):
        self.agent_id = agent_id
        self.role = role
        self.llm_client = LLMClient(provider, base_url)
        self.multi_modal_handler = MultiModalHandler()  # Multi-modal capabilities
        self.knowledge_base = []  # Stores learned knowledge or task history
        self.task_queue = queue.PriorityQueue()  # Priority queue for task management

    # Task execution
    def execute_task(self, task_description):
        """Execute a task based on the description."""
        prompt = f"You are an AI agent specializing in {self.role}. {task_description}"
        print(f"Agent {self.agent_id}: Executing task - {task_description}")
        try:
            response = self.llm_client.send_request(prompt)
            print(f"Agent {self.agent_id}: Task result - {response}")
            self.add_to_knowledge_base(task_description, response)
            return response
        except Exception as e:
            print(f"Agent {self.agent_id}: Failed to execute task. Error: {e}")
            return None

    def execute_text_task(self, task_description):
        """Process a text-based task using multi-modal handler."""
        result = self.multi_modal_handler.process_text(task_description)
        print(f"Agent {self.agent_id}: Text task result - {result}")
        return result

    def execute_image_task(self, image_path, text_prompts):
        """Process an image-based task using multi-modal handler."""
        result = self.multi_modal_handler.process_image(image_path, text_prompts)
        print(f"Agent {self.agent_id}: Image task result - {result}")
        return result

    def execute_audio_task(self, audio_path):
        """Process an audio-based task using multi-modal handler."""
        try:
            result = self.multi_modal_handler.process_audio(audio_path)
            print(f"Agent {self.agent_id}: Audio task result - {result}")
            return result
        except NotImplementedError as e:
            print(f"Agent {self.agent_id}: {e}")
            return None

    # Interactions with other agents
    def interact_with_agent(self, other_agent, task_description):
        """Interact with another agent and collaborate on a task."""
        print(f"Agent {self.agent_id} interacting with Agent {other_agent.agent_id}")
        response = self.execute_task(task_description)
        if response:
            other_agent.receive_message(self.agent_id, response)
        else:
            print(f"Agent {self.agent_id}: Failed to interact with Agent {other_agent.agent_id}.")

    def receive_message(self, sender_id, message):
        """Handle a message received from another agent."""
        print(f"Agent {self.agent_id} received a message from Agent {sender_id}: {message}")

    # Knowledge base management
    def add_to_knowledge_base(self, task_description, result):
        """Store the task and result in the agent's knowledge base."""
        self.knowledge_base.append({"task": task_description, "result": result})

    def save_knowledge_base(self, filename):
        """Save the agent's knowledge base to a file."""
        with open(filename, 'w') as f:
            json.dump(self.knowledge_base, f)
        print(f"Agent {self.agent_id}: Knowledge base saved to {filename}.")

    def load_knowledge_base(self, filename):
        """Load the agent's knowledge base from a file."""
        try:
            with open(filename, 'r') as f:
                self.knowledge_base = json.load(f)
            print(f"Agent {self.agent_id}: Knowledge base loaded from {filename}.")
        except FileNotFoundError:
            print(f"Agent {self.agent_id}: No existing knowledge base found at {filename}. Starting fresh.")

    # Task management
    def add_task(self, priority, task_description):
        """Add a task to the agent's priority queue."""
        self.task_queue.put((priority, task_description))
        print(f"Agent {self.agent_id}: Task added with priority {priority} - {task_description}")

    def process_next_task(self):
        """Process the next task in the priority queue."""
        if not self.task_queue.empty():
            priority, task_description = self.task_queue.get()
            print(f"Agent {self.agent_id}: Processing task with priority {priority} - {task_description}")
            self.execute_task(task_description)
        else:
            print(f"Agent {self.agent_id}: No tasks in the queue.")

    # Async execution
    def execute_task_async(self, task_description):
        """Execute a task asynchronously."""
        thread = threading.Thread(target=self.execute_task, args=(task_description,))
        thread.start()