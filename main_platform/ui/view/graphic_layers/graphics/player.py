from PyQt5 import QtWidgets as _QtWidgets
from PyQt5 import QtGui as _QtGui
from PyQt5 import QtCore as _QtCore

from .element import *
from .card import *

from ....background_threads import *

import love_letter as _love_letter
import typing as _T
import math as _math

class PlayerDisplayedElement(GameDisplayedElement):
    def __init__(self, resources, first_card: _love_letter.LoveLetterCard, second_card: _love_letter.LoveLetterCard, name: str, discard: list[_love_letter.LoveLetterCard] = [], parent = None):
        super().__init__(resources, 0, 0, 300, 300, parent)
        
        self._first_card = first_card
        self._second_card = second_card
        
        self._name = name
        
        if first_card:
            self._first_card_element = CardDisplayedElement(resources, first_card.get_character(), self)
        else:
            self._first_card_element = CardDisplayedElement(resources, None, self)
        self._first_card_element.hide()
        
        if second_card:
            self._second_card_element = CardDisplayedElement(resources, second_card.get_character(), self)
        else:
            self._second_card_element = CardDisplayedElement(resources, None, self)
        self._second_card_element.hide()
        
        self._discard = discard
        
        import random
        for _ in range(3):
            self._discard.append(_love_letter.LoveLetterCard(random.choice([_love_letter.LOVE_LETTER_CHARACTER_GUARD, _love_letter.LOVE_LETTER_CHARACTER_PRIEST, _love_letter.LOVE_LETTER_CHARACTER_BARON, _love_letter.LOVE_LETTER_CHARACTER_HANDMAID, _love_letter.LOVE_LETTER_CHARACTER_PRINCE, _love_letter.LOVE_LETTER_CHARACTER_KING, _love_letter.LOVE_LETTER_CHARACTER_COUNTESS, _love_letter.LOVE_LETTER_CHARACTER_PRINCESS])))
        
        self._won_rounds = 2
        self._max_rounds = 5
        
        self.update_card_position()
    
    def set_max_rounds(self, rounds: int) -> None:
        self._max_rounds = rounds
    
    def get_max_rounds(self) -> int:
        return self._max_rounds
    
    def set_won_rounds(self, rounds: int) -> None:
        self._won_rounds = rounds
    
    def get_won_rounds(self) -> int:
        return self._won_rounds
    
    def start_threads(self):
        self._first_card_element.start_threads()
        self._second_card_element.start_threads()
    
    def stop_threads(self):
        self._first_card_element.stop_threads()
        self._second_card_element.stop_threads()
    
    def update_card_position(self):
        w, h = self._width, self._height
        x, y = -w/2, -h/2
        
        card_rect_x = x + 3*w/20
        card_rect_w = 31*w/40
        
        if self._first_card:
            self._second_card_element.go_to_position(card_rect_x + card_rect_w/2 - card_rect_w/4, 0)
        else:
            self._second_card_element.go_to_position(card_rect_x + card_rect_w/2, 0)
        
        if self._second_card:
            self._first_card_element.go_to_position(card_rect_x + card_rect_w/2 + card_rect_w/4, 0)
        else:
            self._first_card_element.go_to_position(card_rect_x + card_rect_w/2, 0)
        
        self.prepareGeometryChange()
        self.update()
    
    def set_first_card(self, card: _love_letter.LoveLetterCard):
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
        super().paint(painter, options, widget)
        image = self._resources.get_images_mapper().get_image_by_name("player")
        
        w, h = self._width, self._height
        x, y = -w/2, -h/2
        
        variant = "dark" if self._dark_mode else "light"
        painter.drawImage(_QtCore.QRectF(x, y, w, h), image.get_variant(variant))
        
        if self._first_card:
            self.paintChild(self._first_card_element, painter, options, widget)
        
        if self._second_card:
            self.paintChild(self._second_card_element, painter, options, widget)
        
        font = _QtGui.QFont("Chomsky", int(self._width * 10/100))
        fm = _QtGui.QFontMetrics(font)
        text_width = fm.width(self._name)
        text_height = fm.height()
        
        font.setPointSize(int(self._width * 10/100))
        painter.setFont(font)
        
        if self._dark_mode:
            painter.setPen(_QtGui.QColor( 0xFFFFFFFF ))
        else:
            painter.setPen(_QtGui.QColor( 0xFF000000 ))
        
        painter.drawText(_QtCore.QPoint(int(x + w/2 - text_width/2), int(y + h/5 - text_height/2)), self._name)
        
        heart_image = self._resources.get_images_mapper().get_image_by_name("heart")
        
        for n in range(1, self._max_rounds + 1):
            if n <= self._won_rounds:
                displayed_image = heart_image.get_variant("earned")
            else:
                displayed_image = heart_image.get_variant("back")
            
            painter.drawImage(_QtCore.QRectF(x + w/40, y + 3*h/20 + n*w * 3/30, w/15, w/15), displayed_image)
            
        
        for position, card in enumerate(self._discard):
            character = card.get_character().get_name().lower()
            image = self._resources.get_images_mapper().get_image_by_name("character_" + character)
            display_image = image.get_variant("token")
            
            x_pos = x + w/20 + position * w/8
            y_pos = y + 17*h/20
            
            painter.drawImage(_QtCore.QRectF(x_pos, y_pos, w/10, w/10), display_image)
        
    
    def set_size(self, size: int) -> None:
        self._width, self._height = size * 1.8, size * 1.8
        
        self._first_card_element.set_size(size)
        self._second_card_element.set_size(size)
        
        self.update_card_position()
    
#    def go_to_size(self, size: int) -> None:
#        self._size_animation.start_transition(self.get_size(), size, 0.3)
    
    def get_size(self) -> int:
        return self._height / 1.6

