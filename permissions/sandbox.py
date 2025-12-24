class Sandbox:
    """
    Sandbox checks before execution.
    """

    @staticmethod
    def validate(task: dict) -> bool:
        # Extendable for file paths, env vars, etc.
        return True
