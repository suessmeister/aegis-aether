import json
import queue
import numpy as np
from solana.keypair import Keypair
from src.utils.llm_client import LLMClient
from src.utils.multi_modal_handler import MultiModalHandler
from src.swarm.swarm_consensus import SwarmConsensus
from src.utils.blockchain_manager import BlockchainManager
from src.utils.redis_task_queue import RedisTaskQueue
from src.utils.knowledge_graph import KnowledgeGraph
from src.utils.ipfs_client import IPFSClient
from src.utils.agent_collaboration import CollaborationFramework
from src.utils.reinforcement_learning import QLearning
from src.democracy.proposal_manager import ProposalManager


class AIAgent:
    """An intelligent AI agent with reinforcement learning, collaboration framework, multi-chain blockchain integration, multi-modal capabilities, and democratic voting."""

    def __init__(self, agent_id, role, provider, base_url, ethereum_rpc_url=None, state_size=5, action_size=3):
        self.agent_id = agent_id
        self.role = role
        self.llm_client = LLMClient(provider, base_url)
        self.multi_modal_handler = MultiModalHandler()  # Multi-modal capabilities
        self.consensus = SwarmConsensus(agent_id)  # Swarm decision-making
        self.blockchain_manager = BlockchainManager(ethereum_rpc_url=ethereum_rpc_url)  # Multi-chain blockchain manager
        self.redis_queue = RedisTaskQueue()  # Distributed task queue
        self.knowledge_graph = KnowledgeGraph()  # Knowledge graph integration
        self.ipfs_client = IPFSClient()  # IPFS integration
        self.collaboration = CollaborationFramework()  # Collaboration framework
        self.rl_agent = QLearning(state_size, action_size)  # Reinforcement learning
        self.keypair = Keypair.generate()  # Generate a Solana wallet for the agent
        self.proposal_manager = ProposalManager()  # Democratic voting manager
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
            self.execute_text_task(task["task_description"])

    # Blockchain methods (multi-chain support)
    def get_sol_balance(self):
        return self.blockchain_manager.solana_get_balance(self.keypair.public_key)

    def send_sol(self, recipient_pubkey, amount):
        return self.blockchain_manager.solana_send_transaction(self.keypair, recipient_pubkey, amount)

    def get_eth_balance(self, address):
        return self.blockchain_manager.ethereum_get_balance(address)

    def send_eth(self, sender_key, recipient_address, amount_ether):
        return self.blockchain_manager.ethereum_send_transaction(sender_key, recipient_address, amount_ether)

    # On-chain task logging
    def log_task_on_chain(self, task_description, task_result):
        print(f"Agent {self.agent_id}: Logging task on-chain.")
        return self.blockchain_manager.log_task(
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
        return self.ipfs_client.upload_file(file_path)

    def download_from_ipfs(self, cid, output_path):
        self.ipfs_client.retrieve_file(cid, output_path)

    # Collaboration methods
    def send_message(self, recipient_id, message):
        """Send a message to another agent."""
        self.collaboration.send_message(self.agent_id, recipient_id, message)

    def receive_messages(self):
        """Receive messages for this agent."""
        messages = self.collaboration.receive_message(self.agent_id)
        for msg in messages:
            print(f"Agent {self.agent_id} received message: {msg['message']}")

    def delegate_task(self, recipient_id, task_description):
        """Delegate a task to another agent."""
        self.collaboration.delegate_task(self.agent_id, recipient_id, task_description)

    # Self-Optimization (Reinforcement Learning)
    def optimize_task_execution(self, state):
        """Optimize task execution using reinforcement learning."""
        action = self.rl_agent.choose_action(state)
        reward = self.execute_action(action)
        next_state = self.get_environment_state()
        self.rl_agent.update_q_table(state, action, reward, next_state)
        self.rl_agent.decay_exploration()

    def execute_action(self, action):
        """Execute an action and return a reward."""
        if action == 0:  # Process next task
            self.process_next_task()
            return 1  # Reward for successfully processing a task
        elif action == 1:  # Collaborate with another agent
            self.delegate_task(2, "Collaborate on a task")
            return 2  # Higher reward for collaboration
        elif action == 2:  # Save knowledge
            self.save_knowledge_base("knowledge.json")
            return 1  # Reward for saving knowledge
        return 0  # No reward for invalid actions

    def get_environment_state(self):
        """Simulate the agent's environment state."""
        return np.random.randint(5)

    # Swarm decision-making
    def propose_task_to_swarm(self, task_description):
        return self.consensus.propose_task(task_description)

    def vote_on_task(self, proposal_id):
        self.consensus.vote(proposal_id)

    def check_consensus(self):
        return self.consensus.get_consensus()

    # Democratic decision-making
    def create_proposal(self, proposal_id, description, expiration_time):
        self.proposal_manager.create_proposal(proposal_id, description, expiration_time)
        print(f"Agent {self.agent_id} created proposal {proposal_id}: {description}")

    def vote_on_proposal(self, proposal_id):
        vote = "yes" if random.random() > 0.5 else "no"
        self.proposal_manager.vote(proposal_id, vote)
        print(f"Agent {self.agent_id} voted '{vote}' on proposal {proposal_id}.")