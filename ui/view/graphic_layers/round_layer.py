from .layer import *

from .graphics.player import *
from .graphics.deck import *

from .controllers.graphical_player import *
from .controllers.graphical_deck import *

from PyQt5 import QtCore as _QtCore

import love_letter as _love_letter

class RoundGraphicLayer(GraphicLayer):
    def __init__(self, players: list[_love_letter.LoveLetterPlayer], active_player: int, deck: _love_letter.LoveLetterDeck):
        super().__init__()
        
        self._players: list[PlayerDisplayedElement] = []
        self._player_controllers: list[GraphicalPlayerController] = []
        
        self._active_player = active_player
        
        for player in players:
            player_element = PlayerDisplayedElement(player.get_card(), player.get_drawn_card(), player.get_name(), [i.get_character().get_value() for i in player.get_discard()])
            self._players.append(player_element)
            self._player_controllers.append(GraphicalPlayerController(player, player_element))
        
        self._deck = DeckDisplayedElement(0, None)
        
        self._deck_controller = GraphicalDeckController(deck, self._deck)
    
    def get_items(self) -> list[ GameDisplayedElement ]:
        return [self._deck] + self._players
    
    def set_rect(self, x: int, y: int, w: int, h: int) -> None:
        x, y, w, h = x+w*1/10, y + h*1/10, w * 8/10, h * 8/10
        
        self._deck.set_position(x + w/2, y + h/2)
        self._deck.set_size(h/5)
        
        if len(self._players) == 2:
            self._players[0].set_position(x + w/2, y + 5 * h/6)
            self._players[1].set_position(x + w/2, y + h/6)
        elif len(self._players) == 3:
            self._players[0].set_position(x + w/2, y + 5 * h/6)
            self._players[1].set_position(x + w/2 - h/2, y + h/6)
            self._players[2].set_position(x + w/2 + h/2, y + h/6)
        elif len(self._players) == 4:
            self._players[0].set_position(x + w/2, y + 5 * h/6)
            self._players[1].set_position(x + w/2 - h/2, y + h/2)
            self._players[2].set_position(x + w/2, y + h/6)
            self._players[3].set_position(x + w/2 + h/2, y + h/2)
        
        for player in self._players:
            player.set_size(h/5)
        
        
    
    


