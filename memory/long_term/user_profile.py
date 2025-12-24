class UserProfile:
    def __init__(self):
        self.profile = {
            "name": None,
            "language": "en",
            "timezone": None
        }

    def update(self, **kwargs):
        self.profile.update(kwargs)

    def get(self) -> dict:
        return dict(self.profile)
