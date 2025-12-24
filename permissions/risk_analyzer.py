from permissions.policies import PermissionPolicy

class RiskAnalyzer:
    """
    Determines risk level of an action.
    """

    def analyze(self, task: dict) -> str:
        text = (
            task.get("command")
            or task.get("text")
            or ""
        )

        if PermissionPolicy.is_forbidden(text):
            return "critical"

        if PermissionPolicy.is_restricted(text):
            return "high"

        if task.get("type") in PermissionPolicy.SAFE_ACTIONS:
            return "low"

        return "medium"
