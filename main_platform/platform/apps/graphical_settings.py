from .app import *

from .controller.graphical_settings import *
from .state.graphical_settings import *

import events as _events

class GraphicalSettingsApplication(Application):
    def __init__(self, state: GraphicalSettingsApplicationState):
        super().__init__(state, GraphicalSettingsApplicationController(state))

        self._events = _events.EventObject(
            'open_app',
            'close_app'
        )
    
    def get_state(self) -> GraphicalSettingsApplicationState:
        return super().get_state()
    
    def get_controller(self) -> GraphicalSettingsApplicationController:
        return super().get_controller()
