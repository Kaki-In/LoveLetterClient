from PyQt5 import QtWidgets as _QtWidgets
from PyQt5 import QtGui as _QtGui
from PyQt5 import QtCore as _QtCore

import resources as _resources
import typing as _T

from .element import *

class ListDisplayedElement(GameDisplayedElement):
    def __init__(self, resources: _resources.Resources, elements: list[str], font_size: int, parent = None):
        super().__init__(resources, 0, 0, 50, 50, parent)
        self._elements = elements

        resources.get_fonts_mapper().require_font("Chomsky")

        self._size = font_size
        self._scroll_y_position = 0
        self._selected_element: _T.Optional[int] = None
        self._hovered_element: _T.Optional[int] = None

    def set_selected_position(self, position: _T.Optional[int]) -> None:
        self._selected_element = position
    
    def get_selected_position(self) -> _T.Optional[int]:
        return self._selected_element
    
    def set_hovered_position(self, position: _T.Optional[int]) -> None:
        self._hovered_element = position
    
    def get_hovered_position(self) -> _T.Optional[int]:
        return self._hovered_element
    
    def set_elements(self, list: list[str]) -> None:
        self._elements = list
        
    def mousePressEvent(self, event: _QtWidgets.QGraphicsSceneEvent) -> None:
        super().mousePressEvent(event)
        event.accept()

    def item_at(self, y: float) -> int | None:
        y = y - self._width/30
        y_index = int((y + self._scroll_y_position) / self._size)
        return y_index if y_index in range(len(self._elements)) else None
    
    def paint(self, painter: _QtGui.QPainter, options: _QtWidgets.QStyleOptionGraphicsItem, widget: _QtWidgets.QWidget) -> None:
        super().paint(painter, options, widget)

        palette = self._resources.get_themes_mapper().get_palette().get_sub_palette('graphics').get_palette('list')

        br = self.boundingRect()
        width, height = br.width(), br.height()

        painter.setBrush(palette.get_color('background'))
        painter.setPen(palette.get_color('border'))
        painter.drawRoundedRect(br, 10, 10)

        padding = width/30

        x_position = int(br.x() + padding)
        y_position = int(br.y() + padding)

        y_index = 0

        if width - 2*padding > 0 and height - 2*padding > 0:
            elements_pixmap = _QtGui.QPixmap(int(width - 2*padding), int(height - 2*padding))
            elements_pixmap.fill(_QtGui.QColor.fromRgba(0))
            pixmap_painter = _QtGui.QPainter(elements_pixmap)

            font = _QtGui.QFont("Chomsky", int(self._size * 3/5))
            pixmap_painter.setFont(font)

            for y_index, element in enumerate(self._elements):
                if (y_index + 1) * self._size - self._scroll_y_position < 0:
                    continue
                
                if y_index * self._size - self._scroll_y_position > height:
                    continue

                if y_index:
                    pixmap_painter.setPen(palette.get_color('line'))
                    pixmap_painter.drawLine(0, int(y_index * self._size - self._scroll_y_position), int(width - padding*2), int(y_index * self._size - self._scroll_y_position))
                
                if y_index == self._selected_element:
                    background = palette.get_color('selected')
                elif y_index == self._hovered_element:
                    background = palette.get_color('hovered')
                else:
                    background = palette.get_color('default')

                pixmap_painter.setPen(_QtGui.QColor.fromRgba(0))
                pixmap_painter.setBrush(background)
                pixmap_painter.drawRect(_QtCore.QRectF(0, y_index * self._size - self._scroll_y_position+ 1, width - 2*padding, self._size - 1))

                text_width = _QtGui.QFontMetrics(font).width(element)

                pixmap_painter.setPen(palette.get_color('element_text'))
                pixmap_painter.drawStaticText(int((width - text_width)/2 - padding), int((y_index + 1/5)*self._size - self._scroll_y_position), _QtGui.QStaticText(element))

            pixmap_painter.end()

            painter.drawPixmap(x_position, y_position, elements_pixmap)
    
    def set_width(self, width: int) -> None:
        self._width = width
        self.prepareGeometryChange()
    
    def get_width(self) -> float:
        return self._width

    def set_height(self, height: int) -> None:
        self._height = height
        self.prepareGeometryChange()
    
    def get_height(self) -> float:
        return self._height

    def set_font_size(self, size: int) -> None:
        self._size = int(size)
    
    def size(self) -> int:
        return self._size
