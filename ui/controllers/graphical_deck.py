from ..background_threads.linear_animation import *
from ..graphics.deck import *

from PyQt5 import QtCore as _QtCore
import love_letter as _love_letter
import random as _random

class GraphicalDeckController():
    def __init__(self, deck: _love_letter.LoveLetterDeck, view: DeckDisplayedElement):
        self._deck = deck
        self._deck.get_events().addEventListener(_love_letter.DECK_EVENT_NUMBER_CHANGED, self.on_deck_number_changed)
        
        self._cards = []
        
        self._element: DeckDisplayedElement = view
        
        self._element.signal_hover_enter.connect(self.on_deck_hover_enter)
        self._element.signal_hover_leave.connect(self.on_deck_hover_leave)
        
        self._element.deck_card().signal_mouse_press.connect(self.on_deck_pressed)
    
    def on_deck_number_changed(self, card: _love_letter.LoveLetterCard):
        self._element.set_number(len(self._deck))
    
    def on_deck_pressed(self) -> None:
        self._cards.append(self._element.last_card())
        
        if not len(self._deck):
            for card in self._cards:
                self._deck.add_card(card)
            self._cards = []
        
        card = self._deck.take_card()
        self._element.set_card(card)
        
    def on_deck_hover_enter(self, event) -> None:
        pass
    
    def on_deck_hover_leave(self, event) -> None:
        pass
    
