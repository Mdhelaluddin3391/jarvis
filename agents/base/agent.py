from abc import ABC, abstractmethod
from typing import Dict

class Agent(ABC):
    """
    Base class for all agents.
    Agents are the ONLY layer allowed to touch OS / Web / Hardware.
    """

    name: str = "base"

    @abstractmethod
    def can_handle(self, task: Dict) -> bool:
        """Return True if this agent can handle the task"""
        pass

    @abstractmethod
    def execute(self, task: Dict) -> Dict:
        """Execute the task and return AgentResult-like dict"""
        pass
