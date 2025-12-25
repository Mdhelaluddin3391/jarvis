import os
from llms.base.llm import BaseLLM

try:
    from llama_cpp import Llama
    HAS_LLAMA = True
except ImportError:
    HAS_LLAMA = False

class LlamaCppLLM(BaseLLM):
    name = "llama_cpp"

    def __init__(self, model_path: str = "models/llama.gguf"):
        self.model_path = model_path
        self._loaded = False
        self.model = None

    def _load(self):
        if not HAS_LLAMA:
            print("❌ Error: llama-cpp-python not installed.")
            return

        if not os.path.exists(self.model_path):
            print(f"❌ Error: Model not found at {self.model_path}")
            print("Please download a GGUF model (e.g. Mistral or Llama-3) and place it in the models/ folder.")
            return

        print(f"Loading Local LLM from {self.model_path}...")
        # Adjust n_ctx (context window) based on your hardware capabilities
        self.model = Llama(
            model_path=self.model_path, 
            n_ctx=2048, 
            n_threads=4,
            verbose=False
        )
        self._loaded = True

    def generate(self, prompt: str) -> str:
        if not self._loaded:
            self._load()
        
        if not self.model:
            return "Error: Local LLM model failed to load."

        # Perform inference
        # stop=["User:"] prevents the model from hallucinating a conversation
        output = self.model(
            prompt, 
            max_tokens=256, 
            stop=["User:", "\n\n"], 
            echo=False
        )
        
        return output["choices"][0]["text"].strip()