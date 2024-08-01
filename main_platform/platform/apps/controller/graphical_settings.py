from .app_controller import *
from ..state.main import *

class GraphicalSettingsApplicationController(ApplicationController):
    def __init__(self, state: GraphicalSettingsApplicationState):
        super().__init__(state)

