from datetime import datetime

class OutcomeLog:
    def __init__(self):
        self.outcomes = []

    def record(self, success: bool, output: str = "", error: str = ""):
        self.outcomes.append({
            "success": success,
            "output": output,
            "error": error,
            "time": datetime.utcnow().isoformat()
        })

    def list(self):
        return list(self.outcomes)
