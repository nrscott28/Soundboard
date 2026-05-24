import pyaudio

def main(): 
    deviceName = "CABLE Input (VB-Audio Virtual C"
    pos = getDeviceIndexByName(deviceName)

    #Initialize pyaudio
    #p = pyaudio.PyAudio()

    print(f"Name: {deviceName} | Position: {pos}")


#Get device index given the name of the device
def getDeviceIndexByName(name):
    pa = pyaudio.PyAudio()
    pos = -1

    for i in range(pa.get_device_count()):
        info = pa.get_device_info_by_index(i)
        if info.get('name').lower() == name.lower():
            pos = i

    #Terminates instance of PyAudio
    pa.terminate()
    return pos


if __name__ == "__main__":
    main()