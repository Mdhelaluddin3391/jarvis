from agents.base.agent import Agent
from agents.base.result import AgentResult

class PythonAgent(Agent):
    name = "python"

    def can_handle(self, task: dict) -> bool:
        return task.get("type") == "python"

    def execute(self, task: dict) -> AgentResult:
        code = task.get("code")
        if not code:
            return AgentResult(False, error="No Python code")

        local_env = {}
        try:
            exec(code, {}, local_env)
            return AgentResult(True, output=str(local_env))
        except Exception as e:
            return AgentResult(False, error=str(e))
