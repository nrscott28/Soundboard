#Dependencies
import customtkinter as ctk

# ** Import audio engine to play sound when button is pressed **

from config.settings import settings
from audio.sound import Sound           #Hold the sound for the button to play
from pathlib import Path                #Used to get path for sound file

class SoundButton(ctk.CTkButton):
    def __init__(self, master, path: Path, text="", width=settings.buttonSize, height=settings.buttonSize, command=None): #Add Play function to command

        self.path = path
        self.sound = Sound(self.path) #Create sound object to hold sound file and settings

        #Create Button
        super().__init__(
            master=master,
            width=width,
            height=height,
            text=text
        )

        