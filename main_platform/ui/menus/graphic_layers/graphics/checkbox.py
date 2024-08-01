from PyQt5 import QtWidgets as _QtWidgets
from PyQt5 import QtGui as _QtGui
from PyQt5 import QtCore as _QtCore

import resources as _resources
import typing as _T

from ....animations.exponential_animation import *

from .element import *

class CheckBoxDisplayedElement(GameDisplayedElement):
    def __init__(self, resources: _resources.Resources, text: _T.Optional[str], size: int, parent = None):
        super().__init__(resources, 0, 0, 50, 50, parent)

        self._text = text
        self._size = size
        self._enabled = False
        self._value = 0

        self._animation_dot_color = ExponentialAnimation()
        self._animation_dot_color.signal_frame.connect(self.on_animation_frame)

        resources.get_fonts_mapper().require_font("Chomsky")
    
    def start_threads(self) -> None:
        self._animation_dot_color.thread().start()
    
    def stop_thread(self) -> None:
        self._animation_dot_color.stop()
    
    def mousePressEvent(self, event: _QtWidgets.QGraphicsSceneMouseEvent) -> None:
        super().mousePressEvent(event)
        event.accept()
    
    def on_animation_frame(self, percent: float) -> None:
        self._value = percent
        self.update()
        
    def paint(self, painter: _QtGui.QPainter, options: _QtWidgets.QStyleOptionGraphicsItem, widget: _QtWidgets.QWidget) -> None:
        super().paint(painter, options, widget)
        
        palette = self._resources.get_themes_mapper().get_palette().get_sub_palette('graphics').get_palette('checkbox')

        br = self.boundingRect()
        width, height = br.width(), br.height()

        painter.setPen(_QtGui.QColor.fromRgba(0))

        border_color = palette.get_color('border')
        red, green, blue, alpha = border_color.getRgb()
        border_grey = border_color.value()
        painter.setBrush(_QtGui.QColor(int(border_grey + (red - border_grey) * self._value), int(border_grey + (green - border_grey) * self._value), int(border_grey + (blue - border_grey) * self._value)))

        painter.drawRoundedRect(_QtCore.QRectF(0, -height/2, height * 2, height), height/2, height/2)

        painter.setBrush(palette.get_color('background'))
        painter.drawRoundedRect(_QtCore.QRectF(height/4, -height/4, height * 3/2, height/2), height/4, height/4)

        x = height * 3/8 + height * self._value
        
        dot_color = palette.get_color('dot')
        red, green, blue, alpha = dot_color.getRgb()
        dot_grey = border_color.value()
        painter.setBrush(_QtGui.QColor(int(dot_grey + (red - dot_grey) * self._value), int(dot_grey + (green - dot_grey) * self._value), int(dot_grey + (blue - dot_grey) * self._value)))
        
        painter.drawRoundedRect(_QtCore.QRectF(x, -height/8, height/4, height/4), height/8, height/8)

        font = painter.font()
        font.setPointSize(int(self._size))
        font.setFamily('Chomsky')
        painter.setFont(font)

        painter.setPen(palette.get_color('text'))

        painter.drawStaticText(int(height * 5/2), int(-height/2), _QtGui.QStaticText(self._resources.get_translator().translate(self._text)))
    
    def set_font_size(self, size: int) -> None:
        self._size = int(size)
        self._width = size
        self._height = size
    
    def font_size(self) -> int:
        return self._size
    
    def is_enabled(self) -> bool:
        return self._enabled
    
    def enable(self) -> None:
        self._enabled = True
        self._animation_dot_color.start_transition(self._value, 1, 0.25)
    
    def disable(self) -> None:
        self._enabled = False
        self._animation_dot_color.start_transition(self._value, 0, 0.25)
    
    def set_enabled(self, value: bool) -> None:
        if value:
            self.enable()
        else:
            self.disable()
    
    def boundingRect(self) -> _QtCore.QRectF:
        font = _QtGui.QFont()
        font.setPointSize(self._size)
        font.setFamily('Chomsky')

        metrics = _QtGui.QFontMetrics(font)
        width = metrics.width(self._resources.get_translator().translate(self._text))
        height = metrics.height()

        return _QtCore.QRectF(0, -height/2, height * 5/2 + width, height)
    
