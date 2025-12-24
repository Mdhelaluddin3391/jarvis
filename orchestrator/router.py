class Router:
    """
    Decides execution path.
    """

    def route(self, step: dict) -> str:
        step_type = step.get("type")

        # Agents handle these
        if step_type in {
            "cli", "wifi", "app", "audio",
            "file_read", "file_write"
        }:
            return "agent"

        # LLM reasoning
        if step_type == "llm":
            text = step.get("text", "")
            # Simple heuristic (can be replaced later)
            if len(text) > 120:
                return "server_llm"
            return "local_llm"

        return "unknown"
