from .apps import *
from .local_user import *

import typing as _T
import events as _events

class ActivityContext():
    def __init__(self):
        self._user = LocalUser('')
        
        state = FirstApplicationState(self._user)
        self._applications: list[Application] = [Application(state, FirstApplicationController(state))]

        self._events = _events.EventObject(
            'table_changed',
            'application_open', 
            'application_close'
        )

    def get_events(self) -> _events.EventObject:
        return self._events

    def open_application(self, app: Application) -> Application:
        self._applications.append(app)
        self._events["application_open"].emit(app)
    
    def close_application(self) -> None:
        self._applications.pop(-1)
        self._events["application_close"].emit()

    def get_active_application(self) -> Application:
        return self._applications[-1]
    
    def get_local_user(self) -> LocalUser:
        return self._user
