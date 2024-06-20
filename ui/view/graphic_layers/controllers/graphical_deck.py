from ....background_threads.linear_animation import *
from ..graphics.deck import *

from PyQt5 import QtCore as _QtCore
from PyQt5 import QtWidgets as _QtWidgets
import love_letter as _love_letter
import random as _random

class GraphicalDeckController():
    def __init__(self, deck: _love_letter.LoveLetterDeck, view: DeckDisplayedElement):
        self._deck = deck
        self._deck.get_events().addEventListener(_love_letter.DECK_EVENT_NUMBER_CHANGED, self.on_deck_number_changed)
        
        self._cards = []
        
        self._element: DeckDisplayedElement = view
        
        self._element.deck_card().signal_mouse_press.connect(self.on_deck_pressed)
        self._element.deck_card().signal_hover_enter.connect(self.on_deck_hover_enter)
        self._element.deck_card().signal_hover_leave.connect(self.on_deck_hover_leave)
        
        self._element.set_card(None)
        self._element.set_number(len(self._deck))
    
    def on_deck_number_changed(self, card: _love_letter.LoveLetterCard) -> None:
        self._element.set_number(len(self._deck))
    
    def on_deck_pressed(self) -> None:
        if self._element.animation_card().get_position_animations()[0].isRunning():
            return
        
        if self._element.last_card() is not None:
            self._cards.append(self._element.last_card())
        
        if len(self._deck):
            card = self._deck.take_card()
            self._element.set_card(card)
        else:
            for card in self._cards:
                self._deck.add_card(card)
            self._cards = []
            self._deck.shuffle()
            self._element.set_card(None)
        
    def on_deck_hover_enter(self, event: _QtWidgets.QGraphicsSceneMouseEvent) -> None:
        self._element.deck_card().go_to_size(self._element.get_size() * 6/7)
    
    def on_deck_hover_leave(self, event: _QtWidgets.QGraphicsSceneMouseEvent) -> None:
        self._element.deck_card().go_to_size(self._element.get_size())
    
