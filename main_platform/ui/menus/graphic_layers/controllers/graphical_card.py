from ....animations.linear_animation import *
from ..graphics.card import *

import love_letter as _love_letter
import random as _random

class GraphicalCardController():
    def __init__(self, card: _love_letter.LoveLetterCard, view: CardDisplayedElement):
        self._card = card
        self._card.get_events().addEventListener(_love_letter.CARD_EVENT_CHARACTER_CHANGED, self.on_card_character_changed)
        
        self._element: CardDisplayedElement = view
        self._element.start_threads()

        elem_events = self._element.get_events()
        
        elem_events["hover_enter"].addEventFunction(self.on_card_hover_enter)
        elem_events["hover_leave"].addEventFunction(self.on_card_hover_leave)
        elem_events["mouse_press"].addEventFunction(self.on_card_pressed)
        
        self._element.change_character(self._card.get_character())
    
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
    
