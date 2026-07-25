#Dependencies
import customtkinter as ctk
from PIL import Image

from audio.engine import AudioEngine
from config import settings
from ui.settings_window import SettingsWindow
class SoundboardApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        #Attributes
        self.title(settings.title)
        self.geometry(settings.window_size)

        self.engine = AudioEngine()
    
        #   Components  
        
        #Settings Window
        self.settings_window = None   
        self.settings_btn = ctk.CTkButton(self, text="Open Settings", command=self.open_settings)
        self.settings_btn.grid(row=0, column=0, padx=10, pady=10)

        #Close window
        self.protocol("WM_DELETE_WINDOW", self._on_close)


    def open_settings(self):
        if self.settings_window is None or not self.settings_window.winfo_exists():
            self.settings_window = SettingsWindow(self)  # create window if its None or destroyed
        else:
            self.settings_window.focus()  # if window exists focus it

    #Handles closing window
    def _on_close(self):
        self.engine.stop_all()
        self.destroy()