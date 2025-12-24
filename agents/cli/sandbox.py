# Future: restricted execution
class Sandbox:
    ALLOWED_BUILTINS = {"len", "range", "print"}

    @staticmethod
    def is_safe(code: str) -> bool:
        return True  # placeholder (permission layer will control)
