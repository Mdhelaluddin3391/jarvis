from agents.base.agent import Agent
from agents.base.result import AgentResult

class FileWriteAgent(Agent):
    name = "file_write"

    def can_handle(self, task: dict) -> bool:
        return task.get("type") == "file_write"

    def execute(self, task: dict) -> AgentResult:
        path = task.get("path")
        content = task.get("content", "")
        try:
            with open(path, "w") as f:
                f.write(content)
            return AgentResult(True, output="File written")
        except Exception as e:
            return AgentResult(False, error=str(e))
