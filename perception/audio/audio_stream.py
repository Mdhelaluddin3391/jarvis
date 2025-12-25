# perception/audio/audio_stream.py

import numpy as np
import time
from perception.audio.mic_listener import MicListener
from perception.audio.noise_filter import NoiseFilter
from perception.audio.vad import VoiceActivityDetector
from perception.audio.wake_word import WakeWordDetector

# Try importing Faster Whisper
try:
    from faster_whisper import WhisperModel
    HAS_WHISPER = True
except ImportError:
    HAS_WHISPER = False
    print("⚠️  faster-whisper not installed. Voice recognition will be mocked.")

class AudioStream:
    def __init__(self):
        self.mic = MicListener()
        self.noise = NoiseFilter()
        self.vad = VoiceActivityDetector()
        self.wake = WakeWordDetector()
        
        # Load STT Model
        if HAS_WHISPER:
            print("⏳ Loading Whisper model...")
            self.model = WhisperModel("tiny.en", device="cpu", compute_type="int8")
            print("✅ Whisper model loaded.")
        else:
            self.model = None

    def start(self):
        self.mic.start()

    def stop(self):
        self.mic.stop()

    def listen(self) -> str:
        """
        Main blocking loop
        """
        print("🎙️  Listening for 'Jarvis'...")
        
        # 1. Wait for Wake Word
        # We pass small chunks to detect() which maintains internal state
        while True:
            audio_chunk = self.mic.read()
            audio_chunk = audio_chunk.flatten().astype(np.float32)
            
            # Simple noise gate
            filtered = self.noise.filter(audio_chunk)
            if filtered is None:
                continue

            # Pass ONLY the new chunk to the wake word detector
            # The detector handles buffering internally
            if self.wake.detect(filtered):
                print("🔔 Wake Word Detected! Listening for command...")
                self.wake.model.reset() # Reset state after detection
                break
        
        # 2. Capture Command
        command_audio = []
        silence_frames = 0
        max_silence = 40  # ~2 seconds
        
        print("🔴 Recording command...")
        while True:
            chunk = self.mic.read().flatten().astype(np.float32)
            command_audio.append(chunk)
            
            if self.vad.is_speech(chunk):
                silence_frames = 0
            else:
                silence_frames += 1
                
            # Stop if silence persists or max length reached
            if silence_frames > max_silence: 
                break
            if len(command_audio) > 600: # ~15 seconds max
                break
                
        # 3. Transcribe
        full_audio = np.concatenate(command_audio)
        return self._transcribe(full_audio)

    def _transcribe(self, audio: np.ndarray) -> str:
        if not self.model:
            return "test command"

        print("📝 Transcribing...")
        try:
            segments, info = self.model.transcribe(audio, beam_size=5)
            text = " ".join([segment.text for segment in segments]).strip()
            print(f"🗣️  User: {text}")
            return text
        except Exception as e:
            print(f"❌ Transcription error: {e}")
            return ""