from llms.base.llm import BaseLLM

class MistralLLM(BaseLLM):
    name = "mistral"

    def generate(self, prompt: str) -> str:
        return f"[Mistral Local] {prompt}"
