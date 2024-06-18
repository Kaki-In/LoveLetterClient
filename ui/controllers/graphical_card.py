from ..background_threads.linear_animation import *
from ..graphics.card import *

from PyQt5 import QtCore as _QtCore
import love_letter as _love_letter
import random as _random

class GraphicalCardController():
    def __init__(self, card: _love_letter.LoveLetterCard, view: CardDisplayedElement):
        self._card = card
        self._card.get_events().addEventListener(_love_letter.CARD_EVENT_CHARACTER_CHANGED, self.on_card_character_changed)
        
        self._element: CardDisplayedElement = view
        self._element.start_threads()
        
        self._element.signal_hover_enter.connect(self.on_card_hover_enter)
        self._element.signal_hover_leave.connect(self.on_card_hover_leave)
        self._element.signal_mouse_press.connect(self.on_card_pressed)
    
    def on_card_character_changed(self, character: _love_letter.LoveLetterCharacter):
        self._element.set_character(character)
    
    def on_card_pressed(self) -> None:
        if self._card.get_character() is None:
            character = _random.choice([
                _love_letter.LOVE_LETTER_CHARACTER_GUARD,
                _love_letter.LOVE_LETTER_CHARACTER_PRIEST,
                _love_letter.LOVE_LETTER_CHARACTER_BARON,
                _love_letter.LOVE_LETTER_CHARACTER_HANDMAID,
                _love_letter.LOVE_LETTER_CHARACTER_PRINCE,
                _love_letter.LOVE_LETTER_CHARACTER_KING,
                _love_letter.LOVE_LETTER_CHARACTER_COUNTESS,
                _love_letter.LOVE_LETTER_CHARACTER_PRINCESS,
                ])
        else:
            character = None
        self._card.set_character(character)
    
    def on_card_hover_enter(self, event) -> None:
        self._element.go_to_size(300)
    
    def on_card_hover_leave(self, event) -> None:
        self._element.go_to_size(250)
    
