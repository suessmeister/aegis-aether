import requests
from dotenv import load_dotenv
import os

# Load environment variables from a .env file
load_dotenv()


class LLMClient:
    """A universal client for interacting with various LLM providers."""

    def __init__(self, provider, base_url):
        self.provider = provider
        self.base_url = base_url

    def send_request(self, prompt, model="gpt-4o-mini", temperature=0.7):
        """Send a request to the configured LLM provider."""

        # Call the appropriate API based on the provider
        if self.provider == "openai":     
            api_key = os.environ.get("OPENAI_API_KEY")
            print(api_key)   
            response = requests.post(
                            f"{self.base_url}/v1/chat/completions",
                            headers={"Authorization": f"Bearer {api_key}"},
                            json={
                                "model": model,     
                                "messages": [{"role": "system", "content": prompt}],
                                "temperature": temperature,
                            },
                        )

            # Handle response
            if response.status_code != 200:
                raise Exception(f"API Error: {response.status_code} - {response.text}")

            return response.json()["choices"][0]["message"]["content"]

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
