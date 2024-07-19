from PyQt5 import QtWidgets as _QtWidgets
from PyQt5 import QtGui as _QtGui
from PyQt5 import QtCore as _QtCore

from .element import *

from ....animations.exponential_animation import *

class TextInputDisplayedElement(GameDisplayedElement):
    def __init__(self, resources: Resources, text: str, parent = None):
        super().__init__(resources, 0, 0, 250, 50, parent)
        
        self._resources.get_fonts_mapper().require_font("Chomsky")
        
        self._text = text
        self._text_hint = ""
        
        self._ratio = 1
        
        self._size_animation = ExponentialAnimation()
        self._size_animation.signal_frame.connect(self.set_size)
        self._size_animation.set_one_by_one(False)
        
        self._ratio_animation = ExponentialAnimation()
        self._ratio_animation.signal_frame.connect(self.set_ratio)
        self._ratio_animation.set_one_by_one(False)
        
        self._cursor_position = len(text)
        self._blink_state = 0
        
        self._blink_animation = Animation()
        self._blink_animation._verbose = True
        self._blink_animation.signal_frame.connect(self.change_blink_state)
        self._blink_animation.set_one_by_one(False)
        self._blink_animation.setInfinite(True)
        
        self._text_position = 0
        
        self.setFlags(self.GraphicsItemFlag.ItemAcceptsInputMethod | self.GraphicsItemFlag.ItemIsFocusable)
        
        self._centered = False

        self._events.create_event("text_changed")

    def setCentered(self, centered: bool) -> None:
        self._centered = centered
    
    def is_centered(self) -> bool:
        return self._centered
    
    def get_text_hint(self) -> str:
        return self._text_hint
    
    def set_text_hint(self, text: str) -> None:
        self._text_hint = text
    
    def focusInEvent(self, event: _QtGui.QFocusEvent) -> None:
        super().focusInEvent(event)
        self.start_blinking()
        self.update()
    
    def focusOutEvent(self, event: _QtGui.QFocusEvent) -> None:
        self.stop_blinking()
        self.update()
    
    def get_cursor_position(self) -> int:
        return self._cursor_position
    
    def set_cursor_position(self, curs_pos: int) -> None:
        self._cursor_position = curs_pos
    
    def set_text(self, text: str) -> None:
        self._text = text
        self._events["text_changed"].emit(text)
        self.prepareGeometryChange()
    
    def start_blinking(self) -> None:
#        if not self._blink_animation.isRunning():
        self._blink_animation.start_transition(1, 0, 1)
    
    def stop_blinking(self) -> None:
        self._blink_animation.reset()
    
    def change_blink_state(self, state: float) -> None:
        if state == self._blink_state:
            return
        
        self._blink_state = state
        
        self.update()
    
    def get_text(self) -> str:
        return self._text
    
    def start_threads(self):
        self._size_animation.get_thread().start()
        self._ratio_animation.get_thread().start()
        self._blink_animation.get_thread().start()
    
    def stop_threads(self):
        self._size_animation.stop()
        self._ratio_animation.stop()
        self._blink_animation.stop()
    
    def paint(self, painter: _QtGui.QPainter, options: _QtWidgets.QStyleOptionGraphicsItem, widget: _QtWidgets.QWidget) -> None:
        super().paint(painter, options, widget)
        
        if self._height < 3:
            return
        
        r = self.boundingRect()
        w, h = r.width(), r.height()
        x, y = r.x() + w/2, r.y() + h/2
        
        painter.setBrush(_QtGui.QColor(0x3E070C))
        painter.setPen(_QtGui.QColor.fromRgba(0))
        painter.drawRect(self.boundingRect())
        
        painter.setBrush(_QtGui.QColor(0x7D0F19))
        painter.setPen(_QtGui.QColor.fromRgba(0))
        painter.drawRect(_QtCore.QRect(int(r.x() + h/10), int(r.y() + h/10), int(w - h * 2/10), int(h * 8/10)))
        
        font = _QtGui.QFont("Chomsky", int(self._height / 3))
        fm = _QtGui.QFontMetrics(font)
        text_width = fm.width(self._text or self._text_hint)
        text_height = fm.height()
        
        button_width = w - h*4/10
        
        text_image = _QtGui.QPixmap(int(button_width), int(text_height))
        text_image.fill(_QtGui.QColor.fromRgba(0))
        text_painter = _QtGui.QPainter(text_image)
        
        font.setPointSize(int(self._height / 3))
        text_painter.setFont(font)
        
        cursor_x = fm.width(self._text[:self._cursor_position])
        cursor_position = self._text_position + cursor_x
        
        if cursor_position < text_height * 2/10:
            self._text_position = text_height * 2/10 - cursor_x-2
        
        cursor_position = self._text_position + cursor_x
        
        if cursor_position > button_width - text_height * 2/10:
            self._text_position = button_width - cursor_x - 2 - text_height * 2/10
        
        if self._text_position > 1:
            self._text_position = 1
        
        if text_width < button_width and self._centered:
            self._text_position = button_width / 2 - text_width / 2
        
        cursor_position = (self._text_position + cursor_x) if self._text or not self._centered else (button_width / 2)
        
        if self._text:
            text_painter.setPen(_QtGui.QColor(0xFFFFFFFF))
        else:
            text_painter.setPen(_QtGui.QColor.fromRgba(0x80FFFFFF))
        text_painter.drawStaticText(_QtCore.QPoint(int(self._text_position), 0), _QtGui.QStaticText(self._text or self._text_hint))
        
        if self.hasFocus() and self._blink_state:
            text_painter.drawLine(int(cursor_position), 0, int(cursor_position), text_height)
        
        text_painter.end()
        
        painter.drawImage(_QtCore.QPoint(int(x - w/2 + h*2/10), int(y - text_height/2)), text_image.toImage())
        
        if self.hasFocus():
            painter.setPen(_QtGui.QColor(0xFFFFFFFF))
            painter.setBrush(_QtGui.QColor.fromRgba(0))
            painter.drawRect(self.boundingRect())
        
    def set_height(self, size: int) -> None:
        self._height = size
        self.prepareGeometryChange()
        self.update()
    
    def set_width(self, width: int) -> None:
        self._width = width
        self.prepareGeometryChange()
        self.update()
    
    def set_size(self, size: int) -> None:
        self._height = size
        self._width = size * 6
        self.prepareGeometryChange()
        self.update()
    
    def get_size(self):
        return self._height
    
    def set_ratio(self, ratio: int) -> None:
        self._ratio = ratio
        self.prepareGeometryChange()
        self.update()
    
    def get_ratio(self) -> float:
        return self._ratio
    
    def boundingRect(self) -> _QtCore.QRectF:
        font = _QtGui.QFont("Chomsky", int(self._height / 3))
        fm = _QtGui.QFontMetrics(font)
        text_height = fm.height() * self._ratio
        
        width = self._width * self._ratio
        
        return _QtCore.QRectF( -width/2, -text_height/2, width, text_height*2)
    
    def go_to_size(self, size: int, time: float = 0.3) -> None:
        self._size_animation.start_transition(self.get_size(), size, time)
    
    def go_to_ratio(self, ratio: int, time: float = 0.3) -> None:
        self._ratio_animation.start_transition(self.get_ratio(), ratio, time)
    

