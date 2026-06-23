import pyaudio

#Configuration
InputName = "Microphone (PD100X Podcast Microphone)" 
OutputName = "Voicemeeter AUX Input (VB-Audio Voicemeeter VAIO)"#"CABLE Input (VB-Audio Virtual Cable)"

#As of right now this will only work on Windows.
#AUDIO_API = 1 #MME
AUDIO_API = 2 #WASAPI

RATE = 48000
CHUNK = 4096
CHANNELS = 1
FORMAT = pyaudio.paInt16