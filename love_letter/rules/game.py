from .round import LoveLetterRoundRule

from ..objects import *
from ..notifiers import *
from ..mapping import *

import typing as _T
import asyncio as _asyncio

class LoveLetterGameRules():
    def __init__(self, notifier: LoveLetterNotifier, mapper: LoveLetterCharacterMapper):
        self._notifier = notifier
        self._mapper = mapper
        
        self._rounds_rule = LoveLetterRoundRule()
    
    def create_new_deck(self) -> LoveLetterDeck:
        deck = LoveLetterDeck()
        
        for map in self._mapper.get_all_maps():
            for count in range(map.get_count()):
                deck.add_card(LoveLetterCard(map.get_character()))
        
        return deck
    
    def get_notifier(self) -> LoveLetterNotifier:
        return self._notifier
    
    def get_characters_mapper(self) -> LoveLetterCharacterMapper:
        return self._mapper
    
    def is_finished(self, game: LoveLetterGame) -> bool:
        players = game.get_players()
        
        players_number = len(players)
        
        max_points = [6, 5, 4][ players_number - 2 ]
        
        for player in players:
            if player.get_won_rounds() >= max_points:
                return True
        
        return False
    
    async def main_game(self, game: LoveLetterGame) -> None:
        while not self.is_finished(game):
            game.init_new_round(self.create_new_deck())
            
            await self._rounds_rule.main_round(self._mapper, self._notifier, game.get_actual_round())
            
            await _asyncio.sleep(1)
        


