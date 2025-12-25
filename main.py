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
from perception.audio.audio_stream import AudioStream

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

    # Initialize Core Systems
    agent_registry = bootstrap_agents()
    llm_manager = LLMManager()
    memory = MemoryManager()
    
    # Initialize Audio
    audio_stream = AudioStream()

    # Learning & Permissions
    interaction_logger = InteractionLogger()
    risk_analyzer = RiskAnalyzer()
    approval_manager = ApprovalManager()
    brain = Brain(agent_registry, llm_manager)

    print("✅ Systems online.")
    
    # ---- MODE SELECTION ----
    mode = input("Select Mode (text/voice): ").strip().lower()
    voice_mode = (mode == "voice")
    
    if voice_mode:
        print("🎙️  VOICE MODE ACTIVE. Say 'Jarvis' to start.")
        audio_stream.start()
    else:
        print("⌨️  TEXT MODE ACTIVE.")

    # ---- Main loop ----
    while True:
        try:
            user_input = ""
            
            # 1. INPUT PHASE
            if voice_mode:
                # Blocks until wake word + command received
                user_input = audio_stream.listen()
            else:
                user_input = input("You > ").strip()
            
            if not user_input:
                continue

            if user_input.lower() in {"exit", "quit"}:
                print("👋 Shutting down Jarvis.")
                break

            # ... (Rest of the loop logic remains the same: memory, risk, brain, logs) ...
            
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

            # ---- Brain handles input ----
            response = brain.handle(user_input)
            print("Jarvis >", response)

            # ---- Short-term memory ----
            memory.conversation.add("jarvis", response)
            interaction_logger.log(user_input, response)

        except KeyboardInterrupt:
            print("\n👋 Interrupted. Exiting safely.")
            if voice_mode:
                audio_stream.stop()
            break

        except Exception as e:
            print("❌ Unexpected error:", str(e))
            if voice_mode:
                 # Prevent infinite error loops in voice mode
                 audio_stream.stop()
                 break

if __name__ == "__main__":
    main()