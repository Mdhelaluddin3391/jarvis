import os
import requests
from llms.base.llm import BaseLLM

class OpenAILLM(BaseLLM):
    name = "openai"

    def __init__(self):
        self.api_key = os.getenv("OPENAI_API_KEY")
        self.endpoint = "https://api.openai.com/v1/chat/completions"

    def generate(self, prompt: str) -> str:
        if not self.api_key:
            return " OPENAI_API_KEY not set"

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        payload = {
            "model": "gpt-4o-mini",
            "messages": [{"role": "user", "content": prompt}]
        }

        r = requests.post(self.endpoint, headers=headers, json=payload, timeout=30)
        r.raise_for_status()

        return r.json()["choices"][0]["message"]["content"]
