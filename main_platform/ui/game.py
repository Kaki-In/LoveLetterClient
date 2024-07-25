from PyQt5 import QtWidgets as _QtWidgets, uic as _uic
from PyQt5 import QtCore as _QtCore
from PyQt5 import QtGui as _QtGui

from .menus import *
from .menus.graphic_layers.graphics.main_element import *
from .menus.graphic_layers.graphics.mouse import *

import resources as _resources
import os as _os
import typing as _T

class GameWidget(_QtWidgets.QGraphicsView):
    def __init__(self):
        super().__init__()
        
        self._resources = _resources.Resources(_os.environ['HOME'] + _os.sep + ".love_letter" + _os.sep + "resources")

        icon = _QtGui.QIcon(_QtGui.QPixmap(self._resources.get_images_mapper().get_image_by_name("icon").get_variant("64")))
        self.setWindowIcon(icon)
        
        self._resources.get_images_mapper().set_theme_name('cartoon')
    
        self._scene: _QtWidgets.QGraphicsScene = _QtWidgets.QGraphicsScene()
        
        self.setScene(self._scene)
        
        self._main_graphic = MainDisplayedElement(self._resources)
        self._main_graphic.setZValue(0)
        self._main_graphic.start_threads()
        self._scene.addItem(self._main_graphic)
        
        self._mouse = MouseDisplayedElement(self._resources)
        self._mouse.set_size(40)
        
        self._mouse.setZValue(1000)
        
        self._scene.addItem(self._mouse)
        
        self.setMouseTracking(True)
        self.setInteractive(True)

        self.setCursor(_QtCore.Qt.CursorShape.BlankCursor)
        
        self.setVerticalScrollBarPolicy(_QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.setHorizontalScrollBarPolicy(_QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

        self._animation_display = ExponentialAnimation()
        self._animation_display.set_one_by_one(True)
        self._animation_display.signal_frame.connect(self.on_animation_frame)
        self._animation_display.thread().start()
        
        self._layer: _T.Optional[GraphicLayer] = None
        self._last_layer: _T.Optional[GraphicLayer] = None
        self._next_layer: _T.Optional[GraphicLayer] = None

    def set_title(self, title: str) -> None:
        self.setWindowTitle(title)
    
    def get_title(self) -> None:
        return self.windowTitle()
    
    def set_full_screen_mode(self, enabled: bool) -> None:
        if enabled:
            self.showFullScreen()
        else:
            self.show()
    
    def onShow(self) -> None:
        self.resizeEvent()
    
    def get_resources(self) -> _resources.Resources:
        return self._resources
    
    def set_resources(self, resources: _resources.Resources) -> None:
        self._resources = resources

        if self._layer:
            self._layer.set_resources(resources)
        
        self._main_graphic.set_resources(resources)
        self._mouse.set_resources(resources)
    
    def on_animation_frame(self, position: float) -> None:
        if position == 0:
            self._last_layer = self._layer
            self._layer = self._next_layer
            self._next_layer = None

            for item in self._layer.get_items():
                self._scene.addItem(item)

            self._layer.set_resources(self._resources)
        

        w, h = self.width() - 2, self.height() - 2
        
        if self._layer is not None:
            if position > 0:
                self._layer.set_rect(w / 2 - w*position, -h / 2, w, h)
            else:
                self._layer.set_rect(- 3*w / 2 - w*position, -h / 2, w, h)
        
        if self._last_layer is not None:
            self._last_layer.set_rect(-w / 2 - w*position, -h / 2, w, h)
        
        if abs(position) == 1:
            if self._last_layer:
                for item in self._last_layer.get_items():
                    self._scene.removeItem(item)
    
    def displayLayer(self, layer: GraphicLayer, new_layer: bool) -> None:
        if new_layer:
            self._animation_display.start_transition(0, 1, 1)
        else:
            self._animation_display.start_transition(0, -1, 1)
        
        self._main_graphic.set_variant(layer.background_variant())
        
        self._next_layer = layer
    
    def resizeEvent(self, event = None) -> None:
        w, h = self.width() - 2, self.height() - 2
        
        self.setSceneRect(-w / 2, -h / 2, w, h)
        self._main_graphic.set_rect(-w / 2, -h / 2, w, h)
        
        if self._layer is not None and not self._animation_display.isRunning():
            self._layer.set_rect(-w / 2, -h / 2, w, h)
    
    def mouseMoveEvent(self, event: _QtGui.QMouseEvent) -> None:
        super().mouseMoveEvent(event)
        
        position: _QtCore.QPointF = event.pos()
        
        position.setX(int(position.x() - self.width() / 2))
        position.setY(int(position.y() - self.height() / 2))
        
        event.ignore()
        
        x, y = position.x(), position.y()
        self._mouse.set_position(x, y)
        
