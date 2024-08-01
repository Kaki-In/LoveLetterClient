import events as _events

class LocalUser():
    def __init__(self, name: str) -> None:
        self._name = name

        self._events = _events.EventObject(
            'name_changed'
        )
    
    def get_events(self) -> _events.EventObject:
        return self._events
    
    def get_name(self) -> str:
        return self._name
    
    def set_name(self, name: str) -> None:
        self._name = name
        self._events['name_changed'].emit(name)
