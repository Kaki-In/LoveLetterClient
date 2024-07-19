from threading import Thread
from PyQt5 import QtCore as _QtCore
import typing as _T

class Event():
    def __init__(self, *values):
        self._values = values
    
    def values(self) -> tuple[_T.Any, ...]:
        return self._values

class EventHandler(_QtCore.QObject):
    _signal = _QtCore.pyqtSignal(Event)

    def __init__(self):
        super().__init__()

        self._functions = []
    
    def addEventFunction(self, func):
        self._signal.connect(func)
    
    def removeEventFunction(self, func):
        self._signal.disconnect(func)
 
    def emit(self, *values):
        self._signal.emit(Event(*values))

