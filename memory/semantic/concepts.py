class ConceptStore:
    def __init__(self):
        self.concepts = {}

    def add(self, name: str, description: str):
        self.concepts[name] = description

    def get(self, name: str):
        return self.concepts.get(name)

    def all(self):
        return dict(self.concepts)
