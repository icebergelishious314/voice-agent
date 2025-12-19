import sounddevice as sd
import numpy as np
from scipy.io.wavfile import write

SAMPLE_RATE = 16000   # Whisper expects 16kHz
DURATION = 5          # seconds
OUTPUT_FILE = "mic_input.wav"

print("Recording...")
audio = sd.rec(
    int(DURATION * SAMPLE_RATE),
    samplerate=SAMPLE_RATE,
    channels=1,
    dtype="int16"
)
sd.wait()
print("Recording finished.")

write(OUTPUT_FILE, SAMPLE_RATE, audio)
print(f"Saved to {OUTPUT_FILE}")
