from .event import *

import typing as _T
import asyncio as _asyncio

_KeyType = _T.TypeVar('_KeyType')

class EventObject(_T.Generic[_KeyType]):
    def __init__(self, *events_names: _KeyType):
        self.__events: dict[_KeyType, EventHandler] = {}
        
        for name in events_names:
            self.__events[ name ] = EventHandler()
    
    def addEventListener(self, name: _KeyType, function: _T.Callable | _T.Awaitable ) -> None:
        self.__events[ name ].addEventFunction(function)
    
    def getEvent(self, name: _KeyType) -> EventHandler:
        return self.__events[ name ]
    
    def create_event(self, name: str) -> None:
        self.__events[name] = EventHandler()
    
    def create_events(self, *names) -> None:
        for name in names:
            self.create_event(name)
    
    def __getitem__(self, name: _KeyType) -> EventHandler:
        return self.getEvent(name)
    
    def __iter__(self) -> _T.Iterator:
        return iter(self.__events)
    

