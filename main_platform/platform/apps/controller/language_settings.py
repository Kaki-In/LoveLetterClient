from .app_controller import *
from ..state.main import *

class LanguageSettingsApplicationController(ApplicationController):
    def __init__(self, state: LanguageSettingsApplicationState):
        super().__init__(state)

