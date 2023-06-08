# modules/settings.py

import json

class Settings:
    def __init__(self, settings_file_path):
        self.settings_file_path = settings_file_path
        self.settings = self.load_settings()

    def load_settings(self):
        try:
            with open(self.settings_file_path) as settings_file:
                return json.load(settings_file)
        except FileNotFoundError:
            # Use default settings if the file doesn't exist
            return {
                "player": "Luke Skywalker",
                "windowed_width": 1280,
                "windowed_height": 720,
                "fullscreen": False,
                "volume": 1.0,
                "world_size": "small",
                "difficulty": "easy",
                "highscore": 0
            }

    def save_settings(self):
        with open(self.settings_file_path, 'w') as settings_file:
            json.dump(self.settings, settings_file, indent=4)

    # Add any additional methods for manipulating the settings as needed