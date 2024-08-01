from .app_state import *

from ...local_user import *

class MainApplicationState(ApplicationState):
    def __init__(self, local_user: LocalUser):
        super().__init__()
        self._local_user = local_user

    def get_local_user(self) -> LocalUser:
        return self._local_user
    


