#Dependencies
import sounddevice as sd
import soundfile as sf 
import wave

#Modules
import config.settings as config

class AudioEngine: 
    #Initialize Audio Engine
    def __init__(self):
        self._device_index = None # None -> system default


    #Get device index given the name of the device
    def getDeviceIndexByName(self, pa, name):
        pos = -1

        for i in range(pa.get_device_count()):
            info = pa.get_device_info_by_index(i)
            if (info.get('name').lower() == name.lower()) and (info.get('hostApi') == config.AUDIO_API):
                self.printDeviceInfo(pa, i)
                pos = i
        return pos

    #Print device info given index
    def printDeviceInfo(self, index):
        info = sd.query_devices(device=index)
            
        print(f"Device Name: {info['name']}")
        print(f"Max Input Channels: {info['max_input_channels']}")
        print(f"Max Output Channels: {info['max_output_channels']}")
        print(f"Default Sample Rate: {info['default_samplerate']}")


    #Prints out all audio device information to terminal using printDeviceInfo to display
    def showAllDeviceInfo(self, pyaudio_instance):
        for i in range(pyaudio_instance.get_device_count()):
            self.printDeviceInfo(pyaudio_instance, i)


    def play(self, file):
        wf = wave.open(file, 'rb')
        
        # Read data from the file and play it in chunks
        data = wf.readframes(config.CHUNK)
        while len(data) > 0:
            out_stream.write(data)
            data = wf.readframes(config.CHUNK)
        out_stream.stop_stream()
        out_stream.close()
        p.terminate()
        
        wf.close()

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



    #Might not need with sounddevice         
'''
    def openInputStream(self, p):
        in_stream = p.open(format=config.FORMAT, 
            channels= config.IN_CHANNELS, 
            rate=config.RATE, 
            input=True, 
            input_device_index = self.getDeviceIndexByName(p, config.InputName), 
            frames_per_buffer=config.CHUNK)
        return in_stream

    def openOutputStream(self, p):
        out_stream = p.open(format=config.FORMAT, 
            channels=config.OUT_CHANNELS, 
            rate=config.RATE, output=True, 
            output_device_index = self.getDeviceIndexByName(p, config.OutputName), 
            frames_per_buffer=config.CHUNK)
        return out_stream
''' 