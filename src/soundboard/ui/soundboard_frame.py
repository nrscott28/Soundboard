###
#   Holds the list of sounds for the soundboard and functionality for adding / deleting buttons
###

# Dependencies
from pathlib import Path
from config.settings import settings
from customtkinter import CTkFrame
from ui.soundbutton import SoundButton

class SoundboardFrame(CTkFrame):
    def __init__(self, master):
        super().__init__(
            master=master,
            corner_radius=settings.corner_radius
        )
        self.sound_buttons = []  # List to hold sound buttons
    
    def add_button(self, button: SoundButton):
        self.sound_buttons.append(button)

    def delete_button(self, button: SoundButton):
        if button in self.sound_buttons:
            self.sound_buttons.remove(button)
            button.destroy()  # Remove the button from the UI