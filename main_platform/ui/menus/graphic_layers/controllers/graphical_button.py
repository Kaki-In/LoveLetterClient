from ....animations.linear_animation import *
from ..graphics.button import *

import love_letter as _love_letter
import random as _random

class GraphicalButtonController():
    def __init__(self, button: ButtonDisplayedElement):
        self._element: ButtonDisplayedElement = button
        self._element.start_threads()
        
        elem_events = self._element.get_events()
        elem_events["hover_enter"].addEventFunction(self.on_button_hover_enter)
        elem_events["hover_leave"].addEventFunction(self.on_button_hover_leave)
        elem_events["mouse_press"].addEventFunction(self.on_button_pressed)
        elem_events["mouse_release"].addEventFunction(self.on_button_released)
    
    def on_button_pressed(self) -> None:
        if self._element.isEnabled():
            self._element.go_to_ratio(9/10)
    
    def on_button_released(self) -> None:
        if self._element.isEnabled():
            self._element.go_to_ratio(1)
    
    def on_button_hover_enter(self, event) -> None:
        if self._element.isEnabled():
            self._element.go_to_ratio(11/10)
    
    def on_button_hover_leave(self, event) -> None:
        if self._element.isEnabled():
            self._element.go_to_ratio(1)
    
