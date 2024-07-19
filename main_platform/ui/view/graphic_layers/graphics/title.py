from PyQt5 import QtWidgets as _QtWidgets
from PyQt5 import QtGui as _QtGui
from PyQt5 import QtCore as _QtCore

from .element import *

from ....background_threads.exponential_animation import *

class GameTitleDisplayedElement(GameDisplayedElement):
    def __init__(self, resources, parent = None):
        super().__init__(resources, 0, 0, 50, 50, parent)
        
        self._size_animation = ExponentialAnimation()
        self._size_animation.signal_frame.connect(self.set_size)
        self._size_animation.set_one_by_one(False)
        
        self._position_animation_x = ExponentialAnimation()
        self._position_animation_x.signal_frame.connect(self.set_position_x)
        self._position_animation_x.set_one_by_one(False)
        
        self._position_animation_y = ExponentialAnimation()
        self._position_animation_y.signal_frame.connect(self.set_position_y)
        self._position_animation_y.set_one_by_one(False)
        
        self.setAcceptHoverEvents(False)
        self.setAcceptedMouseButtons(_QtCore.Qt.MouseButton.NoButton)
        
    def paint(self, painter: _QtGui.QPainter, options: _QtWidgets.QStyleOptionGraphicsItem, widget: _QtWidgets.QWidget) -> None:
        super().paint(painter, options, widget)
        w, h = self._width, self._height
        x, y = - w/2, - h/2
        
        image_name = "game_title"
        
        painter.drawImage(_QtCore.QRectF(x, y, self._width, self._height), self._resources.get_images_mapper().get_image_by_name(image_name).get_default())
    
    def get_size(self) -> int:
        return self._height
    
    def set_size(self, size: int) -> None:
        self._width, self._height = size *4/2.10, size
        self.prepareGeometryChange()
    
    def go_to_size(self, size: int, time: float = 0.3) -> None:
        self._size_animation.start_transition(self.get_size(), size, time)
    
    def go_to_position(self, x: int, y: int, time: float = 0.5) -> None:
        self._position_animation_x.start_transition(self.x(), x, time)
        self._position_animation_y.start_transition(self.y(), y, time)
    
    def start_threads(self):
        self._size_animation.get_thread().start()
        self._position_animation_x.get_thread().start()
        self._position_animation_y.get_thread().start()
    
    def stop_threads(self):
        self._size_animation.stop()
        self._position_animation_x.stop()
        self._position_animation_y.stop()

