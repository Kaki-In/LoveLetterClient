from ..objects import *
from .message import *
from .result import *

import typing as _T

def _abstract_async_method(f):
    async def raiseNotImplemented(*a, **b) -> _T.Any:
        raise NotImplementedError("This class is only abstract. Please use your own client")
    
    return raiseNotImplemented

class LoveLetterClient():
    def __init__(self):
        pass
    
    @_abstract_async_method
    async def send_message(self, message: ClientMessage) -> None:
        pass
    
    @_abstract_async_method
    async def interact(self, message: ClientMessage) -> ClientResult:
        return ClientResult("", {})
    
