import os as _os
import events as _events
import typing as _T

from .theme import *

class ThemesMapper():
    def __init__(self, dirname: str):
        self._themes: dict[str, Theme] = {}

        self._actual_theme = None
        
        for entity_name in _os.listdir(dirname):
            if _os.path.isdir(dirname + _os.sep + entity_name):
                self._themes[entity_name] = Theme(dirname + _os.sep + entity_name)

                if self._actual_theme is None:
                    self._actual_theme = entity_name
            
        self._events = _events.EventObject(
            'theme',
        )
    
    def add_event_listener(self, name: str, function: _T.Callable) -> None:
        self._events[name].addEventFunction(function)
    
    def get_theme(self, name: str) -> Theme:
        return self._themes[name]

    def get_palette(self) -> PalettesMapper:
        return self._themes[self._actual_theme].get_palettes_mapper()
    
    def get_image_by_name(self, name: str) -> Image:
        return self._themes[self._actual_theme].get_image_by_name(name)
    
    def get_theme_name(self) -> str:
        return self._actual_theme

    def set_theme_name(self, name: str) -> None:
        self._actual_theme = name
        self._events['theme'].emit(name)
    
    def get_theme_names(self) -> list[str]:
        return list(self._themes)



