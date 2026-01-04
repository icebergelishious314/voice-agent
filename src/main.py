print("MAIN.PY STARTED")

import sys
import json
import time
import requests
from pathlib import Path
sys.path.append(str(Path(__file__).parent))

from config import *
from audio.recorder import record_wav
from audio.player import play_wav
from stt.whisper_stt import WhisperSTT
from tts.piper_tts import PiperTTS
from tts.sanitize import sanitize_for_tts
from llm.ollama_client import ollama_respond


INPUT_WAV = "input.wav"
OUTPUT_WAV = "output.wav"

OLLAMA_MODEL = "qwen2.5-abliterate:latest"

# Init STT / TTS (ONCE)
stt = WhisperSTT(WHISPER_MODEL)
tts = PiperTTS(PIPER_MODEL_PATH)

# Conversation memory
messages = [
    {"role": "system", "content": "You are a helpful voice assistant. Keep your responses short."}
]

print("🎧 Voice assistant ready. Say 'exit' or 'quit' to stop.")

while True:
    print("\n🎙️ Speak now...")
    record_wav(INPUT_WAV)

    # Speech → Text
    user_text = stt.transcribe(INPUT_WAV)
    print("🗣️ You said:", user_text)

    # Handle silence / noise
    if not user_text or not user_text.strip():
        print("⚠️ No speech detected, listening again...")
        continue

    # Exit command
    if user_text.lower().strip() in ("exit", "quit", "stop"):
        print("👋 Exiting voice assistant.")
        break

    messages.append({"role": "user", "content": user_text})

    # LLM call
    try:
        assistant_text = ollama_respond(OLLAMA_MODEL, messages)
    except Exception as e:
        print("❌ LLM error:", e)
        continue

    print("🤖 Assistant:", assistant_text)
    clean_text = sanitize_for_tts(assistant_text)

    # Text → Speech
    tts.speak(clean_text, OUTPUT_WAV)
    time.sleep(0.1)
    play_wav(OUTPUT_WAV)

    messages.append({"role": "assistant", "content": assistant_text})

    # Optional: trim memory to prevent context explosion
    MAX_TURNS = 10
    if len(messages) > 2 + MAX_TURNS * 2:
        messages = messages[:2] + messages[-MAX_TURNS * 2:]
