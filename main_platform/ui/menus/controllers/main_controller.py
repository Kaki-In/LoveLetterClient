from .controller import *

from ..graphic_layers.main_menu_layer import *
from ..menus.main_menu import *
from ....settings import *

import events as _events

class MainGraphicLayerController(LayerController):
    def __init__(self, graphic_layer: MainMenuGraphicLayer, menu: MainMenu, settings: MainSettings):
        super().__init__(graphic_layer, menu, settings)

        self.add_layer_event('back', self.on_back_pressed)
    
    def get_layer(self) -> MainMenuGraphicLayer:
        return super().get_layer()
    
    def get_menu(self) -> MainMenu:
        return super().get_menu()
    
    def get_events(self) -> _events.EventObject:
        return self._events
    
    def on_back_pressed(self, event: _events.Event):
        self.close_menu()
    


