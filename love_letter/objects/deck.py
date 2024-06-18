from .card import *
from .character import *

import random as _random
import events as _events

DECK_EVENT_NUMBER_CHANGED = 0

class LoveLetterDeck():
    def __init__(self):
        self._cards: list[ LoveLetterCard ] = []
        self._events: _events.EventObject = _events.EventObject(
            DECK_EVENT_NUMBER_CHANGED
        )
    
    def get_events(self) -> _events.EventObject:
        return self._events
    
    def add_card(self, card) -> None:
        self._cards.append(card)
        
        self._events[ DECK_EVENT_NUMBER_CHANGED ].emit(card)
        
    def shuffle(self) -> None:
        _random.shuffle(self._cards)
    
    def take_card(self) -> LoveLetterCard:
        card = self._cards.pop(0)
        
        self._events[ DECK_EVENT_NUMBER_CHANGED ].emit(card)
        
        return card
    
    def __len__(self) -> int:
        return len(self._cards)
    
    def toJson(self):
        return {
            'cards': [card.toJson() for card in self._cards]
        }
    
