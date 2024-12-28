from src.agents.ai_agent import AIAgent

if __name__ == "__main__":
    # Create an AI agent
    agent = AIAgent(agent_id=1, role="data manager", provider="openai", base_url="https://api.openai.com")

    # Upload a file to IPFS
    file_path = "example_data.txt"  # Replace with your file path
    cid = agent.upload_to_ipfs(file_path)
    print(f"Uploaded file CID: {cid}")

    # Download the file back from IPFS
    if cid:
        output_path = "downloaded_example_data.txt"
        agent.download_from_ipfs(cid, output_path)