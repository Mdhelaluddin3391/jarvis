class ApprovalManager:
    """
    Handles approval for high-risk actions.
    """

    def request(self, task: dict) -> bool:
        print("Approval required for task:")
        print(task)

        response = input("Approve? (yes/no): ").strip().lower()
        return response == "yes"
