#Dependencies
from pydantic import BaseModel 
#-----------[ Audio Settings ]-----------
class Settings(BaseModel):
    # Device Names
    InputName: str = "Microphone (PD100X Podcast Microphone)" 
    OutputName: str = "CABLE Input (VB-Audio Virtual Cable)" #"Voicemeeter AUX Input (VB-Audio Voicemeeter VAIO)"

    # *** As of right now this will only work on Windows. ***

    #Audio Api
    Audio_API: str = "WASAPI" 

    #Bitrate
    rate: int = 48000

    #Sample Size or Chunk
    chunk: int = 2048

    #Number of channels
    in_channels: int = 1
    out_channels: int = 2

    #Audio Format

    #-----------[ App Settings ]-----------
    title: str = "Soundboard"
    window_size: str = "1000x800"


    #-----------[ Button Settings ]-----------


    #-----------[ Settings Window Settings ]-----------
    settings_title: str = "Settings"
    settings_size: str = "600x600+400+400"

settings = Settings()