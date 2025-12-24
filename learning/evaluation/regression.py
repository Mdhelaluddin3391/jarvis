class RegressionEvaluator:
    def check(self, metrics: dict) -> bool:
        return metrics.get("accuracy", 0) > 0.75
