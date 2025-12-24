from orchestrator.intent_parser import IntentParser
from orchestrator.task_planner import TaskPlanner
from orchestrator.router import Router
from orchestrator.execution_manager import ExecutionManager
from orchestrator.feedback_loop import FeedbackLoop
from orchestrator.state import SystemState

class Brain:
    """
    Central decision maker.
    """

    def __init__(self, agent_registry, llm_manager):
        self.intent_parser = IntentParser()
        self.planner = TaskPlanner()
        self.router = Router()
        self.executor = ExecutionManager(agent_registry, llm_manager)
        self.feedback = FeedbackLoop()
        self.state = SystemState()

    def handle(self, user_input: str) -> str:
        # 1. Parse intent
        intent = self.intent_parser.parse(user_input)

        # 2. Plan steps
        steps = self.planner.plan(intent)

        final_output = ""

        for step in steps:
            # 3. Decide route
            route = self.router.route(step)
            step["_route"] = route

            # 4. Execute
            result = self.executor.execute(step)

            # 5. Update state
            self.state.last_task = step
            self.state.last_result = result

            if not result.get("success"):
                self.state.errors += 1
                return f"❌ Error: {result.get('error')}"

            final_output += result.get("output", "") + "\n"

            # 6. Feedback hook
            self.feedback.on_result(intent, result)

        return final_output.strip()
