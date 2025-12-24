class FactsStore:
    def __init__(self):
        self.facts = set()

    def add(self, fact: str):
        self.facts.add(fact)

    def list(self):
        return list(self.facts)
