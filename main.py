# main.py
import sys
from datetime import datetime

# ---- Core Systems ----
from orchestrator.brain import Brain
from agents.registry import AgentRegistry

# ---- Agents ----
from agents.cli.bash_agent import BashAgent
from agents.cli.python_agent import PythonAgent
from agents.file.read_agent import FileReadAgent
from agents.file.write_agent import FileWriteAgent
from agents.system.wifi_agent import WifiAgent
from agents.system.audio_agent import AudioAgent
from agents.system.app_agent import AppAgent
from agents.web.browser_agent import BrowserAgent
from agents.web.search_agent import SearchAgent

# ---- LLM Runtime ----
from llms.manager import LLMManager

# ---- Memory ----
from memory.manager import MemoryManager

# ---- Learning (logging only) ----
from learning.collector.interaction_logger import InteractionLogger
from learning.collector.agent_logger import AgentLogger
from learning.collector.llm_logger import LLMLogger

# ---- Permissions ----
from permissions.risk_analyzer import RiskAnalyzer
from permissions.approvals import ApprovalManager
from permissions.sandbox import Sandbox


def bootstrap_agents() -> AgentRegistry:
    """Register all agents here"""
    registry = AgentRegistry()

    # CLI
    registry.register(BashAgent())
    registry.register(PythonAgent())

    # File
    registry.register(FileReadAgent())
    registry.register(FileWriteAgent())

    # System
    registry.register(WifiAgent())
    registry.register(AudioAgent())
    registry.register(AppAgent())

    # Web
    registry.register(BrowserAgent())
    registry.register(SearchAgent())

    return registry


def main():
    print("🤖 JARVIS v1 booting...")
    print("🕒", datetime.now().isoformat())
    print("-" * 50)

    # ---- Initialize subsystems ----
    agent_registry = bootstrap_agents()
    llm_manager = LLMManager()
    memory = MemoryManager()

    # Learning loggers (observe-only)
    interaction_logger = InteractionLogger()
    agent_logger = AgentLogger()
    llm_logger = LLMLogger()

    # Permissions
    risk_analyzer = RiskAnalyzer()
    approval_manager = ApprovalManager()

    # Brain
    brain = Brain(agent_registry, llm_manager)

    print("✅ Systems online.")
    print("💡 Tips:")
    print("  • CLI command: !ls  |  !pwd")
    print("  • Open app: open firefox")
    print("  • WiFi: wifi on / wifi off")
    print("  • Exit: exit / quit")
    print("-" * 50)

    # ---- Main loop ----
    while True:
        try:
            user_input = input("You > ").strip()
            if not user_input:
                continue

            if user_input.lower() in {"exit", "quit"}:
                print("👋 Shutting down Jarvis.")
                break

            # ---- Short-term memory ----
            memory.conversation.add("user", user_input)

            # ---- Risk analysis (pre-check) ----
            risk = risk_analyzer.analyze({"text": user_input})
            if risk == "critical":
                print("❌ BLOCKED: Critical risk detected.")
                continue

            if risk == "high":
                approved = approval_manager.request({"text": user_input})
                if not approved:
                    print("⛔ Action rejected by user.")
                    continue

            # ---- Sandbox check ----
            if not Sandbox.validate({"text": user_input}):
                print("❌ Sandbox validation failed.")
                continue

            # ---- Brain handles input ----
            response = brain.handle(user_input)

            # ---- Output ----
            print("Jarvis >", response)

            # ---- Short-term memory ----
            memory.conversation.add("jarvis", response)

            # ---- Learning logs (observe only) ----
            interaction_logger.log(user_input, response)

        except KeyboardInterrupt:
            print("\n👋 Interrupted. Exiting safely.")
            break

        except Exception as e:
            print("❌ Unexpected error:", str(e))


if __name__ == "__main__":
    main()
