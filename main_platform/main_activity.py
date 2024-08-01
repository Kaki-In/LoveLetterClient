from .ui import *
from .settings import *
from .controller import *

from PyQt5 import QtWidgets as _QtWidgets, QtGui as _QtGui
APP = _QtWidgets.QApplication([''])

class MainActivity():
    def __init__(self):
        self._window = GameWidget()

        self._thread = MenusThread()

        self._settings = MainSettings()
        self._menus_controller = MenusController(self._thread, self._window, self._settings)

        self._ui_controller = UiController(self._window, self._settings)
    
    def main(self):
        self._thread.start()
        APP.exec()
    


