from datetime import datetime

class EventLog:
    def __init__(self):
        self.events = []

    def record(self, description: str):
        self.events.append({
            "type": "event",
            "description": description,
            "time": datetime.utcnow().isoformat()
        })

    def list(self):
        return list(self.events)
