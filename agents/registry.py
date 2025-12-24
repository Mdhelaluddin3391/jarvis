from typing import List, Dict, Optional
from agents.base.agent import Agent

class AgentRegistry:
    """
    Central registry for all agents.
    Brain will query this to find executor.
    """

    def __init__(self):
        self._agents: List[Agent] = []

    def register(self, agent: Agent):
        self._agents.append(agent)

    def find_agent(self, task: Dict) -> Optional[Agent]:
        for agent in self._agents:
            if agent.can_handle(task):
                return agent
        return None
