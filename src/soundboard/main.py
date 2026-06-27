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
import config

def main():
    #Create Pyaudio instance
    p = pyaudio.PyAudio()
    
    #create Input and Output streams
    #in_stream = sd.openInputStream(p)
    out_stream = sd.openOutputStream(p)

    #Test audio for output. Emulating pressing a soundboard button
    wf = wave.open("sounds/wizard.wav", 'rb')
    

    print("Routing active. Press Ctrl+C to stop.")

    #Play mic audio through VB Cable
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
    data = wf.readframes(config.CHUNK)
    while len(data) > 0:
        out_stream.write(data)
        data = wf.readframes(config.CHUNK)
    out_stream.stop_stream()
    out_stream.close()
    p.terminate()
    
    wf.close()
    
#Runnable Py file
if __name__ == "__main__":
    main()