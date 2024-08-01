from .controller import *
from .state import *

import events as _events

class Application():
    def __init__(self, state: ApplicationState, controller: ApplicationController):
        self._state = state
        self._controller = controller

        self._events = _events.EventObject(
            'open_app',
            'close_app'
        )
    
    def get_state(self) -> ApplicationState:
        return self._state
    
    def get_controller(self) -> ApplicationController:
        return self._controller
