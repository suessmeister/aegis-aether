import requests

class LLMClient:
    """A universal client for interacting with various LLM providers."""

    def __init__(self, provider, base_url):
        self.provider = provider
        self.base_url = base_url

    def send_request(self, prompt, model="gpt-4", temperature=0.7):
        """Send a request to the configured LLM provider."""
        if self.provider == "openai":
            # Call OpenAI API
            response = requests.post(
                f"{self.base_url}/v1/completions",
                headers={"Authorization": f"Bearer YOUR_API_KEY"},
                json={"model": model, "prompt": prompt, "temperature": temperature},
            )
            return response.json()["choices"][0]["text"]

        elif self.provider == "ollama":
            # Call Ollama API for local LLaMA model
            response = requests.post(
                f"{self.base_url}/api/generate",
                json={"model": model, "prompt": prompt},
            )
            return response.json()["response"]

        elif self.provider == "anthropic":
            # Call Anthropic's API
            response = requests.post(
                f"{self.base_url}/v1/complete",
                headers={"Authorization": f"Bearer YOUR_API_KEY"},
                json={"model": model, "prompt": prompt, "temperature": temperature},
            )
            return response.json()["completion"]

        else:
            raise ValueError(f"Unknown provider: {self.provider}")