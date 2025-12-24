class FeedbackLoop:
    """
    Collects execution results.
    """

    def on_result(self, intent: dict, result: dict):
        # For now just return combined data
        return {
            "intent": intent,
            "result": result
        }
