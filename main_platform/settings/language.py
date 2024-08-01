import settings as _settings
import os as _os
import events as _events
import typing as _T

class LanguageSettings():
    def __init__(self, configuration: _settings.SettingsObject):
        self._configuration = configuration
        
        if not 'language' in configuration:
            configuration['language'] = "en_EN"

        self._events = _events.EventObject(
            'language'
        )
    
    def add_event_listener(self, name: str, func: _T.Callable) -> None:
        self._events[name].addEventFunction(func)
        
    def get_language_id(self) -> str:
        return self._configuration['language']
    
    def set_language_id(self, name: str) -> None:
        self._configuration['language'] = name
        self._events['language'].emit(name)
