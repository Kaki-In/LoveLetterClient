import json as _json
import typing as _T
import events as _events

from .list import *

class SettingsObject():
    def __init__(self, data: dict[str, _T.Any]):
        self._data = data
        self._events = _events.EventObject(
            'modified'
        )
    
    def get_events(self) -> _events.EventObject:
        return self._events
    
    def get(self, name: str):
        return self._data[name]
    
    def set(self, name: str, value):
        last_value = self._data[name]

        if type(last_value) in (SettingsObject, SettingsList):
            last_value.get_events()['modified'].removeEventFunction(self.on_value_modified)

        self._data[name] = value

        if type(value) in (SettingsObject, SettingsList):
            value.get_events()['modified'].addEventFunction(self.on_value_modified)

        self._events['modified'].emit()
    
    def to_json(self) -> str:
        return _json.dumps(self._data)
    
    def on_value_modified(self, event: _events.Event):
        self._events['modified'].emit()

def getSettingsFromJson(json) -> SettingsObject:
    return getSettingsFromDict(_json.loads(json))

def getSettingsFromDict(dictionary: dict[str, _T.Any]) -> SettingsObject:
    dictionary = dictionary.copy()
    for key in dictionary:
        value = dictionary[key]
        if type(value) is dict:
            dictionary[key] = getSettingsFromDict(value)
    
    return SettingsObject(dictionary)
