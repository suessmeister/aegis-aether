import redis


class SwarmConsensus:
    """Handles swarm-based decision-making for small and large swarms using Redis.
    
    Note: 
    - For small swarms, basic methods are sufficient.
    - For larger swarms or more complex data operations, use Lua scripts or Redis transactions for better performance and atomicity.
    """

    def __init__(self, agent_id, redis_host="localhost", redis_port=6379):
        self.agent_id = agent_id
        self.redis_client = redis.StrictRedis(host=redis_host, port=redis_port, decode_responses=True)
        self.proposals_key = "swarm_proposals"
        self.votes_key = "swarm_votes"

    # Basic Methods for Small Swarms
    def propose_task(self, task_description):
        """Propose a task to the swarm."""
        proposal_id = self.redis_client.incr(f"{self.proposals_key}:counter")
        self.redis_client.hset(self.proposals_key, proposal_id, task_description)
        print(f"Agent {self.agent_id} proposed task {proposal_id}: {task_description}")
        return proposal_id

    def vote(self, proposal_id):
        """Vote for a proposed task."""
        self.redis_client.hincrby(self.votes_key, proposal_id, 1)
        print(f"Agent {self.agent_id} voted for task {proposal_id}")

    def get_consensus(self):
        """Check if consensus has been reached on any task (small swarms only)."""
        votes = self.redis_client.hgetall(self.votes_key)
        for proposal_id, vote_count in votes.items():
            if int(vote_count) > 2:  # Example threshold for consensus
                task = self.redis_client.hget(self.proposals_key, proposal_id)
                print(f"Consensus reached for task {proposal_id}: {task}")
                return {"proposal_id": proposal_id, "task": task}
        print("No consensus reached.")
        return None

    # Advanced Methods for Larger Swarms
    def propose_task_with_lua(self, task_description):
        """Propose a task using a Lua script (recommended for larger swarms)."""
        lua_script = """
        local proposal_id = redis.call('INCR', KEYS[1])
        redis.call('HSET', KEYS[2], proposal_id, ARGV[1])
        return proposal_id
        """
        script = self.redis_client.register_script(lua_script)
        proposal_id = script(keys=[f"{self.proposals_key}:counter", self.proposals_key], args=[task_description])
        print(f"Agent {self.agent_id} proposed task with Lua {proposal_id}: {task_description}")
        return proposal_id

    def vote_with_transaction(self, proposal_id):
        """Vote for a proposal using Redis transactions."""
        with self.redis_client.pipeline() as pipe:
            pipe.watch(self.votes_key)
            current_votes = int(self.redis_client.hget(self.votes_key, proposal_id) or 0)
            pipe.multi()
            pipe.hincrby(self.votes_key, proposal_id, 1)
            pipe.execute()
        print(f"Agent {self.agent_id} voted for task {proposal_id} using a transaction.")

    def get_consensus_with_lua(self, threshold=3):
        """Check for consensus using a Lua script (for larger swarms)."""
        lua_script = """
        local results = {}
        for proposal_id, vote_count in pairs(redis.call('HGETALL', KEYS[1])) do
            if tonumber(vote_count) >= tonumber(ARGV[1]) then
                table.insert(results, proposal_id)
                table.insert(results, redis.call('HGET', KEYS[2], proposal_id))
            end
        end
        return results
        """
        script = self.redis_client.register_script(lua_script)
        result = script(keys=[self.votes_key, self.proposals_key], args=[threshold])
        consensus = [{"proposal_id": result[i], "task": result[i + 1]} for i in range(0, len(result), 2)]
        if consensus:
            print(f"Consensus reached: {consensus}")
        else:
            print("No consensus reached.")
        return consensus