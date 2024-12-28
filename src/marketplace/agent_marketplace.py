class AgentMarketplace:
    def __init__(self):
        self.market = []

    def list_resource(self, agent_id, resource, price):
        """List a resource on the marketplace."""
        self.market.append({"agent_id": agent_id, "resource": resource, "price": price})
        print(f"Agent {agent_id} listed {resource} for {price} credits.")

    def buy_resource(self, buyer_id, resource, max_price):
        """Buy a resource if available and within the budget."""
        for listing in self.market:
            if listing["resource"] == resource and listing["price"] <= max_price:
                print(f"Agent {buyer_id} bought {resource} from Agent {listing['agent_id']} for {listing['price']} credits.")
                self.market.remove(listing)
                return True
        print(f"Agent {buyer_id} could not buy {resource}.")
        return False

# Example usage
if __name__ == "__main__":
    marketplace = AgentMarketplace()
    marketplace.list_resource(1, "Energy", 10)
    marketplace.list_resource(2, "Data", 15)
    marketplace.buy_resource(3, "Energy", 12)
    marketplace.buy_resource(3, "Data", 10)