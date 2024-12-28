import time

class ProposalManager:
    """Manages proposals and votes within the system."""

    def __init__(self):
        self.proposals = {}

    def create_proposal(self, proposal_id, description, expiration_time):
        """Create a new proposal."""
        self.proposals[proposal_id] = {
            "description": description,
            "votes": {"yes": 0, "no": 0},
            "expiration_time": time.time() + expiration_time,
            "status": "active",
        }
        print(f"Proposal {proposal_id} created: {description}")

    def vote(self, proposal_id, vote_type):
        """Allow agents to vote on a proposal."""
        if proposal_id not in self.proposals:
            print(f"Proposal {proposal_id} does not exist.")
            return
        proposal = self.proposals[proposal_id]
        if time.time() > proposal["expiration_time"]:
            proposal["status"] = "expired"
            print(f"Proposal {proposal_id} has expired.")
            return
        if vote_type not in proposal["votes"]:
            print("Invalid vote type. Use 'yes' or 'no'.")
            return
        proposal["votes"][vote_type] += 1
        print(f"Vote '{vote_type}' recorded for proposal {proposal_id}.")

    def check_results(self, proposal_id):
        """Check the results of a proposal."""
        if proposal_id not in self.proposals:
            print(f"Proposal {proposal_id} does not exist.")
            return
        proposal = self.proposals[proposal_id]
        return {
            "votes": proposal["votes"],
            "status": proposal["status"],
        }