from PyQt5 import QtWidgets as _QtWidgets
from PyQt5 import QtGui as _QtGui
from PyQt5 import QtCore as _QtCore

from .element import *

from ....resources.images import *

class MouseDisplayedElement(GameDisplayedElement):
    def __init__(self, parent = None):
        super().__init__(0, 0, 50, 50, parent)
        
        self.setAcceptHoverEvents(False)
        self.setAcceptedMouseButtons(_QtCore.Qt.MouseButton.NoButton)
        
    def paint(self, painter: _QtGui.QPainter, options: _QtWidgets.QStyleOptionGraphicsItem, widget: _QtWidgets.QWidget) -> None:
        image_name = "mouse"
        painter.drawImage(_QtCore.QRectF(0, 0, self._width, self._height), IMAGES_MAPPER.get_image_by_name(image_name).get_variant('dark'))
    
    def set_size(self, size: int) -> None:
        self._width, self._height = size, size
        self.prepareGeometryChange()
    
    def boundingRect(self) -> _QtCore.QRectF:
        return _QtCore.QRectF(0, 0, self._width, self._height)
    
