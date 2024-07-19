from PyQt5 import QtWidgets as _QtWidgets
from PyQt5 import QtGui as _QtGui
from PyQt5 import QtCore as _QtCore

from ...resources import *

import typing as _T
import events as _events

class GameDisplayedElement(_QtWidgets.QGraphicsObject):
    
    def __init__(self, resources: Resources, x: int, y: int, width: int, height: int, parent = None):
        super().__init__(parent)
        
        self._width: int = width
        self._height: int = height
        
        self.setX(x)
        self.setY(y)
        
        self.setAcceptHoverEvents(True)
        self.setAcceptedMouseButtons(_QtCore.Qt.MouseButton.AllButtons)
        
        self.setZValue(50)
        
        self._resources = resources

        self._events = _events.EventObject(
            "hover_enter", 
            "hover_leave",
            "hover_move",
            "mouse_press",
            "mouse_release",
            "update",
            "key_press"
        )
    
    def get_events(self) -> _events.EventObject:
        return self._events
        
    def get_resources(self) -> Resources:
        return self._resources
    
    def set_resources(self, resources: Resources) -> None:
        self._resources = resources
    
    def start_threads(self) -> None:
        pass
    
    def stop_threads(self) -> None:
        pass
    
    def paint(self, painter: _QtGui.QPainter, options: _QtWidgets.QStyleOptionGraphicsItem, widget: _QtWidgets.QWidget) -> None:
        return
        painter.setPen(0xFFFFFF)
        painter.drawRect(self.boundingRect())
        
    def boundingRect(self) -> _QtCore.QRectF:
        x = -self._width / 2
        y = -self._height / 2
        
        return _QtCore.QRectF(int(x), int(y), int(self._width), int(self._height))
    
    def hoverEnterEvent(self, event) -> None:
        super().hoverEnterEvent(event)
        self._events["hover_enter"].emit(event)
    
    def hoverLeaveEvent(self, event) -> None:
        self._events["hover_leave"].emit(event)
        super().hoverLeaveEvent(event)
    
    def mousePressEvent(self, event) -> None:
        self._events["mouse_press"].emit(event)
        super().mousePressEvent(event)
    
    def mouseReleaseEvent(self, event) -> None:
        self._events["mouse_release"].emit(event)
        super().mouseReleaseEvent(event)
    
    def keyPressEvent(self, event):
        self._events["key_press"].emit(event)
        super().keyPressEvent(event)
    
    def update(self):
        super().update()

        self._events["update"].emit()
        
        if self.parent() is not None:
            self.parent().update()
        
        elif self.scene() is not None:
            self.scene().update()
    
    def applyEffectToImage(self, src: _QtGui.QImage, effect: _QtWidgets.QGraphicsEffect, extent: int = 0) -> _QtGui.QImage:
        scene = _QtWidgets.QGraphicsScene()
        item = _QtWidgets.QGraphicsPixmapItem()
        item.setPixmap(_QtGui.QPixmap.fromImage(src))
        item.setGraphicsEffect(effect)
        scene.addItem(item)
        res = _QtGui.QImage(src.size() + _QtCore.QSize(extent*2, extent*2), _QtGui.QImage.Format.Format_ARGB32)
        res.fill(_QtCore.Qt.GlobalColor.transparent)
        ptr = _QtGui.QPainter(res)
        scene.render(ptr, _QtCore.QRectF(), _QtCore.QRectF( -extent, -extent, src.width()+extent*2, src.height()+extent*2 ) )
        ptr.end()
        return res
    
    def set_position(self, x: int, y: int) -> None:
        self.setX(x)
        self.setY(y)
        self.update()
    
    def set_position_x(self, x: int) -> None:
        self.setX(x)
        self.update()
    
    def set_position_y(self, y: int) -> None:
        self.setY(y)
        self.update()
    
    def paintChild(self, child: 'GameDisplayedElement', painter: _QtGui.QPainter, options: _QtWidgets.QStyleOptionGraphicsItem, widget: _QtWidgets.QWidget) -> None:
        transform = painter.transform()
        
        child_transform = child.transform()
        
        child_transform.setMatrix( 
            child_transform.m11(), child_transform.m12(), child_transform.m13(),
            child_transform.m21(), child_transform.m22(), child_transform.m23(), 
            transform.m31() + child.x(), transform.m32() + child.y(), transform.m33(), 
        )
        painter.setTransform(child_transform)
        child.paint(painter, options, widget)
        painter.setTransform(transform)
    
    def shape(self):
        path = _QtGui.QPainterPath()
        path.addRect(self.boundingRect())
        return path

