from PyQt5 import QtWidgets as _QtWidgets
from PyQt5 import QtGui as _QtGui
from PyQt5 import QtCore as _QtCore

from .element import *
from .card import *

from ..resources.fonts import *
from ..background_threads import *

import love_letter as _love_letter
import typing as _T
import math as _math

class PlayerDisplayedElement(GameDisplayedElement):
    def __init__(self, first_card: _love_letter.LoveLetterCard, second_card: _love_letter.LoveLetterCard, name: str, discard: list[int] = [], parent = None):
        super().__init__(0, 0, 300, 300, parent)
        
        self._first_card = first_card
        self._second_card = second_card
        
        self._name = name
        
        if first_card:
            self._first_card_element = CardDisplayedElement(first_card.get_character())
        else:
            self._first_card_element = CardDisplayedElement(None)
        
        if second_card:
            self._second_card_element = CardDisplayedElement(second_card.get_character())
        else:
            self._second_card_element = CardDisplayedElement(None)
        
        self._first_card_element.start_threads()
        self._second_card_element.start_threads()
        
        self._first_card_element.signal_update.connect(self.update)
        self._second_card_element.signal_update.connect(self.update)
        
        self.update_card_position()
    
    def update_card_position(self):
        if self._first_card:
            self._second_card_element.go_to_position(self._x - 9 * self._width/32, self._y)
        else:
            self._second_card_element.go_to_position(self._x, self._y)
        
        if self._second_card:
            self._first_card_element.go_to_position(self._x + 9 * self._width/32, self._y)
        else:
            self._first_card_element.go_to_position(self._x, self._y)
        
        self.update()
    
    def set_first_card(self, card: _love_letter.LoveLetterCard):
        w, h = self._width, self._height
        x, y = self._x - w/2, self._y - h/2
        
        self._first_card = card
        
        if card is not None:
            self._first_card_element.set_character(card.get_character())
            
        self.update_card_position()
    
    def set_second_card(self, card: _love_letter.LoveLetterCard):
        self._second_card = card
        
        if card:
            self._second_card_element.set_character(card.get_character())
        
        self.update_card_position()
    
    def paint(self, painter: _QtGui.QPainter, options: _QtWidgets.QStyleOptionGraphicsItem, widget: _QtWidgets.QWidget) -> None:
        image = IMAGES_MAPPER.get_image_by_name("player")
        
        w, h = self._width, self._height
        x, y = self._x - w/2, self._y - h/2
        
        margin = self._height / 8
        
        painter.drawImage(_QtCore.QRectF(x-margin, y-margin, w + margin * 2, h + margin * 2), image.get_variant(""))
        
        if self._first_card:
            self._first_card_element.paint(painter, options, widget)
        
        if self._second_card:
            self._second_card_element.paint(painter, options, widget)
        
        font = _QtGui.QFont("Chomsky", int(self._width * 10/100))
        fm = _QtGui.QFontMetrics(font)
        text_width = fm.width(self._name)
        text_height = fm.height()
        
        font.setPointSize(int(self._width * 10/100))
        painter.setFont(font)
        
        painter.setPen(_QtGui.QColor(0xFFFFFFFF ))
        
        painter.drawText(_QtCore.QPoint(int(x + w/2 - text_width/2), int(y + h/10 - text_height/2)), self._name)
    
    
    def set_size(self, size: int) -> None:
        self._width, self._height = size * 1.4, size * 1.4
        
        self._first_card_element.set_size(size)
        self._second_card_element.set_size(size)
        
        self.update_card_position()
    
#    def go_to_size(self, size: int) -> None:
#        self._size_animation.start_transition(self.get_size(), size, 0.3)
    
    def get_size(self) -> int:
        return self._height / 1.6
    
    def set_position(self, x: int, y: int) -> None:
        self._x = x
        self._y = y
        
        self.update_card_position()
    

