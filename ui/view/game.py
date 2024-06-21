from PyQt5 import QtWidgets as _QtWidgets, uic as _uic
from PyQt5 import QtCore as _QtCore
from PyQt5 import QtGui as _QtGui

from .graphic_layers import *
from .graphic_layers.graphics.main_element import *
from .graphic_layers.graphics.mouse import *

# from ..graphic_layers.controllers import *
from .layer_controllers.first_controller import *
#from .layer_controllers.game_controller import *

import love_letter as _love_letter
import typing as _T
import darkdetect as _dark_detect

class GameWidget(_QtWidgets.QGraphicsView):
    def __init__(self):
        super().__init__()
        
        self._scene: _QtWidgets.QGraphicsScene = _QtWidgets.QGraphicsScene()
        
        self.setScene(self._scene)
        
        self._scene.setPalette(CustomPalette())
        
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
        
        self._layer: _T.Optional[GraphicLayer] = None
        
        players: list[_love_letter.LoveLetterPlayer]= []
        players.append(_love_letter.LoveLetterPlayer(1, "Bob"))
        players.append(_love_letter.LoveLetterPlayer(2, "Kaki In"))
        players.append(_love_letter.LoveLetterPlayer(3, "Georges"))
        players.append(_love_letter.LoveLetterPlayer(4, "Michel"))
        
        game = _love_letter.LoveLetterGame(*players)
        rules = _love_letter.LoveLetterGameRules(None, _love_letter.LoveLetterCharacterMapper.create_default_mapping())
        
        deck = rules.create_new_deck()
        game.init_new_round(deck)
        
        round = game.get_actual_round()
        _love_letter.LoveLetterRoundRule().prepare(round)
        
        players[0].take_card(deck.take_card())
        
        layer = RoundGraphicLayer(round.get_players(), round.get_active_player(), deck)
#        self._controller = GameGraphicLayerController(layer)
        self.displayLayer(layer)
        
        self._dark_mode_enabled = _dark_detect.isDark( )
    
    def onShow(self) -> None:
        self.resizeEvent()
    
    def set_dark_mode(self, enabled: bool) -> None:
        self._dark_mode_enabled = enabled
    
    def dark_mode_enabled(self) -> bool:
        return self._dark_mode_enabled
    
    def displayLayer(self, layer: GraphicLayer) -> None:
        if self._layer:
            for item in self._layer.get_items():
                self._scene.removeItem(item)
                
                item.stop_threads()
        
        for item in layer.get_items():
            self._scene.addItem(item)
            
            item.start_threads()
        
        self._layer = layer
    
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
        
