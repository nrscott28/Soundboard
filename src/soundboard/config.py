#Dependencies
import pyaudio

#-----------[ Audio Settings ]-----------
#Device Names
InputName = "Microphone (PD100X Podcast Microphone)" 
OutputName = "Voicemeeter AUX Input (VB-Audio Voicemeeter VAIO)"#"CABLE Input (VB-Audio Virtual Cable)"

#As of right now this will only work on Windows.
#Audio Api
# 1: MME
# 2: WASAPI
AUDIO_API = 2 

#Bitrate
RATE = 48000

#Sample Size or Chunk
CHUNK = 4096

#Number of channels
IN_CHANNELS = 1
OUT_CHANNELS = 1

#Audio Format
FORMAT = pyaudio.paInt16