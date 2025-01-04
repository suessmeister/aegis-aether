import random
import redis

class AdvancedSwarmConsensus:
    """
    Advanced Swarm Consensus module for distributed decision-making.
    """

    def __init__(self, agent_id, redis_host="localhost", redis_port=6379):
        self.agent_id = agent_id
        self.redis_client = redis.StrictRedis(host=redis_host, port=redis_port, decode_responses=True)

    def propose_task(self, task_description):
        """Propose a task to the swarm."""
        proposal_id = f"task_{random.randint(1000, 9999)}"
        self.redis_client.hset(proposal_id, "description", task_description)
        self.redis_client.hset(proposal_id, "votes", 0)
        print(f"Agent {self.agent_id} proposed task: {task_description} with ID {proposal_id}")
        return proposal_id

    def vote(self, proposal_id):
        """Vote on a task proposal."""
        if not self.redis_client.exists(proposal_id):
            print(f"Proposal {proposal_id} does not exist.")
            return False
        current_votes = int(self.redis_client.hget(proposal_id, "votes"))
        self.redis_client.hset(proposal_id, "votes", current_votes + 1)
        print(f"Agent {self.agent_id} voted for proposal {proposal_id}. Total votes: {current_votes + 1}")
        return True

    def get_consensus(self, threshold):
        """Check if consensus is reached on any proposal."""
        for key in self.redis_client.scan_iter("task_*"):
            votes = int(self.redis_client.hget(key, "votes"))
            if votes >= threshold:
                description = self.redis_client.hget(key, "description")
                print(f"Consensus reached on task: {description} with {votes} votes.")
                return key, description
        print("No consensus reached yet.")
        return None, None

    def finalize_task(self, proposal_id):
        """Finalize the task that reached consensus."""
        if self.redis_client.exists(proposal_id):
            task_description = self.redis_client.hget(proposal_id, "description")
            self.redis_client.delete(proposal_id)
            print(f"Task {task_description} with ID {proposal_id} finalized and removed from proposals.")
            return True
        print(f"Proposal {proposal_id} does not exist.")
        return False

# Example Usage
if __name__ == "__main__":
    agent_id = 1
    swarm = AdvancedSwarmConsensus(agent_id)

    # Propose tasks
    proposal_1 = swarm.propose_task("Analyze social media trends")
    proposal_2 = swarm.propose_task("Optimize gaming AI strategies")

    # Agents vote on tasks
    swarm.vote(proposal_1)
    swarm.vote(proposal_1)
    swarm.vote(proposal_2)

    # Check for consensus
    consensus_id, consensus_description = swarm.get_consensus(threshold=2)

    # Finalize task if consensus is reached
    if consensus_id:
        swarm.finalize_task(consensus_id)