import json
import os

current_dir = os.path.dirname(os.path.abspath(__file__))


class Preferences:
    def __init__(self, file_path=".mypy_cache/preferences.json"):
        self.file_path = file_path
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        self.preferences = self.load()

    def save(self):
        with open(self.file_path, "w") as file:
            json.dump(self.preferences, file, indent=4)

    def load(self):
        try:
            with open(self.file_path, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            # Return default preferences if the file doesn't exist
            return {
                "theme": "light",
                "font_size": 10,
                "language": "en",
            }

    def get(self, key, default=None):
        return self.preferences.get(key, default)

    def set(self, key, value):
        self.preferences[key] = value
        self.save()
