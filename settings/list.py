import json as _json
import events as _events

class SettingsList():
    def __init__(self, data = None):
        self._events = _events.EventObject(
            'modified'
        )

        self._data = data or []

    def get_events(self) -> _events.EventObject:
        return self._events
    
    def __getitem__(self, index):
        return self._
