from src.agents.ai_agent import AIAgent

if __name__ == "__main__":
    # Create a multi-modal agent
    multi_agent = AIAgent(agent_id=1, role="multi-modal processor", provider="openai", base_url="https://api.openai.com")

    # Process text task
    multi_agent.execute_text_task("Describe the importance of decentralized AI.")

    # Process image task
    image_path = "sample_image.jpg"
    prompts = ["a beautiful sunset", "a crowded city"]
    multi_agent.execute_image_task(image_path, prompts)

    # Process audio task (placeholder)
    multi_agent.execute_audio_task("sample_audio.wav")