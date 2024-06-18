from .client import *
from .message import *
from .result import *
from .reason import *

import typing as _T
import asyncio as _asyncio

LOVE_LETTER_REASON_GUARD                        = "character.guard"
LOVE_LETTER_REASON_PRIEST                       = "character.priest"
LOVE_LETTER_REASON_BARON                        = "character.baron"
LOVE_LETTER_REASON_PRINCE                       = "character.prince"
LOVE_LETTER_REASON_KING                         = "character.king"
LOVE_LETTER_REASON_UNSAFE_PLAY                  = "unsafe_play"
LOVE_LETTER_GAME_CRASHED                        = "game_crash"

class Notifier():
    def __init__(self):
        self._clients: dict[int, LoveLetterClient] = {}
    
    def plug_client_with_player(self, client: LoveLetterClient, player: LoveLetterPlayer) -> None:
        self._clients[ player.get_id() ] = client
    
    def get_client_by_player(self, player: LoveLetterPlayer) -> LoveLetterClient:
        return self._clients[ player.get_id() ]
    
    async def notify_to_all(self, message: ClientMessage) -> None:
        tasks = []
        for client_id in self._clients:
            client = self._clients[ client_id ]
            tasks.append( client.send_message(message) )
        
        await _asyncio.gather(*tasks)
    
    async def send_message_to_client(self, player: LoveLetterPlayer, message: ClientMessage) -> None:
        client = self.get_client_by_player(player)
        await client.send_message(message)
    
    async def interact_with_client(self, player: LoveLetterPlayer, message: ClientMessage) -> ClientResult:
        client = self.get_client_by_player(player)
        while True:
            result = await client.interact(message)
            if message.answer_is_valid(result):
                return result

class LoveLetterNotifier(Notifier):
    def __init__(self):
        super().__init__()
    
    async def display_card(self, player: LoveLetterPlayer, card: LoveLetterCard, reason: ClientReason) -> None:
        message = ClientMessageDisplayCard(card, reason)
        
        client = self.get_client_by_player(player)
        await self.interact_with_client(player, message)
    
    async def choose_player_between(self, player: LoveLetterPlayer, players: list[LoveLetterPlayer], reason: ClientReason) -> ClientResult:
        message = ClientMessageChoosePlayer(players, reason)
        
        client = self.get_client_by_player(player)
        return await self.interact_with_client(player, message)
    
    async def choose_character(self, mapper: 'LoveLetterCharacterMapper', player: LoveLetterPlayer, reason: ClientReason) ->  ClientResult:
        message = ClientMessageChooseCharacter(reason, mapper)
        
        client = self.get_client_by_player(player)
        return await self.interact_with_client(player, message)
    
    async def choose_card_to_play(self, player: LoveLetterPlayer) -> ClientResult:
        card = player.get_card()
        drawn_card = player.get_drawn_card()
        
        message = ClientMessageChooseCardToPlay(card, drawn_card)
        
        result = await self.interact_with_client(player, message)
        
        return result
    
    async def update_player_protection(self, player: LoveLetterPlayer) -> None:
        message = ClientMessage(LOVE_LETTER_MESSAGE_SET_PROTECTED, {
            'player' : player.get_id(),
            'status' : player.is_protected()
        })
        
        for client_id in self._clients:
            client = self._clients[ client_id ]
            
            await client.send_message(message)
    
    async def set_player_as_eliminated(self, player: LoveLetterPlayer) -> None:
        message = ClientMessage(LOVE_LETTER_MESSAGE_SET_ELIMINATED, {
            'player' : player.get_id(),
        })
        
        for client_id in self._clients:
            client = self._clients[ client_id ]
            
            await client.send_message(message)
    
    async def compare_cards(self, player1: LoveLetterPlayer, player2: LoveLetterPlayer, reason: ClientReason) -> None:
        message = ClientMessageCompareCards(player1, player2, reason)
        
        await _asyncio.gather(self.interact_with_client(player1, message), self.interact_with_client(player2, message))
    
    async def display_unsafe_message(self, player: LoveLetterPlayer, reason: ClientReason) -> None:
        message = ClientMessageDisplayUnsafeMessage(reason)
        
        client = self.get_client_by_player(player)
        await self.interact_with_client(player, message)
    
    async def confirm_unsafe_message(self, player: LoveLetterPlayer, reason: ClientReason) -> ClientResult:
        message = ClientMessageConfirmUnsafeMessage(reason)
        
        client = self.get_client_by_player(player)
        return await self.interact_with_client(player, message)
    
    async def cancel_game(self, reason: ClientReason) -> None:
        message = ClientMessage(LOVE_LETTER_MESSAGE_CANCEL_GAME, {
            "reason": reason
        })
        
        for client_id in self._clients:
            client = self._clients[ client_id ]
            await client.send_message(message)
    
    
    def plug_to_game(self, game: LoveLetterGame) -> None:
        for player in game.get_players():
            self.plug_to_player(player)
    
    def plug_to_player(self, player: LoveLetterPlayer) -> None:
        events = player.get_events()
        
        func_map = {
            PLAYER_EVENT_CARDS: self.on_event_player_cards,
            PLAYER_EVENT_DISCARD: self.on_event_player_discard,
            PLAYER_EVENT_ELIMINATION: self.on_event_player_elimination,
            PLAYER_EVENT_INITIALIZATION: self.on_event_player_initialization,
            PLAYER_EVENT_PROTECTION: self.on_event_player_protection,
            PLAYER_EVENT_ROUND_WON: self.on_event_player_won_round
        }
        
        for func_event in func_map:
            events[ func_event ].addEventFunction(func_map[ func_event ])
    
    
    
    async def on_event_player_cards(self, player: LoveLetterPlayer) -> None:
        message_others = ClientMessage(LOVE_LETTER_MESSAGE_EVENT_PLAYER_CARD, {
            "player": player.get_id(),
            "cards": player.get_card() is not None,
            "drawn_cards": player.get_drawn_card() is not None,
        })
        
        message_player = ClientMessage(LOVE_LETTER_MESSAGE_EVENT_PLAYER_CARD, {
            "player": player.get_id(),
            "cards": player.get_card(),
            "drawn_cards": player.get_drawn_card(),
        })
        
        for client_id in self._clients:
            client = self._clients[ client_id ]
            
            if client_id == player.get_id():
                await client.send_message(message_player)
            else:
                await client.send_message(message_others)
        
    async def on_event_player_discard(self, player: LoveLetterPlayer) -> None:
        message = ClientMessage(LOVE_LETTER_MESSAGE_EVENT_PLAYER_DISCARD, {
            "player": player.get_id(),
            "discard": [card.toJson() for card in player.get_discard()]
        })
        
        for client_id in self._clients:
            client = self._clients[ client_id ]
            
            await client.send_message(message)
        
    async def on_event_player_elimination(self, player: LoveLetterPlayer) -> None:
        message = ClientMessage(LOVE_LETTER_MESSAGE_EVENT_PLAYER_ELIMINATION, {
            "player": player.get_id(),
            "eliminated": player.is_eliminated()
        })
        
        for client_id in self._clients:
            client = self._clients[ client_id ]
            
            await client.send_message(message)
        
    async def on_event_player_initialization(self, player: LoveLetterPlayer) -> None:
        message = ClientMessage(LOVE_LETTER_MESSAGE_EVENT_PLAYER_INITIALIZATION, {
            "player": player.get_id()
        })
        
        for client_id in self._clients:
            client = self._clients[ client_id ]
            
            await client.send_message(message)
        
    async def on_event_player_protection(self, player: LoveLetterPlayer) -> None:
        message = ClientMessage(LOVE_LETTER_MESSAGE_EVENT_PLAYER_PROTECTION, {
            "player": player.get_id(),
            "protected": player.is_protected()
        })
        
        for client_id in self._clients:
            client = self._clients[ client_id ]
            
            await client.send_message(message)
        
    async def on_event_player_won_round(self, player: LoveLetterPlayer) -> None:
        message = ClientMessage(LOVE_LETTER_MESSAGE_EVENT_PLAYER_WON_ROUND, {
            "player": player.get_id()
        })
        
        for client_id in self._clients:
            client = self._clients[ client_id ]
            
            await client.send_message(message)
        
    






