import os
from agents.base.agent import Agent
from agents.base.result import AgentResult

class AudioAgent(Agent):
    name = "audio"

    def can_handle(self, task: dict) -> bool:
        return task.get("type") == "audio"

    def execute(self, task: dict) -> AgentResult:
        level = task.get("volume")
        if level is None:
            return AgentResult(False, error="No volume provided")
        os.system(f"amixer set Master {level}%")
        return AgentResult(True, output=f"Volume set to {level}%")
