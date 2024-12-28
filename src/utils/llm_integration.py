import openai

class LLMIntegration:
    def __init__(self, api_key):
        self.api_key = api_key
        openai.api_key = self.api_key

    def query_gpt(self, prompt, model="gpt-4", max_tokens=100):
        """Query GPT-based models and return the response."""
        try:
            response = openai.ChatCompletion.create(
                model=model,
                messages=[{"role": "user", "content": prompt}],
                max_tokens=max_tokens,
            )
            return response["choices"][0]["message"]["content"].strip()
        except Exception as e:
            print(f"Error querying LLM: {e}")
            return None

# Example usage
if __name__ == "__main__":
    llm = LLMIntegration(api_key="your-openai-api-key")
    response = llm.query_gpt("What is the capital of France?")
    print(f"LLM Response: {response}")