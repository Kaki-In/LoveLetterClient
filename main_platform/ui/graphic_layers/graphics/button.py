from PyQt5 import QtWidgets as _QtWidgets
from PyQt5 import QtGui as _QtGui
from PyQt5 import QtCore as _QtCore

import resources as _resources

from .element import *

from .animations import *

class ButtonDisplayedElement(GameDisplayedElement):
    def __init__(self, resources: _resources.Resources, text: str, parent = None):
        super().__init__(resources, 0, 0, 50, 50, parent)
        
        self._resources.get_fonts_mapper().require_font("Chomsky")
        
        self._text = text

        self._size = 0
        
        self._enabled = True
        
        self._size_animation = ExponentialAnimation()
        self._size_animation.signal_frame.connect(self.set_size)
        self._size_animation.set_one_by_one(False)
        
        self._ratio_animation = ExponentialAnimation()
        self._ratio_animation.signal_frame.connect(self.set_ratio)
        self._ratio_animation.set_one_by_one(False)
        
        self._ratio = 1
    
    def start_threads(self):
        self._size_animation.get_thread().start()
        self._ratio_animation.get_thread().start()
    
    def stop_threads(self):
        self._size_animation.stop()
        self._ratio_animation.stop()
    
    def isEnabled(self) -> bool:
        return self._enabled
    
    def enable(self) -> None:
        self._enabled = True
        self.update()
    
    def disable(self) -> None:
        self._enabled = False
        self.update()
    
    def mousePressEvent(self, event: _QtWidgets.QGraphicsSceneMouseEvent) -> None:
        if self._enabled:
            super().mousePressEvent(event)
            event.accept()
        else:
            event.ignore()
    
    def paint(self, painter: _QtGui.QPainter, options: _QtWidgets.QStyleOptionGraphicsItem, widget: _QtWidgets.QWidget) -> None:
        super().paint(painter, options, widget)

        text = self._resources.get_translator().translate(self._text)

        palette = self._resources.get_themes_mapper().get_palette().get_sub_palette('graphics').get_palette('button')

        if self._size < 3 / self._ratio:
            return
        
        r = self.boundingRect()
        w, h = r.width() - self._size * self._ratio, r.height() - self._size * self._ratio * 4/5
        
        painter.drawImage(r, self._resources.get_themes_mapper().get_image_by_name('button').get_default())

        font = _QtGui.QFont("Chomsky", 500)
        fm = _QtGui.QFontMetrics(font)
        
        text_width = fm.width(text)
        text_height = fm.height()
        
        image_format = w / h
        text_format = text_width / text_height

        if image_format < text_format:
            width = w
            height = width / text_format
        else:
            height = h
            width = text_format * height

        font.setPointSizeF(500 / text_height * height)
        painter.setFont(font)

        fm = _QtGui.QFontMetrics(font)
        
        width = fm.width(text)
        height = fm.height()

        color = _QtGui.QColor(palette.get_color('text'))

        if not self._enabled:
            color.setAlpha(128)

        painter.setPen(color)
        
        painter.drawText(_QtCore.QPoint( int(-width/2), int(height/4)), text)
        
    def set_size(self, size: int) -> None:
        self._size = size
        self.prepareGeometryChange()
    
    def get_size(self):
        return self._size
    
    def set_ratio(self, ratio: float) -> None:
        self._ratio = ratio
        self.prepareGeometryChange()
    
    def get_ratio(self) -> float:
        return self._ratio
    
    def boundingRect(self) -> _QtCore.QRectF:
        image = self._resources.get_themes_mapper().get_image_by_name('button').get_default()
        image_format = image.width() / image.height()

        font = _QtGui.QFont("Chomsky", int(self._size * self._ratio))
        fm = _QtGui.QFontMetrics(font)

        text_width = fm.width(self._text)
        text_height = fm.height()

        text_format = text_width / text_height

        if image_format < text_format:
            height = text_height
            width = image_format * height
        else:
            width = text_width
            height = width / image_format
        
        return _QtCore.QRectF(-width / 2, -height / 2, width, height)
    
    def go_to_size(self, size: int, time: float = 0.3) -> None:
        self._size_animation.start_transition(self.get_size(), size, time)
    
    def go_to_ratio(self, ratio: float, time: float = 0.3) -> None:
        self._ratio_animation.start_transition(self.get_ratio(), ratio, time)
    

