import json
import queue
import threading
from solana.keypair import Keypair
from src.utils.llm_client import LLMClient
from src.utils.multi_modal_handler import MultiModalHandler
from src.swarm.swarm_consensus import SwarmConsensus
from src.integrations.solana_utils import SolanaUtils
from src.integrations.solana_task_logger import SolanaTaskLogger
from src.utils.redis_task_queue import RedisTaskQueue


class AIAgent:
    """An intelligent AI agent with multi-modal capabilities, distributed task queue, Solana blockchain integration, on-chain logging, and swarm decision-making."""

    def __init__(self, agent_id, role, provider, base_url):
        self.agent_id = agent_id
        self.role = role
        self.llm_client = LLMClient(provider, base_url)
        self.multi_modal_handler = MultiModalHandler()  # Multi-modal capabilities
        self.consensus = SwarmConsensus(agent_id)  # Swarm decision-making
        self.solana_utils = SolanaUtils()  # Solana blockchain integration
        self.task_logger = SolanaTaskLogger()  # On-chain task logging
        self.redis_queue = RedisTaskQueue()  # Distributed task queue
        self.keypair = Keypair.generate()  # Generate a Solana wallet for the agent
        self.knowledge_base = []  # Stores learned knowledge or task history
        self.task_queue = queue.PriorityQueue()  # Local task queue for prioritization

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

    # Distributed task queue
    def push_task_to_queue(self, task_description):
        """Push a task to the distributed task queue."""
        task = {
            "agent_id": self.agent_id,
            "role": self.role,
            "task_description": task_description
        }
        self.redis_queue.push_task(task)

    def pull_task_from_queue(self):
        """Pull a task from the distributed task queue."""
        task = self.redis_queue.pop_task()
        if task:
            print(f"Agent {self.agent_id}: Processing task from queue - {task['task_description']}")
            self.execute_task(task["task_description"])

    # Solana blockchain integration
    def check_balance(self):
        """Check the agent's Solana wallet balance."""
        balance = self.solana_utils.get_balance(self.keypair.public_key)
        print(f"Agent {self.agent_id}: Solana wallet balance is {balance} lamports.")
        return balance

    def send_sol(self, recipient_pubkey, amount):
        """Send SOL from the agent's wallet to another wallet."""
        print(f"Agent {self.agent_id}: Sending {amount} lamports to {recipient_pubkey}.")
        response = self.solana_utils.send_transaction(self.keypair, recipient_pubkey, amount)
        print(f"Agent {self.agent_id}: Transaction successful with signature {response}.")
        return response

    def deploy_contract(self, program_path):
        """Deploy a Solana program from the agent's wallet."""
        print(f"Agent {self.agent_id}: Deploying smart contract from {program_path}.")
        response = self.solana_utils.deploy_program(self.keypair, program_path)
        print(f"Agent {self.agent_id}: Contract deployed with signature {response}.")
        return response

    # On-chain task logging
    def log_task_on_chain(self, task_description, task_result):
        """Log a task and its result on the Solana blockchain."""
        print(f"Agent {self.agent_id}: Logging task on-chain.")
        return self.task_logger.log_task(
            sender_keypair=self.keypair,
            task_description=task_description,
            task_result=task_result
        )

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

    # Local task management
    def add_task(self, priority, task_description):
        """Add a task to the agent's local priority queue."""
        self.task_queue.put((priority, task_description))
        print(f"Agent {self.agent_id}: Task added with priority {priority} - {task_description}")

    def process_next_task(self):
        """Process the next task in the local priority queue."""
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