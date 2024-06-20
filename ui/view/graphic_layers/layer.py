from .graphics import *

from PyQt5 import QtCore as _QtCore

class GraphicLayer(_QtCore.QObject):
    def __init__(self):
        super().__init__()
    
    def get_items(self) -> list[ GameDisplayedElement ]:
        return []
    
    def set_rect(self, x: int, y: int, w: int, h: int) -> None:
        pass
    
