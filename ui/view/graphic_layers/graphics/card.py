from PyQt5 import QtWidgets as _QtWidgets
from PyQt5 import QtGui as _QtGui
from PyQt5 import QtCore as _QtCore

from .element import *
from ....resources.fonts import *
from ....resources.images import *
from ....background_threads import *

import love_letter as _love_letter
import typing as _T
import math as _math
import traceback as _traceback
import time as _time

class CardDisplayedElement(GameDisplayedElement):
    def __init__(self, character: _love_letter.LoveLetterCharacter, parent = None):
        self._character = character
        super().__init__(0, 0, 200, 300, parent)
        
        FONTS_MAPPER.require_font("Chomsky")
        
        self._size_animation = ExponentialAnimation()
        self._size_animation.signal_frame.connect(self.set_size)
        self._size_animation.set_one_by_one(False)
        
        self._position_animation_x = ExponentialAnimation()
        self._position_animation_x.signal_frame.connect(self.set_position_x)
        self._position_animation_x.set_one_by_one(False)
        
        self._position_animation_y = ExponentialAnimation()
        self._position_animation_y.signal_frame.connect(self.set_position_y)
        self._position_animation_y.set_one_by_one(False)
        
        self._return_animation = LinearAnimation()
        self._return_animation.signal_frame.connect(self.set_returned)
        self._return_animation.set_one_by_one(True)
        
        self._return_state = 1
        self._new_characters = []
        
    def get_character(self):
        return self._character
    
    def get_size_animation(self):
        return self._size_animation
    
    def get_position_animations(self):
        return self._position_animation_x, self._position_animation_y
    
    def get_return_animation(self):
        return self._return_animation
    
    def start_threads(self):
        self._size_animation.get_thread().start()
        self._position_animation_x.get_thread().start()
        self._position_animation_y.get_thread().start()
        self._return_animation.get_thread().start()
    
    def set_character(self, character: _love_letter.LoveLetterCharacter, time: float = 0.5):
        self._new_characters.append(character)
        self._return_animation.start_transition( -1, 1, time)
    
    def set_returned(self, value: float):
        self._return_state = value
        
        if value > 0:
            self._character = self._new_characters[0]
        if value == 1:
            c = self._new_characters.pop(0)
        
        self.update()
    
    def paint(self, painter: _QtGui.QPainter, options: _QtWidgets.QStyleOptionGraphicsItem, widget: _QtWidgets.QWidget) -> None:
        w, h = int(self._width) + 2, int(self._height) + 2
        
        character = self._character
        
        x = -w / 2
        y = -h / 2
        
        card_pixmap = _QtGui.QPixmap(w, h)
        card_pixmap.fill(_QtGui.QColor.fromRgba(0))
        
        card_painter = _QtGui.QPainter(card_pixmap)
        
        card_painter.setTransform(_QtGui.QTransform(
            _math.sin(abs(self._return_state) * _math.pi / 2)   , 0                                                 , 0,
            0                                                   , 1                                                 , 0,
            w/2                                                 , h/2                                               , 1
        ))
        
        if character is None:
            image_card = IMAGES_MAPPER.get_image_by_name("card").get_variant("back")
        
            card_painter.drawImage(_QtCore.QRectF(-w/2, -h/2, w, h), image_card)
        else:
            image_card = IMAGES_MAPPER.get_image_by_name("card").get_variant("front")
            image_name = "character_" + character.get_name().lower()
            
            blur = _QtWidgets.QGraphicsBlurEffect()
            blur.setBlurRadius(2)
            blur.setBlurHints(_QtWidgets.QGraphicsBlurEffect.BlurHint.PerformanceHint)
            
            card_painter.drawImage(_QtCore.QRectF(w * 5/100 - w/2, h * 10/100 - h/2, w * 90/100, h * 85/100), self.applyEffectToImage(IMAGES_MAPPER.get_image_by_name(image_name).get_variant('dark'), blur))
            card_painter.drawImage(_QtCore.QRectF(-w/2, -h/2, w, h), image_card)
            
            font = _QtGui.QFont("Chomsky", int(self._width * 10/100))
            fm = _QtGui.QFontMetrics(font)
            text_width = fm.width(character.get_name())
            
            font.setPointSize(int(self._width * 10/100))
            card_painter.setFont(font)
            
            card_painter.setPen(_QtGui.QColor(0xFF7D0F19))
            
            card_painter.drawText(_QtCore.QPoint(int(w * 13/100 - w/2), int(h * 11.5/100 - h/2)), str(character.get_value()))
            card_painter.drawText(_QtCore.QPoint(int(w * 56/100 - text_width / 2 - w/2), int(h * 11/100 - h/2)), str(character.get_name()))
        
        card_painter.end()
        
        painter.drawImage(_QtCore.QRectF(x, y, w, h), _QtGui.QImage(card_pixmap))
        
    
    def set_size(self, size: int) -> None:
        self._width, self._height = size * 2/3, size
        self.prepareGeometryChange()
        self.update()
    
    def go_to_size(self, size: int, time: float = 0.3) -> None:
        self._size_animation.start_transition(self.get_size(), size, time)
    
    def get_size(self) -> int:
        return self._height
    
    def go_to_position(self, x: int, y: int, time: float = 0.5) -> None:
        self._position_animation_x.start_transition(self.x(), x, time)
        self._position_animation_y.start_transition(self.y(), y, time)
    
    def stop_threads(self):
        self._size_animation.stop()
        self._position_animation_x.stop()
        self._position_animation_y.stop()

