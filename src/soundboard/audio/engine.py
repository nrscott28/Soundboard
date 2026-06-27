#Dependencies
import pyaudio 
import wave as wf
#Modules
import config.settings as config

class AudioEngine: 
    #Initialize Audio Engine
    def __init__(self):
        self._pa = pyaudio.PyAudio()
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
    def printDeviceInfo(self, pyaudio_instance ,index):
        info = pyaudio_instance.get_device_info_by_index(index)
            
        print(f"Index: {info.get('index')}")
        print(f"Name: {info.get('name')}")
        print(f"API: {info.get('hostApi')}")
        print(f"Input Channels: {info.get('maxInputChannels')}")
        print(f"Output Channels: {info.get('maxOutputChannels')}")
        print(f"Sample Rate: {info.get('defaultSampleRate')} \n")


    #Prints out all audio device information to terminal using printDeviceInfo to display
    def showAllDeviceInfo(self, pyaudio_instance):
        for i in range(pyaudio_instance.get_device_count()):
            self.printDeviceInfo(pyaudio_instance, i)
            

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
    
    def play(self, file):
        # Read data from the file and play it in chunks
        data = wf.readframes(config.CHUNK)
        while len(data) > 0:
            out_stream.write(data)
            data = wf.readframes(config.CHUNK)
        out_stream.stop_stream()
        out_stream.close()
        p.terminate()
        
        wf.close()