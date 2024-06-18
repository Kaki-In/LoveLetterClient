from ..mapping import *
from ..objects import *

from .player_turn import *
from .character import *

import typing as _T

class LoveLetterRoundRule():
    def __init__(self):
        self._players_rule = LoveLetterPlayerTurnRule()
    
    async def main_round(self, mapper: LoveLetterCharacterMapper, notifier: LoveLetterNotifier, round: LoveLetterRound) -> None:
        round.get_deck().shuffle()
        
        players = round.get_players()
        
        round.set_hidden_card(round.get_deck().take_card())
        
        if len(players) == 2:
            for _ in range(3):
                round.add_removed_card(round.get_deck().take_card())
        
        for player in players:
            player.initialize_for_round()
            player.take_card(round.get_deck().take_card())
    
        while not self.is_finished(round):
            await self._players_rule.play(mapper, notifier, round)
            round.select_next_player()
    
    async def make_player_discard(self, mapper: LoveLetterCharacterMapper, notifier: LoveLetterNotifier, player: LoveLetterPlayer, round: LoveLetterRound) -> None:
        card = player.get_card()
        player.lay_card()
        
        char_rule = mapper.get_map_by_character(card.get_character()).get_rule()
        
        await char_rule.execute_on_discarded(mapper, notifier, round, player)
    
    def is_finished(self, round: LoveLetterRound) -> bool:
        return len(round.get_alive_players()) <= 1 or len(round.get_deck()) == 0
    
    
    
    


