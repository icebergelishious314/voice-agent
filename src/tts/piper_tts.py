import subprocess

class PiperTTS:
    def __init__(self, model_path):
        self.model_path = model_path

    def speak(self, text, output_file="tts_output.wav"):
        proc = subprocess.Popen(
            [
                "piper",
                "--model", self.model_path,
                "--output_file", output_file
            ],
            stdin=subprocess.PIPE
        )
        proc.stdin.write(text.encode("utf-8"))
        proc.stdin.close()
        proc.wait()
