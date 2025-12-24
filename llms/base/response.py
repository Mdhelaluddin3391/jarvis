from dataclasses import dataclass
from typing import Optional, Dict

@dataclass
class LLMResponse:
    text: str
    tokens_used: Optional[int] = None
    metadata: Optional[Dict] = None
