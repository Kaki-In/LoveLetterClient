from .geometry import *

import settings as _settings
import events as _events
import typing as _T

class GraphicalSettings():
    def __init__(self, configuration: _settings.SettingsObject):
        self._configuration = configuration
        
        if not 'theme' in configuration:
            configuration['theme'] = "cartoon"
        
        if not 'fullscreen' in configuration:
            configuration['fullscreen'] = True
        
        if not 'geometry' in configuration:
            configuration['geometry'] = _settings.SettingsObject({})

        self._events = _events.EventObject(
            'theme',
            'fullscreen'
        )

    def add_event_listener(self, name: str, func: _T.Callable) -> None:
        self._events[name].addEventFunction(func)
        
    def get_theme_name(self) -> str:
        return self._configuration['theme']
    
    def set_theme_name(self, name: str) -> None:
        self._configuration['theme'] = name
        self._events['theme'].emit(name)
    
    def get_fullscreen_mode(self) -> bool:
        return self._configuration['fullscreen']
    
    def set_fullscreen_mode(self, enabled: bool) -> None:
        self._configuration['fullscreen'] = enabled
        self._events['fullscreen'].emit(enabled)
    
    def get_window_geometry_settings(self) -> GeometrySettings:
        return GeometrySettings(self._configuration['geometry'])
