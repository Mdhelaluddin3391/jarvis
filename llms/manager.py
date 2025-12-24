# llms/manager.py

from llms.local.llama_cpp import LlamaCppLLM
from llms.server.openai_api import OpenAILLM

class LLMManager:
    """
    Central LLM holder.
    NO other module should import this indirectly.
    """

    def __init__(self):
        self.local = LlamaCppLLM()
        self.server = OpenAILLM()

    def status(self) -> dict:
        return {
            "local": self.local.name,
            "server": self.server.name
        }
