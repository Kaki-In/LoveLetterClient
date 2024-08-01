from .app import *

from .controller.first import *
from .state.first import *

import events as _events

class FirstApplication(Application):
    def __init__(self, state: FirstApplicationState):
        super().__init__(state, FirstApplicationController(state))

        self._events = _events.EventObject(
            'open_app',
            'close_app'
        )
    
    def get_state(self) -> FirstApplicationState:
        return super().get_state()
    
    def get_controller(self) -> FirstApplicationController:
        return super().get_controller()
