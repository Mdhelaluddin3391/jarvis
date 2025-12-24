class Preferences:
    def __init__(self):
        self.prefs = {}

    def set(self, key: str, value):
        self.prefs[key] = value

    def get(self, key: str, default=None):
        return self.prefs.get(key, default)

    def all(self) -> dict:
        return dict(self.prefs)
