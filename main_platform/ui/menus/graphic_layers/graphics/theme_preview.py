from PyQt5 import QtWidgets as _QtWidgets
from PyQt5 import QtGui as _QtGui
from PyQt5 import QtCore as _QtCore

from .element import *
from ....animations import *

class ThemePreviewDisplayedElement(GameDisplayedElement):
    def __init__(self, resources: Resources, theme_name: str, parent = None):
        self._theme_name = theme_name
        super().__init__(resources, 0, 0, 20, 20, parent)

        self._theme = resources.get_images_mapper().get_theme(theme_name)
        
    def paint(self, painter: _QtGui.QPainter, options: _QtWidgets.QStyleOptionGraphicsItem, widget: _QtWidgets.QWidget) -> None:
        super().paint(painter, options, widget)

        r = self.boundingRect()
        x, y = r.x(), r.y()
        w, h = r.width(), r.height()

        painter.setBrush(_QtGui.QColor(0, 0, 0, 127))
        painter.setPen(_QtGui.QColor(0, 0, 0, 0))
        painter.drawRoundedRect(self.boundingRect(), self._height/4, self._height/4)

        painter.drawImage(_QtCore.QRectF(x+h/4, y+h/4, w-h/2,h-h/2), self._image)

    def set_size(self, size: int) -> None:
        self._width, self._height = size, size
        self.prepareGeometryChange()
        self.update()
    
    def mousePressEvent(self, event) -> None:
        super().mousePressEvent(event)
        event.accept()
    
    def mouseReleaseEvent(self, event) -> None:
        super().mouseReleaseEvent(event)

    