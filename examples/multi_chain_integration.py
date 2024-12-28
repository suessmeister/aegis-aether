from src.agents.ai_agent import AIAgent

if __name__ == "__main__":
    # Create an AI agent with Ethereum RPC support
    agent = AIAgent(agent_id=1, role="blockchain operator", provider="openai", base_url="https://api.openai.com", ethereum_rpc_url="https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID")

    # Check Solana balance
    sol_balance = agent.get_sol_balance()
    print(f"Solana Balance: {sol_balance} lamports")

    # Check Ethereum balance
    eth_address = "0xYourEthereumAddressHere"
    eth_balance = agent.get_eth_balance(eth_address)
    print(f"Ethereum Balance: {eth_balance} ETH")