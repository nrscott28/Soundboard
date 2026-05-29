#####
# Title: Soundboard
# Author: Nathan Scott
# Date: 2/28/2026
# Description: Soundboard used with VB-Cable to route soundboard audio through microphone so I dont have to pay for discord soundboard
#####

import pyaudio

#Configuration
InputName = "Microphone (PD100X Podcast Microphone)" 
OutputName = "CABLE Input (VB-Audio Virtual Cable)"

#As of right now this will only work on Windows.
#AUDIO_API = 1 #MME
AUDIO_API = 1 #WASAPI

RATE = 48000
CHUNK = 1024
CHANNELS = 1
FORMAT = pyaudio.paInt16

def main():
    
    #Get input and output indexes
    
    InputIndex = getDeviceIndexByName(InputName)
    OutputIndex = getDeviceIndexByName(OutputName)
    

    '''
    print(f"Mic: {InputName} | Position: {InputIndex}")
    print(f"Mic: {OutputName} | Position: {OutputIndex}")
    '''

    #Main Pyaudio loop
    p = pyaudio.PyAudio()

    in_stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, input_device_index=InputIndex, frames_per_buffer=CHUNK)
    out_stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, output=True, output_device_index=OutputIndex, frames_per_buffer=CHUNK)

    print("Routing active. Press Ctrl+C to stop.")

    #Try Playing mic audio through VB Cable
    try:
        while True:
            # Read from mic, write to VB-Cable
            out_stream.write(in_stream.read(CHUNK))
    except KeyboardInterrupt:
        print("Stopped.")
    finally:
        in_stream.close()
    out_stream.close()
    p.terminate()


#Get device index given the name of the device
def getDeviceIndexByName(name):
    pa = pyaudio.PyAudio()
    pos = -1

    for i in range(pa.get_device_count()):
        info = pa.get_device_info_by_index(i)
        if (info.get('name').lower() == name.lower()) and (info.get('hostApi') == AUDIO_API):
            print(f"{i} index with {info.get('hostApi')} api index")
            pos = i

    #Terminates instance of PyAudio
    pa.terminate()
    return pos


if __name__ == "__main__":
    main()