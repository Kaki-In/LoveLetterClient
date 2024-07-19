from .menu import *

class FirstMenu(Menu):
    def __init__(self):
        super().__init__()
        self._name: str = ""
    
    def is_valid(self) -> bool:
        return bool(self._name)
    
    def get_name(self) -> str:
        return self._name
    
    def set_name(self, name: str) -> None:
        self._name = name


