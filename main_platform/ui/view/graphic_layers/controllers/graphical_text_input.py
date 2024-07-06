from ....background_threads.linear_animation import *
from ..graphics.text_input import *

import love_letter as _love_letter
import random as _random
import events as _events

class GraphicalTextInputController():
    def __init__(self, text_input: TextInputDisplayedElement):
        self._element: TextInputDisplayedElement = text_input
        self._element.start_threads()

        elem_events = self._element.get_events()

        elem_events["hover_enter"].addEventFunction(self.on_text_hover_enter)
        elem_events["hover_leave"].addEventFunction(self.on_text_hover_leave)
        elem_events["mouse_press"].addEventFunction(self.on_text_pressed)
        elem_events["mouse_release"].addEventFunction(self.on_text_released)
        elem_events["key_press"].addEventFunction(self.on_key_press)
        
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
    
    def on_key_press(self, event: _events.Event) -> None:
#        print(event.key())
#        print(repr(event.text()))
        
        last_text = self._element.get_text()
        last_cursor = self._element.get_cursor_position()
        
        event = event.values()[0]
        
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
    
