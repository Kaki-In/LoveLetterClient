from .controller import *

from ..ui.graphic_layers.first_layer import *
from ..settings import *

import events as _events
import typing as _T

class FirstGraphicLayerController(LayerController):
    def __init__(self, graphic_layer: FirstGraphicLayer, application: FirstApplicationState, settings: MainSettings):
        super().__init__(graphic_layer, application, settings)

        self.add_layer_event('button_press', self.on_button_press)
        self.add_layer_event('button_release', self.on_button_release)
        self.add_layer_event('text_changed', self.on_text_changed)
        self.add_layer_event('open_settings_released', self.on_open_settings_released)

        self.add_user_event('name_changed', self.on_application_name_changed)

        graphic_layer.set_name(settings.get_user_settings().get_name())
    
    def add_user_event(self, name: str, function: _T.Callable) -> None:
        self.get_application_state().get_local_user().get_events()[name].addEventFunction(function)
    
    def get_layer(self) -> FirstGraphicLayer:
        return super().get_layer()
    
    def get_application_state(self) -> FirstApplicationState:
        return super().get_application_state()
    
    def get_events(self) -> _events.EventObject:
        return self._events
    
    def on_button_press(self) -> None:
        pass
    
    def on_button_release(self) -> None:
        state = MainApplicationState(self.get_application_state().get_local_user())
        self.open_application(MainApplication(state))
    
    def on_open_settings_released(self, event: _events.Event) -> None:
        state = SettingsApplicationState()
        self.open_application(SettingsApplication(state))
        
    def on_text_changed(self, event: _events.Event) -> None:
        value = event.values()[0]
        state = self.get_application_state()

        state.get_local_user().set_name(value)

        layer = self.get_layer()

        if state.is_valid():
            layer.enable_button()
        else:
            layer.disable_button()
    
    def on_application_name_changed(self, event: _events.Event) -> None:
        self.get_settings().get_user_settings().set_name(event.values()[0])
    


