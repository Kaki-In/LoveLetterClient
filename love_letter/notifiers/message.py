import typing as _T

from love_letter.notifiers.result import ClientResult

from .result import *
from .reason import *

from ..objects import *

LOVE_LETTER_MESSAGE_DISPLAY_CARD                = "display.card"
LOVE_LETTER_MESSAGE_CHOOSE_PLAYER               = "choose.player"
LOVE_LETTER_MESSAGE_CHOOSE_CHARACTER            = "choose.character"
LOVE_LETTER_MESSAGE_CHOOSE_CARD_TO_PLAY         = "choose.card_to_play"
LOVE_LETTER_MESSAGE_SET_PROTECTED               = "set_player.protected"
LOVE_LETTER_MESSAGE_SET_ELIMINATED              = "set_player.eliminated"
LOVE_LETTER_MESSAGE_COMPARE                     = "compare_cards"
LOVE_LETTER_MESSAGE_CONFIRM_UNSAFE              = "unsafe_play.confirm"
LOVE_LETTER_MESSAGE_DISPLAY_UNSAFE              = "unsafe_play.display"
LOVE_LETTER_MESSAGE_CANCEL_GAME                 = "cancel_game"

LOVE_LETTER_MESSAGE_EVENT_PLAYER_CARD           = "event.player.cards"
LOVE_LETTER_MESSAGE_EVENT_PLAYER_DISCARD        = "event.player.discard"
LOVE_LETTER_MESSAGE_EVENT_PLAYER_ELIMINATION    = "event.player.elimination"
LOVE_LETTER_MESSAGE_EVENT_PLAYER_INITIALIZATION = "event.player.initialization"
LOVE_LETTER_MESSAGE_EVENT_PLAYER_PROTECTION     = "event.player.protection"
LOVE_LETTER_MESSAGE_EVENT_PLAYER_WON_ROUND      = "event.player.won_round"

class ClientMessage():
    def __init__(self, name: str, args: dict[str, _T.Any]):
        self._name = name
        self._args = args
    
    def toJson(self) -> dict[str, _T.Any]:
        return {
            "name": self._name,
            "args": self._args
        }
    
    def get_name(self):
        return self._name
    
    def get_args(self):
        return self._args
    
    def answer_is_valid(self, result: ClientResult) -> bool:
        return result.get_name() == self._name
    
class ClientMessageDisplayCard(ClientMessage):
    def __init__(self, card: LoveLetterCard, reason: ClientReason):
        super().__init__(LOVE_LETTER_MESSAGE_DISPLAY_CARD, {
            'character' : card.get_character().get_name(),
            'reason'    : reason.toJson()
        })

class ClientMessageChoosePlayer(ClientMessage):
    def __init__(self, players: list[LoveLetterPlayer], reason: ClientReason):
        ids = [player.get_id() for player in players]
        
        super().__init__(LOVE_LETTER_MESSAGE_CHOOSE_PLAYER, {
            'players' : ids,
            'reason'  : reason.toJson()
        })
        
        self._ids = ids
    
    def answer_is_valid(self, result: ClientResult) -> bool:
        if "player_id" in result.get_args():
            if result.get_args()["player_id"] in self._ids:
                return super().answer_is_valid(result)
        
        return False

class ClientMessageChooseCharacter(ClientMessage):
    def __init__(self, reason: ClientReason, mapper):
        super().__init__(LOVE_LETTER_MESSAGE_CHOOSE_CHARACTER, {
            'reason': reason.toJson()
        })
        
        self._mapper = mapper
    
    def answer_is_valid(self, result: ClientResult) -> bool:
        if "character_name" in result.get_args():
            name = result.get_args()["character_name"]
            map = self._mapper.get_map_by_character_name(name)
            
            if map is not None:
                return super().answer_is_valid(result)
        
        return False
    
class ClientMessageChooseCardToPlay(ClientMessage):
    def __init__(self, card: LoveLetterCard, drawn_card: LoveLetterCard):
        super().__init__(LOVE_LETTER_MESSAGE_CHOOSE_CARD_TO_PLAY, {
            'card'       : card.get_character().get_name(),
            'drawn_card' : drawn_card.get_character().get_name()
        })
    
    def answer_is_valid(self, result: ClientResult) -> bool:
        if "card" in result.get_args():
            if result.get_args()["card"] in ("hand_card", "drawn_card"):
                return super().answer_is_valid(result)
        
        return False

class ClientMessageCompareCards(ClientMessage):
    def __init__(self, player: LoveLetterPlayer, target: LoveLetterPlayer, reason: ClientReason):
        super().__init__(LOVE_LETTER_MESSAGE_COMPARE, {
            'player' : player.get_id(),
            'player_card' : player.get_card().get_character().get_name(),
            'target' : target.get_id(),
            'target_card' : target.get_card().get_character().get_name(),
            'reason'  : reason.toJson()
        })
    

class ClientMessageDisplayUnsafeMessage(ClientMessage):
    def __init__(self, reason: ClientReason):
        super().__init__(LOVE_LETTER_MESSAGE_DISPLAY_UNSAFE, {
            'reason'    : reason.toJson()
        })

class ClientMessageConfirmUnsafeMessage(ClientMessage):
    def __init__(self, reason: ClientReason):
        super().__init__(LOVE_LETTER_MESSAGE_CONFIRM_UNSAFE, {
            'reason'    : reason.toJson()
        })


