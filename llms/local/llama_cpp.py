from llms.base.llm import BaseLLM

class LlamaCppLLM(BaseLLM):
    name = "llama_cpp"

    def __init__(self, model_path: str = "models/llama.gguf"):
        self.model_path = model_path
        self._loaded = False

    def _load(self):
        # Placeholder: integrate llama-cpp-python here
        self._loaded = True

    def generate(self, prompt: str) -> str:
        if not self._loaded:
            self._load()

        # MOCK RESPONSE (replace with real llama.cpp inference)
        return f"[Local LLM] Response to: {prompt}"
