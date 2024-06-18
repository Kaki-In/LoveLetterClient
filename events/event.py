from threading import Thread

class EventHandler():
    def __init__(self):
        self._functions = []
    
    def addEventFunction(self, func):
        self._functions.append(func)
    
    def emit(self, *values):
        for func in self._functions:
            Thread(target = func, args = values).start()
