###
# Holds a sound for buttons to play. This class is used to manage the sound file and its settings.
###

from pathlib import Path
from soundboard.config import settings


class Sound:
	def __init__(self, path: str | Path) -> None:
		self.path = Path(path)
		