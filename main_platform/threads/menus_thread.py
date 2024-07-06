from .menus import *
from .menus.first_menu import *

import threading as _threading
import time as _time
import events as _events

class MenusThread():
    def __init__(self):
        self._menus: list[Menu] = []
        self._thread: _threading.Thread = None

        self._events = _events.EventObject(
            "menu_open", 
            "menu_close"
        )

    def get_events(self) -> _events.EventObject:
        return self._events

    def get_menu(self) -> Menu:
        return self._menus[-1]
    
    def open_menu(self, menu: Menu) -> Menu:
        self._menus.append(menu)
        self._events["menu_open"].emit(menu)
    
    def close_menu(self) -> None:
        self._menus.pop(-1)
        self._events["menu_close"].emit()

    def start(self):
        thread = _threading.Thread(target = self.run)
        thread.start()
        
    def run(self) -> None:
        self.open_menu(FirstMenu())
    


