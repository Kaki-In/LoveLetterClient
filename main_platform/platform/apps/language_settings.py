from .app import *

from .controller.language_settings import *
from .state.language_settings import *

import events as _events

class LanguageSettingsApplication(Application):
    def __init__(self, state: LanguageSettingsApplicationState):
        super().__init__(state, LanguageSettingsApplicationController(state))

        self._events = _events.EventObject(
            'open_app',
            'close_app'
        )
    
    def get_state(self) -> LanguageSettingsApplicationState:
        return super().get_state()
    
    def get_controller(self) -> LanguageSettingsApplicationController:
        return super().get_controller()
