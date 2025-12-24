import requests
from llms.base.llm import BaseLLM

class CustomServerLLM(BaseLLM):
    name = "custom_server"

    def __init__(self, url: str = "http://localhost:8000/generate"):
        self.url = url

    def generate(self, prompt: str) -> str:
        r = requests.post(self.url, json={"prompt": prompt}, timeout=30)
        r.raise_for_status()
        return r.json().get("text", "")
