class TaskPlanner:
    """
    Converts intent into executable steps.
    """

    def plan(self, intent: dict) -> list[dict]:
        intent_type = intent.get("type")

        # Direct execution
        if intent_type in {
            "cli", "wifi", "app", "audio",
            "file_read", "file_write"
        }:
            return [intent]

        # Chat / reasoning handled by LLM
        if intent_type == "chat":
            return [{
                "type": "llm",
                "text": intent.get("text")
            }]

        return []
