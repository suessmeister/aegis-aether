import openai
import requests

class OpenAIProvider:
    def __init__(self, api_key):
        openai.api_key = api_key

    def generate_text(self, prompt):
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=100
        )
        return response.choices[0].text.strip()

class OtherLLMProvider:
    def __init__(self, api_key):
        self.api_key = api_key

    def generate_text(self, prompt):
        response = requests.post(
            "https://api.otherllm.com/generate",
            headers={"Authorization": f"Bearer {self.api_key}"},
            json={"prompt": prompt}
        )
        return response.json().get("text", "").strip()

# Example usage
if __name__ == "__main__":
    openai_provider = OpenAIProvider("your-openai-api-key")
    print(openai_provider.generate_text("Hello, how are you?"))

    other_provider = OtherLLMProvider("your-otherllm-api-key")
    print(other_provider.generate_text("Hello, how are you?"))