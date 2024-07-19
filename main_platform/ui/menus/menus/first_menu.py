from .menu import *

import events as _events

class FirstMenu(Menu):
    def __init__(self):
        super().__init__()
        self._name: str = ""
        self._events.create_events(
            'name_changed'
        )
    
    def get_events(self) -> _events.EventObject:
        return self._events
    
    def is_valid(self) -> bool:
        return bool(self._name)
    
    def get_name(self) -> str:
        return self._name
    
    def set_name(self, name: str) -> None:
        self._name = name
        self._events['name_changed'].emit(name)


