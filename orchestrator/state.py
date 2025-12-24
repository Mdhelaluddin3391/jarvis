from dataclasses import dataclass, field
from typing import Dict, Any

@dataclass
class SystemState:
    """
    Holds global system state.
    This is NOT memory, this is runtime status.
    """
    active_llm: str = "local"
    last_task: Dict[str, Any] = field(default_factory=dict)
    last_result: Dict[str, Any] = field(default_factory=dict)
    errors: int = 0
