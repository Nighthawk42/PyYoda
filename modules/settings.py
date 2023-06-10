# modules/settings.py

import json
from pathlib import Path

class Settings:
    def __init__(self, settings_file_path):
        self.settings_file_path = settings_file_path
        with open(settings_file_path, 'r') as f:
            self.settings = json.load(f)

    def load_settings(self):
        try:
            with open(self.settings_file_path) as settings_file:
                return json.load(settings_file)
        except FileNotFoundError:
            default_settings = {
                "player": "Luke Skywalker",
                "window_width": 1280,
                "window_height": 720,
                "fullscreen": False,
                "volume": 1.0,
                "mute": False,
                "world_size": "small",
                "difficulty": "easy",
                "wins": 0,
                "losses": 0,
                "highscore": 0
            }
            return default_settings

    def save_settings(self):
        settings_file = Path(self.settings_file_path)
        try:
            settings_file.write_text(json.dumps(self.settings, indent=4))
        except Exception as e:
            print(f"Error saving settings: {e}")
        finally:
            settings_file.close()

        # Add any additional methods for manipulating the settings as needed