from .app_state import *

import typing as _T
import events as _events

import resources as _resources

class GraphicalSettingsApplicationState(ApplicationState):
    def __init__(self):
        super().__init__()

        self._theme: int = None
        self._themes: list[tuple[str, _resources.Theme]] = []

        self._events.create_events(
            'theme_changed',
            'theme_list_changed',
            'fullscreen_changed'
        )

        self._fullscreen = False
    
    def get_events(self) -> _events.EventObject:
        return self._events
    
    def get_themes(self) -> list[tuple[str, _resources.Theme]]:
        return self._themes
    
    def add_theme(self, id: str, name: _resources.Theme) -> None:
        self._themes.append((id, name))
        self._events['theme_list_changed'].emit()
    
    def clear_themes(self) -> None:
        self._themes = []
        self._events['theme_list_changed'].emit()
    
    def get_theme(self) -> int:
        return self._theme
    
    def set_theme(self, value: int) -> None:
        self._theme = value
        self._events['theme_changed'].emit(value)
    
    def get_fullscreen(self) -> bool:
        return self._fullscreen
    
    def set_fullscreen(self, enabled: bool) -> None:
        self._fullscreen = enabled
