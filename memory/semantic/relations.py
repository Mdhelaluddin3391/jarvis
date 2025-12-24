class RelationStore:
    def __init__(self):
        self.relations = []

    def add(self, source: str, relation: str, target: str):
        self.relations.append({
            "source": source,
            "relation": relation,
            "target": target
        })

    def list(self):
        return list(self.relations)
