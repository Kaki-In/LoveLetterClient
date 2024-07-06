from ..ui.view.graphic_layers.main_menu_layer import *
from ..threads.menus.main_menu import *

import events as _events

class MainGraphicLayerController():
    def __init__(self, graphic_layer: MainMenuGraphicLayer, menu: MainMenu):

        self._layer = graphic_layer

        self._menu = menu

        self._events = _events.EventObject(
            "open_menu",
            "close_menu"
        )
    
    def get_events(self) -> _events.EventObject:
        return self._events
    
    def layer(self) -> MainMenuGraphicLayer:
        return self._layer
    
    def menu(self) -> MainMenu:
        return self._menu
    


