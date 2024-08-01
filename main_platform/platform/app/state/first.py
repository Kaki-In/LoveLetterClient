from .app_state import *

from ...local_user import *

class FirstApplicationState(ApplicationState):
    def __init__(self, local_user: LocalUser):
        self._user = local_user
    
    def get_local_user(self) -> LocalUser:
        return self._user
