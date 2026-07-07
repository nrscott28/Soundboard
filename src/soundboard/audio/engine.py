#Dependencies
import sounddevice as sd
import soundfile as sf 
import threading

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
        devices = []
        for i, dev in enumerate(sd.query_devices()):
            if dev["max_output_channels"] > 0:
                devices.append({"index": i, "name": dev["name"]})
        print(devices)


    #Creates thread so UI is responsive when play button is clicked
    def play(self, filepath: str):
        threading.Thread(target=self._play, args=(filepath,), daemon=True).start()

    #Plays the audio
    def _play(self, filepath: str):
        data, samplerate = sf.read(filepath, dtype="int16")
        sd.play(data, samplerate, device=self._device_index)