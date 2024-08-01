from .app_state import *

from ...local_user import *

class FirstApplicationState(ApplicationState):
    def __init__(self, local_user: LocalUser):
        super().__init__()
        self._user = local_user
    
    def get_local_user(self) -> LocalUser:
        return self._user
    
    def is_valid(self) -> bool:
        return bool(self._user.get_name())
