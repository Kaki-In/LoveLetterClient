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
        
        blur_effect = _QtWidgets.QGraphicsBlurEffect()
        blur_effect.setBlurRadius(20)
        blur_effect.setBlurHints(blur_effect.BlurHint.AnimationHint)
        
        image_name = "background"
        self._background_image = self.applyEffectToImage(IMAGES_MAPPER.get_image_by_name(image_name).get_variant('dark'), blur_effect)
        
#        self.setGraphicsEffect(blur_effect)
        
    
    def paint(self, painter: _QtGui.QPainter, options: _QtWidgets.QStyleOptionGraphicsItem, widget: _QtWidgets.QWidget) -> None:
        image = self._background_image
        
        cx = self._width/2
        cy = self._height/2
        
        x = 0
        while x - self._size <= self._width / 2:
            y = 0
            while y - self._size <= self._height / 2:
                painter.drawImage(_QtCore.QRectF(cx + x, cy + y, self._size + 2, self._size + 2), image)
                painter.drawImage(_QtCore.QRectF(cx-x-self._size, cy + y, self._size + 2, self._size + 2), image)
                painter.drawImage(_QtCore.QRectF(cx + x, cy-y-self._size, self._size + 2, self._size + 2), image)
                painter.drawImage(_QtCore.QRectF(cx-x-self._size, cy-y-self._size, self._size + 2, self._size + 2), image)
                y += self._size
            x += self._size
    
    def boundingRect(self) -> _QtCore.QRectF:
        return _QtCore.QRectF(self.x(), self.y(), self._width * 2, self._height * 2)
    
    def set_rect(self, x: float, y: float, w: float, h: float) -> None:
        self.setX(x)
        self.setY(y)
        
        self._width = w
        self._height = h
        
        self.prepareGeometryChange()
    
