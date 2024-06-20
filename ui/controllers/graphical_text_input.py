from ..background_threads.linear_animation import *
from ..graphics.text_input import *

from PyQt5 import QtCore as _QtCore
import love_letter as _love_letter
import random as _random

class GraphicalTextInputController():
    def __init__(self, text_input: TextInputDisplayedElement):
        self._element: TextInputDisplayedElement = text_input
        self._element.start_threads()
        
        self._element.signal_hover_enter.connect(self.on_text_hover_enter)
        self._element.signal_hover_leave.connect(self.on_text_hover_leave)
        self._element.signal_mouse_press.connect(self.on_text_pressed)
        self._element.signal_mouse_release.connect(self.on_text_released)
        self._element.signal_key_press.connect(self.on_key_press)
    
    def on_text_pressed(self) -> None:
        pass
    
    def on_text_released(self) -> None:
        pass
    
    def on_text_hover_enter(self, event) -> None:
        self._element.go_to_size(110)
    
    def on_text_hover_leave(self, event) -> None:
        self._element.go_to_size(100)
    
    def on_key_press(self, event: _QtCore.QEvent) -> None:
#        print(event.key())
#        print(repr(event.text()))
        
        last_text = self._element.get_text()
        text = event.text()
        
        if text == "\x08":
            new_text = last_text[:-1]
        elif text != "\r":
            new_text = last_text + text
        
        self._element.set_text(new_text)
    
