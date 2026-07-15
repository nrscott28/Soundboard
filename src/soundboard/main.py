#####
# Title: Soundboard
# Author: Nathan Scott
# Date: 2/28/2026
# Description: Soundboard used with VB-Cable to route soundboard audio through microphone so I dont have to pay for discord soundboard
#####

#Modules
#from config import settings
#from audio.engine import AudioEngine
from app import SoundboardApp
def main():
    #Create app
    app = SoundboardApp()
    app.mainloop()


    #Test audio for output. Emulating pressing a soundboard button
    #wf = wave.open("src\soundboard\\assets\sounds\wizard.wav", 'rb')
    
    #engine = AudioEngine()
    #engine.showAllDeviceInfo()
    #engine.play("soundboard/assets/sounds/wizard.wav")
    #index = engine.getDeviceIndex(settings.OutputName, settings.Audio_API)
    #print(f"Index: {index}, Name: {settings.OutputName}, Host API: {settings.Audio_API}")
    
    
    
#Runnable Py file
if __name__ == "__main__":
    main()