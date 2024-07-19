import json as _json
import events as _events
import os as _os

from .settings import *

class SettingsFile():
    def __init__(self, path: str):
        self._path = path
        self._settings = self._load_settings()
        self._settings.get_events()['modified'].addEventFunction(self.on_settings_modified)

    def on_settings_modified(self, event: _events.Event) -> None:
        self.save()
    
    def _load_settings(self) -> SettingsObject:
        if not _os.path.exists(self._path):
            file = open(self._path, "w")
            file.write("{}")
            file.close()
    
        file = open(self._path, "r")
        data = file.read()
        file.close()
        return getSettingsFromJson(data)
    
    def get_settings(self) -> SettingsObject:
        return self._settings

    def save(self) -> None:
        file = open(self._path, "w")
        file.write(self._settings.to_json())
        file.close()
 

