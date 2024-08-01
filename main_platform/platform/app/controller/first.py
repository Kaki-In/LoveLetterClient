from .app_controller import *
from ..state.first import *

class FirstApplicationController(ApplicationController):
    def __init__(self, state: FirstApplicationState):
        super().__init__(state)
    
    def get_state(self) -> FirstApplicationState:
        return super().get_state()

