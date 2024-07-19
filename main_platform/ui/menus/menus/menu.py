import events as _events

class Menu():
    def __init__(self):
        self._events = _events.EventObject()
    
    def get_events(self) -> _events.EventObject:
        return self._events
