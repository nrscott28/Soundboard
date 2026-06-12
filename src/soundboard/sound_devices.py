#Dependencies
import pyaudio

#Get device index given the name of the device
def getDeviceIndexByName(pa, name):
    pos = -1

    for i in range(pa.get_device_count()):
        info = pa.get_device_info_by_index(i)
        if (info.get('name').lower() == name.lower()) and (info.get('hostApi') == AUDIO_API):
            printDeviceInfo(pa, i)
            pos = i
    return pos

#Print device info given index
def printDeviceInfo(pyaudio_instance ,index):
    info = pyaudio_instance.get_device_info_by_index(index)
        
    print(f"Index: {info.get('index')}")
    print(f"Name: {info.get('name')}")
    print(f"API: {info.get('hostApi')}")
    print(f"Input Channels: {info.get('maxInputChannels')}")
    print(f"Output Channels: {info.get('maxOutputChannels')}")
    print(f"Sample Rate: {info.get('defaultSampleRate')} \n")


#Prints out all audio device information to terminal using printDeviceInfo to display
def showAllDeviceInfo(pyaudio_instance):
    for i in range(pyaudio_instance.get_device_count()):
        printDeviceInfo(pyaudio_instance, i)
        

def openInputStream(FORMAT, CHANNELS):
    in_stream = p.open(format=FORMAT, 
        channels=CHANNELS, 
        rate=RATE, 
        input=True, 
        input_device_index=InputIndex, 
        frames_per_buffer=CHUNK)

def openOutputStream(Format, Channels, Rate, Output):
    out_stream = p.open(format=FORMAT, 
        channels=CHANNELS, 
        rate=RATE, output=True, 
        output_device_index=OutputIndex, 
        frames_per_buffer=CHUNK)