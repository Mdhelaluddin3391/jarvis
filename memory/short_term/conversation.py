# memory/short_term/conversation.py

from collections import deque
from typing import List, Dict


class ConversationMemory:
    """
    Short-term conversation buffer.
    """

    def __init__(self, max_turns: int = 10):
        self.buffer = deque(maxlen=max_turns)

    def add(self, role: str, content: str):
        self.buffer.append({
            "role": role,
            "content": content
        })

    def get(self) -> List[Dict]:
        return list(self.buffer)

    def clear(self):
        self.buffer.clear()
