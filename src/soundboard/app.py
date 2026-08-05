#Dependencies
import customtkinter as ctk
from PIL import Image

from audio.engine import AudioEngine
from config import settings
from ui.settings_window import SettingsWindow

#Sets theme
ctk.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("src/soundboard/ui/themes/red.json")

class SoundboardApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        #Attributes
        self.title(settings.title)
        self.geometry(settings.window_size)

        self.grid_rowconfigure(0, weight=0)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        

        self.engine = AudioEngine()
    
        #   Components  

        # Top Options Frame
        options_frame = ctk.CTkFrame(self, height = 100, corner_radius=20)
        options_frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

        # Buttons Frame
        buttons_frame = ctk.CTkFrame(self, corner_radius=20)
        buttons_frame.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)
        
        #Settings Popup Window
        self.settings_window = None   
        self.settings_btn = ctk.CTkButton(master=options_frame, text="Settings", command=self.open_settings)
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