import subprocess

text = "There once was a code in my hand, To run TTS on local land. With pipes and command line, Voices spoke with a chime, And errors danced like a band!"

process = subprocess.Popen(
    [
        "piper",
        "--model", "voices/en_US-hfc_female-medium.onnx",
        "--output_file", "piper_output.wav"
    ],
    stdin=subprocess.PIPE
)

process.stdin.write(text.encode("utf-8"))
process.stdin.close()
process.wait()
