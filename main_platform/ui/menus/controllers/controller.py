from ..graphic_layers.layer import *
from ..menus import *
from ....settings import *

import typing as _T
import events as _events

class LayerController():
    def __init__(self, graphic_layer: GraphicLayer, menu: Menu, settings: MainSettings):
        self._layer = graphic_layer
        self._menu = menu
        self._settings = settings

        self._events = _events.EventObject(
            "open_menu",
            "close_menu",
        )

    def get_layer(self) -> GraphicLayer:
        return self._layer
    
    def get_menu(self) -> Menu:
        return self._menu
    
    def get_settings(self) -> MainSettings:
        return self._settings
    
    def get_events(self) -> _events.EventObject:
        return self._events
    
    def add_layer_event(self, name: str, func: _T.Callable) -> None:
        self._layer.get_events().addEventListener(name, func)

    def add_menu_event(self, name: str, func: _T.Callable) -> None:
        self._menu.get_events().addEventListener(name, func)
    
    def open_menu(self, name: str) -> None:
        self._events["open_menu"].emit(name)
    
    def close_menu(self) -> None:
        self._events['close_menu'].emit()
