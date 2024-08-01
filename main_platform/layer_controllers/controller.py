from ..ui.graphic_layers import *
from ..settings import *
from ..platform.apps import *

import typing as _T
import events as _events

class LayerController():
    def __init__(self, graphic_layer: GraphicLayer, application_state: ApplicationState, settings: MainSettings):
        self._layer = graphic_layer
        self._state = application_state
        self._settings = settings

        self._events = _events.EventObject(
            "open_application",
            "close_application",
        )

    def get_layer(self) -> GraphicLayer:
        return self._layer
    
    def get_application_state(self) -> ApplicationState:
        return self._state
    
    def get_settings(self) -> MainSettings:
        return self._settings
    
    def get_events(self) -> _events.EventObject:
        return self._events
    
    def add_layer_event(self, name: str, func: _T.Callable) -> None:
        self._layer.get_events().addEventListener(name, func)

    def add_appstate_event(self, name: str, func: _T.Callable) -> None:
        self._state.get_events().addEventListener(name, func)
    
    def open_application(self, application: Application) -> None:
        self._events["open_application"].emit(application)
    
    def close_application(self) -> None:
        self._events['close_application'].emit()
