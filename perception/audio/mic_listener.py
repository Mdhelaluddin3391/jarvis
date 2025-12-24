# perception/audio/mic_listener.py
import sounddevice as sd
import numpy as np
from queue import Queue


class MicListener:
    def __init__(self, sample_rate=16000, block_size=160):
        self.sample_rate = sample_rate
        self.block_size = block_size
        self.queue = Queue()

    def _callback(self, indata, frames, time, status):
        if status:
            print(status)
        self.queue.put(indata.copy())

    def start(self):
        self.stream = sd.InputStream(
            samplerate=self.sample_rate,
            channels=1,
            blocksize=self.block_size,
            callback=self._callback,
        )
        self.stream.start()

    def read(self):
        return self.queue.get()

    def stop(self):
        self.stream.stop()
        self.stream.close()
