#Dependencies
import customtkinter as ctk

from audio.engine import AudioEngine
from config import settings

class SoundboardApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title(settings.title)
        self.geometry(settings.window_size)

        self.engine = AudioEngine()