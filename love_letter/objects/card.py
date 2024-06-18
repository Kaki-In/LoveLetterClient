from .character import *

import typing as _T
import events as _events

CARD_EVENT_CHARACTER_CHANGED = 0

class LoveLetterCard():
    def __init__(self, character: _T.Optional[LoveLetterCharacter]):
        self._character: _T.Optional[LoveLetterCharacter] = character
        self._events = _events.EventObject(
            CARD_EVENT_CHARACTER_CHANGED
        )
    
    def get_character(self) -> LoveLetterCharacter:
        return self._character
    
    def set_character(self, character: _T.Optional[LoveLetterCharacter]) -> None:
        self._character = character
        self._events[CARD_EVENT_CHARACTER_CHANGED].emit(self._character)
    
    def __lt__(self, second_card: 'LoveLetterCard') -> bool:
        return self.get_character() < second_card.get_character()
    
    def __gt__(self, second_card: 'LoveLetterCard') -> bool:
        return self.get_character() > second_card.get_character()
    
    def __eq__(self, second_card: 'LoveLetterCard') -> bool:
        return self.get_character() == second_card.get_character()
    
    def get_events(self) -> _events.EventObject:
        return self._events
    
    def toJson(self):
        if self._character is None:
            return {
                'character_name': None
            }
        else:
            return {
                'character_name': self._character.get_name()
            }
