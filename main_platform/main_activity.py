from .ui import *
from .objects.settings import *

from PyQt5 import QtWidgets as _QtWidgets, QtGui as _QtGui
APP = _QtWidgets.QApplication([''])

class MainActivity():
    def __init__(self):
        self._window = GameWidget()
        self._thread = MenusThread()

        self._settings = MainSettings()
        self._controller = MenusController(self._thread, self._window, self._settings)
    
    def main(self):
        self._thread.start()
        APP.exec()
    


