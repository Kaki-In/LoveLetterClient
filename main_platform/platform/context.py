from .app import *
from .local_user import *

import typing as _T
import events as _events

class ActivityContext():
    def __init__(self):
        self._user = LocalUser('')
        self._applications: list[Application] = [FirstApplication()]

        self._events = _events.EventObject(
            'table_changed'
            "application_open", 
            "application_close"
        )

    def get_events(self) -> _events.EventObject:
        return self._events

    def open_application(self, menu: Application) -> Application:
        self._applications.append(menu)
        self._events["menu_open"].emit(menu)
    
    def close_menu(self) -> None:
        self._applications.pop(-1)
        self._events["menu_close"].emit()

    def get_active_application(self) -> Application:
        return self._applications[-1]
    
    def get_local_user(self) -> LocalUser:
        return self._user
