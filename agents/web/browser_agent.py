import webbrowser
from agents.base.agent import Agent
from agents.base.result import AgentResult

class BrowserAgent(Agent):
    name = "browser"

    def can_handle(self, task: dict) -> bool:
        return task.get("type") == "open_url"

    def execute(self, task: dict) -> AgentResult:
        url = task.get("url")
        if not url:
            return AgentResult(False, error="No URL")

        webbrowser.open(url)
        return AgentResult(True, output=f"Opened {url}")
