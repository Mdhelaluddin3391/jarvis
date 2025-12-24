class IntentParser:
    """
    Converts raw user input into a normalized intent.
    """

    def parse(self, user_input: str) -> dict:
        text = user_input.strip()

        # CLI shortcut
        if text.startswith("!"):
            return {
                "intent": "cli",
                "type": "cli",
                "command": text[1:]
            }

        # WiFi control
        if "wifi on" in text.lower():
            return {"intent": "wifi", "type": "wifi", "action": "on"}

        if "wifi off" in text.lower():
            return {"intent": "wifi", "type": "wifi", "action": "off"}

        # Open app
        if text.lower().startswith("open "):
            return {
                "intent": "app",
                "type": "app",
                "name": text[5:]
            }

        # Default = chat / reasoning
        return {
            "intent": "chat",
            "type": "chat",
            "text": text
        }
