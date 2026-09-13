###
# Holds a sound for buttons to play. This class is used to manage the sound file and its settings.
###

#Dependencies
from pathlib import Path
from config.settings import settings


class Sound:
	def __init__(self, path: str | Path) -> None:
		self.path = Path(path)
		