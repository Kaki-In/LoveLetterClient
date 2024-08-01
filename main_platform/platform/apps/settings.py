from .app import *

from .controller.settings import *
from .state.settings import *

import events as _events

class SettingsApplication(Application):
    def __init__(self, state: SettingsApplicationState):
        super().__init__(state, SettingsApplicationController(state))

        self._events = _events.EventObject(
            'open_app',
            'close_app'
        )
    
    def get_state(self) -> SettingsApplicationState:
        return super().get_state()
    
    def get_controller(self) -> SettingsApplicationController:
        return super().get_controller()
