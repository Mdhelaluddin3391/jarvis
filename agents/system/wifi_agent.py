import os
from agents.base.agent import Agent
from agents.base.result import AgentResult

class WifiAgent(Agent):
    name = "wifi"

    def can_handle(self, task: dict) -> bool:
        return task.get("type") == "wifi"

    def execute(self, task: dict) -> AgentResult:
        action = task.get("action")
        if action == "on":
            os.system("nmcli radio wifi on")
            return AgentResult(True, output="WiFi ON")
        if action == "off":
            os.system("nmcli radio wifi off")
            return AgentResult(True, output="WiFi OFF")
        return AgentResult(False, error="Invalid WiFi action")
