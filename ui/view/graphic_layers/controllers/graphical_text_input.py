from ....background_threads.linear_animation import *
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
        
        self._element.setCentered(True)
    
    def on_text_pressed(self) -> None:
        pass
    
    def on_text_released(self) -> None:
        pass
    
    def on_text_hover_enter(self, event) -> None:
#        self._element.go_to_ratio(11/10)
        pass
    
    def on_text_hover_leave(self, event) -> None:
        pass
#        self._element.go_to_ratio(1)
    
    def on_key_press(self, event: _QtCore.QEvent) -> None:
#        print(event.key())
#        print(repr(event.text()))
        
        last_text = self._element.get_text()
        last_cursor = self._element.get_cursor_position()
        
        text = event.text()
        
        new_text = last_text
        new_cursor = last_cursor
        if text == "\x08":
            if last_cursor > 0:
                new_text = last_text[:last_cursor - 1] + last_text[last_cursor:]
                new_cursor = last_cursor - 1
        elif event.key() == 16777234:
            if last_cursor > 0:
                new_cursor = last_cursor - 1
        elif event.key() == 16777236:
            if last_cursor <= len(last_text):
                new_cursor = last_cursor + 1
        elif text != "\r":
            new_text = last_text[:last_cursor] + text + last_text[last_cursor :]
            new_cursor = last_cursor + len(text)
        
        self._element.set_text(new_text)
        self._element.set_cursor_position(new_cursor)
        
        self._element.start_blinking()
    
