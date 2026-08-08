#Dependencies
import customtkinter as ctk
from config.settings import settings
class SoundButton(ctk.CTkButton):
    def __init__(self, master, width=settings.buttonSize, height=settings.buttonSize):
        