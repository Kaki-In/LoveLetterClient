from ..ui.view.graphic_layers.first_layer import *
from ..threads.menus.first_menu import *

import events as _events

class FirstGraphicLayerController():
    def __init__(self, graphic_layer: FirstGraphicLayer, menu: FirstMenu):

        self._layer = graphic_layer
        self._layer.get_events()["button_press"].addEventFunction(self.on_button_press)
        self._layer.get_events()["button_release"].addEventFunction(self.on_button_release)
        self._layer.get_events()["text_changed"].addEventFunction(self.on_text_changed)
        self._layer.get_events()["open_settings_released"].addEventFunction(self.on_open_settings_released)

        self._menu = menu

        self._events = _events.EventObject(
            "open_menu",
            "close_menu",
        )
    
    def get_events(self) -> _events.EventObject:
        return self._events
    
    def on_button_press(self) -> None:
        pass
    
    def on_button_release(self) -> None:
        self._events["open_menu"].emit("main")
    
    def on_open_settings_released(self, event: _events.Event) -> None:
        self._events['open_menu'].emit("settings")
    
    def on_text_changed(self, event: _events.Event) -> None:
        value = event.values()[0]
        self._menu.set_name(value)

        if self._menu.is_valid():
            self._layer.enable_button()
        else:
            self._layer.disable_button()
        
    
    def layer(self) -> FirstGraphicLayer:
        return self._layer
    
    def menu(self) -> FirstMenu:
        return self._menu
    


