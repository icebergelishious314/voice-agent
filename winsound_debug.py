import winsound
from pathlib import Path

wav = Path("output.wav").resolve()
print("Playing:", wav)

winsound.PlaySound(
    str(wav),
    winsound.SND_FILENAME | winsound.SND_SYNC
)

print("Done")