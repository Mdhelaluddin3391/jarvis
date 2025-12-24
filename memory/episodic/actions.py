from datetime import datetime

class ActionLog:
    def __init__(self):
        self.actions = []

    def record(self, agent: str, task: dict):
        self.actions.append({
            "agent": agent,
            "task": task,
            "time": datetime.utcnow().isoformat()
        })

    def list(self):
        return list(self.actions)
