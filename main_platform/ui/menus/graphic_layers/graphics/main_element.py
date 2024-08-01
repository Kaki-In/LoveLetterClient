from PyQt5 import QtWidgets as _QtWidgets
from PyQt5 import QtGui as _QtGui
from PyQt5 import QtCore as _QtCore

import resources as _resources

from .element import *
from ....animations import *

class MainDisplayedElement(GameDisplayedElement):
    def __init__(self, resources: _resources.Resources, parent=None):
        super().__init__(resources, 0, 0, 0, 0)
        
        self._size = 300
        
        self.setAcceptHoverEvents(False)
        self.setAcceptedMouseButtons(_QtCore.Qt.MouseButton.NoButton)
        
        self._variant = ""
        self._last_variant = ""
        self._next_variant = ""

        self._animation_variant = ExponentialAnimation()
        self._animation_variant.set_one_by_one(True)
        self._animation_variant.signal_frame.connect(self.on_signal_frame)

        self._animation_state = 0
    
    def start_threads(self) -> None:
        self._animation_variant.get_thread().start()
    
    def stop_threads(self) -> None:
        self._animation_variant.stop()
    
    def set_variant(self, name: str, time: float = 1.) -> None:
        self._next_variant = name
        self._animation_variant.start_transition(0, 1, time)
    
    def get_variant(self) -> str:
        return self._variant
    
    def paint(self, painter: _QtGui.QPainter, options: _QtWidgets.QStyleOptionGraphicsItem, widget: _QtWidgets.QWidget) -> None:
        super().paint(painter, options, widget)
        
        cx = self._width/2
        cy = self._height/2

        last_background = self._resources.get_themes_mapper().get_image_by_name("background").get_variant(self._last_variant)
        background = self._resources.get_themes_mapper().get_image_by_name("background").get_variant(self._variant)

        if self._animation_state != 1:
            effect = _QtWidgets.QGraphicsOpacityEffect()
            effect.setOpacity(self._animation_state)

            background = self.applyEffectToImage(background, effect)
            
            x = 0
            while x - self._size <= self._width / 2:
                y = 0
                while y - self._size <= self._height / 2:
                    painter.drawImage(_QtCore.QRectF(cx + x, cy + y, self._size + 0.5, self._size + 0.5), last_background)
                    painter.drawImage(_QtCore.QRectF(cx-x-self._size, cy + y, self._size + 0.5, self._size + 0.5), last_background)
                    painter.drawImage(_QtCore.QRectF(cx + x, cy-y-self._size, self._size + 0.5, self._size + 0.5), last_background)
                    painter.drawImage(_QtCore.QRectF(cx-x-self._size, cy-y-self._size, self._size + 0.5, self._size + 0.5), last_background)
                    y += self._size
                x += self._size

        x = 0
        while x - self._size <= self._width / 2:
            y = 0
            while y - self._size <= self._height / 2:
                painter.drawImage(_QtCore.QRectF(cx + x, cy + y, self._size + 0.5, self._size + 0.5), background)
                painter.drawImage(_QtCore.QRectF(cx-x-self._size, cy + y, self._size + 0.5, self._size + 0.5), background)
                painter.drawImage(_QtCore.QRectF(cx + x, cy-y-self._size, self._size + 0.5, self._size + 0.5), background)
                painter.drawImage(_QtCore.QRectF(cx-x-self._size, cy-y-self._size, self._size + 0.5, self._size + 0.5), background)
                y += self._size
            x += self._size

    def boundingRect(self) -> _QtCore.QRectF:
        return _QtCore.QRectF(self.x(), self.y(), self._width * 2, self._height * 2)
    
    def set_rect(self, x: float, y: float, w: float, h: float) -> None:
        self.setX(x)
        self.setY(y)
        
        self._width = w
        self._height = h
        
        self._size = (w + h) / 10
        
        self.prepareGeometryChange()
    
    def on_signal_frame(self, value: float) -> None:
        self._animation_state = value
        
        if value == 0:
            self._last_variant = self._variant
            self._variant = self._next_variant
            self._next_variant = ""
        
        self.update()

