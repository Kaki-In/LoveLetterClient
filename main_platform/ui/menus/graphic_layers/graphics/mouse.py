from PyQt5 import QtWidgets as _QtWidgets
from PyQt5 import QtGui as _QtGui
from PyQt5 import QtCore as _QtCore

import resources as _resources

from .element import *

class MouseDisplayedElement(GameDisplayedElement):
    def __init__(self, resources: _resources.Resources, parent = None):
        super().__init__(resources, 0, 0, 50, 50, parent)
        
        self.setAcceptHoverEvents(False)
        self.setAcceptedMouseButtons(_QtCore.Qt.MouseButton.NoButton)
        
    def paint(self, painter: _QtGui.QPainter, options: _QtWidgets.QStyleOptionGraphicsItem, widget: _QtWidgets.QWidget) -> None:
        super().paint(painter, options, widget)
        image_name = "mouse"
        painter.drawImage(_QtCore.QRectF(0, 0, self._width, self._height), self._resources.get_themes_mapper().get_image_by_name(image_name).get_default())
    
    def set_size(self, size: int) -> None:
        self._width, self._height = size, size
        self.prepareGeometryChange()
    
    def boundingRect(self) -> _QtCore.QRectF:
        return _QtCore.QRectF(0, 0, self._width, self._height)
    
