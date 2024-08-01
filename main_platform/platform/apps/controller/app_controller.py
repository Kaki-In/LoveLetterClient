from ..state import *

class ApplicationController():
    def __init__(self, state: ApplicationState):
        self._state = state
    
    def get_state(self) -> ApplicationState:
        return self._state


