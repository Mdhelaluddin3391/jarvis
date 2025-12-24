# perception/audio/audio_stream.py

import numpy as np
from perception.audio.mic_listener import MicListener
from perception.audio.noise_filter import NoiseFilter
from perception.audio.vad import VoiceActivityDetector
from perception.audio.wake_word import WakeWordDetector


class AudioStream:
    def __init__(self):
        self.mic = MicListener()
        self.noise = NoiseFilter()
        self.vad = VoiceActivityDetector()
        self.wake = WakeWordDetector()
        self.buffer = np.array([], dtype=np.float32)

    def listen_for_wake_word(self):
        print("🎙️ Listening for wake word...")
        self.mic.start()

        while True:
            audio = self.mic.read()

            # flatten + normalize
            audio = audio.flatten().astype(np.float32)

            audio = self.noise.filter(audio)
            if audio is None:
                continue

            if not self.vad.is_speech(audio):
                continue

            # 🔑 BUFFER AUDIO
            self.buffer = np.concatenate([self.buffer, audio])

            # openwakeword needs >= 400 samples (25ms @ 16kHz)
            if len(self.buffer) < 400:
                continue

            if self.wake.detect(self.buffer):
                self.buffer = np.array([], dtype=np.float32)
                return True

            # keep buffer small (avoid memory growth)
            self.buffer = self.buffer[-800:]
