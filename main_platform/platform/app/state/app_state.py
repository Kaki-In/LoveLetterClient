import events as _events

class ApplicationState():
    def __init__(self):
        self._events = _events.EventObject(
            'update'
        )
    
    def get_events(self) -> _events.EventObject:
        return self._events

