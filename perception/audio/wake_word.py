# perception/audio/wake_word.py

import numpy as np
from openwakeword.model import Model


class WakeWordDetector:
    """
    Stable wake-word detector using OpenWakeWord
    """

    def __init__(self, keyword="jarvis", threshold=0.6):
        self.keyword = keyword
        self.threshold = threshold
        self.model = Model()

        # Required dicts (OpenWakeWord quirk)
        self.thresholds = {self.keyword: self.threshold}
        self.patience = {self.keyword: 3}

    def detect(self, audio: np.ndarray) -> bool:
        if audio is None or len(audio) < 400:
            return False

        pcm16 = (audio * 32767).astype(np.int16)

        # 🔑 IMPORTANT: positional args only
        scores = self.model.predict(
            pcm16,
            16000,
            self.thresholds,
            self.patience
        )

        score = scores.get(self.keyword, 0.0)

        if score >= self.threshold:
            print(f"🔔 Wake word detected: {self.keyword} ({score:.2f})")
            return True

        return False
