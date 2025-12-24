# perception/audio/vad.py
import webrtcvad
import numpy as np


class VoiceActivityDetector:
    def __init__(self, mode=2, sample_rate=16000):
        self.vad = webrtcvad.Vad(mode)
        self.sample_rate = sample_rate

    def is_speech(self, audio: np.ndarray):
        pcm = (audio * 32767).astype(np.int16).tobytes()
        return self.vad.is_speech(pcm, self.sample_rate)
