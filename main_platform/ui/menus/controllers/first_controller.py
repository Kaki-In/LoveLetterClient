from .controller import *

from ..graphic_layers.first_layer import *
from ..menus.first_menu import *
from ....objects.settings import *

import events as _events

class FirstGraphicLayerController(LayerController):
    def __init__(self, graphic_layer: FirstGraphicLayer, menu: FirstMenu, settings: MainSettings):
        super().__init__(graphic_layer, menu, settings)

        self.add_layer_event('button_press', self.on_button_press)
        self.add_layer_event('button_release', self.on_button_release)
        self.add_layer_event('text_changed', self.on_text_changed)
        self.add_layer_event('open_settings_released', self.on_open_settings_released)

        self.add_menu_event('name_changed', self.on_menu_name_changed)

        graphic_layer.set_name(settings.get_user_settings().get_name())
    
    def get_layer(self) -> FirstGraphicLayer:
        return super().get_layer()
    
    def get_menu(self) -> FirstMenu:
        return super().get_menu()
    
    def get_events(self) -> _events.EventObject:
        return self._events
    
    def on_button_press(self) -> None:
        pass
    
    def on_button_release(self) -> None:
        self.open_menu('main')
    
    def on_open_settings_released(self, event: _events.Event) -> None:
        self.open_menu('settings')
    
    def on_text_changed(self, event: _events.Event) -> None:
        value = event.values()[0]
        menu = self.get_menu()

        menu.set_name(value)

        layer = self.get_layer()

        if menu.is_valid():
            layer.enable_button()
        else:
            layer.disable_button()
    
    def on_menu_name_changed(self, event: _events.Event) -> None:
        self.get_settings().get_user_settings().set_name(event.values()[0])
    


