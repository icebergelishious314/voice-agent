import whisper

print("Loading Whisper model...")
model = whisper.load_model("base")

print("Transcribing audio...")
result = model.transcribe("D:\AI Stuff\Voice Mode Project\\testing123.wav")

print("Transcription:")
print(result["text"])