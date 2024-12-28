from src.agents.ai_agent import AIAgent

if __name__ == "__main__":
    # Create an agent with Solana integration
    solana_agent = AIAgent(agent_id=1, role="blockchain operator", provider="openai", base_url="https://api.openai.com")

    # Check agent's Solana wallet balance
    solana_agent.check_balance()

    # Send SOL to another wallet (replace with a real recipient public key)
    recipient_public_key = "YourRecipientPublicKeyHere"
    solana_agent.send_sol(recipient_pubkey=recipient_public_key, amount=1000000)  # 1 SOL in lamports

    # Deploy a Solana program (smart contract)
    program_path = "path/to/your/solana/program.so"
    solana_agent.deploy_contract(program_path)