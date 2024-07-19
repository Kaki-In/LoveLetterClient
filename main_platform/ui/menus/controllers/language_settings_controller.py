from .controller import *

from ..graphic_layers.language_settings import *
from ..menus.settings_menu import *
from ....objects.settings import *

import events as _events

class LanguageSettingsGraphicLayerController(LayerController):
    def __init__(self, graphic_layer: LanguageSettingsLayer, menu: LanguageSettingsMenu, settings: MainSettings):
        super().__init__(graphic_layer, menu, settings)

        self.add_layer_event('back', self.on_back_pressed)

    def get_layer(self) -> LanguageSettingsLayer:
        return super().get_layer()
    
    def get_menu(self) -> LanguageSettingsMenu:
        return super().get_menu()
    
    def get_events(self) -> _events.EventObject:
        return self._events
    
    def on_back_pressed(self, event: _events.Event) -> None:
        self.close_menu()
    
    def on_graphical_settings_pressed(self, event: _events.Event) -> None:
        return
        self.open_menu('settings.graphical')
    
    def on_language_settings_pressed(self, event: _events.Event) -> None:
        self.open_menu('settings.language')
