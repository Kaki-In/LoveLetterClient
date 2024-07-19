from .graphics import *

import events as _events

class GraphicLayer():
    def __init__(self, resources: Resources):
        super().__init__()
        
        self._resources = resources

        self._events = _events.EventObject()
    
    def get_events(self) -> _events.EventObject:
        return self._events
        
    def set_resources(self, resources: Resources) -> None:
        self._resources = resources
    
    def get_resources(self) -> Resources:
        return self._resources
    
    def background_variant(self) -> str:
        return ""
    
    def get_items(self) -> list[ GameDisplayedElement ]:
        return []
    
    def set_rect(self, x: int, y: int, w: int, h: int) -> None:
        pass
    
