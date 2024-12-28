import random
from threading import Lock


class SwarmConsensus:
    """Leaderless consensus mechanism for distributed swarm decision-making."""

    def __init__(self, agent_id):
        self.agent_id = agent_id
        self.proposals = []  # List of proposed tasks or decisions
        self.votes = {}  # Tracks votes for each proposal
        self.lock = Lock()  # Ensure thread-safe updates

    def propose_task(self, task_description):
        """Propose a task to the swarm."""
        proposal_id = f"{self.agent_id}-{random.randint(1000, 9999)}"
        self.proposals.append({"id": proposal_id, "task": task_description, "votes": 0})
        print(f"Agent {self.agent_id}: Proposed task - {task_description} (ID: {proposal_id})")
        return proposal_id

    def vote(self, proposal_id):
        """Vote for a specific proposal."""
        with self.lock:
            if proposal_id not in self.votes:
                self.votes[proposal_id] = 1
            else:
                self.votes[proposal_id] += 1
        print(f"Agent {self.agent_id}: Voted for proposal ID {proposal_id}")

    def get_consensus(self):
        """Determine if any proposal has reached consensus."""
        with self.lock:
            if not self.votes:
                print(f"Agent {self.agent_id}: No votes have been cast yet.")
                return None
            # Find the proposal with the highest votes
            max_votes = max(self.votes.values())
            for proposal in self.proposals:
                if self.votes.get(proposal["id"], 0) == max_votes:
                    print(f"Agent {self.agent_id}: Consensus reached for proposal ID {proposal['id']}")
                    return proposal
        print(f"Agent {self.agent_id}: No consensus reached.")
        return None