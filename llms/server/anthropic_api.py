import os
import requests
from llms.base.llm import BaseLLM

class AnthropicLLM(BaseLLM):
    name = "anthropic"

    def __init__(self):
        self.api_key = os.getenv("ANTHROPIC_API_KEY")
        self.endpoint = "https://api.anthropic.com/v1/messages"

    def generate(self, prompt: str) -> str:
        if not self.api_key:
            return "❌ ANTHROPIC_API_KEY not set"

        headers = {
            "x-api-key": self.api_key,
            "Content-Type": "application/json"
        }

        payload = {
            "model": "claude-3-sonnet-20240229",
            "max_tokens": 512,
            "messages": [{"role": "user", "content": prompt}]
        }

        r = requests.post(self.endpoint, headers=headers, json=payload, timeout=30)
        r.raise_for_status()

        return r.json()["content"][0]["text"]
