###
#   Holds the list of sounds for the soundboard and functionality for adding / deleting buttons
###

# Dependencies
from pathlib import Path
from config.settings import settings
from customtkinter import CTkFrame

class SoundboardFrame(CTkFrame):
    def __init__(self, master):
        super().__init__(
            master=master,
            corner_radius=settings.corner_radius
        )
        self.sound_buttons = []  # List to hold sound buttons
    
        