from PyQt5 import QtWidgets as _QtWidgets
from PyQt5 import QtGui as _QtGui
from PyQt5 import QtCore as _QtCore

from .element import *

from ..resources import *
from ..background_threads.exponential_animation import *

class TextInputDisplayedElement(GameDisplayedElement):
    def __init__(self, text: str, parent = None):
        super().__init__(0, 0, 250, 50, parent)
        
        FONTS_MAPPER.require_font("Chomsky")
        
        self._text = text
        
        self._size_animation = ExponentialAnimation()
        self._size_animation.signal_frame.connect(self.set_size)
        self._size_animation.set_one_by_one(False)
        
        self.setFlags(self.GraphicsItemFlag.ItemAcceptsInputMethod | self.GraphicsItemFlag.ItemIsFocusable | self.GraphicsItemFlag.ItemIsMovable)
    
    def set_text(self, text: str) -> None:
        self._text = text
        self.prepareGeometryChange()
    
    def get_text(self) -> str:
        return self._text
    
    def start_threads(self):
        self._size_animation.get_thread().start()
    
    def paint(self, painter: _QtGui.QPainter, options: _QtWidgets.QStyleOptionGraphicsItem, widget: _QtWidgets.QWidget) -> None:
        r = self.boundingRect()
        w, h = r.width(), r.height()
        x, y = r.x() + w/2, r.y() + h/2
        
        painter.setBrush(_QtGui.QColor(0x3E070C))
        painter.setPen(_QtGui.QColor.fromRgba(0))
        painter.drawRect(self.boundingRect())
        
        painter.setBrush(_QtGui.QColor(0x7D0F19))
        painter.setPen(_QtGui.QColor.fromRgba(0))
        painter.drawRect(_QtCore.QRect(int(r.x() + h/10), int(r.y() + h/10), int(w - h * 2/10), int(h * 8/10)))
        
        font = _QtGui.QFont("Chomsky", int(self._height / 3))
        fm = _QtGui.QFontMetrics(font)
        text_width = fm.width(self._text)
        text_height = fm.height()
        
        font.setPointSize(int(self._height / 3))
        painter.setFont(font)
        
        painter.setPen(_QtGui.QColor(0xFFFFFFFF))
        painter.drawText(_QtCore.QPoint(int(x - text_width/2), int(y + text_height/4)), self._text)
        
        if self.hasFocus():
            painter.setBrush(_QtGui.QColor.fromRgba(0))
            painter.drawRect(self.boundingRect())
        
    def set_size(self, size: int) -> None:
        self._height = size
        self.update()
    
    def get_size(self):
        return self._height
    
    def boundingRect(self) -> _QtCore.QRectF:
        font = _QtGui.QFont("Chomsky", int(self._height / 3))
        fm = _QtGui.QFontMetrics(font)
        text_height = fm.height()
        text_width = fm.width(self._text)
        
        button_width = text_width + 2*text_height
        
        return _QtCore.QRectF( - button_width/2, -text_height/2, button_width, text_height*3)
    
    def set_position(self, x: int, y: int) -> None:
        self._x = x
        self._y = y
        self.update()
    
    def go_to_size(self, size: int, time: float = 0.3) -> None:
        self._size_animation.start_transition(self.get_size(), size, time)
    

