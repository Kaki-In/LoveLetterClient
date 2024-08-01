import json as _json
import typing as _T
import events as _events

from .data import *

class SettingsObject(SettingsData):
    def __init__(self, data: dict[str, _T.Any] = None):
        super().__init__()
        self._data = data or {}

        for key in data:
            self.plug_events(data[key])

        self._events = _events.EventObject(
            'modified'
        )
    
    def get_events(self) -> _events.EventObject:
        return self._events
    
    def get(self, name: str):
        return self._data[name]
    
    def __set__(self, name: str, value) -> None:
        self._data[name] = value

    def to_json(self) -> str:
        d = {}
        for name in self._data:
            value = self._data[name]

            if issubclass(type(value), SettingsData):
                d[name] = value.to_json()
            else:
                d[name] = value
        return d
    
    def on_value_modified(self, event: _events.Event):
        self._events['modified'].emit()
    
    def __iter__(self) -> _T.Iterator:
        return iter(self._data)
    
    def __len__(self) -> int:
        return len(list(self))

