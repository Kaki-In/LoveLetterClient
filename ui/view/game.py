from PyQt5 import QtWidgets as _QtWidgets, uic as _uic
from PyQt5 import QtCore as _QtCore
from PyQt5 import QtGui as _QtGui

from ..graphics.mouse import *
from ..graphics.main_element import *
from ..graphics.card import *
from ..graphics.player import *
from ..graphics.deck import *

from ..controllers import *

import love_letter as _love_letter

class GameWidget(_QtWidgets.QGraphicsView):
    def __init__(self):
        super().__init__()
        
        self._scene: _QtWidgets.QGraphicsScene = _QtWidgets.QGraphicsScene()
        
        self.setScene(self._scene)
        
        self._main_graphic = MainDisplayedElement()
        self._main_graphic.setZValue(-10)
        self._scene.addItem(self._main_graphic)
        
        self._mouse = MouseDisplayedElement()
        self._mouse.set_size(40)
        
        self._mouse.setZValue(1000)
        
        self._scene.addItem(self._mouse)
        
        self.setMouseTracking(True)
        self.setInteractive(True)
        
        self.setVerticalScrollBarPolicy(_QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.setHorizontalScrollBarPolicy(_QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        
        self._controllers = []
        
        player1 = PlayerDisplayedElement(_love_letter.LoveLetterCard(_love_letter.LOVE_LETTER_CHARACTER_BARON), _love_letter.LoveLetterCard(_love_letter.LOVE_LETTER_CHARACTER_PRINCESS), "Blop")
        player2 = PlayerDisplayedElement(_love_letter.LoveLetterCard(None), None, "Test")
        
        self._scene.addItem(player1)
        self._scene.addItem(player2)
        
        player1.set_position(-500, 0)
        player1.set_size(200)
        
        player2.set_position(500, 0)
        player2.set_size(200)

        deck = DeckDisplayedElement(10, _love_letter.LoveLetterCard(None))
        
        map = _love_letter.LoveLetterCharacterMapper.create_default_mapping()
        d = _love_letter.LoveLetterDeck()
        
        for elem in map.get_all_maps():
            for c in range(elem.get_count()):
                d.add_card(_love_letter.LoveLetterCard(elem.get_character()))
        
        self._controllers.append(GraphicalDeckController(d, deck))
        
        self._scene.addItem(deck)

        deck.set_position(0, 300)
        deck.set_size(200)
        
    def onShow(self):
        self.resizeEvent()
    
    def resizeEvent(self, event = None) -> None:
        w, h = self.width() - 2, self.height() - 2
        
        self.setSceneRect(-w / 2, -h / 2, w, h)
        self._main_graphic.set_rect(-w / 2, -h / 2, w, h)
    
    def mouseMoveEvent(self, event: _QtGui.QMouseEvent) -> None:
        super().mouseMoveEvent(event)
        
        position: _QtCore.QPointF = event.pos()
        
        position.setX(int(position.x() - self.width() / 2))
        position.setY(int(position.y() - self.height() / 2))
        
        event.ignore()
        
        x, y = position.x(), position.y()
        self._mouse.set_position(x, y)
        
        self._scene.update()
        
