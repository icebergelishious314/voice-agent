from config import *
from audio.recorder import record_wav
from audio.player import play_wav
from stt.whisper_stt import WhisperSTT
from tts.piper_tts import PiperTTS

INPUT_WAV = "input.wav"
OUTPUT_WAV = "output.wav"

stt = WhisperSTT(WHISPER_MODEL)
tts = PiperTTS(PIPER_MODEL_PATH)

print("Speak now...")
record_wav(INPUT_WAV, RECORD_SECONDS)

text = stt.transcribe(INPUT_WAV)
print("You said:", text)

if text:
    tts.speak(text, OUTPUT_WAV)
    play_wav(OUTPUT_WAV)
