import subprocess
from agents.base.agent import Agent
from agents.base.result import AgentResult

class BashAgent(Agent):
    name = "bash"

    def can_handle(self, task: dict) -> bool:
        return task.get("type") == "cli"

    def execute(self, task: dict) -> AgentResult:
        command = task.get("command")
        if not command:
            return AgentResult(False, error="No command provided")

        try:
            output = subprocess.check_output(
                command,
                shell=True,
                stderr=subprocess.STDOUT,
                timeout=20,
                text=True
            )
            return AgentResult(True, output=output.strip())
        except subprocess.CalledProcessError as e:
            return AgentResult(False, error=e.output)
