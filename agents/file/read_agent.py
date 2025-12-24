from agents.base.agent import Agent
from agents.base.result import AgentResult

class FileReadAgent(Agent):
    name = "file_read"

    def can_handle(self, task: dict) -> bool:
        return task.get("type") == "file_read"

    def execute(self, task: dict) -> AgentResult:
        path = task.get("path")
        try:
            with open(path, "r") as f:
                return AgentResult(True, output=f.read())
        except Exception as e:
            return AgentResult(False, error=str(e))
