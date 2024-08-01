from .app_controller import *
from ..state.main import *

class SettingsApplicationController(ApplicationController):
    def __init__(self, state: SettingsApplicationState):
        super().__init__(state)

