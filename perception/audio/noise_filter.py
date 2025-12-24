# perception/audio/noise_filter.py
import numpy as np


class NoiseFilter:
    def __init__(self, threshold=0.01):
        self.threshold = threshold

    def filter(self, audio: np.ndarray):
        rms = np.sqrt(np.mean(audio ** 2))
        if rms < self.threshold:
            return None
        return audio
