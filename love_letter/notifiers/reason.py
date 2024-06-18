import typing as _T

class ClientReason():
    def __init__(self, name: str, args: dict[str, _T.Any]):
        self._name = name
        self._args = args
    
    def toJson(self) -> dict[str, _T.Any]:
        return {
            "name": self._name,
            "args": self._args
        }
    
    def name(self) -> str:
        return self._name
    
    def args(self) -> dict[str, _T.Any]:
        return self._args
    
