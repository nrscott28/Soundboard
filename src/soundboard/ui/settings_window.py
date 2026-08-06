#Dependencies
import customtkinter as ctk

from config.settings import settings

class SettingsWindow(ctk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title(settings.settings_title)
        self.geometry(settings.settings_size)
        self.after(10,self.lift())

        