import json as _json
import events as _events
import typing as _T

from .data import *

class SettingsList(SettingsData):
    def __init__(self, data = None):
        self._events = _events.EventObject(
            'modified'
        )
        super().__init__()
        self._data = data or []

    def get_events(self) -> _events.EventObject:
        return self._events
    
    def __set__(self, index: int, value) -> None:
        self._data[index] = value
    
    def append(self, value) -> None:
        self._data.append(value)
        self.plug_events(value)
        self.on_value_modified()
    
    def insert(self, index: int, value) -> None:
        self._data.insert(index, value)
        self.plug_events(value)
        self.on_value_modified()
    
    def remove(self, value) -> None:
        self._data.remove(value)
        self.unplug_events(value)
        self.on_value_modified()
    
    def to_json(self):
        l = []
        for value in self._data:
            if issubclass(type(value), SettingsData):
                l.append(value.to_json())
            else:
                l(_json.dumps(value))
        return l
    
    def __iter__(self) -> _T.Iterator:
        return iter(self._data)
