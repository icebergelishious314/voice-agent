import sounddevice as sd
import soundfile as sf

def play_wav(filename):
    audio, sr = sf.read(filename)
    sd.play(audio, sr)
    sd.wait()
