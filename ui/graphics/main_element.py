from PyQt5 import QtWidgets as _QtWidgets
from PyQt5 import QtGui as _QtGui
from PyQt5 import QtCore as _QtCore

from .element import *

class MainDisplayedElement(GameDisplayedElement):
    def __init__(self, parent=None):
        super().__init__(0, 0, 0, 0)
        
        self._size = 150
        
        self.setAcceptHoverEvents(False)
        self.setAcceptedMouseButtons(_QtCore.Qt.MouseButton.NoButton)
    
    def paint(self, painter: _QtGui.QPainter, options: _QtWidgets.QStyleOptionGraphicsItem, widget: _QtWidgets.QWidget) -> None:
        image_name = "background"
        image = IMAGES_MAPPER.get_image_by_name(image_name).get_variant('dark')
        
        x = 0
        while x - self._size <= self._width / 2:
            y = 0
            while y - self._size <= self._height / 2:
                painter.drawImage(_QtCore.QRectF(x, y, self._size, self._size), image)
                painter.drawImage(_QtCore.QRectF(-x-self._size, y, self._size, self._size), image)
                painter.drawImage(_QtCore.QRectF(x, -y-self._size, self._size, self._size), image)
                painter.drawImage(_QtCore.QRectF(-x-self._size, -y-self._size, self._size, self._size), image)
                y += self._size
            x += self._size
    
    def set_rect(self, x: float, y: float, w: float, h: float) -> None:
        self._x = 0
        self._y = 0
        self._width = w
        self._height = h
    
