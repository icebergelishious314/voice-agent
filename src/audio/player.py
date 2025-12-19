import winsound
from pathlib import Path

def play_wav(path):
    path = Path(path).resolve()
    print("Playing:", path)

    winsound.PlaySound(
        str(path),
        winsound.SND_FILENAME   # ← no SND_SYNC
    )
