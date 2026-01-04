from pathlib import Path
import winsound

import soundfile as sf
import numpy as np


def add_preroll_silence(in_wav_path, ms=120, out_wav_path=None):
    """
    Create a new WAV with `ms` milliseconds of silence prepended.
    Writes to a new file by default (safer than overwriting).
    Returns the output path (Path).
    """
    in_wav_path = Path(in_wav_path).resolve()

    if out_wav_path is None:
        out_wav_path = in_wav_path.with_name(in_wav_path.stem + "_preroll" + in_wav_path.suffix)
    out_wav_path = Path(out_wav_path).resolve()

    data, sr = sf.read(in_wav_path, always_2d=True)  # shape: (samples, channels)
    n_silence = int(sr * (ms / 1000.0))

    # Match dtype so we don't accidentally change format
    # sf.read returns float64 by default; we’ll write float WAV unless you need PCM16 specifically.
    silence = np.zeros((n_silence, data.shape[1]), dtype=data.dtype)

    padded = np.concatenate([silence, data], axis=0)

    # Write padded file
    sf.write(out_wav_path, padded, sr)

    return out_wav_path


def play_wav(path):
    path = Path(path).resolve()
    print("Playing:", path)

    # Even if sync flags are flaky, this at least gives the device a “lead-in”
    winsound.PlaySound(str(path), winsound.SND_FILENAME)
