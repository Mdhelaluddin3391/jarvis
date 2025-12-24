from dataclasses import dataclass
from typing import Optional, Dict

@dataclass
class AgentResult:
    success: bool
    output: str = ""
    error: str = ""
    metadata: Optional[Dict] = None
