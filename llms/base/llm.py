from abc import ABC, abstractmethod

class BaseLLM(ABC):
    """
    All LLMs (local or server) must implement this.
    """

    name: str = "base"

    @abstractmethod
    def generate(self, prompt: str) -> str:
        pass
