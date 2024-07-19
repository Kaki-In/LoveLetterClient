from .menu import *

import typing as _T
import events as _events

class LanguageSettingsMenu(Menu):
    def __init__(self):
        super().__init__()

        self._language = None
        self._events.create_events(
            'language_changed'
        )
    
    def get_events(self) -> _events.EventObject:
        return self._events
    
    def get_language(self) -> _T.Optional[str]:
        return self._language
    
    def set_language(self, value: str) -> None:
        self._language = value
