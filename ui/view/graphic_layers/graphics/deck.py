from PyQt5 import QtWidgets as _QtWidgets
from PyQt5 import QtGui as _QtGui
from PyQt5 import QtCore as _QtCore

from .element import *
from .card import *

from ....resources.fonts import *
from ....resources.images import *
from ....background_threads import *

import love_letter as _love_letter
import typing as _T
import math as _math

class DeckDisplayedElement(GameDisplayedElement):
    def __init__(self, count: int, last_card: _love_letter.LoveLetterCard, parent = None):
        super().__init__(0, 0, 450, 300, parent)
        
        self._last_card = last_card
        self._last_displayed_card = _love_letter.LoveLetterCard(last_card.get_character())
        
        self._count = count
        
        self._no_card = CardDisplayedElement(None, self)
        self._no_card.set_position(-self._width / 2 + self._height * 1/3, - self._height / 2 + self._height / 2)
        self._no_card.hide()
        
#        self._return_animation = LinearAnimation()
#        self._return_animation.signal_frame.connect(self.set_returned)
#        self._return_animation.get_thread().start()
#        self._return_animation.set_one_by_one(True)
#        
        self._return_state = 1
        
        self._animation_card = CardDisplayedElement(None, self)
        self._animation_card.set_position(- self._width / 2 + self._height * 1/3, - self._height / 2 + self._height / 2)
        self._animation_card.hide()
        self._animation_card.setAcceptedMouseButtons(_QtCore.Qt.MouseButton.NoButton)
        self._animation_card.setAcceptHoverEvents(False)
        
        self._animation_card.setZValue(self.zValue() - 1)
        
        self._animation_above_deck = True
        
        self._no_card.signal_update.connect(self.update)
        self._animation_card.signal_update.connect(self.update)
        
        self._animation_card.setAcceptedMouseButtons(_QtCore.Qt.MouseButton.NoButton)
        self._animation_card.setAcceptHoverEvents(False)
        
        self._deck_selected = False
    
    def start_threads(self):
        self._no_card.start_threads()
        self._animation_card.start_threads()
    
    def stop_threads(self):
        self._no_card.stop_threads()
        self._animation_card.stop_threads()
    
    def deck_card(self) -> CardDisplayedElement:
        return self._no_card
    
    def animation_card(self) -> CardDisplayedElement:
        return self._animation_card
    
    def set_card(self, card: _love_letter.LoveLetterCard):
        w, h = self._width, self._height
        x, y = -w/2, -h/2
        
        self._last_card = card
        
        if card.get_character():
            self._last_displayed_card.set_character(self._animation_card.get_character())
            
            self._animation_card._character = None
            self._animation_card.set_character(card.get_character(), 0.4)
            self._animation_card.set_size(self.get_size() * 6/7)
            self._animation_card.go_to_size(self.get_size())
            self._animation_card.set_position(x + h * 1/3, y + h / 2)
            self._animation_card.go_to_position(x + w - h * 1/3, y + h / 2, 1)
            self._animation_above_deck = False
        
        else:
            self._last_displayed_card.set_character(None)
            
            self._animation_card.set_character(card.get_character(), 0.2)
            self._animation_card.set_size(self.get_size())
            self._animation_card.go_to_size(self.get_size() * 6/7)
            self._animation_card.set_position(x + w - h * 1/3, y + h / 2)
            self._animation_card.go_to_position(x + h * 1/3, y + h / 2, 0.5)
            self._animation_above_deck = True
        
    def last_card(self):
        return self._last_card
    
    def set_number(self, number: int):
        self._count = number
    
    def paint(self, painter: _QtGui.QPainter, options: _QtWidgets.QStyleOptionGraphicsItem, widget: _QtWidgets.QWidget) -> None:
        image = IMAGES_MAPPER.get_image_by_name("deck")
        
        x, y = -self._width / 2, -self._height / 2
        w, h = self._width, self._height
        
        painter.drawImage(_QtCore.QRectF(x, y, w, h), image.get_variant(""))
        
        if self._count and not (self._animation_above_deck and self._animation_card.get_position_animations()[0].isRunning()):
            self._no_card.set_position(x + h * 1/3, y + h / 2)
            self.paintChild(self._no_card, painter, options, widget)
        
        if self._last_displayed_card.get_character():
            last_card = CardDisplayedElement(self._last_displayed_card.get_character())
            last_card.set_position(x + w - h * 1/3, y + h / 2)
            last_card.set_size(h * 8/9)
            self.paintChild(last_card, painter, options, widget)
        
        if not self._animation_above_deck or self._animation_card.get_position_animations()[0].isRunning():
            self.paintChild(self._animation_card, painter, options, widget)
        
        font = _QtGui.QFont("Chomsky", int(self._width * 10/100))
        fm = _QtGui.QFontMetrics(font)
        text_width = fm.width(str(self._count))
        text_height = fm.height()
        
        font.setPointSize(int(self._width * 10/100))
        painter.setFont(font)
        
        painter.setPen(_QtGui.QColor(0xFFFFFFFF ))
        
        painter.drawText(_QtCore.QPoint(int(x + h * 1/3 - text_width/2), int(y + h/2 - text_height/2)), str(self._count))
    
    def set_size(self, size: int) -> None:
        self._width, self._height = size * 3/2 * 9/8, size * 9/8
        
        self._no_card.set_size(size)
        self._animation_card.set_size(size)
        
        self._animation_card.set_position(- self._width / 2 + self._height * 1/3, - self._height / 2 + self._height / 2)
        self._no_card.set_position(- self._width / 2 + self._height * 1/3, - self._height / 2 + self._height / 2)
        
        self.scene().update()
    
    def mousePressEvent(self, event: _QtWidgets.QGraphicsSceneMouseEvent) -> None:
        self.signal_mouse_press.emit(event)
        rect = _QtCore.QRectF(self._no_card.boundingRect())
        
        if _QtCore.QRectF(rect.x() + self._no_card.x(), rect.y() + self._no_card.y(), rect.width(), rect.height()).contains(event.pos()):
            self._no_card.mousePressEvent(event)
        
        super().mousePressEvent(event)
    
    def hoverMoveEvent(self, event: _QtWidgets.QGraphicsSceneMouseEvent) -> None:
        rect = _QtCore.QRectF(self._no_card.boundingRect())
        
        if _QtCore.QRectF(rect.x() + self._no_card.x(), rect.y() + self._no_card.y(), rect.width(), rect.height()).contains(event.pos()):
            if not self._deck_selected:
                self._no_card.hoverEnterEvent(event)
                self._deck_selected = True
        
        elif self._deck_selected:
            self._no_card.hoverLeaveEvent(event)
            self._deck_selected = False
        super().hoverMoveEvent(event)
    
    def hoverLeaveEvent(self, event: _QtWidgets.QGraphicsSceneMouseEvent) -> None:
        if self._deck_selected:
            self._no_card.hoverLeaveEvent(event)
            self._deck_selected = False
        super().hoverLeaveEvent(event)
    
    def get_size(self) -> int:
        return self._height * 8/9
    

