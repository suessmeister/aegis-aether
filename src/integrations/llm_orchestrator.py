import openai
import requests

class LLMProvider:
    def generate(self, prompt):
        raise NotImplementedError("Providers must implement the generate method.")

class OpenAIProvider(LLMProvider):
    def __init__(self, api_key):
        openai.api_key = api_key

    def generate(self, prompt):
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=100
        )
        return response.choices[0].text.strip()

class OtherProvider(LLMProvider):
    def __init__(self, api_url, api_key):
        self.api_url = api_url
        self.api_key = api_key

    def generate(self, prompt):
        response = requests.post(
            self.api_url,
            headers={"Authorization": f"Bearer {self.api_key}"},
            json={"prompt": prompt}
        )
        return response.json().get("text", "")

class LLMOrchestrator:
    def __init__(self):
        self.providers = {}

    def register_provider(self, name, provider):
        self.providers[name] = provider

    def generate_from_all(self, prompt):
        results = {}
        for name, provider in self.providers.items():
            results[name] = provider.generate(prompt)
        return results

# Example usage
if __name__ == "__main__":
    orchestrator = LLMOrchestrator()
    orchestrator.register_provider("openai", OpenAIProvider("your-openai-api-key"))
    orchestrator.register_provider("other", OtherProvider("https://api.otherllm.com", "your-api-key"))

    prompt = "What is the meaning of life?"
    responses = orchestrator.generate_from_all(prompt)
    for provider, response in responses.items():
        print(f"{provider}: {response}")