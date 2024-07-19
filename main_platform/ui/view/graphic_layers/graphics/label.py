from PyQt5 import QtWidgets as _QtWidgets
from PyQt5 import QtGui as _QtGui
from PyQt5 import QtCore as _QtCore

from .element import *

class LabelDisplayedElement(GameDisplayedElement):
    def __init__(self, resources: Resources, text: str, size: int, parent = None):
        super().__init__(resources, 0, 0, 50, 50, parent)

        self._text = text
        self._size = size

        resources.get_fonts_mapper().require_font("Chomsky")
        
    def paint(self, painter: _QtGui.QPainter, options: _QtWidgets.QStyleOptionGraphicsItem, widget: _QtWidgets.QWidget) -> None:
        super().paint(painter, options, widget)

        br = self.boundingRect()
        width, height = br.width(), br.height()

        gradient = _QtGui.QLinearGradient(_QtCore.QPoint(int(-width/2), 0), _QtCore.QPoint(int(width/2), 0))
        gradient.setColorAt(0, _QtGui.QColor(0, 0, 0, 0))
        gradient.setColorAt(0.25, _QtGui.QColor(0, 0, 0))
        gradient.setColorAt(0.75, _QtGui.QColor(0, 0, 0))
        gradient.setColorAt(1, _QtGui.QColor(0, 0, 0, 0))

        painter.setBrush(gradient)
        painter.setPen(_QtGui.QColor(0,0,0,0))
        painter.drawRect(int(-width/2), int(-height/2), int(width), int(height))

        font = painter.font()
        font.setPointSize(int(self._size / 2))
        font.setFamily('Chomsky')
        painter.setFont(font)

        painter.setPen(_QtGui.QColor(0xFFFFFF))

        painter.drawStaticText(int(-width/4), int(-height/4), _QtGui.QStaticText(self._resources.get_translator().translate(self._text)))
    
    def set_size(self, size: int) -> None:
        self._size = int(size)
    
    def size(self) -> int:
        return self._size
    
    def boundingRect(self) -> _QtCore.QRectF:
        font = _QtGui.QFont()
        font.setPointSize(self._size)
        font.setFamily('Chomsky')

        metrics = _QtGui.QFontMetrics(font)
        width = metrics.width(self._resources.get_translator().translate(self._text))
        height = metrics.height()

        return _QtCore.QRectF(-width/2, -height/2, width, height)
    
