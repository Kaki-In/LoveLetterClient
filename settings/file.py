import json as _json
import events as _events
import os as _os
import typing as _T

from .object import *
from .list import *

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
        return getSettingsObjectFromJson(data)
    
    def get_settings(self) -> SettingsObject:
        return self._settings

    def save(self) -> None:
        file = open(self._path, "w")
        file.write(_json.dumps(self._settings.to_json(), indent=2))
        file.close()

def getSettingsObjectFromJson(json) -> SettingsObject:
    return getSettingsFromDict(_json.loads(json))

def getSettingsListFromJson(json) -> SettingsList:
    return getSettingsFromList(_json.loads(json))

def getSettingsFromDict(dictionary: dict[str, _T.Any]) -> SettingsObject:
    dictionary = dictionary.copy()
    for key in dictionary:
        value = dictionary[key]

        dictionary[key] = getSettingsDataFromObj(value)
        
    return SettingsObject(dictionary)

def getSettingsFromList(list: list) -> SettingsList:
    result_list = []

    for element in list:
        result_list.append(getSettingsDataFromObj(element))
    
    return SettingsList(result_list)

def getSettingsDataFromObj(obj) -> SettingsData | _T.Any:
    if type(obj) is dict:
        return getSettingsFromDict(obj)
    
    elif type(obj) is list:
        return getSettingsFromList(obj)
    
    else:
        return obj
