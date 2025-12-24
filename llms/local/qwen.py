from llms.base.llm import BaseLLM

class QwenLLM(BaseLLM):
    name = "qwen"

    def generate(self, prompt: str) -> str:
        return f"[Qwen Local] {prompt}"
