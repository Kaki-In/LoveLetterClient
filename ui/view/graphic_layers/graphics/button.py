from PyQt5 import QtWidgets as _QtWidgets
from PyQt5 import QtGui as _QtGui
from PyQt5 import QtCore as _QtCore

from .element import *

from ....resources import *
from ....background_threads.exponential_animation import *

class ButtonDisplayedElement(GameDisplayedElement):
    def __init__(self, text: str, parent = None):
        super().__init__(0, 0, 50, 50, parent)
        
        FONTS_MAPPER.require_font("Chomsky")
        
        self._text = text
        
        self._enabled = True
        
        self._size_animation = ExponentialAnimation()
        self._size_animation.signal_frame.connect(self.set_size)
        self._size_animation.set_one_by_one(False)
        
        self._ratio_animation = ExponentialAnimation()
        self._ratio_animation.signal_frame.connect(self.set_ratio)
        self._ratio_animation.set_one_by_one(False)
        
        self._ratio = 1
    
    def start_threads(self):
        self._size_animation.get_thread().start()
        self._ratio_animation.get_thread().start()
    
    def stop_threads(self):
        self._size_animation.stop()
        self._ratio_animation.stop()
    
    def isEnabled(self) -> bool:
        return self._enabled
    
    def enable(self) -> None:
        self._enabled = True
    
    def disable(self) -> None:
        self._enabled = False
    
    def mousePressEvent(self, event: _QtWidgets.QGraphicsSceneMouseEvent) -> None:
        super().mousePressEvent(event)
        event.accept()
    
    def paint(self, painter: _QtGui.QPainter, options: _QtWidgets.QStyleOptionGraphicsItem, widget: _QtWidgets.QWidget) -> None:
        r = self.boundingRect()
        w, h = r.width() * self._ratio, r.height() * self._ratio
        
        image = IMAGES_MAPPER.get_image_by_name('button').get_variant('')
        painter.drawImage(r, image)
        
        font = _QtGui.QFont("Chomsky", int(self._height / 3 * self._ratio))
        fm = _QtGui.QFontMetrics(font)
        text_width = fm.width(self._text)
        text_height = fm.height()
        
        font.setPointSize(int(self._height / 3 * self._ratio))
        painter.setFont(font)
        
        if self._enabled:
            painter.setPen(_QtGui.QColor(0xFFFFFFFF))
        else:
            painter.setPen(_QtGui.QColor.fromRgba(0x80FFFFFF))
        
        painter.drawText(_QtCore.QPoint( int(-text_width/2), int(text_height/4)), self._text)
        
        return
        painter.setBrush(_QtGui.QColor(0x3E070C))
        painter.setPen(_QtGui.QColor.fromRgba(0))
        painter.drawRect(self.boundingRect())
        
        painter.setBrush(_QtGui.QColor(0x7D0F19))
        painter.setPen(_QtGui.QColor.fromRgba(0))
        painter.drawRect(_QtCore.QRect(int(r.x() + h/10), int(r.y() + h/10), int(w - h * 2/10), int(h * 8/10)))
        
    def set_size(self, size: int) -> None:
        self._height = size
        self.prepareGeometryChange()
    
    def get_size(self):
        return self._height
    
    def set_ratio(self, ratio: float) -> None:
        self._ratio = ratio
        self.prepareGeometryChange()
    
    def get_ratio(self) -> float:
        return self._ratio
    
    def boundingRect(self) -> _QtCore.QRectF:
        font = _QtGui.QFont("Chomsky", int(self._height))
        fm = _QtGui.QFontMetrics(font)
        text_width = fm.width(self._text) * self._ratio
        text_height = fm.height() * self._ratio
        
        return _QtCore.QRectF(-text_width / 2, -text_height / 2, text_width, text_height)
    
    def go_to_size(self, size: int, time: float = 0.3) -> None:
        self._size_animation.start_transition(self.get_size(), size, time)
    
    def go_to_ratio(self, ratio: float, time: float = 0.3) -> None:
        self._ratio_animation.start_transition(self.get_ratio(), ratio, time)
    

