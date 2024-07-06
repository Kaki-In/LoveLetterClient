from ....background_threads.linear_animation import *
from ..graphics.player import *

import love_letter as _love_letter
import random as _random

class GraphicalPlayerController():
    def __init__(self, player: _love_letter.LoveLetterPlayer, view: PlayerDisplayedElement):
        self._player = player
        
        player.get_events().addEventListener(_love_letter.PLAYER_EVENT_ROUND_WON, self.on_player_won_round)
        player.get_events().addEventListener(_love_letter.PLAYER_EVENT_CARDS, self.on_player_cards_changed)
        player.get_events().addEventListener(_love_letter.PLAYER_EVENT_DISCARD, self.on_player_discarded)
        player.get_events().addEventListener(_love_letter.PLAYER_EVENT_ELIMINATION, self.on_player_eliminated)
        player.get_events().addEventListener(_love_letter.PLAYER_EVENT_INITIALIZATION, self.on_player_initialization)
        player.get_events().addEventListener(_love_letter.PLAYER_EVENT_PROTECTION, self.on_player_protected)
        
        self._element: PlayerDisplayedElement = view
    
    def set_max_rounds(self, max_rounds: int) -> None:
        self._element.set_max_rounds(max_rounds)
    
    def on_player_won_round(self):
        pass
    
    def on_player_cards_changed(self):
        pass
    
    def on_player_discarded(self):
        pass
    
    def on_player_eliminated(self):
        pass
    
    def on_player_initialization(self):
        pass
    
    def on_player_protected(self):
        pass
    
