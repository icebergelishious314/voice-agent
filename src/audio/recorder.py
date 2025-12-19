def record_wav(filename, seconds, samplerate=16000):
    import sounddevice as sd
    from scipy.io.wavfile import write

    audio = sd.rec(
        int(seconds * samplerate),
        samplerate=samplerate,
        channels=1,
        dtype="int16"
    )
    sd.wait()
    write(filename, samplerate, audio)
