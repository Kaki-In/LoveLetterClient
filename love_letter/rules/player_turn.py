from .character import *

from ..notifiers import *
from ..objects import *

import typing as _T

class LoveLetterPlayerTurnRule():
    def __init__(self):
        pass
    
    async def play(self, mapper: 'LoveLetterCharacterMapper', notifier: LoveLetterNotifier, round: LoveLetterRound) -> None:
        player = round.get_active_player()
        
        player.take_card(round.draw())
        
        if player.is_protected():
            player.stop_protection()
        
        confirmed = False
        
        while not confirmed:
            card_result = await notifier.choose_card_to_play(player)
            
            if card_result.get_args()[ "card" ] == "hand_card":
                card = player.get_card()
            else:
                card = player.get_drawn_card()
            
            print(card.get_character().get_name())
            
            card_map = mapper.get_map_by_character( card.get_character() )
            card_rule = card_map.get_rule()
            
            safe_state = await card_rule.can_be_safely_laid(mapper, notifier, round)
            
            if safe_state == LOVE_LETTER_CHARACTER_RULE_SAFE:
                confirmed = True
            else:
                reason = ClientReason(LOVE_LETTER_REASON_UNSAFE_PLAY, {
                    'unsafe_status' : safe_state
                })
                if safe_state == LOVE_LETTER_CHARACTER_RULE_UNSAFE_COUNTESS_PRESENCE:
                    await notifier.display_unsafe_message(player, reason)
                    confirmed = False
                else:
                    answer = await notifier.confirm_unsafe_message(player, reason)
                    confirmed = answer.get_args()[ "confirmed" ]
        
        if card_result.get_args()[ "card" ] == "hand_card":
            player.lay_card()
            player.add_to_discard(card)
        else:
            player.lay_drawn_card()
            player.add_to_discard(card)
        
        await card_rule.execute_on_player_turn(mapper, notifier, round)
        print("Done")
    
    async def make_player_discard(self, mapper: 'LoveLetterCharacterMapper', notifier: LoveLetterNotifier, round: LoveLetterRound, player: LoveLetterPlayer) -> None:
        card = player.get_card()
        player.lay_card()
        player.add_to_discard(card)
        
        map = mapper.get_map_by_character( card.get_character() )
        await map.get_rule().execute_on_discarded(mapper, notifier, round, player)
    

