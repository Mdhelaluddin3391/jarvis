import json
from datetime import datetime
from pathlib import Path

class AgentLogger:
    def __init__(self, base_dir="learning/datasets/raw"):
        self.path = Path(base_dir) / "agent_actions.jsonl"
        self.path.parent.mkdir(parents=True, exist_ok=True)

    def log(self, agent_name: str, task: dict, result: dict):
        record = {
            "type": "agent_action",
            "agent": agent_name,
            "task": task,
            "result": result,
            "timestamp": datetime.utcnow().isoformat()
        }
        with self.path.open("a") as f:
            f.write(json.dumps(record) + "\n")
