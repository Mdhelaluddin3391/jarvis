class FaissStore:
    def __init__(self):
        self.vectors = []
        self.payloads = []

    def add(self, vector: list[float], payload: dict):
        self.vectors.append(vector)
        self.payloads.append(payload)

    def search(self, vector: list[float], top_k: int = 5):
        return self.payloads[:top_k]
