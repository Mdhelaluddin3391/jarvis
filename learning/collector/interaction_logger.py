import json
from datetime import datetime
from pathlib import Path

class InteractionLogger:
    def __init__(self, base_dir="learning/datasets/raw"):
        self.path = Path(base_dir) / "interactions.jsonl"
        self.path.parent.mkdir(parents=True, exist_ok=True)

    def log(self, user_input: str, response: str):
        record = {
            "type": "interaction",
            "user_input": user_input,
            "response": response,
            "timestamp": datetime.utcnow().isoformat()
        }
        with self.path.open("a") as f:
            f.write(json.dumps(record) + "\n")
