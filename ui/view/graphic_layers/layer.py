from .graphics import *

from PyQt5 import QtCore as _QtCore

class GraphicLayer(_QtCore.QObject):
    def __init__(self):
        super().__init__()
        
        self._dark_mode = False
    
    def set_dark_mode(self, enabled: bool) -> None:
        self._dark_mode = enabled
        for item in self.get_items():
            item.set_dark_mode(enabled)
    
    def dark_mode_enabled(self) -> bool:
        return self._dark_mode
    
    def get_items(self) -> list[ GameDisplayedElement ]:
        return []
    
    def set_rect(self, x: int, y: int, w: int, h: int) -> None:
        pass
    
