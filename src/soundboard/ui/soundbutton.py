#Dependencies
import customtkinter as ctk

# ** Import audio engine to play sound when button is pressed **

from config.settings import settings
class SoundButton(ctk.CTkButton):
    def __init__(self, master, text="", width=settings.buttonSize, height=settings.buttonSize, command=None): #Add Play function to command

        
        #Create Button
        super().__init__(
            master=master,
            width=width,
            height=height,
            text=text
        )

        