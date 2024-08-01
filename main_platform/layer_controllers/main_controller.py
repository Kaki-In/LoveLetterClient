from .controller import *

from ..ui.graphic_layers.main_layer import *
from ..platform.apps.state.main import *
from ..settings import *

import events as _events

class MainGraphicLayerController(LayerController):
    def __init__(self, graphic_layer: MainGraphicLayer, application: MainApplicationState, settings: MainSettings):
        super().__init__(graphic_layer, application, settings)

        self.add_layer_event('back', self.on_back_pressed)
    
    def get_layer(self) -> MainGraphicLayer:
        return super().get_layer()
    
    def get_application_state(self) -> MainApplicationState:
        return super().get_application_state()
    
    def get_events(self) -> _events.EventObject:
        return self._events
    
    def on_back_pressed(self, event: _events.Event):
        self.close_application()
    


