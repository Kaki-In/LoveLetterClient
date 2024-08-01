from main_platform.platform.app.controller import ApplicationController
from .state.first import *
from .controller.first import *

from .app import *

from ..local_user import *

class FirstApplication(Application):
    def __init__(self, local_user: LocalUser) -> None:
        super().__init__(FirstApplicationState(local_user), FirstApplicationController)
    
    def get_state(self) -> FirstApplicationState:
        return super().get_state()
    
    def get_controller(self) -> FirstApplicationController:
        return super().get_controller()


