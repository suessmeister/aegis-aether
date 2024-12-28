from src.democracy.proposal_manager import ProposalManager

class SwarmVoting:
    """Handles proposal creation and voting within the swarm."""

    def __init__(self, agents):
        self.agents = agents
        self.proposal_manager = ProposalManager()

    def create_and_vote(self, description, expiration_time):
        """Create a proposal and initiate voting."""
        proposal_id = f"proposal-{len(self.proposal_manager.proposals) + 1}"
        # Randomly select an agent to create the proposal
        creator_agent = self.agents[0]  # Example: first agent creates the proposal
        creator_agent.create_proposal(self.proposal_manager, proposal_id, description, expiration_time)

        # All agents vote on the proposal
        for agent in self.agents:
            vote = agent.decide_vote(proposal_id)
            self.proposal_manager.vote(proposal_id, vote)

        # Check and return the results
        results = self.proposal_manager.check_results(proposal_id)
        return results