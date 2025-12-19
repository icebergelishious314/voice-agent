import sounddevice as sd
import numpy as np
from scipy.io.wavfile import write
import whisper

SAMPLE_RATE = 16000
DURATION = 5
AUDIO_FILE = "mic_input.wav"

print("Loading Whisper model...")
model = whisper.load_model("base")  # use "small" later if you want

print("Recording...")
audio = sd.rec(
    int(DURATION * SAMPLE_RATE),
    samplerate=SAMPLE_RATE,
    channels=1,
    dtype="int16"
)
sd.wait()
print("Recording finished.")

write(AUDIO_FILE, SAMPLE_RATE, audio)

print("Transcribing...")
result = model.transcribe(AUDIO_FILE)

print("\n=== TRANSCRIPTION ===")
print(result["text"])
