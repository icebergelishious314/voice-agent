### Powershell for new PC setup
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
winget install ffmpeg

### In CMD

D:
cd "D:\AI Stuff\Voice Mode Project Too"
pyenv local 3.9.13

to view structure: tree src /F

### In VScode
python -m venv venv
venv\Scripts\activate

### now in venv

pip install openai-whisper
pip install TTS
pip install requests
pip install sounddevice scipy numpy
pip install TTS soundfile
pip install piper-tts
pip install simpleaudio

### Adding files to project folder

create folder "Voice Mode Project/voices"
download voices from here: https://rhasspy.github.io/piper-samples/###en_US-hfc_female-medium ans save in above folder
save the ".onnx" file and ."json" in the voices folder







