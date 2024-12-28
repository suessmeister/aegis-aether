import json
import queue
from solana.keypair import Keypair
from src.utils.llm_client import LLMClient
from src.utils.multi_modal_handler import MultiModalHandler
from src.swarm.swarm_consensus import SwarmConsensus
from src.integrations.solana_utils import SolanaUtils
from src.integrations.solana_task_logger import SolanaTaskLogger
from src.utils.redis_task_queue import RedisTaskQueue
from src.utils.knowledge_graph import KnowledgeGraph
from src.utils.ipfs_client import IPFSClient


class AIAgent:
    """An intelligent AI agent with IPFS integration, knowledge graph, multi-modal capabilities, distributed task queue, and blockchain features."""

    def __init__(self, agent_id, role, provider, base_url):
        self.agent_id = agent_id
        self.role = role
        self.llm_client = LLMClient(provider, base_url)
        self.multi_modal_handler = MultiModalHandler()  # Multi-modal capabilities
        self.consensus = SwarmConsensus(agent_id)  # Swarm decision-making
        self.solana_utils = SolanaUtils()  # Solana blockchain integration
        self.task_logger = SolanaTaskLogger()  # On-chain task logging
        self.redis_queue = RedisTaskQueue()  # Distributed task queue
        self.knowledge_graph = KnowledgeGraph()  # Knowledge graph integration
        self.ipfs_client = IPFSClient()  # IPFS integration
        self.keypair = Keypair.generate()  # Generate a Solana wallet for the agent
        self.knowledge_base = []  # Stores learned knowledge or task history
        self.task_queue = queue.PriorityQueue()  # Local task queue for prioritization

    # Multi-modal task execution
    def execute_text_task(self, task_description):
        result = self.multi_modal_handler.process_text(task_description)
        print(f"Agent {self.agent_id}: Text task result - {result}")
        return result

    def execute_image_task(self, image_path, text_prompts):
        result = self.multi_modal_handler.process_image(image_path, text_prompts)
        print(f"Agent {self.agent_id}: Image task result - {result}")
        return result

    def execute_audio_task(self, audio_path):
        try:
            result = self.multi_modal_handler.process_audio(audio_path)
            print(f"Agent {self.agent_id}: Audio task result - {result}")
            return result
        except NotImplementedError as e:
            print(f"Agent {self.agent_id}: {e}")
            return None

    # Distributed task queue
    def push_task_to_queue(self, task_description):
        task = {
            "agent_id": self.agent_id,
            "role": self.role,
            "task_description": task_description
        }
        self.redis_queue.push_task(task)

    def pull_task_from_queue(self):
        task = self.redis_queue.pop_task()
        if task:
            print(f"Agent {self.agent_id}: Processing task from queue - {task['task_description']}")
            self.execute_task(task["task_description"])

    # Solana blockchain integration
    def check_balance(self):
        balance = self.solana_utils.get_balance(self.keypair.public_key)
        print(f"Agent {self.agent_id}: Solana wallet balance is {balance} lamports.")
        return balance

    def send_sol(self, recipient_pubkey, amount):
        print(f"Agent {self.agent_id}: Sending {amount} lamports to {recipient_pubkey}.")
        response = self.solana_utils.send_transaction(self.keypair, recipient_pubkey, amount)
        print(f"Agent {self.agent_id}: Transaction successful with signature {response}.")
        return response

    def deploy_contract(self, program_path):
        print(f"Agent {self.agent_id}: Deploying smart contract from {program_path}.")
        response = self.solana_utils.deploy_program(self.keypair, program_path)
        print(f"Agent {self.agent_id}: Contract deployed with signature {response}.")
        return response

    # On-chain task logging
    def log_task_on_chain(self, task_description, task_result):
        print(f"Agent {self.agent_id}: Logging task on-chain.")
        return self.task_logger.log_task(
            sender_keypair=self.keypair,
            task_description=task_description,
            task_result=task_result
        )

    # Knowledge graph methods
    def add_knowledge(self, concept, attributes=None):
        self.knowledge_graph.add_concept(concept, attributes)

    def add_knowledge_relationship(self, concept1, concept2, relationship_type):
        self.knowledge_graph.add_relationship(concept1, concept2, relationship_type)

    def query_knowledge(self, concept):
        return self.knowledge_graph.query_concept(concept)

    def visualize_knowledge_graph(self, output_path="knowledge_graph.png"):
        self.knowledge_graph.visualize_graph(output_path)

    # IPFS integration
    def upload_to_ipfs(self, file_path):
        """Upload a file to IPFS."""
        return self.ipfs_client.upload_file(file_path)

    def download_from_ipfs(self, cid, output_path):
        """Download a file from IPFS."""
        self.ipfs_client.retrieve_file(cid, output_path)

    # Swarm decision-making
    def propose_task_to_swarm(self, task_description):
        return self.consensus.propose_task(task_description)

    def vote_on_task(self, proposal_id):
        self.consensus.vote(proposal_id)

    def check_consensus(self):
        return self.consensus.get_consensus()

    # Local task management
    def add_task(self, priority, task_description):
        self.task_queue.put((priority, task_description))
        print(f"Agent {self.agent_id}: Task added with priority {priority} - {task_description}")

    def process_next_task(self):
        if not self.task_queue.empty():
            priority, task_description = self.task_queue.get()
            print(f"Agent {self.agent_id}: Processing task with priority {priority} - {task_description}")
            self.execute_task(task_description)
        else:
            print(f"Agent {self.agent_id}: No tasks in the queue.")

    # Knowledge base management
    def add_to_knowledge_base(self, task_description, result):
        self.knowledge_base.append({"task": task_description, "result": result})

    def save_knowledge_base(self, filename):
        with open(filename, 'w') as f:
            json.dump(self.knowledge_base, f)
        print(f"Agent {self.agent_id}: Knowledge base saved to {filename}.")

    def load_knowledge_base(self, filename):
        try:
            with open(filename, 'r') as f:
                self.knowledge_base = json.load(f)
            print(f"Agent {self.agent_id}: Knowledge base loaded from {filename}.")
        except FileNotFoundError:
            print(f"Agent {self.agent_id}: No existing knowledge base found at {filename}. Starting fresh.")