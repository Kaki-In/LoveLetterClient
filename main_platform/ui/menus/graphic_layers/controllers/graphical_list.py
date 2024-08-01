from ....animations.linear_animation import *
from ..graphics.dlist import *

import love_letter as _love_letter
import random as _random
import events as _events

from PyQt5 import QtWidgets as _QtWidgets

class GraphicalListController():
    def __init__(self, list: ListDisplayedElement):
        self._element: ListDisplayedElement = list
        self._element.start_threads()
        
        elem_events = list.get_events()

        elem_events["hover_enter"].addEventFunction(self.on_list_entered)
        elem_events["hover_move"].addEventFunction(self.on_list_hovered)
        elem_events["hover_leave"].addEventFunction(self.on_list_left)
        elem_events["mouse_press"].addEventFunction(self.on_list_pressed)
        elem_events["mouse_release"].addEventFunction(self.on_list_released)

        self._events = _events.EventObject(
            'item_selected',
            'item_hovered'
        )
    
    def get_events(self) -> _events.EventObject:
        return self._events
    
    def on_list_pressed(self, event: _events.Event) -> None:
        pass
    
    def on_list_released(self, event: _events.Event) -> None:
        qevent: _QtWidgets.QGraphicsSceneHoverEvent = event.values()[0]

        x = qevent.pos().x()
        y = qevent.pos().y() + self._element.get_height() / 2

        item = self._element.item_at(y)
        if item is None:
            return

        self._element.set_selected_position(item)
        self._events['item_selected'].emit(item)
    
    def on_list_entered(self, event: _events.Event) -> None:
        self.on_list_hovered(event)

    def on_list_left(self, event: _events.Event) -> None:
        self._element.set_hovered_position(None)

    def on_list_hovered(self, event: _events.Event) -> None:
        qevent: _QtWidgets.QGraphicsSceneHoverEvent = event.values()[0]

        x = qevent.pos().x()
        y = qevent.pos().y() + self._element.get_height() / 2

        item = self._element.item_at(y)
        self._element.set_hovered_position(item)

        self._events['item_hovered'].emit(item)

    
