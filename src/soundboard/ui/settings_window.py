#Dependencies
import customtkinter as ctk

from config import settings

class SettingsWindow(ctk.CTkTopLevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title(settings.settings_title)
        self.geometry(settings.settings_size)

        