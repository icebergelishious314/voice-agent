import sounddevice as sd

for i, dev in enumerate(sd.query_devices()):
    print(f"{i}: {dev['name']} | in={dev['max_input_channels']} out={dev['max_output_channels']} | default_sr={dev['default_samplerate']}")
