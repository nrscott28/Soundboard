###
#   Holds the list of sounds for the soundboard and functionality for adding / deleting buttons
###

# Dependencies
from pathlib import Path
from config.settings import settings
from customtkinter import CTkFrame
from ui.soundbutton import SoundButton

import json

class SoundboardFrame(CTkFrame):
    def __init__(self, master):
        super().__init__(
            master=master,
            corner_radius=settings.corner_radius
        )
        self.sound_buttons = []  # List to hold sound buttons

    # Populate buttons based on buttons json file
    def populate_buttons(self):
        # Clear existing buttons
        for button in self.sound_buttons:
            button.destroy()
        self.sound_buttons.clear()

        # Populate buttons based on settings
        for button_data in settings.buttons:
            if True: continue
            else:
                print(f"Sound file not found: {sound_path}") 

    #save all buttons to the buttons json file
    def save_buttons(self):
        

    def add_button(self, button: SoundButton):
        self.sound_buttons.append(button)
        self.save_buttons()  # Save the updated list of buttons to the buttons json file

    def delete_button(self, button: SoundButton):
        if button in self.sound_buttons:
            self.sound_buttons.remove(button)
            button.destroy()  # Remove the button from the UI