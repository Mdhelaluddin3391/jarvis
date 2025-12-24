import os
from agents.base.agent import Agent
from agents.base.result import AgentResult

class PowerAgent(Agent):
    name = "power"

    def can_handle(self, task: dict) -> bool:
        return task.get("type") == "power"

    def execute(self, task: dict) -> AgentResult:
        action = task.get("action")
        if action == "shutdown":
            os.system("shutdown now")
            return AgentResult(True, output="Shutting down")
        return AgentResult(False, error="Unsupported power action")
