import json as _json
import typing as _T
import events as _events

class SettingsData():
    def __init__(self):
        self._events = _events.EventObject(
            'modified'
        )
    
    def get_events(self) -> _events.EventObject:
        return self._events
    
    def get(self, name: _T.Any):
        return None
    
    def __set__(self, name: _T.Any, value) -> None:
        pass

    def __getitem__(self, index: int):
        return self.get(index)
    
    def __setitem__(self, index: int, value) -> None:
        return self.set(index, value)
    
    def set(self, name: _T.Any, value):
        try:
            last_value = self.get(name)
            self.unplug_events(last_value)
        except (KeyError, IndexError):
            pass

        self.__set__(name, value)
        self.plug_events(value)

        self._events['modified'].emit()
    
    def plug_events(self, object: 'SettingsData' | _T.Any) -> None:
        if issubclass(type(object), SettingsData):
            object.get_events()['modified'].addEventFunction(self.on_value_modified)
    
    def unplug_events(self, object: 'SettingsData' | _T.Any) -> None:
        if issubclass(type(object), SettingsData):
            object.get_events()['modified'].removeEventFunction(self.on_value_modified)

    def on_value_modified(self, event: _events.Event):
        self._events['modified'].emit()
    
    def to_json(self):
        return None


