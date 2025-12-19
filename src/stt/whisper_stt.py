import whisper

class WhisperSTT:
    def __init__(self, model_name="base"):
        self.model = whisper.load_model(model_name)

    def transcribe(self, wav_file):
        result = self.model.transcribe(wav_file)
        return result["text"].strip()

