import webbrowser
from urllib.parse import quote
from agents.base.agent import Agent
from agents.base.result import AgentResult

class SearchAgent(Agent):
    name = "search"

    def can_handle(self, task: dict) -> bool:
        return task.get("type") == "search"

    def execute(self, task: dict) -> AgentResult:
        query = quote(task.get("query", ""))
        url = f"https://www.google.com/search?q={query}"
        webbrowser.open(url)
        return AgentResult(True, output=f"Searching {query}")
