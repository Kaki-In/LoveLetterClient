from PyQt5 import QtWidgets as _QtWidgets, uic as _uic
from PyQt5 import QtCore as _QtCore
from PyQt5 import QtGui as _QtGui

from ..graphics.mouse import *
from ..graphics.main_element import *
from ..graphics.card import *
from ..graphics.player import *
from ..graphics.deck import *
from ..graphics.button import *
from ..graphics.text_input import *

from ..controllers import *

import love_letter as _love_letter

class GameWidget(_QtWidgets.QGraphicsView):
    def __init__(self):
        super().__init__()
        
        self._scene: _QtWidgets.QGraphicsScene = _QtWidgets.QGraphicsScene()
        
        self.setScene(self._scene)
        
        self._main_graphic = MainDisplayedElement()
        self._main_graphic.setZValue(0)
        self._scene.addItem(self._main_graphic)
        
        self._mouse = MouseDisplayedElement()
        self._mouse.set_size(40)
        
        self._mouse.setZValue(1000)
        
        self._scene.addItem(self._mouse)
        
        self.setMouseTracking(True)
        self.setInteractive(True)
        
        self.setVerticalScrollBarPolicy(_QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.setHorizontalScrollBarPolicy(_QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        
        button = ButtonDisplayedElement("Jouer")
        self._scene.addItem(button)
        
        self._bcontrol = GraphicalButtonController(button)
    
        card = CardDisplayedElement(_love_letter.LOVE_LETTER_CHARACTER_BARON)
        self._card_controller = GraphicalCardController(_love_letter.LoveLetterCard(_love_letter.LOVE_LETTER_CHARACTER_BARON), card)
        self._scene.addItem(card)
    
        tinput = TextInputDisplayedElement("Bonjour")
        tinput.set_position(0, 250)
        self._scene.addItem(tinput)
        
        self._icontrol = GraphicalTextInputController(tinput)
        
        deck = DeckDisplayedElement(16, _love_letter.LoveLetterCard(None))
        lldeck = _love_letter.LoveLetterDeck()
        self._dcontrol = GraphicalDeckController(lldeck, deck)
        
        mapper = _love_letter.LoveLetterCharacterMapper.create_default_mapping()
        for map in mapper.get_all_maps():
            for c in range(map.get_count()):
                lldeck.add_card(_love_letter.LoveLetterCard(map.get_character()))
        
        self._scene.addItem(deck)
    
    def onShow(self) -> None:
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
        
