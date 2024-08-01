from .app import *

from .controller.main import *
from .state.main import *

import events as _events

class MainApplication(Application):
    def __init__(self, state: MainApplicationState):
        super().__init__(state, MainApplicationController(state))

        self._events = _events.EventObject(
            'open_app',
            'close_app'
        )
    
    def get_state(self) -> MainApplicationState:
        return super().get_state()
    
    def get_controller(self) -> MainApplicationController:
        return super().get_controller()
