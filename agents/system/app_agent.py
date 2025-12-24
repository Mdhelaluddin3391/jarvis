import subprocess
from agents.base.agent import Agent
from agents.base.result import AgentResult

class AppAgent(Agent):
    name = "app"

    def can_handle(self, task: dict) -> bool:
        return task.get("type") == "app"

    def execute(self, task: dict) -> AgentResult:
        app = task.get("name")
        if not app:
            return AgentResult(False, error="No app name")
        subprocess.Popen(app, shell=True)
        return AgentResult(True, output=f"Opened {app}")
