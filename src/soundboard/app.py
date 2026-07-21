#Dependencies
import customtkinter as ctk

from audio.engine import AudioEngine
from config import settings

class SoundboardApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        #Attributes
        self.title(settings.title)
        self.geometry(settings.window_size)

        self.engine = AudioEngine()

        #Components  
        

        #Close window
        self.protocol("WM_DELETE_WINDOW", self._on_close)

    #Handles closing window
    def _on_close(self):
        self.engine.stop_all()
        self.destroy()