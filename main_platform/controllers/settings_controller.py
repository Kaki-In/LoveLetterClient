from ..ui.view.graphic_layers.settings_layer import *
from ..threads.menus.settings_menu import *

import events as _events

class SettingsGraphicLayerController():
    def __init__(self, graphic_layer: SettingsLayer, menu: SettingsMenu):
        self._graphic_layer = graphic_layer
        self._graphic_layer.get_events()['back'].addEventFunction(self.on_back_pressed)
        self._menu = menu

        self._events = _events.EventObject(
            "open_menu",
            "close_menu",
        )

    def get_events(self) -> _events.EventObject:
        return self._events
    
    def on_back_pressed(self, event: _events.Event):
        self._events['close_menu'].emit()
