from PyQt5 import QtWidgets as _QtWidgets, uic as _uic
from PyQt5 import QtCore as _QtCore
from PyQt5 import QtGui as _QtGui

from .graphic_layers import *
from .graphic_layers.graphics.main_element import *
from .graphic_layers.graphics.mouse import *

import love_letter as _love_letter
import typing as _T
import darkdetect as _dark_detect

class GameWidget(_QtWidgets.QGraphicsView):
    def __init__(self, resources: Resources):
        super().__init__()
        
        self._resources = resources
    
        self._scene: _QtWidgets.QGraphicsScene = _QtWidgets.QGraphicsScene()
        
        self.setScene(self._scene)
        
        self._main_graphic = MainDisplayedElement(resources)
        self._main_graphic.setZValue(0)
        self._scene.addItem(self._main_graphic)
        
        self._mouse = MouseDisplayedElement(resources)
        self._mouse.set_size(40)
        
        self._mouse.setZValue(1000)
        
        self._scene.addItem(self._mouse)
        
        self.setMouseTracking(True)
        self.setInteractive(True)
        
        self.setVerticalScrollBarPolicy(_QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.setHorizontalScrollBarPolicy(_QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        
        self._layer: _T.Optional[GraphicLayer] = None
        
    def onShow(self) -> None:
        self.resizeEvent()
    
    def get_resources(self) -> Resources:
        return self._resources
    
    def set_resources(self, resources: Resources) -> None:
        self._resources = resources
        if self._layer:
            self._layer.set_resources(resources)
        
        self._main_graphic.set_resources(resources)
        self._mouse.set_resources(resources)
    
    def displayLayer(self, layer: GraphicLayer) -> None:
        if self._layer:
            for item in self._layer.get_items():
                self._scene.removeItem(item)
                
                item.stop_threads()
        
        for item in layer.get_items():
            self._scene.addItem(item)
            
            item.start_threads()
        
        self._layer = layer
        self._layer.set_resources(self._resources)
        
        w, h = self.width() - 2, self.height() - 2
        self._layer.set_rect(-w / 2, -h / 2, w, h)
    
    def resizeEvent(self, event = None) -> None:
        w, h = self.width() - 2, self.height() - 2
        
        self.setSceneRect(-w / 2, -h / 2, w, h)
        self._main_graphic.set_rect(-w / 2, -h / 2, w, h)
        
        if self._layer is not None:
            self._layer.set_rect(-w / 2, -h / 2, w, h)
    
    def mouseMoveEvent(self, event: _QtGui.QMouseEvent) -> None:
        super().mouseMoveEvent(event)
        
        position: _QtCore.QPointF = event.pos()
        
        position.setX(int(position.x() - self.width() / 2))
        position.setY(int(position.y() - self.height() / 2))
        
        event.ignore()
        
        x, y = position.x(), position.y()
        self._mouse.set_position(x, y)
        
