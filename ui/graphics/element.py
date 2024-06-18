from PyQt5 import QtWidgets as _QtWidgets
from PyQt5 import QtGui as _QtGui
from PyQt5 import QtCore as _QtCore

import typing as _T
import events as _events

from ..resources.images import *

class GameDisplayedElement(_QtWidgets.QGraphicsObject):
    
    signal_hover_enter = _QtCore.pyqtSignal(_QtWidgets.QGraphicsSceneHoverEvent)
    signal_hover_leave = _QtCore.pyqtSignal(_QtWidgets.QGraphicsSceneHoverEvent)
    signal_hover_move = _QtCore.pyqtSignal(_QtWidgets.QGraphicsSceneHoverEvent)
    
    signal_mouse_press = _QtCore.pyqtSignal(_QtWidgets.QGraphicsSceneMouseEvent)
    
    signal_update = _QtCore.pyqtSignal()
    
    z_value = 0
    
    def __init__(self, x: int, y: int, width: int, height: int, parent = None):
        super().__init__(parent)
        
        self._width: int = width
        self._height: int = height
        self._x: int = x
        self._y: int = y
        
        self.setZValue(self.z_value)
        self.z_value += 1
        
        self.setAcceptHoverEvents(True)
        self.setAcceptedMouseButtons(_QtCore.Qt.MouseButton.AllButtons)
        
    def paint(self, painter: _QtGui.QPainter, options: _QtWidgets.QStyleOptionGraphicsItem, widget: _QtWidgets.QWidget) -> None:
        pass
    
    def boundingRect(self) -> _QtCore.QRectF:
        x = self._x - self._width / 2
        y = self._y - self._height / 2
        
        return _QtCore.QRectF(int(x), int(y), int(self._width), int(self._height))
    
    def hoverEnterEvent(self, event) -> None:
        self.signal_hover_enter.emit(event)
    
    def hoverLeaveEvent(self, event) -> None:
        self.signal_hover_leave.emit(event)
    
    def mousePressEvent(self, event) -> None:
        self.signal_mouse_press.emit(event)
    
    def update(self):
        self.signal_update.emit()
        
        if self.scene() is not None:
            self.scene().update()
        
        elif self.parent() is not None:
            self.parent().update()
    
