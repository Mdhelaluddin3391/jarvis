import json
from datetime import datetime
from pathlib import Path

class LLMLogger:
    def __init__(self, base_dir="learning/datasets/raw"):
        self.path = Path(base_dir) / "llm_calls.jsonl"
        self.path.parent.mkdir(parents=True, exist_ok=True)

    def log(self, llm_name: str, prompt: str, output: str):
        record = {
            "type": "llm_call",
            "llm": llm_name,
            "prompt": prompt,
            "output": output,
            "timestamp": datetime.utcnow().isoformat()
        }
        with self.path.open("a") as f:
            f.write(json.dumps(record) + "\n")
