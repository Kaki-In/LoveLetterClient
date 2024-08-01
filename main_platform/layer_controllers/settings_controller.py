from .controller import *

from ..ui.graphic_layers.settings_layer import *
from ..platform.apps.state.settings import *
from ..settings import *

import events as _events

class SettingsGraphicLayerController(LayerController):
    def __init__(self, graphic_layer: SettingsLayer, application: SettingsApplicationState, settings: MainSettings):
        super().__init__(graphic_layer, application, settings)

        self.add_layer_event('back', self.on_back_pressed)
        self.add_layer_event('open_graphical_settings', self.on_graphical_settings_pressed)
        self.add_layer_event('open_language_settings', self.on_language_settings_pressed)

    def get_layer(self) -> SettingsLayer:
        return super().get_layer()
    
    def get_application_state(self) -> SettingsApplicationState:
        return super().get_application_state()
    
    def get_events(self) -> _events.EventObject:
        return self._events
    
    def on_back_pressed(self, event: _events.Event) -> None:
        self.close_application()
    
    def on_graphical_settings_pressed(self, event: _events.Event) -> None:
        state = GraphicalSettingsApplicationState()
        self.open_application(GraphicalSettingsApplication(state))
    
    def on_language_settings_pressed(self, event: _events.Event) -> None:
        state = LanguageSettingsApplicationState()
        self.open_application(LanguageSettingsApplication(state))
