from ..background_threads.linear_animation import *
from ..graphics.button import *

from PyQt5 import QtCore as _QtCore
import love_letter as _love_letter
import random as _random

class GraphicalButtonController():
    def __init__(self, button: ButtonDisplayedElement):
        self._element: ButtonDisplayedElement = button
        self._element.start_threads()
        
        self._element.signal_hover_enter.connect(self.on_button_hover_enter)
        self._element.signal_hover_leave.connect(self.on_button_hover_leave)
        self._element.signal_mouse_press.connect(self.on_button_pressed)
        self._element.signal_mouse_release.connect(self.on_button_released)
    
    def on_button_pressed(self) -> None:
        self._element.go_to_size(90)
    
    def on_button_released(self) -> None:
        self._element.go_to_size(110)
    
    def on_button_hover_enter(self, event) -> None:
        self._element.go_to_size(110)
    
    def on_button_hover_leave(self, event) -> None:
        self._element.go_to_size(100)
    
