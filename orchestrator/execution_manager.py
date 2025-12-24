from agents.registry import AgentRegistry

class ExecutionManager:
    """
    Executes planned steps.
    """

    def __init__(self, agent_registry: AgentRegistry, llm_manager):
        self.agents = agent_registry
        self.llms = llm_manager

    def execute(self, step: dict) -> dict:
        route = step.get("_route")

        if route == "agent":
            agent = self.agents.find_agent(step)
            if not agent:
                return {"success": False, "error": "No agent found"}
            result = agent.execute(step)
            return result.__dict__

        if route == "local_llm":
            return {
                "success": True,
                "output": self.llms.local.generate(step["text"])
            }

        if route == "server_llm":
            return {
                "success": True,
                "output": self.llms.server.generate(step["text"])
            }

        return {"success": False, "error": "Invalid route"}
