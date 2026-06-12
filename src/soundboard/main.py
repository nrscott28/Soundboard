#####
# Title: Soundboard
# Author: Nathan Scott
# Date: 2/28/2026
# Description: Soundboard used with VB-Cable to route soundboard audio through microphone so I dont have to pay for discord soundboard
#####

#Dependencies
import pyaudio
import wave

#Modules
import sound_devices as sd

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

def main():
    #Create Pyaudio instance
    p = pyaudio.PyAudio()
    
    #Get input and output indexes
    InputIndex = sd.getDeviceIndexByName(p, InputName)
    OutputIndex = sd.getDeviceIndexByName(p, OutputName)
    
    wf = wave.open("Soundboard\sounds\wizard.wav", 'rb')

    #Main Pyaudio loop
    '''
    in_stream = p.open(format=FORMAT, 
                       channels=CHANNELS, 
                       rate=RATE, 
                       input=True, 
                       input_device_index=InputIndex, 
                       frames_per_buffer=CHUNK)
    '''
    
    out_stream = p.open(format=FORMAT, 
                        channels=CHANNELS, 
                        rate=RATE, output=True, 
                        output_device_index=OutputIndex, 
                        frames_per_buffer=CHUNK)

    print("Routing active. Press Ctrl+C to stop.")

    #Try Playing mic audio through VB Cable
    '''
    try:
        while True:
            # Read from mic, write to VB-Cable
            out_stream.write(in_stream.read(CHUNK, exception_on_overflow=False))
    except KeyboardInterrupt:
        print("Stopped.")
    finally:
        in_stream.close()
        out_stream.close()
    '''
    # Read data from the file and play it in chunks
    data = wf.readframes(CHUNK)
    while len(data) > 0:
        out_stream.write(data)
        data = wf.readframes(CHUNK)
    out_stream.stop_stream()
    out_stream.close()
    p.terminate()
    
    wf.close()
    
   

     #Get audio information
    '''
    p = pyaudio.PyAudio()

    for i in range(p.get_device_count()):
        info = p.get_device_info_by_index(i)
        print(f"[{i}] {info['name']}")
        print(f"     Default SR: {info['defaultSampleRate']}")
        print(f"     Max Input Ch: {info['maxInputChannels']}")
        print(f"     Max Output Ch: {info['maxOutputChannels']}")

    p.terminate()
    '''
#Runnable Py file
if __name__ == "__main__":
    main()