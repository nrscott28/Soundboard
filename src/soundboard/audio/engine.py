#Dependencies
import sounddevice as sd                # Manages sound devices, playback, and streams
import soundfile as sf                  # Manages sound files
import threading                        # Creates threads for each sound played
import os                               # Used to check if file exists

#Modules
from config import settings

class AudioEngine: 
    #Initialize Audio Engine
    def __init__(self):
        sd.default.device = settings.OutputName
        self._device_index = None # None -> system default


    #Get device index given the name of the device and the desired audio API
    def getDeviceIndex(self, device_name, selected_api):
        index = -1
        target_api = None
        
        #Get hostapi index
        for api in sd.query_hostapis():
            if selected_api.lower() == api["name"].lower():
                target_api = api["index"]
        
        if target_api is None: 
            print(f"Error: Host API {selected_api} not found")
            return None

        #Find device with matching hostapi and name
        for idx, dev in enumerate(sd.query_devices()):
            if dev["name"].lower() == device_name.lower() and dev["hostapi"] == target_api:
                return idx
        
        #Will continue if no matching device is found
        print(f"Error: No device found with name {device_name}")
        return None

    #Print device info given index
    def printDeviceInfo(self, index):
        info = sd.query_devices(device=index)
            
        print(f"Device Name: {info['name']}")
        print(f"Max Input Channels: {info['max_input_channels']}")
        print(f"Max Output Channels: {info['max_output_channels']}")
        print(f"Default Sample Rate: {info['default_samplerate']}")


    #Prints out all audio device information to terminal using printDeviceInfo to display
    def showAllDeviceInfo(self):
        devices = []
        for i, dev in enumerate(sd.query_devices()):
            if dev["max_output_channels"] > 0:
                print(f"Index: {i}")
                print(f"Device: {dev}")

    def setOutputDevice(self, index):
        self._device_index = index

    #Creates thread so UI is responsive when play button is clicked
    #  *** MP3 not supported by soundfile ***
    def play(self, filepath: str):
        if not os.path.exists(filepath):
            print(f"File not found: {filepath}")
        return threading.Thread(target=self._play, args=(filepath,), daemon=True).start()

    #Plays the audio
    def _play(self, filepath: str):
        try:
            data, samplerate = sf.read(filepath, dtype="float32")
            
            #Checks number of dimensions, which is the number of channels. Reshapes if it is one channel
            if data.ndim == 1:
                data = data.reshape(-1, 1)
            
            #Use Output Stream instead of play so theres more control over parameters
            with sd.OutputStream(samplerate=samplerate, channels=data.shape[1],
                                device=self._device_index) as stream:
                stream.write(data)  # blocks until done, no sd.wait() needed
        except Exception as e:
            print(f"Audio error playing {filepath}: {e}")


        