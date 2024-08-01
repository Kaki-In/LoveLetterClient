from .app_controller import *
from ..state.main import *

class MainApplicationController(ApplicationController):
    def __init__(self, state: MainApplicationState):
        super().__init__(state)

