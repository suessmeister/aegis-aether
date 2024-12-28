import json
import queue
import threading
from src.utils.llm_client import LLMClient
from src.utils.multi_modal_handler import MultiModalHandler
from src.swarm.swarm_consensus import SwarmConsensus


class AIAgent:
    """An intelligent AI agent with multi-modal capabilities, task management, and swarm decision-making."""

    def __init__(self, agent_id, role, provider, base_url):
        self.agent_id = agent_id
        self.role = role
        self.llm_client = LLMClient(provider, base_url)
        self.multi_modal_handler = MultiModalHandler()  # Multi-modal capabilities
        self.consensus = SwarmConsensus(agent_id)  # Swarm decision-making
        self.knowledge_base = []  # Stores learned knowledge or task history
        self.task_queue = queue.PriorityQueue()  # Priority queue for task management

    # Multi-modal task execution
    def execute_text_task(self, task_description):
        """Process a text-based task."""
        result = self.multi_modal_handler.process_text(task_description)
        print(f"Agent {self.agent_id}: Text task result - {result}")
        return result

    def execute_image_task(self, image_path, text_prompts):
        """Process an image-based task."""
        result = self.multi_modal_handler.process_image(image_path, text_prompts)
        print(f"Agent {self.agent_id}: Image task result - {result}")
        return result

    def execute_audio_task(self, audio_path):
        """Process an audio-based task."""
        try:
            result = self.multi_modal_handler.process_audio(audio_path)
            print(f"Agent {self.agent_id}: Audio task result - {result}")
            return result
        except NotImplementedError as e:
            print(f"Agent {self.agent_id}: {e}")
            return None

    # Swarm decision-making
    def propose_task_to_swarm(self, task_description):
        """Propose a task to the swarm for consensus."""
        return self.consensus.propose_task(task_description)

    def vote_on_task(self, proposal_id):
        """Vote for a proposed task."""
        self.consensus.vote(proposal_id)

    def check_consensus(self):
        """Check if consensus has been reached on any task."""
        return self.consensus.get_consensus()

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