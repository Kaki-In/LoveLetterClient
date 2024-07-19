from PyQt5 import QtWidgets as _QtWidgets
from PyQt5 import QtGui as _QtGui
from PyQt5 import QtCore as _QtCore

from .element import *
from ....animations import *

class IconButtonDisplayedElement(GameDisplayedElement):
    def __init__(self, resources: Resources, icon_name: str, parent = None):
        self._icon = icon_name
        self._ratio = 1
        super().__init__(resources, 0, 0, 20, 20, parent)

        self._ratio_animation = ExponentialAnimation()
        self._ratio_animation.signal_frame.connect(self.set_ratio)
        self._ratio_animation.set_one_by_one(False)

        self._title = ""
        resources.get_fonts_mapper().require_font("Chomsky")
        
        self._image = resources.get_images_mapper().get_image_by_name(icon_name).get_variant("icon")
    
    def set_title(self, title: str) -> None:
        self._title = title
    
    def get_title(self) -> str:
        return self._title
        
    def start_threads(self):
        self._ratio_animation.get_thread().start()
    
    def stop_threads(self):
        self._ratio_animation.stop()
    
    def paint(self, painter: _QtGui.QPainter, options: _QtWidgets.QStyleOptionGraphicsItem, widget: _QtWidgets.QWidget) -> None:
        super().paint(painter, options, widget)

        r = self.boundingRect()
        x, y = r.x(), r.y()
        w, h = r.width(), r.height()

        painter.setBrush(_QtGui.QColor(0, 0, 0, 127))
        painter.setPen(_QtGui.QColor(0, 0, 0, 0))
        painter.drawRoundedRect(self.boundingRect(), self._height/4, self._height/4)

        painter.drawImage(_QtCore.QRectF(-h/4, -h/4, w-h/2,h-h/2), self._image)

        if not self._title: return

        font = _QtGui.QFont()
        font.setPointSizeF(h/10)
        font.setFamily("Chomsky")

        metrics = _QtGui.QFontMetrics(font)
        text_width = metrics.width(self._resources.get_translator().translate(self._title))

        painter.setPen(_QtGui.QColor(0xFFFFFF))
        painter.setFont(font)
        painter.drawStaticText(int(-text_width/2), int(h * 1/5), _QtGui.QStaticText(self._resources.get_translator().translate(self._title)))

    def set_size(self, size: int) -> None:
        self._width, self._height = size, size
        self.prepareGeometryChange()
        self.update()
    
    def boundingRect(self) -> _QtCore.QRectF:
        x = -self._width / 2 * self._ratio
        y = -self._height / 2 * self._ratio
        
        return _QtCore.QRectF(int(x), int(y), int(self._width * self._ratio), int(self._height * self._ratio))
    
    
    def mousePressEvent(self, event) -> None:
        super().mousePressEvent(event)
        event.accept()
    
    def mouseReleaseEvent(self, event) -> None:
        super().mouseReleaseEvent(event)

    def set_ratio(self, ratio: float) -> None:
        self._ratio = ratio
        self.prepareGeometryChange()
    
    def get_ratio(self) -> float:
        return self._ratio
    
    def go_to_ratio(self, ratio: float, time: float = 0.3) -> None:
        self._ratio_animation.start_transition(self.get_ratio(), ratio, time)
    