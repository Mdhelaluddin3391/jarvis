class ChromaStore:
    def __init__(self):
        self.items = []

    def add(self, embedding: list[float], metadata: dict):
        self.items.append((embedding, metadata))

    def query(self, embedding: list[float], limit: int = 5):
        return self.items[:limit]
