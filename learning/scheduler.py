class LearningScheduler:
    """
    Decides WHEN training should happen.
    """

    def should_train(self, dataset_size: int) -> bool:
        return dataset_size >= 1000  # safe threshold

    def next_job(self):
        return "finetune"
