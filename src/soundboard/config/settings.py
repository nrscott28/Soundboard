#Dependencies

#-----------[ Audio Settings ]-----------
#Device Names
InputName = "Microphone (PD100X Podcast Microphone)" 
OutputName = "CABLE Input (VB-Audio Virtual Cable)" #"Voicemeeter AUX Input (VB-Audio Voicemeeter VAIO)"

#As of right now this will only work on Windows.
#Audio Api
# 1: MME
# 2: WASAPI
AUDIO_API = 2 

#Bitrate
RATE = 48000

#Sample Size or Chunk
CHUNK = 2048

#Number of channels
IN_CHANNELS = 1
OUT_CHANNELS = 2

#Audio Format
#FORMAT = 