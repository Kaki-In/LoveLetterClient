from .ui import *
from .settings import *
from .controller import *

from PyQt5 import QtWidgets as _QtWidgets, QtGui as _QtGui
APP = _QtWidgets.QApplication([''])

class MainActivity():
    def __init__(self):
        self._window = GameWidget()
        self._activity = ActivityContext()
        self._settings = MainSettings()
        self._apps_controller = ActivityAppsController(self._activity, self._window, self._settings)

        self._ui_controller = UiController(self._window, self._settings)
    
    def main(self):
        APP.exec()
    


