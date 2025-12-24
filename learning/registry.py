class ModelRegistry:
    def __init__(self):
        self.models = []

    def register(self, name: str, version: str, metrics: dict):
        self.models.append({
            "name": name,
            "version": version,
            "metrics": metrics
        })

    def latest(self):
        return self.models[-1] if self.models else None
