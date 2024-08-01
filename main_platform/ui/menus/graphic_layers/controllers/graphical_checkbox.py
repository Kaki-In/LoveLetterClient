from ....animations.linear_animation import *
from ..graphics.checkbox import *

import events as _events
import typing as _T

class GraphicalCheckboxController():
    def __init__(self, check_box: CheckBoxDisplayedElement):
        self._element: CheckBoxDisplayedElement = check_box
        self._element.start_threads()
        
        elem_events = self._element.get_events()
        elem_events["mouse_release"].addEventFunction(self.on_mouse_released)

        self._events = _events.EventObject(
            'change'
        )
    
    def on_mouse_released(self, event) -> None:
        self._element.set_enabled(not self._element.is_enabled())
        self._events['change'].emit(self._element.is_enabled())

    def add_event_listener(self, name: str, function: _T.Callable) -> None:
        self._events[name].addEventFunction(function)
