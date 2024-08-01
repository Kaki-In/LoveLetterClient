from .controller import *

from ..graphic_layers.settings_layer import *
from ..menus.settings_menu import *
from ....settings import *

import events as _events

class SettingsGraphicLayerController(LayerController):
    def __init__(self, graphic_layer: SettingsLayer, menu: SettingsMenu, settings: MainSettings):
        super().__init__(graphic_layer, menu, settings)

        self.add_layer_event('back', self.on_back_pressed)
        self.add_layer_event('open_graphical_settings', self.on_graphical_settings_pressed)
        self.add_layer_event('open_language_settings', self.on_language_settings_pressed)

    def get_events(self) -> _events.EventObject:
        return self._events
    
    def on_back_pressed(self, event: _events.Event) -> None:
        self.close_menu()
    
    def on_graphical_settings_pressed(self, event: _events.Event) -> None:
        self.open_menu('settings.graphical')
    
    def on_language_settings_pressed(self, event: _events.Event) -> None:
        self.open_menu('settings.language')
