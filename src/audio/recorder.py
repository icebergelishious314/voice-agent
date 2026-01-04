def record_wav( filename, samplerate=44100, silence_duration=1.5, max_duration=10.0 ):
    import sounddevice as sd
    import numpy as np
    from scipy.io.wavfile import write
    import time

    block_size = int(samplerate * 0.1)  # 100 ms blocks
    audio_chunks = []

    heard_speech = False
    silence_start_time = None
    start_time = time.time()

    print("🎙️ Calibrating noise floor...")

    # --- Calibrate noise floor (real RMS, normalized) ---
    try:
        with sd.InputStream(
            samplerate=samplerate,
            channels=1,
            dtype="int16",
            blocksize=block_size
        ) as stream:
            print("✅ InputStream opened")

            rms_values = []
            for i in range(5):
                block, _ = stream.read(block_size)
                print(f"Read block {i}")
                block = block.astype(np.float32) / 32768.0
                rms = np.sqrt(np.mean(block ** 2))
                rms_values.append(rms)

    except Exception as e:
        print("❌ Audio input error:", repr(e))
        return

    noise_floor = np.mean(rms_values)
    speech_threshold = max(noise_floor * 3.0, 0.01)

    print(f"🎚️ Noise floor: {noise_floor:.4f}")
    print(f"🎯 Speech threshold: {speech_threshold:.4f}")
    print("🎙️ Recording...")

    # --- Recording loop ---
    with sd.InputStream(
        samplerate=samplerate,
        channels=1,
        dtype="int16",
        blocksize=block_size
    ) as stream:

        while True:
            block, _ = stream.read(block_size)
            audio_chunks.append(block)

            # Normalize to [-1.0, 1.0]
            block_f = block.astype(np.float32) / 32768.0
            rms = np.sqrt(np.mean(block_f ** 2))

            now = time.time()

            # Detect speech
            if rms > speech_threshold:
                if not heard_speech:
                    print("🗣️ Speech detected")
                heard_speech = True
                silence_start_time = None
            else:
                if heard_speech and silence_start_time is None:
                    silence_start_time = now

            # Stop after sustained silence (REAL time)
            if heard_speech and silence_start_time:
                if now - silence_start_time >= silence_duration:
                    print("🛑 Sustained silence, stopping")
                    break

            # Safety cutoff
            if now - start_time >= max_duration:
                print("⏱️ Max duration reached")
                break

    audio = np.concatenate(audio_chunks, axis=0)
    write(filename, samplerate, audio)

    print(f"💾 Saved recording to {filename}")
